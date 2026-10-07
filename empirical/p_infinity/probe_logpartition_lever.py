"""
THE LOG-PARTITION LEVER, tested (GPD paranoid pass).

The proposed proof: log-partition Phi convex => Fisher PSD => KL D(P_beta||u)>=0 (Gibbs) => Weil
positivity => RH; with Euler product (T0 Thm 4.7 separability) protecting it in the infinite limit.

This script tests the ONE load-bearing identification "Weil quadratic form = KL/Bregman divergence",
because if it held, RH would be proved. It does not. The exact gap (the program's own Tower Theorem):
the KL/Fisher is the order-2 ADDITIVE object, which over Q is DEFINITE <=> VACUOUS -- it holds for
RH-respecting AND RH-violating data alike, so it cannot encode RH. The Weil form's RH-content is the
PRIME-SUBTRACTED part (the minus sign the proposal itself identifies as the absorption/Legendre/(-1)^n),
which is NOT a single convex KL but a DIFFERENCE of convex potentials -> indefinite -> = RH (arch-domination).

Three decisive tests + the genuine deposit. mpmath/sympy. No torch.
"""
import mpmath as mp, sympy as sp
mp.mp.dps = 25

def KL_from_uniform(xledger, beta):
    """D(P_beta || u) = log N - H(P_beta), the T0 conjugate potential (Thm 2.7). >=0 by Gibbs, any ledger."""
    x = [mp.mpf(v) for v in xledger]; N = len(x)
    g = mp.e**(sum(mp.log(v) for v in x)/N)         # geometric mean
    y = [mp.log(v) - mp.log(g) for v in x]          # centered log-ledger
    w = [mp.e**(beta*yi) for yi in y]; Z = sum(w)
    P = [wi/Z for wi in w]
    H = -sum(p*mp.log(p) for p in P if p > 0)
    return mp.log(N) - H

print("="*86)
print("TEST 1 -- the user's true facts: KL = conjugate potential >= 0 for ANY ledger (Gibbs, VACUOUS)")
print("="*86)
import random
random.seed(7)
ledgers = {
    "uniform-ish":       [1.0, 1.01, 0.99, 1.02],
    "random A":          [random.uniform(0.2, 5) for _ in range(6)],
    "random B":          [random.uniform(0.2, 5) for _ in range(6)],
    "zeta-like (mult.)": [1, 2, 3, 5, 7, 11],          # a 'multiplicative' ledger
    "DH-like (perturbed)":[1, 2, 3, 5, 7, 11.7],       # a non-multiplicative perturbation
}
print(f"  {'ledger':>22} {'beta=0.5':>12} {'beta=1.5':>12} {'beta=-2':>12} {'all >=0?':>9}")
for name, x in ledgers.items():
    vals = [KL_from_uniform(x, b) for b in (0.5, 1.5, -2.0)]
    print(f"  {name:>22} " + " ".join(f"{mp.nstr(v,6):>12}" for v in vals) + f" {str(all(v>=0 for v in vals)):>9}")
print("""  => D(P_beta||u) >= 0 for EVERY ledger -- structured, random, multiplicative, OR perturbed. It is
     Gibbs' inequality; it knows NOTHING about RH. This is the VACUOUS order-2 positivity (Tower Theorem:
     additive/Fisher = definite <=> vacuous). It cannot, by itself, encode or prove RH.""")

print("="*86)
print("TEST 2 -- KL is blind to the RH-distinguishing structure; only the cross-prime FUSION defect sees it")
print("="*86)
# T0 Thm 4.7: fusion/Euler-product => separable => cross-prime defect Delta_y(beta) = K_y - sum_i K_{y^(i)} = 0.
# We compare a SEPARABLE (Euler/multiplicative) ledger vs a NON-separable (DH-like cross-prime) ledger on Z/6.
def K(xledger, beta):
    x=[mp.mpf(v) for v in xledger]; N=len(x); g=mp.e**(sum(mp.log(v) for v in x)/N)
    y=[mp.log(v)-mp.log(g) for v in x]
    return mp.log(sum(mp.e**(beta*yi) for yi in y)/N)
# Z/6 = Z/2 x Z/3 ; ledger indexed by (s2,s3). Separable: y = a(s2)+b(s3). Non-sep: + cross term.
import itertools
idx = list(itertools.product(range(2), range(3)))
a2 = {0:0.3, 1:-0.3}; b3 = {0:0.5, 1:-0.1, 2:-0.4}
sep   = [mp.e**(a2[s2]+b3[s3]) for (s2,s3) in idx]                       # separable (Euler/multiplicative)
nonsep= [mp.e**(a2[s2]+b3[s3] + (0.6 if (s2,s3) in [(1,2),(0,0)] else -0.4)) for (s2,s3) in idx]  # + cross term
def fusion_defect(x):
    # Delta = K_full(beta) - [K_axis2(beta)+K_axis3(beta)] at beta=1 (vanishes iff separable)
    b=mp.mpf(1)
    x2=[mp.mpf(v) for v in x]; N=6; g=mp.e**(sum(mp.log(v) for v in x2)/N); y=[mp.log(v)-mp.log(g) for v in x2]
    Kf=mp.log(sum(mp.e**(b*yi) for yi in y)/N)
    # marginal over axis-3 (average), then axis-2 cumulant, and vice versa (Hoeffding axes)
    yA2=[sum(y[i] for i in range(6) if idx[i][0]==s2)/3 for s2 in range(2)]
    yA3=[sum(y[i] for i in range(6) if idx[i][1]==s3)/2 for s3 in range(3)]
    K2=mp.log(sum(mp.e**(b*v) for v in yA2)/2); K3=mp.log(sum(mp.e**(b*v) for v in yA3)/3)
    return Kf-(K2+K3)
print(f"  {'ledger':>26} {'D(P||u)>=0 (KL)':>16} {'fusion defect Delta':>20} {'distinguishes RH?':>18}")
for name,x in [("separable (Euler/mult.)",sep),("non-sep (DH-like cross)",nonsep)]:
    kl=KL_from_uniform(x,1.0); fd=fusion_defect(x)
    print(f"  {name:>26} {str(kl>=0):>16} {mp.nstr(fd,6):>20} {'(only Delta)':>18}")
print("""  => KL>=0 for BOTH (vacuous). The cross-prime FUSION defect Delta is ~0 for the separable
     (Euler-product/multiplicative) ledger and != 0 for the non-separable (DH-like) one -- THIS is what
     distinguishes the zeta class from Davenport-Heilbronn (N9). But (N9, proven) fusion closure is
     NECESSARY, NOT SUFFICIENT: it discharges DH; it does not prove RH for genuine zeta. The KL convexity
     rides on 'valid family', which holds regardless of RH; separability is the DH-filter, not RH.""")

print("="*86)
print("TEST 3 -- the minus sign (absorption/Legendre/(-1)^n) breaks the KL: Weil = (convex) - (prime)")
print("="*86)
def signature(M):
    lam=sp.symbols('lam'); rs=sp.Poly(sp.expand(M.charpoly(lam).as_expr()),lam).real_roots()
    p=sum(1 for r in rs if r.is_positive); n=sum(1 for r in rs if r.is_negative); return p,len(rs)-p-n,n
q=7
print(f"  F_q primitive form M=[[-2q,-a],[-a,-2]] (q={q}): diagonal = the convex/'KL' energy part (always")
print(f"  definite); off-diagonal -a = the PRIME minus (absorption/Legendre). RH = the minus doesn't break it.")
print(f"  {'a (prime flux)':>16} {'diagonal def?':>14} {'full M signature':>18} {'M neg-def (RH)?':>16}")
for a in (0, 4, 6):
    diag = sp.Matrix([[-2*q,0],[0,-2]]); full = sp.Matrix([[-2*q,-a],[-a,-2]])
    dd = signature(diag)==(0,0,2); sg = signature(full)
    print(f"  {a:>16} {str(dd):>14} {str(sg):>18} {str(sg==(0,0,2)):>16}")
print("""  => the DIAGONAL ('convex/KL energy', no prime) is ALWAYS negative-definite (the vacuous positivity);
     the OFF-DIAGONAL -a (the prime minus the proposal itself names as absorption/(-1)^n) is what flips the
     full form indefinite for |a|>2sqrt q. The full Weil form is (convex) MINUS (prime) -- a DIFFERENCE of
     convex potentials, NOT a single convex KL -> NOT automatically positive. RH = the convex part dominates
     the prime subtraction (|a|<=2sqrt q = arch-domination). The very minus sign that makes the dictionary
     beautiful is exactly what defeats 'KL => positive'.""")

print("="*86)
print("VERDICT (calibrated)")
print("="*86)
print("""  GENUINE DEPOSITS (real, keep):
   * The Connes dictionary is accurate: K*_y(xi)=D(P_beta||u) (T0 Thm 2.7) maps to Connes' archimedean
     W_inf; the absorption spectrum = the Legendre minus = the (-1)^n transfer (N5). Beautiful & correct.
   * CONNES' OPEN QUESTION 1 (conceptual reason for ARCHIMEDEAN positivity W_inf>=0): the KL/relative-entropy
     framing IS a genuine candidate conceptual reason -- the archimedean (convex) part is a relative entropy,
     >=0 by Gibbs. [A] (the precise identity W_inf = D needs checking; structurally it answers the lament.)
   * Separability = the N9 cross-prime fusion / DH-filter (Euler product => no cross-prime interaction).
  THE GAP (why it does NOT close RH):
   * 'Weil form = KL' is FALSE -- it is the Tower-Theorem conflation. KL/Fisher (order-2 additive) is
     definite <=> VACUOUS (Test 1: holds for random & DH-like ledgers); it cannot encode RH.
   * The primes enter with the Legendre MINUS (Test 3); the full Weil form is (convex KL) - (prime), a
     DIFFERENCE of convex potentials, indefinite; RH = the convex dominates the subtraction = arch-domination.
   * Separability is NECESSARY-NOT-SUFFICIENT (N9): it kills DH; the residue for genuine zeta is the
     ARCHIMEDEAN domination, not the multiplicative separability.
  NET: the log-partition lever answers Connes Q1 CONCEPTUALLY on the archimedean (KL) side -- a real deposit
  -- but the prime minus sign (the program's own (-1)^n/absorption) breaks the convex-KL structure exactly
  where RH lives. The convexity gives the vacuous half for free; RH is the contentful half it cannot see.""")
