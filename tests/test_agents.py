from rcs_core.agents.temporal import TemporalAgent
from rcs_core.agents.spatial import SpatialAgent


def test_temporal_agent_epoch():
    agent = TemporalAgent()
    assert agent.increment_epoch() == 1
    assert agent.generate_time_anchor()["epoch"] == 1


def test_spatial_agent_signal():
    agent = SpatialAgent()
    signal = agent.generate_spatial_signal("node_1", (1.2, 3.4))
    assert signal["target"] == "node_1"
    assert signal["payload"]["x"] == 1.2
