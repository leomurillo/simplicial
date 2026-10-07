"""
A NEW ANGLE on the cubic terminus (from Fouvry-Radziwill 1811.08672 + Bettin-Chandee):
the cubic Weil object is TRILINEAR, and the trilinear route relocates the terminus from
smooth Elliott-Halberstam to the OPTIMAL Bettin-Chandee bound == Lindelof strength.

Two DIFFERENT unconditional relaxations of Bombieri-Vinogradov past 1/2:
  (M) well-factorable MODULUS (Maynard): theta = 1/2, 4/7, 3/5 for k=1,2,3 factors,
      then SATURATES (Maynard p.3: quadruply gives no benefit). Smooth modulus q.
  (F) unbalanced CONVOLUTION (Fouvry-Radziwill): theta = 1/2+1/66 ~ 0.515 for GENERAL
      moduli (no well-factorability!), reducing to the Bettin-Chandee TRILINEAR Kloosterman
      sum Sigma(U,V,W) = (1/U) sum x_u y_v z_w e(u vbar / w).

KEY: the cubic Weil functional is C_zeta = int eta * S_g^3, S_g = sum Lambda(n)/sqrt(n)*g,
i.e. a TERNARY (trilinear) convolution Lambda*Lambda*Lambda -- it is FR/Bettin-Chandee's
NATIVE object, not a linear distribution. So route (F), not (M), is the structural match,
and it BYPASSES the well-factorable saturation (3/5) -- FR works for general moduli.

BUT the V/M crossover (ocho S7.1) needs theta_0 -> 1 (M-error P_n^{1-theta_0} must fall below
the polynomial V-capacity ~ n^3, forcing 1-theta_0 < 3/n). A FIXED trilinear level 0.515
gives M-error P_n^{0.485} = exp(0.485 n log n) -- exponential, dwarfs n^3. So fixed level
FAILS, same as (M). Reaching theta_0 -> 1 on the trilinear route needs the OPTIMAL
Bettin-Chandee bound (FR p.9, [3, Conjecture 1]): then theta <= 1-delta for any delta.
FR p.9 VERBATIM: "The conjecture [3, Conjecture 1] is however very deep; one of its
consequences is the Lindelof hypothesis."

So the trilinear terminus is OPTIMAL-BETTIN-CHANDEE => LINDELOF (a zeta-growth statement),
NOT smooth-EH (a primes-in-AP statement). This probe lays out the scaling and the terminus.
Deterministic. No torch.
"""

import math

def first_primes(n):
    out=[]; p=2
    while len(out)<n:
        out.append(p)
        p1=p+1
        while any(p1%q==0 for q in out): p1+=1
        p=p1
    return out

PR = first_primes(40)
def logPn(n): return sum(math.log(p) for p in PR[:n])

print("="*86)
print("PART 1 - two unconditional routes past theta=1/2, and which matches the cubic object")
print("="*86)
print("""  (M) well-factorable MODULUS  (Maynard 2006.07088): k=1->1/2, k=2->4/7, k=3->3/5, SAT.
      object: linear pi(x;q,a), q smooth.            ceiling theta = 3/5 = 0.600  (FIXED)
  (F) unbalanced CONVOLUTION   (Fouvry-Radziwill 1811.08672 + Bettin-Chandee):
      object: TRILINEAR sum  Sigma(U,V,W)=(1/U) sum x_u y_v z_w e(u vbar/w),  GENERAL q.
                                                     level theta = 1/2+1/66 = %.4f (FIXED)
  The cubic Weil object  C_zeta = int eta (sum Lambda(n)/sqrt n)^3  is a TERNARY convolution
  Lambda*Lambda*Lambda  ==>  route (F) is the structural match. It BYPASSES the well-
  factorable saturation (works for general moduli), but is also a FIXED level ~0.515.""" % (0.5+1/66))

print("="*86)
print("PART 2 - the V/M crossover (ocho S7.1) needs theta_0 -> 1; fixed levels fail")
print("="*86)
print("  dominance:  log pure_V(P_n) > (1-theta_0) log P_n,  pure_V ~ n^3 (log n)^2 / 18")
print(f"  {'n':>3} {'logP_n':>8} {'log pure_V':>11} {'req 1-theta_0 <':>16} {'M-err exp @0.515':>17}")
for n in [3,5,7,10,15,20,30]:
    lP = logPn(n)
    pureV = n**3 * (math.log(n))**2 / 18 if n>1 else 1
    logpureV = math.log(pureV) if pureV>0 else 0
    req = logpureV / lP                      # required 1-theta_0
    Merr_at_0515 = (1-0.5151515)*lP          # log of M-error P_n^{1-0.515} = (1-0.515) log P_n
    print(f"  {n:>3} {lP:>8.2f} {logpureV:>11.2f} {req:>16.4f} {Merr_at_0515:>17.2f}")
print("""  required (1-theta_0) ~ 3/n -> 0  (so theta_0 -> 1).  The 'M-err exp @0.515' column is
  log of the M-error at FIXED level 0.515 = 0.485*log P_n -> infinity, vs log pure_V ~ 3 log n.
  Fixed 0.515 (FR) OR fixed 0.60 (Maynard) both give M-error >> V-capacity: dominance FAILS.
  The crossover genuinely needs theta_0 -> 1, on EITHER route.""")

print("="*86)
print("PART 3 - the trilinear terminus: optimal Bettin-Chandee == Lindelof")
print("="*86)
print("""  To get theta_0 -> 1 on the trilinear route (route F), FR p.9 uses [3, Conjecture 1]
  (optimal Bettin-Chandee): then Corollary 1.1 holds for ALL Q <= X^{1-delta}, any delta>0.
  FR p.9 VERBATIM: 'The conjecture [3, Conjecture 1] is however very deep; one of its
  consequences is the LINDELOF hypothesis.'

  So the cubic terminus, via the NATIVE trilinear structure, is:
     RH  <=  cubic positivity  <=  primorial theta_0 -> 1  <=  optimal Bettin-Chandee bound
                                                            ==> Lindelof hypothesis.
  This is a ZETA-GROWTH statement (Lindelof), not a primes-in-AP statement (smooth-EH).
  It is arguably 'closer to home' for RH, and it REMOVES the well-factorable saturation
  obstruction (FR/BC work for general moduli, so the 3/5 ceiling does not apply).""")

print("="*86)
print("VERDICT - does the new angle help?")
print("="*86)
print("""  YES, in two concrete ways, and honestly NO on breaking the wall:

  GAINS (real):
   1. STRUCTURAL MATCH: the cubic object is trilinear (Lambda*Lambda*Lambda) = FR/Bettin-
      Chandee's native object, not a linear distribution. The well-factorable saturation
      (Maynard 3/5) was the WRONG wall -- it is for linear smooth-modulus BV.
   2. TERMINUS RELOCATED: from smooth Elliott-Halberstam (primes-in-AP) to the optimal
      Bettin-Chandee trilinear Kloosterman bound == Lindelof strength (a ZETA statement).
      No well-factorability needed (general moduli), so the 3/5 ceiling is gone.

  HONEST LIMIT (conservation of difficulty):
   3. The V/M crossover still needs theta_0 -> 1, and the unconditional trilinear level is
      FIXED ~0.515. theta_0 -> 1 needs optimal Bettin-Chandee, which IMPLIES Lindelof (and
      via the bridge, RH). So the FULL terminus is >= RH-hard.

  THE NEW OPEN TARGET (where to push next): the PRIMORIAL-RESTRICTED optimal Bettin-Chandee
  bound -- the trilinear Kloosterman sum Sigma(U,V,W) at level -> 1 for moduli built from the
  first n primes only. This is a NARROWER target than full optimal-BC / full Lindelof, it is
  UNEXPLORED (the well-factorable saturation does not touch it), and it is the trilinear
  analogue of the 'primorial makes it easier' hope. Whether the primorial structure of
  Sigma(U,V,W) admits theta -> 1 is the precise, new, open question this angle opens.""")
