import json
from client import VisionWebActionBoundingBoxGrounder

def main():
    grounder = VisionWebActionBoundingBoxGrounder()
    instruction = "Click on the primary Submit Order button"
    candidates = [
        {"id": "el_01", "label": "Cancel", "role": "button", "bbox": {"x": 100, "y": 400, "w": 80, "h": 36}},
        {"id": "el_02", "label": "Submit Order", "role": "button", "bbox": {"x": 200, "y": 400, "w": 120, "h": 36}},
        {"id": "el_03", "label": "Apply Coupon", "role": "button", "bbox": {"x": 350, "y": 400, "w": 100, "h": 36}}
    ]
    result = grounder.ground_action_target(instruction, candidates)
    print("Action Grounding Result:")
    print(json.dumps(result, indent=2))
    assert result["target_id"] == "el_02"
    assert result["click_coordinates"]["x"] == 260.0
    assert result["click_coordinates"]["y"] == 418.0
    print("Action grounder verification: PASS")

if __name__ == "__main__":
    main()
