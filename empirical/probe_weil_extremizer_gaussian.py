"""
Idea A test: is the Weil-form extremizer forced/near Gaussian?  (arch-domination brainstorm)

Weil quadratic form on even test functions, in the r-variable (phi(r) = g-hat on the critical line):
   Q(g) = (1/2pi) int |phi(r)|^2 rho_inf(r) dr  -  (1/2pi) int |phi|^2 P(r) dr  +  2 |phi(i/2)|^2
   rho_inf(r) = Re psi(1/4 + i r/2) - log pi          [archimedean: smooth, metaplectic SL(2,R)-symmetric,
                                                        Gaussian = distinguished extremal vector]
   P(r)       = 2 sum_n Lambda(n) n^{-1/2} cos(r log n) [prime: oscillatory, discrete support {log p^m},
                                                        BREAKS SL(2,R) -> only parity survives]
   +2|phi(i/2)|^2 : the pole term (rank-1, positive; the pole-driven margin of sec 8.7).

STRONG A (a continuous symmetry forces Gaussian extremizers): ANALYTICALLY FALSE -- the primes break
SL(2,R) to parity (Z/2).  WEAK A (extremizer near-Gaussian = Gaussian + small prime correction): tested
here.  Build W_{jk} in scaled even-Hermite modes phi_n^sigma(r)=e_n(sigma r) (n=0,2,4,...; e_0 = Gaussian),
find the minimal eigenvector, measure its Gaussian (n=0) overlap, sweep scale sigma and prime cutoff.

PRE-REGISTERED FALSIFIER:
  * weak A SUPPORTED  if  min-eigvec Gaussian-overlap |v[0]|^2/||v||^2 > 0.9 robustly across sigma;
  * weak A FAILS      if  the overlap is < 0.9 / the prime modes (n=2,4,...) carry substantial weight,
                         i.e. the extremizer is prime-shaped, not Gaussian.
Expectation (from the symmetry argument): primes MIX the modes -> overlap < 1 -> extremizer not Gaussian.

No torch. numpy + scipy (Hermite, digamma).
"""
import numpy as np
from numpy.polynomial.hermite_e import hermeval  # probabilists' Hermite (He_n)
from scipy.special import gammaln, digamma

# ---- even Hermite FUNCTIONS e_n (physicists', L2-normalized): e_n(x)=H_n(x)e^{-x^2/2}/sqrt(2^n n! sqrt(pi))
from numpy.polynomial.hermite import hermval, Hermite

def herm_func(n, x):
    c = np.zeros(n + 1); c[n] = 1.0
    Hn = hermval(x, c)
    norm = np.exp(0.5 * (n * np.log(2) + gammaln(n + 1) + 0.5 * np.log(np.pi)))
    return Hn * np.exp(-x**2 / 2) / norm

def herm_func_imag(n, y):
    """e_n(i y) for real y (even n -> real). H_n(iy) via hermval at complex arg; e^{-(iy)^2/2}=e^{y^2/2}."""
    c = np.zeros(n + 1); c[n] = 1.0
    Hn = hermval(1j * y, c)
    norm = np.exp(0.5 * (n * np.log(2) + gammaln(n + 1) + 0.5 * np.log(np.pi)))
    return (Hn * np.exp(y**2 / 2) / norm).real      # even n -> real

# ---- von Mangoldt prime powers
def von_mangoldt(maxn):
    out = []
    for n in range(2, maxn + 1):
        m, p = n, 2
        while p * p <= m and m % p:
            p += 1
        if m % p:
            p = m
        t = n
        while t % p == 0:
            t //= p
        if t == 1:
            out.append((n, np.log(p)))
    return out

LAM = von_mangoldt(2000)
R, NR = 120.0, 8000
r = np.linspace(-R, R, NR)
dr = r[1] - r[0]
rho_inf = digamma(0.25 + 1j * r / 2).real - np.log(np.pi)
Pmult = 2 * sum((lam / np.sqrt(n)) * np.cos(r * np.log(n)) for n, lam in LAM)   # prime multiplier P(r)
M = rho_inf - Pmult                                                            # full multiplier


def weil_matrix(sigma, modes):
    phis = [herm_func(n, sigma * r) for n in modes]          # phi_n^sigma(r) = e_n(sigma r)
    poles = [2 ** 0.5 * herm_func_imag(n, sigma * 0.5) for n in modes]  # ~ phi_n(i/2); factor folded below
    K = len(modes)
    W = np.zeros((K, K))
    for a in range(K):
        for b in range(a, K):
            integ = np.sum(phis[a] * phis[b] * M) * dr / (2 * np.pi)
            pole = 2.0 * herm_func_imag(modes[a], sigma * 0.5) * herm_func_imag(modes[b], sigma * 0.5)
            W[a, b] = W[b, a] = integ + pole
    return W


if __name__ == "__main__":
    print("Idea A: is the Weil-form extremizer Gaussian?  (strong A already analytically FALSE: primes")
    print("break the archimedean SL(2,R) to parity).  Testing WEAK A = extremizer near-Gaussian.")
    print("=" * 82)
    modes = [0, 2, 4, 6, 8]
    print(f"  even Hermite modes n = {modes};  n=0 is the Gaussian.")
    print(f"  {'sigma':>6} | {'mu_min':>11} | {'Gauss overlap |v0|^2':>20} | min-eigvec (|v_n|^2 on n=0,2,4,6,8)")
    print("  " + "-" * 78)
    for sigma in [0.04, 0.06, 0.08, 0.10, 0.14, 0.20, 0.30]:
        W = weil_matrix(sigma, modes)
        vals, vecs = np.linalg.eigh(W)
        v = vecs[:, 0]
        w = v**2 / np.sum(v**2)
        print(f"  {sigma:>6.2f} | {vals[0]:>11.4f} | {w[0]:>20.3f} | "
              + " ".join(f"{x:.3f}" for x in w))
    print("  " + "-" * 78)
    print("READOUT: if |v0|^2 > 0.9 across sigma -> weak A supported (extremizer ~ Gaussian).")
    print("         if the prime modes n=2,4,6,8 carry weight / overlap < 0.9 -> extremizer is")
    print("         PRIME-SHAPED, weak A FAILS, idea A retired (symmetry does NOT force Gaussian).")
