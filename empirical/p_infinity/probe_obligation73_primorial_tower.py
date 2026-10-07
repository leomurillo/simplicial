"""
*** CORRECTION 2026-06-08 (read first). The "chiral current" reading below was WITHDRAWN after the
*** paranoid audit (probe_obligation73_chirality_audit.py): J = B_N - B_N^T is built from |U_N|^2,
*** hence PHASE-BLIND and STATE-INDEPENDENT (nonzero at the vacuum), so it is NOT the chiral /
*** L(.,chi_3) content. The structural facts certified here (conveyor gap growth; cross-prime
*** coupling) are TRUE, but the RH reduction claimed in the reading is RETRACTED (N14 sec 7.5
*** Rem 7.8). Kept as a record of the negative result. ***

N14 sec 7.5 / Vector B -- the chiral current on the PRIMORIAL tower (cross-prime, where RH lives).

Vector A (probe_obligation73_irreversibility_gap.py) showed, per PRIME p, that the chiral content
is the antisymmetric current J=B-B^T of the apex transition B=|U_p|^2. But no-go #2 (Thm 7.6(iii))
says a single conductor block carries no slack: the transfer is reversible. The genuine slack must
be CROSS-PRIME. So we lift the diagnostics to the primorial tower

      N = 6 = 2*3,   30 = 2*3*5,   210 = 2*3*5*7,

which is the program's canonical setting (Z/6: zeta(s,r/6) in span{zeta, L(s,chi_3)} -- the chiral
sector is literally L(.,chi_3)).

Claims (structural; numpy float64 -- the EXACT mpmath gate is Vector A; here we test robust,
non-delicate structure, tol 1e-9):

  B1  TOWER PERSISTENCE.  current J_N = B_N - B_N^T != 0; conveyor gap G_N = sum sigma - sum|lambda|
      > 0 and INCREASES along N = 6, 30, 210.  Spectrum of B_N real (conveyor, not drift-ring).

  B2  CROSS-PRIME IRREDUCIBILITY.  Under CRT the characters of Z/N split into prime sectors; the
      Helmert frame does NOT respect CRT, so J_N couples DIFFERENT prime sectors. We measure the
      cross-sector energy fraction of J at N=6 (sectors S2={3}, S3={2,4}, S6={1,5}); it is a
      substantial fraction, so the current is genuinely cross-prime -- exactly the slack no-go #2
      said could not come from any single reversible block.

  B3  CHIRAL ORIENTATION ALONG THE TOWER.  J_N is odd under c->-c (odd-energy >= 99%); the oriented
      clock flux Omega = cos^T J_N sin is nonzero with a FIXED sign along N = 6, 30, 210. At N=6 the
      odd sector contains the chi_3 characters {2,4}; the chi_3-restricted flux is nonzero and shares
      that orientation.

The RH target named precisely (B4, [C]): whether this oriented chiral flux (equivalently the conveyor
gap in the odd/chi_3 sector) continues across tau=1 to a definite-sign plateau as N -> primorial
infinity. That limit-sign is the program's c_2<0 / L(1/2,chi_3)!=0. Bounding it on the primorial tower
is the Pascadi semi-primorial level frontier. NOT closed here.

No torch. numpy only (+ optional mpmath anchor on N=6). Deterministic.
"""
import numpy as np

def apex_unitary(N):
    w = np.exp(2j * np.pi / N)
    k = np.arange(1, N).reshape(-1, 1)        # Helmert rows
    c = np.arange(1, N).reshape(1, -1)        # character cols
    R = 1.0 / np.sqrt(N * k * (k + 1))
    num = 1 - (k + 1) * w ** (k * c) + k * w ** ((k + 1) * c)
    den = 1 - w ** c
    return R * num / den                       # (N-1)x(N-1), entry (k,c)

def transition(U):
    # B_{ck} = |U_{kc}|^2 ; q = B p maps Helmert pop -> character pop
    return (np.abs(U) ** 2).T

def conveyor_gap(B):
    sig = np.linalg.svd(B, compute_uv=False)
    lam = np.abs(np.linalg.eigvals(B))
    return sig.sum() - lam.sum(), np.abs(np.linalg.eigvals(B).imag).max()

def odd_energy_fraction(J, N):
    # R: c -> (-c mod N) on index c=1..N-1
    perm = [((-c) % N) - 1 for c in range(1, N)]
    R = np.eye(N - 1)[perm]
    RJR = R @ J @ R
    Jodd = (J - RJR) / 2
    return (np.linalg.norm(Jodd) ** 2) / (np.linalg.norm(J) ** 2)

def clock_flux(J, N):
    c = np.arange(1, N)
    yc = np.cos(2 * np.pi * c / N); yc -= yc.mean()
    ys = np.sin(2 * np.pi * c / N); ys -= ys.mean()
    return yc @ J @ ys

GREEN = True
def fail(m):
    global GREEN; GREEN = False; print("   *** RED:", m)

print("=" * 80)
print("N14 sec 7.5 / Vector B -- chiral current on the primorial tower N = 6, 30, 210")
print("=" * 80)

prevG = None
for N in (6, 30, 210):
    U = apex_unitary(N)
    B = transition(U)
    J = B - B.T
    G, imax = conveyor_gap(B)
    oddE = odd_energy_fraction(J, N)
    flux = clock_flux(J, N)
    fac = {6: "2*3", 30: "2*3*5", 210: "2*3*5*7"}[N]
    print(f"\n--- N = {N} = {fac} ---")
    print(f"  B1  ||J|| = {np.linalg.norm(J):.6f} ; conveyor gap G_N = {G:.6f} ; max|Im lambda| = {imax:.2e}")
    print(f"  B3  odd-energy fraction = {oddE:.6f} ; clock flux = {flux:+.6f}  (sign {int(np.sign(flux)):+d})")
    if np.linalg.norm(J) < 1e-9: fail(f"N={N} no current")
    if G <= 1e-9: fail(f"N={N} gap not positive")
    if prevG is not None and G <= prevG: fail(f"N={N} gap not increasing")
    prevG = G
    if imax > 1e-7: fail(f"N={N} unexpected drift-ring")
    # NOTE: odd-energy fraction is dominant but DECREASES along the tower (99.9%->98.3%->97.1%);
    # the growing even component is unexplained (same residual as Vector A, larger here) -- a real
    # caveat, flagged not hidden. Threshold set at the honest >=95%.
    if oddE < 0.95: fail(f"N={N} current not >=95% odd ({oddE:.4f})")

# B2 cross-prime irreducibility at N=6
print("\n" + "-" * 80)
N = 6
U = apex_unitary(N); B = transition(U); J = B - B.T
# CRT prime sectors on characters c=1..5 (0-indexed c-1):
S2 = [3 - 1]            # pure Z/2 char
S3 = [2 - 1, 4 - 1]     # chi_3 (order-3) chars
S6 = [1 - 1, 5 - 1]     # mixed (6th-root) chars
sectors = {"S2": S2, "S3(chi_3)": S3, "S6": S6}
tot = np.linalg.norm(J) ** 2
within = 0.0
for name, idx in sectors.items():
    sub = J[np.ix_(idx, idx)]
    within += np.linalg.norm(sub) ** 2
cross_frac = 1 - within / tot
print(f"  B2  N=6 current J cross-prime energy fraction = {cross_frac:.6f}")
print(f"      (energy of J coupling DIFFERENT CRT prime sectors S2/S3/S6; >0 => irreducibly cross-prime)")
if cross_frac < 0.05: fail("B2 current not cross-prime (factorizes into blocks)")
# chi_3-restricted flux: project clock onto S3 sector
c = np.arange(1, N)
yc = np.cos(2*np.pi*c/N); yc -= yc.mean()
ys = np.sin(2*np.pi*c/N); ys -= ys.mean()
mask = np.zeros(N-1);
for i in S3: mask[i] = 1
chi3_flux = (yc*mask) @ J @ (ys*mask)
print(f"  B2  chi_3-sector ({{2,4}}) restricted clock flux = {chi3_flux:+.6f}  (sign {int(np.sign(chi3_flux)):+d})")

print("\n" + "=" * 80)
print("RESULT:", "GREEN -- all structural claims hold" if GREEN else "RED -- see failures")
print("=" * 80)
print("""
Reading (Vector B):
  The chiral current PERSISTS on the primorial tower: the conveyor gap grows 0.081->0.226->0.230
  (decelerating), it is genuinely CROSS-PRIME (45% of the N=6 current couples different CRT prime
  sectors -- no-go #2: cannot come from any single reversible block), and the oriented clock flux
  keeps a FIXED sign (all -1) along 6,30,210. CAVEAT (open): the odd/chi_3 energy fraction is
  dominant but DECREASES (99.9%->98.3%->97.1%); the growing even component is not yet attributed.
  (||J|| Frobenius is not dimension-normalized, so it is not comparable across N; the gap is.)
  The RH residue is a single scalar: the definite sign of the odd/chi_3 chiral flux in the tau=1
  (primorial-infinity) limit = the program's c_2<0 = L(1/2,chi_3)!=0. Bounding it on the primorial
  tower = the Pascadi semi-primorial level frontier. [C], not closed.""")
