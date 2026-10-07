"""
THE UNIFORM QUESTION: does the chiral cubic Jensen margin -> 0 or a POSITIVE LIMIT as conductor -> inf?

The floor-lift localized RH-via-moments to: the cubic (d=3) Jensen margin stays > 0 UNIFORMLY over the
chiral (odd) family of self-dual L-functions. inf over shift n is at n=0 (lowest zero, tightest). So the
RH-bearing quantity is:  inf_chi  margin_{d=3,n=0}(chi)  over the odd family, as conductor q -> inf.
  * -> 0   => no uniform lower bound; chiral positivity marginal at high conductor (RH-critical there).
  * -> c>0 => uniform lower bound; comfortable.

Odd chars: Legendre (a/p) for primes p == 3 mod 4 (chi_{-p}, ODD), plus chi_{-4}, chi_{-8}. Even contrast:
p == 1 mod 4. Completed Lambda(s,chi)=(q/pi)^{(s+eps)/2} Gamma((s+eps)/2) L(s,chi); Xi=Lambda(1/2+it)
(analytic). Small Cauchy radius r=1 (inside every first zero T_1 ~ 2pi/log q >~ 1.5 for q<=67).

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 25

def legendre(a, p):
    a %= p
    if a == 0: return 0
    r = pow(a, (p-1)//2, p)
    return 1 if r == 1 else -1

def Lfun(chi, q): return lambda s: q**(-s)*mp.fsum(chi(a)*mp.zeta(s, mp.mpf(a)/q) for a in range(1, q) if chi(a) != 0)
def Xi_completed(chi, q, eps):
    L = Lfun(chi, q)
    return lambda t: (q/mp.pi)**((mp.mpf(1)/2+1j*t+eps)/2)*mp.gamma((mp.mpf(1)/2+1j*t+eps)/2)*L(mp.mpf(1)/2+1j*t)

def taylor_a(Xifun, M, r=mp.mpf(1), N=48):
    pts = [Xifun(r*mp.e**(2j*mp.pi*jj/N)) for jj in range(N)]
    return [(-1)**m * mp.re(mp.fsum(pts[jj]*mp.e**(-2j*mp.pi*(2*m)*jj/N) for jj in range(N))/(N*r**(2*m)))
            for m in range(M+1)]

def cubic_margin0(A):
    rho = A[0]/A[1]
    coef = [mp.binomial(3, j)*A[j]*rho**j for j in range(4)]
    roots = mp.polyroots([coef[3-j] for j in range(4)], maxsteps=300, extraprec=80)
    im = max(abs(mp.im(r)) for r in roots); re = sorted(mp.re(r) for r in roots)
    if im > mp.mpf(10)**-6*(1+max(abs(x) for x in re)): return None
    sp = re[-1]-re[0]; g = [re[1]-re[0], re[2]-re[1]]
    return float(min(g)/sp)

# build character list
ODD = []   # (label, q, eps=1, chi)
for q in (3, 7, 11, 19, 23, 31, 43, 47, 59, 67):    # primes == 3 mod 4
    ODD.append((f"chi-{q}", q, 1, (lambda a, q=q: legendre(a, q))))
ODD.append(("chi-4", 4, 1, (lambda a: {1:1,3:-1}.get(a % 4, 0))))
ODD.append(("chi-8", 8, 1, (lambda a: {1:1,3:1,5:-1,7:-1}.get(a % 8, 0))))
EVEN = [(f"chi+{q}", q, 0, (lambda a, q=q: legendre(a, q))) for q in (5, 13, 17, 29, 41)]

print("=" * 80)
print("Uniform question: chiral cubic margin (d=3, n=0) vs conductor -> 0 or positive limit?")
print("=" * 80)
def run(group, name):
    out = []
    for lab, q, eps, chi in group:
        A = taylor_a(Xi_completed(chi, q, eps), 4)
        if not all(mp.re(x) > 0 for x in A[:4]):
            print(f"  {lab:>8} q={q:>3}  (coeffs not all +; skip)"); continue
        m = cubic_margin0(A)
        out.append((q, m))
        print(f"  {lab:>8}  q={q:>3}  log q={float(mp.log(q)):.3f}   margin(d=3,n=0) = {('%.4f'%m) if m else 'CMPLX'}")
    return out
print("\nCHIRAL (odd) family, by conductor:")
od = sorted([(q, m) for q, m in run(ODD, 'odd') if m], key=lambda x: x[0])
print("\nEVEN family (contrast):")
ev = sorted([(q, m) for q, m in run(EVEN, 'even') if m], key=lambda x: x[0])

# trend: fit margin ~ A + B/log q  (does B/log q -> 0, i.e. margin -> A as q->inf?)
def fit_limit(data):
    # least squares margin = A + B * x, x = 1/log q
    xs = [1/mp.log(q) for q, m in data]; ys = [mp.mpf(m) for q, m in data]
    n = len(xs); sx = mp.fsum(xs); sy = mp.fsum(ys); sxx = mp.fsum(x*x for x in xs); sxy = mp.fsum(x*y for x, y in zip(xs, ys))
    B = (n*sxy - sx*sy)/(n*sxx - sx*sx); A = (sy - B*sx)/n
    return float(A), float(B)
print("\n" + "=" * 80)
print("TREND (fit margin = A + B/log q;  q->inf  =>  margin -> A):")
for data, nm in ((od, "chiral/odd"), (ev, "even")):
    if len(data) >= 3:
        A, B = fit_limit(data)
        print(f"  {nm:>12}: margin -> A = {A:+.4f}  (slope B={B:+.3f}/log q);  "
              f"extrapolated q->inf limit = {A:.4f} -> {'POSITIVE (uniform bound, comfortable)' if A>0.02 else 'NEAR 0 (marginal/critical)'}")
print(f"""
READING: if the chiral extrapolated limit A is POSITIVE and bounded away from 0, the cubic margin has a
  UNIFORM lower bound over the odd family -> RH-positivity comfortable across conductors (no high-conductor
  catastrophe). If A ~ 0 (margin drifts to 0 as q->inf), the chiral positivity is MARGINAL at high conductor
  -- the RH-critical region is the high-conductor tail, and "uniform over the family" is exactly where it
  bites. Either way this turns the localized RH quantity into a measured trend with an extrapolated limit.
""")
print("=" * 80)
