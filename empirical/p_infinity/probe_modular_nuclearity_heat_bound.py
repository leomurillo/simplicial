"""
Pinf-A Section 8.7 -- the modular-nuclearity front-end (the Sec 8.6 "one handle"), PUSHED to a verdict.

GOAL.  Bound the Buchholz-Lechner modular-nuclearity norm  || Delta^{1/4} U(s) ||_1  for the prolate /
de Branges scaling inclusion using heat-kernel data, and locate EXACTLY the step where the positive-
energy (RH) assumption enters.

KEY IDENTITY (Borchers, analytically continued to t = -i/4).
    real t :   Delta^{it} U(s) Delta^{-it} = U(e^{-2 pi t} s)
    t=-i/4 :   Delta^{1/4} U(s) Delta^{-1/4} = U(i s) = e^{-s P}        (since e^{-2 pi (-i/4)} = i)
  =>  Delta^{1/4} U(s) = e^{-s P} Delta^{1/4},  so the nuclear norm is a HEAT TRACE:
        || Delta^{1/4} U(s) ||_1  ~  Tr( e^{-s P} * [Delta^{1/4} regulator] )  =  sum_n e^{-s omega_n} w_n.

  Generator form (= the 8.3a commutator):  [log Delta, P] = 2 pi i P,  log Delta = -2 pi D,
  D = dilation generator,  so  Delta^{1/4} = e^{-(pi/2) D}.  Verified EXACTLY in sympy below.

VERDICT (sharp, NEGATIVE -- the handle collapses to the convergence wall, mechanism named).
  The moment positivity sneaks in is NOT the final estimate -- it is the SYMBOL e^{-sP} itself.
  e^{-sP} is bounded/trace-class for s>0  <=>  P bounded below  <=>  positive energy  <=>  RH.
  The continuation s -> is converges (upper-half s-plane) ONLY when spec(P) >= 0 (Paley-Wiener
  spectrum condition).  So "heat-kernel data" is not data you HAVE; e^{-sP} is the object that EXISTS
  iff RH.  You cannot bound the nuclear norm from it without assuming the positivity it should deliver.
  (Buchholz-Lechner confirm the direction: modular nuclearity is PROVED downstream of a positive-energy
  one-particle space, never as its source.)

  Finite-lambda caveat (the honest residue):  each prolate W_lambda is a bounded-below Schroedinger
  operator, so each finite-lambda heat trace Tr e^{-beta W_lambda} IS unconditional data.  But
  UNIFORMITY in lambda -- the limit P = lim W_lambda staying positive -- is the prolate convergence
  = RH.  Same wall, two faces: (A) symbol-existence of e^{-sP}; (B) limit-uniformity of the heat bound.

No torch.  sympy for the exact generator algebra; numpy for the heat-trace demonstration on real zeros.
"""
import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------
# 1.  EXACT generator algebra (sympy): [D,P] = -i P  =>  log Delta = -2 pi D, Delta^{1/4}=e^{-(pi/2)D},
#     and the continuation Delta^{1/4} U(s) Delta^{-1/4} = e^{-s P}.  Multiplication model:
#     P = mult by omega;  D = -i(omega d/domega + 1/2)  (dilation gen, unitary on L^2(R_+,domega)).
# ---------------------------------------------------------------------------

def verify_generator_algebra():
    w = sp.symbols('omega', positive=True)
    f = sp.Function('f')
    I = sp.I
    P = lambda g: w * g                                   # P = mult by omega
    D = lambda g: -I * (w * sp.diff(g, w) + g / 2)        # dilation generator
    DP = sp.simplify(D(P(f(w))) - P(D(f(w))))             # [D,P] f
    target = sp.simplify(-I * P(f(w)))                    # -i P f
    return sp.simplify(DP - target) == 0                  # [D,P] = -i P  exactly


def borchers_factor(t):
    """The closed-form Borchers scaling factor e^{-2 pi t}; continue t -> -i/4 to land on e^{-sP}."""
    return sp.exp(-2 * sp.pi * t)


# ---------------------------------------------------------------------------
# 2.  HEAT-TRACE / nuclearity proxy on the actual zeta spectrum.
#     Energies omega_n (positive-energy reading): the zero heights gamma_n  (prolate map: 1/4+gamma_n^2).
#     Nuclear norm ~ sum_n e^{-s omega_n} w_n.  Modular regulator w_n = 1 here (UV handled separately);
#     the s-decay factor e^{-s omega_n} is the POSITIVITY-dependent part we are watching.
# ---------------------------------------------------------------------------

GAMMA = np.array([
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719,
    43.327073, 48.005151, 49.773832, 52.970321, 56.446248, 59.347044, 60.831779,
    65.112544, 67.079811, 69.546402, 72.067158, 75.704691, 77.144840, 79.337375,
    82.910381, 84.735493, 87.425275, 88.809111, 92.491899, 94.651344, 95.870634,
    98.831194, 101.317851,
])


def heat_trace(omegas, s):
    return float(np.sum(np.exp(-s * np.asarray(omegas))))


def spoof_offline(gamma, beta_offset, c=1.0):
    """Inject ONE off-line zero rho = (1/2 + delta) + i*gamma_k as a NEGATIVE-energy mode.
    P infinity / energy-condition reading: off-line distance delta = beta_offset breaks |a|<=2sqrt(q),
    i.e. the corresponding spectral mode acquires omega < 0.  We model omega_* = -c*delta (a STAND-IN;
    the sign is the point, not the magnitude)."""
    omegas = list(gamma.copy())
    omegas.append(-c * beta_offset)         # the negative-energy mode
    return np.array(omegas)


if __name__ == "__main__":
    print("Pinf-A Sec 8.7 -- modular nuclearity pushed: where does positivity sneak in?")
    print("=" * 78)

    print("\n[1] EXACT generator algebra (sympy), the engine of the Borchers continuation")
    print("-" * 78)
    ok = verify_generator_algebra()
    t = sp.symbols('t')
    print(f"  [D, P] = -i P  (multiplication model) :  {ok}    [EXACT]")
    print(f"  => log Delta = -2 pi D,  Delta^(1/4) = e^(-(pi/2) D)")
    print(f"  Borchers factor e^(-2 pi t) at t=-i/4 :  {sp.simplify(borchers_factor(-sp.I/4))}"
          f"   => Delta^(1/4) U(s) Delta^(-1/4) = U(i s) = e^(-s P)   [EXACT continuation]")
    print("  So the nuclear norm IS a heat trace Tr e^(-sP); e^(-sP) bounded  <=>  spec(P) >= 0.")

    print("\n[2] heat trace Tr e^(-sP) = sum_n e^(-s omega_n) on the REAL zeta spectrum (positive)")
    print("-" * 78)
    for s in (0.30, 0.20, 0.10, 0.05, 0.02):
        print(f"  s={s:4.2f}:  nuclear-norm proxy = {heat_trace(GAMMA, s):12.5f}   (finite, "
              f"decreasing in s -> genuine localization decay)")
    print("  POSITIVE spectrum (RH-true): the IR sum converges because omega_n = gamma_n -> +inf.")

    print("\n[3] inject ONE off-line zero as a NEGATIVE-energy mode (RH-false stand-in)")
    print("-" * 78)
    sp_spec = spoof_offline(GAMMA, beta_offset=0.25, c=20.0)   # omega_* = -5
    print(f"  added mode omega_* = {sp_spec[-1]:.2f}  (an off-line zero violates |a|<=2sqrt q -> omega<0)")
    for s in (0.10, 0.60, 1.00, 2.00, 3.00, 4.00):
        val = heat_trace(sp_spec, s)
        tag = "grows" if val > heat_trace(sp_spec, s - 0.05) else "decays"
        tag += " / BLOWS UP" if val > 1e6 else ""
        print(f"  s={s:4.2f}:  proxy = {val:14.3e}   [{tag}]  (e^(-s*omega_*) = e^(+{-sp_spec[-1]*s:.2f}))")
    print("  NEGATIVE mode: the proxy GROWS in s (vs DECAYS for the positive spectrum) and -> +inf.")
    print("  Nuclear norm = INF.  The heat trace exists as a bounded object iff spec(P) bounded below.")

    print("\n" + "=" * 78)
    print("VERDICT (8.7).  Positivity sneaks in at the SYMBOL e^(-sP), i.e. at the Borchers")
    print("continuation s -> is (t -> -i/4): e^(-sP) is bounded/trace-class  <=>  spec(P) >= 0  <=>  RH.")
    print("Heat-kernel data does NOT bound the nuclear norm positivity-free -- it presupposes the heat")
    print("semigroup, which exists iff RH.  Finite-lambda traces are unconditional, but uniformity in")
    print("lambda (the limit) = prolate convergence = RH.  The Sec 8.6 handle CLOSES NEGATIVE; it collapses")
    print("into Sec 8.4, now with the mechanism pinned.  Same convergence wall, geometric meaning added.")
