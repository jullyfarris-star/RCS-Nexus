"""
Module: orchestrator.py
Project: RCS-Nexus
Description: Central system orchestrator coordinating signal intake,
             buffering, sleep cycle defragmentation, and memory consolidation.
"""

import asyncio
import logging
from collections import deque

logger = logging.getLogger("RCS-Nexus.Orchestrator")


class NexusOrchestrator:
    def __init__(self, token_threshold=700, check_interval_seconds=2):
        self.token_threshold = token_threshold
        self.check_interval_seconds = check_interval_seconds
        self.execution_buffer = deque(maxlen=200)
        self.long_term_knowledge_base = []
        self.running = False
        self._monitor_task = None

    async def start(self):
        if self.running:
            return
        self.running = True
        self._monitor_task = asyncio.create_task(self._monitor_loop())

    async def stop(self):
        self.running = False
        if self._monitor_task:
            self._monitor_task.cancel()
            try:
                await self._monitor_task
            except asyncio.CancelledError:
                pass
        await self.trigger_sleep_cycle()

    async def ingest_signal(self, signal):
        if not signal:
            return
        self.execution_buffer.append(signal)
        logger.info("Received signal for orchestration: %s", signal)

    async def _monitor_loop(self):
        while self.running:
            await asyncio.sleep(self.check_interval_seconds)
            current_token_count = self._estimate_buffer_tokens()
            if current_token_count >= self.token_threshold:
                logger.warning(
                    "Token threshold reached (%s >= %s). Triggering sleep cycle.",
                    current_token_count,
                    self.token_threshold,
                )
                await self.trigger_sleep_cycle()

    def _estimate_buffer_tokens(self):
        total = 0
        for item in self.execution_buffer:
            total += len(str(item).split())
        return total

    async def trigger_sleep_cycle(self):
        logger.info("Executing defragmentation sleep cycle...")

        if not self.execution_buffer:
            logger.info("Buffer empty; no memory consolidation required.")
            return

        memory_clusters = {}
        for item in self.execution_buffer:
            source = item.get("source", "unknown")
            target = item.get("target", "unknown")
            relation = item.get("relation_type", "context")

            key = (source, target, relation)
            current = memory_clusters.get(key, {"consolidated_weight": 0})
            current["source"] = source
            current["target"] = target
            current["relation_type"] = relation
            current["consolidated_weight"] = current["consolidated_weight"] + 1
            memory_clusters[key] = current

        for node in memory_clusters.values():
            self.long_term_knowledge_base.append(node)

        self.execution_buffer.clear()
        logger.info("Sleep cycle complete. Execution buffer flushed and knowledge graph compacted.")
