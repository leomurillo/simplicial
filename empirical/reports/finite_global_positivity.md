# Finite Global-Positivity Model — how far, and the archimedean wall

**Script:** `empirical/verify_finite_global_positivity.py`
**Context:** RH-direction step (c); metaplectic/UPT global positivity; P4 פWeil / P3 פ15.
**Status:** function-field (circle) positivity = RH captured exactly; wall = archimedean place

Exact integers only; no floating point in any PSD / sign decision. The transcript is the record.

```text
How far does an EXACT FINITE model of Weil/adelic global positivity reach, and where is
the archimedean wall?  (RH-direction step (c); metaplectic/UPT global-positivity.)

Grounded-paranoid-delusional gate: meanings fixed BEFORE the run.

The idea. On the FUNCTION-FIELD face (a curve C/F_q) the Riemann Hypothesis is Weil's
theorem and the whole object is finite and exact: Frobenius acts on H^1 with eigenvalues
alpha_1..alpha_{2g}, the power sums S_k = sum_i alpha_i^k are integers (S_0=2g; N_k =
q^k + 1 - S_k are the point counts), and RH is the statement |alpha_i| = sqrt(q), i.e. the
eigenvalues lie on the CIRCLE of radius sqrt(q). By Herglotz/Bochner that circle-positivity
is a TOEPLITZ positivity: c_k = S_k/q^{k/2} are the trigonometric moments of a positive
measure on the circle (the angle atoms) iff the Toeplitz matrix (c_{m-m'}) is PSD. Clearing
the sqrt(q) by the diagonal congruence diag(q^{m/2}) gives the EXACT INTEGER matrix

        M_{m,m'} = S_{|m-m'|} * q^{min(m,m')},

with  M >= 0  <=>  Toeplitz >= 0  <=>  eigenvalues on the circle  <=>  RH for the curve.

This is a finite, exact, RH-equivalent positivity. The number-field side has the SAME shape
but two ingredients a finite model cannot supply: (i) infinitely many zeros (no finite
operator; the program's KU-3 finite Bures envelope already failed), and (ii) the geometry is
the LINE/strip, not the circle -- the number-field "primorial" obstruction is a HANKEL
(real-line moment) failure, D_3 = -787680 < 0, while the curve is a TOEPLITZ (circle) success.
The circle-vs-line difference is exactly the archimedean place: the metaplectic/UPT step
SELECTS the archimedean local factor pi^{-s/2} Gamma(s/2) (the line's completion), but its
global-positivity contribution is the open part. The finite model reaches the wall there.

============================================================================
PRE-REGISTRATION (matched-pair; fixed pre-run)
============================================================================
K: the integer matrix M is PSD exactly for Hasse-valid curves (RH holds) and NOT PSD for
   RH-violators (a^2 > 4q etc.), at the genus-1 and genus-2 levels, by exact leading-minor
   signs -- so the finite model captures function-field global positivity precisely; and the
   transport wall is identified as the archimedean place (circle Toeplitz holds vs line Hankel
   fails) plus infinite spectrum.
L: M does not track RH (PSD for a violator, or non-PSD for a real curve), or the wall is
   elsewhere (the finite model already fails on the function-field face).
JOINT-ON-DISJOINT: K that the function-field/circle positivity is exactly captured AND that
   the number-field transport hits the archimedean wall (line Hankel D_3<0 vs circle Toeplitz
   PSD; finite vs infinite spectrum) -- the wall is the place, made concrete.
============================================================================

Exact integers only; no floating point in any positivity, sign, or PSD decision.

================  FUNCTION-FIELD FACE: circle (Toeplitz) positivity = RH (exact)  ========
M_{m,m'} = S_{|m-m'|} q^{min(m,m')}; PSD <=> Frobenius eigenvalues on |z|=sqrt(q) <=> RH.
Level-1 leading minor is exactly 4q - a^2, the Hasse-Weil bound.

  -- genus 1 (T^2 - aT + q) --
   q | a  | a^2<=4q (RH) | leading minors of M            | M PSD | model == RH
  ---+----+--------------+--------------------------------+-------+------------
   7 | -1 | True         | [2, 27, 0, 0, 0]               | True  | True   Fermat cubic /F_7 (P4 פWeil)
   2 |  2 | True         | [2, 4, 0, 0, 0]                | True  | True   real
   3 |  3 | True         | [2, 3, 0, 0, 0]                | True  | True   real
   5 |  4 | True         | [2, 4, 0, 0, 0]                | True  | True   real
   7 |  5 | True         | [2, 3, 0, 0, 0]                | True  | True   real
   7 |  6 | False        | [2, -8, 0, 0, 0]               | False | True   RH-VIOLATOR (no curve: Hasse forbids)
   2 |  3 | False        | [2, -1, 0, 0, 0]               | False | True   RH-VIOLATOR
   5 |  5 | False        | [2, -5, 0, 0, 0]               | False | True   RH-VIOLATOR

  -- genus 2 (E_a x E_b over F_q; RH <=> a^2<=4q AND b^2<=4q) --
   q | a,b   | RH    | leading minors of M                    | M PSD | model == RH
  ---+-------+-------+----------------------------------------+-------+------------
   7 | -1,2  | True  | [4, 111, 6426, 2571912, 0]             | True  | True   real x real
   5 |  4,-2 | True  | [4, 76, 7200, 2073600, 0]              | True  | True   real x real
   7 |  6,2  | False | [4, 48, 3584, -2408448, 0]             | False | True   VIOLATOR (first factor)
   5 |  5,0  | False | [4, 55, 3750, -1562500, 0]             | False | True   VIOLATOR (first factor)

  [FF-verdict] integer Toeplitz model tracks curve-RH on every case: True

================  THE WALL: number-field transport (exact contrast)  ====================
  Number-field 'primorial' is a LINE (Hankel / real-line moment) object, not a circle one.
  Hankel leading minors of the primorial: [1, 2, 24, -787680]
      -> first negative at k=3 (D_3 = -787680 < 0): NOT a moment sequence; RH OPEN.

  Side by side:
    function field : CIRCLE  (Toeplitz)  -> PSD holds       -> RH is Weil's THEOREM
    number field   : LINE    (Hankel)    -> D_3 < 0 fails   -> RH is OPEN
  The circle-vs-line difference IS the archimedean place. A curve is complete (no
  archimedean place; finite 2g-dim Frobenius). Spec Z has the place at infinity and
  infinitely many zeros (no finite operator -- the program's KU-3 confirmed this).

================  REALIZED BRANCH  ================
JOINT-ON-DISJOINT.

K  (model reaches): the EXACT integer Toeplitz positivity captures function-field global
   positivity precisely -- PSD <=> RH on every genus-1 and genus-2 case, the level-1 minor
   IS the Hasse-Weil bound 4q-a^2, and RH-violators are detected by an exact negative minor.
   On the face where RH is proven and there is no archimedean place, the finite model is the
   whole story.

L  (wall = the place): the number-field transport needs the LINE (Hankel), where the
   primorial fails (D_3<0), not the CIRCLE (Toeplitz), where the curve succeeds; and it
   needs an infinite spectrum (KU-3). Both missing ingredients are the archimedean place.
   The metaplectic/UPT step selects the place's local factor pi^{-s/2}Gamma(s/2) (the line's
   completion) but cannot supply its global-positivity contribution from finite data.

>>> HOW FAR THE FINITE MODEL GOES: all the way to PROVEN global positivity on the
>>> function-field (circle) face, and exactly to -- not across -- the archimedean wall on
>>> the number-field (line) face. The wall is the place, now exhibited as circle vs line.
```
