# 'Are we sure it is geodesic?' -- geodesic is connection-dependent on a Fisher-Rao sphere

**Script:** `empirical/verify_sphere_geodesic_connections.py`
**Context:** assessing a physics.SE question (predict spherical motion from two points) info-geometrically.
**Finding:** same two priors -> three different 'geodesic' predictions (Amari alpha = 0, -1, +1);
the great circle is only the metric (alpha=0) one.  Plus the physics point: generic spherical
motion is non-geodesic (forces).  Two points cannot certify geodesy.
**Nature:** numerical (numpy), conceptual demonstration.

```text
'Are we sure it is geodesic?' -- on a statistical (Fisher-Rao) sphere, GEODESIC is not one curve.

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

  two priors (as categorical distributions / points on the Fisher-Rao 2-sphere):
    p1 = [0.5 0.3 0.2]   p2 = [0.3  0.45 0.25]
    u1 = sqrt(p1) = [0.70711 0.54772 0.44721]   u2 = sqrt(p2) = [0.54772 0.67082 0.5    ]   (unit vectors)
    angular step p1->p2 on the sphere: 11.950 deg

================  three 'geodesic' predictions of the NEXT position from the SAME p1,p2  =====
  alpha= 0  great circle (Levi-Civita/Fisher-Rao):  p3 = [0.13293 0.58498 0.28208]
  alpha=-1  mixture (straight in p):                 p3 = [0.1 0.6 0.3]
  alpha=+1  exponential (straight in log p):         p3 = [0.15418 0.57816 0.26767]

  pairwise angular separation of the predictions on the sphere (u=sqrt p):
    great-circle  vs  mixture     : 2.983 deg
    great-circle  vs  exponential : 1.808 deg
    mixture       vs  exponential : 4.783 deg

================  WHAT THIS SHOWS  ================
Same two priors, THREE different 'next positions' -- one per natural connection.  'Geodesic'
on a statistical manifold is connection-dependent: the great circle is only the alpha=0
(Levi-Civita/metric) member of Amari's alpha-family; the dually-flat e (+1) and m (-1)
geodesics -- the natural straight lines for exponential-family drift and for Bayesian/mixture
dynamics -- are DIFFERENT curves.  Two points fix none of this; choosing the great circle is
an (often unstated) assumption that the motion is free-kinetic, not inferential.

(Separately, on the PHYSICS side: a geodesic on S^2 is a great circle = force-FREE constrained
motion.  Generic 'spherical motion' is NON-geodesic -- a spherical pendulum precesses, a
conical pendulum / central-force orbit runs on a small (latitude) circle, a charged particle
in a field follows neither.  Geodesic <=> no tangential force; that is a strong claim two
positions cannot certify.  With >=3 positions one could TEST it: great-circleness, constant
speed, and purely-normal acceleration are all checkable; with 2 they are assumed.)
```
