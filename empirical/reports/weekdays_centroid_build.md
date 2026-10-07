# Weekday Centroid Build Report

## Status

No probability dump was supplied.  The script only wrote the prompt manifest.

## Token Bins

These are exact next-token strings expected in the dump unless the dump already provides `weekday_probs`.

- Monday: `Monday`, ` Monday`
- Tuesday: `Tuesday`, ` Tuesday`
- Wednesday: `Wednesday`, ` Wednesday`
- Thursday: `Thursday`, ` Thursday`
- Friday: `Friday`, ` Friday`
- Saturday: `Saturday`, ` Saturday`
- Sunday: `Sunday`, ` Sunday`

## Prompt Manifest

Wrote `empirical\data\weekdays_probe_manifest.json`.

## Next Command

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\compute_weekdays_K_CH.py --centroids-json empirical\data\weekdays_llama31_8b_centroids_7bin.json --report empirical\reports\weekdays_llama31_8b_K_CH.md --json empirical\reports\weekdays_llama31_8b_K_CH.json
```
