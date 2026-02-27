"""Structured planning contracts emitted by the cognitive core."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from .types import ConfidenceScore


class PlanStep(BaseModel):
    step_id: str = Field(min_length=1)
    description: str = Field(min_length=1)
    required_tools: list[str] = Field(default_factory=list)
    expected_observation: str = Field(min_length=1)
    timeout_seconds: int = Field(ge=1, default=60)


class PlanPacket(BaseModel):
    plan_id: str = Field(min_length=1)
    objective: str = Field(min_length=1)
    constraints: list[str] = Field(default_factory=list)
    steps: list[PlanStep] = Field(min_length=1)
    termination_conditions: list[str] = Field(min_length=1)
    confidence: ConfidenceScore
    metadata: dict[str, Any] = Field(default_factory=dict)

