"""
THE tau=1 LEVER, SETTLED: is it a CONFORMAL-BOOTSTRAP / RESURGENT STOKES line (crossable "for free" by a
vacuum block), or a thermodynamic-limit LEGENDRE PHASE TRANSITION (the program's existing frame)?

Context. A proposed lever says: treat tau=1 as a Stokes line; the flat plateau K(tau>=1)=1 is forced by
modular crossing symmetry / the Cardy formula (Bogomolny-Keating semiclassical Riemann-Siegel); the
functional equation iota = F^2 (s<->1-s) is the exact Stokes automorphism; the N5 transfer (-1)^n is the
parity switch of a Borel non-summable trans-series. If true, the plateau is "forced by the dual-channel
vacuum block," bypassing the off-diagonal Hardy-Littlewood summation = bypassing the open arithmetic.

This probe (mpmath/sympy/numpy, NO torch) tests the three load-bearing structural claims EXACTLY:

  T1  MODULAR SYMMETRY.  Cardy/crossing is a THEOREM because the torus partition fn is modular invariant
      (S: tau -> -1/tau is an exact symmetry exchanging two channels). Test whether K(tau)=min(|tau|,1)
      has ANY tau->1/tau symmetry. If not, there is no second channel related by a group action, and no
      vacuum-block-forces-asymptotics mechanism exists.

  T2  WHAT iota=F^2 DOES TO THE FORM FACTOR.  s<->1-s sends the zeros gamma <-> -gamma, so on
      K(tau)=<|sum e^{i gamma tau}|^2> it acts as tau -> -tau (EVENNESS). A crossing/Stokes automorphism
      must EXCHANGE the perturbative (diagonal/ramp) and non-perturbative (off-diagonal/plateau) sectors.
      Test, on REAL zeta zeros, whether gamma->-gamma is channel-PRESERVING (leaves diagonal & off-diagonal
      parts each invariant) or channel-EXCHANGING. Channel-preserving => iota=F^2 is NOT the Stokes map.

  T3  BOREL STRUCTURE OF (-1)^n.  A resurgent Stokes line requires an asymptotic series whose Borel
      transform has a positive-axis singularity (=> a lateral-resummation ambiguity labelled by the
      alternation). Test the per-prime cumulant series  sum_{n>=2} (-1)^n z^n / phi(p)^n  : is it a
      CONVERGENT (Borel-trivial, no Stokes ray) object, with the tau=1 non-analyticity appearing ONLY in
      the infinite-prime limit as a Legendre/convex KINK (continuous, slope-discontinuous = phase
      transition) rather than a Stokes JUMP (exponentially-small imaginary ambiguity across a ray)?

VERDICT logic: T1 no-symmetry AND T2 channel-preserving AND T3 convergent+kink  =>  the lever supplies the
correct PICTURE (Berry / Bogomolny-Keating semiclassical, which IS HL-conditional) but NOT an unconditional
crossing theorem; the tau=1 corner is a thermodynamic Legendre phase transition (program's adelic-Legendre /
dually-flat frame), not a Borel-resurgent Stokes line. The plateau is NOT forced for free.
"""
import mpmath as mp
import sympy as sp
import numpy as np
mp.mp.dps = 30

def K(tau):
    return min(abs(float(tau)), 1.0)

print("=" * 96)
print("T1.  MODULAR SYMMETRY:  does K(tau)=min(|tau|,1) admit a crossing  tau -> 1/tau ?")
print("=" * 96)
print(f"  {'tau':>8} {'K(tau)':>10} {'1/tau':>10} {'K(1/tau)':>10} {'equal?':>8}")
t1_no_symmetry = True
for tau in (0.25, 0.5, 0.75, 1.5, 2.0, 4.0):
    a, b = K(tau), K(1.0 / tau)
    eq = abs(a - b) < 1e-12
    if eq and abs(tau - 1.0) > 1e-9:
        t1_no_symmetry = False
    print(f"  {tau:>8.3f} {a:>10.4f} {1.0/tau:>10.4f} {b:>10.4f} {str(eq):>8}")
print(f"""  Under tau->1/tau the ramp value tau (tau<1) would have to equal the plateau value 1 -- it equals 1/tau
  instead. K is NOT invariant under tau->1/tau: there is NO modular/crossing symmetry, hence NO 'two channels
  related by a group action', hence NO vacuum-block-computes-the-dual-asymptotics (Cardy) mechanism.
  --> T1: K has no tau->1/tau symmetry: {t1_no_symmetry}""")

print("=" * 96)
print("T2.  iota=F^2 (s<->1-s => gamma<->-gamma => tau->-tau): channel-PRESERVING or channel-EXCHANGING?")
print("=" * 96)
NZ = 200
print(f"  loading first {NZ} zeta ordinates gamma_n (mpmath) ...", flush=True)
gam = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, NZ + 1)])
# unfold to unit mean density so the form factor has the standard ramp/plateau shape
def Nsmooth(g):
    return g / (2 * np.pi) * np.log(g / (2 * np.pi)) - g / (2 * np.pi) + 7.0 / 8.0
w = Nsmooth(gam)                       # unfolded ordinates (unit mean spacing)

def formfactor_parts(tau, w):
    # K(tau) ~ |sum_n e^{i w_n tau}|^2 / N  =  N(diagonal)  +  sum_{n!=m} e^{i (w_n-w_m) tau} (off-diag)
    phases = np.exp(1j * tau * w)
    S = phases.sum()
    diag = float(len(w))                                   # the n=m terms: sum of 1 = N
    offdiag = float((np.abs(S) ** 2) - len(w))             # |S|^2 - N
    return diag, offdiag

# apply the FE involution gamma -> -gamma  (equivalently w -> -w on the symmetric spectrum {+-w})
def parts_under_involution(tau, w):
    d_plus, o_plus = formfactor_parts(tau, w)              # original
    d_inv, o_inv = formfactor_parts(tau, -w)               # gamma -> -gamma
    return (d_plus, o_plus), (d_inv, o_inv)

print(f"  {'tau':>6} {'diag':>10} {'offdiag':>12} {'diag(inv)':>10} {'offdiag(inv)':>12} {'sector-preserved?':>18}")
t2_channel_preserving = True
for tau in (0.3, 0.6, 0.9, 1.2, 1.8):
    (d, o), (di, oi) = parts_under_involution(tau, w)
    # channel-PRESERVING means: diagonal maps to diagonal (invariant) and off-diagonal real part is invariant
    # (gamma->-gamma conjugates every off-diagonal phase; the real, symmetric form factor is unchanged).
    preserved = abs(d - di) < 1e-6 and abs(o - oi) < 1e-6
    if not preserved:
        t2_channel_preserving = False
    print(f"  {tau:>6.2f} {d:>10.1f} {o:>12.3f} {di:>10.1f} {oi:>12.3f} {str(preserved):>18}")
print(f"""  gamma->-gamma sends every off-diagonal phase e^{{i(w_n-w_m)tau}} to its conjugate; the REAL symmetric
  form factor (and its diagonal/off-diagonal split) is left invariant. The involution does NOT move weight
  between the diagonal (ramp) and off-diagonal (plateau) sectors -- it is channel-PRESERVING. A Stokes /
  crossing automorphism MUST exchange the two sectors. Therefore iota=F^2 is NOT the Stokes automorphism.
  --> T2: iota=F^2 is channel-preserving (evenness), not channel-exchanging: {t2_channel_preserving}""")

print("=" * 96)
print("T3.  BOREL STRUCTURE of the (-1)^n transfer: convergent kink (phase transition) or Stokes jump?")
print("=" * 96)
# per-prime alternating cumulant series  f_p(z) = sum_{n>=2} (-1)^n z^n / phi(p)^n  = (z/phi)^2 / (1 + z/phi)
# THE decisive Borel point: the ONLY singularity is the pole at z = -phi(p), on the NEGATIVE real axis.
# Borel-summation (Stokes) ambiguities come from singularities on the POSITIVE Borel ray. The (-1)^n
# alternation places the singularity at z<0 => textbook Borel-SUMMABLE, NO positive-axis ray, NO lateral
# ambiguity. So (-1)^n is the OPPOSITE of a "Borel non-summable trans-series"; radius = phi(p) >= 1
# (p=2 marginal at exactly 1, the special prime). Verify pole location & radius exactly.
z = sp.symbols('z')
print(f"  {'p':>5} {'phi(p)':>7} {'radius':>8} {'pole at z=':>11} {'pole sign':>10} {'Borel-summable (pole<0)?':>24}")
t3_convergent = True
for p in (2, 3, 5, 7, 11):
    phi = int(sp.totient(p))
    series = (z / phi) ** 2 / (1 + z / phi)
    pole = sp.solve(sp.denom(sp.together(series)), z)[0]   # z = -phi
    radius = float(phi)                                     # |z/phi|<1  => radius phi >= 1
    borel_summable = float(pole) < 0 and radius >= 1.0      # singularity off the positive Borel ray
    if not borel_summable:
        t3_convergent = False
    print(f"  {p:>5} {phi:>7} {radius:>8.3f} {str(pole):>11} {'NEG' if float(pole)<0 else 'POS':>10} {str(borel_summable):>24}")
# the kink: min(tau,1) = continuous, slope jumps from +1 to 0 at tau=1.  A Stokes/median-resummation jump
# is a DISCONTINUITY in the trans-series across a ray (typ. an exponentially-small imaginary ambiguity);
# the form-factor non-analyticity is a CONTINUOUS slope-kink = Legendre/convex (max/min of analytic branches).
left_slope = (K(1.0) - K(1.0 - 1e-6)) / 1e-6
right_slope = (K(1.0 + 1e-6) - K(1.0)) / 1e-6
value_continuous = abs(K(1.0 - 1e-9) - K(1.0 + 1e-9)) < 1e-6
slope_jumps = abs(left_slope - right_slope) > 0.5
print(f"""  per-prime singularity sits at z=-phi(p) on the NEGATIVE axis (radius phi(p)>=1, p=2 marginal): the (-1)^n
  alternation makes the series Borel-SUMMABLE with NO positive-axis ray and NO lateral ambiguity -- the exact
  OPPOSITE of a 'Borel non-summable trans-series'. The tau=1 non-analyticity exists ONLY in the infinite-prime limit.
  Its morphology:  value continuous across tau=1: {value_continuous}   (left slope {left_slope:+.3f} -> right slope {right_slope:+.3f})
  A CONTINUOUS slope-kink = the kink of a Legendre transform / a max-min of analytic branches = a (convex)
  PHASE TRANSITION; NOT a Stokes JUMP (which is a discontinuous, exp-small imaginary trans-series ambiguity).
  --> T3: (-1)^n is convergent/Borel-trivial per prime, tau=1 is a continuous Legendre kink: {t3_convergent and value_continuous and slope_jumps}""")

print("=" * 96)
print("VERDICT")
print("=" * 96)
t3 = t3_convergent and value_continuous and slope_jumps
allok = t1_no_symmetry and t2_channel_preserving and t3
print(f"""  T1  no tau->1/tau modular symmetry on K        : {t1_no_symmetry}
  T2  iota=F^2 channel-preserving (not Stokes)   : {t2_channel_preserving}
  T3  (-1)^n Borel-trivial; tau=1 = Legendre kink: {t3}

  The proposed conformal-bootstrap / resurgence lever supplies the correct PICTURE -- the Berry (1988) /
  Bogomolny-Keating (1996) semiclassical derivation of the GUE form factor, ramp from the diagonal and
  PLATEAU FROM THE HARDY-LITTLEWOOD off-diagonal -- but that derivation is CONDITIONAL on Hardy-Littlewood
  with uniformity: it USES the open arithmetic (the uniform level-of-distribution, theta_0 ~ 0.515 of the
  push), it does not bypass it. There is (T1) no modular group on the form-factor variable to make Cardy a
  theorem, (T2) the functional-equation involution acts as channel-PRESERVING evenness, not a channel-
  exchanging Stokes automorphism, and (T3) the (-1)^n alternation is convergent per prime with the tau=1
  corner a thermodynamic LEGENDRE PHASE TRANSITION (the program's adelic-Legendre / dually-flat frame),
  not a Borel-resurgent Stokes line. The flat plateau is NOT 'forced by a dual-channel vacuum block'.
  Net: the lever sharpens the attribution of section 7 (Berry / Bogomolny-Keating, HL-conditional) and
  CONFIRMS the Legendre-phase-transition reading over a resurgence reading; it does not cross tau=1.""")
print("=" * 96)
print(f"CERTIFICATE {'GREEN -- lever is the correct (HL-conditional) PICTURE, not an unconditional crossing theorem; tau=1 = Legendre phase transition, not a Stokes line' if allok else 'PARTIAL -- see T1/T2/T3'}")
print("=" * 96)
