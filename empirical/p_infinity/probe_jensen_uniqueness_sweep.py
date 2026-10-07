"""
UNIQUENESS SWEEP: cubic (d=3) Jensen margin across self-dual characters -- is chi_{-3} the GLOBAL
margin-minimizer (the RH-critical knob), or one of a family? And is the minimizer ODD (chiral)?

Geometry: each completed L is a point on the moduli of self-dual L-functions; Xi_chi in Laguerre-Polya is
a positive state; the d=3 Jensen margin = the third-order (Amari-Chentsov / skewness / chiral) distance to
non-hyperbolicity = the info-geometric distance to RH-failure. Smallest margin = most chiral = RH-critical.

Sweep (real primitive quadratic chars + the genuine cubic mod 9):
  cond 1  : zeta                    (even, baseline)
  cond 3  : chi_{-3}  Q(sqrt-3)=Q(zeta_3)  (ODD)  <- the Z/6 chiral seed [cond 6 = this, imprimitive]
  cond 4  : chi_{-4}  Q(i)          (ODD)
  cond 5  : chi_{+5}  Q(sqrt5)      (even)
  cond 7  : chi_{-7}  Q(sqrt-7)     (ODD)
  cond 8  : chi_{+8}  Q(sqrt2)      (even)
  cond 8  : chi_{-8}  Q(sqrt-2)     (ODD)
  cond 9  : cubic chi_9 via self-dual product L(s,chi_9)L(s,chi_9bar)  (the GENUINE cubic)

Completed: Lambda(s,chi)=(q/pi)^{(s+eps)/2} Gamma((s+eps)/2) L(s,chi), eps=0 even /1 odd; Xi=Lambda(1/2+it)
(ANALYTIC -- no re() before the Cauchy-Taylor; re() only on final coeffs). No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 30
W3 = mp.e**(2j*mp.pi/3)

def Lfun(chi, q):
    """L(s,chi) = q^{-s} sum_a chi(a) zeta(s, a/q)."""
    return lambda s: q**(-s) * mp.fsum(chi(a)*mp.zeta(s, mp.mpf(a)/q) for a in range(1, q) if chi(a) != 0)

def completed_Xi(chi, q, eps):
    L = Lfun(chi, q)
    return lambda t: (q/mp.pi)**((mp.mpf(1)/2+1j*t+eps)/2) * mp.gamma((mp.mpf(1)/2+1j*t+eps)/2) * L(mp.mpf(1)/2+1j*t)

# quadratic characters (value tables; a in 1..q-1)
CH = {
 'chi-3'  : (3, 1, {1:1,2:-1}),
 'chi-4'  : (4, 1, {1:1,3:-1,2:0}),
 'chi+5'  : (5, 0, {1:1,2:-1,3:-1,4:1}),
 'chi-7'  : (7, 1, {1:1,2:1,3:-1,4:1,5:-1,6:-1}),
 'chi+8'  : (8, 0, {1:1,3:-1,5:-1,7:1,2:0,4:0,6:0}),
 'chi-8'  : (8, 1, {1:1,3:1,5:-1,7:-1,2:0,4:0,6:0}),
}

def xi_zeta(t):
    s = mp.mpf(1)/2+1j*t
    return mp.mpf(1)/2*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)

# cubic mod 9 (genuine cubic): self-dual product D(s)=L(s,chi9)L(s,chi9bar)
def ind9():
    ind = {}; x = 1
    for e in range(6): ind[x] = e; x = x*2 % 9
    return ind
I9 = ind9()
def chi9(a):  return W3**(I9[a%9]) if a % 3 != 0 else 0
def chi9b(a): return W3**(-I9[a%9]) if a % 3 != 0 else 0
def xi_cubic9(t):
    s = mp.mpf(1)/2+1j*t
    L = Lfun(chi9, 9)(s); Lb = Lfun(chi9b, 9)(s)
    return ((9/mp.pi)**(s/2)*mp.gamma(s/2))**2 * L * Lb   # even, conductor 81, Gamma(s/2)^2

def taylor_a(Xifun, M, r=mp.mpf(3), N=64):
    # fixed-point Cauchy/DFT: c_k = (1/(N r^k)) sum_j Xi(r w^j) w^{-jk}, w=e^{2pi i/N} (N evals; fast)
    pts = [Xifun(r*mp.e**(2j*mp.pi*jj/N)) for jj in range(N)]
    out = []
    for m in range(M+1):
        k = 2*m
        c = mp.fsum(pts[jj]*mp.e**(-2j*mp.pi*k*jj/N) for jj in range(N)) / (N*r**k)
        out.append((-1)**m * mp.re(c))
    return out

def cubic_margin(A, n):
    rho = A[n]/A[n+1]
    coef = [mp.binomial(3, j)*A[n+j]*rho**j for j in range(4)]
    roots = mp.polyroots([coef[3-j] for j in range(4)], maxsteps=300, extraprec=80)
    im = max(abs(mp.im(r)) for r in roots); re = sorted(mp.re(r) for r in roots)
    if im > mp.mpf(10)**-7*(1+max(abs(x) for x in re)): return None
    sp = re[-1]-re[0]; g = [re[i+1]-re[i] for i in range(2)]
    return float(min(g)/sp)

NM = 6
print("=" * 88)
print("Uniqueness sweep: cubic (d=3) Jensen margin across self-dual L-functions")
print("=" * 88)
print(f"  {'character':>10} {'cond':>5} {'parity':>6} {'|L(1/2)|':>10} {'d=3 margin n=0':>15} {'n=1':>8} {'n=2':>8}")

rows = []
# zeta
A = taylor_a(xi_zeta, NM)
m0,m1,m2 = cubic_margin(A,0), cubic_margin(A,1), cubic_margin(A,2)
Lh = abs(mp.zeta(mp.mpf(1)/2))
rows.append(('zeta',1,'even',Lh,m0,m1,m2))
# quadratic chars
for name,(q,eps,tab) in CH.items():
    chi = lambda a,tab=tab,q=q: tab.get(a % q, 0)
    A = taylor_a(completed_Xi(chi,q,eps), NM)
    m0,m1,m2 = cubic_margin(A,0), cubic_margin(A,1), cubic_margin(A,2)
    Lh = abs(Lfun(chi,q)(mp.mpf(1)/2))
    rows.append((name,q,'odd' if eps else 'even',Lh,m0,m1,m2))
# cubic mod 9
A = taylor_a(xi_cubic9, NM)
m0,m1,m2 = cubic_margin(A,0), cubic_margin(A,1), cubic_margin(A,2)
Lh = abs(Lfun(chi9,9)(mp.mpf(1)/2))
rows.append(('cubic-9',9,'even',Lh,m0,m1,m2))

for name,q,par,Lh,m0,m1,m2 in rows:
    f=lambda x:(f"{x:.4f}" if x is not None else " CMPLX")
    print(f"  {name:>10} {q:>5} {par:>6} {mp.nstr(Lh,5):>10} {f(m0):>15} {f(m1):>8} {f(m2):>8}")

# find minimizer at n=0
valid = [(name,par,m0) for name,q,par,Lh,m0,m1,m2 in rows if m0 is not None]
mn = min(valid, key=lambda r:r[2])
odds = [m for _,p,m in valid if p=='odd']; evens=[m for _,p,m in valid if p=='even']
print(f"\n  MARGIN-MINIMIZER (n=0, d=3): {mn[0]} (margin {mn[2]:.4f}, {mn[1]})")
print(f"  ODD chars  margins: {sorted(f'{m:.3f}' for m in odds)}  (mean {sum(odds)/len(odds):.4f})")
print(f"  EVEN chars margins: {sorted(f'{m:.3f}' for m in evens)}  (mean {sum(evens)/len(evens):.4f})")

print("\n" + "=" * 88)
print("""READING (information-geometric):
  * the d=3 Jensen margin = third-order/Amari-Chentsov (skewness/chiral) distance to RH-failure. The sweep
    scans the moduli of self-dual L-functions; the MINIMIZER is the most chiral = the RH-critical direction.
  * If the ODD (chiral) characters cluster BELOW the EVEN ones, parity (not conductor) drives the squeeze:
    the cubic/skewness lives in the chiral (odd) sector, exactly the program's order-3 = chiral = L(.,chi_3).
  * cond 6 = chi_{-3} (imprimitive) -> the Z/6 nontrivial character IS the chiral seed; cond 9 (genuine
    cubic) tests whether a true order-3 character out-skews the Z/6 quadratic. Whichever wins names the
    global RH-critical knob. If chi_{-3} (the smallest-conductor odd / Z/6 seed) is the minimizer, it is
    UNIQUELY critical -- the primorial chiral direction -- and L(1/2,chi_3) is THE knob.
""")
print("=" * 88)
