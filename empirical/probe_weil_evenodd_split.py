"""
Connes S6.6(a), the one surviving non-circular lever: is the finite Weil form's ground state
SIMPLE + EVEN? Reduces (per the adversarial assault) to the SIGN of the even-odd ground split
  Delta(lambda) = lambda_0^odd(QW_lambda) - lambda_0^even(QW_lambda).
Even wins (Delta>0) => simple+even ground (necessary, NOT sufficient, for the limit transfer).

CLEAN FREQUENCY-SPACE build (fixes the ill-conditioned x-space singular-kernel builds v1-v3).
The Weil quadratic form on phi supported in [-a,a] (a=(log X)/2, primes<=X):
  W(phi) = (1/pi) int_0^inf |phihat(r)|^2 M(r) dr  +  (main rank-1 term)
  M(r) = Re psi(1/4+ir/2) - log pi  -  2 sum_{n<=X} (Lambda(n)/sqrt n) cos(r log n)
  main: EVEN sector  +2 (int phi cosh(x/2))^2 ;  ODD sector  -2 (int phi sinh(x/2))^2.
M(r) is a bounded multiplier (no x-space singularity) -> well-conditioned. Diagonalize in the
EVEN basis {cos((2k+1)pi x/2a)} and ODD basis {sin(k pi x/a)} on [-a,a] (both vanish at +-a).

The archimedean+main background is parity-structured; Delta isolates the parity-asymmetric
(arithmetic) content. We report sign(Delta), the gap, and which primes drive Delta.
numpy + mpmath. No torch.
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 18

def prime_powers(X):
    sieve=np.ones(X+1,bool); sieve[:2]=False
    for i in range(2,int(X**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    out=[]
    for p in np.where(sieve)[0]:
        pe=int(p)
        while pe<=X: out.append((pe,float(np.log(p)))); pe*=int(p)
    return out

def even_hat(k,a,r):   # FT of cos(w x) on [-a,a], w=(2k+1)pi/2a ; real even
    w=(2*k+1)*np.pi/(2*a)
    def sinc_a(d): return np.where(np.abs(d)<1e-9, a, np.sin(d*a)/np.where(np.abs(d)<1e-9,1,d))
    return sinc_a(w-r)+sinc_a(w+r)
def odd_hat(k,a,r):    # int sin(w x) sin(r x) dx on [-a,a], w=k pi/a ; real
    w=k*np.pi/a
    def sinc_a(d): return np.where(np.abs(d)<1e-9, a, np.sin(d*a)/np.where(np.abs(d)<1e-9,1,d))
    return sinc_a(w-r)-sinc_a(w+r)

def analyze(X, K=26, R=400.0, dr=0.02):
    a=0.5*np.log(X)
    r=np.arange(dr,R,dr)
    Om=np.array([float(mp.re(mp.digamma(0.25+0.5j*rr))) for rr in r])-float(np.log(np.pi))
    prime=np.zeros_like(r)
    for (n,logp) in prime_powers(X):
        prime+= (logp/np.sqrt(n))*np.cos(r*np.log(n))
    M = Om - 2*prime                                   # frequency multiplier
    x=np.linspace(-a,a,2000); dx=x[1]-x[0]
    # EVEN block
    PhiE=np.array([even_hat(k,a,r) for k in range(K)])          # (K, len r)
    WE=(PhiE*(M*dr))@PhiE.T/np.pi
    # even main: +2 (int phi cosh)^2
    ce=np.array([ (np.cos((2*k+1)*np.pi*x/(2*a))*np.cosh(x/2)).sum()*dx for k in range(K)])
    WE+=2*np.outer(ce,ce)
    we,Ve=np.linalg.eigh(WE)
    # ODD block
    PhiO=np.array([odd_hat(k,a,r) for k in range(1,K+1)])
    WO=(PhiO*(M*dr))@PhiO.T/np.pi
    so=np.array([ (np.sin(k*np.pi*x/a)*np.sinh(x/2)).sum()*dx for k in range(1,K+1)])
    WO+=-2*np.outer(so,so)
    wo,Vo=np.linalg.eigh(WO)
    return a, we, wo

ZETA1=14.134725
print("="*80)
print("Connes S6.6(a): even-odd ground split Delta(lambda)=lam0_odd - lam0_even (clean freq build)")
print("="*80)
print(f"  {'X':>4} {'a':>7} {'lam0_even':>12} {'lam0_odd':>12} {'Delta':>12} {'even gap':>10} {'verdict':>14}")
prev=None
for X in [13,30,60,120,210]:
    a,we,wo=analyze(X)
    d=wo[0]-we[0]
    egap=we[1]-we[0]
    verdict = "EVEN wins" if d>0 else "ODD wins"
    print(f"  {X:>4} {a:>7.3f} {we[0]:>12.5f} {wo[0]:>12.5f} {d:>+12.5f} {egap:>10.5f} {verdict:>14}")
print("""
  READING (honest):
   - Delta>0 at every X and even-gap>0 => the finite Weil ground state is EVEN and SIMPLE,
     i.e. Connes S6.6(a) holds for these finite truncations (clean frequency build, no
     singular-kernel artifact). This is the necessary precondition for the Hurwitz/
     Caratheodory-Fejer limit transfer.
   - Delta sign-flips or even-gap->0 => S6.6(a) is genuinely delicate even finitely.
   - EITHER WAY this is NECESSARY, NOT SUFFICIENT: the metric identity theta_x ~ k_lambda
     (= RH) is untouched. This probes a real lemma on the route, not RH.""")
