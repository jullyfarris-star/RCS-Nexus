import math
from typing import Dict, Any, Tuple

class SpatialAgent:
    def __init__(self, agent_id: str = "agent_spatial_01"):
        self.agent_id = agent_id

    def calculate_distance(self, pos1: Tuple[float, float], pos2: Tuple[float, float]) -> float:
        return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

    def generate_spatial_signal(self, node_id: str, coordinates: Tuple[float, float], target_hub: str = "sector_delta") -> Dict[str, Any]:
        distance_to_center = self.calculate_distance(coordinates, (0.0, 0.0))
        calculated_weight = max(0.5, round(5.0 / (distance_to_center + 1.0), 2))
        return {
            "vector_type": "spatial_node",
            "payload": {
                "source": f"entity_{node_id}",
                "target": target_hub,
                "relation_type": "spatial_proximity",
                "weight": calculated_weight,
                "meta": {"coordinates_xy": coordinates}
            }
        }
