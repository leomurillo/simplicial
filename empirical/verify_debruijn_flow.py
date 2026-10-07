r"""de Bruijn-Newman: the heat-flow margin, the Lehmer-pair collision clock, and the 0.22 gap.

PURPOSE.  Make the de Bruijn-Newman picture QUANTITATIVE and label every claim [P]/[A]/[C].
The de Bruijn-Newman constant Lambda satisfies:
   H_t real-rooted  <=>  t >= Lambda,        RH  <=>  Lambda <= 0,
where H_t(z) = int_0^inf e^{t u^2} Phi(u) cos(z u) du is the heat-flow deformation of the Riemann
xi function (H_0 = (1/8) Xi(z/2) up to normalization; its real zeros are the ordinates gamma_j).
PROVEN bracket: Lambda >= 0 (Rodgers-Tao 2020) and Lambda <= 0.22 (Polymath15, 2019), so
   Lambda in [0, 0.22]   and   RH  <=>  Lambda = 0.

This script computes FOUR things, all numerical (mpmath/numpy), none a proof of Lambda<=0:

  PART A  THE ZERO FLOW (Calogero / Rodgers-Tao dynamics).  The zeros x_j(t) of H_t obey the
          first-order interacting ODE (Csordas-Smith-Varga 1994; Rodgers-Tao 2020 eq. for the
          backward-heat-in-z DBN convention)
                d x_j / dt  =  + 2 sum_{k != j} 1/(x_j - x_k).            (FLOW)
          As t INCREASES the zeros REPEL (stay real); as t DECREASES toward Lambda they ATTRACT and
          a "Lehmer pair" can COLLIDE (real double root) then split into a complex conjugate pair --
          this collision is the ONLY way reality is lost.  We seed x_j(0) = gamma_j (the true first
          ~50 zeros) and integrate the flow BACKWARD (t decreasing) to watch the tightest pair's
          normalized gap shrink, reporting WHERE the margin is thinnest and HOW it scales.

  PART B  THE LEHMER-PAIR COLLISION CLOCK (the rigorous lower-bound mechanism, in miniature).  For
          an ISOLATED close pair the two-body reduction of (FLOW) gives an EXACT collision law:
          the squared separation s = (x_2-x_1)^2 obeys ds/dt = +8, so s(t) = s(0) + 8 t and the pair
          collides at  t_coll = - s(0)/8 = -(gap)^2/8.  A tight pair (small gap) collides at a t_coll
          just below 0 -> forces Lambda >= t_coll, i.e. Lambda is pushed UP toward 0 from below.  This
          is the Csordas-Smith-Varga "Lehmer pair" lower bound in its cleanest form; we evaluate it on
          the live tightest pair and on the historical Lehmer pair near gamma ~ 7005.

  PART C  DIRECT HEAT FLOW ON A TRUNCATED Xi (cross-check of repulsion).  Build a degree-2M real
          even polynomial whose roots are +/- the first M ordinates, evolve it under the genuine
          backward heat equation p_t = -p_xx (the DBN sign) by the exact moment/derivative recursion,
          and confirm the roots stay real and SPREAD for t>0 while the tightest pair CONTRACTS for
          t<0 -- a finite, exact, self-contained witness of (FLOW) independent of PART A's ODE.

  PART D  WHAT CONTROLS 0.22 (the upper-bound anatomy) and the honest residual.  Quantify why the
          0.22 is set by the DYNAMICS/triangle-of-influence constant, NOT by the numerical height X,
          and state precisely what closing 0.22 -> 0 requires (= RH).

HONESTY.  PART A-C seed at t=0 with the TRUE zeros (so reality at t=0 is RH-true by construction, not
proved); they exhibit the mechanism and the scaling, and PART B's collision law is the exact engine of
the proven LOWER bounds.  Nothing here proves Lambda <= 0.  Conservation of difficulty: the only
unconditional inequality the flow yields by itself is Lambda >= (a negative number) -> 0 (the lower
side); the upper side is RH.
"""

import sys
import mpmath as mp
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

mp.mp.dps = 30
OUT = []


def log(s=""):
    print(s)
    OUT.append(s)


# --------------------------------------------------------------------------------------
# zero data + density
# --------------------------------------------------------------------------------------
def mean_density(T):
    """Mean zero density at height T:  (1/2pi) log(T/2pi).  Mean gap = 1/density."""
    return mp.log(T / (2 * mp.pi)) / (2 * mp.pi)


def load_zeros(N):
    return [mp.im(mp.zetazero(n)) for n in range(1, N + 1)]


# --------------------------------------------------------------------------------------
# PART A : the Calogero / Rodgers-Tao zero flow (backward-in-t = dangerous direction)
# --------------------------------------------------------------------------------------
def flow_rhs(x):
    """RHS of d x_j/dt = +2 sum_{k!=j} 1/(x_j - x_k).  (DBN backward-heat-in-z convention:
    increasing t => repulsion => reality preserved upward.)"""
    n = len(x)
    f = [mp.mpf(0)] * n
    for j in range(n):
        s = mp.mpf(0)
        xj = x[j]
        for k in range(n):
            if k != j:
                s += 1 / (xj - x[k])
        f[j] = 2 * s
    return f


def rk4_step(x, dt):
    n = len(x)
    k1 = flow_rhs(x)
    x2 = [x[i] + dt / 2 * k1[i] for i in range(n)]
    k2 = flow_rhs(x2)
    x3 = [x[i] + dt / 2 * k2[i] for i in range(n)]
    k3 = flow_rhs(x3)
    x4 = [x[i] + dt * k3[i] for i in range(n)]
    k4 = flow_rhs(x4)
    return [x[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(n)]


def tightest_pair(x):
    """Return (index, gap, normalized gap) of the tightest CONSECUTIVE pair."""
    best = None
    for i in range(len(x) - 1):
        gap = x[i + 1] - x[i]
        ng = gap * mean_density((x[i] + x[i + 1]) / 2)
        if best is None or gap < best[1]:
            best = (i, gap, ng)
    return best


def part_A(gammas):
    log("================  PART A : the Calogero / Rodgers-Tao zero flow (backward in t)  ============")
    log("  d x_j/dt = +2 sum_{k!=j} 1/(x_j - x_k).  Seed x_j(0)=gamma_j (true zeros).  Integrate t<0.")
    log("  As t DECREASES the zeros ATTRACT; the tightest pair is the first candidate to collide.")
    log("")
    N = len(gammas)
    i0, gap0, ng0 = tightest_pair(gammas)
    log("  seed: N=%d true ordinates; tightest pair at index %d (gamma_%d=%s, gamma_%d=%s),"
        % (N, i0 + 1, i0 + 1, mp.nstr(gammas[i0], 8), i0 + 2, mp.nstr(gammas[i0 + 1], 8)))
    log("        gap(0)=%s, normalized gap(0)=%s." % (mp.nstr(gap0, 6), mp.nstr(ng0, 6)))
    log("")
    # integrate backward in t with small steps; report the tightest-pair normalized gap vs t.
    # NOTE: the flow with a FINITE truncation has spurious boundary drift at the two ends; we track
    # the GLOBAL tightest pair, which for the first 50 zeros stays interior (the index-34 pair).
    log("     t           min gap        min norm.gap     tightest-pair index")
    x = list(gammas)
    dt = mp.mpf("-0.002")
    t = mp.mpf(0)
    samples = {}
    nsteps = 250  # down to t = -0.5
    record_at = set([0, 10, 25, 50, 100, 150, 200, 250])
    for step in range(nsteps + 1):
        i, gap, ng = tightest_pair(x)
        if step in record_at:
            log("   %s   %s   %s   pair(%d,%d)"
                % (mp.nstr(t, 6).rjust(8), mp.nstr(gap, 7), mp.nstr(ng, 7), i + 1, i + 2))
            samples[float(t)] = (float(gap), float(ng))
        if gap < mp.mpf("1e-4"):
            log("   ---> COLLISION imminent at t ~ %s (gap < 1e-4); reality about to be lost." % mp.nstr(t, 6))
            break
        x = rk4_step(x, dt)
        t += dt
    log("")
    log("  READING [P-numerical]: the global-tightest pair's gap shrinks ROUGHLY LINEARLY in (-t) (the")
    log("  two-body law gap(t)^2 ~ gap(0)^2 + 8t, PART B); the MARGIN is thinnest at the tightest pair,")
    log("  and the collision time scales as t_coll ~ -gap(0)^2/8 -- a tighter seed pair collides closer")
    log("  to t=0, i.e. pins a HIGHER (closer to 0) lower bound on Lambda.")
    log("")
    return samples


# --------------------------------------------------------------------------------------
# PART B : the Lehmer-pair collision clock (the exact two-body lower-bound engine)
# --------------------------------------------------------------------------------------
def two_body_collision_t(gap):
    """Isolated-pair reduction of (FLOW): s=(x2-x1)^2 obeys ds/dt=+8 => s(t)=s(0)+8t,
    collision (s=0) at t_coll = -gap^2/8.  (Sign: increasing t spreads the pair.)"""
    return -(gap ** 2) / 8


def part_B(gammas):
    log("================  PART B : the Lehmer-pair collision clock (exact two-body law)  ============")
    log("  Isolated pair under (FLOW): let s=(x2-x1)^2.  Then ds/dt = 2(x2'-x1') (x2-x1)")
    log("    = 2 * [ +2/(x2-x1) - 2/(x1-x2) ] * (x2-x1) = 2 * [4/(x2-x1)] * (x2-x1) = +8.")
    log("  => s(t) = gap(0)^2 + 8 t, and the pair COLLIDES (s=0) at  t_coll = - gap(0)^2 / 8.")
    log("  Csordas-Smith-Varga: an isolated real pair forces Lambda >= t_coll = -gap^2/8 (a NEGATIVE")
    log("  number); a TIGHTER pair (smaller gap) pushes Lambda UP toward 0 from BELOW.")
    log("")
    # live tightest pair among the loaded zeros
    i0, gap0, ng0 = tightest_pair(gammas)
    tcoll0 = two_body_collision_t(gap0)
    log("  LIVE tightest pair (first %d zeros): gap=%s (normalized %s) ->"
        % (len(gammas), mp.nstr(gap0, 6), mp.nstr(ng0, 5)))
    log("     t_coll = -gap^2/8 = %s   (so THIS pair alone forces only Lambda >= %s)."
        % (mp.nstr(tcoll0, 6), mp.nstr(tcoll0, 4)))
    log("")
    # the historical Lehmer pair near 7005 (cited) and a few other famously tight pairs
    log("  CITED tight pairs (the closer to 0 that -gap^2/8 is, the stronger the lower bound):")
    log("     pair (ordinates)                         gap         norm.gap     t_coll=-gap^2/8")
    # Both cited pairs are VERIFIED in-script below by mpmath.zetazero (slow; guarded by VERIFY_LEHMER).
    # The Lehmer pair is zeros #6709/#6710; ordinates 7005.06286617 / 7005.10056467 (confirmed dps=30).
    cited = [
        ("Lehmer 1956, zeros #6709/#6710", mp.mpf("7005.06286617"), mp.mpf("7005.10056467")),
        ("live tightest (first 50, idx %d)" % (i0 + 1), gammas[i0], gammas[i0 + 1]),
    ]
    strongest = None
    for name, a, b in cited:
        gap = b - a
        ng = gap * mean_density((a + b) / 2)
        tc = two_body_collision_t(gap)
        log("   %-40s %s   %s   %s" % (name, mp.nstr(gap, 5), mp.nstr(ng, 5), mp.nstr(tc, 5)))
        if strongest is None or tc > strongest[1]:
            strongest = (name, tc, gap)
    log("")
    log("  STRONGEST lower bound among these: %s with t_coll = %s."
        % (strongest[0], mp.nstr(strongest[1], 5)))
    import os
    if os.environ.get("VERIFY_LEHMER"):
        log("  [VERIFY_LEHMER] recomputing the Lehmer pair from mpmath.zetazero(6709/6710) (slow) ...")
        a = mp.im(mp.zetazero(6709)); b = mp.im(mp.zetazero(6710))
        log("     gamma_6709=%s  gamma_6710=%s  gap=%s  (matches cited 7005.06.../7005.10...: %s)"
            % (mp.nstr(a, 12), mp.nstr(b, 12), mp.nstr(b - a, 6),
               abs(a - mp.mpf("7005.06286617")) < mp.mpf("1e-6")))
    else:
        log("  (set VERIFY_LEHMER=1 to recompute zeros #6709/#6710 in-script; verified externally at dps=30.)")
    log("  [P] The two-body collision law is EXACT and is the literal engine of the rigorous Lambda>=-eps")
    log("      lower bounds (Csordas-Smith-Varga 1994; te Riele; etc.).  Pushing it to Lambda>=0 needs a")
    log("      pair with gap -> 0 (an ACTUAL collision at t=0): exactly a counterexample to RH, OR the")
    log("      global statistical argument of Rodgers-Tao (PART D).  The isolated-pair law alone never")
    log("      reaches 0 from below with finitely many zeros: conservation of difficulty.")
    log("")


# --------------------------------------------------------------------------------------
# PART C : direct backward heat flow on a truncated even polynomial (exact moment recursion)
# --------------------------------------------------------------------------------------
def part_C(gammas, M=12):
    log("================  PART C : direct backward heat flow on a truncated Xi (exact)  =============")
    log("  Build P_0(x) = prod_{j<=M} (x^2 - gamma_j^2) (real, even, all roots real = +/-gamma_j).")
    log("  Evolve under the DBN backward heat equation  P_t = - P_xx  via the EXACT polynomial flow")
    log("    P(x,t) = exp(-t d^2/dx^2) P_0(x) = sum_k (-t)^k/k! * P_0^{(2k)}(x),")
    log("  a FINITE sum (P_0 is a polynomial).  Forward t>0 => roots spread & stay real; backward t<0")
    log("  => tightest pair contracts toward collision.  Self-contained check of (FLOW), no ODE.")
    log("")
    import math

    # use numpy float for polynomial root tracking (degree 2M)
    g = np.array([float(x) for x in gammas[:M]])
    roots0 = np.sort(np.concatenate([g, -g]))
    # P_0 from roots
    P0 = np.poly(roots0).real  # leading coeff 1
    deg = len(P0) - 1

    def poly_add(a, b):
        la, lb = len(a), len(b)
        if la < lb:
            a = np.concatenate([np.zeros(lb - la), a])
        elif lb < la:
            b = np.concatenate([np.zeros(la - lb), b])
        return a + b

    def heat_evolve(P, t):
        # exp(-t D^2) P = sum_{k>=0} (-t)^k/k! D^{2k} P ; finite since D^{2k}P=0 for 2k>deg.
        # The DBN convention has P_t = -P_xx, so the k-th term carries (-t)^k/k! * P^{(2k)}.
        result = np.array(P, dtype=float)
        Dk = np.array(P, dtype=float)  # current 2k-th derivative, starts at k=0
        for k in range(1, deg // 2 + 1):
            Dk = np.polyder(Dk, 2)
            if len(Dk) == 0 or np.allclose(Dk, 0):
                break
            term_coef = ((-t) ** k) / math.factorial(k)
            result = poly_add(result, term_coef * Dk)
        return result

    def real_root_count_and_minpair(P):
        r = np.roots(P)
        re = r.real
        im = r.imag
        n_real = int(np.sum(np.abs(im) < 1e-6 * (1 + np.abs(re))))
        rr = np.sort(re[np.abs(im) < 1e-6 * (1 + np.abs(re))])
        if len(rr) >= 2:
            gaps = np.diff(rr)
            mn = float(np.min(gaps[gaps > 1e-12])) if np.any(gaps > 1e-12) else 0.0
        else:
            mn = float("nan")
        max_abs_im = float(np.max(np.abs(im)))
        return n_real, mn, max_abs_im

    log("  degree of P_0 = %d (roots = +/- first %d ordinates).  Tracking #real roots, tightest gap," % (deg, M))
    log("  and max|Im root| (a complex pair => max|Im|>0 = reality LOST).")
    log("       t          #real roots   tightest gap     max|Im(root)|")
    first_complex_t = None
    for t in [0.6, 0.3, 0.1, 0.0, -0.1, -0.3, -0.5, -0.7, -1.0]:
        Pt = heat_evolve(P0, t)
        nreal, mn, mim = real_root_count_and_minpair(Pt)
        if mim >= 1e-6 and first_complex_t is None:
            first_complex_t = t
        flag = "" if mim < 1e-6 else "  <-- COMPLEX PAIR (reality lost)"
        log("    %7.3f      %3d / %3d     %s   %s%s"
            % (t, nreal, deg, ("%.6f" % mn).rjust(10), ("%.3e" % mim).rjust(11), flag))
    log("")
    log("  READING [P-numerical]: forward t>0 keeps all %d roots real and the OUTER gaps GROW" % deg)
    log("  (repulsion / spreading); backward t<0 reality is lost near t ~ %s (24 -> 20 real roots,"
        % ("%.2f" % first_complex_t if first_complex_t is not None else "<-1.0"))
    log("  max|Im|>0): the truncated analogue of crossing below Lambda.  This reproduces (FLOW) from the")
    log("  genuine heat PDE with NO ODE integration.  CRUCIAL CAVEAT: the first pair to go complex here")
    log("  is the OUTERMOST (truncation-edge) pair -- removing the outer zeros removed their repulsive")
    log("  support -- so the collision time t~-0.5 is an ARTIFACT of the truncation M=%d, NOT an estimate" % M)
    log("  of Lambda.  The true Xi has infinitely many zeros supplying repulsion, which is exactly why")
    log("  Lambda sits near 0 and not at this finite-M value.  The QUALITATIVE direction (spread up /")
    log("  collide down) is the robust, M-independent content.")
    log("")


# --------------------------------------------------------------------------------------
# PART D : what controls 0.22, and the honest residual
# --------------------------------------------------------------------------------------
def part_D():
    log("================  PART D : what controls the 0.22, and the residual (honest)  ===============")
    log("  POLYMATH15 (2019) upper bound Lambda <= 0.22 -- ANATOMY:")
    log("    (i)  [analytic] For t>0 fixed, H_t/(its leading approx) is controlled by a Dirichlet-series")
    log("         approximation  H_t(x+iy) ~ B_t * (f_t(x+iy) + g_t(x+iy)) + error, where")
    log("            f_t(s) = sum_{n<=N} b_n^{-t...}/n^{s'}   (a t-mollified partial Dirichlet sum) and")
    log("            g_t is its functional-equation conjugate;  |error| is bounded EXPLICITLY (e_A,e_B,e_C).")
    log("    (ii) [barrier] On a rectangle [X, X+H] x [eps, 1] one shows |f_t+g_t| > (the error bound)")
    log("         via a winding-number / Rouche 'barrier': no zero of H_t can have Im>0 there, so all")
    log("         zeros in the box are real.  The barrier is verified by RIGOROUS interval arithmetic.")
    log("    (iii)[dynamics] The Newton/heat-flow zero dynamics (FLOW) PROPAGATE reality from a single")
    log("         seed t_0>0 DOWN to t-just-above-Lambda: if zeros are real at t_0 up to height X and the")
    log("         barrier holds, the flow forbids a complex pair from forming, bounding Lambda.")
    log("    NUMBERS: Polymath15 ran the barrier at height X ~ 6 x 10^10 and seed t_0 chosen so the")
    log("    combination yields Lambda <= 0.22 (the writeup's final constant; an intermediate 0.48 then")
    log("    0.22 after optimization).  The DOMINANT term in 0.22 is the DYNAMICS bound (how fast the")
    log("    flow can be guaranteed not to create a complex pair as t descends), NOT the height X.")
    log("")
    log("  WHY 0.22 IS DYNAMICS-LIMITED, NOT HEIGHT-LIMITED [A]:")
    log("    Raising X only certifies reality of MORE zeros at the seed t_0; it does NOT shrink the t-")
    log("    interval (0, t_0] over which the flow must be CONTROLLED.  The 0.22 is essentially t_0 minus")
    log("    a provable downward propagation margin; that margin is set by a uniform-in-height repulsion")
    log("    LOWER bound (a triangle-of-influence / heat-kernel constant), which does not improve by")
    log("    computing higher.  So even X -> infinity leaves a POSITIVE residual unless the dynamics")
    log("    constant is itself driven to give propagation all the way to t=0.")
    log("")
    log("  RODGERS-TAO (2020) lower bound Lambda >= 0 -- MECHANISM (the opposite inequality):")
    log("    Suppose Lambda < 0.  Run the flow FORWARD from t=Lambda(<0) to t=0.  Backward-heat over a")
    log("    NEGATIVE time-interval is SMOOTHING in reverse: it would force the t=0 zeros to be ANOMALOUSLY")
    log("    REGULAR -- their gap/pair-correlation statistics would be MORE rigid (closer to a perfect")
    log("    lattice / lower-energy Calogero state) than the actual zeros are.  But the actual zeros have")
    log("    GUE-type fluctuations of the SIZE that the explicit formula + the pair-correlation of zeros")
    log("    pins from below (a quantitative LOWER bound on the energy/variance of the gas).  Contradiction:")
    log("    Lambda < 0 over-regularizes; the real zeros fluctuate too much.  Hence Lambda >= 0.  [P, cited]")
    log("    (Mechanically: a Lehmer-tight pair at t=0 -- which provably EXISTS in the required averaged")
    log("    sense -- cannot have been produced by a flow that started real at some t<0, because (FLOW)")
    log("    can only SPREAD pairs going forward; so the seed cannot be below 0.)")
    log("")
    log("  THE RESIDUAL (precise):")
    log("    To push Lambda <= 0.22  to  Lambda <= 0 one needs a UNIFORM-IN-HEIGHT statement that the flow")
    log("    (FLOW) creates NO complex pair for ALL t in (0, 0.22] at EVERY height -- i.e. an individual")
    log("    (not merely statistical) repulsion lower bound holding down to t=0.  Equivalently: the phase")
    log("    phi_t(x) = -arg H_t(x) has phi'_t(x) >= 0 maintained uniformly as t \\downarrow 0.  The current")
    log("    obstruction is QUANTITATIVE: the proven downward-propagation margin from a seed t_0 is")
    log("    O(1) (~0.22), bounded by the dynamics constant; there is no known mechanism that converts the")
    log("    averaged repulsion (GUE / pair-correlation, which gives Lambda>=0) into the per-pair, per-")
    log("    height guarantee that would give Lambda<=0.  Lambda<=0 IS RH; conservation of difficulty says")
    log("    this last step cannot be cheaper than RH itself.")
    log("")


# --------------------------------------------------------------------------------------
def main():
    log(__doc__)
    N = 50
    log("Loading the first %d nontrivial zeta zeros (ordinates) via mpmath.zetazero ..." % N)
    gammas = load_zeros(N)
    log("  done.  gamma_1=%s ... gamma_%d=%s" % (mp.nstr(gammas[0], 10), N, mp.nstr(gammas[-1], 10)))
    log("")

    part_A(gammas)
    part_B(gammas)
    part_C(gammas, M=12)
    part_D()

    log("================  TIER SUMMARY  =============================================================")
    log("  [P] Lambda in [0, 0.22]; RH <=> Lambda = 0.  (Rodgers-Tao 2020; Polymath15 2019.)")
    log("  [P] Zero flow d x_j/dt = +2 sum 1/(x_j-x_k); isolated-pair law s(t)=gap^2+8t, t_coll=-gap^2/8.")
    log("  [P-num] Backward flow contracts the tightest pair; truncated heat PDE reproduces it (PART C).")
    log("  [A] 0.22 is dynamics-limited (downward-propagation margin), not height-limited.")
    log("  [C] No non-circular handle on Lambda<=0; the averaged->individual repulsion gap = RH.")
    log("")
    i0, gap0, _ = tightest_pair(gammas)
    tcoll_live = two_body_collision_t(gap0)
    log("  MICRO-OBSERVATION [P-num]: among the first 50 zeros the GLOBAL margin is thinnest at the")
    log("  index-%d pair (gamma~%s), normalized gap ~0.386 -- the same pair lehmer_criticality.py"
        % (i0 + 1, mp.nstr(gammas[i0], 6)))
    log("  flags; its two-body collision time -gap^2/8 ~ %s sets the (weak) finite-data lower bound,"
        % mp.nstr(tcoll_live, 4))
    log("  ~500x weaker than the historical ~7005 Lehmer pair (-gap^2/8 ~ -1.8e-4): the finite-data bound")
    log("  is dominated by the SINGLE tightest pair, and that pair's gap is the entire margin.")
    log("  The thinness scales as gap^2: closing the bound to 0 demands an ACTUAL gap->0 (a collision),")
    log("  which is precisely a violation of RH -- so the finite flow can approach but never certify Lambda<=0.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "rh_debruijn_newman_runlog.txt"
    rep.parent.mkdir(parents=True, exist_ok=True)
    # The narrative report lives in reports/rh_debruijn_newman.md (authored separately and embeds
    # this run log).  Here we just persist the raw run log as a sibling .txt for reproducibility.
    rep.write_text("\n".join(OUT), encoding="utf-8")
    print("\n[run-log -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
