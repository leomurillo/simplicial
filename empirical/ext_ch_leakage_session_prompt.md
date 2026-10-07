# Session Prompt: Run the Ext_CH Leakage Extractor

We have a reusable extractor for the mixed tame/wild row:

```powershell
python empirical/compute_ext_ch_leakage.py `
  --grid-json path\to\f4_u2_logits_grid.json `
  --report empirical\reports\f4_u2_ext_ch_leakage.md `
  --json-out empirical\reports\f4_u2_ext_ch_leakage.json
```

Expected input JSON:

```json
{
  "logits_grid": [
    [[16 target logits at s0,r0], [16 target logits at s0,r1]],
    [[16 target logits at s1,r0], [16 target logits at s1,r1]]
  ]
}
```

`probs_grid` with the same shape is also accepted.  The last axis must be in
the default label order

```text
(0,0), (0,1), (0,w), (0,w+1),
(1,0), (1,1), (1,w), (1,w+1),
(w,0), (w,1), (w,w), (w,w+1),
(w+1,0), (w+1,1), (w+1,w), (w+1,w+1)
```

The script reports:

1. the pure-tame negative control: tame-axis/tame-input output into wild
   character rows should be small;
2. raw mixed cubic wild leakage;
3. the mixed composition defect
   \(K(\alpha)K(\beta)-K(\alpha+\beta)\) after the 2D finite difference;
4. top defect entries with character labels.

Interpretation guardrail: do not expect a strictly tame ray to leak into wild.
The theory says pure tame is closed.  The Ext_CH signal is the mixed
tame/wild finite difference after pure-axis subtraction.
