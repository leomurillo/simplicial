"""Torch-free tuning (LEAN): find the d_sub where the parity phase boundary is clean, and show it
degrades as d_sub grows (the practical obstruction). numpy only -- safe locally."""
import sys
import numpy as np
from kernel_probe import cv_metric
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

rng = np.random.default_rng(0)
N = 1500

def parity_test(d_sub, k, lam):
    Z = rng.standard_normal((N, d_sub)) + 0.5 * rng.standard_t(3, size=(N, d_sub))
    y = np.prod(np.sign(Z[:, :k]), axis=1)
    return {m: round(cv_metric(Z, y, m, "clf", lam=lam, n_splits=3), 3) for m in (1, 2, 3, 4)}

print("Goal: degree<k ~ .5, degree>=k high, sharp jump at m=k.\n")
for k in (2, 3, 4):
    print(f"=== k={k} ===")
    for d_sub in (k, k + 2, 8):
        accs = parity_test(d_sub, k, 1e-4)
        below = accs[k - 1] if k - 1 >= 1 else 0.5
        clean = "  <== CLEAN" if (accs[k] >= 0.85 and below <= 0.65) else ""
        print(f"  d_sub={d_sub:<2} acc={accs}  jump@k={accs[k]-below:+.2f}{clean}")
    print()
