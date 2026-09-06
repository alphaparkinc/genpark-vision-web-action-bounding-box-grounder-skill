# GenPark AI Agent Skill - Vision Web Action Bounding Box Grounder

Resolves natural language browser directives to exact spatial (x, y) click targets and bounding boxes.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[Natural Language Browser Command] --> B[Fuzzy & Substring Entity Matcher]
    B --> C[Candidate Element Selector]
    C --> D[Calculate Geometric Center & Margin Offsets]
    D --> E[Precision Coordinates: x, y for Click / Hover Action]
```

## Features
- **Spatial Center Computation**: Converts relative box boundaries to exact mouse cursor targets.
- **Zero External Dependencies**: Pure Python standard library implementation.
