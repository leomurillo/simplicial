"""Independent checker for Krasikov-Lagarias certificates (Paper 01g, Section 12.8).

Usage: python verify_kl_certificate.py <k> <gamma>

Loads kl_cert_k{k}.npy, the principal variables c_k^m for the classes m = 2 (mod 3)
modulo 3^k in increasing order of m, and verifies that they form a feasible solution
of the linear program L_k^NT(lambda), lambda = 2^gamma, of Krasikov-Lagarias
(Acta Arith. 109 (2003), eqs. (2.7)-(2.14)):

  (L0) 1 <= c_k^m                                   (min normalized to 1)
  (L1) m = 2 (mod 9): c^m <= c^{4m} lambda^-2 + a^{(4m-2)/3} lambda^(alpha-2)
  (L2) m = 5 (mod 9): c^m <= c^{4m} lambda^-2
  (L3) m = 8 (mod 9): c^m <= c^{4m} lambda^-2 + a^{(2m-1)/3} lambda^(alpha-1)
  (L4) a^j = min(c^j, c^{j+3^(k-1)}, c^{j+2*3^(k-1)}) for j mod 3^(k-1)

with alpha = log2 3. By their Theorem 2.2, feasibility for some 1 < lambda <= 2 gives
pi_a(x) >= x^(log2 lambda) for all sufficiently large x, for every a not divisible by 3.

Check 1: all constraints in float64, requiring relative slack > 1e-9 (float64 rounding
is below 1e-13 here). Check 2: the 2000 tightest constraints recomputed in 60-digit
mpmath arithmetic from the exact dyadic values of the stored float64 numbers.
"""
import sys, math
from pathlib import Path
import numpy as np
import mpmath as mp

k = int(sys.argv[1]); gamma = mp.mpf(sys.argv[2])
HERE = Path(__file__).resolve().parent
c = np.load(HERE / f"kl_cert_k{k}.npy")
M = 3 ** k
prin = np.arange(2, M, 3)                      # m = 2 mod 3, increasing
assert len(c) == len(prin)
pos = np.full(M, -1, dtype=np.int64); pos[prin] = np.arange(len(prin))
def C(m): return c[pos[m % M]]
assert (pos[prin % M] >= 0).all()
cmin = c.min()
ok_L0 = abs(cmin - 1.0) < 1e-12 and (c >= 1.0 - 1e-12).all()
# auxiliary variables for classes j = 2 mod 3 modulo 3^(k-1)
def aux(j):
    j = j % (M // 3)
    return np.minimum(np.minimum(C(j), C(j + M // 3)), C(j + 2 * (M // 3)))
lam = float(mp.power(2, gamma)); alpha = math.log2(3)
rows = []
for res, kind in ((2, "L1"), (5, "L2"), (8, "L3")):
    m = prin[prin % 9 == res]
    lhs = C(m)
    rhs = C(4 * m) * lam ** -2
    if kind == "L1": rhs = rhs + aux((4 * m - 2) // 3) * lam ** (alpha - 2)
    if kind == "L3": rhs = rhs + aux((2 * m - 1) // 3) * lam ** (alpha - 1)
    rel = (rhs - lhs) / lhs
    rows.append((kind, m, rel))
minrel = min(r[2].min() for r in rows)
ok_float = minrel > 1e-9
# high-precision recheck of the tightest constraints
mp.mp.dps = 60
L = mp.power(2, gamma); A = mp.log(3) / mp.log(2)
tight = []
for kind, m, rel in rows:
    idx = np.argsort(rel)[:2000]
    tight += [(kind, int(m[i])) for i in idx]
worst = mp.inf
for kind, mm in tight:
    lhs = mp.mpf(float(C(mm)))
    rhs = mp.mpf(float(C(4 * mm))) * L ** -2
    if kind == "L1": rhs += mp.mpf(float(aux((4 * mm - 2) // 3))) * L ** (A - 2)
    if kind == "L3": rhs += mp.mpf(float(aux((2 * mm - 1) // 3))) * L ** (A - 1)
    worst = min(worst, (rhs - lhs) / lhs)
ok_mp = worst > 0
print(f"k={k}, gamma={sys.argv[2]}, lambda={mp.nstr(L, 12)}: variables {len(c)}, Cmax {c.max():.4f}")
print(f"  (L0) min = 1: {ok_L0}")
print(f"  (L1)-(L3) float64 min relative slack: {minrel:.3e}  -> {ok_float}")
print(f"  60-digit recheck of 6000 tightest constraints: min relative slack {mp.nstr(worst, 6)} -> {ok_mp}")
ok = ok_L0 and ok_float and ok_mp
print("CERTIFICATE VALID" if ok else "CERTIFICATE FAILED")
sys.exit(0 if ok else 1)
