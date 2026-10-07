"""
Pushing the phase bound to its correct (RH-equivalent) form: the GLOBAL de Branges target.

The recast gave the PHASE condition. But the POINTWISE real-axis bound theta'(t) >= -pi S'(t)  is the
first Laguerre inequality (Xi')^2 - Xi Xi'' >= 0 -- NECESSARY-not-sufficient (an off-line zero's sign-
reversing term is maskable on the line; likely already a theorem, Csordas-Varga). The RH content is the
GLOBAL phase condition, in the UPPER HALF-PLANE C+:

    m_B(t) = -Xi'(t)/Xi(t) = -sum_{zeros gamma} 1/(t-gamma)    is HERGLOTZ  (Im m_B >= 0 on C+)  <=>  RH.

This is the LINEAR (additive over zeros = the arrow) object the Elkies/max-entropy grounding points to --
NOT the quadratic Weil/amplitude form. We verify it IS RH-equivalent and IS the phase/linear object:

  A  real zeros (RH): Im m_B(t) = sum_g Im[-1/(t-g)] = sum_g y/((x-g)^2+y^2) > 0 on all of C+ -- Herglotz.
  B  a single zero pushed OFF the real t-axis (an off-line zeta zero, t=gamma+i*delta) injects a term
     with Im < 0 for 0<y<delta -- BREAKING Herglotz. So global C+ Herglotz <=> all zeros real <=> RH,
     and the breakage is LINEAR (one bad pole), not a quadratic near-cancellation.

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 25

GAM = [mp.im(mp.zetazero(n)) for n in range(1, 26)]      # first 25 zeta zeros (real t, RH)

def ImmB(t, zeros):                                       # Im of m_B = -sum 1/(t-g) over the given zeros
    return mp.fsum(mp.im(-1/(t - g)) for g in zeros)

# zero multiset in the t-plane: +-gamma_n (real, under RH)
real_zeros = [g for g in GAM] + [-g for g in GAM]

print("=" * 80)
print("The global de Branges target: m_B = -Xi'/Xi Herglotz on C+ (Im m_B>=0)  <=>  RH")
print("=" * 80)

print("\nA. real zeros (RH): min Im m_B over a C+ grid (x in [0,40], y in [0.3,6]) should be > 0:")
xs = [mp.mpf(x) for x in range(0, 41, 2)]
ys = [mp.mpf(s) for s in ('0.3','0.6','1','2','4','6')]
mn = min(ImmB(x + 1j*y, real_zeros) for x in xs for y in ys)
print(f"   min Im m_B (real zeros) = {mp.nstr(mn,5)}   -> {'HERGLOTZ (>=0): RH holds' if mn > 0 else 'NOT Herglotz'}")

print("\nB. push ONE zero off the real t-axis: gamma_1 -> gamma_1 + i*delta (an off-line zeta zero):")
print(f"   {'delta':>7} {'min Im m_B on C+':>18} {'where (x,y)':>16} {'Herglotz?':>11}")
for delta in [mp.mpf(s) for s in ('0','0.05','0.15','0.3')]:
    zeros = list(real_zeros)
    zeros[0] = GAM[0] + 1j*delta                          # move +gamma_1 off-axis (Im>0)
    # scan finely near the moved zero (x~gamma_1, small y) where breakage appears
    best = None; bestxy = None
    for xi in range(120, 165):                            # x near 12..16.5
        x = mp.mpf(xi)/10
        for yj in range(1, 40):
            y = mp.mpf(yj)/100                            # y in (0, 0.4)
            v = ImmB(x + 1j*y, zeros)
            if best is None or v < best: best, bestxy = v, (x, y)
    tag = 'YES' if best >= -mp.mpf(10)**(-9) else 'NO -> RH broken'
    print(f"   {mp.nstr(delta,3):>7} {mp.nstr(best,5):>18} {f'({mp.nstr(bestxy[0],4)},{mp.nstr(bestxy[1],3)})':>16} {tag:>11}")
print("   => delta=0 (on the line): Im m_B>=0 (Herglotz, RH). delta>0 (off-line): Im m_B goes NEGATIVE")
print("      just below the displaced zero -> Herglotz BROKEN. One off-line zero = one bad pole (LINEAR).")

print("\n" + "=" * 80)
print("""SYNTHESIS — the sharpened de Branges target, in the Elkies-grounded phase coordinate:
  * RH = m_B = -Xi'/Xi HERGLOTZ on C+ (Im m_B>=0). This is the GLOBAL phase condition -- the ANGULAR /
    arrow / linear object (m_B = -sum 1/(t-gamma), additive over zeros), exactly what the max-entropy
    grounding says is RH-native. NOT the pointwise real-axis bound (= Laguerre L_1, necessary-not-suff).
  * The breakage is LINEAR: one off-line zero injects ONE pole with Im<0 below it (verified). Contrast
    the quadratic Weil/energy form, where an off-line zero is a near-cancellation in a |.|^2 sum (the
    phase-blind square, marginal). Same RH event, but in the phase coordinate it is a single linear
    defect, not a marginal quadratic cancellation -- the Elkies reason the arrow/phase is the clean
    object and the amplitude is its free square.
  * HONEST: this IS the program's de Branges m_B-Herglotz RH-equivalent (master-state). The push does
    not crack it; it GROUNDS and SHARPENS it -- the correct target is the C+ Herglotz (linear/phase),
    the real-axis Laguerre is the free necessary-not-sufficient shadow, and the amplitude contraction
    rho_E was the phase-blind square (its marginality explained). The open content = control the C+
    phase / the pole locations = RH. The genuine gain this thread: the coordinate (angular/phase/linear)
    and the REASON (max-entropy on (Z/p)^x), not a new crack.
""")
print("=" * 80)
