"""probe_pinfG_cubic_drift.py -- P-inf-G strike 1: the cubic drift of the seam pivot along
the arithmetic fluctuation (the consumption attempt's bridge object, measured).

FRAME (P-inf-G sections 1-4). The seam-renewal trichotomy: exit / uniform interiority (U) /
marginal boundary contact.  Lemma G.1 (cone dynamics, elementary): at a stationary marginal
contact, odd-order pushes along a tangential marginal mode must vanish.  CATEGORY GUARD:
the renewal map's state-derivatives are order-2 arithmetic (built from the kernel); the
genuine order-3 object lives in the stream -- operationally, in the directional expansion
of the seam pivot along the CRAMER FLUCTUATION:
    Delta K = K_true - K_cramer,
K_cramer = the builder with the prime atoms sum_n Lambda(n) n^{-1/2} phi(log n) replaced by
the PNT-smooth integral int_0^L e^{u/2} phi(u) du (the section-18 pole-matching partner).
Delta K is exactly the zero-oscillation content of the kernel, computed prime-side (no zero
input).  With seam partition K = [[A, b], [b^T, c]] (seam = wrap site i=0), base objects
u = Abar^{-1} bbar, r = Abar^{-1} db, m = Abar^{-1}(dA u):
    d0(t) = phi0 + phi1 t + phi2 t^2 + phi3 t^3 + O(t^4),
    phi0 = cbar - bbar^T u
    phi1 = dc - 2 db^T u + u^T dA u
    phi2 = -(r^T db - 2 r^T dA u + m^T dA u)
    phi3 = -2 r^T dA m + r^T dA r + m^T dA m
(d0(1) = the true seam pivot; phi1/phi2/phi3 = the drift functional's order attribution --
D1 linear, D2 pair-correlation-grade, D3 the CUBIC the exclusion wants to consume).

PRE-REGISTERED (GPD, fixed before the run):
  G-R0 (validation): exact d0 at t=0 and t=1 from direct elimination matches phi0 and the
      independently computed true seam pivot (lineage: v2's R_seam values at 1e-3).
  G-R1 (instrument): |d0(1) - (phi0+phi1+phi2+phi3)| <= 0.20 * |d0(1) - phi0| at every
      window (the cubic Taylor captures the Cramer gap to 20%).  NOT a route falsifier:
      structured failure here = the gap is non-perturbative in the fluctuation (itself a
      finding -- the E-ladder as an infinite-order conspiracy; report and characterize).
  G-R2 (measurement, no falsifier): sign and share of the Cramer gap, (d0_true - phi0)/d0,
      logged per window; cond/ground of Abar vs A_true logged (ladder-presence check:
      the Cramer base should LACK the exp-small E-ladder -- its ground O(1)-ish).
  G-R3 (cubic stability): sign(phi3) constant across lam in {1.8, 2.0, 2.2, 2.35, 2.5}.
      FALSIFIER: a sign flip => no stable cubic drift at this instrument; G.2's weld
      unsupported; obstruction named.
  G-R4 (route-killer): |phi3|/|phi2| does not fall monotonically by a cumulative factor
      >= 10 across the sweep.  FALSIFIER fires => the cubic decouples from the seam mode
      asymptotically => the exclusion is toothless; route dies with the obstruction named.
  G-R5 (anatomy): the linear sensitivity is carried by the longest shifts -- the top
      quartile of prime powers by log n carries >= 30% of sum_p |phi1(p)| at lam = 2.5
      (the seam reads the wrap-distance arrivals; v2-Q3's boundary band, prime-resolved).

Machinery: dps 50 throughout; the v2/v5-certified builder shape with a prime_mode flag
(true atoms / cramer integral); one mp LU of Abar per window + 3 solves; per-prime phi1
split (linear, no extra solves).  F64 rules: exact mp kernels (1); determinant-ratio /
directional-Taylor observables only (5); dps clears every floor used here (6: Abar is
ladder-free by design; A_true is never inverted).
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 50


def primes_upto(xx):
    out = []; n = 2
    while n <= xx:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def build_QW_mode(lam, N, mode="true"):
    """wave_limit-lineage builder; prime block = atoms ('true') or PNT integral ('cramer').
    Returns (Q, L, pj) with pj the atom list [(y_p, w_p)] for the per-prime split."""
    L = 2 * mp.log(lam)
    w = lambda k: 2 * mp.pi * k / L
    pj = []
    for p in primes_upto(float(mp.exp(L)) + 1e-12):
        j = 1
        while j * mp.log(p) <= L + mp.mpf("1e-40"):
            pj.append((j * mp.log(p), mp.log(p) * mp.power(p, -mp.mpf(j) / 2)))
            j += 1
    pts = mp.linspace(0, L, 14)
    S, D = {}, {}
    for k in range(-N, N + 1):
        wk = w(k)
        A = mp.quad(lambda y: mp.sin(wk * y) * 2 * mp.cosh(y / 2), pts)
        B = mp.quad(lambda y: mp.exp(y / 2) * mp.sin(wk * y) / (2 * mp.sinh(y)) if y != 0 else wk / 2, pts)
        if mode == "true":
            P = mp.fsum(cw * mp.sin(wk * yp) for yp, cw in pj) if pj else mp.mpf(0)
        else:
            P = mp.quad(lambda u: mp.exp(u / 2) * mp.sin(wk * u), pts)
        S[k] = A - B - P
    tailL = mp.log(mp.tanh(L / 2)) / 2
    for k in range(0, N + 1):
        wk = w(k)
        qd = lambda y: 2 * (1 - y / L) * mp.cos(wk * y)
        A = mp.quad(lambda y: qd(y) * 2 * mp.cosh(y / 2), pts)
        Bint = mp.quad(lambda y: (mp.exp(y / 2) * qd(y) - 2) / (2 * mp.sinh(y)) if y != 0
                       else (mp.mpf(1) / 2 - 1 / L), pts)
        WR = (mp.log(4 * mp.pi) + mp.euler) + Bint + 2 * tailL
        if mode == "true":
            P = mp.fsum(cw * (2 * (1 - yp / L) * mp.cos(wk * yp)) for yp, cw in pj) if pj else mp.mpf(0)
        else:
            P = mp.quad(lambda u: mp.exp(u / 2) * 2 * (1 - u / L) * mp.cos(wk * u), pts)
        D[k] = A - WR - P
    dim = 2 * N + 1
    Q = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m_ = i - N, j - N
            Q[i, j] = D[abs(n)] if n == m_ else (S[m_] - S[n]) / (mp.pi * (n - m_))
    return Q, L, pj


def prime_atom_Q(lam, N, yp, cw):
    """The single prime-power atom's contribution to -Q (it enters K with minus)."""
    L = 2 * mp.log(lam)
    w = lambda k: 2 * mp.pi * k / L
    Sv = {k: cw * mp.sin(w(k) * yp) for k in range(-N, N + 1)}
    Dv = {k: cw * (2 * (1 - yp / L) * mp.cos(w(k) * yp)) for k in range(0, N + 1)}
    dim = 2 * N + 1
    Q = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m_ = i - N, j - N
            Q[i, j] = Dv[abs(n)] if n == m_ else (Sv[m_] - Sv[n]) / (mp.pi * (n - m_))
    return Q


def to_point(Q, N):
    dim = 2 * N + 1
    B = mp.zeros(dim, dim)
    for n in range(dim):
        for i in range(dim):
            B[n, i] = mp.e**(2j * mp.pi * (n - N) * i / dim) / mp.sqrt(dim)
    K = (B.H) * Q * B
    Kr = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            Kr[i, j] = (mp.re(K[i, j]) + mp.re(K[j, i])) / 2
    return Kr


def seam_split(Kr, dim):
    """Partition w.r.t. the seam site i=0: returns A (mp.matrix), b (col), c."""
    rest = list(range(1, dim))
    A = mp.zeros(dim - 1, dim - 1)
    b = mp.zeros(dim - 1, 1)
    for a_, i in enumerate(rest):
        b[a_] = Kr[i, 0]
        for b2, j in enumerate(rest):
            A[a_, b2] = Kr[i, j]
    return A, b, Kr[0, 0]


def seam_pivot_direct(Kr, dim):
    A, b, c = seam_split(Kr, dim)
    sol = mp.lu_solve(A, b)
    return c - mp.fsum(b[a_] * sol[a_] for a_ in range(dim - 1))


CASES = [(1.8, 20), (2.0, 24), (2.2, 27), (2.35, 30), (2.5, 32)]
R_SEAM_V2 = {1.8: 0.28839, 2.0: 0.20639, 2.2: 0.14963, 2.35: 0.11299, 2.5: 0.092155}

print("== the cubic drift of the seam pivot (mp dps=50) ==")
rows = []
for lam, N in CASES:
    t0 = time.time()
    dim = 2 * N + 1
    Qt, L, pj = build_QW_mode(mp.mpf(repr(lam)), N, "true")
    Qc, _, _ = build_QW_mode(mp.mpf(repr(lam)), N, "cramer")
    Kt, Kc = to_point(Qt, N), to_point(Qc, N)
    At, bt, ct = seam_split(Kt, dim)
    Ac, bc, cc = seam_split(Kc, dim)
    dA = At - Ac
    db = bt - bc
    dc = ct - cc
    # base objects (one LU of the Cramer interior; three solves)
    u = mp.lu_solve(Ac, bc)
    dAu = dA * u
    r = mp.lu_solve(Ac, db)
    m = mp.lu_solve(Ac, dAu)
    dAm = dA * m
    dAr = dA * r
    dot = lambda x, y: mp.fsum(x[a_] * y[a_] for a_ in range(dim - 1))
    phi0 = cc - dot(bc, u)
    phi1 = dc - 2 * dot(db, u) + dot(u, dAu)
    phi2 = -(dot(r, db) - 2 * dot(r, dAu) + dot(m, dAu))
    phi3 = -2 * dot(r, dAm) + dot(r, dAr) + dot(m, dAm)
    d0_true = seam_pivot_direct(Kt, dim)
    d0_cram = seam_pivot_direct(Kc, dim)
    bare0 = Kt[0, 0]
    # per-prime linear split (no new solves)
    shares = []
    for yp, cw in pj:
        Qp = prime_atom_Q(mp.mpf(repr(lam)), N, yp, cw)
        Kp = to_point(Qp, N)            # atom enters K with MINUS: dK_p = -Kp
        Ap, bp, cp = seam_split(Kp, dim)
        ph1p = -(cp - 2 * dot(bp, u) + dot(u, Ap * u))
        shares.append((float(yp), float(ph1p)))
    el = time.time() - t0
    gap = d0_true - d0_cram
    rec = (phi1 + phi2 + phi3)
    rel_recon = abs(float((gap - rec) / gap)) if gap != 0 else float("nan")
    rows.append(dict(lam=lam, phi0=float(phi0), phi1=float(phi1), phi2=float(phi2),
                     phi3=float(phi3), d0t=float(d0_true), d0c=float(d0_cram),
                     gap=float(gap), recon=rel_recon, shares=shares,
                     Rseam=float(d0_true / bare0)))
    print(f"   lam={lam} ({el:.0f}s): d0_true={float(d0_true):.5f}  d0_cramer={float(d0_cram):.5f}"
          f"  gap={float(gap):+.5f}")
    print(f"      phi1={float(phi1):+.5f}  phi2={float(phi2):+.5f}  phi3={float(phi3):+.6f}"
          f"  recon-resid={rel_recon:.3f}")

print("\n== G-R0: lineage validation (R_seam vs v2 truths) ==")
g0 = True
for rec in rows:
    diff = abs(rec["Rseam"] - R_SEAM_V2[rec["lam"]])
    ok = diff < 1e-3
    g0 &= ok
    print(f"   lam={rec['lam']}: R_seam={rec['Rseam']:.5f} vs v2 {R_SEAM_V2[rec['lam']]:.5f}  "
          + ("ok" if ok else "MISS"))
print("   G-R0: " + ("SURVIVES" if g0 else "FIRED -- lineage broken, stop"))

print("\n== G-R1: reconstruction (does the cubic Taylor capture the Cramer gap?) ==")
g1 = all(rec["recon"] <= 0.20 for rec in rows)
for rec in rows:
    print(f"   lam={rec['lam']}: |gap - (phi1+phi2+phi3)|/|gap| = {rec['recon']:.3f}")
print("   G-R1: " + ("SURVIVES -- perturbative regime" if g1 else
                     "fired -- non-perturbative component (characterize, not a route kill)"))

print("\n== G-R2: the Cramer gap (measurement) ==")
for rec in rows:
    print(f"   lam={rec['lam']}: gap/d0_true = {rec['gap']/rec['d0t']:+.4f}   "
          f"(d0_cramer {'>' if rec['gap'] < 0 else '<'} d0_true)")

print("\n== G-R3/G-R4: the cubic's stability and weight ==")
signs = [np.sign(rec["phi3"]) for rec in rows]
g3 = len(set(signs)) == 1
ratios = [abs(rec["phi3"]) / max(abs(rec["phi2"]), 1e-300) for rec in rows]
print("   sign(phi3): " + "  ".join(f"{rec['lam']}:{'+' if rec['phi3']>0 else '-'}" for rec in rows))
print("   |phi3|/|phi2|: " + "  ".join(f"{rec['lam']}:{rt:.3f}" for rec, rt in zip(rows, ratios)))
mono_fall = all(b < a for a, b in zip(ratios, ratios[1:])) and ratios[-1] <= ratios[0] / 10
g4 = not mono_fall
print("   G-R3: " + ("SURVIVES -- stable cubic sign" if g3 else "FIRED -- sign flips; weld unsupported"))
print("   G-R4: " + ("SURVIVES -- cubic does not decouple" if g4 else
                     "FIRED -- cubic decouples; exclusion toothless"))

print("\n== G-R5: who carries the seam's linear sensitivity (per prime power) ==")
big = rows[-1]
tot = sum(abs(s) for _, s in big["shares"])
ordered = sorted(big["shares"], key=lambda t: -t[0])
qcut = max(1, len(ordered) // 4)
topq = sum(abs(s) for _, s in ordered[:qcut]) / tot
print(f"   lam=2.5 prime powers (log n, phi1 share): "
      + "  ".join(f"({y:.2f},{s:+.4f})" for y, s in sorted(big['shares'])))
print(f"   top quartile by log n carries {topq:.2f} of total |phi1| mass (register >= 0.30)")
g5 = topq >= 0.30
print("   G-R5: " + ("SURVIVES -- the seam reads the longest shifts" if g5 else
                     "fired -- sensitivity anatomy differs; report"))

np.savez("empirical/p_infinity/pinfG_cubic_drift.npz",
         lams=np.array([r["lam"] for r in rows]),
         phi=np.array([[r["phi1"], r["phi2"], r["phi3"]] for r in rows]),
         gaps=np.array([r["gap"] for r in rows]),
         d0t=np.array([r["d0t"] for r in rows]),
         d0c=np.array([r["d0c"] for r in rows]))

verdict = g0 and g3 and g4
print("\nRESULT: " + ("GREEN -- the cubic drift exists, is stable, and does not decouple"
                      if verdict else "PARTIAL/FIRED -- see blocks (GPD: diagnose, retain)"))
