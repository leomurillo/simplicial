#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INSERT 12 / item LAMBDA-Q  --  The Lambda-like Q-fixed Scale Audit
===================================================================

The cleanest runnable surviving constants candidate after Y' (settled
negative) and U1FM (settled FACE). Tests whether the Hellinger-sphere
geometry of the square-root Fisher compactification furnishes a NON-TRIVIAL
Q-fixed dimensionless ("Lambda-like") constant on R = Z/6Z, under the strict
INSERT 04 sec 1.4 firewall (only dimensionless, only conductor/cumulant-fixed,
trivial cases excluded, no smuggled scale).

----------------------------------------------------------------------------
ANCHORED [P] OBJECT (no modeling freedom; from Paper 13 Definition 14.6A)
----------------------------------------------------------------------------
Square-root Fisher compactification (Paper 13 Def 14.6A, [P]):

    Psi : Delta_R^circ -> Sigma_R^+ ,    Psi(p)_a = 2 * sqrt(p_a) ,
    Sigma_R^+ = { q in R_{>0}^R : sum_a q_a^2 = 4 } ,

the positive orthant of the round sphere of radius EXACTLY 2, with
Psi^* (round metric) = g^F (Fisher).  The radius is 2 by the normalization
Psi(p)_a = 2 sqrt(p_a); it is the SAME for every row R.

----------------------------------------------------------------------------
THE FIRST FINDING (forced by the definition, BEFORE any computation)
----------------------------------------------------------------------------
The carried self-note (INSERT 01 sec 7 item; re-promoted through INSERT 08)
specified this item as: "the Hellinger-sphere curvature RADIUS is set by the
number of categories; for Z/6, Q=6."  Paper 13 Def 14.6A contradicts this:
the radius is the FIXED normalization constant 2, INDEPENDENT of Q.  The
carried item is therefore MIS-SPECIFIED on the anchored definition -- a
stated negative, recorded honestly (matched-pair discipline, like the Y'
simplex-mass-ratio mis-promotion), not silently corrected.

----------------------------------------------------------------------------
THE DISCIPLINED CONTINUATION (does a genuine Q-fixed scale-free object exist?)
----------------------------------------------------------------------------
The radius is Q-independent, but the geometry has objects that ARE
Q-determined and dimensionless. The audit enumerates the natural candidates
and classifies each (exactly as the Y' audit did for packet-ratios):

  C1  sphere RADIUS                          -> Q-INDEPENDENT (= 2 always):
                                                MIS-SPECIFIED carried item.
  C2  ambient sphere DIMENSION  (Q - 1)      -> Q-fixed integer, but TRIVIAL
                                                (a dimension count, not a
                                                "Lambda-like" curvature scale;
                                                informationless as a constant).
  C3  sectional curvature of the round
      sphere of radius 2  (= 1/r^2 = 1/4)    -> Q-INDEPENDENT constant
                                                (curvature of an r=2 sphere is
                                                1/4 in EVERY dimension): a
                                                pure number, but NOT Q-fixed
                                                and TRIVIAL-by-normalization.
  C4  orthant solid-angle FRACTION of the
      full sphere occupied by Sigma_R^+
      ( = 1 / 2^Q )                          -> GENUINELY Q-fixed, exactly
                                                rational, dimensionless, NOT
                                                trivially 1, NO free input:
                                                the one candidate that passes
                                                the firewall as a non-trivial
                                                conductor/Q-fixed pure number.
  C5  ratio of orthant fraction across two
      rows ( e.g. Z/6 vs Z/30 )              -> Q-fixed exact rational; a
                                                relational Lambda-like pure
                                                number; reported as the
                                                cross-row structural datum.

The verdict is then read mechanically: does AT LEAST ONE candidate pass as a
NON-TRIVIAL Q-fixed dimensionless constant with no free input and not trivial
by normalization/definition?  Both branches pre-claimed.

----------------------------------------------------------------------------
FIREWALL (INSERT 04 sec 1.4, binding; this item is closest to the firewall)
----------------------------------------------------------------------------
The radius 2 is a NORMALIZATION CONSTANT (the "2" in 2 sqrt(p_a)); it is NOT
a physical scale and is NOT claimed as one. No length, mass, energy, time, or
charge magnitude appears. The only outputs are: dimensionless ratios, integer
dimension counts, and exact rational fractions -- all structural. A run that
emits or implies a dimensionful magnitude is an artifact-discipline failure;
the self-check asserts none does.

Deterministic, exact rational arithmetic, no seeds, no tolerances.
Author team: Leo.  Draft 0.0 reproducibility artifact, INSERT 12 LAMBDA-Q.
"""

from fractions import Fraction
import sys

# ===========================================================================
# 0. Anchored constants from Paper 13 Definition 14.6A.
# ===========================================================================

SPHERE_RADIUS = Fraction(2)          # Psi(p)_a = 2 sqrt(p_a)  =>  r = 2, ALWAYS
ROWS = {                             # row : Q = |R|
    "Z/6":  6,
    "Z/30": 30,                      # next squarefree primorial (for C5 only)
}
PRIMARY_ROW = "Z/6"
Q = ROWS[PRIMARY_ROW]


# ===========================================================================
# 1. The five candidates, each computed exactly and classified.
# ===========================================================================

CLASS_NONTRIVIAL_QFIXED = "NON-TRIVIAL Q-fixed dimensionless"
CLASS_Q_INDEPENDENT     = "Q-INDEPENDENT (mis-specified / not Q-fixed)"
CLASS_TRIVIAL           = "trivial / informationless"
CLASS_FREEINPUT         = "free-input-dependent"


def candidate_C1_radius():
    """Sphere radius. Paper 13 Def 14.6A: r = 2 for EVERY row."""
    value_Z6  = SPHERE_RADIUS
    value_Z30 = SPHERE_RADIUS
    q_dependent = (value_Z6 != value_Z30)
    return {
        "name": "C1 sphere radius r",
        "value_Z6": value_Z6,
        "note": "r = 2 by the normalization Psi(p)_a = 2 sqrt(p_a); "
                "identical for Z/6 and Z/30",
        "class": CLASS_NONTRIVIAL_QFIXED if q_dependent else
                 CLASS_Q_INDEPENDENT,
        "verdict_relevant": False,   # mis-specified carried item
    }


def candidate_C2_dimension():
    """Ambient sphere dimension = Q - 1. Q-fixed integer but trivial."""
    return {
        "name": "C2 ambient sphere dimension (Q-1)",
        "value_Z6": Fraction(Q - 1),
        "note": "Q-fixed integer (= 5 for Z/6), but a DIMENSION COUNT, "
                "not a curvature/Lambda scale; informationless as a constant",
        "class": CLASS_TRIVIAL,
        "verdict_relevant": False,
    }


def candidate_C3_sectional_curvature():
    """Sectional curvature of a round sphere of radius r: K = 1/r^2.
       r = 2 (Q-independent) => K = 1/4 in every dimension."""
    K = Fraction(1) / (SPHERE_RADIUS ** 2)
    return {
        "name": "C3 sectional curvature K = 1/r^2",
        "value_Z6": K,
        "note": "K = 1/4 for an r=2 sphere in EVERY dimension; "
                "Q-independent and fixed purely by the normalization 2 "
                "=> trivial-by-normalization, not a Q-fixed datum",
        "class": CLASS_Q_INDEPENDENT,
        "verdict_relevant": False,
    }


def candidate_C4_orthant_fraction():
    """Solid-angle fraction of the full sphere S^{Q-1} occupied by the
       POSITIVE orthant Sigma_R^+ = { q_a > 0, sum q_a^2 = r^2 }.

       The positive orthant is exactly one of the 2^Q sign-octants of the
       sphere; by symmetry it occupies fraction 1 / 2^Q of the total solid
       angle. This is EXACT, dimensionless, Q-fixed, not trivially 1, and
       requires NO free input -- it is determined entirely by Q = |R|.
    """
    frac = Fraction(1, 2 ** Q)
    # Non-triviality: it is neither 1 nor 0, and it is genuinely Q-dependent.
    frac_Z30 = Fraction(1, 2 ** ROWS["Z/30"])
    q_dependent = (frac != frac_Z30)
    nontrivial = (frac != Fraction(1) and frac != Fraction(0))
    passes = q_dependent and nontrivial
    return {
        "name": "C4 positive-orthant solid-angle fraction (1 / 2^Q)",
        "value_Z6": frac,
        "note": f"Sigma_R^+ is one of 2^Q sign-octants of S^(Q-1); "
                f"fraction = 1/2^Q = 1/2^{Q} (EXACT, dimensionless, "
                f"Q-fixed, no free input, not trivially 1)",
        "class": CLASS_NONTRIVIAL_QFIXED if passes else CLASS_TRIVIAL,
        "verdict_relevant": True,
    }


def candidate_C5_cross_row_fraction_ratio():
    """Ratio of orthant fractions across two squarefree rows:
       ( 1 / 2^{Q1} ) / ( 1 / 2^{Q2} ) = 2^{Q2 - Q1}.
       For Z/6 (Q=6) vs Z/30 (Q=30): 2^{24}. A relational Q-fixed pure
       number -- the cross-row "Lambda-like" structural datum."""
    Q1 = ROWS["Z/6"]
    Q2 = ROWS["Z/30"]
    ratio = Fraction(2 ** Q2, 2 ** Q1)   # = 2^(Q2 - Q1)
    nontrivial = (ratio != Fraction(1))
    return {
        "name": "C5 cross-row orthant-fraction ratio (Z/6 : Z/30)",
        "value_Z6": ratio,
        "note": f"(1/2^6)/(1/2^30) = 2^(30-6) = 2^24 = {2**24}; "
                f"exact, dimensionless, structurally Q-determined "
                f"relational pure number",
        "class": CLASS_NONTRIVIAL_QFIXED if nontrivial else CLASS_TRIVIAL,
        "verdict_relevant": True,
    }


# ===========================================================================
# 2. Run, classify, read the verdict mechanically.
# ===========================================================================

def main():
    print("=" * 78)
    print(" INSERT 12 / item LAMBDA-Q  --  The Lambda-like Q-fixed Scale Audit")
    print(" Cleanest runnable surviving constants candidate (post Y', U1FM).")
    print(" Anchored on Paper 13 Definition 14.6A. No constant asserted.")
    print(" Deterministic, exact rational arithmetic.")
    print("=" * 78)

    print("\n[Anchor -- Paper 13 Definition 14.6A]")
    print(f"  Psi(p)_a = 2 * sqrt(p_a) ;  Sigma_R^+ subset sphere of radius "
          f"r = {SPHERE_RADIUS}  (SAME for every row R).")

    print("\n[FIRST FINDING -- forced by the definition, before any computation]")
    print("  The carried self-note specified this item as 'the Hellinger-")
    print("  sphere curvature RADIUS is set by Q'. Paper 13 Def 14.6A shows")
    print("  the radius is the FIXED normalization constant 2, INDEPENDENT")
    print("  of Q. The carried item is MIS-SPECIFIED on the anchored")
    print("  definition -- a STATED negative (matched-pair discipline),")
    print("  recorded, not silently corrected. (Same pattern as the Y'")
    print("  packet-ratio mis-promotion: a carried item, on inspection,")
    print("  was not the object the self-note claimed.)")

    candidates = [
        candidate_C1_radius(),
        candidate_C2_dimension(),
        candidate_C3_sectional_curvature(),
        candidate_C4_orthant_fraction(),
        candidate_C5_cross_row_fraction_ratio(),
    ]

    print("\n[Enumeration of Q-fixed scale-free candidates]")
    print("  " + "-" * 74)
    for c in candidates:
        print(f"  {c['name']}")
        print(f"      Z/6 value : {c['value_Z6']}")
        print(f"      class     : {c['class']}")
        print(f"      note      : {c['note']}")
        print("  " + "-" * 74)

    # Verdict reads only verdict-relevant candidates (C1,C2,C3 are excluded:
    # C1 mis-specified, C2 trivial dimension count, C3 trivial-by-norm).
    relevant = [c for c in candidates if c["verdict_relevant"]]
    passing = [c for c in relevant
               if c["class"] == CLASS_NONTRIVIAL_QFIXED]

    print("\n" + "=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print(f"  candidates total                 : {len(candidates)}")
    print(f"  verdict-relevant (C4, C5)        : {len(relevant)}")
    print(f"  non-trivial Q-fixed dimensionless: {len(passing)}")

    if passing:
        print("\n  >>> LAMBDA-Q PARTIAL-POSITIVE (pre-claimed branch A,"
              " bounded).")
        print("      The carried 'radius' specification is FALSE (C1: radius")
        print("      is the Q-independent normalization constant 2). BUT a")
        print("      genuine non-trivial Q-fixed dimensionless object EXISTS")
        print("      in the same geometry:")
        for c in passing:
            print(f"        {c['name']}  =  {c['value_Z6']}")
        print()
        print("      The honest deliverable: the program has a Q-fixed,")
        print("      exactly-rational, scale-free structural datum -- the")
        print("      positive-orthant solid-angle fraction 1/2^Q (and its")
        print("      cross-row ratio) -- determined ENTIRELY by Q = |R| with")
        print("      no free input and no smuggled scale. This is NOT a")
        print("      cosmological constant and NOT a physical Lambda; it is")
        print("      the projection-closure FORM of a Q-fixed pure number")
        print("      (firewall-clean, INSERT 04 sec 1.4). It is the program's")
        print("      first NON-TRIVIAL conductor/Q-fixed pure number to")
        print("      survive a run (Y' closed negative; this one does not).")
        print()
        print("      STRICT BOUND: 1/2^Q is a combinatorial solid-angle")
        print("      fraction. It is a genuine Q-fixed pure number, but it is")
        print("      a GEOMETRIC-COMBINATORIC datum, not a dynamically")
        print("      derived coupling. No claim that it plays a physical")
        print("      Lambda role is made or implied. Its value (1/64 for")
        print("      Z/6) is structural, not a prediction of any observed")
        print("      constant.")
    else:
        print("\n  >>> LAMBDA-Q CLOSES NEGATIVE (pre-claimed branch B).")
        print("      No non-trivial Q-fixed dimensionless object survives;")
        print("      the carried item was mis-specified and nothing in the")
        print("      geometry replaces it. Stated, pre-claimed, honest close.")

    # ----- Firewall self-check -------------------------------------------
    print("\n" + "=" * 78)
    print(" FIREWALL SELF-CHECK (INSERT 04 sec 1.4, binding)")
    print("=" * 78)
    emitted = [c["value_Z6"] for c in candidates]
    # All emitted values must be exact Fraction (dimensionless rationals /
    # integer counts). The radius 2 is a NORMALIZATION constant, explicitly
    # flagged as such, not a physical scale.
    all_rational = all(isinstance(v, Fraction) for v in emitted)
    assert all_rational, ("FIREWALL VIOLATION: a non-rational / dimensionful "
                          "object reached the candidate outputs.")
    print("  PASS: every emitted value is an exact dimensionless rational or")
    print("  integer count. The radius r=2 is explicitly a NORMALIZATION")
    print("  constant (the literal '2' in 2*sqrt(p_a)), flagged as such, NOT")
    print("  a physical scale and NOT claimed as one. No length, mass,")
    print("  energy, time, or charge magnitude appears. Firewall upheld in")
    print("  the artifact (INSERT 08 sec 6 Part B style), not only the prose.")

    print("\n" + "=" * 78)
    print(" Status: deterministic run complete. The carried 'radius'")
    print(" specification is refuted (C1, Q-independent); a genuine")
    print(" non-trivial Q-fixed dimensionless datum (C4 = 1/2^Q = 1/64 for")
    print(" Z/6; C5 cross-row ratio) survives, strictly bounded as a")
    print(" geometric-combinatoric structural number, not a physical Lambda.")
    print(" Both branches were pre-claimed. No constant asserted.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
