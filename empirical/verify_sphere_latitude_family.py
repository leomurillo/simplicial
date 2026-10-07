r"""The physics.SE question, made concrete: two points on a sphere -> a ONE-PARAMETER FAMILY of
circles (latitudes), hence a family of predictions for r(t+2).  The great circle is ONE member.

Setup (verbatim from the post): particle on a sphere R const, purely tangential, UNIFORM (constant
angular velocity); observe r(t), r(t+1); predict r(t+2) with equal time steps.

OP's (correct) insight: the rotation axis can be ANY line through the origin; the particle could ride
ANY circle through the two points (any 'latitude'), not necessarily the great circle.  Commenters:
(i) only the great circle is a geodesic (force-free); a small circle needs a tangential force; (ii)
two points do NOT determine a circle -> infinite family; (iii) least action canNOT pick among systems
with different constraints/potentials.

This probe sweeps the family.  A circle through p1,p2 has axis a with a.p1 = a.p2, i.e. a _|_ (p1-p2):
the admissible axes form a GREAT CIRCLE.  For each axis a, the unique rotation R(a,phi) with R p1 = p2
gives the prediction p3 = R p2.  We sweep a, show the predictions p3(a) span a large arc (the 'space
of possibilities'), mark the great-circle (geodesic) member and the rotation-invariant ('max-entropy
prior') mean, and confirm: TWO POINTS DO NOT DETERMINE r(t+2); a model (a force law, or a prior over
axes) must be supplied.

NUMERICAL (numpy), labelled.
"""

import sys
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
np.set_printoptions(precision=4, suppress=True)


def rodrigues(a, phi, v):
    a = a / np.linalg.norm(a)
    return (v * np.cos(phi) + np.cross(a, v) * np.sin(phi) + a * (a @ v) * (1 - np.cos(phi)))


def phi_p1_to_p2(a, p1, p2):
    a = a / np.linalg.norm(a)
    q1 = p1 - (a @ p1) * a
    q2 = p2 - (a @ p2) * a
    if np.linalg.norm(q1) < 1e-9 or np.linalg.norm(q2) < 1e-9:
        return None
    return np.arctan2(a @ np.cross(q1, q2), q1 @ q2)


def ang(u, v):
    u = u / np.linalg.norm(u); v = v / np.linalg.norm(v)
    return np.degrees(np.arccos(np.clip(u @ v, -1, 1)))


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    p1 = np.array([1.0, 0.20, 0.10]); p1 /= np.linalg.norm(p1)
    p2 = np.array([0.80, 0.55, 0.20]); p2 /= np.linalg.norm(p2)
    log("  observed:  r(t)=p1=%s   r(t+1)=p2=%s   step=%.2f deg" % (p1, p2, ang(p1, p2)))
    log("")

    # admissible axes: a _|_ (p1-p2); parametrize that great circle
    d = p1 - p2
    e1 = np.cross(d, [1, 0, 0])
    if np.linalg.norm(e1) < 1e-6:
        e1 = np.cross(d, [0, 1, 0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(d, e1); e2 /= np.linalg.norm(e2)   # e1,e2 span the plane _|_ d

    a_great = np.cross(p1, p2); a_great /= np.linalg.norm(a_great)

    preds = []
    log("================  the family of predictions p3(a) as the axis (latitude) sweeps  ============")
    log("   axis angle psi   latitude(a.p1)   rotation phi(deg)    predicted r(t+2) = p3")
    for psi in np.linspace(0, np.pi, 13, endpoint=False):
        a = np.cos(psi) * e1 + np.sin(psi) * e2
        phi = phi_p1_to_p2(a, p1, p2)
        if phi is None or abs(phi) < 1e-6:
            continue
        p3 = rodrigues(a, phi, p2)
        preds.append(p3)
        lat = a @ p1
        tag = "  <- GREAT CIRCLE (geodesic)" if ang(a, a_great) < 6 or ang(a, -a_great) < 6 else ""
        log("     %5.1f         %+.3f          %7.1f         %s%s"
            % (np.degrees(psi), lat, np.degrees(phi), np.array2string(p3), tag))
    preds = np.array(preds)

    # the geodesic (great-circle) prediction, explicitly
    phi_g = phi_p1_to_p2(a_great, p1, p2)
    p3_great = rodrigues(a_great, phi_g, p2)

    # the rotation-invariant ('max-entropy over axis') mean prediction
    p3_mean = preds.mean(axis=0); p3_mean /= np.linalg.norm(p3_mean)

    log("")
    spread = max(ang(preds[i], preds[j]) for i in range(len(preds)) for j in range(i + 1, len(preds)))
    log("  SPREAD of the prediction family: %.1f deg  (two points leave r(t+2) this undetermined)." % spread)
    log("  great-circle (geodesic, force-free) prediction:        p3 = %s" % p3_great)
    log("  rotation-invariant 'max-entropy prior' mean prediction: p3 = %s  (NOT the great circle:" % p3_mean)
    log("    %.1f deg away) -- a coherent 'most likely' answer, but the PRIOR is doing the work."
        % ang(p3_great, p3_mean))
    log("")
    log("================  WHAT THIS SHOWS (answering the post)  ================")
    log("1. OPTIMAL prediction? -- CONDITIONAL on a model, not unconditional.  Two points + constant")
    log("   angular speed leave a whole great circle of axes (latitudes); r(t+2) is undetermined by")
    log("   %.0f deg.  There is no model-free 'optimal'." % spread)
    log("2. Is the great circle NECESSARY? -- It is the UNIQUE geodesic = force-FREE motion (angular")
    log("   momentum conserved).  It is necessary iff there is no tangential force.  Every other")
    log("   latitude needs a specific tangential (toward-a-pole) force = a specific potential.  So")
    log("   'great circle' is selected by the PHYSICS assumption (no tangential force), not by the data.")
    log("3. If NOT the great circle? -- then a tangential force/potential fixes the latitude, and you")
    log("   must know it; the two points alone cannot.  Absent it, only a Bayesian estimate under a")
    log("   PRIOR over axes is possible (e.g. the max-entropy mean above) -- which is exactly the OP's")
    log("   'not greatest, not shortest' answer, made rigorous.  BUT: this is BAYES, not least action.")
    log("")
    log("THE CATCH ON 'use least action (LA) to pick the most likely latitude': least action chooses")
    log("the PATH within a FIXED Lagrangian; it cannot choose AMONG Lagrangians/latitudes (Vavrik's")
    log("comment).  With the free Lagrangian it returns the great circle (the SHORTEST) -- contradicting")
    log("the OP's 'not the shortest'.  To land on a small circle one must put in a potential, OR replace")
    log("'least action' with an explicit PRIOR over axes (Bayesian model selection).  The honest move:")
    log("state the prior (= the unstated physics).  Info-geometry: 'most likely' and 'geodesic' both")
    log("depend on a choice (prior / connection) NOT in the data; they collapse to one answer only at")
    log("the symmetric (force-free / max-entropy) corner.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "sphere_latitude_family.md"
    header = [
        "# Two points on a sphere -> a one-parameter family of latitudes; the great circle is one member",
        "",
        "**Script:** `empirical/verify_sphere_latitude_family.py`",
        "**Context:** the actual physics.SE question (predict r(t+2) on a sphere from two points).",
        "**Finding:** r(t+2) is undetermined across a wide arc; great circle = the unique geodesic (force-free);",
        "any other latitude needs a tangential force; 'most likely' needs a PRIOR (Bayes), not least action.",
        "**Nature:** numerical (numpy), conceptual demonstration.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
