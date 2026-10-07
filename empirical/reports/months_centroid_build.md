# Month C12 Centroid Build Report

## Status

No probability dump was supplied.  The script only wrote the prompt manifest.

## Token Bins

These are exact next-token strings expected in the dump unless the dump already provides label probabilities.

- January: `January`, ` January`
- February: `February`, ` February`
- March: `March`, ` March`
- April: `April`, ` April`
- May: `May`, ` May`
- June: `June`, ` June`
- July: `July`, ` July`
- August: `August`, ` August`
- September: `September`, ` September`
- October: `October`, ` October`
- November: `November`, ` November`
- December: `December`, ` December`

## Prompt Manifest

Wrote `empirical\data\months_probe_manifest.json`.

## Next Command

```powershell
C:\Users\leomu\.local\bin\python.exe empirical\compute_cyclic_K_CH.py --preset months --centroids-json <centroids.json>
```
