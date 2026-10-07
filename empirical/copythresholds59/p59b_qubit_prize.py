"""
Paper 59 certificate, part Q: the size of the prize for qubit copies (two Gibbs qubits per copy, A colder).
mpmath / fractions only.  Usage: python p59b_qubit_prize.py

Exact n-copy ergotropy: the n-copy state is diagonal with groups (a, b) = (#excited A, #excited B), multiplicity
C(n, a) C(n, b), energy a eps_A + b eps_B; the passive energy pairs probabilities (descending) with energies (ascending)
with multiplicities.  f(n) = W(n) / (n W_rev), W_rev = reversible (finite-body Carnot) work of one copy.  n_half = least n
with f(n) >= 1/2 (the harvest number).  eps_A = x, eps_B = 1, beta_B = 1, beta_A = 1 + delta.

DISCLOSURE.  An exploratory scan (scratchpad explore_qubit_prize2.py) computed n*, f(n*), n_half for golden, sqrt3 and
x = 1/2 at delta in {0.4, 0.2, 0.1, 0.05, 0.025}.  Block R below reproduces those values deterministically and is NOT
BLIND.  Block B was written before any computation for its spectra and IS BLIND.

PRE-REGISTERED (written 2026-10-02)
  R1 [not blind] reproduction: the 15 (n*, f(n*), n_half) values of the exploratory table, to 3 significant figures.
  R2 [exact structure] in every case W(n) < 1e-30 W_rev for n < n* and W(n*) > 0, and n* equals the denominator of the
     Stern-Brocot simplest fraction of (x, x(1 + delta)) (Port Theorem 6.6 via Corollary 6.7).
  B1 [BLIND] at delta = 0.05: x = 1/sqrt2 (badly approximable) has n* = 7, x = 3/4 (resonant) has n* = 9 (Stern-Brocot).
  B2 [BLIND] at delta = 0.05: f(n*) for 1/sqrt2 exceeds f(n*) for 3/4 by at least a factor 10, and n_half(1/sqrt2) <
     n_half(3/4) (the harvest also favours the badly approximable spectrum).        L: either inequality fails.
"""
import math
from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 50
res = []
def check(name, ok, detail=""):
    res.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

def ergotropy_n(n, eA, eB, bA, bB):
    qA = 1 / (1 + mp.exp(bA * eA)); qB = 1 / (1 + mp.exp(bB * eB))
    groups = []
    for a in range(n + 1):
        for b in range(n + 1):
            mult = math.comb(n, a) * math.comb(n, b)
            lp = a * mp.log(qA) + (n - a) * mp.log(1 - qA) + b * mp.log(qB) + (n - b) * mp.log(1 - qB)
            groups.append((lp, a * eA + b * eB, mult))
    Eavg = mp.fsum(mp.exp(lp) * E * mu for lp, E, mu in groups)
    byp = sorted(groups, key=lambda g: -g[0]); byE = sorted(groups, key=lambda g: g[1])
    Epass = mp.mpf(0); j = 0; rem = byE[0][2]
    for lp, E, mu in byp:
        left = mu
        while left > 0:
            take = min(left, rem)
            Epass += take * mp.exp(lp) * byE[j][1]
            left -= take; rem -= take
            if rem == 0 and j + 1 < len(byE):
                j += 1; rem = byE[j][2]
    return Eavg - Epass

def W_rev(eA, eB, bA, bB):
    def E(e, b): return e / (1 + mp.exp(b * e))
    def S(e, b):
        q = 1 / (1 + mp.exp(b * e)); return -(q * mp.log(q) + (1 - q) * mp.log(1 - q))
    Ei = E(eA, bA) + E(eB, bB); Si = S(eA, bA) + S(eB, bB)
    lo, hi = min(bA, bB), max(bA, bB)
    for _ in range(250):
        mid = (lo + hi) / 2
        if S(eA, mid) + S(eB, mid) > Si: lo = mid
        else: hi = mid
    bs = (lo + hi) / 2
    return Ei - E(eA, bs) - E(eB, bs)

def scan(x, delta, nmax=160):
    d = mp.mpf(delta); eA, eB = x, mp.mpf(1); bA, bB = 1 + d, mp.mpf(1)
    Wr = W_rev(eA, eB, bA, bB)
    nstar = fstar = nhalf = None; below_ok = True
    for n in range(1, nmax + 1):
        f = ergotropy_n(n, eA, eB, bA, bB) / n / Wr
        if nstar is None:
            if f > mp.mpf('1e-30'):
                nstar, fstar = n, f
            else:
                below_ok &= f < mp.mpf('1e-30')
        if nhalf is None and f >= 0.5:
            nhalf = n; break
    return nstar, fstar, nhalf, below_ok

def sb_den(lo_pred, hi_pred):
    lp, lq, rp, rq = 0, 1, 1, 0
    while True:
        a, b = lp + rp, lq + rq
        if lo_pred(a, b): lp, lq = a, b
        elif hi_pred(a, b): rp, rq = a, b
        else: return a, b

phi = (1 + mp.sqrt(5)) / 2
TABLE = {("golden", '0.4'): (3, 0.1355, 6), ("golden", '0.2'): (3, 0.1989, 5), ("golden", '0.1'): (3, 0.1379, 11),
         ("golden", '0.05'): (8, 0.001589, 39), ("golden", '0.025'): (8, 0.00227, 35),
         ("sqrt3", '0.4'): (3, 0.1961, 5), ("sqrt3", '0.2'): (3, 0.1413, 7), ("sqrt3", '0.1'): (5, 0.05063, 14),
         ("sqrt3", '0.05'): (5, 0.03593, 24), ("sqrt3", '0.025'): (12, 6.494e-5, 70),
         ("half", '0.4'): (3, 0.1076, 9), ("half", '0.2'): (7, 0.006664, 29), ("half", '0.1'): (11, 8.225e-5, 94),
         ("half", '0.05'): (21, 5.186e-9, None), ("half", '0.025'): (41, 1.632e-17, None)}
XS = {"golden": 1 / phi, "sqrt3": 1 / mp.sqrt(3), "half": mp.mpf(1) / 2}
okR1 = True; okR2 = True; det = []
for (name, dl), (n0, f0, h0) in TABLE.items():
    x = XS[name]
    nstar, fstar, nhalf, below = scan(x, dl)
    same = nstar == n0 and nhalf == h0 and abs(float(fstar) / f0 - 1) < 2e-3
    okR1 &= same
    xd = mp.mpf(dl)
    a, b = sb_den(lambda p, q: mp.mpf(p) / q <= x, lambda p, q: mp.mpf(p) / q >= x * (1 + xd))
    okR2 &= below and nstar == b
    det.append(f"{name} {dl}: n*={nstar} (SB {b}), f={mp.nstr(fstar, 4)}, n_half={nhalf}")
    print("   " + det[-1], flush=True)
check("R1 [not blind] reproduction of the exploratory prize table (15 cases)", okR1)
check("R2 [exact structure] W = 0 below n*, W > 0 at n*, n* = Stern-Brocot denominator (15 cases)", okR2)

# ------------------------------------------------------------- blind block
nb1 = scan(1 / mp.sqrt(2), '0.05', nmax=200)
nb2 = scan(mp.mpf(3) / 4, '0.05', nmax=200)
print(f"   blind: 1/sqrt2: n*={nb1[0]}, f(n*)={mp.nstr(nb1[1], 4)}, n_half={nb1[2]};  3/4: n*={nb2[0]}, "
      f"f(n*)={mp.nstr(nb2[1], 4)}, n_half={nb2[2]}", flush=True)
check("B1 [BLIND] delta = 0.05: n*(1/sqrt2) = 7, n*(3/4) = 9", nb1[0] == 7 and nb2[0] == 9)
h1 = nb1[2] if nb1[2] is not None else 10 ** 9
h2 = nb2[2] if nb2[2] is not None else 10 ** 9
check("B2 [BLIND] delta = 0.05: f(n*) larger by >= 10x and n_half smaller for 1/sqrt2 than for 3/4",
      nb1[1] >= 10 * nb2[1] and h1 < h2, f"ratio f = {mp.nstr(nb1[1] / nb2[1], 4)}; n_half {nb1[2]} vs {nb2[2]}")
print(f"\nTOTAL: {sum(res)}/{len(res)} PASS")
