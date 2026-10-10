import asyncio

from rcs_core.orchestrator import NexusOrchestrator


def test_orchestrator_ingest_and_sleep_cycle():
    orchestrator = NexusOrchestrator(token_threshold=1)
    signal = {"source": "x", "target": "y", "relation_type": "link"}

    asyncio.run(orchestrator.ingest_signal(signal))
    assert len(orchestrator.execution_buffer) == 1
