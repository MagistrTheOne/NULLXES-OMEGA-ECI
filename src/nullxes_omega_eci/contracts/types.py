"""Core data contracts shared across system planes."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Modality(str, Enum):
    TEXT = "text"
    CODE = "code"
    VISION = "vision"
    AUDIO = "audio"
    MUSIC_SYMBOLIC = "music_symbolic"
    MUSIC_GENERATIVE = "music_generative"
    TOOL_USE = "tool_use"
    ROBOTICS = "robotics_control_interface"


class ConfidenceScore(BaseModel):
    value: float = Field(ge=0.0, le=1.0)
    calibration_bucket: str = Field(min_length=1)


class ContextPacket(BaseModel):
    session_id: str = Field(min_length=1)
    modality: Modality
    token_count: int = Field(ge=1)
    payload: dict[str, Any] = Field(default_factory=dict)

