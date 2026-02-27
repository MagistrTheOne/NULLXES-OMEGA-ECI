# RunPod Operations

This project uses RunPod for all training and weight updates.

## Local policy

- Local machines are used for:
  - code changes
  - config authoring
  - documentation
- Local machines are not used for:
  - pretraining
  - post-training
  - checkpoint optimization passes

## Remote execution flow

1. Build or select container image for CUDA/NCCL/TE stack.
2. Mount remote storage for datasets and checkpoints.
3. Upload or sync code snapshot from this repository.
4. Launch stage-specific training job with immutable config.
5. Stream logs and metrics to tracking backend.
6. Save checkpoints with signed metadata.
7. Validate model quality gates before promoting checkpoint.

## Hardware profiles

- B200 profile:
  - primary sparse pretraining and high-throughput MoE runs
- H200 profile:
  - compatibility runs, long-context passes, and post-training refinement

## Checkpoint policy

- Save full checkpoint at fixed global-step intervals.
- Save optimizer state at lower cadence when cost is high.
- Keep immutable manifest:
  - git commit hash
  - config hash
  - data snapshot ID
  - trainer version

## Failure and resume policy

- On worker preemption:
  - restart from last verified checkpoint
  - verify optimizer state compatibility
- On data mount issues:
  - fail fast and avoid partial writes
- On divergence:
  - roll back to previous stable checkpoint and lower learning rate schedule

## Security notes

- Never commit secrets in repository.
- Use RunPod secrets/variables for keys and endpoints.
- Restrict storage credentials to least privilege.

