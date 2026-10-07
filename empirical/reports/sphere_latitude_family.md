# Two points on a sphere -> a one-parameter family of latitudes; the great circle is one member

**Script:** `empirical/verify_sphere_latitude_family.py`
**Context:** the actual physics.SE question (predict r(t+2) on a sphere from two points).
**Finding:** r(t+2) is undetermined across a wide arc; great circle = the unique geodesic (force-free);
any other latitude needs a tangential force; 'most likely' needs a PRIOR (Bayes), not least action.
**Nature:** numerical (numpy), conceptual demonstration.

```text
The physics.SE question, made concrete: two points on a sphere -> a ONE-PARAMETER FAMILY of
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

  observed:  r(t)=p1=[0.9759 0.1952 0.0976]   r(t+1)=p2=[0.8071 0.5549 0.2018]   step=23.70 deg

================  the family of predictions p3(a) as the axis (latitude) sweeps  ============
   axis angle psi   latitude(a.p1)   rotation phi(deg)    predicted r(t+2) = p3
       0.0         +0.039             23.7         [0.5019 0.8189 0.2783]  <- GREAT CIRCLE (geodesic)
      13.8         -0.196             24.2         [0.5042 0.8297 0.2395]
      27.7         -0.420             26.2         [0.5094 0.8379 0.1961]
      41.5         -0.619             30.3         [0.5199 0.8424 0.1419]
      55.4         -0.782             38.5         [0.5425 0.8375 0.0645]
      69.2         -0.900             56.3         [ 0.603   0.7954 -0.0613]
      83.1         -0.966            105.2         [ 0.8078  0.5512 -0.209 ]
      96.9         -0.976           -138.1         [0.9025 0.1984 0.3823]
     110.8         -0.928            -67.1         [0.619  0.5437 0.5668]
     124.6         -0.827            -42.9         [0.5386 0.6918 0.4809]
     138.5         -0.678            -32.4         [0.5142 0.7526 0.4112]
     152.3         -0.489            -27.2         [0.5052 0.7846 0.3593]
     166.2         -0.272            -24.6         [0.502  0.8047 0.3168]

  SPREAD of the prediction family: 47.3 deg  (two points leave r(t+2) this undetermined).
  great-circle (geodesic, force-free) prediction:        p3 = [0.5021 0.8209 0.2719]
  rotation-invariant 'max-entropy prior' mean prediction: p3 = [0.6108 0.7494 0.2555]  (NOT the great circle:
    7.5 deg away) -- a coherent 'most likely' answer, but the PRIOR is doing the work.

================  WHAT THIS SHOWS (answering the post)  ================
1. OPTIMAL prediction? -- CONDITIONAL on a model, not unconditional.  Two points + constant
   angular speed leave a whole great circle of axes (latitudes); r(t+2) is undetermined by
   47 deg.  There is no model-free 'optimal'.
2. Is the great circle NECESSARY? -- It is the UNIQUE geodesic = force-FREE motion (angular
   momentum conserved).  It is necessary iff there is no tangential force.  Every other
   latitude needs a specific tangential (toward-a-pole) force = a specific potential.  So
   'great circle' is selected by the PHYSICS assumption (no tangential force), not by the data.
3. If NOT the great circle? -- then a tangential force/potential fixes the latitude, and you
   must know it; the two points alone cannot.  Absent it, only a Bayesian estimate under a
   PRIOR over axes is possible (e.g. the max-entropy mean above) -- which is exactly the OP's
   'not greatest, not shortest' answer, made rigorous.  BUT: this is BAYES, not least action.

THE CATCH ON 'use least action (LA) to pick the most likely latitude': least action chooses
the PATH within a FIXED Lagrangian; it cannot choose AMONG Lagrangians/latitudes (Vavrik's
comment).  With the free Lagrangian it returns the great circle (the SHORTEST) -- contradicting
the OP's 'not the shortest'.  To land on a small circle one must put in a potential, OR replace
'least action' with an explicit PRIOR over axes (Bayesian model selection).  The honest move:
state the prior (= the unstated physics).  Info-geometry: 'most likely' and 'geodesic' both
depend on a choice (prior / connection) NOT in the data; they collapse to one answer only at
the symmetric (force-free / max-entropy) corner.
```
