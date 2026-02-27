"""Reference skeleton for hierarchical MoE routing behavior."""

from __future__ import annotations

from dataclasses import dataclass

from nullxes_omega_eci.contracts.router import RouterDecision, RouterInput


@dataclass
class HierarchicalRouterConfig:
    total_experts: int = 144
    routed_top_k: int = 12
    shared_top_k: int = 2


class HierarchicalRouter:
    """Contract-level router skeleton.

    This file intentionally avoids heavy runtime dependencies. The actual
    runtime kernel should be implemented inside the training stack.
    """

    def __init__(self, config: HierarchicalRouterConfig) -> None:
        self.config = config

    def route(self, payload: RouterInput) -> RouterDecision:
        # Placeholder strategy for interface completeness.
        # Runtime implementation should inject learned gating logic.
        selected = list(range(self.config.routed_top_k))
        shared = list(range(self.config.shared_top_k))
        probs = [1.0 / len(selected)] * len(selected)
        return RouterDecision(
            route_mode="hierarchical_hybrid",
            selected_expert_ids=selected,
            shared_expert_ids=shared,
            gate_probabilities=probs,
            overflowed=False,
        )

