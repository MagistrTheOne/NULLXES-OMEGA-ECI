#!/usr/bin/env bash
set -euo pipefail

# Template script: run on RunPod worker or CI runner with storage access.

export SRC_PATH="${SRC_PATH:-/workspace/checkpoints}"
export DEST_PATH="${DEST_PATH:-s3://replace-bucket/nullxes-omega-eci/checkpoints}"

echo "Sync from ${SRC_PATH} to ${DEST_PATH}"
echo "Replace with your object-storage sync command."
echo "Example: aws s3 sync ${SRC_PATH} ${DEST_PATH} --delete"

