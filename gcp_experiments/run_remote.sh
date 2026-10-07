#!/bin/bash
# Remote setup + run for A1/A4 on a fresh Debian GCP instance. Idempotent-ish; stops on error.
set -e
echo "=== apt deps ==="
sudo apt-get update -qq
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3-venv python3-pip python3-full >/dev/null
cd ~/gcp_experiments
echo "=== venv + pip ==="
python3 -m venv venv
. venv/bin/activate
pip install --quiet --upgrade pip
pip install --quiet torch --index-url https://download.pytorch.org/whl/cpu
pip install --quiet "transformers>=4.40" "numpy>=1.26" "datasets>=2.18"
export GCP_RUN=1
echo "=== numpy selftest (no torch) ==="
python kernel_probe.py
echo "=== A1 compositionality tax ==="
python a1_compositionality_tax.py
echo "=== A4 dark structure ==="
python a4_dark_structure.py
echo "=== DONE; results: ==="
ls -la results/
