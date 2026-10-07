#!/bin/bash
# setup PARI + cypari2, smoke-test the fast backend
sudo apt-get update -q >/dev/null 2>&1
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -q python3-pip pari-gp libpari-dev >/tmp/apt.log 2>&1
echo "[setup] apt: $(tail -1 /tmp/apt.log)"
pip3 install --break-system-packages -q cypari2 mpmath numpy >/tmp/pip.log 2>&1 && echo "[setup] pip OK" || { echo "[setup] pip FAIL:"; tail -6 /tmp/pip.log; }
echo "[cores] nproc = $(nproc)"
echo "[smoke] PARI lfunlambda test (D=-8, the conductor mpmath mis-evaluated):"
python3 - <<'PY'
try:
    import cypari2
    p = cypari2.Pari(); p.set_real_precision(38)
    for D in (-8, -3, 5):
        v = complex(p.lfunlambda(p.lfuncreate(int(D)), p('1/2')))
        print(f"   Lambda(1/2, chi_{D}) = {v.real:.6f} (im {v.imag:.1e})")
    print("   cypari2 OK -> backend=pari (fast, high conductor)")
except Exception as e:
    print("   cypari2 UNAVAILABLE:", repr(e), "-> will fall back to backend=mpmath")
PY
