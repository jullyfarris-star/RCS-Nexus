import logging
import tiktoken
import networkx as nx
from typing import Dict, List, Any, Tuple

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("RCS-Nexus.BufferCleaner")

class ContextBufferCleaner:
    def __init__(self, target_model: str = "gpt-4", token_threshold: int = 2048):
        self.encoder = tiktoken.encoding_for_model(target_model)
        self.token_threshold = token_threshold
        
    def calculate_token_weight(self, text_stream: str) -> int:
        return len(self.encoder.encode(text_stream))

    def analyze_and_cluster(self, short_term_buffer: List[Dict[str, Any]]) -> nx.Graph:
        graph = nx.Graph()
        for entry in short_term_buffer:
            payload = entry.get("payload", {})
            source = payload.get("source")
            target = payload.get("target")
            relation = payload.get("relation_type", "associated_with")
            weight = payload.get("weight", 1.0)
            
            if source and target:
                if graph.has_edge(source, target):
                    graph[source][target]['weight'] += weight
                else:
                    graph.add_edge(source, target, relation=relation, weight=weight)
        return graph

    def compress_relations(self, memory_graph: nx.Graph, importance_floor: float = 1.5) -> List[Dict[str, Any]]:
        compressed_knowledge = []
        for source, target, data in memory_graph.edges(data=True):
            if data.get('weight', 0.0) >= importance_floor:
                compressed_knowledge.append({
                    "source": source,
                    "target": target,
                    "relation_type": data.get("relation"),
                    "consolidated_weight": data.get("weight")
                })
        return compressed_knowledge

    def execute_sleep_cycle(self, short_term_buffer: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], str]:
        logger.info("Initiating system sleep cycle...")
        if not short_term_buffer:
            return [], "Buffer empty."
        
        temporary_graph = self.analyze_and_cluster(short_term_buffer)
        consolidated_facts = self.compress_relations(temporary_graph)
        abstract_schema_summary = f"Compressed {temporary_graph.number_of_edges()} edges down to {len(consolidated_facts)} nodes."
        
        short_term_buffer.clear()
        return consolidated_facts, abstract_schema_summary
