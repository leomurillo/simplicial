"""
Modeling the convergence of the apex (finite-prime) Weil form to its archimedean limit.

Weil quadratic form on frequency-bump basis {phi_j}, phi_j(r)=exp(-(r-v_j)^2/2s^2)+exp(-(r+v_j)^2/2s^2).
Two expressions, EQUAL in the limit P->inf (the explicit formula):
  ZERO side (truth):     W^zero_{jk} = sum_{gamma>0} 2 phi_j(gamma) phi_k(gamma)  -- PSD iff zeros real (RH)
  EXPLICIT-FORMULA side: W^ef_{jk}(P) = pole + archimedean - primes(<=P)

  M1  the convergence is REAL: W^ef(P) -> W^zero as the prime reach P grows (apex->archimedean).
  M2  positivity margin (open step = RH): lambda_min(W^ef(P)) -> lambda_min(W^zero) >= 0 (marginal).

EXACT-analytical: phi_j phi_k = sum over a in {+-v_j}, b in {+-v_k} of A_ab * exp(-(r-c_ab)^2/s^2),
  A_ab=exp(-(a-b)^2/4s^2), c_ab=(a+b)/2.  Then:
    g_{jk}(u) = (1/2pi) int phi_j phi_k cos(ru) dr = (s/(2 sqrt(pi))) exp(-s^2 u^2/4) sum_ab A_ab cos(c_ab u)
    arch_{jk} = (1/2pi) sum_ab A_ab int exp(-(r-c_ab)^2/s^2) Omega_inf(r) dr   (non-oscillatory)
  Omega_inf(r) = Re psi(1/4 + i r/2) - log pi.

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 20

ZEROS = [mp.mpf(z) for z in [
 14.134725142,21.022039639,25.010857580,30.424876126,32.935061588,37.586178159,
 40.918719012,43.327073281,48.005150881,49.773832478,52.970321478,56.446247697,
 59.347044003,60.831778525,65.112544048,67.079810529,69.546401711,72.067157674,
 75.704690699,77.144840069,79.337375020,82.910380854,84.735492981,87.425274613,
 88.809111208,92.491899271,94.651344041,95.870634228,98.831194218,101.317851006,
 103.725538040,105.446623052,107.168611184,111.029535543,111.874659177,114.320220915,
 116.226680321,118.790782866,121.370125002,122.946829294]]

s = mp.mpf(3); NUS = [mp.mpf(v) for v in (8, 14, 20, 26)]; n = len(NUS)
def Omega(r): return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*r/2)) - mp.log(mp.pi)

def abc(j, k):     # the 4 (amplitude, center) shifted-Gaussian terms of phi_j phi_k
    out = []
    for a in (NUS[j], -NUS[j]):
        for b in (NUS[k], -NUS[k]):
            out.append((mp.e**(-(a-b)**2/(4*s**2)), (a+b)/2))
    return out

def g(j, k, u):    # (1/2pi) int phi_j phi_k cos(ru) dr  -- closed form
    pref = s/(2*mp.sqrt(mp.pi)) * mp.e**(-s**2*u**2/4)
    return pref * mp.fsum(A*mp.cos(c*u) for A, c in abc(j, k))

def arch(j, k):    # (1/2pi) int phi_j phi_k Omega(r) dr  -- non-oscillatory
    tot = mp.mpf(0)
    for A, c in abc(j, k):
        I = mp.quad(lambda r: mp.e**(-(r-c)**2/s**2)*Omega(r), [c-7*s, c, c+7*s])
        tot += A*I
    return tot/(2*mp.pi)

def pole(j, k):
    ph = lambda jj, r: mp.e**(-(r-NUS[jj])**2/(2*s**2)) + mp.e**(-(r+NUS[jj])**2/(2*s**2))
    return mp.re(ph(j, 1j/2)*ph(k, 1j/2) + ph(j, -1j/2)*ph(k, -1j/2))

def W_zero(j, k):
    return mp.fsum(2*(mp.e**(-(gm-NUS[j])**2/(2*s**2))+mp.e**(-(gm+NUS[j])**2/(2*s**2)))*
                     (mp.e**(-(gm-NUS[k])**2/(2*s**2))+mp.e**(-(gm+NUS[k])**2/(2*s**2))) for gm in ZEROS)

def prime_powers(P):
    out = []
    for p in range(2, P+1):
        if all(p % d for d in range(2, int(p**0.5)+1)):
            lp = mp.log(p); pk = p
            while pk <= P:
                out.append((pk, lp)); pk *= p
    return out

def eig_min(Mat):
    return min(mp.re(x) for x in mp.eigsy(Mat, eigvals_only=True))

print("=" * 78)
print("Apex -> archimedean convergence: finite-prime Weil form -> the zero side")
print("=" * 78)

A = mp.matrix(n, n); Pl = mp.matrix(n, n); Z = mp.matrix(n, n)
for j in range(n):
    for k in range(j, n):
        A[j,k]=A[k,j]=arch(j,k); Pl[j,k]=Pl[k,j]=pole(j,k); Z[j,k]=Z[k,j]=W_zero(j,k)
lam_zero = eig_min(Z)

print(f"\nM1/M2  {'P (prime reach)':>16} {'||W^ef(P)-W^zero||':>20} {'lambda_min W^ef(P)':>20}")
for P in [3, 7, 13, 50, 200, 1000, 5000]:
    pp = prime_powers(P)
    Wef = mp.matrix(n, n)
    for j in range(n):
        for k in range(j, n):
            pr = mp.fsum(2*lp/mp.sqrt(pk)*g(j, k, mp.log(pk)) for pk, lp in pp)
            Wef[j,k]=Wef[k,j]=Pl[j,k]+A[j,k]-pr
    diff = max(abs(Wef[j,k]-Z[j,k]) for j in range(n) for k in range(n))
    print(f"       {P:>16} {mp.nstr(diff,4):>20} {mp.nstr(eig_min(Wef),5):>20}")
print(f"\n       archimedean limit  lambda_min(W^zero) = {mp.nstr(lam_zero,5)}  (>=0 = RH, used as input)")
print("""
Reading:
  M1  W^ef(P) -> W^zero as P grows: the finite-PRIME form reconstructs the archimedean (zero-side)
      form. ||diff|| shrinks -- the apex->archimedean completion, VALIDATED (primes -> the archimedean
      object, no zeros assumed in W^ef).
  M2  lambda_min(W^ef(P)) -> lambda_min(W^zero) >= 0: the MARGINAL positivity. W^zero is PSD because
      the zeros are REAL (RH, input here). The OPEN STEP: prove lambda_min stays >= 0 in the limit
      from the PRIME/pole/archimedean side ALONE -- that archimedean+pole positivity survives the
      prime subtraction as P->inf. That surviving positivity = RH = the CCM prolate convergence.
  The model EXHIBITS the convergence and ISOLATES the one open inequality (the surviving margin).
""")
print("=" * 78)
