# (a) the archimedean forcing structure = the Hermite/oscillator limit of the Jensen tower

**Script:** `empirical/verify_jensen_hermite_archimedean.py`
**Context:** continues verify_jensen_turan_peaks; names (a)'s forcing structure; ties GOR-Zagier
Hermite limit to the program's metaplectic-UPT Bargmann-Fock selection (Q8vM3 Lock B).
**Nature:** numerical (mpmath moments + roots), labelled.  GOR-Zagier is the theorem; this exhibits it.

```text
(a) continued: the archimedean forcing structure, on the peaks side, IS the Hermite/oscillator limit.

The peaks-side tower of RH (from verify_jensen_turan_peaks.py):
  * amplitude = moment/Hankel positivity        -- FREE (Phi>0); NOT RH;
  * peaks     = Jensen hyperbolicity (all d, n)  -- the RH content;
  * and the Turan margin is LARGEST at low n, decreasing toward 1 (marginality, peaks-side).

Griffin-Ono-Rolen-Zagier (PNAS 2019) proved: for each degree d, the suitably renormalized
Jensen polynomials J_{d,n} converge to the HERMITE polynomial H_d as n -> infinity; hence each
J_{d,n} is hyperbolic for all n >= N(d).  So the tower has a sharp shape:
  * LARGE n (each degree) is FORCED -> Hermite.  And Hermite polynomials ARE the archimedean
    structure: eigenfunctions of the Fourier transform = harmonic-oscillator / Bargmann-Fock
    number states.  This program already proved (Q8vM3 Lock B, project_metaplectic_selection_UPT)
    that Uniform Place Treatment FORCES Bargmann-Fock at v=infinity.  So the large-n peaks are
    forced by the SAME archimedean oscillator the metaplectic-UPT selects.  (a)'s 'prolate /
    archimedean local positivity' = this oscillator limit.
  * LOW n is the RESIDUAL = the dominant low zeros = the biggest peaks (matches the Turan-margin
    trend).  RH = also the low (pre-asymptotic) head lies in the oscillator's hyperbolic class.

This probe makes the identification concrete and NORMALIZATION-FREE: standardize the roots of
J_{d,n} (mean 0, variance 1) and compare to the standardized Hermite (Gauss-Hermite) nodes.
GOR-Zagier => standardized J_{d,n} roots -> standardized H_d roots, but at a ~1/log n RATE.
We TEST the identification and report what is actually witnessable for n in reach (<= ~30):
  (1) are all tested J_{d,n} hyperbolic (real-rooted)?  -- a check against the proven range;
  (2) how close is each standardized J_{d,n} root-shape to the Hermite/oscillator nodes?
  (3) GATE NOTE: the pre-registered guess "deviation -> 0, monotone, largest at low n" is
      REFUTED by the data (see below); the honest finding replaces it and is retained.

NUMERICAL (mpmath moments + mpmath roots), labelled.  NOT a proof: GOR-Zagier is the theorem
(the limit), here corroborated as 'shape already ~Hermite + all hyperbolic'; the ->0 limit is
~1/log n and is NOT numerically witnessable (it would stay a few % even at n ~ 1e6).

Computing 34 Phi-moments (dps=40, finite bound) ...
  done.  (gamma_n = (-1)^n a_n n!/(2n)! are the Jensen-tower coefficients.)

================  J_{d,n} roots  ->  standardized HERMITE (oscillator) nodes  ========
For each degree d: standardize roots of J_{d,n} (mean 0, var 1) and compare to the
standardized Gauss-Hermite nodes of H_d.  (Limit is Hermite, but at a ~1/log n rate.)

  d=2  low n : n0:3.444e-41  n1:0.0  n2:0.0  n3:3.444e-41  n4:0.0
       high n: n28:6.888e-41  n29:0.0  n30:6.888e-41  n31:0.0
       (d=2 is standardization-trivial: any 2 reals -> +-1 = H_2 exactly; no shape info.)
       non-hyperbolic (complex-root) J_{2,n} among tested: 0   (all hyperbolic)

  d=3  low n : n0:0.01433  n1:0.02108  n2:0.02541  n3:0.02827  n4:0.03019
       high n: n27:0.03163  n28:0.03145  n29:0.03127  n30:0.03108
       std-root deviation from Hermite: min 0.01433, max 0.03393 over n in reach
       => shape is UNIFORMLY ~Hermite (a few %%); it does NOT visibly ->0 (rises then
          plateaus): the GOR-Zagier ->0 limit is ~1/log n, unwitnessable here.
       non-hyperbolic (complex-root) J_{3,n} among tested: 0   (all hyperbolic)

  d=4  low n : n0:0.02592  n1:0.02814  n2:0.02977  n3:0.03095  n4:0.03217
       high n: n26:0.03254  n27:0.03234  n28:0.03214  n29:0.03195
       std-root deviation from Hermite: min 0.02592, max 0.03499 over n in reach
       => shape is UNIFORMLY ~Hermite (a few %%); it does NOT visibly ->0 (rises then
          plateaus): the GOR-Zagier ->0 limit is ~1/log n, unwitnessable here.
       non-hyperbolic (complex-root) J_{4,n} among tested: 0   (all hyperbolic)

  d=5  low n : n0:0.03888  n1:0.04173  n2:0.04469  n3:0.04728  n4:0.04904
       high n: n25:0.04827  n26:0.04797  n27:0.04767  n28:0.04738
       std-root deviation from Hermite: min 0.03888, max 0.05197 over n in reach
       => shape is UNIFORMLY ~Hermite (a few %%); it does NOT visibly ->0 (rises then
          plateaus): the GOR-Zagier ->0 limit is ~1/log n, unwitnessable here.
       non-hyperbolic (complex-root) J_{5,n} among tested: 0   (all hyperbolic)

================  WHAT THIS IS (honest reading)  ================
CONFIRMED in reach: every tested J_{d,n} (d=2..5, n<=~30) is HYPERBOLIC (real-rooted), and
its standardized root-shape sits UNIFORMLY CLOSE (~1-5%) to the Hermite/oscillator nodes.
The archimedean-oscillator shape is thus PERVASIVE, not merely asymptotic.

GATE CATCH (retained): the pre-registered guess -- deviation ->0, monotone, largest at low n
-- is REFUTED.  The deviation is small everywhere and mildly RISES then plateaus; the true
GOR-Zagier convergence to Hermite is ~1/log n, so it is NOT numerically witnessable (it would
remain a few %% even at n ~ 1e6).  Lesson: the limit is a THEOREM, not a numerical observation.

WHAT STANDS (the identification): Hermite = Fourier eigenfunctions = harmonic-oscillator /
Bargmann-Fock number states = THE ARCHIMEDEAN local structure.  GOR-Zagier (theorem) forces
J_{d,n} -> H_d for each d at large n; the program's metaplectic-UPT (Q8vM3 Lock B) independently
forces Bargmann-Fock at v=infinity.  So move (a)'s 'prolate/archimedean local positivity' is,
on the peaks side, this oscillator/Hermite class -- numerics corroborate the shape is already
oscillator-like + fully hyperbolic in reach.  RH's open content stays the SAME marginal step
(verify_jensen_turan_peaks: Turan margin largest at low n): whether ALL degrees stay hyperbolic
-- equivalently whether the low-n head joins the archimedean-forced oscillator tail.
Cornered, not crossed; the forcing structure is NAMED, and the limit is not numerically faked.
```
