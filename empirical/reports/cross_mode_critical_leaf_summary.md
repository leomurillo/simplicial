# Cross-Mode Critical-Leaf Summary

- JSON artifact: `C:\Projects\simplicial\empirical\reports\cross_mode_critical_leaf_summary.json`
- Quotient columns are normalizer orbit quotients on the selected leaf; H4->H3 is a support-level orbit cokernel, not a full higher-current rank quotient.

| mode | algebra | selected leaf | balanced leakage | support/KCH leakage | full-block status | full-block deficit | residual/atom | nu_E residual | C2 orbit vol | residual orbit support | orbit residual mass | H3 orbits | H4 orbits | H4->H3 cokernel | reading |
|---|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| neural | weekdays / llama31_8b | `full_nontrivial` | 0.000000 | 0.000000 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | centroid projection; no Ext_CH full-block complex |
| neural | months / llama31_8b | `conductor_3` | 0.000000 | 0.000000 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | centroid projection; no Ext_CH full-block complex |
| neural | weekdays / mistral_7b | `full_nontrivial` | 0.000000 | 0.000000 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | centroid projection; no Ext_CH full-block complex |
| local_atlas | F_4[u]/(u^2) | `u^2` | 0.000000 | 0.000000 | residual | 1.000000 | 1.000000 | 0.015625 | 1552 | 26 | 0.016753 | 2 | 9 | 0 | support closes but full-block residual survives |
| local_atlas | F_2[u]/(u^2) | `u+u^2` | 0.000000 | 0.000000 | residual | 1.000000 | 1.000000 | 0.065574 | 31 | 2 | 0.064516 | 1 | 4 | 0 | support closes but full-block residual survives |
| local_atlas | F_2[u]/(u^3) | `u^2+u^3` | 0.000000 | 0.000000 | residual | 1.000000 | 1.000000 | 0.032787 | 136 | 6 | 0.044118 | 1 | 8 | 0 | support closes but full-block residual survives |
| local_atlas | F_2[u]/(u^4) | `u^3+u^4` | 0.000000 | 0.000000 | residual | 1.000000 | 1.000000 | 0.016393 | 612 | 20 | 0.032680 | 1 | 16 | 0 | support closes but full-block residual survives |
| local_atlas | F_2[u]/(u^5) | `u^4+u^5` | 0.000000 | 0.000000 | residual | 1.000000 | 1.000000 | 0.008197 | 2544 | 48 | 0.018868 | 1 | 28 | 0 | support closes but full-block residual survives |
| local_atlas | F_8[u]/(u^2) | `u^2` | 0.000000 | 0.000000 | modular_residual | 1.000000 | 1.000000 | 0.001953 | 76480 | 152 | 0.001987 | 4 | 53 | 0 | support closes but modular full-block residual survives |

## Reading

The neural rows identify non-flat conductor leaves with zero KCH outside budget in the cyclic proxy. The local rows identify support-closed leaves, but the per-leaf full-block audit shows that the filtered residual is still not killed on the exact rows that were small enough to run. The C2-volume and orbit-quotient residual masses decay along the F2 suffix tower while the relative full-block deficit remains 1.0; the H4-to-H3 support orbit cokernel vanishes on the selected local rows. The closure gap is now a quotient-level saturation question rather than a support-closure question.
Rows marked `modular_residual` are finite-field full-block reductions from `streaming_modular_residual`; they are residual evidence, not rational closure proofs.
