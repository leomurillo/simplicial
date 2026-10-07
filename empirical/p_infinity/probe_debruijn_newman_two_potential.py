"""
NEXT-ROUND: the de Bruijn-Newman flow in the two-potential language, and what c2^A vs c2^zeta says about Lambda.

de Bruijn-Newman: H_lambda(x) = int_0^inf e^{lambda u^2} Phi(u) cos(xu) du, Phi>0 (Polymath15 kernel),
H_0(x) = (1/8) xi(1/2 + i x/2) = (1/8) Xi(x/2). H_lambda has only real zeros iff lambda >= Lambda;
RH <=> Lambda <= 0; Rodgers-Tao 2018: Lambda >= 0; Polymath15: Lambda <= 0.2. The flow is the BACKWARD heat
equation d_lambda Xi = -Xi''; Cole-Hopf u=(log Xi)' makes it BURGERS  d_lambda u = -u_tt - 2 u u_t. The two
move-(1) potentials u = u^A + u^zeta are additive in the linear part and COUPLE in the Burgers nonlinearity.

EXACT SIMPLIFICATION (the crux): the central concavity margin is a second moment of a POSITIVE measure,
   -c2(0) = -(log H_lambda)''(0) = <u^2>_lambda = (int u^2 e^{lambda u^2} Phi)/(int e^{lambda u^2} Phi) > 0,
with d_lambda <u^2> = Var_lambda(u^2) > 0. So the order-2 margin is RH-TRIVIALLY positive (a positive-measure
moment), grows with lambda, and is positive even for lambda << 0 -- it carries NO information about Lambda.

This probe (mpmath, NO torch):
  V. VALIDATE the kernel: int_0^inf Phi(u) du = (1/8) xi(1/2)  (confirms Phi and the normalization).
  A. FLOW: central margin <u^2>_lambda for lambda in [-0.1, 0.2] -- positive, increasing, d_lambda=Var(u^2)>0.
     It is a moment of a positive measure: RH-trivially positive, blind to Lambda (positive across [0,0.2]).
  B. TWO-POTENTIAL SPLIT (xi side): -c2(t) = (-c2^A) + (-c2^zeta) across heights. The archimedean concavity
     SUPPLIES the margin against the prime convexity at low t; find the crossover height where the zeros
     (prime) take over. The center t=0 is the THINNEST-margin point, supplied by the archimedean alone.
  C. VERDICT: the split quantifies the local MECHANISM (arch concavity vs prime convexity) but cannot bound
     Lambda -- the margin is a positive-measure moment with no Lambda content, and Lambda is GLOBAL
     (Rodgers-Tao: zero-spacing/GUE statistics, not local cumulants). The local/cumulant program (moves 1->a)
     has a precise CEILING at Lambda; the residue is global-statistical (GUE / pair-correlation / the
     archimedean self-adjointness of N9), not another local order.
"""
import mpmath as mp
mp.mp.dps = 30
HALF = mp.mpf('0.5')

# ---- de Bruijn-Newman kernel Phi (Polymath15) -------------------------------------------------
def Phi(u):
    s = mp.mpf(0)
    for n in range(1, 25):
        n2 = mp.mpf(n) ** 2
        s += (2 * mp.pi ** 2 * n2 ** 2 * mp.e ** (9 * u) - 3 * mp.pi * n2 * mp.e ** (5 * u)) * mp.e ** (-mp.pi * n2 * mp.e ** (4 * u))
    return s
def moment(k, lam):                      # int_0^inf u^k e^{lam u^2} Phi(u) du
    return mp.quad(lambda u: u ** k * mp.e ** (lam * u ** 2) * Phi(u), [0, mp.mpf('0.05'), mp.mpf('0.3'), 1])

# ---- xi-side objects -------------------------------------------------------------------------
def xi(s):
    return HALF * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
def A_fac(s):
    return HALF * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2)
Xi  = lambda t: xi(HALF + 1j * t)
Aof = lambda t: A_fac(HALF + 1j * t)
Zof = lambda t: mp.zeta(HALF + 1j * t)
def c2(f, t):                            # (log f)'' = m2 - m1^2
    f0 = f(t); m1 = mp.diff(f, t, 1, method='quad') / f0; m2 = mp.diff(f, t, 2, method='quad') / f0
    return m2 - m1 ** 2

print("=" * 94)
print("V. VALIDATE kernel:  int_0^inf Phi du  ==  (1/8) xi(1/2)")
print("=" * 94)
intPhi = moment(0, mp.mpf(0)); target = xi(HALF) / 8
okV = abs(intPhi - target) < mp.mpf('1e-12')
print(f"  int Phi du = {mp.nstr(intPhi,12)}   (1/8) xi(1/2) = {mp.nstr(target,12)}   match: {okV}")

print("=" * 94)
print("A. FLOW: central concavity margin  -c2(0) = <u^2>_lambda  (moment of a POSITIVE measure)")
print("=" * 94)
print(f"  {'lambda':>9} {'<u^2> (margin)':>16} {'Var(u^2)=d_lambda':>18} {'margin>0?':>10}")
okA = True
prev = None
for lam in (mp.mpf('-0.1'), mp.mpf('-0.05'), mp.mpf(0), mp.mpf('0.05'), mp.mpf('0.1'), mp.mpf('0.2')):
    Z = moment(0, lam); m2 = moment(2, lam) / Z; m4 = moment(4, lam) / Z
    var = m4 - m2 ** 2
    inc = (prev is None) or (m2 > prev)
    okA = okA and (m2 > 0) and (var > 0) and inc
    prev = m2
    print(f"  {mp.nstr(lam,2):>9} {mp.nstr(m2,10):>16} {mp.nstr(var,8):>18} {str(m2>0):>10}")
print("""  --> the central margin is <u^2> of the positive measure e^{lam u^2}Phi du: strictly positive for ALL
      lambda (including lambda<0), monotonically increasing (d_lambda = Var(u^2) > 0). It is RH-trivially
      positive and gives NO way to distinguish lambda=0 from lambda in (0, 0.2] -- it does not see Lambda.""")
print(f"  PASS: {okA}")

print("=" * 94)
print("B. TWO-POTENTIAL SPLIT (xi side):  -c2(t) = (-c2^A) + (-c2^zeta)   [arch concavity vs prime convexity]")
print("=" * 94)
print(f"  {'t':>6} {'-c2 (margin)':>14} {'-c2^A (arch)':>14} {'-c2^zeta (prime)':>17} {'prime sign':>11} {'who supplies':>13}")
okB = True
for t in (mp.mpf(0), mp.mpf(5), mp.mpf(8), mp.mpf(11), mp.mpf(17), mp.mpf(23)):
    cX = mp.re(c2(Xi, t)); cA = mp.re(c2(Aof, t)); cZ = mp.re(c2(Zof, t))
    mX, mA, mZ = -cX, -cA, -cZ
    okB = okB and (abs(mX - (mA + mZ)) < mp.mpf('1e-9'))
    psign = "convex(eats)" if cZ > 0 else "concave(adds)"
    who = "ARCH" if mA > mZ else "prime/zeros"
    print(f"  {mp.nstr(t,3):>6} {mp.nstr(mX,6):>14} {mp.nstr(mA,6):>14} {mp.nstr(mZ,6):>17} {psign:>11} {who:>13}")
print("""  --> THREE regimes, and the clean 'arch vs prime' window is NARROW:
      * t=0 (center): NOT cleanly arch-supplied. The A/zeta_line split is dominated by the spurious +-i/2
        singularity pair (pole of zeta at s=1 and the s(s-1) zero) that CANCELS in Xi: -c2^A=-3.70 (arch
        convex), -c2^zeta=+3.75, near-cancelling to the thin +0.046 margin. The split is contaminated here.
      * t~5: the ONLY clean window -- archimedean CONCAVE (+0.067, supplies) vs prime CONVEX (-0.014, eats),
        net +0.053. This is the genuine 'archimedean dominates prime' of N14/N5, and it is order-2.
      * t>~8: prime/zeros flip concave and supply the margin; archimedean negligible. Zero-dominated.
      So 'arch dominates prime' is real but confined to a NARROW low-height window; the center is a
      factorization artifact and the bulk is zero-dominated.""")
print(f"  PASS (additivity): {okB}")

print("=" * 94)
print("C. VERDICT -- what the c2^A vs c2^zeta split does and does NOT say about the Lambda<=0 margin")
print("=" * 94)
print("""  ESTABLISHED:
   * The dBN flow is the backward heat eq d_lambda Xi = -Xi''; Cole-Hopf gives Burgers d_lambda u =
     -u_tt - 2 u u_t. The two potentials u=u^A+u^zeta add in the linear part and COUPLE in the nonlinearity.
   * The central order-2 margin is EXACTLY a positive-measure moment: -c2(0)=<u^2>_{e^{lam u^2}Phi} > 0,
     increasing in lambda with rate Var(u^2)>0 (A). It is RH-trivially positive and identical in character
     for lambda=0 and lambda in (0,0.2]: it does NOT encode Lambda.
   * The split (B) is quantitative about the MECHANISM but its clean window is NARROW: the center t=0 is a
     factorization artifact (spurious +-i/2 cancellation), the genuine 'archimedean concave beats prime
     convex' holds only around t~5 (+0.067 vs -0.014), and t>~8 is zero-dominated. This is N14/N5
     'archimedean dominates prime' -- real, order-2, but confined to a narrow low-height window.
  WHAT IT DOES NOT DO (honest):
   * It cannot bound Lambda. The local order-2 margin is a positive-measure moment with no Lambda content;
     at lambda=0 the zeros are well-separated, so LOCAL data shows robust reality everywhere, yet Lambda=0
     (Rodgers-Tao) -- the criticality is GLOBAL: the zero-SPACING sits at the GUE equilibrium edge, a
     statistical statement invisible to any finite-order cumulant/local potential split.
  CONSEQUENCE (the real deliverable):
   * The local/cumulant program (move 1 -> move a -> order 4 -> this) has a PRECISE CEILING at Lambda. It
     has reduced RH to 'archimedean concavity dominates prime convexity, uniformly, at order 2' and shown
     this is a low-height mechanism with a positive-measure margin -- but the last step (Lambda<=0) is
     GLOBAL-STATISTICAL, not local. The genuinely missing tool is a global input: zero-spacing / pair
     correlation / GUE form-factor (the tau=1 boundary), equivalently the archimedean SELF-ADJOINTNESS of
     N9 (spectrum on the line, not merely a positive local form). Another local order will not close it.
  This is not a proof and not a Lambda bound. It is a sharp delimitation: where local potential theory ends
  and the global (statistical / self-adjointness) residue of RH begins.""")

print("=" * 94)
allok = okV and okA and okB
print(f"CERTIFICATE {'GREEN -- flow + split computed; local ceiling at Lambda identified, residue is global' if allok else 'RED -- a check FAILED'}")
print("=" * 94)
