param(
  [string]$RootDir = "D:\datasets\omega_mid",
  [string]$Registry = "configs/data/dataset_registry.yaml",
  [string]$HfToken = ""
)

if ([string]::IsNullOrWhiteSpace($HfToken)) {
  Write-Error "HF token required. Pass -HfToken or set secret in environment."
  exit 1
}

$env:HF_TOKEN = $HfToken
New-Item -ItemType Directory -Force -Path $RootDir | Out-Null

$py = @"
import os
from pathlib import Path
import yaml
from huggingface_hub import snapshot_download

root = Path(r'''$RootDir''')
registry = Path(r'''$Registry''')

data = yaml.safe_load(registry.read_text(encoding='utf-8'))
for item in data.get('sources', []):
    status = item.get('status', '')
    if status not in {'use', 'use_sample_only'}:
        continue
    repo = item['repo']
    repo_type = item.get('repo_type', 'dataset')
    local_dir = root / repo.replace('/', '__')
    local_dir.mkdir(parents=True, exist_ok=True)
    print(f"[download] {repo} -> {local_dir}")
    snapshot_download(
        repo_id=repo,
        repo_type=repo_type,
        local_dir=str(local_dir),
        local_dir_use_symlinks=False,
        resume_download=True,
    )
print('Done')
"@

$py | python -
