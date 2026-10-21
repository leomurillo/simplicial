"""Paper 01g, Section 11 (the rational world and the limit of continuity) -- certificate.

2026-10-17. Criteria declared before first execution. Author certificate after
derivation and exploratory probes; not blind. Retain logs; report failures.

R1  Farey edges are +1 steps: for every pair of Farey neighbours a/b < c/d with
    b,d <= 150 (bc - ad = 1), e(c/d) - e(a/b) = e(ad+1) - e(ad) exactly.
R2  Continued-fraction journeys (phi, sqrt2, e, pi, cbrt2; 40 convergents each):
    consecutive convergents differ by +-Delta_{n_k}, n_k = min(p_k q_{k-1}, p_{k-1} q_k),
    and |ln(r_k/r_{k-1})| = ln(1+1/n_k) (to 1e-40). The height P+(n_k(n_k+1)) exceeds
    the largest Stormer-relevant prime 23 for every k >= 12 in each journey. For phi the
    numerator F_{k+2} brings a prime never seen before in the journey for every k<=40
    except k in {4, 10} (Carmichael's exceptions F_6=8, F_12=144).
R3  Stormer floor of the +1 resolution: for N<=7 the largest n<4e5 with n(n+1)
    p_N-smooth is 1, 8, 80, 4374, 9800, 123200, 336140.
R4  Weyl law: the number of classes of Z^N/Z1 with frame radius <= R equals
    c_N R^{N-1}(1+o(1)), c_N = omega_{N-1} sqrt(N) ((N-1)/N)^{(N-1)/2}; ratio within
    2% at R=32 (N=2,3) and R=12 (N=4). Equidistribution: the fraction of class sizes
    mod ln P_N lying in [0, ln P_N/2) is within 0.02 of 1/2 at those radii.
R5  Commas: the finest nonzero size |ln q| (mod ln P_N) among classes of radius <= R is
    3^12/2^19 (N=2, R=32), 32805/32768 (N=3, R=24), 250047/250000 (N=4, R=12), and
    4375/4374 is the finest at N=4, R=10.
R6  Continuum limit of a fixed frame (N=3): for 5-smooth n <= e^T, T=120, the
    standard-form size statistic sigma(n)/T (sigma = ln n - massaction*ln 30) matches,
    in Kolmogorov distance < 0.03, the law of <l,u> - ln30*min(u) for u uniform in the
    simplex {u>=0, <l,u> <= 1} (Monte Carlo, 400000 samples).
"""
from pathlib import Path
import json, math, sys, time, bisect
from fractions import Fraction as Fr
import numpy as np, itertools
import mpmath as mp
from sympy import factorint, primerange, continued_fraction_iterator, sqrt, E, pi, cbrt

sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
rows = []; t0 = time.perf_counter()
def check(name, ok, detail=""):
    rows.append({"name": name, "pass": bool(ok), "detail": detail}); print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)
PR = list(primerange(2, 10**6))
def vec(q):
    q = Fr(q); d = {}
    for p, a in factorint(q.numerator).items(): d[p] = d.get(p, 0) + a
    for p, a in factorint(q.denominator).items(): d[p] = d.get(p, 0) - a
    return d
def diff(a, b):
    k = set(a) | set(b); return {p: a.get(p, 0) - b.get(p, 0) for p in k if a.get(p, 0) != b.get(p, 0)}

# ---------------- R1
bad = 0; edges = 0
for b in range(1, 151):
    for d in range(1, 151):
        # a/b < c/d neighbours: bc - ad = 1, 0<=a/b, c/d<=1
        for a in range(0, b + 1):
            if math.gcd(a, b) != 1: continue
            if (1 + a * d) % b: continue
            c = (1 + a * d) // b
            if c > d or math.gcd(c, d) != 1 or a == 0: continue
            edges += 1
            if diff(vec(Fr(c, d)), vec(Fr(a, b))) != diff(vec(a * d + 1), vec(a * d)): bad += 1
check("R1 Farey edges are +1 steps", bad == 0 and edges > 1000, f"{edges} Farey edges (b,d<=150), mismatches {bad}")

# ---------------- R2
mp.mp.dps = 120
ok = True; info = {}
for name, x in {"phi": (1 + sqrt(5)) / 2, "sqrt2": sqrt(2), "e": E, "pi": pi, "cbrt2": cbrt(2)}.items():
    it = continued_fraction_iterator(x); a = [int(next(it)) for _ in range(41)]
    ps, qs = [1, a[0]], [0, 1]
    for ak in a[1:]: ps.append(ak * ps[-1] + ps[-2]); qs.append(ak * qs[-1] + qs[-2])
    ps, qs = ps[1:], qs[1:]
    seen = set(); heights = []; newp = []
    for k in range(1, len(ps)):
        A, B = ps[k] * qs[k - 1], ps[k - 1] * qs[k]; n = min(A, B); sgn = 1 if A > B else -1
        D = diff(vec(Fr(ps[k], qs[k])), vec(Fr(ps[k - 1], qs[k - 1])))
        st = diff(vec(n + 1), vec(n))
        ok &= abs(A - B) == 1 and D == {p: sgn * v for p, v in st.items()}
        jump = abs(mp.log(mp.mpf(ps[k]) / qs[k] / (mp.mpf(ps[k - 1]) / qs[k - 1])))
        ok &= abs(jump - mp.log(1 + mp.mpf(1) / n)) < mp.mpf(10) ** -40
        heights.append(max(factorint(n * (n + 1))))
        pr = set(factorint(ps[k])) | set(factorint(qs[k])); newp.append(len(pr - seen)); seen |= pr
    ok &= all(h > 23 for h in heights[11:])
    info[name] = {"max_height": max(heights), "primes_seen": len(seen)}
    if name == "phi":
        zero = [k + 1 for k, c in enumerate(newp) if c == 0]
        ok &= zero == [4, 10]
        info[name]["no_new_prime_steps"] = zero
check("R2 continued-fraction journeys", ok, json.dumps(info))

# ---------------- R3
L = 400_002
gpf = np.ones(L + 1, np.int64)
for p in PR:
    if p > L: break
    gpf[p::p] = p
floors = []
for N in range(1, 8):
    m = np.arange(1, L)
    sel = m[np.maximum(gpf[m], gpf[m + 1]) <= PR[N - 1]]
    floors.append(int(sel.max()))
check("R3 Stormer floor of +1 resolution", floors == [1, 8, 80, 4374, 9800, 123200, 336140], f"{floors}")

# ---------------- R4 / R5
def classes(N, R):
    lnp = np.array([math.log(p) for p in PR[:N]]); lnP = lnp.sum()
    Bd = int(math.ceil(R * 1.5)) + 1
    grid = np.array(list(itertools.product(range(-Bd, Bd + 1), repeat=N - 1)), dtype=np.int64)
    V = np.hstack([grid, np.zeros((len(grid), 1), np.int64)])
    S = V.sum(1); Qn = (V * V).sum(1)
    V = V[(N * Qn - S * S) <= (N - 1) * R * R + 1e-9]
    return V, lnp, lnP
okW = True; det = {}
for N, R in ((2, 32), (3, 32), (4, 12)):
    V, lnp, lnP = classes(N, R)
    cN = (2 * math.pi ** ((N - 1) / 2) / math.gamma((N - 1) / 2) / (N - 1)) * math.sqrt(N) * ((N - 1) / N) ** ((N - 1) / 2)
    ratio = len(V) / (cN * R ** (N - 1))
    sz = (V @ lnp) % lnP; half = float(np.mean(sz < lnP / 2))
    okW &= abs(ratio - 1) < 0.02 and abs(half - 0.5) < 0.02
    det[N] = {"count": len(V), "ratio": round(ratio, 4), "half": round(half, 4)}
check("R4 Weyl law and equidistribution", okW, json.dumps(det))
def finest(N, R):
    V, lnp, lnP = classes(N, R)
    s = V @ lnp; r = np.abs((s + lnP / 2) % lnP - lnP / 2)
    i = np.flatnonzero(r > 1e-12)[np.argmin(r[r > 1e-12])]
    v = V[i]; k = round((s[i] - r[i] * np.sign(((s[i] + lnP / 2) % lnP) - lnP / 2)) / lnP) if False else None
    # reconstruct the rational: shift by the gauge so that the size is near 0
    j = -round(s[i] / lnP); w = v + j
    q = Fr(1)
    for p, e_ in zip(PR[:N], w): q *= Fr(p) ** int(e_)
    return q if q > 1 else 1 / q
got = {(2, 32): finest(2, 32), (3, 24): finest(3, 24), (4, 12): finest(4, 12), (4, 10): finest(4, 10)}
exp = {(2, 32): Fr(3**12, 2**19), (3, 24): Fr(32805, 32768), (4, 12): Fr(250047, 250000), (4, 10): Fr(4375, 4374)}
check("R5 commas", got == exp, "; ".join(f"N={k[0]},R={k[1]}: {got[k]}" for k in got))

# ---------------- R6
T = 120.0; lns = [math.log(2), math.log(3), math.log(5)]; ln30 = sum(lns)
sig = []
for a in range(0, int(T / lns[0]) + 1):
    for b in range(0, int((T - a * lns[0]) / lns[1]) + 1):
        cmax = int((T - a * lns[0] - b * lns[1]) / lns[2])
        for c in range(0, cmax + 1):
            m = min(a, b, c); sig.append((a * lns[0] + b * lns[1] + c * lns[2] - m * ln30) / T)
sig = np.sort(np.array(sig))
rng = np.random.default_rng(20261017)
z = rng.dirichlet(np.ones(4), size=400000)[:, :3]  # uniform on {z>=0, sum z<=1}
u = z / np.array(lns)
mc = np.sort((u @ np.array(lns)) - ln30 * u.min(1))
grid = np.linspace(0, 1, 2001)
F1 = np.searchsorted(sig, grid, side="right") / len(sig); F2 = np.searchsorted(mc, grid, side="right") / len(mc)
ks = float(np.abs(F1 - F2).max())
check("R6 continuum limit (tent law)", ks < 0.03, f"{len(sig)} lattice points; Kolmogorov distance {ks:.4f}")

el = time.perf_counter() - t0; npass = sum(r["pass"] for r in rows)
print(f"\n{npass}/{len(rows)} passed in {el:.1f} s")
(HERE / "cert_rational_world_results.json").write_text(json.dumps({"rows": rows, "elapsed_s": el}, indent=2))
sys.exit(0 if npass == len(rows) else 1)
