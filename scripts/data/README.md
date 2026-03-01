# Dataset Downloads (RunPod-first)

Files:
- configs/data/dataset_registry.yaml
- scripts/data/download_hf_datasets.sh
- scripts/data/download_hf_datasets.ps1

Run on RunPod:

```bash
pip install -U huggingface_hub pyyaml
export HF_TOKEN=***
bash scripts/data/download_hf_datasets.sh
```

Notes:
- Downloads only entries with status: use or use_sample_only.
- conditional entries are skipped by default.
- Verify licenses before merging into final train mix.
