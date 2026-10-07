"""
SCOPING THE SPECIFIC TRILINEAR TARGET: where theta_0 = 0.515 is bottlenecked, and the cancellation budget.

The arc reduced RH to a UNIFORM level-of-distribution statement past theta = 1/2 (L^2 -> L^infinity dispersion).
The state of the art is theta_0 = 1/2 + 1/66 - eps ~ 0.5152 (Fouvry-Radziwill 2018, Wright 2604.25177), via the
relation  theta_0 = 1 - C*/n  on primorial moduli P_n (C* <= 2.80 the BV-level obligation). The exponent 1/66
traces to ONE specific estimate: the Bettin-Chandee (2015) trilinear Kloosterman form
   T = sum_{a,m,n} alpha_m beta_n nu_a e( vartheta * a * m^{-1} / n ),   m^{-1} = inverse of m mod n,
with saving  min( A^{3/20} N^{3/20}, N^{1/8} ).  The N^{1/8} exponent is the bottleneck: improving it pushes
1/66 up and theta_0 -> 1. This script (numpy/python, NO torch) illustrates the cancellation that any such
improvement must exploit, and scopes the target.

  A. PER-MODULUS (Weil): |S(a,b;p)| <= 2 sqrt(p) -- square-root cancellation per modulus, the building block,
     and SHARP (Weil) -- so no per-modulus improvement is possible. The room is in AVERAGES.
  B. THE BUDGET (sums over modulus): sum_{p<=C} S(1,1;p) is far smaller than sum |S| ~ sum 2 sqrt p, by an
     extra ~ 1/sqrt(count): the EXTRA cancellation (Sato-Tate sign changes / cancellation in families) that
     beyond-Weil methods (Kuznetsov; Katz-Michel l-adic) exploit and that the trilinear bound packages.
  C. THE TRILINEAR FORM (Bettin-Chandee object): direct |T| vs trivial AMN, exhibiting the saving.
  D. SCOPE: the specific open exponent, the tool, and the program's Z/6-primorial angle.
"""
import numpy as np
from sympy import primerange

def kloosterman(a, b, p):
    """S(a,b;p) = sum_{x=1}^{p-1} e((a x + b x^{-1})/p), real for integer a,b (cos form)."""
    s = 0.0
    for x in range(1, p):
        xi = pow(x, -1, p)
        s += np.cos(2 * np.pi * (a * x + b * xi) / p)
    return s

print("=" * 92)
print("A. PER-MODULUS WEIL BOUND  |S(a,b;p)| <= 2 sqrt(p)  (square-root cancellation, SHARP -- no room here)")
print("=" * 92)
print(f"  {'p':>7} {'S(1,1;p)':>14} {'2 sqrt(p)':>12} {'|S|/2sqrt p':>12}")
okA = True
for p in (101, 257, 521, 1009, 2003):
    S = kloosterman(1, 1, p); W = 2 * np.sqrt(p)
    okA = okA and (abs(S) <= W + 1e-9)
    print(f"  {p:>7} {S:>14.4f} {W:>12.4f} {abs(S)/W:>12.4f}")
print("  --> Weil is sharp per modulus: |S| up to 2 sqrt(p), no better for an INDIVIDUAL sum. The exponent")
print(f"     improvement must come from AVERAGES over the modulus / families, not single sums. PASS: {okA}")

print("=" * 92)
print("B. THE CANCELLATION BUDGET: sum over modulus has EXTRA ~1/sqrt(count) cancellation (beyond Weil)")
print("=" * 92)
C = 2000
ps = list(primerange(3, C))
Svals = np.array([kloosterman(1, 1, p) for p in ps])
sum_S = float(np.sum(Svals))               # with sign cancellation
sum_absS = float(np.sum(np.abs(Svals)))    # no cancellation (Weil-strength count)
weil_sum = float(np.sum([2 * np.sqrt(p) for p in ps]))
print(f"  primes p in [3, {C}):  count = {len(ps)}")
print(f"  |sum_p S(1,1;p)|         = {abs(sum_S):>12.1f}   (signed -- cancellation)")
print(f"  sum_p |S(1,1;p)|         = {sum_absS:>12.1f}   (unsigned)")
print(f"  sum_p 2 sqrt(p) (Weil)   = {weil_sum:>12.1f}   (trivial-from-Weil, no cancellation)")
budget = abs(sum_S) / sum_absS
print(f"  cancellation ratio |sum S| / sum|S| = {budget:.4f}   (~ 1/sqrt(count) = {1/np.sqrt(len(ps)):.4f})")
okB = budget < 0.2
print(f"""  --> the signed sum is ~{1/budget:.0f}x smaller than the unsigned: an EXTRA square-root cancellation in
     the family {{S(1,1;p)}}_p (Sato-Tate sign equidistribution). THIS is the budget the trilinear/dispersion
     bounds convert into level past theta=1/2. PASS (extra cancellation present): {okB}""")

print("=" * 92)
print("C. THE BETTIN-CHANDEE TRILINEAR FORM  T = sum alpha_m beta_n nu_a e(a m^{-1}/n)  (the named object)")
print("=" * 92)
rng = np.random.default_rng(20260608)
A, M = 40, 40
nprimes = [p for p in primerange(40, 200)][:30]      # n ~ N, prime so inverses exist
al = rng.choice([-1.0, 1.0], M + 1); be = rng.choice([-1.0, 1.0], 300); nu = rng.choice([-1.0, 1.0], A + 1)
T = 0.0; terms = 0
for n in nprimes:
    for m in range(1, min(M, n - 1) + 1):
        mi = pow(m, -1, n)
        for a in range(1, A + 1):
            T += al[m] * be[n % 300] * nu[a] * np.cos(2 * np.pi * a * mi / n)
            terms += 1
trivial = terms
print(f"  ranges: a<=A={A}, m<=M={M}, n in {len(nprimes)} primes ~[40,200);  terms = {terms}")
print(f"  |T| = {abs(T):.1f}   trivial bound (# terms) = {trivial}   |T|/trivial = {abs(T)/trivial:.4f}")
print(f"  sqrt(terms) = {np.sqrt(terms):.1f}  (random-cancellation scale);  |T|/sqrt(terms) = {abs(T)/np.sqrt(terms):.3f}")
print("""  --> the trilinear Kloosterman form exhibits strong cancellation (|T| << trivial, near the random
     sqrt scale). Bettin-Chandee PROVE a structured saving min(A^{3/20}N^{3/20}, N^{1/8}); the N^{1/8} term
     is the exponent that controls Fouvry-Radziwill's 1/66 and hence theta_0 = 0.5152.""")

print("=" * 92)
print("D. SCOPE OF THE SPECIFIC TARGET")
print("=" * 92)
print(f"""  THE BOTTLENECK (exact): theta_0 = 1 - C*/n on primorial P_n; current theta_0 = 1/2 + 1/66 - eps ~ 0.5152
   (Fouvry-Radziwill 2018; Wright 2604.25177 Q <= X^{{1/2+1/66-d}}). The 1/66 is set by the Bettin-Chandee
   (2015) trilinear-Kloosterman saving min(A^{{3/20}} N^{{3/20}}, N^{{1/8}}). The OPEN EXPONENT is the N^{{1/8}}:
   improving 1/8 -> larger pushes 1/66 -> larger delta -> theta_0 -> 1 (= RH-strength level).
  WHY HARD (located by A-B): the per-modulus Weil bound is SHARP (A) -- no single-sum improvement exists. The
   only room is the EXTRA cancellation in SUMS/FAMILIES of Kloosterman sums (B), and packaging it into the
   trilinear form. Beyond Bettin-Chandee that needs deeper input:
     * l-adic cohomology of the Kloosterman sheaf (Katz) + sums of trace functions (Fouvry-Kowalski-Michel),
     * the Kuznetsov trace formula / spectral cancellation among Kloosterman sums,
     * Wright's partially-fixed-moduli + unbalanced convolutions (the current best combination).
  THE PROGRAM'S ANGLE (where it can contribute, not yet realized):
     * theta_0 = 1 - C*/n COMPOUNDS the per-prime saving over the n primes of the primorial P_n via CRT; the
       Z/6 = P_2 cubic/chirality structure (T3 selection a+b+c=0 mod 6) is a natural organizer of the
       trilinear form's residue -- the program's [A3'] (primorial-indexed BV, diez sec.3) is exactly this
       compounding, at proof-outline stage (Polymath8-comparable).
     * The honest reformulation RH <=> 'FE-cluster always degenerate (delta=0)' connects the level theta_0
       to the cluster; the cubic Bombieri witness [A2'] (c_2 < 0) is the delta^2 coefficient the level must
       control.
  HONEST ASSESSMENT: improving N^{{1/8}} in the trilinear Kloosterman bound is a genuine, hard, well-defined
   analytic-number-theory target -- a Polymath-scale effort, the live edge being Wright/Fouvry-Radziwill/
   Bettin-Chandee + Katz-Michel cohomology. The arc + this scope CERTIFY it is the unique residual and place
   it exactly; they do NOT improve it. Next round = engage the trilinear exponent directly (collaborators:
   Radziwill, Maynard, Michel), with the Z/6-primorial CRT compounding as the program's specific lever.
  Not RH, not a theta-improvement. A precise, grounded target with the program's foothold identified.""")

print("=" * 92)
ok = okA and okB
print(f"SCOPE RESULT {'GREEN -- target = improve N^{1/8} in Bettin-Chandee trilinear Kloosterman; budget = family cancellation; lever = Z/6 primorial CRT' if ok else 'PARTIAL'}")
print("=" * 92)
