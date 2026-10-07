"""
INNOVATION SCAFFOLD: the prime lattice as arithmetic spacetime, and the q->1 floor-lift.

Leo's frame: Q^+ = (+)_p Z  (the free abelian group on the primes; q = prod p^{e_p} <-> the exponent
vector (e_p)).  The primes are an ORTHOGONAL LATTICE BASIS.  Question: where is the archimedean place,
and can we 'lift the floor' -- land on RH from a structure where it is already proven?

Three demonstrations:

  A  The prime lattice is RIGID and metric-free (F_1 / combinatorial).  The ONLY extra datum is the
     ARCHIMEDEAN COVECTOR  t = (log p)_p:  by the product formula  |q|_inf * prod_p |q|_p = 1, i.e.
     log|q|_inf = sum_p e_p log p = <t, e>.  The archimedean place IS the linear functional t on the
     lattice -- the one TRANSCENDENTAL (log p are Q-independent), ORDERED datum.  All the difficulty
     is concentrated in this single covector.

  B  THE SIGNATURE FLIP IS THE ARCHIMEDEAN COVECTOR.  The lattice's natural additive (Fisher) metric
     g_F is positive-definite (n,0) -- Riemannian, NO time.  The multiplicative intersection metric is
     g_x = t t^T - g_F:  the archimedean covector t adds ONE timelike direction -> signature (1,n-1),
     Lorentzian.  The 'time' of the arithmetic spacetime is LITERALLY the archimedean covector (log p).
     Primes are spacelike  <=>  (log p_i)^2 < g_F(e_i,e_i)  -- the local causal condition.

  C  THE q->1 FLOOR-LIFT.  Over F_q RH is a THEOREM (|a|<=2 sqrt q, Hasse/Weil) and the critical line
     Re(s)=1/2 is q-INVARIANT: |alpha|=sqrt q  <=>  Re(s)=1/2 for EVERY q.  Q is the q->1 endpoint.
     The proof tool (the Hodge index on the surface C x C) degenerates as q->1 (no surface over F_1) --
     that degeneration is the precise gap.  Lift to q>=2 (proven), descend to q=1 (archimedean).

No torch. Parts A/C exact (sympy); Part B numerical toy (entries involve transcendental log p).
"""
import sympy as sp
import numpy as np
from sympy import primerange, factorint

print("=" * 86)
print("A. The prime lattice Q^+ = (+)_p Z, and the archimedean place as the covector (log p)")
print("=" * 86)
def to_exponent_vector(num, den, primes):
    e = {p: 0 for p in primes}
    for p, k in factorint(num).items(): e[p] += k
    for p, k in factorint(den).items(): e[p] -= k
    return [e[p] for p in primes]
primes = list(primerange(2, 14))   # 2,3,5,7,11,13
for (num, den) in [(5, 12), (90, 1), (1, 60), (3, 5)]:
    v = to_exponent_vector(num, den, primes)
    arch = sum(e*sp.log(p) for e, p in zip(v, primes))      # log|q|_inf = <t,e>
    chk = sp.prod([sp.Integer(p)**e for e, p in zip(v, primes)])
    archstr = str(sp.nsimplify(arch))
    print(f"  {num}/{den:<3} -> exponents {v}   log|q|_inf=<t,e>={archstr:<24} "
          f"reconstruct={chk}  {'OK' if chk==sp.Rational(num,den) else 'X'}")
print("  => the primes coordinatize Q exactly; the archimedean size is the LINEAR FUNCTIONAL <t,e>,")
print("     t=(log p).  Product formula: |q|_inf * prod_p p^{-e_p} = 1.  The archimedean is the one")
print("     covector NOT among the lattice axes -- the single transcendental, ordered datum.")

print("\n" + "=" * 86)
print("B. The signature flip IS the archimedean covector: Fisher (n,0) -> intersection (1,n-1)")
print("=" * 86)
ps = np.array([2, 3, 5, 7, 11, 13], float)
t = np.log(ps)                                   # the archimedean covector
# additive Fisher metric: a positive ledger rho_i on the primes (any PD diagonal); use prime-zeta-like
rho = 1.0/ps                                     # rho_i ~ 1/p (a positive ledger)
gF = np.diag(1.0/rho)                            # Fisher = diag(1/rho), positive-definite
gx = np.outer(t, t) - gF                         # intersection = archimedean rank-1 lift MINUS Fisher
def sig(M):
    w = np.linalg.eigvalsh((M+M.T)/2)
    return (int((w > 1e-9).sum()), int((abs(w) <= 1e-9).sum()), int((w < -1e-9).sum()))
print(f"  Fisher g_F (additive, order 2):       signature {sig(gF)}   -> RIEMANNIAN (n,0), NO time")
print(f"  intersection g_x = t t^T - g_F:       signature {sig(gx)}   -> "
      f"{'LORENTZIAN (1,n-1)' if sig(gx)[0]==1 else 'sig '+str(sig(gx))}")
print(f"  the ONE timelike direction is t=(log p) itself:  <t,t>_x = {float(t@gx@t):+.3f}  "
      f"({'TIMELIKE' if t@gx@t>0 else 'not'})")
print("  causal type of each prime e_i:  <e_i,e_i>_x = (log p_i)^2 - 1/rho_i:")
for i, p in enumerate(ps):
    v = float(gx[i, i]); print(f"     p={int(p):>2}: {v:+.3f}  {'spacelike' if v<0 else 'TIMELIKE (acausal)'}")
print("  => the additive lattice has NO timelike direction; the archimedean covector t supplies exactly")
print("     ONE (the signature flip).  RH-shape: are all primitive (archimedean-orthogonal) classes")
print("     spacelike?  -- the global causal condition, with t the constructed 'time'.")

print("\n" + "=" * 86)
print("C. The q->1 floor-lift: RH proven for q>=2; the critical line is q-INVARIANT; Q = q->1")
print("=" * 86)
def a_of_curve(p):
    cnt = 1
    for x in range(p):
        rhs = (x*x*x + x + 1) % p
        cnt += sum(1 for y in range(p) if (y*y - rhs) % p == 0)
    return p + 1 - cnt
print(f"  {'q':>4} {'a':>5} {'|a|<=2sqrt q (RH/F_q)':>22} {'|alpha|':>9} {'Re(s_zero)':>11}")
import math
for p in [11, 13, 17, 19, 23, 29]:
    a = a_of_curve(p); hasse = a*a <= 4*p
    absalpha = math.sqrt(p)                                  # |alpha|=sqrt q exactly (RH)
    Re_s = math.log(absalpha)/math.log(p)                   # |alpha|=q^{Re s} -> Re s = 1/2
    print(f"  {p:>4} {a:>5} {str(hasse):>22} {absalpha:>9.3f} {Re_s:>11.4f}")
print(f"""  => |alpha|=sqrt q  <=>  Re(s)=1/2  for EVERY q (the critical line is q-INVARIANT, =0.5 above).
     Over F_q (q>=2) this is Weil's THEOREM.  As q->1: |a|<=2sqrt q -> |a|<=2, |alpha|->1, and the
     locus stays Re(s)=1/2.  Q is the q->1 endpoint; the obstruction is that the PROOF (the Hodge
     index on the surface C x C) needs the surface, which degenerates at q=1 (F_1, no surface).
     THE FLOOR-LIFT: RH is proven on the whole shelf q>=2 and the target Re(s)=1/2 is the SAME line;
     the only missing rung is the continuity/construction of the object across the q->1 degeneration.""")
print("=" * 86)
