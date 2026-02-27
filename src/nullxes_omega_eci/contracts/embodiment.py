"""Embodiment bridge contracts between cognition and motor layers."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from .planning import PlanPacket


class RobotState(BaseModel):
    robot_id: str = Field(min_length=1)
    timestamp_ms: int = Field(ge=0)
    state_vector: list[float] = Field(default_factory=list)
    sensors: dict[str, Any] = Field(default_factory=dict)


class MotorCommandEnvelope(BaseModel):
    command_id: str = Field(min_length=1)
    robot_id: str = Field(min_length=1)
    source_plan_id: str = Field(min_length=1)
    action_type: str = Field(min_length=1)
    parameters: dict[str, Any] = Field(default_factory=dict)
    hard_safety_constraints: list[str] = Field(default_factory=list)


class EmbodimentBridgeMessage(BaseModel):
    plan: PlanPacket
    robot_state: RobotState
    control_horizon_seconds: float = Field(ge=0.01, default=1.0)

