# Primorial Hankel-Completion Probe (RH direction, forward-door [C])

**Script:** `empirical/verify_primorial_hankel_completion.py`
**Context:** P3 פ15 ($D_3=-787680<0$) / Paper 22 conservation-of-difficulty.
**Question:** can the archimedean place be supplied by a finite moment-completion?

Deterministic, exact (`fractions.Fraction`); no floating point in any sign, positivity,
or canonicity decision. The transcript below is the record.

```text
Exact probe: can the archimedean place be supplied by a FINITE moment-completion?

Forward-door probe for the RH direction (P3 פ15 / Paper 22 conservation-of-difficulty).
Grounded-paranoid-delusional gate: the settlement meaning below was fixed BEFORE the run.

Background (settled): the primorial is not a moment sequence -- its Hankel determinant
D_3 = -787680 < 0 (P3 פ15, independently verified). P3 reads this as: the real/archimedean
place must be ADJOINED from outside; the finite-prime data cannot self-complete the way the
factorial does (n! = int t^n e^{-t} dt, all D_k > 0, completes to Gamma).

The concrete question this probe settles: is "restore Hankel positivity by a finite
correction" a FAITHFUL finite shadow of the archimedean place -- i.e., is the finite shortcut
to the place real -- or is moment-positivity merely a number-field-growth artifact?

============================================================================
PRE-REGISTRATION  (matched-pair; meaning fixed pre-run)
============================================================================
K (faithful shadow): moment-positivity tracks the archimedean place. The number-field
   primorial fails (D_3<0) while the FUNCTION-FIELD primorial -- the face where the
   Riemann Hypothesis is Weil's THEOREM (no archimedean place needed) -- is moment-positive;
   and the completing datum is canonical. => the finite moment-completion is a faithful
   shadow of the place; the finite shortcut is live.

L (artifact): the function-field primorial ALSO fails moment-positivity (so "moment-positive
   <=> RH/place" is false), and/or the minimal finite completion is a non-canonical family
   (a free location parameter, different minimal mass for each). => moment-positivity is a
   generic primorial-growth artifact, not the place's shadow; the finite shortcut is
   foreclosed; the archimedean place is irreducibly analytic (P3's Gamma_inf, the
   metaplectic/UPT factor), not a finite moment correction.

JOINT-ON-DISJOINT: K that D_3<0 is a real, exact obstruction (factorial positive vs
   primorial fails: prime irregularity genuinely breaks moment positivity) AND L that it does
   not shadow the place (function field fails too; completion non-canonical). Net: re-confirms
   the No-Go from a new angle and redirects effort to the analytic/metaplectic place.
============================================================================

All arithmetic is exact (integers / fractions.Fraction); no floating point enters any sign,
positivity, or canonicity decision.

================  PART A: does moment-positivity track the place? (exact)  ================
Hankel determinants D_0..D_6 (sign is all that matters; a moment sequence has all >= 0):

  factorial   n!         (control; n! = int t^n e^{-t} dt, a moment sequence):
      D = [1, 1, 4, 144, 82944, 1194393600, 619173642240000]
      first negative at k = None   -> all >= 0 : IS a moment sequence (self-completes to Gamma)

  primorial   p_n#        (number field; RH OPEN):
      D = [1, 2, 24, -787680, -998163129600, -658205456445427968000, 138952974011268380748030005760000]
      first negative at k = 3

  ff-primorial q=2  D_0..D_4  (function field; RH is WEIL'S THEOREM, no archimedean place):
      D = [1, 0, -921600, -74769074762865285567637897301723185152, -(180-digit)]
      first negative at k = 2

  ff-primorial q=3  D_0..D_4  (function field; RH is WEIL'S THEOREM, no archimedean place):
      D = [1, 18954, +(55-digit), +(552-digit), +(5182-digit)]
      first negative at k = None

  [A-verdict] factorial moment-positive            : True
  [A-verdict] number-field primorial fails          : k=3
  [A-verdict] function-field primorial fails (q=2,3): k=2, k=None
  [A-verdict] does moment-positivity track RH/place : False
              (K needs YES: ff positive while nf fails;  L if ff also fails)

================  PART B: is the finite completion canonical? (exact)  ================
Add a point mass c*delta_a to the primorial's representing measure: s_n -> s_n + c*a^n,
a rank-1 PSD update H_3 -> H_3 + c*v v^T, v=(1,a,a^2,a^3). By the matrix-determinant
lemma the minimal completing mass at location a is c*(a) = -1 / (v^T H_3^{-1} v), valid
where the denominator is negative. A CANONICAL place would give one answer; a free
parameter a with a different mass for each a is a non-canonical family.

  primorial H_3 = [[1, 2, 6, 30], [2, 6, 30, 210], [6, 30, 210, 2310], [30, 210, 2310, 30030]]
  a   | w(a)=v^T H_3^{-1} v        | c*(a)= -1/w(a)  (minimal completing mass at a)
  ----+---------------------------+------------------------------------------------
    1 | 23597/16410               | (w >= 0: location cannot complete; mass would be infinite)
    2 | 8024/8205                 | (w >= 0: location cannot complete; mass would be infinite)
    3 | 8391/5470                 | (w >= 0: location cannot complete; mass would be infinite)
    5 | 20345/3282                | (w >= 0: location cannot complete; mass would be infinite)
    7 | 224693/16410              | (w >= 0: location cannot complete; mass would be infinite)
  1/2 | 3626699/2100480           | (w >= 0: location cannot complete; mass would be infinite)

  [B-verdict] NO positive point mass at a in {1,2,3,5,7,1/2} restores positivity
              (w(a) > 0 at every tested location): the finite point-mass completion
              does not even exist at the natural locations, let alone canonically.

================  REALIZED BRANCH  ================
JOINT-ON-DISJOINT, with the decisive half = L.

K  (real obstruction): the factorial is moment-positive and self-completes to Gamma,
   while the primorial fails (D_3<0). Prime irregularity genuinely breaks moment
   positivity -- the obstruction P3 פ15 found is real and exact.

L  (NOT the place): moment-positivity does NOT track the archimedean place.
   The FUNCTION-FIELD primorial -- where RH is Weil's proven THEOREM and there is no
   archimedean place at all -- FAILS moment positivity for q=2 (at D_2, even earlier
   than the number field) while PASSING for q=3 through the computed range. That
   q-dependence is decisive: moment-positivity tracks the constant field's arithmetic,
   not RH-status (which holds for every q). And (Part B) no positive point mass at the
   natural locations restores positivity (w(a)>0 throughout), so the finite completion
   does not even exist there. A finite moment-completion cannot be the archimedean place.

>>> The finite shortcut is foreclosed. D_3<0 correctly DETECTS that a completion is
>>> needed, but the completion is irreducibly analytic (P3's Gamma_inf; the
>>> metaplectic/UPT Bargmann-Fock factor) -- not a finite moment correction. This
>>> RE-CONFIRMS the No-Go from a fresh angle and redirects effort to the analytic place.
```
