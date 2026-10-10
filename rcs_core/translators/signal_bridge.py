"""
Module: signal_bridge.py
Project: RCS-Nexus
Description: Structural validation and translation layer for converting raw telemetry into normalized signal objects.
"""


class SignalBridge:
    def validate_and_transform(self, raw_signal):
        if not isinstance(raw_signal, dict):
            return None

        required = {"source", "target", "relation_type"}
        if not required.issubset(raw_signal.keys()):
            return None

        return {
            "source": raw_signal["source"],
            "target": raw_signal["target"],
            "relation_type": raw_signal["relation_type"],
            "timestamp": raw_signal.get("timestamp"),
            "epoch": raw_signal.get("epoch"),
            "payload": raw_signal.get("payload", {}),
        }
