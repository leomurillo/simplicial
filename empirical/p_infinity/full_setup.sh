#!/bin/bash
# complete setup: PARI + cypari2 + mpmath/numpy (python3-dev/pkg-config/libgmp were the missing build deps)
sudo apt-get update -q >/dev/null 2>&1
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -q python3-pip python3-dev pkg-config pari-gp libpari-dev libgmp-dev >/tmp/apt.log 2>&1
echo "[setup] apt done"
pip3 install --break-system-packages -q cypari2 mpmath numpy >/tmp/pip.log 2>&1 && echo "[setup] pip OK" || { echo "[setup] pip FAIL"; tail -6 /tmp/pip.log; }
python3 - <<'PY'
import os
try:
    import cypari2, mpmath
    p=cypari2.Pari(); p.set_real_precision(90)
    print("[setup] cypari2+mpmath OK; sample Lambda(1/2,chi_-3) =", complex(p.lfunlambda(p.lfuncreate(-3), p('1/2'))).real)
    print("[setup] cores =", os.cpu_count())
except Exception as e:
    print("[setup] IMPORT FAIL:", repr(e))
PY
