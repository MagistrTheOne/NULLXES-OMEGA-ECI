# RunPod script templates

These scripts are templates for remote execution on RunPod workers.

## Usage notes

- Do not execute heavy training locally.
- Update environment variables in RunPod secrets.
- Pin config paths and checkpoint prefixes before launch.

## Scripts

- `submit_pretrain.sh`: pretraining launch template.
- `submit_posttrain.sh`: post-training launch template.
- `sync_checkpoints.sh`: checkpoint sync helper template.

