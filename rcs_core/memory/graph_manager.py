"""
Module: graph_manager.py
Project: RCS-Nexus
Description: Semantic graph manager for memory clustering and relationship persistence.
"""


class GraphManager:
    def __init__(self):
        self.nodes = {}

    def add_relation(self, source, target, relation_type, weight=1):
        key = (source, target, relation_type)
        if key not in self.nodes:
            self.nodes[key] = {
                "source": source,
                "target": target,
                "relation_type": relation_type,
                "weight": 0,
            }
        self.nodes[key]["weight"] += weight

    def summarize(self):
        return list(self.nodes.values())
