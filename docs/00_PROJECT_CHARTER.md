# Project Charter

Project: `NULLXES OMEGA ECI`  
Company: `NULLXES LLC`

## Mission

Build an Embodied Multimodal Cognitive Intelligence architecture with sparse MoE scaling that targets:

- Strong multi-step reasoning.
- Advanced coding and planning.
- Long-horizon multimodal task execution.
- Embodied deployment via a clean cognition-to-motor abstraction layer.

## Program boundaries

- This repository is for architecture, contracts, and documentation.
- No local training and no local heavy inference.
- Weight training, checkpoints, and optimization runs happen on RunPod.

## Technical target envelope

- Total parameters: ~`220B`.
- Experts: `144`.
- Active experts per token: `14` (12 routed + 2 shared).
- Layers: `56`.
- Hidden size: `7168`.
- Expert FFN size: `28672`.
- Native context: `128K`.
- Post-training target context: `1M+`.

## Hardware target

- Primary: `B200` clusters for high-throughput sparse training.
- Secondary: `H200` clusters for compatibility, long-context and post-training passes.

## Success definition

Reach approximately `85%` on controlled AGI-equivalent benchmark suites spanning:

- abstract reasoning
- coding
- planning
- multimodal grounding
- adaptive task transfer

