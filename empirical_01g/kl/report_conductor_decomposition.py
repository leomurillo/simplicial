"""Generate the human-readable report from the probe and verifier outputs."""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
OUT=HERE/'conductor_results'


def main():
    data=json.loads((OUT/'results.json').read_text())
    verification=json.loads((OUT/'verification.json').read_text())
    assert verification['all_checks_passed']
    rows=[d['metrics'] for d in data['details']]
    endpoint=[r for r in rows if r['family']=='kl_fixed' and r['gamma']==1]
    saved=[r for r in rows if r['family']=='kl_saved']
    syr={r['k']:r for r in rows if r['family']=='syracuse'}
    last=max(endpoint,key=lambda r:r['k'])
    k=last['k']
    late=[d for d in data['details'] if d['metrics']['k']==k and
          (d['metrics']['family'] in ('syracuse','kl_saved') or d['metrics']['gamma']==1)]
    text=[r'''# T8 and the prime crystal: conductor decomposition of Collatz vectors

Date: 2026-10-17. Status: reproducible finite numerical exploration, with exact rational checks at small levels. This report does not establish the comparison conjecture, an asymptotic estimate, or Collatz convergence.

## Outcome

The multiplicative character decomposition identifies the top-digit discrepancy exactly with the conductor-3^k block. On the tested vectors, an L1 bound on this block is strong enough to imply the desired comparison with Syracuse lift loss. The corresponding unweighted L2 bound fails at the gamma=1 endpoint on the higher tested levels. Spatial concentration explains why a second-moment estimate discards too much information.

## Definitions and exact identities

Use k for residue depth, not the number of primes in the crystal. On U_k=(Z/3^k Z)^*, normalize each positive vector v to f=v/E(v), where E is uniform over units. E_{k-1} averages the three lifts of each coarse unit. Set h=f-E_{k-1}f. All norms below use this uniform measure.

Since 2 generates U_k, use characters chi_t(2^j)=exp(2*pi*i*t*j/(2*3^(k-1))). An FFT in this order computes the multiplicative Fourier transform. Characters of conductor 3^k have t not divisible by 3. Hence

\[
\|h\|_2^2=\sum_{\operatorname{cond}(\chi)=3^k}|\widehat f(\chi)|^2.
\]

For the T8 centered apex, these coefficients are D_v(1,chi)/D_v(1,chi_0). This uses the actual vector v as the positive ledger, not its logarithm in place of v.

Write ell(v)=1-rho(v), where rho is the average minimum of the normalized lift triples. On a zero-sum triple h, let m=-min(h), and P be the total positive mass. Then m<=P<=2m and sum|h|=2P. Averaging gives the two-sided estimate

\[
\boxed{\tfrac34\|h\|_1\le\ell(v)\le\tfrac32\|h\|_1.}
\]

Also, the other two coordinates sum to m, so their squared sum is at least m^2/2. Therefore m^2 <= (2/3) sum h_i^2. Averaging and Jensen give

\[
\boxed{\ell(v)\le\sqrt2\,\|h\|_2.}
\]

These are elementary inequalities for all positive vectors, independent of any Collatz conjecture. The two-sided L1 estimate means that L1 control is equivalent to lift-loss control up to universal constants; the character representation does not by itself solve the obstruction.

## Inputs and reconstruction

- Syracuse laws are generated deterministically by the geometric circular-convolution recurrence with P(a)=2^(-a). There is no Monte Carlo sampling.
- The six existing kl_cert_k9.npy through kl_cert_k14.npy files store only c(r) for r=2 mod 3, at distinct certified exponents. They are not full vectors, and they are not exactly critical-exponent vectors.
- For r=1 mod 3, reconstruct c(r)=2^(-gamma)c(2r)/lambda, using the recorded one-step eigenvalue lambda, not 2^gamma. Set c=0 on multiples of 3. Check the full nonlinear eigen-equation afterwards.
- Fresh fixed-exponent runs use gamma=0.5,0.8,0.9,1 for k=2..10, plus gamma=1 for k=11..14. Stopping checks relative vector convergence and the final operator residual, rather than eigenvalue stabilization alone.
- Input certificate hashes and the analysis-script hash are recorded. Existing certificates and manuscripts were not modified.

## Fixed exponent gamma=1: direct comparison

Here ell(mu_k) is the Syracuse lift loss. Each ratio below is divided by ell(mu_k). A bound ratio below one suffices for the desired finite-level comparison. This is the endpoint of the proposed exponent interval, but these computations do not prove monotonicity in gamma or cover the continuum of exponents.

| k | Syracuse loss | KL loss | actual ratio | (3/2)L1 ratio | sqrt(2)L2 ratio |
|---:|---:|---:|---:|---:|---:|
''']
    for r in endpoint:
        text.append(f"| {r['k']} | {syr[r['k']]['lift_loss']:.6f} | {r['lift_loss']:.6f} | {r['loss_over_syracuse_loss']:.4f} | {r['l1_bound_over_syracuse_loss']:.4f} | {r['l2_bound_over_syracuse_loss']:.4f} |\n")
    text.append('\n## Saved certificates: varying exponents\n\nThese rows must not be read as a fixed-gamma sequence.\n\n| k | gamma | KL loss | L1 | L2 | (3/2)L1 / Syracuse loss |\n|---:|---:|---:|---:|---:|---:|\n')
    for r in saved:
        text.append(f"| {r['k']} | {r['gamma']:.4f} | {r['lift_loss']:.6f} | {r['l1']:.6f} | {r['l2']:.6f} | {r['l1_bound_over_syracuse_loss']:.4f} |\n")
    text.append(f'\n## Spatial and spectral concentration at k={k}\n\nSpatial percentages refer to coarse lift triples, ranked separately for each quantity. Spectral percentages refer to individual conductor-3^k character modes; conjugate modes are counted separately.\n\n| family | gamma | L1 | L2 | contexts carrying 90% of L1 | contexts carrying 90% of energy | energy in top 1% of contexts | energy in top 1% of modes |\n|---|---:|---:|---:|---:|---:|---:|---:|\n')
    for d in late:
        r=d['metrics']
        gamma='--' if r['gamma'] is None else str(r['gamma'])
        text.append(f"| {r['family']} | {gamma} | {r['l1']:.6f} | {r['l2']:.6f} | {100*r['l1_fraction90']:.2f}% | {100*r['energy_fraction90']:.2f}% | {100*r['energy_top1pct_share']:.2f}% | {100*r['spectral_top1pct_share']:.2f}% |\n")
    text.append('\nConcentration in residue space is much stronger than concentration in a few individual character modes. The Syracuse top-block L2 norm stays near 0.56 over the tested range, while its L1 norm falls. This is a finite-range observation, not a claim about limiting rates. A sparse-mode truncation cannot be justified simply from these spectra.\n\nThe depth decomposition uses d=v_3(j+1) for the coarse representative j; the last bin means d>=k-1. It includes all unit contexts, so d=0 is included. This is not the same weighting as the odd-row gain/occupation distributions in Section 12.14.\n\n| family | loss share at depth <=2 | L1 share at depth <=2 | energy share at depth <=2 |\n|---|---:|---:|---:|\n')
    for d in late:
        selected=[s for s in d['spatial_depth'] if s['depth']<=2]
        text.append(f"| {d['metrics']['family']} | {100*sum(s['loss_share'] for s in selected):.2f}% | {100*sum(s['l1_share'] for s in selected):.2f}% | {100*sum(s['energy_share'] for s in selected):.2f}% |\n")
    text.append(r'''
## What this suggests proving next

The direct sufficient inequality is

\[
\tfrac32\|(I-E_{k-1})f_{k,\gamma}\|_1\le\ell(\mu_k).
\]

It holds on every tested KL vector. For the manuscript's weaker asymptotic target, a fixed polynomial factor in k on the right would suffice, assuming its stated Syracuse mixing input. The unproved work is to control the nonlinear minimum operator uniformly in k and in the required gamma interval.

A practical proof decomposition is to split the L1 contribution into shallow and deep residue contexts. Establish a comparison on bounded depths and a tail estimate for the remaining absolute discrepancy. The measured small deep-context L1 contribution makes this plausible, but the present numbers do not prove a uniform tail bound or control adversarial occupations.

Do not replace the sum of absolute values by a global Cauchy-Schwarz estimate unless the resulting bound remains below the comparison target: the tables show that it does not at gamma=1 for higher tested k. Nor does failure of this particular L2 bound rule out weighted, local, or truncated L2 estimates.

The conductor energy, norm inequalities, and residue-depth profiles provide a concrete interface between T8 and the prime-crystal program. What is still missing is an estimate, not another change of basis.

## Verification and limits

''')
    text.append(f"- {len(rows)} vectors analyzed; all internal checks passed.\n")
    text.append(f"- Maximum relative Parseval discrepancy: {max(r['parseval_relative_error'] for r in rows):.3e}.\n")
    text.append(f"- Maximum full-operator absolute eigenvalue residual across saved reconstructions: {max(r['operator_residual'] for r in saved):.3e}. This reflects the original approximate eigenvectors and is not an interval enclosure.\n")
    text.append(f"- Maximum full-operator residual across fresh fixed-exponent runs: {max(r['operator_residual'] for r in rows if r['family']=='kl_fixed'):.3e}.\n")
    text.append('- Direct character summation and inverse projection checked independently of FFT formulas for k<=5.\n- Exact Fraction arithmetic checks at k=2..6 verify Syracuse norms, both norm bounds, and agreement with the floating recurrence.\n- The deficit identity, full Parseval sum, conductor-block sizes, probability normalization, projective consistency, and input hashes were checked.\n- All large-level Fourier values are float64 exploratory results; finite checks cannot establish uniformity, asymptotics, or the comparison conjecture.\n')
    text.append(r'''
## Reproduce and inspect

From the repository root, with Python, NumPy, and SciPy:

```powershell
python empirical_01g/kl/conductor_decomposition.py
python empirical_01g/kl/verify_conductor_decomposition.py
python empirical_01g/kl/report_conductor_decomposition.py
```

- [Full results and depth profiles](results.json)
- [Metrics table](metrics.csv)
- [Every conductor block](conductor_blocks.csv)
- [Independent verification](verification.json)
- [Analysis source](../conductor_decomposition.py)
- [Verifier source](../verify_conductor_decomposition.py)

Source manuscripts: 01g.simplicial_prime_crystal.md, Sections 12.8 and 12.14; T8-MultiplicativeApexDirichletPolynomials-Draft1.md, Sections 1.3, 1.4, and 2.3. The character-block identity and inequalities above are derived explicitly here; no new external analytic-number-theory theorem is assumed for the computations.
''')
    (OUT/'report.md').write_text(''.join(text),encoding='utf-8')
    print(OUT/'report.md')


if __name__=='__main__':
    main()
