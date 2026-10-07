"""
LEAD #1 (the actual analytic bottleneck): does the energy margin mu = 1 - rho_E decay to 0 as the prolate
WINDOW grows, and at what rate?  Cross-check against Sliwinski's uncertainty floor ~1/(4 ln lambda).

rho_E = lambda_max(A^-1/2 P A^-1/2) on a basis of Gaussian packets at frequencies NUS (the window). Growing
the window (more packets, higher frequencies) = larger lambda = capturing more zeros = the CCM mu_lambda->0
limit. We build A=pole+arch and P=primes ONCE on a large frequency grid, then read leading sub-windows.

Honest aim: characterize the decay (numerics), NOT prove it. If mu shrinks ~ 1/ln(window) it is consistent
with the Sliwinski uncertainty-limited convergence (and with RH); the PROOF of the rate is the open step.

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 18

# frequency grid (the window); leading subsets = growing lambda
NUS_FULL = [mp.mpf(v) for v in (8, 14, 20, 26, 32, 38, 44, 50)]
s = mp.mpf(3)
def Omega(r): return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*r/2)) - mp.log(mp.pi)
def abc(a0, b0):
    out = []
    for a in (a0, -a0):
        for b in (b0, -b0):
            out.append((mp.e**(-(a-b)**2/(4*s**2)), (a+b)/2))
    return out
def gfun(a0, b0, u):
    pref = s/(2*mp.sqrt(mp.pi)) * mp.e**(-s**2*u**2/4)
    return pref * mp.fsum(A*mp.cos(c*u) for A, c in abc(a0, b0))
def arch(a0, b0):
    tot = mp.mpf(0)
    for A, c in abc(a0, b0):
        tot += A*mp.quad(lambda r: mp.e**(-(r-c)**2/s**2)*Omega(r), [c-7*s, c, c+7*s])
    return tot/(2*mp.pi)
def pole(a0, b0):
    ph = lambda v, r: mp.e**(-(r-v)**2/(2*s**2)) + mp.e**(-(r+v)**2/(2*s**2))
    return mp.re(ph(a0,1j/2)*ph(b0,1j/2) + ph(a0,-1j/2)*ph(b0,-1j/2))
def prime_powers(P):
    out = []
    for p in range(2, P+1):
        if all(p % d for d in range(2, int(p**0.5)+1)):
            lp = mp.log(p); pk = p
            while pk <= P:
                out.append((pk, lp)); pk *= p
    return out

nF = len(NUS_FULL); pp = prime_powers(2000)
Afull = mp.matrix(nF, nF); Pfull = mp.matrix(nF, nF)
print("building Weil form on the frequency grid (one-time)...")
for j in range(nF):
    for k in range(j, nF):
        Afull[j,k]=Afull[k,j]= pole(NUS_FULL[j],NUS_FULL[k]) + arch(NUS_FULL[j],NUS_FULL[k])
        Pfull[j,k]=Pfull[k,j]= mp.fsum(2*lp/mp.sqrt(pk)*gfun(NUS_FULL[j],NUS_FULL[k],mp.log(pk)) for pk,lp in pp)

def rho_E_sub(m):
    A = Afull[:m,:m]; P = Pfull[:m,:m]
    E,Q = mp.eigsy((A+A.T)/2)
    Aih = Q*mp.diag([1/mp.sqrt(mp.re(E[i])) for i in range(m)])*Q.T
    T = Aih*P*Aih
    ET,_ = mp.eigsy((T+T.T)/2)
    return max(mp.re(ET[i]) for i in range(m))

print("=" * 80)
print("Energy margin mu = 1 - rho_E vs window size (the CCM mu_lambda -> 0 question)")
print("=" * 80)
print(f"\n  {'window m':>9} {'top freq':>9} {'rho_E':>16} {'margin mu=1-rho_E':>20}")
prev = None
margins = []
for m in range(2, nF+1):
    r = rho_E_sub(m); mu = 1 - r; margins.append((m, float(NUS_FULL[m-1]), mu))
    print(f"  {m:>9} {mp.nstr(NUS_FULL[m-1],4):>9} {mp.nstr(r,12):>16} {mp.nstr(mu,5):>20}")

print(f"\n  decay check (is mu shrinking? ratio of successive margins):")
for i in range(1, len(margins)):
    m0, _, mu0 = margins[i-1]; m1, f1, mu1 = margins[i]
    if mu0 != 0:
        print(f"    m={m0}->{m1}: mu {mp.nstr(mu0,3)} -> {mp.nstr(mu1,3)}   ratio {mp.nstr(mu1/mu0,4)}")

print("""
HONEST READING:
  * If mu = 1 - rho_E shrinks toward 0 as the window grows, it is consistent with CCM mu_lambda -> 0
    (the convergence whose proof IS RH) and with Sliwinski's uncertainty-limited rate. The numerics
    CHARACTERIZE the decay; they do NOT prove it -- the uniform-in-window bound on the prime sum
    (the prime contribution to P on the growing prolate) is the open analytic step.
  * If mu does NOT cleanly shrink (basis too coarse / window effects), that is a limitation of this
    finite Gaussian-packet model, not evidence against CCM. The faithful object is the CCM prolate
    operator; this is a tractable proxy for the trend.
  This is genuine exploration of the lead-#1 frontier, reported as numerics only -- no proof claimed.
""")
print("=" * 80)
