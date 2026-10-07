"""
NEXT-ROUND MOVE (a): the difference-of-convex (DC) potential under the functional-equation reflection.

Move (1) put both sides of the Weil form in the same currency: Weil = (archimedean relative entropy, N14)
- (prime free energy log zeta), a DIFFERENCE of convex potentials, trivially signed on Re(s)>1; RH = the
domination under continuation to the critical line. This probe pushes the reflection symmetry s<->1-s.

REALIZATION. The reflection s<->1-s is t<->-t on Xi(t)=xi(1/2+it) (real, even). RH <=> Xi has only real
zeros <=> Xi in the Laguerre-Polya (LP) class. The SECOND-ORDER shadow of LP is the first Laguerre
inequality
    L1[Xi](t) = Xi'(t)^2 - Xi(t) Xi''(t) = -Xi^2 (log|Xi|)''  >= 0   (for all real t),
i.e. log|Xi| is CONCAVE -- the reflection-symmetric DC condition (archimedean concavity dominates the prime
part). It factors EXACTLY through the two potentials of move (1): with Xi = A * zeta_line,
    L1[Xi] = L1[A] * zeta_line^2 + A^2 * L1[zeta_line],   equivalently
    (log|Xi|)'' = (log|A|)'' + (log|zeta_line|)''.

What this probe establishes (mpmath, exact-to-precision, NO torch):
  A. REFLECTION.  Xi(t)=Xi(-t), real; t<->-t is the s<->1-s fixed-line structure (critical line = fixed set).
  B. SECOND-ORDER DC SHADOW.  L1[Xi](t) >= 0 on the computed range (necessary for RH; holds), even in t.
  C. THE TWO POTENTIALS INSIDE THE CONDITION.  the exact factorization L1[Xi]=L1[A]zeta^2+A^2 L1[zeta],
     and the concavity split (log|Xi|)''=(log|A|)''+(log|zeta_line|)'' -- archimedean concavity vs prime part.
  D. L1 DETECTS OFF-AXIS ZEROS.  toy Xi=t^2+b^2 (zeros at +-ib, OFF the line) gives L1=2(t^2-b^2)<0 for
     |t|<b: the second-order shadow SEES an isolated off-line pair. (Reflection pairs zeros; L1 catches them.)
  E. VERDICT / THE RESIDUE.  L1>=0 is necessary, verified, decomposes into arch+prime, and catches isolated
     off-axis pairs -- but it is NOT sufficient. RH = the FULL LP hierarchy (all orders). The residue beyond
     L1 is "beyond second order" = the program's Conductor-Blind-Spot / cumulant-tower regime (N5 Rem 6.3:
     order-by-order identity holds; the closure across the form-factor boundary is RH).

Honest scope: locates RH as the higher-order (beyond-2) domination on the reflection fixed line. NOT a proof.
"""
import mpmath as mp
mp.mp.dps = 40
HALF = mp.mpf('0.5')

def xi(s):                       # completed zeta  xi(s)=1/2 s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
    return HALF * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
def A_fac(s):                    # archimedean factor (xi without zeta)
    return HALF * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2)

Xi   = lambda t: xi(HALF + 1j * t)            # real for real t
Aof  = lambda t: A_fac(HALF + 1j * t)         # complex on the line
Zof  = lambda t: mp.zeta(HALF + 1j * t)       # complex on the line

def fdd(f, t):                   # (f, f', f'') at real t via high-precision differentiation
    return f(t), mp.diff(f, t, 1), mp.diff(f, t, 2)
def L1_from(f0, f1, f2):
    return f1 ** 2 - f0 * f2

# zeros of Xi (= ordinates of zeta zeros) for sampling at/around them
GAMMAS = [mp.im(mp.zetazero(k)) for k in (1, 2, 3)]   # 14.1347, 21.0220, 25.0109
SAMPLES = [mp.mpf(0), mp.mpf(5), mp.mpf(10), GAMMAS[0], mp.mpf(18), GAMMAS[1], mp.mpf(28)]

print("=" * 96)
print("A. REFLECTION  Xi(t)=Xi(-t), real  (t<->-t IS the functional-equation s<->1-s; fixed set = crit. line)")
print("=" * 96)
okA = True
print(f"  {'t':>8} {'Xi(t)':>16} {'Xi(-t)':>16} {'Im Xi(t)':>12} {'even & real?':>13}")
for t in (mp.mpf('3.3'), mp.mpf(7), mp.mpf('15.5')):
    p, m = Xi(t), Xi(-t)
    ev = abs(p - m) < mp.mpf('1e-30') and abs(mp.im(p)) < mp.mpf('1e-25')
    okA = okA and ev
    print(f"  {mp.nstr(t,3):>8} {mp.nstr(mp.re(p),8):>16} {mp.nstr(mp.re(m),8):>16} {mp.nstr(mp.im(p),2):>12} {str(ev):>13}")
print(f"  --> Xi even and real: {okA}")

print("=" * 96)
print("B. SECOND-ORDER DC SHADOW  L1[Xi](t)=Xi'^2-Xi*Xi'' >= 0  (<=> log|Xi| concave; necessary for RH)")
print("=" * 96)
okB = True
print(f"  {'t':>10} {'Xi':>14} {'L1[Xi]':>18} {'d2 log|Xi|':>16} {'>=0?':>6} {'note':>10}")
L1Xi_cache = {}
for t in SAMPLES:
    f0, f1, f2 = fdd(Xi, t)
    f0, f1, f2 = mp.re(f0), mp.re(f1), mp.re(f2)
    L = L1_from(f0, f1, f2); L1Xi_cache[str(t)] = (f0, f1, f2, L)
    conc = (-L / f0 ** 2) if abs(f0) > mp.mpf('1e-12') else mp.mpf('nan')   # (log|Xi|)'' = -L1/Xi^2
    near_zero = any(abs(t - g) < mp.mpf('1e-6') for g in GAMMAS)
    note = "ZERO of Xi" if near_zero else ""
    ok = (L >= -mp.mpf('1e-12'))
    okB = okB and ok
    print(f"  {mp.nstr(t,5):>10} {mp.nstr(f0,6):>14} {mp.nstr(L,8):>18} {mp.nstr(conc,6):>16} {str(ok):>6} {note:>10}")
print("  --> L1[Xi] >= 0 on the range (= log|Xi| concave): the reflection-symmetric second-order RH shadow,")
print(f"      verified, consistent with RH. At zeros of Xi, L1 = Xi'^2 >= 0 automatically.  PASS: {okB}")

print("=" * 96)
print("C. THE TWO POTENTIALS INSIDE THE CONDITION  L1[Xi] = L1[A]*zeta^2 + A^2*L1[zeta]  (exact)")
print("=" * 96)
okC = True
print(f"  {'t':>8} {'L1[Xi] (direct)':>20} {'L1[A]z^2+A^2 L1[z]':>22} {'rel err':>10}")
for t in (mp.mpf(5), mp.mpf(10), mp.mpf(18), mp.mpf(28)):
    a0, a1, a2 = fdd(Aof, t); z0, z1, z2 = fdd(Zof, t); x0, x1, x2 = fdd(Xi, t)
    LXi = L1_from(mp.re(x0), mp.re(x1), mp.re(x2))
    LA, LZ = L1_from(a0, a1, a2), L1_from(z0, z1, z2)
    recon = LA * z0 ** 2 + a0 ** 2 * LZ
    err = abs(LXi - recon) / abs(LXi)
    okC = okC and (err < mp.mpf('1e-12')) and (abs(mp.im(recon)) < mp.mpf('1e-8'))
    print(f"  {mp.nstr(t,3):>8} {mp.nstr(LXi,12):>20} {mp.nstr(mp.re(recon),12):>22} {mp.nstr(err,3):>10}")
print("  --> the second-order condition splits EXACTLY into the archimedean form L1[A] and the prime form")
print(f"      L1[zeta_line], weighted by the other factor. Both move-(1) potentials live here. PASS: {okC}")
print("  Concavity register (log|Xi|)'' = (log|A|)'' + (log|zeta_line|)''  [arch dominance, sign<=0]:")
print(f"     {'t':>8} {'d2 log|Xi|':>15} {'d2 log|A|':>15} {'d2 log|zeta|':>16} {'sum check':>11}")
okC2 = True
for t in (mp.mpf(5), mp.mpf(10), mp.mpf(18), mp.mpf(28)):
    a0, a1, a2 = fdd(Aof, t); z0, z1, z2 = fdd(Zof, t); x0, x1, x2 = fdd(Xi, t)
    cXi = mp.re(-L1_from(mp.re(x0), mp.re(x1), mp.re(x2)) / mp.re(x0) ** 2)
    cA  = mp.re(-L1_from(a0, a1, a2) / a0 ** 2)
    cZ  = mp.re(-L1_from(z0, z1, z2) / z0 ** 2)
    err = abs(cXi - (cA + cZ))
    okC2 = okC2 and (err < mp.mpf('1e-10'))
    print(f"     {mp.nstr(t,3):>8} {mp.nstr(cXi,6):>15} {mp.nstr(cA,6):>15} {mp.nstr(cZ,6):>16} {mp.nstr(err,2):>11}")
print(f"     --> total concavity = archimedean concavity + prime term, exactly. PASS: {okC2}")

print("=" * 96)
print("D. L1 DETECTS OFF-AXIS ZEROS  toy Xi_fake(t)=t^2+b^2 (zeros +-ib OFF the line) -> L1=2(t^2-b^2)")
print("=" * 96)
b = mp.mpf(3)
okD = True
print(f"  {'t':>6} {'L1[t^2+b^2]':>16} {'2(t^2-b^2)':>14} {'sign':>6}")
for t in (mp.mpf(0), mp.mpf(1), b, mp.mpf(5)):
    f0, f1, f2 = fdd(lambda u: u ** 2 + b ** 2, t)
    L = L1_from(f0, f1, f2); cf = 2 * (t ** 2 - b ** 2)
    okD = okD and (abs(L - cf) < mp.mpf('1e-20'))
    print(f"  {mp.nstr(t,3):>6} {mp.nstr(L,8):>16} {mp.nstr(cf,8):>14} {'<0' if L < 0 else '>=0':>6}")
print("  --> L1 < 0 for |t| < b = 3: the second-order shadow SEES an isolated off-line zero pair. The")
print(f"      functional-equation reflection pairs any off-line zero rho with 1-rho,rho-bar; L1 catches it. PASS: {okD}")

print("=" * 96)
print("E. VERDICT -- where the reflection + second-order DC structure leaves RH")
print("=" * 96)
print("""  ESTABLISHED (this probe):
   * The functional-equation reflection s<->1-s is t<->-t on Xi; the critical line is its FIXED SET (A).
   * The second-order DC condition is the first Laguerre inequality L1[Xi]>=0 (log|Xi| concave), verified
     on the range, consistent with RH (B); it factors EXACTLY into the two move-(1) potentials,
     L1[Xi]=L1[A]zeta^2+A^2 L1[zeta], i.e. (log|Xi|)''=(log|A|)''+(log|zeta_line|)'' -- archimedean
     concavity vs the prime term, the domination now read at SECOND ORDER on the fixed line (C).
   * L1 already detects an isolated off-axis zero pair (D): the second-order shadow is not vacuous.
  THE RESIDUE (honest):
   * L1>=0 is NECESSARY, not sufficient. RH = the FULL Laguerre-Polya hierarchy: L1>=0 AND all higher
     Laguerre/Turan inequalities (order 4, 6, ...). The reflection pins the fixed line and the second-order
     domination, but cannot by itself force the higher orders.
   * The residue is therefore EXACTLY 'beyond second order' -- the program's Conductor Blind Spot /
     cumulant-tower regime. This matches N5 Rem 6.3 (the apex<->n-level identity holds order by order; the
     closure across the form-factor boundary tau=1 is RH) and N9 (fusion closure necessary-not-sufficient;
     residue archimedean). Move (1) gave both potentials at every order; the reflection localizes RH to the
     higher-order domination of the archimedean concavity over the prime convexity on the critical line.
  NET: the DC + reflection structure reduces RH to a clean, classical, order-graded statement -- second
  order (L1) is in hand and verified; the open content is the >=4th-order Laguerre-Polya domination on the
  fixed line. NOT a proof; a sharp, computable localization of exactly what remains.""")

allok = okA and okB and okC and okC2 and okD
print("=" * 96)
print(f"CERTIFICATE {'GREEN -- reflection + 2nd-order DC verified; residue = beyond-2nd-order on the fixed line' if allok else 'RED -- a check FAILED'}")
print("=" * 96)
