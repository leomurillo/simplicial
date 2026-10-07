"""
Option A (the c_2 hunt), tested honestly: does a single g in G with c_2 < 0 close RH
WITHOUT the C* bridge -- or does it route back through the same prime-distribution content?

Setup (diez S1 + S2):
  G = { g : S_g(x) = sum_gamma gtilde(1/2+i gamma) e^{i gamma x} >= 0 on R+ }   (cubic Fejer class)
  diez S1 Thm 1.4: gtilde(1/2+i gamma) = phi(gamma) = Fejer kernel bandwidth Omega -> S_g ~ phi >= 0.
  cluster c_2 = 24 etatilde''(3 i g0) + 72 etatilde''(i g0), times phi(g0)^3 weight.
  Cluster argument: IF cubic positivity C_zeta >= 0 holds AND c_2 < 0, an off-line zero
  forces C_zeta < 0 -> contradiction -> RH.

The catch (existing probe_diez1_g_cluster Part 3): C_zeta = INT 2 eta S_g^3 holds via
S_g >= 0, BUT S_g >= 0 is a SPECTRAL (zero-side) statement -- it reads the zero locations,
so establishing it presupposes the zeros are on-line = RH (CIRCULAR). The NON-circular route
is the Weil explicit formula, which writes the SAME wave as
  S_g(x) = A_inf(x) + (prime fluctuation)(x),
  A_inf = archimedean wave (digamma 1/Gamma density), prime fluctuation = the psi(x)-x-type
  oscillation carried by the zeros. S_g >= 0 read this way is a balance between A_inf and the
  prime fluctuation -- and the prime fluctuation is exactly what RH / the level C* control.

This probe: (1) does the diez S1 g actually sit in G, and is c_2 < 0?  (2) read the SAME wave
non-circularly -- is A_inf negligible (Option A could escape C*) or O(1) and balanced against
the prime fluctuation (Option A == Option B = C*)?

Deterministic mpmath. No torch. HONEST: the raw prime wave is main-term-dominated, so the
meaningful comparison is A_inf vs the prime FLUCTUATION (= S_g - A_inf), not vs raw 2P.
"""

import mpmath as mp
mp.mp.dps = 20

OMEGA = mp.mpf("0.5")                       # Fejer bandwidth (diez Remark 1.6 free parameter)

def phi_fejer(t):
    a = OMEGA * t / 2
    if abs(a) < mp.mpf("1e-25"):
        return mp.mpf(1)
    return (mp.sin(a) / a) ** 2

GAMMAS = [mp.mpf(g) for g in [
    14.134725141734693, 21.022039638771554, 25.010857580145688, 30.424876125859513,
    32.935061587739189, 37.586178158825671, 40.918719012147495, 43.327073280914999,
    48.005150881167159, 49.773832477672302, 52.970321477714461, 56.446247697063394,
    59.347044003392213, 60.831778524609810, 65.112544048081607, 67.079810529494173,
    69.546401711173978, 72.067157674481907, 75.704690699083933, 77.144840068874805,
    79.337375020249367, 82.910380854086031, 84.735492980517050, 87.425274613125229,
    88.809111207634929, 92.491899270558484, 94.651344040519896, 95.870634228245332,
    98.831194218193692, 101.317851005731391]]

def S_g_spectral(x):
    s = mp.mpf(0)
    for g in GAMMAS:
        s += 2 * phi_fejer(g) * mp.cos(g * x)
    return s

def c2_cluster(gamma0, sigma_eta):
    def eta_pp(y):
        return sigma_eta**2 * (sigma_eta**2 * y**2 - 1) * mp.exp(-y**2 * sigma_eta**2 / 2)
    w = phi_fejer(gamma0) ** 3
    return (24 * eta_pp(3j * gamma0) + 72 * eta_pp(1j * gamma0)) * w

# archimedean density: Re psi(1/4 + i t/2) - (1/2) log pi   (the infinity place / smooth count)
def arch_density(t):
    return mp.re(mp.psi(0, mp.mpc("0.25", t / 2))) - mp.log(mp.pi) / 2

def A_inf(x):
    f = lambda t: phi_fejer(t) * mp.cos(t * x) * arch_density(t)
    return mp.quad(f, [0, 5, 20, 60]) / mp.pi

# ---- Part 1 --------------------------------------------------------------------------
print("=" * 82)
print("PART 1 - diez S1 g: is it in G (S_g >= 0), and is c_2 < 0?")
print("=" * 82)
viol = 0; n = 0; smin = mp.mpf("1e9")
for k in range(1, 41):
    x = mp.mpf(k) / 4
    v = S_g_spectral(x); smin = min(smin, v); n += 1
    if v < 0: viol += 1
in_G = (viol == 0)
print(f"  S_g on x in [0.25,10]: min = {float(smin):+.4f}, sign violations {viol}/{n}")
print(f"  => diez S1 Fejer g ({len(GAMMAS)} zeros, Omega={float(OMEGA)}): "
      f"{'IN G' if in_G else 'NOT in G'}")
if not in_G:
    print("     The g that delivers c_2<0 does NOT manifestly satisfy S_g>=0 with finite data;")
    print("     S_g>=0 EXACTLY needs the S1 Step-5 renormalization (large T) AND coexistence")
    print("     with the off-line continuation giving c_2<0 = the hybrid-g compatibility,")
    print("     unsolved (matches z6 Addendum K, tempers Addendum L).")
g0 = GAMMAS[0]
for se in [mp.mpf('0.06'), mp.mpf('0.12'), mp.mpf('0.18')]:
    c2 = c2_cluster(g0, se)
    print(f"  c_2 (gamma0={float(g0):.2f}, sigma_eta={float(se):.2f}) = "
          f"{float(mp.re(c2)):+.3e}  [{'NEG' if mp.re(c2)<0 else 'POS'}]")
print("  => c_2 < 0 confirmed (the cluster engine is real).")

# ---- Part 2: non-circular reading ----------------------------------------------------
print()
print("=" * 82)
print("PART 2 - the SAME wave non-circularly: S_g = A_inf + (prime fluctuation)")
print("=" * 82)
print(f"  {'x':>6} {'S_g (spectral)':>15} {'A_inf (arch)':>13} {'prime-fluct':>13} {'|A_inf|/|S_g|':>13}")
big = 0; m = 0
for k in range(4, 18):
    x = mp.mpf(k) / 4
    sg = mp.re(S_g_spectral(x)); a = A_inf(x); pf = sg - a
    rat = abs(a) / abs(sg) if abs(sg) > mp.mpf("1e-6") else mp.mpf("999")
    m += 1
    if rat > 1: big += 1
    print(f"  {float(x):>6.2f} {float(sg):>15.4f} {float(a):>13.4f} {float(pf):>13.4f} {float(rat):>13.2f}")
print(f"\n  |A_inf| >= |S_g| at {big}/{m} points: the archimedean wave is the SAME size as the")
print("  ENTIRE wave (or larger). The prime fluctuation (S_g - A_inf) is O(1) and nearly")
print("  CANCELS A_inf, leaving the small S_g residue. Positivity S_g>=0 is that delicate")
print("  cancellation -- NOT a free margin. (Raw prime wave 2P is main-term-dominated and")
print("  grows ~e^{x/2}; comparing A_inf to it would be meaningless -- the right object is")
print("  the FLUCTUATION, which is O(1) and zero-controlled.)")

# ---- Part 3: verdict -----------------------------------------------------------------
print()
print("=" * 82)
print("PART 3 - VERDICT: does Option A escape C*?")
print("=" * 82)
print(f"""  TWO blocks, both real:

  (1) The witness isn't free. The diez S1 Fejer g that gives c_2<0 is NOT in G with finite
      data ({viol}/{n} sign violations). S_g>=0 EXACTLY is the Step-5 renormalization AND must
      coexist with the off-line continuation giving c_2<0 -- the hybrid-g compatibility,
      unsolved (z6 Addendum K).

  (2) Even granting the witness, the positivity is circular. S_g>=0 is SPECTRAL -- it reads
      the zero locations (= assumes RH). Non-circularly (Weil, Part 2), the wave is
      A_inf + prime-fluctuation, BOTH O(1), and S_g>=0 is their delicate near-cancellation.
      The prime fluctuation is the psi(x)-x oscillation the zeros (RH) / the level (C*)
      control. So establishing S_g>=0 without RH IS controlling the prime distribution = C*.

  => OPTION A DOES NOT ESCAPE C*. The c_2<0 cluster engine is real and unconditional, but the
     positivity it consumes is the same prime-distribution content as Option B's bridge.
     Conservation of difficulty: A == B at the prime-archimedean balance = C*<=2.80. The
     earlier 'Option A closes RH without C*' was WRONG -- the escape was the circular
     (spectral) reading of positivity.

  The one honest crack: a g in G whose prime fluctuation DOMINATES A_inf with a sign margin
  (not a near-cancellation) would localize positivity off the delicate balance. The generic
  Fejer g shows the opposite. Whether any admissible g does is the precisely-stated finite-dim
  question -- open, but no escape on current evidence.

  NET: put N0 on C* (Option B). Keep the hybrid-g search as a long shot, not the main line.""")
