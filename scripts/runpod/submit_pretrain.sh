#!/usr/bin/env bash
set -euo pipefail

# Template script: run on RunPod worker only.

export CONFIG_PATH="${CONFIG_PATH:-configs/training/runpod_pretrain.yaml}"
export MODEL_CONFIG_PATH="${MODEL_CONFIG_PATH:-configs/model/eci_moe_220b.yaml}"
export CLUSTER_CONFIG_PATH="${CLUSTER_CONFIG_PATH:-configs/infra/runpod_cluster_template.yaml}"

echo "[pretrain] config: ${CONFIG_PATH}"
echo "[pretrain] model: ${MODEL_CONFIG_PATH}"
echo "[pretrain] cluster: ${CLUSTER_CONFIG_PATH}"

echo "Replace this section with your trainer launch command."
echo "Example: torchrun --nproc_per_node=8 train.py --config ${CONFIG_PATH}"

