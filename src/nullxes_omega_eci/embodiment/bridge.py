"""Embodiment bridge skeleton for plan-level control handoff."""

from __future__ import annotations

from nullxes_omega_eci.contracts.embodiment import EmbodimentBridgeMessage, MotorCommandEnvelope


class EmbodimentBridge:
    def to_motor_commands(self, message: EmbodimentBridgeMessage) -> list[MotorCommandEnvelope]:
        commands: list[MotorCommandEnvelope] = []
        for step in message.plan.steps:
            commands.append(
                MotorCommandEnvelope(
                    command_id=f"{message.plan.plan_id}:{step.step_id}",
                    robot_id=message.robot_state.robot_id,
                    source_plan_id=message.plan.plan_id,
                    action_type="execute_step",
                    parameters={"description": step.description},
                    hard_safety_constraints=message.plan.constraints,
                )
            )
        return commands

