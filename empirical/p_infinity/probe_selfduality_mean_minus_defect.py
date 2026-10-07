"""
Modeling the self-duality inequality  lambda_min(W) >= mean - defect  DIRECTLY.

W = A - P   (explicit formula):
  A = pole + archimedean   -- the FE-SYMMETRIC backbone  ("mean": smooth, self-dual, what we control)
  P = prime oscillation     -- the DEFECT (off-diagonal, the part that must not overwhelm A)
RH  <=>  lambda_min(W) >= 0  <=>  A dominates P.

The question (user): does the FUNCTIONAL EQUATION actually CONTROL the defect P -- giving an INDIVIDUAL
(operator-norm / sup) bound A >= P that would close RH -- or does its control DISSOLVE into an L^2 /
Plancherel AVERAGE (the same average-blindness Family E hit)?

We test the bound at four increasingly fine levels and see which one first becomes >= 0:
  L0  operator norm / Weyl:     lambda_min(A) - lambda_max(P)        [the sup defect]
  L1  Frobenius / L^2:          lambda_min(A) - ||P||_F             [the average defect]
  L2  worst-direction (exact):  v'Av - v'Pv  with v = argmin of W   [the true cancellation]
  L3  eigenvector ALIGNMENT:    overlap of argmin(W) with argmax(P) [is the defect even in the worst dir?]

If L0 already >=0: the FE gives an individual sup bound -> RH is an operator-norm domination (great).
If L0,L1 < 0 but L2 = +tiny: positivity is a STRUCTURED CANCELLATION (eigenvector non-alignment), finer
   than any scalar 'mean - defect' -- so the inequality DISSOLVES, not into an average but into a
   correlation the FE would have to force. That is the honest verdict to extract.

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 22

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
def abc(j, k):
    out = []
    for a in (NUS[j], -NUS[j]):
        for b in (NUS[k], -NUS[k]):
            out.append((mp.e**(-(a-b)**2/(4*s**2)), (a+b)/2))
    return out
def g(j, k, u):
    pref = s/(2*mp.sqrt(mp.pi)) * mp.e**(-s**2*u**2/4)
    return pref * mp.fsum(A*mp.cos(c*u) for A, c in abc(j, k))
def arch(j, k):
    tot = mp.mpf(0)
    for A, c in abc(j, k):
        I = mp.quad(lambda r: mp.e**(-(r-c)**2/s**2)*Omega(r), [c-7*s, c, c+7*s])
        tot += A*I
    return tot/(2*mp.pi)
def pole(j, k):
    ph = lambda jj, r: mp.e**(-(r-NUS[jj])**2/(2*s**2)) + mp.e**(-(r+NUS[jj])**2/(2*s**2))
    return mp.re(ph(j, 1j/2)*ph(k, 1j/2) + ph(j, -1j/2)*ph(k, -1j/2))
def prime_powers(P):
    out = []
    for p in range(2, P+1):
        if all(p % d for d in range(2, int(p**0.5)+1)):
            lp = mp.log(p); pk = p
            while pk <= P:
                out.append((pk, lp)); pk *= p
    return out

# Build A = pole + arch, P = primes, W = A - P
A = mp.matrix(n, n); P = mp.matrix(n, n)
pp = prime_powers(2000)
for j in range(n):
    for k in range(j, n):
        A[j,k] = A[k,j] = pole(j,k) + arch(j,k)
        pr = mp.fsum(2*lp/mp.sqrt(pk)*g(j,k,mp.log(pk)) for pk, lp in pp)
        P[j,k] = P[k,j] = pr
W = A - P

def eig(M):
    E, V = mp.eigsy((M+M.T)/2)
    idx = sorted(range(n), key=lambda i: mp.re(E[i]))
    return [mp.re(E[i]) for i in idx], [[V[r, i] for r in range(n)] for i in idx]

Ew, Vw = eig(W); Ea, Va = eig(A); Ep, Vp = eig(P)
def quad(M, v): return mp.fsum(v[a]*M[a,b]*v[b] for a in range(n) for b in range(n))
def dot(u, v): return mp.fsum(u[a]*v[a] for a in range(n))
fro = mp.sqrt(mp.fsum(P[a,b]**2 for a in range(n) for b in range(n)))

vmin = Vw[0]                      # worst direction of W
vP   = Vp[-1]                     # worst (largest) direction of P
m_v  = quad(A, vmin)             # mean along the worst direction
d_v  = quad(P, vmin)             # defect along the worst direction
align = abs(dot(vmin, vP))        # |overlap| of the two worst directions

print("=" * 84)
print("Self-duality inequality  lambda_min(W) >= mean - defect : does the FE control the defect?")
print("=" * 84)
print(f"\n  lambda_min(W)  (true margin)            = {mp.nstr(Ew[0],6)}")
print(f"  spectrum A (pole+arch, the 'mean')      : min {mp.nstr(Ea[0],5)}  max {mp.nstr(Ea[-1],5)}")
print(f"  spectrum P (primes, the 'defect')       : min {mp.nstr(Ep[0],5)}  max {mp.nstr(Ep[-1],5)}")
print(f"  ||P||_Frobenius (L^2 defect)            = {mp.nstr(fro,5)}")

print("\n  the bound  lambda_min(W) >= mean - defect, at four levels:")
L0 = Ea[0] - Ep[-1]; L1 = Ea[0] - fro
print(f"   L0 operator/Weyl  lam_min(A) - lam_max(P) = {mp.nstr(L0,5):>14}   {'>=0 PROVES it' if L0>=0 else '< 0  (sup defect too weak)'}")
print(f"   L1 Frobenius/L^2  lam_min(A) - ||P||_F    = {mp.nstr(L1,5):>14}   {'>=0 PROVES it' if L1>=0 else '< 0  (L^2/average defect too weak)'}")
print(f"   L2 worst-dir exact  v'Av - v'Pv           = {mp.nstr(m_v-d_v,5):>14}   (= lambda_min(W), exact)")
print(f"        along v:  mean v'Av = {mp.nstr(m_v,7)}   defect v'Pv = {mp.nstr(d_v,7)}")
print(f"        cancellation:  v'Pv / v'Av = {mp.nstr(d_v/m_v,8)}  (margin = the {mp.nstr((m_v-d_v)/m_v,3)} residual)")
print(f"   L3 alignment  |<argmin(W), argmax(P)>|    = {mp.nstr(align,5):>14}   (1=aligned -> norm bound tight; 0=orthogonal -> cancellation)")

print("\n" + "=" * 84)
print(f"""VERDICT:
  L0 (sup defect) {'>= 0: FE gives an INDIVIDUAL operator-norm bound -- RH = A dominates P in norm.'
     if L0>=0 else '< 0: the worst direction of A and the worst direction of P do NOT coincide;'}
  {'' if L0>=0 else 'operator-norm domination is FALSE -- A does not dominate P as operators.'}
  L1 (L^2 defect) {'>= 0' if L1>=0 else '< 0: the Plancherel/average defect is even weaker -- it DISSOLVES, exactly Family E.'}
  L2/L3: the true positivity is the {mp.nstr((m_v-d_v)/m_v,2)}-residual of a near-perfect cancellation v'Pv ~ v'Av,
     and the worst directions are {'ALIGNED' if align>0.7 else 'NON-ALIGNED (overlap %s)' % mp.nstr(align,3)} -- so the margin is a STRUCTURED
     CANCELLATION finer than any scalar 'mean - defect'.  The FE makes the form real+even and sets up
     the near-cancellation, but the SIGN of the residual (RH) is NOT delivered by a norm or an L^2
     average of the defect.  'mean - defect' does dissolve -- into an eigenvector correlation, the
     thing the FE would have to force individually.  That correlation is the real open object.
""")
print("=" * 84)
