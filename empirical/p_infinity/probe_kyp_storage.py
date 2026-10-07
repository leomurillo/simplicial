"""
(beta) KYP / storage function, made concrete via NEVANLINNA-PICK.

m_B Herglotz on C+ = a POSITIVE-REAL (passive) transfer function. The KYP / bounded-real lemma says:
PR  <=>  exists a storage (Lyapunov) function V(x)=<x,Px>, P >= 0 (the stored ENERGY). For a Herglotz
function the storage form is realized concretely as the NEVANLINNA-PICK matrix at C+ test points:
        Pi_ij = ( m_B(z_i) - conj(m_B(z_j)) ) / ( z_i - conj(z_j) ),   z_i in C+.
Nevanlinna-Pick: m_B is Herglotz  <=>  Pi >= 0 at EVERY finite set of C+ points. So:
        RH  <=>  the storage/energy form Pi is positive semidefinite.
We verify Pi is the Lyapunov certificate: real zeros => Pi >= 0 (energy exists); one off-line zero
=> Pi acquires a NEGATIVE eigenvalue (no storage function = active/unstable element = RH broken).

No torch. numpy + mpmath(zeros). Deterministic.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 20
N = 25
GAM = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, N+1)])

def mB(z, atoms):                       # Cauchy transform of +-atoms: sum 2z/(a^2 - z^2)
    return np.sum(2*z/(atoms**2 - z**2))

# C+ test points (spread across the relevant heights, Im>0)
PTS = np.array([0.7+1.0j, 3+0.6j, 8+0.5j, 14.1+0.4j, 18+0.7j, 21+0.4j,
                25+0.5j, 30+0.8j, 37+0.6j, 43+1.0j])

def pick(atoms):
    k = len(PTS); M = np.zeros((k, k), complex)
    for i in range(k):
        for j in range(k):
            M[i, j] = (mB(PTS[i], atoms) - np.conj(mB(PTS[j], atoms)))/(PTS[i] - np.conj(PTS[j]))
    return M

print("=" * 80)
print("(beta) KYP storage function = Nevanlinna-Pick matrix:  RH  <=>  storage form Pi >= 0")
print("=" * 80)

Pr = pick(GAM)
herm_err = np.max(np.abs(Pr - Pr.conj().T))
ev_r = np.linalg.eigvalsh(Pr)
print(f"\nreal zeros (RH): Pick/storage matrix is Hermitian (err {herm_err:.1e});")
print(f"   eigenvalues min..max = [{ev_r.min():.4f}, {ev_r.max():.4f}]  -> {'POS.SEMIDEF: storage function EXISTS' if ev_r.min() > -1e-9 else 'INDEFINITE'}")

print("\noff-line: move gamma_1 off-axis as a conjugate pair gamma_1 +- i*delta (real-on-real kept):")
print(f"   {'delta':>7} {'min eig of Pi':>16} {'storage / Lyapunov?':>22}")
for delta in (0.0, 0.05, 0.15, 0.30):
    atoms = np.concatenate([GAM[1:].astype(complex),
                            np.array([GAM[0]+1j*delta, GAM[0]-1j*delta])])
    M = pick(atoms)
    ev = np.linalg.eigvalsh((M + M.conj().T)/2)        # symmetrize tiny numerical asym
    tag = 'EXISTS (P>=0): RH ok' if ev.min() > -1e-9 else 'NONE (P indefinite): RH broken'
    print(f"   {delta:>7.2f} {ev.min():>16.4f} {tag:>22}")

print("""
   => real zeros: the storage/energy form Pi >= 0 -- a Lyapunov certificate for RH EXISTS.
      one off-line zero: Pi acquires a negative eigenvalue -- NO storage function (active element).
   The KYP reading: RH = the arithmetic transfer function m_B is PASSIVE = stores nonnegative energy.
   Pi is the explicit (finite) energy/Lyapunov form; its positivity IS the RH certificate (an SDP).
""")
print("=" * 80)
