"""
Module: temporal.py
Project: RCS-Nexus
Description: Timeline agent responsible for epoch tracking and timestamped chain anchors.
"""

import time


class TemporalAgent:
    def __init__(self):
        self.epoch = 0

    def increment_epoch(self):
        self.epoch += 1
        return self.epoch

    def generate_time_anchor(self, label="checkpoint"):
        return {
            "source": "temporal_agent",
            "target": label,
            "relation_type": "time_anchor",
            "timestamp": int(time.time()),
            "epoch": self.epoch,
            "payload": {"label": label},
        }
