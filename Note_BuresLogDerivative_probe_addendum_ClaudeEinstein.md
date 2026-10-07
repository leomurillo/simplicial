# Addendum: Corrected Probe for the Bures Log-Derivative Object

The primary note is `Note_BuresLogDerivative_mN4pR.md`.

The executable probe to use is:

```powershell
python empirical\probe_BuresLogDerivative_vK8sT.py
```

The earlier `probe_BuresLogDerivative_mN4pR.py` printed the main identity and
sample diagnostics correctly, but its grid scan evaluated the formula for
`xi(s)` at the removable point `s=0`, where mpmath sees the gamma pole before
the `s(s-1)` cancellation. Per the no-edit rule, that file is left untouched
and this corrected probe avoids the removable singularity in the scan.
