"""Tool plane contracts for safe and deterministic tool execution."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class ToolCallStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"


class ToolCallRequest(BaseModel):
    call_id: str = Field(min_length=1)
    tool_name: str = Field(min_length=1)
    arguments: dict[str, Any] = Field(default_factory=dict)
    timeout_seconds: int = Field(ge=1, default=30)
    rollback_on_failure: bool = True


class ToolCallResult(BaseModel):
    call_id: str = Field(min_length=1)
    status: ToolCallStatus
    output: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None
    duration_ms: int = Field(ge=0, default=0)

