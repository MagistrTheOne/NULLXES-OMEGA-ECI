# Library Stack

This stack is selected for sparse large-scale training on `B200/H200` and low-latency inference paths for embodied deployment.

## Core language and packaging

- Python `3.11`
- `pyproject.toml` with explicit pinned ranges
- `pydantic` for strict config and payload contracts

## Model and training runtime

- `PyTorch` for core framework
- `NVIDIA Transformer Engine` for BF16/FP8 efficiency
- `Megatron-Core` (or Megatron-LM integration) for TP/PP/EP/CP scale
- `NCCL` and CUDA runtime for distributed collectives
- `FlashAttention-2` for efficient attention kernels

## Sparse MoE and routing

- Megatron MoE primitives for expert parallelism
- Custom hierarchical router module in project code
- Optional fallback experiments with `DeepSpeed-MoE` for A/B comparisons

## Data and preprocessing

- `WebDataset` for large streaming shards
- `datasets` for dataset curation workflows
- `Apache Arrow` / Parquet-backed metadata tables
- `sentencepiece` or equivalent tokenizer tooling

## Evaluation and benchmark harness

- `lm-eval` style harness integration for text/reasoning tasks
- `bigcode-eval` style coding evaluation integration
- Internal multimodal and planning benchmarks (project-defined)
- `pytest` for interface and contract validation

## Inference and serving

- `vLLM` for high-throughput serving experiments
- `TensorRT-LLM` for latency-critical optimized deployment
- `FastAPI` for control plane and typed RPC endpoints

## Embodiment and robotics integration

- `ROS 2` for robotics messaging and deployment integration
- `Isaac Lab` and/or `MuJoCo` for simulation workflows
- Optional skill-policy frameworks via PyTorch policy heads

## Orchestration and observability

- `Hydra` for experiment composition
- `Weights & Biases` or `MLflow` for experiment tracking
- `Prometheus` + `Grafana` for infra metrics

## Security and compliance helpers

- `detect-secrets` for leak prevention in CI
- Artifact signing and checksum validation in checkpoint workflow

## Selection policy

- Default stack should remain minimal and battle-tested.
- Any new library must include:
  - explicit reason for adoption
  - operational cost estimate
  - rollback strategy

