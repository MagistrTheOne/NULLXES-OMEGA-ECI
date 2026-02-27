"""Memory plane contracts with episodic/semantic separation."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class MemoryType(str, Enum):
    EPISODIC = "episodic"
    SEMANTIC = "semantic"


class MemoryWriteIntent(BaseModel):
    session_id: str = Field(min_length=1)
    memory_type: MemoryType
    content: dict[str, Any] = Field(default_factory=dict)
    priority: float = Field(ge=0.0, le=1.0, default=0.5)


class MemoryReadQuery(BaseModel):
    session_id: str = Field(min_length=1)
    memory_type: MemoryType
    query: str = Field(min_length=1)
    max_items: int = Field(ge=1, le=128, default=10)


class MemoryItem(BaseModel):
    item_id: str = Field(min_length=1)
    memory_type: MemoryType
    payload: dict[str, Any] = Field(default_factory=dict)
    relevance: float = Field(ge=0.0, le=1.0)
    freshness_hours: float = Field(ge=0.0)

