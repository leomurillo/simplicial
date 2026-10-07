"""probe_pinfG_cubic_drift_v2.py -- P-inf-G strike 1, round 2: the per-arrival cubic
re-based INSIDE the cone, read in the d_minus (chiral) block, with the NON-CIRCULARITY
GATE as the headline falsifier.

ROUND-1 POST-MORTEM (P-inf-G section 6): the Cramer base is INDEFINITE (Prop G.4) -- the
low-order coefficients were boundary-crossing artifacts.  ROUND 2 re-bases at the TRUE
kernel.  TWO SMOKE-TEST DISCOVERIES locked into this design before the run:

  (SMK-1, the boundary node) An atom at the window edge y = L' is INVISIBLE in its own
  frame: sin(2 pi k y/L') = 0 for all k AND the Fejer ramp (1 - y/L') = 0.  Arrivals
  phase in continuously as the window grows PAST them.  Hence the edge band
  (lam^2, lam^2+1] is the wrong instrument (its atom sits on the node); the per-arrival
  push must be read at the CROSSOVER BAND (lam^2 - 1, lam^2] -- one rung behind the
  edge, exactly where the saturation wave (F.22, section 20) says the eating happens.
  Band atoms: lam=1.8 -> n=3; 2.0 -> 4=2^2; 2.2 -> 4; 2.35 -> 5; 2.5 -> NONE (n=6
  composite: the pure-smooth control step).

  (SMK-2, the radius) Replacing ONE band's atoms by their PNT mean already exits the
  cone (float min-eig -0.14 at the smoke window): the cone is only ~eps thin in the
  fluctuation direction (the exp-small ladder rungs are exponentially sensitive
  detectors, F section 23.5 -- here certified at single-arrival granularity: Prop G.4
  LOCALIZED to one arrival).  Consequently the Taylor radius at the true base is ~eps
  and NO order-3 polynomial captures the full step: the phi's are GERM objects -- which
  is what Lemma G.1 consumes (D T, D^2 T, D^3 T at the point).  The validity test is an
  exact algebra unit test + radius readings, NOT "capture the gap" (round 1's framing,
  wrong both times for opposite reasons).  The pole-normalized SHAPE INVARIANT
      g3 = phi3 * phi1 / phi2^2    (== 1 for a pure single-pole resonance)
  is the carrier of cubic content beyond resolvent blow-up; the gate runs on BOTH the
  raw phi3 and g3.

THE FRAME.  Everything lives on the lam'-grid (lam'^2 = lam^2 + 1).  The certified
builder is LINEAR in the prime measure:
   K_true(lam') = full build;  A_band = atom block of (lam^2-1, lam^2];  S_band = PNT
   block int e^{u/2} over the band;  K_mixed = K_true + A_K - S_K (band smoothed);
   deltaK_arr = K_true - K_mixed = S_K - A_K  = the band's fluctuation, EXACTLY
   (arch/pole/WR cancel identically).  t=1 endpoint = the true kernel (lineage free).
CHANNELS (Thm F.27): d_minus = odd edge O_1 | O_2..O_m (PRIMARY -- the chiral block;
the direction deltaK is reflection-INVARIANT, so this is NOT G.1's symmetry-killed
channel, which needs an odd state-vector); d_plus = even edge; d_0 = seam.

PRE-REGISTERED (GPD; locked before the full run; none can fire on RH-true -- W2):
  W0a (starvation, F64-6): K_true(lam') passes mp Cholesky at dps 65 at every window.
      Fired -> HALT window.
  W0b (symmetry): reflection defects of K_true and deltaK <= 1e-30.  Fired -> HALT.
  W0c (ALGEBRA unit test): the phi-formulas vs Richardson finite differences of d(t) on
      a random 6x6 exact instance, relative error <= 1e-8 per coefficient.
      Fired -> formula bug: HALT (this also retro-guards round 1's formulas).
  W0d (cone status of the mixed base, measurement): mp Cholesky verdict + float min-eig
      (indicative, F64-3).  Expected NON-PSD = Prop G.4 localized to ONE arrival --
      a discovery-grade certificate, not a falsifier.
  W0e (radius readings): |phi2/phi1|, |phi3/phi2| per channel/window, read against the
      ladder eps(lam') (Fuchs pace).  Measurement (the germ's pole structure).
  GATE-A (HEADLINE -- vacuity): off-line family drho(u) = -4[cosh(delta u)-1]cos(g1 u)
      (FE-symmetric quadruple 1/2 +- delta +- i g1, g1 = 14.1347...), delta in
      {0.1, 0.2, 0.3}, at lam in {2.0, 2.5}: deformed base = K_true - blk(drho,[0,L']),
      deformed direction = deltaK - blk(drho, band).  Jitter J = |phi3(65) - phi3(50)|
      on the same objects.  RULE: max_delta |resp(phi3, d_minus)| <= 10 J at BOTH
      windows -> the cubic is BLIND to zero displacement: G.2's route CIRCULAR at this
      instrument; report plainly.
  GATE-A' (normalized vacuity): same rule on g3 with its own jitter J_g.  (The raw phi3
      response is expected resolvent-dominated; g3 is the shape object.  BOTH blind ->
      vacuity verdict; raw responds while g3 blind -> the leak is NAMED: deformation
      read only through the order-2 resolvent/ladder channel.)
  GATE-B/B' (specificity, reading): on-line control = pair moved g1 -> g1+1
      (RH-PRESERVING), Frobenius-matched to off d=0.2.  R_spec = |resp(off)|/|resp(ctrl)|
      on phi3 and on g3: > 3 reads off-line-ness; ~ 1 generic.  Reported, no falsifier.
  S1 (oriented sign, reading + soft rule): sign(phi3/phi1) on d_minus constant across
      atom-bearing windows {1.8, 2.0, 2.2, 2.35}.  CAVEAT registered: under single-pole
      domination phi3/phi1 = 1/t0^2 > 0 trivially -- auto-survival is then VACUOUS
      and is reported as such (the informative sign lives in g3 - 1).
  S2 (non-decoupling, soft): |phi3|/|phi2| not falling x10 cumulatively (expected to
      RISE at Fuchs pace if the ladder dominates -- auto-survival again flagged).
  S3 (diagonal-triple attribution): deltaK = D_a + D_s; phi3(a D_a + b D_s) = c30 a^3 +
      c21 a^2 b + c12 a b^2 + c03 b^3 by 4 exact evaluations (identity check vs phi3 at
      (1,1) <= 1e-25 rel); c30 = the pure-atom triple = the Lambda(n)^3 n^{-3/2}-grade
      unconditional-ground candidate.  Shares reported.
  S4 (channel anatomy): phi-tables on (d_minus, d_plus, d_0); RG-time normalization
      phi3 * lam'^2; relative phi_k / d(1).
  S5 (free ladder check): R_seam at the five lam' windows vs the p = 3.2 +- 0.2
      power-law band through the certified points (deviation = arrival-phase wiggle).
  S6 (the resummed push, (U)-grade reading): the EXACT per-arrival effect d(1) vs d(0)
      per channel -- the eating ratio d_true/d_mixed of one arrival's fluctuation; its
      window-stability = interiority data for (U) from a new instrument.

Machinery: dps 65 (F64-6: floor eps(2.693) ~ 1e-31; near-radical direction, F64-3);
builder = wave-limit lineage verbatim; one full build + two band blocks per window;
LU-based channel pivots only (F64-5).  Lineage: certified lam=2.5 window rebuilt at
dps 65 must give R_seam = 0.09216.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")

HERE = "empirical/p_infinity/"
GAMMA1 = mp.mpf("14.134725141734693790457251983562")

SMOKE = "--smoke" in sys.argv
DPS = 35 if SMOKE else 65
mp.mp.dps = DPS


def primes_upto(xx):
    out = []; n = 2
    while n <= xx:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def build_QW_mode(lam, N, mode="true"):
    """wave_limit-lineage builder (round-1 verbatim); prime block = atoms or PNT integral."""
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


def assemble_Q(Sv, Dv, N):
    dim = 2 * N + 1
    Q = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m_ = i - N, j - N
            Q[i, j] = Dv[abs(n)] if n == m_ else (Sv[m_] - Sv[n]) / (mp.pi * (n - m_))
    return Q


def atoms_blk_Q(Lp, N, atoms):
    """P-side block of atoms [(y, w)] in the L'-frame (enters K with MINUS)."""
    w = lambda k: 2 * mp.pi * k / Lp
    Sv = {k: mp.fsum(cw * mp.sin(w(k) * yp) for yp, cw in atoms) if atoms else mp.mpf(0)
          for k in range(-N, N + 1)}
    Dv = {k: mp.fsum(cw * 2 * (1 - yp / Lp) * mp.cos(w(k) * yp) for yp, cw in atoms)
          if atoms else mp.mpf(0) for k in range(0, N + 1)}
    return assemble_Q(Sv, Dv, N)


def density_blk_Q(Lp, N, dens, a, b, npts):
    """P-side block of a smooth density on [a,b] in the L'-frame (enters K with MINUS)."""
    w = lambda k: 2 * mp.pi * k / Lp
    pts = mp.linspace(a, b, npts)
    Sv = {k: mp.quad(lambda u: dens(u) * mp.sin(w(k) * u), pts) for k in range(-N, N + 1)}
    Dv = {k: mp.quad(lambda u: dens(u) * 2 * (1 - u / Lp) * mp.cos(w(k) * u), pts)
          for k in range(0, N + 1)}
    return assemble_Q(Sv, Dv, N)


_BCACHE = {}
def to_point(Q, N):
    dim = 2 * N + 1
    key = (dim, mp.mp.dps)
    if key not in _BCACHE:
        B = mp.zeros(dim, dim)
        for n in range(dim):
            for i in range(dim):
                B[n, i] = mp.e**(2j * mp.pi * (n - N) * i / dim) / mp.sqrt(dim)
        _BCACHE[key] = B
    B = _BCACHE[key]
    K = (B.H) * Q * B
    Kr = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            Kr[i, j] = (mp.re(K[i, j]) + mp.re(K[j, i])) / 2
    return Kr


def band_atoms(lo, hi):
    """Prime-power atoms with lo < n <= hi (exact integer comparisons)."""
    out = []
    n = int(mp.floor(lo)) + 1
    while mp.mpf(n) <= hi:
        if mp.mpf(n) > lo:
            m_, p_found = n, None
            for p in primes_upto(n):
                if n % p == 0:
                    m_ = n
                    while m_ % p == 0:
                        m_ //= p
                    p_found = p
                    break
            if p_found is not None and m_ == 1:
                out.append((mp.log(n), mp.log(p_found) * mp.power(n, -mp.mpf(1) / 2)))
        n += 1
    return out


def refl_defect(X, dim):
    num = mp.fsum((X[(dim - i) % dim, (dim - j) % dim] - X[i, j])**2
                  for i in range(dim) for j in range(dim))
    den = mp.fsum(X[i, j]**2 for i in range(dim) for j in range(dim))
    return float(mp.sqrt(num / den)) if den > 0 else 0.0


def cholesky_psd(K):
    try:
        mp.cholesky(K)
        return True
    except Exception:
        return False


def fmin_eig(K, dim):
    Kf = np.array([[float(K[i, j]) for j in range(dim)] for i in range(dim)])
    return float(np.linalg.eigvalsh(0.5 * (Kf + Kf.T))[0])


def channel_parts(K, dim, which):
    """(A, b, c) for the channel pivot d = c - b^T A^{-1} b."""
    d_ = dim
    m = (dim - 1) // 2
    if which == "seam":
        rest = list(range(1, dim))
        A = mp.zeros(dim - 1, dim - 1)
        b = mp.matrix(dim - 1, 1)
        for a_, i in enumerate(rest):
            b[a_] = K[i, 0]
            for b2, j in enumerate(rest):
                A[a_, b2] = K[i, j]
        return A, b, K[0, 0]
    sgn = mp.mpf(1) if which == "even" else mp.mpf(-1)
    idx = list(range(2, m + 1))
    ni = len(idx)
    A = mp.zeros(ni, ni)
    b = mp.matrix(ni, 1)
    for a_, k in enumerate(idx):
        b[a_] = (K[k, 1] + sgn * K[k, d_ - 1] + sgn * K[d_ - k, 1] + K[d_ - k, d_ - 1]) / 2
        for b2, l in enumerate(idx):
            A[a_, b2] = (K[k, l] + sgn * K[k, d_ - l] + sgn * K[d_ - k, l] + K[d_ - k, d_ - l]) / 2
    c = (K[1, 1] + sgn * K[1, d_ - 1] + sgn * K[d_ - 1, 1] + K[d_ - 1, d_ - 1]) / 2
    return A, b, c


def dot(x, y, n):
    return mp.fsum(x[a_] * y[a_] for a_ in range(n))


def phi_expand(Abase, bbase, cbase, dA, db, dc):
    """phi0..phi3 of the channel pivot along (dA, db, dc) at the given base (one LU)."""
    n = Abase.rows
    u = mp.lu_solve(Abase, bbase)
    dAu = dA * u
    r = mp.lu_solve(Abase, db)
    m_ = mp.lu_solve(Abase, dAu)
    dAm = dA * m_
    dAr = dA * r
    phi0 = cbase - dot(bbase, u, n)
    phi1 = dc - 2 * dot(db, u, n) + dot(u, dAu, n)
    phi2 = -(dot(r, db, n) - 2 * dot(r, dAu, n) + dot(m_, dAu, n))
    phi3 = -2 * dot(r, dAm, n) + dot(r, dAr, n) + dot(m_, dAm, n)
    return phi0, phi1, phi2, phi3, u


def phi3_only(Abase, u, dA, db, dc):
    n = Abase.rows
    dAu = dA * u
    r = mp.lu_solve(Abase, db)
    m_ = mp.lu_solve(Abase, dAu)
    return -2 * dot(r, dA * m_, n) + dot(r, dA * r, n) + dot(m_, dA * m_, n)


def direct_pivot(K, dim, which):
    A, b, c = channel_parts(K, dim, which)
    sol = mp.lu_solve(A, b)
    return c - dot(b, sol, b.rows)


def g3_of(phi):
    p1, p2, p3 = phi[1], phi[2], phi[3]
    return float(p3 * p1 / p2**2) if p2 != 0 else float("nan")


CHANNELS = ("odd", "even", "seam")


# ---------------------------------------------------------------- W0c: algebra unit test
def algebra_unit_test():
    mp.mp.dps = 60
    rng = np.random.default_rng(7)
    n = 6
    Araw = rng.uniform(-1, 1, (n, n))
    A0 = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            A0[i, j] = mp.mpf(repr(float((Araw[i, j] + Araw[j, i]) / 2 + (8.0 if i == j else 0.0))))
    b0 = mp.matrix([mp.mpf(repr(float(x))) for x in rng.uniform(-1, 1, n)])
    c0 = mp.mpf("5.0")
    dAr = rng.uniform(-1, 1, (n, n))
    dA = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            dA[i, j] = mp.mpf(repr(float((dAr[i, j] + dAr[j, i]) / 2)))
    db = mp.matrix([mp.mpf(repr(float(x))) for x in rng.uniform(-1, 1, n)])
    dc = mp.mpf("0.37")

    def dval(t):
        At = A0 + t * dA
        bt = b0 + t * db
        sol = mp.lu_solve(At, bt)
        return (c0 + t * dc) - dot(bt, sol, n)

    h = mp.mpf("1e-10")
    d0_, dp, dm, dp2, dm2 = dval(0), dval(h), dval(-h), dval(2 * h), dval(-2 * h)
    f1 = (8 * (dp - dm) - (dp2 - dm2)) / (12 * h)
    f2 = (16 * (dp + dm - 2 * d0_) - (dp2 + dm2 - 2 * d0_)) / (24 * h**2)
    f3 = ((dp2 - dm2) - 2 * (dp - dm)) / (12 * h**3)
    p0, p1, p2, p3, _ = phi_expand(A0, b0, c0, dA, db, dc)
    errs = [float(abs(p1 - f1) / abs(f1)), float(abs(p2 - f2) / abs(f2)),
            float(abs(p3 - f3) / abs(f3))]
    mp.mp.dps = DPS
    return errs


# ---------------------------------------------------------------- per-window machinery
def build_window(lam, Np=None, dps=None):
    """Returns dict with K_true, dK, K_mixed, band data, on the lam'-frame."""
    if dps:
        mp.mp.dps = dps
    lam_mp = mp.mpf(repr(lam))
    lam2 = lam_mp**2
    lamp = mp.sqrt(lam2 + 1)
    Lp = 2 * mp.log(lamp)
    if Np is None:
        Np = int(round(float(24 / (2 * mp.log(2)) * Lp)))
    dim = 2 * Np + 1
    lo, hi = lam2 - 1, lam2                     # the CROSSOVER band (SMK-1)
    a_lo, a_hi = mp.log(lo), mp.log(hi)
    atoms = band_atoms(lo, hi)
    Qt, _, _ = build_QW_mode(lamp, Np, "true")
    K_true = to_point(Qt, Np)
    KA = to_point(atoms_blk_Q(Lp, Np, atoms), Np)
    KS = to_point(density_blk_Q(Lp, Np, lambda u: mp.exp(u / 2), a_lo, a_hi, 8), Np)
    dK = KS - KA
    return dict(lam=lam, lamp=lamp, Lp=Lp, L_lo=a_lo, L_hi=a_hi, Np=Np, dim=dim,
                atoms=atoms, K_true=K_true, KA=KA, KS=KS, dK=dK,
                am=float(mp.fsum(w_ for _, w_ in atoms)) if atoms else 0.0,
                sm=float(2 * (mp.sqrt(hi) - mp.sqrt(lo))))


def window_phis(K_true, dK, dim):
    out = {}
    K_mixed = K_true - dK
    for ch in CHANNELS:
        At, bt, ct = channel_parts(K_true, dim, ch)
        dA, db, dc = channel_parts(dK, dim, ch)
        p0, p1, p2, p3, u = phi_expand(At, bt, ct, dA, db, dc)
        d_mix = direct_pivot(K_mixed, dim, ch)
        out[ch] = dict(phi=(p0, p1, p2, p3), u=u, At=At,
                       d_true=p0, d_mix=d_mix)
    return out, K_mixed


# ---------------------------------------------------------------- main sweep
CASES = [1.8, 2.0, 2.2, 2.35, 2.5]
if SMOKE:
    CASES = [2.0]

print(f"== P-inf-G round 2: per-arrival cubic, crossover band, chiral block (dps={DPS}) ==")
print("   frame: lam'-grid; base = TRUE kernel (germ); band = (lam^2-1, lam^2]\n")

ut = algebra_unit_test()
w0c = all(e <= 1e-8 for e in ut)
print(f"   W0c algebra unit test (phi1/2/3 vs Richardson): {ut[0]:.1e} {ut[1]:.1e} {ut[2]:.1e}"
      + ("   SURVIVES" if w0c else "   FIRED -- formula bug, HALT"))
if not w0c:
    sys.exit(1)

RES = {}
for lam in CASES:
    t0 = time.time()
    W = build_window(lam, Np=(12 if SMOKE else None))
    dim = W["dim"]
    psd_true = cholesky_psd(W["K_true"])
    def_true, def_dK = refl_defect(W["K_true"], dim), refl_defect(W["dK"], dim)
    ph, K_mixed = window_phis(W["K_true"], W["dK"], dim)
    psd_mixed = cholesky_psd(K_mixed)
    fme = fmin_eig(K_mixed, dim)
    attr = {}
    if W["atoms"]:
        for ch in ("odd", "seam"):
            At, u = ph[ch]["At"], ph[ch]["u"]
            Da = -W["KA"]
            Ds = W["KS"]
            Da_A, Da_b, Da_c = channel_parts(Da, dim, ch)
            Ds_A, Ds_b, Ds_c = channel_parts(Ds, dim, ch)
            f10 = phi3_only(At, u, Da_A, Da_b, Da_c)
            f01 = phi3_only(At, u, Ds_A, Ds_b, Ds_c)
            f11 = phi3_only(At, u, Da_A + Ds_A, Da_b + Ds_b, Da_c + Ds_c)
            f1m = phi3_only(At, u, Da_A - Ds_A, Da_b - Ds_b, Da_c - Ds_c)
            c30, c03 = f10, f01
            c21 = (f11 - f1m) / 2 - c03
            c12 = (f11 + f1m) / 2 - c30
            ident = float(abs(f11 - ph[ch]["phi"][3]) / max(abs(f11), mp.mpf("1e-80")))
            attr[ch] = dict(c30=float(c30), c21=float(c21), c12=float(c12),
                            c03=float(c03), ident=ident)
    Rseam = float(ph["seam"]["d_true"] / W["K_true"][0, 0])
    RES[lam] = dict(W=W, dim=dim, lamp=float(W["lamp"]), am=W["am"], sm=W["sm"],
                    fluc=W["am"] - W["sm"],
                    psd_true=psd_true, psd_mixed=psd_mixed, fme_mixed=fme,
                    def_true=def_true, def_dK=def_dK,
                    ph={ch: dict(phi=[float(x) for x in ph[ch]["phi"]],
                                 d_true=float(ph[ch]["d_true"]),
                                 d_mix=float(ph[ch]["d_mix"]),
                                 g3=g3_of([float(x) for x in ph[ch]["phi"]]))
                        for ch in CHANNELS},
                    attr=attr, Rseam=Rseam)
    el = time.time() - t0
    a_str = (f"n={int(round(float(mp.e**W['atoms'][0][0])))}" if W["atoms"] else "NONE (composite)")
    print(f"   lam={lam} -> lam'={float(W['lamp']):.5f} (dim={dim}, {el:.0f}s): band atom {a_str}, "
          f"psi-fluc={RES[lam]['fluc']:+.4f}")
    print(f"      PSD: true={'OK' if psd_true else 'FAIL!'} mixed={'OK' if psd_mixed else 'NON-PSD'}"
          f" (float min-eig {fme:+.2e})  refl: K={def_true:.1e} dK={def_dK:.1e}")
    for ch in CHANNELS:
        r = RES[lam]["ph"][ch]
        print(f"      {ch:5}: d(1)={r['d_true']:+.4e}  d(0)={r['d_mix']:+.4e}  "
              f"phi1={r['phi'][1]:+.3e} phi2={r['phi'][2]:+.3e} phi3={r['phi'][3]:+.3e} "
              f"g3={r['g3']:+.4f}")

if SMOKE:
    a = RES[CASES[0]]["attr"].get("odd")
    if a:
        print(f"\n   smoke attribution(odd): c30={a['c30']:+.3e} c21={a['c21']:+.3e} "
              f"c12={a['c12']:+.3e} c03={a['c03']:+.3e} ident={a['ident']:.1e}")
    print("\nSMOKE OK")
    sys.exit(0)

# ---------------------------------------------------------------- lineage anchor
print("\n== lineage anchor: certified lam=2.5 window rebuilt at dps 65 ==")
t0 = time.time()
Qa, _, _ = build_QW_mode(mp.mpf("2.5"), 32, "true")
Ka = to_point(Qa, 32)
Ra = float(direct_pivot(Ka, 65, "seam") / Ka[0, 0])
print(f"   R_seam(2.5) = {Ra:.5f} vs certified 0.09216  "
      + ("ok" if abs(Ra - 0.09216) < 1e-3 else "MISS -- lineage broken") + f" ({time.time()-t0:.0f}s)")

# ---------------------------------------------------------------- the gate
print("\n== GATE: off-line deformation response (the non-circularity audit) ==")
GATE_LAMS = [2.0, 2.5]
DELTAS = ["0.1", "0.2", "0.3"]
GAMMA2 = GAMMA1 + 1

gate = {}
for lam in GATE_LAMS:
    W = RES[lam]["W"]
    dim, Np, Lp = RES[lam]["dim"], W["Np"], W["Lp"]
    K_true, dK = W["K_true"], W["dK"]
    base = {}
    for ch in ("odd", "seam"):
        At, bt, ct = channel_parts(K_true, dim, ch)
        dA, db, dc = channel_parts(dK, dim, ch)
        p0, p1, p2, p3, _ = phi_expand(At, bt, ct, dA, db, dc)
        base[ch] = (p0, p1, p2, p3)
    gate[lam] = dict(base={ch: [float(x) for x in base[ch]] for ch in ("odd", "seam")},
                     defs={})
    fro_ref = None
    for tag in DELTAS + ["ctrl"]:
        t0 = time.time()
        if tag == "ctrl":
            dens = lambda u: -2 * (mp.cos(GAMMA2 * u) - mp.cos(GAMMA1 * u))
        else:
            dlt = mp.mpf(tag)
            dens = lambda u, d=dlt: -4 * (mp.cosh(d * u) - 1) * mp.cos(GAMMA1 * u)
        Pfull = to_point(density_blk_Q(Lp, Np, dens, mp.mpf(0), Lp, 28), Np)
        Pinc = to_point(density_blk_Q(Lp, Np, dens, W["L_lo"], W["L_hi"], 8), Np)
        fro = mp.sqrt(mp.fsum(Pfull[i, j]**2 for i in range(dim) for j in range(dim)))
        if tag == "0.2":
            fro_ref = fro
        if tag == "ctrl":
            scale = fro_ref / fro
            Pfull, Pinc = scale * Pfull, scale * Pinc
            fro = fro_ref
        K_def = K_true - Pfull
        dK_def = dK - Pinc
        psd_def = cholesky_psd(K_def)
        row = dict(fro=float(fro), psd=psd_def)
        for ch in ("odd", "seam"):
            At, bt, ct = channel_parts(K_def, dim, ch)
            dA, db, dc = channel_parts(dK_def, dim, ch)
            p0, p1, p2, p3, _ = phi_expand(At, bt, ct, dA, db, dc)
            g3d = g3_of([float(p0), float(p1), float(p2), float(p3)])
            g3b = g3_of([float(x) for x in base[ch]])
            row[ch] = dict(phi3=float(p3), resp=float(p3 - base[ch][3]),
                           g3=g3d, g3resp=g3d - g3b, d_true=float(p0))
        gate[lam]["defs"][tag] = row
        print(f"   lam={lam} {('off d=' + tag) if tag != 'ctrl' else 'ON-LINE ctrl'}: "
              f"fro={row['fro']:.3e} PSD={'OK' if psd_def else 'NON-PSD'} | "
              f"odd: resp={row['odd']['resp']:+.3e} g3resp={row['odd']['g3resp']:+.4f} | "
              f"seam: resp={row['seam']['resp']:+.3e} g3resp={row['seam']['g3resp']:+.4f}"
              f"  ({time.time()-t0:.0f}s)")

# ---------------------------------------------------------------- jitter floor
print("\n== jitter floor (dps 50 rerun, lam=2.0 incl. off d=0.2) ==")
mp.mp.dps = 50
lam = 2.0
W50 = build_window(lam, Np=RES[lam]["W"]["Np"])
dim = W50["dim"]
jit, jit_g = {}, {}
for ch in ("odd", "seam"):
    At, bt, ct = channel_parts(W50["K_true"], dim, ch)
    dA, db, dc = channel_parts(W50["dK"], dim, ch)
    _, p1, p2, p3, _ = phi_expand(At, bt, ct, dA, db, dc)
    jit[ch] = abs(float(p3) - RES[lam]["ph"][ch]["phi"][3])
    jit_g[ch] = abs(g3_of([0, float(p1), float(p2), float(p3)]) - RES[lam]["ph"][ch]["g3"])
dlt = mp.mpf("0.2")
dens = lambda u: -4 * (mp.cosh(dlt * u) - 1) * mp.cos(GAMMA1 * u)
Pfull = to_point(density_blk_Q(W50["Lp"], W50["Np"], dens, mp.mpf(0), W50["Lp"], 28), W50["Np"])
Pinc = to_point(density_blk_Q(W50["Lp"], W50["Np"], dens, W50["L_lo"], W50["L_hi"], 8), W50["Np"])
K_def50, dK_def50 = W50["K_true"] - Pfull, W50["dK"] - Pinc
jd, jd_g = {}, {}
for ch in ("odd", "seam"):
    At, bt, ct = channel_parts(K_def50, dim, ch)
    dA, db, dc = channel_parts(dK_def50, dim, ch)
    _, p1, p2, p3, _ = phi_expand(At, bt, ct, dA, db, dc)
    jd[ch] = abs(float(p3) - gate[2.0]["defs"]["0.2"][ch]["phi3"])
    jd_g[ch] = abs(g3_of([0, float(p1), float(p2), float(p3)]) - gate[2.0]["defs"]["0.2"][ch]["g3"])
J = max(max(jit.values()), max(jd.values()))
Jg = max(max(jit_g.values()), max(jd_g.values()))
print(f"   phi3 jitter: clean odd={jit['odd']:.2e} seam={jit['seam']:.2e}; "
      f"deformed odd={jd['odd']:.2e} seam={jd['seam']:.2e}  ->  J = {J:.2e}")
print(f"   g3 jitter:   clean odd={jit_g['odd']:.2e} seam={jit_g['seam']:.2e}; "
      f"deformed odd={jd_g['odd']:.2e} seam={jd_g['seam']:.2e}  ->  J_g = {Jg:.2e}")
mp.mp.dps = DPS

# ---------------------------------------------------------------- verdicts
print("\n== W0: instrument validity ==")
w0a = all(RES[l]["psd_true"] for l in CASES)
w0b = all(max(RES[l]["def_true"], RES[l]["def_dK"]) <= 1e-30 for l in CASES)
print("   W0a true-base PSD at all windows: " + ("SURVIVES" if w0a else "FIRED -- HALT"))
print(f"   W0b reflection defects: max = "
      f"{max(max(RES[l]['def_true'], RES[l]['def_dK']) for l in CASES):.1e}"
      + ("   SURVIVES" if w0b else "   FIRED -- HALT"))
print("   W0d mixed-base cone status: " + "  ".join(
    f"{l}:{'PSD' if RES[l]['psd_mixed'] else 'NON-PSD'}({RES[l]['fme_mixed']:+.1e})"
    for l in CASES))
print("   W0e radius readings (d_minus): " + "  ".join(
    f"{l}:|p2/p1|={abs(RES[l]['ph']['odd']['phi'][2]/RES[l]['ph']['odd']['phi'][1]):.1e}"
    for l in CASES))

print("\n== GATE-A / A' (headline): is the cubic blind to zero displacement? ==")
blind_raw, blind_g3 = True, True
for lam in GATE_LAMS:
    rmax = max(abs(gate[lam]["defs"][d]["odd"]["resp"]) for d in DELTAS)
    gmax = max(abs(gate[lam]["defs"][d]["odd"]["g3resp"]) for d in DELTAS)
    fr, fg = rmax <= 10 * J, gmax <= 10 * Jg
    blind_raw &= fr
    blind_g3 &= fg
    print(f"   lam={lam}: max|resp phi3| = {rmax:.3e} vs 10J = {10*J:.2e} "
          f"({'blind' if fr else 'responds'});  max|resp g3| = {gmax:.3e} vs 10Jg = {10*Jg:.2e} "
          f"({'blind' if fg else 'responds'})")
if blind_raw and blind_g3:
    print("   GATE-A: FIRED -- the cubic is VACUOUS at certified windows (circular route)")
elif blind_g3:
    print("   GATE-A': g3 BLIND while raw phi3 responds -- LEAK NAMED: the deformation is "
          "read only through the order-2 resolvent/ladder channel; the shape-level cubic "
          "consumes no zero-position input at these windows")
else:
    print("   GATE-A/A': SURVIVES -- the normalized cubic responds to zero displacement")

print("\n== GATE-B / B': specificity (off-line vs matched on-line) ==")
for lam in GATE_LAMS:
    for obj, key in (("phi3", "resp"), ("g3", "g3resp")):
        off = abs(gate[lam]["defs"]["0.2"]["odd"][key])
        ctl = abs(gate[lam]["defs"]["ctrl"]["odd"][key])
        R = off / ctl if ctl > 0 else float("inf")
        print(f"   lam={lam} {obj:4}: |off 0.2| = {off:.3e}  |ctrl| = {ctl:.3e}  "
              f"R_spec = {R:.2f}  ({'OFF-LINE-specific' if R > 3 else 'generic'})")

print("\n== S1/S2: the oriented cubic across the sweep (d_minus channel) ==")
ABEAR = [l for l in CASES if RES[l]["W"]["atoms"]]
print("   lam   fluc     phi1(d-)      phi3(d-)      phi3/phi1    |phi3|/|phi2|   g3        phi3*lam'^2")
orient, ratios32 = [], []
for l in CASES:
    r = RES[l]["ph"]["odd"]["phi"]
    o = r[3] / r[1] if r[1] != 0 else float("nan")
    rat = abs(r[3]) / abs(r[2]) if r[2] != 0 else float("inf")
    if l in ABEAR:
        orient.append(np.sign(o))
        ratios32.append(rat)
    print(f"   {l:4} {RES[l]['fluc']:+.3f}  {r[1]:+.5e}  {r[3]:+.5e}  {o:+.3e}  "
          f"{rat:.3e}   {RES[l]['ph']['odd']['g3']:+.4f}  {r[3]*RES[l]['lamp']**2:+.4e}")
s1 = len(set(orient)) == 1
mono_fall = (all(b < a for a, b in zip(ratios32, ratios32[1:]))
             and ratios32[-1] <= ratios32[0] / 10)
s2 = not mono_fall
print("   S1 (oriented sign, atom-bearing): " + ("constant" if s1 else "NOT constant")
      + "   S2 (|phi3/phi2| collapse x10): " + ("no collapse" if s2 else "COLLAPSED"))

print("\n== S3: diagonal-triple attribution (atom-bearing windows) ==")
for l in CASES:
    if not RES[l]["attr"]:
        print(f"   lam={l}: composite step (no atom) -- pure-smooth control")
        continue
    for ch in ("odd", "seam"):
        a = RES[l]["attr"][ch]
        tot = abs(a["c30"]) + abs(a["c21"]) + abs(a["c12"]) + abs(a["c03"])
        print(f"   lam={l} {ch:5}: c30={a['c30']:+.3e} c21={a['c21']:+.3e} "
              f"c12={a['c12']:+.3e} c03={a['c03']:+.3e}  aaa-share={abs(a['c30'])/tot:.3f}"
              f"  [ident {a['ident']:.1e}]")

print("\n== S5: free ladder check (R_seam at the lam' windows vs p=3.2 band) ==")
cert = {1.5: 0.4956, 1.8: 0.2884, 2.0: 0.2064, 2.2: 0.1496, 2.35: 0.1130, 2.5: 0.0922, 3.0: 0.0576}
lx = np.log(np.array(sorted(cert)))
ly = np.log(np.array([cert[k] for k in sorted(cert)]))
co = np.polyfit(2 * lx, ly, 1)
print(f"   certified-series p (refit) = {-co[0]:.2f}")
for l in CASES:
    lp = RES[l]["lamp"]
    pred = float(np.exp(np.polyval(co, 2 * np.log(lp))))
    dev = (RES[l]["Rseam"] - pred) / pred
    print(f"   lam'={lp:.4f}: R_seam = {RES[l]['Rseam']:.5f}  power-law pred = {pred:.5f}  "
          f"dev = {dev:+.1%}")

print("\n== S6: the resummed per-arrival push (exact endpoints; (U)-grade reading) ==")
print("   lam    ch     d_true        d_mixed       d_true/d_mixed")
for l in CASES:
    for ch in CHANNELS:
        r = RES[l]["ph"][ch]
        rt = r["d_true"] / r["d_mix"] if r["d_mix"] != 0 else float("nan")
        print(f"   {l:4}  {ch:5}  {r['d_true']:+.4e}  {r['d_mix']:+.4e}  {rt:+.4e}")

np.savez(HERE + "pinfG_cubic_drift_v2.npz",
         lams=np.array(CASES),
         lamps=np.array([RES[l]["lamp"] for l in CASES]),
         fluc=np.array([RES[l]["fluc"] for l in CASES]),
         phi_odd=np.array([RES[l]["ph"]["odd"]["phi"] for l in CASES]),
         phi_even=np.array([RES[l]["ph"]["even"]["phi"] for l in CASES]),
         phi_seam=np.array([RES[l]["ph"]["seam"]["phi"] for l in CASES]),
         g3_odd=np.array([RES[l]["ph"]["odd"]["g3"] for l in CASES]),
         d_true=np.array([[RES[l]["ph"][ch]["d_true"] for ch in CHANNELS] for l in CASES]),
         d_mix=np.array([[RES[l]["ph"][ch]["d_mix"] for ch in CHANNELS] for l in CASES]),
         psd_mixed=np.array([RES[l]["psd_mixed"] for l in CASES]),
         fme_mixed=np.array([RES[l]["fme_mixed"] for l in CASES]),
         Rseam=np.array([RES[l]["Rseam"] for l in CASES]),
         gate_lams=np.array(GATE_LAMS),
         gate_resp_odd=np.array([[gate[l]["defs"][d]["odd"]["resp"] for d in DELTAS + ["ctrl"]]
                                 for l in GATE_LAMS]),
         gate_g3resp_odd=np.array([[gate[l]["defs"][d]["odd"]["g3resp"] for d in DELTAS + ["ctrl"]]
                                   for l in GATE_LAMS]),
         gate_resp_seam=np.array([[gate[l]["defs"][d]["seam"]["resp"] for d in DELTAS + ["ctrl"]]
                                  for l in GATE_LAMS]),
         gate_psd=np.array([[gate[l]["defs"][d]["psd"] for d in DELTAS + ["ctrl"]]
                            for l in GATE_LAMS]),
         jitter=np.array([J, Jg]))
print("\nARCHIVED: pinfG_cubic_drift_v2.npz")

ok = w0a and w0b and w0c and not (blind_raw and blind_g3)
print("RESULT: " + ("GREEN -- instrument valid; gate verdicts and readings above"
                    if ok else "FIRED/PARTIAL -- see W0/GATE blocks (GPD: diagnose, retain)"))
