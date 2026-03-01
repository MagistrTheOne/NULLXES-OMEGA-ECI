#!/usr/bin/env bash
set -euo pipefail

# Run on RunPod worker.
# Requires: huggingface_hub, pyyaml

ROOT_DIR="${ROOT_DIR:-/workspace/data/omega_mid}"
REGISTRY="${REGISTRY:-configs/data/dataset_registry.yaml}"
HF_TOKEN="${HF_TOKEN:-}"

if [[ -z "${HF_TOKEN}" ]]; then
  echo "HF_TOKEN is empty. Set HF_TOKEN in RunPod secrets."
  exit 1
fi

mkdir -p "${ROOT_DIR}"

python - <<'PY'
import os
from pathlib import Path
import yaml
from huggingface_hub import snapshot_download

root = Path(os.environ.get("ROOT_DIR", "/workspace/data/omega_mid"))
registry = Path(os.environ.get("REGISTRY", "configs/data/dataset_registry.yaml"))

data = yaml.safe_load(registry.read_text(encoding="utf-8"))
for item in data.get("sources", []):
    status = item.get("status", "")
    if status not in {"use", "use_sample_only"}:
        continue
    repo = item["repo"]
    repo_type = item.get("repo_type", "dataset")
    local_dir = root / repo.replace("/", "__")
    local_dir.mkdir(parents=True, exist_ok=True)
    print(f"[download] {repo} -> {local_dir}")
    snapshot_download(
        repo_id=repo,
        repo_type=repo_type,
        local_dir=str(local_dir),
        local_dir_use_symlinks=False,
        resume_download=True,
    )

print("Done")
PY
