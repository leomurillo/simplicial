r"""'Are we sure it is geodesic?' -- on a statistical (Fisher-Rao) sphere, GEODESIC is not one curve.

Setup (the physics.SE question, from its title): a particle in spherical motion; given two prior
positions p1, p2, predict the next.  The textbook move: assume great-circle (geodesic) motion at
constant angular speed and extrapolate.  This probe shows that the moment the sphere carries an
INFORMATION-GEOMETRIC structure (the round sphere IS the Fisher-Rao manifold of the categorical
family, via p -> u = sqrt(p)), "the geodesic" splits into Amari's one-parameter alpha-family, and
the SAME two priors give DIFFERENT predicted third points:

  alpha = 0  (Levi-Civita / Fisher-Rao):  great circle in u=sqrt(p).         (the textbook answer)
  alpha = -1 (mixture / m-connection):     straight line in p (mean params).  p(t)=(1-t)p1+t p2.
  alpha = +1 (exponential / e-connection): straight line in log p (natural).  p(t) ~ p1^{1-t} p2^t.

The m- and e-geodesics are the NATURAL straight lines for statistical/inferential dynamics
(Bayesian mixing ~ m; exponential-family drift ~ e); the great circle is the free-kinetic
(Levi-Civita) one.  Two points cannot say which -- so 'geodesic' is a modeling choice, not a given.

NUMERICAL (numpy), labelled.  This is a conceptual demonstration, not a claim about the specific post.
"""

import sys
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
np.set_printoptions(precision=5, suppress=True)


def to_u(p):
    return np.sqrt(p)            # simplex -> positive orthant of the unit sphere (Fisher-Rao isometry)


def ang(u, v):
    return np.degrees(np.arccos(np.clip(u @ v, -1, 1)))


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    p1 = np.array([0.50, 0.30, 0.20])
    p2 = np.array([0.30, 0.45, 0.25])
    log("  two priors (as categorical distributions / points on the Fisher-Rao 2-sphere):")
    log("    p1 = %s   p2 = %s" % (p1, p2))
    log("    u1 = sqrt(p1) = %s   u2 = sqrt(p2) = %s   (unit vectors)" % (to_u(p1), to_u(p2)))
    log("    angular step p1->p2 on the sphere: %.3f deg" % ang(to_u(p1), to_u(p2)))
    log("")

    # alpha = 0 : great-circle (Levi-Civita) extrapolation, constant angular speed
    u1, u2 = to_u(p1), to_u(p2)
    th = np.arccos(np.clip(u1 @ u2, -1, 1))
    w = (u2 - u1 * np.cos(th)) / np.sin(th)          # unit tangent at u1 toward u2
    u3_FR = u1 * np.cos(2 * th) + w * np.sin(2 * th)  # continue one more step
    p3_FR = u3_FR ** 2

    # alpha = -1 : mixture geodesic, straight in p (extrapolate t=2)
    p3_m = 2 * p2 - p1

    # alpha = +1 : exponential geodesic, straight in log p (extrapolate t=2): p ~ p2^2 / p1
    raw = p2 ** 2 / p1
    p3_e = raw / raw.sum()

    log("================  three 'geodesic' predictions of the NEXT position from the SAME p1,p2  =====")
    log("  alpha= 0  great circle (Levi-Civita/Fisher-Rao):  p3 = %s" % p3_FR)
    log("  alpha=-1  mixture (straight in p):                 p3 = %s" % p3_m)
    log("  alpha=+1  exponential (straight in log p):         p3 = %s" % p3_e)
    log("")
    log("  pairwise angular separation of the predictions on the sphere (u=sqrt p):")
    log("    great-circle  vs  mixture     : %.3f deg" % ang(u3_FR, to_u(np.clip(p3_m, 1e-12, None))))
    log("    great-circle  vs  exponential : %.3f deg" % ang(u3_FR, to_u(p3_e)))
    log("    mixture       vs  exponential : %.3f deg" % ang(to_u(np.clip(p3_m, 1e-12, None)), to_u(p3_e)))
    log("")
    log("================  WHAT THIS SHOWS  ================")
    log("Same two priors, THREE different 'next positions' -- one per natural connection.  'Geodesic'")
    log("on a statistical manifold is connection-dependent: the great circle is only the alpha=0")
    log("(Levi-Civita/metric) member of Amari's alpha-family; the dually-flat e (+1) and m (-1)")
    log("geodesics -- the natural straight lines for exponential-family drift and for Bayesian/mixture")
    log("dynamics -- are DIFFERENT curves.  Two points fix none of this; choosing the great circle is")
    log("an (often unstated) assumption that the motion is free-kinetic, not inferential.")
    log("")
    log("(Separately, on the PHYSICS side: a geodesic on S^2 is a great circle = force-FREE constrained")
    log("motion.  Generic 'spherical motion' is NON-geodesic -- a spherical pendulum precesses, a")
    log("conical pendulum / central-force orbit runs on a small (latitude) circle, a charged particle")
    log("in a field follows neither.  Geodesic <=> no tangential force; that is a strong claim two")
    log("positions cannot certify.  With >=3 positions one could TEST it: great-circleness, constant")
    log("speed, and purely-normal acceleration are all checkable; with 2 they are assumed.)")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "sphere_geodesic_connections.md"
    header = [
        "# 'Are we sure it is geodesic?' -- geodesic is connection-dependent on a Fisher-Rao sphere",
        "",
        "**Script:** `empirical/verify_sphere_geodesic_connections.py`",
        "**Context:** assessing a physics.SE question (predict spherical motion from two points) info-geometrically.",
        "**Finding:** same two priors -> three different 'geodesic' predictions (Amari alpha = 0, -1, +1);",
        "the great circle is only the metric (alpha=0) one.  Plus the physics point: generic spherical",
        "motion is non-geodesic (forces).  Two points cannot certify geodesy.",
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
