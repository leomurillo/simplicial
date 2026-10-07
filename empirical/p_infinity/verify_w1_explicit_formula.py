"""verify_w1_explicit_formula.py — certify W1's load-bearing step before writing it.

ocho S_g(x) = sum_gamma g~(1/2+i gamma) e^{i gamma x}  (sum over zeta zeros, ZERO side).
W1 pushes this through the Guinand-Weil explicit formula to a PRIME side:

  S_g(x) = [g~(0)e^{-x/2}+g~(1)e^{x/2}]            (poles rho=0,1)
         + c_arch * (1/2pi) int g~(1/2+ir)e^{irx} [Re psi(1/4+ir/2) - log pi] dr   (archimedean, n-INDEP)
         - sum_{n>=2} (Lambda(n)/sqrt n)[G(log n - x) + G(-log n - x)],            (PRIME triple-able)

with g~(1/2+ir) = int G(v) e^{irv} dv,  G(v) = g(e^v) e^{v/2}.  Test: G(v)=exp(-v^2/2sig^2) Gaussian,
so g~(1/2+ir)=sig sqrt(2pi) exp(-sig^2 r^2/2).  We compute S_g(x) from the first NZ zeta zeros and from
the prime side, and confirm the residual (zeros - poles + primes) equals the archimedean integral with a
SINGLE constant c_arch across all x (which both verifies the identity and pins the 1/2 in the Gamma term).
"""
import mpmath as mp
from sympy import primerange
mp.mp.dps = 30
sig = mp.mpf('0.15')
C   = sig*mp.sqrt(2*mp.pi)
def G(u):  return mp.e**(-u*u/(2*sig*sig))
def gt(r): return C*mp.e**(-sig*sig*r*r/2)         # g~(1/2+ir)

NZ = 80
zeros = [mp.im(mp.zetazero(k)) for k in range(1, NZ+1)]
print(f"first/last zero used: {float(zeros[0]):.3f} .. {float(zeros[-1]):.3f};  gt(last)/gt(first)={float(gt(zeros[-1])/gt(zeros[0])):.1e}")

def S_zeros(x):                                     # sum over +/- gamma : 2 gt(g) cos(g x)
    return 2*C*sum(mp.e**(-sig*sig*g*g/2)*mp.cos(g*x) for g in zeros)
def poles(x):
    g0 = C*mp.e**(sig*sig/8)                        # g~(0)=g~(1)=int G(v)e^{-v/2}dv
    return g0*(mp.e**(-x/2)+mp.e**(x/2))
def primesum(x):
    s = mp.mpf(0)
    P = list(primerange(2, int(mp.e**(x+10*sig))+3))
    for p in P:
        lp = mp.log(p); k = 1
        while k*lp <= x + 10*sig:
            s += (lp/mp.sqrt(p**k))*(G(k*lp - x) + G(-k*lp - x)); k += 1
    return s
def arch_raw(x):                                    # (1/2pi) int_{-inf}^{inf} gt(r)cos(rx)[Re psi(1/4+ir/2)-log pi] dr
    f = lambda r: gt(r)*mp.cos(r*x)*(mp.re(mp.digamma(mp.mpf('0.25')+1j*r/2)) - mp.log(mp.pi))
    return (1/mp.pi)*mp.quad(f, [0, 8, 20, 45, 80])   # even integrand: (1/2pi)int_{-inf}^{inf} = (1/pi)int_0^inf

print(f"\n{'x':>7} {'S(zeros)':>12} {'poles':>10} {'primes':>11} {'residual':>12} {'arch_raw':>12} {'ratio':>8}")
ratios = []
for x in [mp.mpf(v) for v in ['0.40','0.6931','1.00','1.0986','1.40','1.6094','2.00']]:
    Sz = S_zeros(x); po = poles(x); pr = primesum(x); ar = arch_raw(x)
    res = Sz - po + pr                              # should equal c_arch * arch_raw
    r = res/ar if ar != 0 else mp.nan
    ratios.append(r)
    print(f"{float(x):>7.4f} {float(Sz):>12.6f} {float(po):>10.4f} {float(pr):>11.6f} {float(res):>12.6f} {float(ar):>12.6f} {float(r):>8.5f}")

rv = [float(r) for r in ratios]
mean = sum(rv)/len(rv); spread = max(rv)-min(rv)
print(f"\nresidual/arch_raw : mean={mean:.5f}  spread={spread:.2e}  (1/2 -> Gamma-arg-half; constant => identity verified)")
print(f"  reconstruct vs zeros with c_arch={mean:.4f}:")
for x in [mp.mpf('0.6931'), mp.mpf('1.40')]:
    recon = poles(x) + mean*arch_raw(x) - primesum(x)
    print(f"    x={float(x):.4f}: prime-side={float(recon):.8f}  zero-side={float(S_zeros(x)):.8f}  reldiff={float(abs(recon-S_zeros(x))/abs(S_zeros(x))):.1e}")
