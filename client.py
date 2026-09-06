import difflib
from typing import Dict, Any, List, Optional

class VisionWebActionBoundingBoxGrounder:
    """
    Matches natural language action descriptions to the closest matching visual/DOM target
    and calculates click centers and safe interaction offsets.
    """
    def ground_action_target(
        self,
        instruction: str,
        candidates: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        low_inst = instruction.lower().strip()
        best_candidate: Optional[Dict[str, Any]] = None
        best_score = 0.0
        match_type = "none"

        for cand in candidates:
            label = cand.get("label", "").lower().strip()
            role = cand.get("role", "").lower().strip()
            combined = f"{role} {label}"

            # 1. Exact Substring Match
            if label and label in low_inst:
                score = 0.95
                if score > best_score:
                    best_score = score
                    best_candidate = cand
                    match_type = "exact_substring"
            # 2. Fuzzy Match
            else:
                sim = difflib.SequenceMatcher(None, low_inst, combined).ratio()
                if sim > best_score and sim >= 0.45:
                    best_score = sim
                    best_candidate = cand
                    match_type = "fuzzy_semantic"

        if not best_candidate and candidates:
            best_candidate = candidates[0]
            best_score = 0.3
            match_type = "fallback_first"

        # Calculate click coordinate center
        bbox = best_candidate.get("bbox", {"x": 0, "y": 0, "w": 0, "h": 0}) if best_candidate else {}
        center_x = round(bbox.get("x", 0) + bbox.get("w", 0) / 2.0, 1)
        center_y = round(bbox.get("y", 0) + bbox.get("h", 0) / 2.0, 1)

        return {
            "instruction": instruction,
            "target_id": best_candidate.get("id") if best_candidate else None,
            "target_label": best_candidate.get("label") if best_candidate else None,
            "match_confidence": round(best_score, 3),
            "match_type": match_type,
            "click_coordinates": {"x": center_x, "y": center_y},
            "bounding_box": bbox
        }
