"""
*** CORRECTION 2026-06-08 (read first). The "chiral handle" interpretation below was WITHDRAWN
*** after a paranoid audit (probe_obligation73_chirality_audit.py): J = B - B^T is built from
*** B = |U_p|^2 and is therefore PHASE-BLIND and STATE-INDEPENDENT -- it is NONZERO at the vacuum
*** where the true arrow vanishes, so it is NOT the chiral / L(.,chi_3) current. The genuine chiral
*** content is the state-dependent PHASE C(rho)=Im(rho_chi). What this script certifies is still
*** TRUE -- the transpose-asymmetry / conveyor non-normality of |U_p|^2 -- but its RH/chiral
*** interpretation in the text below is RETRACTED (see N14 sec 7.5 Rem 7.8). Kept as a record. ***

N14 sec 7.5 certificate (Vector A) -- the chiral handle: the apex channel's irreversible
current J = B - B^T, the object Theorem 7.6(ii) proved the symmetric defect is blind to.

Background (N14 sec 7.4, Thm 7.6). The apex pinching channel Phi_p delivers the even/metric
coarse-graining defect S(Bp)-S(p) >= 0 (B = |U_p|^2 doubly stochastic) but is BLIND to the
odd/chiral L(.,chi_3) sector, because that defect is built from |U_p|^2 alone (a symmetric,
self-adjoint instrument). This certificate exhibits the discarded chiral content explicitly:
it lives in the ANTISYMMETRIC part of the transition, the probability current

      J := B - B^T   (detailed-balance defect of B w.r.t. the uniform vacuum).

Certified claims (exact, mpmath dps=40), p in {3,5,7,11,13}:

  A1  INTRINSIC NON-NORMAL CURRENT.  J != 0 for p>=5 (J == 0 at p=3, the degenerate
      reversible 2x2 case).  B has REAL spectrum (Im lambda = 0) -> the irreversibility is
      CONVEYOR type (E10: left != right singular charts), not DRIFT-RING type (E9: Im lambda).
      The conveyor / departure-from-normality gap  G_p = sum sigma(B) - sum |lambda(B)| > 0
      and is MONOTONE INCREASING in p.

  A2  CHIRAL PARITY.  Under the character parity R: c -> -c (= complex conjugation chi_c->chi_{-c},
      the parity separating even zeta from odd L(.,chi_3)), the current J is ODD: in the orthogonal
      Frobenius split ||J||^2 = ||J_odd||^2 + ||J_even||^2, the ODD ENERGY fraction is >= 99% for all
      p (exact 100% at p=3,5). A small even component appears for p>=7 and grows slowly with p
      (even energy 0.19%, 0.57%, 0.74% at p=7,11,13) -- flagged, not yet attributed (candidate: the
      prime-power/ramp diagonal). => J is, to >=99% of its energy, the chiral / odd-character sector.

  A3  THE BLIND SPOT IS A ONE-OBSERVABLE FACT.  J antisymmetric => y^T J y = 0 for EVERY single
      real observable y: one symmetric instrument reads zero current (Thm 7.6(ii), exactly).
      A current needs a CYCLE (two observables): the flux Omega(y1,y2) = y1^T J y2 of the
      canonical time/frequency clock pair (cos, sin) is NONZERO with a CONSISTENT orientation
      (same sign) across all p>=5. This is the 2-encoder readout of the Irreversible Blind Spot.

Open (the honest residue, [C] = RH, deferred to Vector B / cross-prime): whether the per-prime
chiral flux / gap G_p continues across tau=1 to a definite-sign plateau. That continuation is RH.

No torch. mpmath only. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 40

TOL = mp.mpf(10) ** (-30)
GREEN = True

def fail(m):
    global GREEN
    GREEN = False
    print("   *** RED:", m)

def apex_unitary(p):
    w = mp.e ** (2j * mp.pi / p)
    N1 = p - 1
    U = mp.zeros(N1, N1)
    for k in range(1, p):
        Rk = 1 / mp.sqrt(p * k * (k + 1))
        for c in range(1, p):
            s = mp.fsum(w ** (c * j) for j in range(0, k)) - k * w ** (c * k)
            U[k - 1, c - 1] = Rk * s
    return U

def mod2_transition(U):
    N1 = U.rows
    B = mp.zeros(N1, N1)
    for k in range(N1):
        for c in range(N1):
            B[c, k] = abs(U[k, c]) ** 2
    return B

def fro(M):
    return mp.sqrt(mp.fsum(abs(M[i, j]) ** 2 for i in range(M.rows) for j in range(M.cols)))

def parity_perm(p):
    N1 = p - 1
    R = mp.zeros(N1, N1)
    for c in range(1, p):
        R[((-c) % p) - 1, c - 1] = 1
    return R

def singvals(B):
    N1 = B.rows
    H = B.T * B
    Hs = mp.matrix(N1, N1)
    for i in range(N1):
        for j in range(N1):
            Hs[i, j] = (mp.re(H[i, j]) + mp.re(H[j, i])) / 2
    return sorted((mp.sqrt(max(e, 0)) for e in mp.eigsy(Hs, eigvals_only=True)), reverse=True)

def centered(v):
    m = mp.fsum(v) / len(v)
    return [vi - m for vi in v]

def quad(y1, J, y2):
    N1 = J.rows
    return mp.fsum(y1[a] * mp.re(J[a, b]) * y2[b] for a in range(N1) for b in range(N1))

print("=" * 80)
print("N14 sec 7.5 (Vector A) -- the chiral handle: apex current J = B - B^T")
print("=" * 80)

prev_G = None
for p in (3, 5, 7, 11, 13):
    N1 = p - 1
    U = apex_unitary(p)
    B = mod2_transition(U)
    J = B - B.T
    nJ = fro(J)
    metric = fro(B - (B + B.T) / 2)  # = ||antisym|| actually; use metric scale ref:
    metric_scale = fro((B + B.T) / 2 - mp.eye(N1) * (mp.mpf(1) / N1))

    # A1: conveyor gap
    sig = singvals(B)
    E = mp.eig(B, left=False, right=False)
    Gp = mp.fsum(sig) - mp.fsum(abs(e) for e in E)
    imax = max(abs(mp.im(e)) for e in E)

    # A2: parity -- orthogonal Frobenius split, ODD energy fraction
    R = parity_perm(p)
    RJR = R * J * R
    Jeven = (J + RJR) / 2     # R-even part of J (the odd part is (J-RJR)/2)
    even_energy = (fro(Jeven) / nJ) ** 2 if nJ > TOL else mp.mpf(0)
    odd_energy = 1 - even_energy if nJ > TOL else mp.mpf(1)

    # A3: blind spot + clock flux
    yc = centered([mp.cos(2 * mp.pi * c / p) for c in range(1, p)])
    ys = centered([mp.sin(2 * mp.pi * c / p) for c in range(1, p)])
    self_flux = max(abs(quad(yc, J, yc)), abs(quad(ys, J, ys)))   # one-observable: must be 0
    clock_flux = quad(yc, J, ys)                                   # two-observable: nonzero, oriented

    print(f"\n--- p = {p}  (N'={N1}) ---")
    print(f"  A1  ||J|| = {mp.nstr(nJ,6)}  ({'== 0 reversible' if nJ<TOL else 'current present'});  "
          f"max|Im lambda(B)| = {mp.nstr(imax,3)} (conveyor)")
    print(f"      conveyor gap G_p = sum sigma - sum|lambda| = {mp.nstr(Gp,6)}  (>0 => non-normal)")
    print(f"  A2  ODD energy fraction of J = {mp.nstr(odd_energy,8)}  (even energy {mp.nstr(even_energy,4)})")
    print(f"  A3  one-observable flux y^T J y = {mp.nstr(self_flux,3)} (==0: blind);  "
          f"clock flux cos^T J sin = {mp.nstr(clock_flux,6)}")

    # assertions
    if p == 3:
        if nJ > TOL: fail("A1 p=3 should be reversible (J=0)")
    else:
        if nJ < TOL: fail(f"A1 p={p} current vanished")
        if Gp <= TOL: fail(f"A1 p={p} conveyor gap not positive")
        if prev_G is not None and Gp <= prev_G: fail(f"A1 gap not monotone at p={p}")
        prev_G = Gp
        if odd_energy < mp.mpf('0.98'): fail(f"A2 p={p} J not >=98% odd by energy ({mp.nstr(odd_energy,5)})")
        if abs(clock_flux) < TOL: fail(f"A3 p={p} clock flux vanished")
    if imax > mp.mpf('1e-30'): fail(f"A1 p={p} unexpected drift-ring (Im lambda != 0)")
    if self_flux > TOL: fail(f"A3 p={p} one-observable flux nonzero (should be exactly 0)")

# orientation consistency across p
print("\n" + "-" * 80)
fluxes = []
for p in (5, 7, 11, 13):
    U = apex_unitary(p); B = mod2_transition(U); J = B - B.T
    yc = centered([mp.cos(2 * mp.pi * c / p) for c in range(1, p)])
    ys = centered([mp.sin(2 * mp.pi * c / p) for c in range(1, p)])
    fluxes.append(quad(yc, J, ys))
signs = set(int(mp.sign(f)) for f in fluxes)
print(f"  clock-flux signs across p=5,7,11,13: {[int(mp.sign(f)) for f in fluxes]}  -> "
      f"{'CONSISTENT orientation' if len(signs)==1 else 'MIXED (no fixed arrow)'}")
if len(signs) != 1:
    fail("A3 clock-flux orientation not consistent across primes")

print("\n" + "=" * 80)
print("RESULT:", "GREEN -- all certified" if GREEN else "RED -- see failures above")
print("=" * 80)
print("""
Reading:
  The chiral content Thm 7.6(ii) called invisible is the antisymmetric current J = B - B^T,
  intrinsic to U_p. It is (i) a genuine NON-NORMAL conveyor (gap G_p>0, growing), (ii) ODD
  under the character parity c->-c (the even-zeta / odd-L(.,chi_3) split), and (iii) readable
  only by a TWO-observable flux (one symmetric instrument gives y^T J y == 0 exactly -- the
  blind spot, made quantitative). The clock flux has a fixed orientation across primes.
  RH-residue (deferred to Vector B): does the per-prime current continue across tau=1 to a
  definite-sign plateau.  [C]
""")
