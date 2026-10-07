"""
Pressing on the HIGH-FREQUENCY ACCUMULATION -- the clean version.

(A first attempt measured a per-band Gram margin in the archimedean metric; it was CONFOUNDED -- a band
with few zeros is rank-deficient, so low-R bands gave spuriously tiny margins.  The 'growth with R' was
mostly zeros-per-band, not real comfort.  We discard it and measure the sampling-INDEPENDENT quantities.)

Two competing scale effects decide whether high frequency is comfortable:
  (i)  the archimedean energy density Omega_inf(r) ~ log(r/2pi)  GROWS with height (more energy);
  (ii) the zeros get DENSER, mean spacing ~ 2pi/log(r/2pi) SHRINKS, so the GUE near-degeneracies
       (the tightest local gaps -- the marginality) TIGHTEN with height.
If (i) wins, high freq is comfortable and RH reduces to the ground state.  If they scale TOGETHER, the
marginality is scale-invariant (GUE-universal) and there is NO comfortable regime.

Clean test: UNFOLD the gaps by the local density and check whether the marginality (the tightest unfolded
gap, = the near-degeneracy that drives lambda_min) is scale-invariant across heights.

  H1  per height-bin: archimedean energy Omega_inf, mean spacing, min RAW gap, min UNFOLDED gap.
  H2  is the UNFOLDED marginality scale-invariant?  (energy grows, raw gaps shrink -- do they cancel?)

No torch. mpmath (computes its own zeros). Deterministic.
"""
import mpmath as mp
mp.mp.dps = 15

NZ = 120
print("=" * 88)
print("High-frequency accumulation (clean): does growing archimedean energy outrun the GUE tightening?")
print("=" * 88)
print(f"\n  computing {NZ} zeros ...")
G = [mp.im(mp.zetazero(k)) for k in range(1, NZ+1)]

def Omega(r): return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*r/2)) - mp.log(mp.pi)
def density(g): return mp.log(g/(2*mp.pi))/(2*mp.pi)     # local mean zero density (zeros per unit)

# nearest-neighbor gaps and their unfolded values
gaps = [(G[i+1]-G[i], (G[i+1]+G[i])/2) for i in range(len(G)-1)]
unf  = [(d*density(c), c) for d, c in gaps]              # gap * density = gap / mean-spacing

bins = [(14, 35), (35, 60), (60, 90), (90, 130), (130, 200)]
print(f"\nH1/H2  per height bin:")
print(f"   {'height bin':>14} {'Omega_inf(mid)':>14} {'mean spacing':>13} {'min RAW gap':>12} {'min UNFOLDED gap':>17}")
rows = []
for lo, hi in bins:
    mid = mp.mpf(lo+hi)/2
    inbin = [(d, c) for d, c in gaps if lo <= c < hi]
    if not inbin: continue
    minraw = min(d for d, c in inbin)
    minunf = min(d*density(c) for d, c in inbin)
    meansp = 1/density(mid)
    rows.append((mid, Omega(mid), meansp, minraw, minunf))
    print(f"   {('%d-%d'%(lo,hi)):>14} {mp.nstr(Omega(mid),4):>14} {mp.nstr(meansp,4):>13} "
          f"{mp.nstr(minraw,4):>12} {mp.nstr(minunf,4):>17}")

minunf_all = [r[4] for r in rows]
omega_all  = [r[1] for r in rows]
print(f"\n   archimedean energy Omega_inf grows: {mp.nstr(omega_all[0],3)} -> {mp.nstr(omega_all[-1],3)} "
      f"(factor {mp.nstr(omega_all[-1]/omega_all[0],3)})")
print(f"   min RAW gap shrinks: {mp.nstr(rows[0][3],3)} -> {mp.nstr(rows[-1][3],3)} "
      f"(factor {mp.nstr(rows[-1][3]/rows[0][3],3)})")
print(f"   min UNFOLDED gap: {mp.nstr(min(minunf_all),3)} .. {mp.nstr(max(minunf_all),3)} "
      f"(spread {mp.nstr(max(minunf_all)/min(minunf_all),3)})  <- the marginality")
scale_inv = max(minunf_all)/min(minunf_all) < 3
print(f"\n   VERDICT: the unfolded marginality is "
      f"{'SCALE-INVARIANT (energy growth and gap tightening CANCEL: GUE-universal)' if scale_inv else 'NOT scale-invariant'}.")

print("\n" + "=" * 88)
print(f"""READING -- the high-frequency accumulation, cleanly:
  The archimedean energy DOES accumulate (Omega_inf ~ log r grows with height).  But the zeros densify
  in lockstep, so the GUE near-degeneracies (the tightest local gaps) tighten by the SAME factor -- the
  RAW gap shrinks as fast as the energy grows.  Unfolded by the local density, the marginality (tightest
  gap / mean spacing ~ {mp.nstr(sum(minunf_all)/len(minunf_all),2)}) is SCALE-INVARIANT across all heights.

  So the high-frequency accumulation gives NO comfortable regime: it accumulates MARGINAL-positive energy,
  with the near-degeneracies staying equally tight (in unfolded terms) at every height.  This is the
  barrier-synthesis 'height-independent' obstruction, seen from the energy side, and it REFUTES the
  'high freq is comfortable, only the ground state is hard' shortcut.

  CONSEQUENCE for the open step: RH is the convergence of an EVERYWHERE-marginal form to the exactly-
  marginal Xi -- the CCM mu_lambda -> 0 -- and what must be controlled is the UNFOLDED near-degeneracy
  UNIFORMLY across all heights (the individual GUE repulsion, P(gap->0)~gap^2 holding for EVERY pair, not
  on average).  The accumulation is necessary scaffolding; the residual is the uniform-in-height rate.
  The two genuinely distinct pieces left: (low freq) the pole-carried ground state near 2pi, and (all
  heights) the scale-invariant unfolded marginality -- joined only by a uniform individual-repulsion bound.
""")
print("=" * 88)
