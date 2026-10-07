# Z6 Sector-Projected Gaussian Audit

- Claim tested: sector-projected Gaussian protocol sector purity, interior spillover, boundary shutoff
- Status: KILL
- max tangent mixed ratio: 1.618432e-01
- interior K_CH mixed ratio: 9.898073e-01
- boundary K_CH mixed ratio: 5.000001e-01
- boundary broken-edge probability mass: 3.166661e-07
- kills: ['D eta has mixed-sector leakage; base map is not V2+V3 sector-pure', 'boundary K_CH mixed spillover does not vanish']

## Interpretation

This audit checks the corrected Gaussian protocol rather than assuming it
works. A KILL on tangent mixed ratio means the normalized exponential map
still creates mixed-sector tangent components despite pure-sector logits.
