"""
probe_chiral_weil_margin.py

PUSH (Leo's directive): test the N8 chirality-protection thesis on the ACTUAL assembled Weil
operator, not the finite cubic Gram. Thesis: the odd (chi_3) sector is protected; the even (zeta)
sector carries the archimedean negativity. Decidable: build the Weil quadratic form for BOTH
zeta and L(s,chi_3) on the same support-[-L,L] even test class, and compare margins lambda_min
as primes enter.

Weil form  Q(g) = c^T M c,  M = A + (POLE) - P:
  A_jk   = (1/2pi) int ghat_j ghat_k * dens(r) dr      [archimedean floor]
           dens_zeta(r) = Re psi(1/4 + ir/2) - log pi                       (even char, a=0)
           dens_chi3(r) = Re psi(3/4 + ir/2) + log 3 - log pi               (odd char chi_3, a=1)
  POLE   = 2 G G^T                 (ONLY for zeta: simple pole at s=1; chi_3 L is entire -> none)
  P_jk   = 2 sum_n eps(n) Lam(n)/sqrt(n) (g_j*g_k)(log n),  log n <= 2L
           eps(n) = 1 for zeta;  eps(n) = chi_3(n) in {+1,-1,0} for L(s,chi_3).

Archimedean well depth at r=0:  zeta -5.37  vs  chi_3 -1.12  (chi_3 sits in a SHALLOWER well).
Question: does lambda_min(chi_3) stay >= 0 (protected) while lambda_min(zeta) erodes negative?

Deterministic: numpy + mpmath.
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 20

def dens_zeta(rvals):
    lp = float(mp.log(mp.pi))
    return np.array([float(mp.re(mp.digamma(mp.mpf(1)/4 + 1j*mp.mpf(r)/2))) - lp for r in rvals])

def dens_chi3(rvals):
    c = float(mp.log(3) - mp.log(mp.pi))
    return np.array([float(mp.re(mp.digamma(mp.mpf(3)/4 + 1j*mp.mpf(r)/2))) + c for r in rvals])

def chi3(n):
    m = n % 3
    return 0 if m == 0 else (1 if m == 1 else -1)

def prime_powers_upto(Nmax):
    out = []
    for n in range(2, Nmax+1):
        t = n; ps = set(); d = 2
        while d*d <= t:
            while t % d == 0: ps.add(d); t //= d
            d += 1
        if t > 1: ps.add(t)
        if len(ps) == 1:
            p = next(iter(ps)); out.append((n, float(mp.log(p))))
    return out

def basis(u, L, m):
    env = np.where(np.abs(u) <= L, (1+np.cos(np.pi*u/L))/2, 0.0)
    return np.array([env*np.cos(k*np.pi*u/L) for k in range(m)])

def weil_M(L, which, m=14):
    du = 2*L/4000; u = np.arange(-L, L+du/2, du)
    g = basis(u, L, m)
    R, dr = 260.0, 0.05; r = np.arange(-R, R+dr/2, dr)
    ghat = (g @ np.cos(np.outer(r, u)).T)*du
    dens = dens_zeta(r) if which == "zeta" else dens_chi3(r)
    A = np.zeros((m, m))
    for j in range(m):
        wj = ghat[j]*dens*dr/(2*np.pi)
        for k in range(j, m):
            A[j, k] = A[k, j] = np.sum(wj*ghat[k])
    M = A.copy()
    if which == "zeta":                                   # simple pole at s=1
        Gk = (g*np.cosh(u/2)) @ np.ones_like(u)*du
        M += 2*np.outer(Gk, Gk)
    Nmax = int(np.floor(np.exp(2*L)))
    vm = [(n, lam) for (n, lam) in prime_powers_upto(Nmax) if np.log(n) <= 2*L+1e-9]
    P = np.zeros((m, m))
    for (n, lam) in vm:
        w = np.log(n); eps = 1.0 if which == "zeta" else chi3(n)
        if eps == 0: continue
        gs = np.array([np.interp(u-w, u, g[k], left=0, right=0) for k in range(m)])
        P += 2*eps*lam/np.sqrt(n)*((g @ gs.T)*du)
    M = M - P
    return (M+M.T)/2, len(vm)

print("="*80)
print("CHIRAL WEIL MARGINS:  lambda_min(zeta)  vs  lambda_min(L(.,chi_3))  as primes enter")
print("="*80)
print(f"  {'L':>5} {'#pp':>5} {'lambda_min ZETA':>18} {'lambda_min CHI_3':>18} {'chi3 - zeta':>12}")
for L in [1.0, 1.5, 2.0, 2.5, 3.0, 3.5]:
    Mz, nz = weil_M(L, "zeta")
    Mc, nc = weil_M(L, "chi3")
    lz = np.linalg.eigvalsh(Mz)[0]
    lc = np.linalg.eigvalsh(Mc)[0]
    print(f"  {L:>5} {nz:>5} {lz:>18.6e} {lc:>18.6e} {lc-lz:>12.3e}")
print("""
READING.
  - If lambda_min(chi_3) stays >= 0 (or markedly less negative) while lambda_min(zeta) erodes,
    the odd/chiral sector IS structurally more protected -- Leo's thesis gets real support on the
    true operator, and the question sharpens to: does the chi_3 protection transfer to zeta via
    the Z/6 (Dedekind Q(sqrt-3) = zeta * L(.,chi_3)) coupling?
  - If both erode together, the chiral sector is no more protected (GRH-chi_3 is as open as RH);
    conservation of difficulty. Either way this is a real datum on the actual Weil margin.""")
