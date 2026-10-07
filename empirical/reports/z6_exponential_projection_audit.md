# Z6 Exponential Projection Audit

- Claim tested: Z6 exponential projection sector purity, interior spillover, and dyadic-boundary vanishing
- Status: KILL
- max tangent mixed ratio: 8.213274e-01
- interior K_CH mixed ratio: 4.010842e-01
- dyadic-boundary K_CH mixed ratio: 4.418255e-01
- kills: ['D eta has mixed-sector leakage; base map is not V2+V3 sector-pure', 'dyadic-boundary K_CH mixed spillover does not vanish']

## Interpretation

A PASS would support the exponential protocol as a sector-pure base map
with interior ternary spillover and dyadic-boundary shutoff. A KILL means
one of those advertised properties is false for the tested convention.
This audit does not evaluate Cotton-York matching or E6 variational
closure.
