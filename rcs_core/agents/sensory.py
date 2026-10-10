"""
Module: sensory.py
Project: RCS-Nexus
Description: Sensory input normalization and telemetry capture layer.
"""


class SensoryAgent:
    def capture(self, raw_payload):
        return {
            "source": "sensory_agent",
            "target": "raw_stream",
            "relation_type": "telemetry_ingest",
            "payload": raw_payload,
        }
