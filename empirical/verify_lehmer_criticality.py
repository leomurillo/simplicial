r"""Forcing the displacement away: the t->0 face, the repulsion mechanism, and why Lambda=0 is a knife-edge.

The unified open step (P0 sec8.3, Conj 8.5): force the additive/phase object to FORBID a zero's off-axis
displacement.  On the de Bruijn-Newman face this is: the heat-flow Xi_t(z)=int e^{tu^2}Phi cos(uz) du is
real-rooted for t>Lambda; RH = Lambda<=0 (real-rooted down to t=0).  As t DECREASES, a complex pair can
only appear via a COLLISION of two real roots (a real double root) -- "phase leakage."  The mechanism
that RESISTS collision is the zeros' mutual REPULSION: under the heat/Dyson flow the roots obey
x_j' = -2 sum_{k!=j} 1/(x_j - x_k) (repulsive), so real roots push apart; a collision is the repulsion
losing.  This repulsion IS the GUE / Montgomery pair-correlation = the archimedean oscillator (front a):
the SAME object three faces over.

So "force the additive/phase object to forbid the displacement" = "the repulsion never loses, down to t=0"
= Lambda<=0 = RH.  And the marginality is concrete and famous:
  * CLOSE PAIRS (Lehmer pairs) = near-collisions.  A pair of zeros far closer than the mean spacing is a
    pair the backward flow would collide quickly -- so it forces Lambda BOUNDED BELOW (Lehmer; Csordas-
    Smith-Varga): tighter pair => Lambda forced closer to 0 from BELOW.  Rodgers-Tao (2018) closed this:
    Lambda >= 0 unconditionally.  RH = Lambda <= 0.  So Lambda = 0 is the KNIFE-EDGE: close pairs exist
    (forcing Lambda>=0) yet none actually collides at t=0 (RH).  The repulsion wins -- but only just.

This probe makes the criticality concrete: (1) the closest normalized zero-pair in reach (live demo that
near-collisions occur); (2) the famous Lehmer pair near T~7005 (cited) as the extreme; (3) the honest
verdict: the forcing mechanism (repulsion) is real and PROVABLY critical from below (Lambda>=0), but the
upper side (Lambda<=0, "no pair EVER collides") needs the INDIVIDUAL (not statistical) guarantee -- which
is RH.  NOT a proof; the marginality is now a named arithmetic phenomenon.

NUMERICAL (mpmath), labelled.
"""

import sys
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 25


def density(T):
    # mean zero density at height T: (1/2pi) log(T/2pi); mean gap = 1/density
    return mp.log(T / (2 * mp.pi)) / (2 * mp.pi)


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    N = 100
    log("Computing the first %d nontrivial zeros (ordinates) ..." % N)
    g = [mp.im(mp.zetazero(n)) for n in range(1, N + 1)]
    log("  done.")
    log("")

    # ---- PART 1 : closest normalized pair in reach (near-collisions occur) ----
    log("================  PART 1 : the closest normalized zero-pair in reach (a near-collision)  ====")
    rows = []
    for i in range(N - 1):
        gap = g[i + 1] - g[i]
        ng = gap * density(g[i])           # normalized gap; mean ~ 1
        rows.append((i + 1, g[i], g[i + 1], gap, ng))
    rows_sorted = sorted(rows, key=lambda r: r[4])
    log("  normalized gap = (gap) x (local density); GUE mean = 1, and P(small) ~ (gap)^2 (repulsion).")
    log("  The 4 closest consecutive pairs among the first %d zeros:" % N)
    log("     n     gamma_n        gamma_{n+1}      gap        normalized gap")
    for (n, a, b, gap, ng) in rows_sorted[:4]:
        log("   %4d   %s   %s   %s    %s" % (n, mp.nstr(a, 8), mp.nstr(b, 8), mp.nstr(gap, 5), mp.nstr(ng, 5)))
    nclose = sum(1 for r in rows if r[4] < mp.mpf("0.6"))
    log("  pairs with normalized gap < 0.6 (notably close): %d of %d  -- repulsion suppresses but does"
        % (nclose, N - 1))
    log("  NOT forbid close pairs; each is a near-collision the backward heat flow would tighten.")
    log("")

    # ---- PART 2 : the famous Lehmer pair (cited extreme) ----
    log("================  PART 2 : the Lehmer pair near T ~ 7005 (the extreme near-collision)  ======")
    gL1 = mp.mpf("7005.062866")
    gL2 = mp.mpf("7005.100564")
    gapL = gL2 - gL1
    ngL = gapL * density(gL1)
    log("  (cited; Lehmer 1956) gamma ~ %s and %s, gap ~ %s," % (mp.nstr(gL1, 10), mp.nstr(gL2, 10), mp.nstr(gapL, 4)))
    log("  normalized gap ~ %s  -- about %sx tighter than the mean: a celebrated near-collision."
        % (mp.nstr(ngL, 4), mp.nstr(1 / ngL, 3)))
    log("  Such pairs are exactly what gives RIGOROUS LOWER bounds on the de Bruijn-Newman constant")
    log("  (Csordas-Smith-Varga 'Lehmer pair' criterion): the tighter the pair, the closer Lambda is")
    log("  pushed to 0 FROM BELOW.  The historical chain of Lehmer pairs drove Lambda > -(tiny), and")
    log("  Rodgers-Tao (2018) then proved Lambda >= 0 outright.")
    log("")

    # ---- PART 3 : the criticality / the honest verdict ----
    log("================  PART 3 : Lambda = 0 is a knife-edge; the forcing, honestly  ================")
    log("THE MECHANISM (real): zero repulsion (x_j' = -2 sum 1/(x_j-x_k)) resists collision; it is the")
    log("GUE/Montgomery pair-correlation = the archimedean oscillator (front a) -- the SAME object as the")
    log("phase clock phi' (front b's count) and the Kubo-Mori curvature current.  Forcing the additive/")
    log("phase object to forbid the off-axis displacement = the repulsion never losing, down to t=0.")
    log("")
    log("WHAT IS PROVEN (non-circular): Lambda >= 0 (Rodgers-Tao), driven from below by close (Lehmer)")
    log("pairs -- near-collisions that exist and pin Lambda up against 0.  So the displacement is")
    log("PERPETUALLY ATTEMPTED (close pairs) and the lower side is settled.")
    log("WHAT IS OPEN (= RH): Lambda <= 0 -- that NO pair EVER actually collides at t=0.  The repulsion")
    log("is STATISTICALLY sufficient (GUE: P(gap->0) ~ gap^2), but RH needs the INDIVIDUAL guarantee for")
    log("every pair at every height -- the same average->individual gap as the Siegel core, the same")
    log("'soft bound is the wrong instrument' as the Born/Bures/CRT blindness.  Lambda = 0 is the knife-")
    log("edge: the repulsion wins at t=0 (RH) by exactly zero margin (the Weil margin 0 / R(0)~0.9999).")
    log("")
    log("HONEST VERDICT: the forcing mechanism is named and provably critical from one side; the other")
    log("side is RH and is NOT crossed.  The marginality is no longer abstract -- it is the existence of")
    log("Lehmer pairs (proven near-collisions) against the absence of an actual collision (RH).  The one")
    log("missing ingredient remains the individual/integrality guarantee that the statistical repulsion")
    log("does not supply: self-adjointness of H = phi'>=0 from arithmetic = Lambda<=0 = L(1,chi) bound.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "lehmer_criticality.md"
    header = [
        "# Forcing the displacement: zero repulsion, Lehmer pairs, and the Lambda=0 knife-edge",
        "",
        "**Script:** `empirical/verify_lehmer_criticality.py`",
        "**Context:** attempting the unified open step (P0 Conj 8.5) on the de Bruijn-Newman (t->0) face.",
        "**Finding:** repulsion is the forcing mechanism (= GUE/oscillator); close (Lehmer) pairs prove",
        "Lambda>=0 from below; Lambda<=0 (no actual collision) is RH; Lambda=0 = knife-edge, margin 0.",
        "**Nature:** numerical (mpmath), labelled.  NOT a proof (the upper side IS RH).",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
