"""
KREIN / inverse-spectral route: build the HILBERT-POLYA operator from the zero measure.

m_B = Cauchy transform of mu = sum delta_gamma is a Weyl m-function. The inverse-spectral machine
(Krein / Gelfand-Levitan; discretely = the Stieltjes-Lanczos algorithm) reconstructs the SELF-ADJOINT
operator whose spectral measure is mu -- the tridiagonal JACOBI matrix J (the discrete canonical system):
        J = tridiag(a_n [hopping], b_n [potential]),   spectrum(J) = the zeros.
RH  <=>  mu supported on R  <=>  J is real-symmetric (self-adjoint), b_n, a_n real.
We Lanczos diag(gamma) with a flat cyclic vector to get (a_n,b_n) = the reconstructed Hilbert-Polya
"potential" b_n and "hopping" a_n, inspect their structure, and show an off-axis zero makes them COMPLEX
(non-self-adjoint = RH broken).

No torch. numpy + mpmath(zeros). Deterministic.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 20
N = 40
GAM = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, N+1)])

def lanczos(diag, v0):
    """Lanczos tridiagonalization of diag(diag) with start v0 -> (alpha=b_n, beta=a_n)."""
    n = len(diag); A = np.asarray(diag, complex)
    v0 = v0/np.sqrt(v0.conj() @ v0)
    alpha = np.zeros(n, complex); beta = np.zeros(n-1, complex)
    vprev = np.zeros(n, complex); v = v0.copy(); bprev = 0.0
    for j in range(n):
        w = A*v - bprev*vprev
        a = (v.conj() @ w); alpha[j] = a
        w = w - a*v
        if j < n-1:
            b = np.sqrt(w.conj() @ w); beta[j] = b
            if abs(b) < 1e-14: break
            vprev, v, bprev = v, w/b, b
    return alpha, beta

print("=" * 80)
print("KREIN: the Hilbert-Polya Jacobi operator reconstructed from the zero measure (spectrum = zeros)")
print("=" * 80)

# real zeros -> real-symmetric Jacobi matrix (self-adjoint Hilbert-Polya operator)
b, a = lanczos(GAM, np.ones(N))
print(f"\nreal zeros (RH): reconstructed potential b_n and hopping a_n (should be REAL):")
print(f"   max |Im b_n| = {np.max(np.abs(b.imag)):.2e}   max |Im a_n| = {np.max(np.abs(a.imag)):.2e}  (self-adjoint)")
print(f"   {'n':>3} {'b_n (potential)':>18} {'a_n (hopping)':>16}")
for n in (0, 1, 2, 5, 10, 20, 30, 38):
    bn = f"{b[n].real:.4f}"
    an = f"{a[n].real:.4f}" if n < N-1 else "  --"
    print(f"   {n:>3} {bn:>18} {an:>16}")
# growth diagnostics: potential center vs height, hopping growth
print(f"\n   potential b_n tracks the spectral centroid; b_n grows ~ with the zero heights:")
print(f"     b_0={b[0].real:.3f} (mean of gammas={GAM.mean():.3f}); b_38={b[38].real:.3f}")
print(f"   hopping a_n (kinetic) grows: a_0={a[0].real:.3f} -> a_20={a[20].real:.3f} -> a_38={a[38].real:.3f}")
# check eigenvalues reproduce the zeros
T = np.diag(b.real) + np.diag(a.real, 1) + np.diag(a.real, -1)
ev = np.sort(np.linalg.eigvalsh(T))
print(f"   eigenvalues of J reproduce the zeros: max|eig - gamma| = {np.max(np.abs(ev - np.sort(GAM))):.2e}")

# off-line zero -> complex atom -> complex (non-self-adjoint) Jacobi coefficients
print("\noff-line: move gamma_1 -> gamma_1 + i*delta (one zero off the line):")
print(f"   {'delta':>7} {'max |Im b_n|':>16} {'self-adjoint?':>16}")
for delta in (0.0, 0.1, 0.3):
    g = GAM.astype(complex).copy(); g[0] = GAM[0] + 1j*delta
    bb, aa = lanczos(g, np.ones(N))
    immax = np.max(np.abs(bb.imag))
    print(f"   {delta:>7.2f} {immax:>16.3e} {'YES' if immax < 1e-9 else 'NO -> RH broken':>16}")
print("""
   => real zeros: J is real-symmetric -- a genuine SELF-ADJOINT (Hilbert-Polya) operator with spectrum
      exactly the zeros; the reconstructed potential b_n and hopping a_n are real and structured.
      one off-line zero: the moments go complex -> b_n complex -> J non-self-adjoint = RH broken.
   The Krein machine turns m_B (which we hold as the Cauchy transform of the zeros) into the explicit
   discrete Hilbert-Polya operator; RH = that operator is self-adjoint.
""")
print("=" * 80)
