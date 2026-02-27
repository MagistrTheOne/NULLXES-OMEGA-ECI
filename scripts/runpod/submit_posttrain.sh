#!/usr/bin/env bash
set -euo pipefail

# Template script: run on RunPod worker only.

export CONFIG_PATH="${CONFIG_PATH:-configs/training/runpod_posttrain.yaml}"
export MODEL_CONFIG_PATH="${MODEL_CONFIG_PATH:-configs/model/eci_moe_220b.yaml}"
export CLUSTER_CONFIG_PATH="${CLUSTER_CONFIG_PATH:-configs/infra/runpod_cluster_template.yaml}"

echo "[posttrain] config: ${CONFIG_PATH}"
echo "[posttrain] model: ${MODEL_CONFIG_PATH}"
echo "[posttrain] cluster: ${CLUSTER_CONFIG_PATH}"

echo "Replace this section with your post-training launch command."
echo "Example: torchrun --nproc_per_node=8 posttrain.py --config ${CONFIG_PATH}"

