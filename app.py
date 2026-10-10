"""
Module: app.py
Project: RCS-Nexus
Description: Main deployment and execution script. Mounts the orchestrator,
             initiates asynchronous agent routines, routes validated impulses,
             and triggers context defragmentation.
"""

import asyncio
import logging
import random

from rcs_core.orchestrator import NexusOrchestrator
from rcs_core.translators.signal_bridge import SignalBridge
from rcs_core.agents.temporal import TemporalAgent
from rcs_core.agents.spatial import SpatialAgent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(name)s] - %(levelname)s - %(message)s"
)
logger = logging.getLogger("RCS-Nexus.MainApp")


async def run_system_simulation():
    logger.info("=========================================================")
    logger.info("STARTING COOPERATIVE AI SUBSYSTEM: RCS-NEXUS ECOSYSTEM")
    logger.info("=========================================================")

    orchestrator = NexusOrchestrator(token_threshold=700, check_interval_seconds=2)
    bridge = SignalBridge()
    agent_time = TemporalAgent()
    agent_space = SpatialAgent()

    await orchestrator.start()
    logger.info("System fully operational. Ingesting continuous multi-agent telemetry streams...")

    try:
        for step in range(1, 7):
            logger.info(f"\n--- System Active Working Cycle: Step {step} ---")

            agent_time.increment_epoch()
            raw_time_signal = agent_time.generate_time_anchor(label=f"routine_checkpoint_{step}")

            mock_coords = (
                round(random.uniform(-5.0, 5.0), 2),
                round(random.uniform(-5.0, 5.0), 2),
            )
            raw_space_signal = agent_space.generate_spatial_signal(
                node_id=f"matrix_node_{step}",
                coordinates=mock_coords,
            )

            validated_time = bridge.validate_and_transform(raw_time_signal)
            validated_space = bridge.validate_and_transform(raw_space_signal)

            if validated_time:
                await orchestrator.ingest_signal(validated_time)
            if validated_space:
                await orchestrator.ingest_signal(validated_space)

            await asyncio.sleep(1.0)

        logger.info("\nSimulation sequence completed. Allowing background monitors to settle...")
        await asyncio.sleep(2.5)

    except KeyboardInterrupt:
        logger.warning("Simulation forcefully interrupted by user.")

    finally:
        logger.info("\n=========================================================")
        await orchestrator.stop()
        logger.info("=========================================================")

        print("\n[FINAL STATE OF LONG-TERM KNOWLEDGE BASE]")
        print(f"Total stable links stored: {len(orchestrator.long_term_knowledge_base)}")
        for idx, node in enumerate(orchestrator.long_term_knowledge_base, 1):
            print(f"  {idx}. [{node['relation_type'].upper()}] {node['source']} ===> {node['target']} (Weight: {node['consolidated_weight']})")


if __name__ == "__main__":
    asyncio.run(run_system_simulation())
