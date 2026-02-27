# NULLXES OMEGA ECI

Owner: `NULLXES LLC`

This repository is the architecture and documentation workspace for an Embodied Multimodal Cognitive Intelligence (ECI) program based on a sparse Mixture-of-Experts (MoE) backbone.

## Operating constraints

- Local machine: documentation and code structure only.
- Training and weight updates: RunPod workers only.
- Target hardware profile: NVIDIA `H200` and `B200` class clusters.
- No local launch of training or large-scale inference pipelines.

## Primary objective

Define and implement a system blueprint that can exceed GPT-4-class reasoning and Grok-style MoE capability while preserving low-latency deployment paths for embodied robotics.

## Repository map

- `docs/`: architecture, stages, library stack, runbook, and risk controls.
- `configs/`: model/training/infra/evaluation/policy configs.
- `src/`: typed contracts and interface skeletons for cognitive, memory, tool, and embodiment planes.
- `scripts/runpod/`: remote-only job templates and operational helpers.

## Contributor workflow

1. Read `docs/00_PROJECT_CHARTER.md`.
2. Execute work in stage order from `docs/01_IMPLEMENTATION_STAGES.md`.
3. Keep all interfaces aligned with `configs/model/eci_moe_220b.yaml`.
4. Use `docs/04_RUNPOD_OPERATIONS.md` for remote execution.

