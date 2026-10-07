# B6 Tool Use Versus Internal Compression Probe

- timestamp: `2026-06-03T20:33:12.458519+00:00`
- seed: `20260603`
- trials per kind: `260`
- calibration episodes: `800`
- evidence train/test: `192` / `192`
- lookup keys: `64`
- noise scale: `0.35`
- compression/memory/tool cost: `0.08` / `0.55` / `0.16`
- alpha: `0.05`

## Claim Tested

B6-E1 asks whether an agent should externalize exact high-cardinality lookup
problems instead of absorbing them as internal compression. Tool episodes are
solvable by internal key memory, but only at a high capacity cost. The
capacity-aware boundary should choose externalize.

## Conformal Null Thresholds

| score | threshold |
|---|---|
| alpha | 0.050 |
| scalar | 1.000 |
| retained | 0.008 |
| compression_value | -0.066 |
| key_memory_gain | -0.201 |
| tool_value | -0.151 |
| family_margin | 0.015 |
| fixed_gain | 0.120 |
| fixed_compression_value | 0.080 |
| fixed_memory_gain | 0.450 |
| fixed_tool_value | 0.080 |

## Agent Summary

| agent | routing accuracy | noise false admission | retained success | compress success | tool success | tool as internal compression |
|---|---|---|---|---|---|---|
| scalar | 0.249 | 0.004 | 0.000 | 0.000 | 0.000 | 0.000 |
| compression_only | 0.500 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| naive_internal_memory | 0.500 | 0.000 | 0.000 | 1.000 | 0.000 | 1.000 |
| tool_only | 0.500 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| capacity_boundary | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 0.000 |
| t18_conformal_tool | 0.996 | 0.015 | 1.000 | 1.000 | 1.000 | 0.000 |

## Accuracy by Episode Kind

| kind | true op | scalar | compression only | naive memory | tool only | capacity boundary | T18 conformal tool |
|---|---|---|---|---|---|---|---|
| retained | reweight | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 |
| compress | compress | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 |
| tool | externalize | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 1.000 |
| noise | suppress | 0.996 | 1.000 | 1.000 | 1.000 | 1.000 | 0.985 |

## AUC Checks

| check | AUC |
|---|---|
| scalar_non_noise_vs_noise | 0.492 |
| retained_gain_retained_vs_noise | 1.000 |
| compression_value_compress_vs_noise | 1.000 |
| tool_value_tool_vs_noise | 1.000 |
| key_memory_gain_tool_vs_noise | 1.000 |
| tool_value_tool_vs_compress | 1.000 |
| compression_value_compress_vs_tool | 1.000 |

## Mean Scores by Kind

| kind | scalar | retained | compression value | key memory gain | key memory value | tool value | tool minus memory |
|---|---|---|---|---|---|---|---|
| retained | 1.000 | 0.892 | -0.101 | -0.409 | -0.959 | -0.165 | 0.793 |
| compress | 1.000 | -0.005 | 0.808 | -0.410 | -0.960 | -0.165 | 0.795 |
| tool | 1.000 | -0.006 | -0.099 | 0.789 | 0.239 | 0.722 | 0.483 |
| noise | 1.000 | -0.005 | -0.102 | -0.402 | -0.952 | -0.165 | 0.787 |

## Pass Checks

| check | result |
|---|---|
| scalar_surprise_matched | pass |
| compression_only_fails_tool | pass |
| naive_memory_overcompresses_tool | pass |
| tool_only_fails_compress | pass |
| capacity_boundary_routes_core_cases | pass |
| conformal_routes_tool | pass |
| conformal_false_admission_controlled | pass |

Overall: **PASS**

## Interpretation

This is a pass if scalar surprise stays matched, low-rank compression fails
exact lookup, naive internal key memory over-compresses tool episodes, tool-only
fails genuine compression, and the capacity-aware routers send lookup cases to
externalize while controlling false admissions under the conformal null.

This would falsify the tool-use bucket if internal compression solved exact
lookup as cheaply as tool use, or if tool use and compression collapsed under
matched surprise.
