"""Memory manager skeleton with episodic and semantic separation."""

from __future__ import annotations

from collections import defaultdict

from nullxes_omega_eci.contracts.memory import MemoryItem, MemoryReadQuery, MemoryWriteIntent


class MemoryManager:
    def __init__(self) -> None:
        self._storage: dict[str, list[MemoryItem]] = defaultdict(list)

    def write(self, intent: MemoryWriteIntent) -> str:
        item_id = f"{intent.session_id}:{intent.memory_type.value}:{len(self._storage[intent.session_id])}"
        item = MemoryItem(
            item_id=item_id,
            memory_type=intent.memory_type,
            payload=intent.content,
            relevance=intent.priority,
            freshness_hours=0.0,
        )
        self._storage[intent.session_id].append(item)
        return item_id

    def read(self, query: MemoryReadQuery) -> list[MemoryItem]:
        items = [
            item
            for item in self._storage.get(query.session_id, [])
            if item.memory_type == query.memory_type
        ]
        return items[: query.max_items]

