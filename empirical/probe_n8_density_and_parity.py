"""
probe_n8_density_and_parity.py  (v2 -- Q3 grid bug fixed, Q2 closed form added)

Q2 (anchor scaling). Leo: normalize the raw asymmetric trace by phi(N); the density
rho_N = Tr_asym/phi(N) converges to C*|L(1/2,chi_3)|^2 (|L|^2 = 0.231238). We extend to many moduli,
extract the exact pattern, and follow the PRIMORIAL sequence (the N->infinity relevant to the proof).

Q3 (Archimedean Annihilation Lemma  P_odd U_inf P_odd = 0). Distinguish, on a SYMMETRIC grid with
parity x -> -x:
  - cosine TRANSFORM  C[i,j] = cos(x_i x_j)         (kernel depends on the PRODUCT)  -> annihilates odd
  - even CONVOLUTION  K[i,j] = g(x_i - x_j), g even  (kernel depends on the DIFFERENCE)-> preserves odd
  - MULTIPLIER        diag(m(x_i)), m even                                            -> preserves odd
The standard Weil archimedean term is multiplication by the even symbol Omega_inf(r) -- a multiplier.
N5 (per Leo) gives U_inf as the CC20 *convolution* kernel k^u(lambda,mu). Both multiplier and
even-convolution PRESERVE the odd sector; only a genuine cosine TRANSFORM annihilates it.

numpy. No torch.
"""
import numpy as np
from math import gcd

w_of = lambda N: np.exp(2j*np.pi/N)
Z3   = np.exp(2j*np.pi/3)
L2   = 0.4808726238**2     # |L(1/2,chi_3)|^2 = 0.231238

def twisted_HF(N, twist):
    w = w_of(N); W = np.zeros((N-1, N-1), complex)
    for ki, k in enumerate(range(1, N)):
        Rk = 1.0/np.sqrt(N*k*(k+1))
        for ci, c in enumerate(range(1, N)):
            z = twist*w**c
            W[ki, ci] = Rk*(sum(z**j for j in range(k)) - k*z**k)
    return W

def defect(N):
    W = twisted_HF(N, Z3); G = W.conj().T @ W; D = np.eye(N-1) - G
    ev, U = np.linalg.eigh(D); j = int(np.argmax(ev))
    return np.sqrt(max(ev[j], 0.0)) * U[:, j]

def mult_asym(N):
    psi = defect(N); pf = np.zeros(N, complex); pf[1:] = psi
    w = w_of(N)
    f = np.array([sum(pf[c]*w**(c*s) for c in range(N)) for s in range(N)])/np.sqrt(N)
    units = [s for s in range(1, N) if gcd(s, N) == 1]
    A = float(np.real(len(units)*sum(f[s]*np.conj(f[(N-s) % N]) for s in units)))
    return -A, len(units)

def closed_form(N):
    rho = 1.0/6.0
    m = N
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % p == 0:
            rho *= (1 - 1.0/p)
    return rho

print("="*86)
print("Q2  rho_N = Tr_asym/phi(N):  is it |L(1/2,chi3)|^2 = 0.231238, or a structure-dependent rational?")
print("="*86)
print(f"  {'N':>5} {'factor':>12} {'rho_N':>9} {'(1/6)prod_{p>=5,p|N}(1-1/p)':>28} {'rho_N/|L|^2':>11}")
for N in [6,12,18,36,  30,60,90,  42,84,  66,  210]:
    A, phiN = mult_asym(N)
    rho = A/phiN
    print(f"  {N:>5} {N:>12} {rho:>9.5f} {closed_form(N):>28.5f} {rho/L2:>11.4f}")

print("\n  PRIMORIAL sequence (the N -> infinity that the proof's limit actually uses):")
print(f"  {'P_k':>8} {'rho = (1/6)prod_{5<=p<=p_k}(1-1/p)':>36}")
prims = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
Pk = 1
for p in prims:
    Pk *= p
    if p >= 5 and Pk <= 10**12:
        print(f"  {Pk:>8} {closed_form(Pk) if Pk < 50 else (1/6)*np.prod([1-1/q for q in prims if 5<=q<=p]):>36.5f}")
print("""  reading: rho_N is the EXACT rational (1/6) * prod_{p|N, p>=5}(1-1/p) -- purely algebraic,
  modulus-structure dependent, and NOT equal to the transcendental |L(1/2,chi_3)|^2 = 0.2312
  (ratios 0.49-0.72, varying). Along the PRIMORIAL sequence prod(1-1/p) -> 0 (Mertens, ~e^-gamma/
  log p_k), so rho_N -> 0. Under Leo's own phi(N) normalization the density does NOT settle on a
  positive anchor; it tends to ZERO. (The RAW trace grows instead -- but that is the bulk, Q1.)
  PINCER: bulk trace grows (not the edge); intensive density -> 0 (no floor). Neither is a positive
  EDGE floor on lambda_0^odd.""")

print("\n" + "="*86)
print("Q3  even-symbol operator: annihilate the odd sector (lemma) or preserve it?  [grid bug fixed]")
print("="*86)
n = 81
x = np.linspace(-4, 4, n)                 # SYMMETRIC grid; parity is x -> -x  (index i -> n-1-i)
Pm = np.zeros((n, n))
for i in range(n): Pm[i, n-1-i] = 1.0
Po = 0.5*(np.eye(n) - Pm)
C    = np.cos(np.outer(x, x))             # cosine TRANSFORM: kernel ~ cos(product)
K    = np.exp(-np.subtract.outer(x, x)**2/0.5)   # even CONVOLUTION: kernel ~ g(difference)
Mult = np.diag(np.abs(x))                 # MULTIPLIER by even symbol |x|
for name, Op in [("cosine TRANSFORM cos(x.y)", C),
                 ("even CONVOLUTION g(x-y)", K),
                 ("MULT by even symbol |x|", Mult)]:
    block = np.linalg.norm(Po @ Op @ Po)/np.linalg.norm(Op)
    verdict = "ANNIHILATES odd  -> lemma OK for this type" if block < 1e-9 \
              else "PRESERVES odd   -> lemma FAILS for this type"
    print(f"  {name:26s}: ||P_odd Op P_odd||/||Op|| = {block:8.4f}   {verdict}")
print("""  reading: only the cosine TRANSFORM (product kernel) annihilates the odd sector. An even
  CONVOLUTION (difference kernel) and a MULTIPLIER by an even symbol both PRESERVE it. The Weil
  archimedean term is multiplication by the even Omega_inf(r) = Re psi(1/4+ir/2) - log pi -- a
  multiplier; and N5's U_inf is (per Leo) the CC20 convolution kernel. Either way it PRESERVES the
  odd sector, so P_odd U_inf P_odd != 0 and the Annihilation Lemma does not hold UNLESS U_inf is
  literally a cosine transform (product kernel), not a convolution/multiplier. This is the precise
  point to confirm in N5.""")
