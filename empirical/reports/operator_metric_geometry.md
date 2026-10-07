# Front (a): the Hilbert-Polya operator lives in the additive/Kubo-Mori geometry

**Script:** `empirical/verify_operator_metric_geometry.py`
**Context:** front (a); resolves the HPo Bures-curvature obstruction via T24's Kubo-Mori metric.
**Finding:** zeros = 1/y Herglotz curvature currents in the additive/log geometry; finite (blind)
in the quadratic Bures/FS geometry.  The operator must use the additive (Kubo-Mori) inner product.
**Nature:** numerical (mpmath), labelled.  NOT a proof (self-adjointness in KM = RH).

```text
Front (a), the new lever: the Hilbert-Polya operator must live in the ADDITIVE (Kubo-Mori)
geometry, where the zeros are curvature currents -- NOT the quadratic (Bures) geometry, which is
provably BLIND to them.

Cross-referencing two corpus findings:
  * HPo-notes Addendum C (the "Bures-curvature obstruction"): the Bures/Fubini-Study curvature
    kappa = |M'|^2/(1+|M|^2)^2  (M = L_chi3 / Xi) is FINITE at the Xi-zeros -- it cannot be the
    zero-detecting current; the Herglotz positivity must come from a separate input.
  * T24 (Chentsov-Petz monotone-metric fork): the ADDITIVE / dually-flat monotone metric is
    KUBO-MORI (Hessian of relative entropy), NOT Bures (SLD). The HPo program used Bures throughout.

The resolution (the lever): the zeros DO appear as singular curvature -- in the LOG / ADDITIVE
geometry, which is the Kubo-Mori side and the geometry in which the Weil explicit formula is
additive over places.  Concretely:
  * additive / log-derivative (Kubo-Mori-type):  m_B(z) = -Xi'/Xi = -d/dz log Xi.  At a simple
    zero rho=gamma (real), Xi(gamma+iy) ~ Xi'(gamma)(iy), so Im m_B(gamma+iy) ~ 1/y -> +infinity:
    a HERGLOTZ POLE = the zero as a curvature current (Delta log|Xi| = 2*pi*sum delta_zeros).
  * quadratic / Bures-Fubini-Study:  kappa = |M'|^2/(1+|M|^2)^2 stays FINITE at the same zero
    (M has a pole there, but the FS metric of a meromorphic function is bounded -- S^2 is smooth).

So the operator H = N_inf (UPT Bargmann-Fock number operator) + V_arith with V_arith = m_B must
be assembled in the additive/Kubo-Mori inner product; in it the spectrum {gamma_n} is the singular
support of the curvature.  Bures (the metric the HPo notes used) smooths the zeros away -- that is
why the smooth-Bures routes (Addendum C/G) stalled.

This probe verifies the contrast at gamma_1, gamma_2: Im m_B(gamma+iy) ~ 1/y (additive: pole) vs
kappa_EO(gamma) finite (quadratic: blind).  NUMERICAL (mpmath), labelled.  NOT a proof; it
identifies the correct geometry for the operator and explains the HPo Bures obstruction as a
wrong-metric artifact.

================  zero gamma_1 = 14.1347251417  ================
  ADDITIVE (log-derivative m_B = -Xi'/Xi):  Im m_B(gamma+iy) should ~ 1/y (Herglotz pole)
      y         Im m_B(gamma+iy)      (1/y for reference)
    0.1    10.006768      10.0
    0.05    20.003384      20.0
    0.02    50.001354      50.0
    0.01    100.00068      100.0
    0.005    200.00034      200.0
    -> Im m_B ~ 1/y: the zero is a CURVATURE CURRENT in the additive/log geometry.

  QUADRATIC (Bures/Fubini-Study kappa = |M'|^2/(1+|M|^2)^2, M = L_chi3/Xi):
    residue of M at gamma: A = L3/Xi' = (-1799.27 + 1073.25j)
    kappa(gamma) = 1/|A|^2 = 2.2782962e-7   (FINITE -- the quadratic metric is BLIND to the zero)
      kappa(gamma+0.05) = 2.1910814e-7
      kappa(gamma+0.01) = 2.2579826e-7
      kappa(gamma+0.002) = 2.2741166e-7
    -> kappa stays bounded at the zero: Bures/FS curvature does NOT see it.

================  zero gamma_2 = 21.0220396388  ================
  ADDITIVE (log-derivative m_B = -Xi'/Xi):  Im m_B(gamma+iy) should ~ 1/y (Herglotz pole)
      y         Im m_B(gamma+iy)      (1/y for reference)
    0.1    10.013884      10.0
    0.05    20.006944      20.0
    0.02    50.002778      50.0
    0.01    100.00139      100.0
    0.005    200.00069      200.0
    -> Im m_B ~ 1/y: the zero is a CURVATURE CURRENT in the additive/log geometry.

  QUADRATIC (Bures/Fubini-Study kappa = |M'|^2/(1+|M|^2)^2, M = L_chi3/Xi):
    residue of M at gamma: A = L3/Xi' = (-1016.06 + 78993.1j)
    kappa(gamma) = 1/|A|^2 = 1.6023218e-10   (FINITE -- the quadratic metric is BLIND to the zero)
      kappa(gamma+0.05) = 9.6338361e-11
      kappa(gamma+0.01) = 1.4445771e-10
      kappa(gamma+0.002) = 1.5693329e-10
    -> kappa stays bounded at the zero: Bures/FS curvature does NOT see it.

================  WHAT THIS IS  ================
CONFIRMED: at the zeros, the ADDITIVE log-derivative m_B = -Xi'/Xi has a 1/y Herglotz pole
(the zero as a curvature current; Delta log|Xi| = 2*pi*sum delta_zeros, Poisson-Jensen),
while the QUADRATIC Bures/Fubini-Study curvature kappa stays FINITE (the HPo Addendum-C
obstruction, reproduced).  The two geometries disagree exactly AT the spectrum.

LEVER for front (a): the Hilbert-Polya operator H = N_inf + V_arith (N_inf = UPT Bargmann-Fock
number operator; V_arith = m_B = -Xi'/Xi) must be built in the ADDITIVE / KUBO-MORI geometry
-- the dually-flat metric T24 singles out, the one in which the Weil explicit formula is
additive over places and the zeros ARE the curvature singular-support.  The HPo program's
Bures (SLD) metric is the WRONG, zero-blind choice; its smooth-Bures routes (Addendum C/G)
stalled for exactly this reason.  NOT a proof: self-adjointness of H in the Kubo-Mori
geometry is still RH -- but the geometry is now the correct (additive) one, with the zeros
manifest as curvature currents rather than smoothed away.
```
