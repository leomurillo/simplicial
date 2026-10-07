"""probe_krein_collision_spectral_flow.py — certificate for P-infinity-E SS14 (Theorem E.15).

The spectral-flow formulation of the F_q -> Q deformation, in three exact demonstrations:

CHECK A  (Pontryagin pinning, Pi_kappa): a J-self-adjoint matrix A = J H (H Hermitian) in
         Pi_1 has AT MOST ONE conjugate pair of non-real eigenvalues (20000 random samples,
         never 2); in Pi_2 up to two pairs occur.  Along continuous deformations in Pi_1
         with the "pole pair" occupying the slot, ALL other eigenvalues stay pinned to the
         real axis (2001-step paths) — real-eigenvalue collisions pass through, never leave.
CHECK B  (Honda-Tate boundary = Krein collision locus): on the rank-2 function-field carrier
         F = companion(lambda^2 - a*lambda + q), q = 9, the invariant-form equation
         F^H B F = q B has a POSITIVE-definite Hermitian solution iff |a| < 2 sqrt(q) = 6;
         at |a| = 6 the definite cone degenerates; for |a| > 6 EVERY invariant Hermitian
         form is hyperbolic (one negative square appears).  The eigenvalues leave |alpha| =
         sqrt(q) exactly there.  E.8's fake curve (a = 7) sits past the collision: its
         non-realizability as a curve = Krein instability of the deformation.
CHECK C  (index jump <=> form degeneracy): the definiteness witness w(a) = max over the
         invariant cone of the normalized minimal eigenvalue is positive for a < 6, crosses
         0 AT the collision a = 6, and is negative beyond — the index jumps exactly at the
         degeneracy point of the form, never elsewhere.

Deterministic (seeded), local, seconds.
"""
import sys
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
rng = np.random.default_rng(20260611)

# ---------------- CHECK A: Pontryagin pinning ----------------
print("== CHECK A: Pi_kappa pinning — non-real pairs <= kappa; Pi_1 paths stay pinned ==")
def rand_herm(n):
    X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (X + X.conj().T) / 2

def nonreal_pairs(A, tol=1e-9):
    ev = np.linalg.eigvals(A)
    return int(np.sum(np.abs(ev.imag) > tol * (1 + np.abs(ev)))) // 2

J1 = np.diag([-1.0, 1, 1, 1, 1, 1]); J2 = np.diag([-1.0, -1, 1, 1, 1, 1])
c1 = [nonreal_pairs(J1 @ rand_herm(6)) for _ in range(20000)]
c2 = [nonreal_pairs(J2 @ rand_herm(6)) for _ in range(20000)]
okA1 = max(c1) <= 1 and max(c2) <= 2 and (1 in c1) and (2 in c2)
print(f"   Pi_1: max non-real pairs over 20000 samples = {max(c1)} (theorem: <=1; freq of 1: "
      f"{100*np.mean(np.array(c1)==1):.1f}%)")
print(f"   Pi_2: max non-real pairs over 20000 samples = {max(c2)} (theorem: <=2; freq of 2: "
      f"{100*np.mean(np.array(c2)==2):.1f}%)")
viol = 0
for trial in range(40):
    H0, H1 = rand_herm(6), rand_herm(6)
    if nonreal_pairs(J1 @ H0) != 1:
        continue
    for tau in np.linspace(0, 1, 2001):
        if nonreal_pairs(J1 @ ((1 - tau) * H0 + tau * H1)) > 1:
            viol += 1
            break
okA = okA1 and viol == 0
print(f"   Pi_1 deformation paths (2001 steps x ~40): excursions above 1 pair = {viol}")
print("   " + ("PASS — with the pole pair holding Pi_1's single slot, every other eigenvalue "
               "is PINNED to the real axis along arbitrary deformations" if okA else "FAIL"))

# ---------------- CHECK B/C: Honda-Tate = Krein collision on the rank-2 carrier ----------------
print("\n== CHECK B/C: F^H B F = qB on companion(lambda^2 - a lambda + q), q=9 — sweep a ==")
q = 9.0
BASIS = [np.array([[1, 0], [0, 0]], complex), np.array([[0, 0], [0, 1]], complex),
         np.array([[0, 1], [1, 0]], complex) / np.sqrt(2),
         np.array([[0, -1j], [1j, 0]], complex) / np.sqrt(2)]

def coords(B):
    return np.array([np.real(np.trace(E.conj().T @ B)) for E in BASIS])

def witness(a):
    """max over the invariant Hermitian cone of min-eig(B)/||B||; nullspace dim."""
    F = np.array([[0, -q], [1, a]], complex)
    M = np.column_stack([coords(F.conj().T @ E @ F - q * E) for E in BASIS])
    _, s, Vt = np.linalg.svd(M)
    null = [sum(Vt[k, i] * BASIS[i] for i in range(4)) for k in range(4) if s[k] < 1e-9]
    if not null:
        return -np.inf, 0
    best = -np.inf
    for th in np.linspace(0, np.pi, 721):
        for sg in (1, -1):
            B = sg * (np.cos(th) * null[0] + (np.sin(th) * null[1] if len(null) > 1 else 0))
            nb = np.linalg.norm(B)
            if nb < 1e-12:
                continue
            best = max(best, float(np.min(np.linalg.eigvalsh(B / nb))))
    return best, len(null)

print("   a      |alpha|+-          nullspace  witness w(a)   regime")
okB = True
rows = []
for a in (0.0, 3.0, 5.0, 5.9, 6.0, 6.1, 7.0, 8.0):
    disc = a * a - 4 * q
    al = (a + np.sqrt(complex(disc))) / 2
    w, k = witness(a)
    rows.append((a, w))
    regime = ("on-circle, definite form exists" if a < 6 else
              "COLLISION (Jordan block)" if a == 6 else "off-circle, every form hyperbolic")
    print(f"   {a:4.1f}   |{abs(al):.4f}|,|{abs(q/al):.4f}|   dim={k}      {w:+.4f}        {regime}")
# the witness scales ~ (6 - a) near the collision (marginality), so the threshold must too
okB = (all(w > 1e-3 for a, w in rows if a < 6)
       and all(w < -1e-3 for a, w in rows if a > 6)
       and abs([w for a, w in rows if a == 6][0]) < 1e-3)
print("   fake curve of Thm E.8: a = 7 > 6 = 2 sqrt(q)  ->  past the collision "
      f"(w(7) = {[w for a, w in rows if a == 7][0]:+.3f} < 0: no positive polarization, "
      "matching Honda-Tate non-realizability)")
print("   " + ("PASS — positive invariant form exists iff |a| < 2 sqrt(q); index jumps EXACTLY "
               "at the Krein collision = the Honda-Tate boundary" if okB else "FAIL"))

# continuity of the witness across the collision (index jump <=> degeneracy, not before/after)
aa = np.linspace(5.5, 6.5, 41)
ws = [witness(a)[0] for a in aa]
cross = [a for a, w1, w2 in zip(aa[:-1], ws[:-1], ws[1:]) if w1 >= 0 > w2]
okC = len(cross) == 1 and abs(cross[0] - 6.0) < 0.05
print(f"\n   witness sign change located at a = {cross[0] if cross else float('nan'):.3f} "
      f"(expect 6.000) — single crossing: {len(cross) == 1}")
print("   " + ("PASS — the form degenerates AT the collision and nowhere else" if okC else "FAIL"))

allok = okA and okB and okC
print("\nRESULT: " + ("GREEN — Pi_1 pins all but the pole pair to the axis; the F_q index can "
                      "jump ONLY through a degeneracy of the invariant form, and on the rank-2 "
                      "carrier that locus is exactly |a| = 2 sqrt(q) (Honda-Tate = Krein collision)"
                      if allok else "RED"))
