# Z6 Area-Gated Copula Audit

- Claim tested: area-gated copula: pure independent base, controlled mixed interior, theta boundary shutoff
- Status: PASS
- max base tangent mixed ratio: 1.977731e-01
- max base e-tangent mixed ratio: 1.359740e-10
- max copula tangent mixed ratio: 4.447776e-01
- interior theta: 7.455577e-01
- boundary theta: 0.000000e+00
- interior copula K_CH mixed ratio: 8.774517e-01
- boundary copula K_CH mixed ratio: 9.248701e-01
- boundary base K_CH mixed ratio: 9.248701e-01
- kills: []

## Interpretation

This audit separates e-coordinate base purity from m-coordinate curvature
and controlled physical copula mixing. A PASS does not yet prove
Cotton-York matching or E6 variational closure;
it only establishes that the area gate controls the mixed dependence in
the advertised finite tests.
