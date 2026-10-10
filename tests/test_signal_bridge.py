from rcs_core.translators.signal_bridge import SignalBridge


def test_validate_and_transform_success():
    bridge = SignalBridge()
    raw = {
        "source": "temporal_agent",
        "target": "checkpoint_1",
        "relation_type": "time_anchor",
        "timestamp": 123,
        "payload": {"label": "checkpoint_1"},
    }

    result = bridge.validate_and_transform(raw)
    assert result["source"] == "temporal_agent"
    assert result["target"] == "checkpoint_1"
    assert result["relation_type"] == "time_anchor"
