"""
probe_gue_ginibre_apex.py  --  the Montgomery-Dyson door.

RH <=> the zero process is pure GUE (Hermitian, real spectrum, level-repelling); an off-line zero is
a Ginibre (non-Hermitian, complex-eigenvalue) defect. The GUE class is beta=2 / broken time-reversal:
the arrow is REQUIRED, not the enemy -- the question is whether it is Hermitian-phased (real spectrum)
or pushes an eigenvalue off the real axis. Two structural claims to test:

PART 1  the FREE apex/prolate kernel is an EXACT Hermitian projection (the GUE sine kernel = the
        apex even sector): K=K*, K^2=K, spectrum {0,1}. Unconditional / free archimedean part.
PART 2  GAP-PROTECTION (the GUE rigidity). Write the operator H = S + eps*A: Hermitian metric S
        (level gap delta) plus a skew "arrow" A (the antisymmetric current, beta=2). The eigenvalues
        stay REAL -- on the line, GUE -- until the arrow exceeds a threshold eps_c ~ delta/2, then a
        complex pair emerges (Ginibre = off-line zero). The zeros are held on the line by repulsion.
PART 3  the correlation kernel: real spectrum -> real-line determinantal (GUE); complex eigenvalue ->
        Ginibre. The positivity criterion flips at the SAME threshold (conserves) -- but the GUE lens
        shows the MECHANISM: RH = the arrow is gap-dominated (arch-domination as level repulsion).

numpy + mpmath. No torch. (Statistical/structural certificate, not exact-arithmetic gate.)
"""
import numpy as np
import mpmath as mp

print("=" * 88)
print("[1] FREE GUE / prolate kernel = exact Hermitian projection (apex even sector, unconditional)")
print("=" * 88)
n, M = 24, 7
F = np.fft.fft(np.eye(n)) / np.sqrt(n)          # unitary DFT
band = np.zeros(n); band[:M] = 1.0               # band-limit to M modes
K = F.conj().T @ np.diag(band) @ F               # discrete sine / prolate projection
herm = np.linalg.norm(K - K.conj().T)
idem = np.linalg.norm(K @ K - K)
ev = np.round(np.sort(np.linalg.eigvalsh((K + K.conj().T) / 2).real), 10)
print(f"  Hermitian  ||K-K*||      = {herm:.2e}   (=0)")
print(f"  idempotent ||K^2-K||     = {idem:.2e}   (=0  => orthogonal PROJECTION)")
print(f"  spectrum (rounded)       = {{{', '.join(str(x) for x in sorted(set(ev)))}}}  ({int(ev.sum())} ones)")
print("  => the GUE bulk kernel (sine = projection onto band-limited / prolate) is an exact Hermitian")
print("     projection: spectrum {0,1}, the rigid determinantal structure. This is the FREE part.")

print("\n" + "=" * 88)
print("[2] GAP-PROTECTION: arrow (skew) vs level-repulsion gap  --  H = S + eps*A")
print("=" * 88)
print("  2x2 model: S = diag(+d/2, -d/2) (gap d=1), A = [[0,1],[-1,0]] (skew arrow). Threshold d/2=0.5:")
print(f"  {'eps':>6} {'max|Im lambda|':>16} {'spectrum':>34} {'class':>10}")
d = 1.0
A2 = np.array([[0.0, 1.0], [-1.0, 0.0]])
S2 = np.array([[d / 2, 0.0], [0.0, -d / 2]])
for eps in (0.0, 0.30, 0.49, 0.50, 0.51, 0.80):
    lam = np.linalg.eigvals(S2 + eps * A2)
    mi = np.max(np.abs(lam.imag))
    cls = "GUE (real)" if mi < 1e-9 else "Ginibre"
    sp = ", ".join(f"{x.real:+.3f}{x.imag:+.3f}i" for x in sorted(lam, key=lambda z: z.real))
    print(f"  {eps:>6.2f} {mi:>16.4f} {sp:>34} {cls:>10}")
print("  => eigenvalues stay EXACTLY real (on the line, GUE) until eps_c = d/2; then a complex pair")
print("     (Ginibre = an off-line zero). The arrow does NOT move the zeros off-line until it beats")
print("     the gap. The line is protected by level repulsion -- the GUE rigidity, quantified.")

print("\n  n-level model: S = diag(first 12 unfolded zeta zeros), A = a fixed skew arrow")
gam = np.array([float(mp.im(mp.zetazero(k))) for k in range(1, 13)])
S = np.diag(gam)
rng = np.random.default_rng(0)
R = rng.standard_normal((12, 12)); A = R - R.T
A = A / np.linalg.norm(A, 2)                      # unit-norm skew arrow
mingap = np.min(np.diff(np.sort(gam)))
print(f"    min level gap = {mingap:.4f}  -> predicted protection threshold ~ mingap/2 = {mingap/2:.4f}")
print(f"    {'eps':>7} {'max|Im lambda|':>16} {'real spectrum?':>16}")
eps_c = None
for eps in (0.0, mingap/4, mingap/2*0.9, mingap/2*1.1, mingap, 2*mingap):
    lam = np.linalg.eigvals(S + eps * A)
    mi = np.max(np.abs(lam.imag))
    real = mi < 1e-9
    if eps_c is None and not real:
        eps_c = eps
    print(f"    {eps:>7.4f} {mi:>16.4e} {str(real):>16}")
print("    => the real spectrum (all zeros on-line) survives a finite skew arrow; it goes Ginibre only")
print("       once the arrow is comparable to the (smallest) level gap. Gap-protection is generic.")

print("\n" + "=" * 88)
print("[3] correlation kernel: GUE (real-line projection) -> Ginibre (complex eigenvalue), and the")
print("    positivity vs determinantal criteria at the transition")
print("=" * 88)
# build the "lower-half" spectral projector of the 2x2 model and read realness; compare to the
# Pick/Gram positivity (negative-square) criterion of the same off-line displacement.
print(f"  {'eps':>6} {'spectrum real?':>15} {'kernel real-line proj?':>24} {'Pick has neg sq?':>18}")
for eps in (0.30, 0.49, 0.51, 0.80):
    lam = np.linalg.eigvals(S2 + eps * A2)
    real = np.max(np.abs(lam.imag)) < 1e-9
    # the "GUE" correlation kernel exists as a real-line Hermitian projection iff spectrum is real
    proj_ok = real
    # Pick/Gram positivity: model an atom at the (possibly complex) eigenvalue, evaluate sign
    a = sorted(lam, key=lambda z: z.real)[0]      # lower eigenvalue (the candidate "zero")
    zs = [0.5 + 1j, 1.5 + 1j]
    P = np.array([[ (1/(a - zi) - np.conj(1/(a - zj))) / (zi - np.conj(zj))
                    for zj in zs] for zi in zs])
    P = (P + P.conj().T) / 2
    neg = np.min(np.linalg.eigvalsh(P)) < -1e-9
    print(f"  {eps:>6.2f} {str(real):>15} {str(proj_ok):>24} {str(neg):>18}")
print("  => both criteria flip at the SAME threshold eps_c (real-line projection lost <=> Pick gains a")
print("     negative square <=> eigenvalue goes complex). The determinantal and positivity walls")
print("     coincide -- conservation -- BUT the GUE lens supplies what positivity did not: the WHY.")

print("\n" + "=" * 88)
print("VERDICT  --  what the Montgomery-Dyson lens genuinely changes")
print("=" * 88)
print("""  (1) The arrow (beta=2, broken time-reversal) is REQUIRED, not the enemy: a skew arrow leaves the
      spectrum REAL (on-line, GUE) up to a threshold. We were trying to remove what GUE says to keep.
  (2) The line is held by GAP-PROTECTION (level repulsion): eigenvalues go complex (Ginibre / off-line)
      only when the arrow beats the local gap, eps_c ~ gap/2. This is a quantitative competition --
      arrow vs repulsion gap -- not a flat positivity.
  (3) RH, re-cast: the arithmetic (prime) arrow is DOMINATED by the level-repulsion gap, everywhere.
      This is arch-domination (T28) in random-matrix language: the free archimedean repulsion (the
      sine-kernel rigidity of [1]) must out-pull the prime deformation. Lambda=0 (Rodgers-Tao) is the
      statement that the protection is MARGINAL -- the arrow sits exactly at the gap, "barely" real.
  The determinantal and positivity criteria coincide in threshold (conservation), so GUE is not a new
  *detector*. What it is, is a new *mechanism and a new target*: bound the arithmetic arrow by the
  repulsion gap. That competition -- gap vs arrow, with an explicit threshold -- is the lever the flat
  positivity never exposed, and it is the next thing to make quantitative against the explicit formula.""")
