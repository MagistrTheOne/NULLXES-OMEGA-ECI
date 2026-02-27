# Benchmark and Risk Program

## Benchmark objective

Target approximately `85%` aggregate score on controlled AGI-equivalent benchmark tracks:

- abstract reasoning
- coding
- planning
- multimodal grounding
- adaptive transfer

## Metric families

- Task success rate
- Calibration quality (confidence vs correctness)
- Tool-call reliability
- Long-horizon completion rate
- Cross-modal grounding accuracy
- Latency budgets for embodied path

## Core risks and mitigations

1. Router collapse or expert imbalance
   - Mitigation: routing load constraints and expert utilization regularization.
2. Modality interference
   - Mitigation: staged curriculum and controlled modality sampling.
3. Long-context quality degradation
   - Mitigation: retrieval-grounded memory and long-context-specific post-training.
4. Tool misuse and plan instability
   - Mitigation: typed planning schema, verifier checks, rollback rules.
5. Sim-to-real embodiment gap
   - Mitigation: domain randomization and conservative fallback controllers.
6. MoE communication overhead
   - Mitigation: topology-aware expert placement and routing locality bias.

## Release gate template

Checkpoint promotion requires:

- benchmark threshold pass
- no critical safety regression
- reproducible training metadata
- rollback checkpoint availability

