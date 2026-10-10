"""
Module: buffer_cleaner.py
Project: RCS-Nexus
Description: Memory buffer cleaner and defragmentation routine for long-running cognitive loops.
"""


class BufferCleaner:
    def __init__(self):
        pass

    def compact(self, execution_buffer):
        compacted = []
        seen = set()

        for item in execution_buffer:
            identity = (item.get("source"), item.get("target"), item.get("relation_type"))
            if identity in seen:
                continue
            seen.add(identity)
            compacted.append(item)

        return compacted
