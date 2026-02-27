"""MoE routing contracts for hierarchical expert selection."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class RouterInput(BaseModel):
    sequence_id: str = Field(min_length=1)
    token_index: int = Field(ge=0)
    segment_label: str = Field(min_length=1)
    hidden_state_norm: float = Field(ge=0.0)


class RouterDecision(BaseModel):
    route_mode: Literal["hierarchical_hybrid"]
    selected_expert_ids: list[int] = Field(min_length=1)
    shared_expert_ids: list[int] = Field(default_factory=list)
    gate_probabilities: list[float] = Field(min_length=1)
    overflowed: bool = False


class RouterStats(BaseModel):
    aux_load_loss: float = Field(ge=0.0)
    expert_utilization_entropy: float = Field(ge=0.0)
    dropped_token_count: int = Field(ge=0)

