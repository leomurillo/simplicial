# Apex zero-variety probe suite — findings log

Object: M(beta, c) = (1/N) sum_s exp(beta y_s) conj(chi_c(s)), a finite
exponential sum in beta (entire, exponential type). Zeros located by
argument principle (rigorous count) + grid-seeded Newton (mpmath, dps=30).
Deterministic numpy/mpmath gate; no torch, no network.

Spine targets: T1 analytic class, T2 strip, T3 counting law = Delta_y/pi,
T4 exact-line locus / no-go mechanism, T5 functional equation,
T6 Newton-polygon (complex sector), T7 Carlson rigidity (imported).

================================================================================
## RESUME / COMPACTION ANCHOR (2026-06-17) — read first
================================================================================
WHO/WHERE: paper = "The Zero Variety of the Apex Generator: From the Lee-Yang
Lattice to Weil's Line" (forward door T0 6.6 = T7 7.4, resolves T7 Conj 7.4).
Suite: empirical/apex_zeros/ (apex_core.py, ff_core.py, ff_ext.py, c1..c12,
run_all.py). All deterministic numpy/mpmath/exact-int, NO torch. GATE C1-C12 GREEN.

THE THESIS (one line): "a critical line is an EQUAL-MODULUS phenomenon."
Tilt formula  Re = log|coeff|/log(base): additive char coeffs (|.|=1) -> Re 0
(trivial line); units-indicator phi-weights -> arithmetic, not special;
function-field Gauss/Jacobi (|.|=sqrt q) -> Re 1/2 = WEIL (provable). The 1/2 is
norm-q purity in the cyclotomic CM field; the log-density ζ has = the archimedean
place the additive apex lacks.

SPINE (all PASS): T1 analytic/exp-type (C1); T2 strip |Re|<=log(N-1)/gap (C1);
T3 counting n(T)=(Delta_y/pi)T+O(1), c-indep (C2); T4 exact-line locus = geometric
(equal-spacing) ledger only (C3) + generic mean->0 no-go (C5); T5 functional eq
conj M(conj b,c)=M(b,-c) (C7); T6 complex sector = Newton polygon of conv{y_s},
edge-normal rays (C6); T7 Carlson rigidity imported (T7 Prop 5.7).
3 NEW THEOREMS (ours, beyond T0/T7 which had only N=2): (1) equal-spacing exact
line (C3); (2) Newton-polygon zero variety (C6, = Conj 7.4); (3) Ramanujan 2-term
bridge (C8). Higher genus: C10 (quartic g=3, Gaussian-integer CM). Two-place 1/2:
C11 (p-adic Newton, avg slope 1/2 = archimedean weight). Function-field innovation
chain: C12 (Levinson/Toeplitz, PSD<=>purity) — the bridge to the Connes/(H0') thread.

SCOPE TIERS: finite additive theory (C1-C7) = THEOREM [P/A]. Additive critical
line = NO-GO with mechanism [P] (replaces T7 Conj 7.6-additive). Function-field
Weil 1/2 (C9-C12) = re-derivation of classical Weil/Mazur/CM inside the apex frame
[P]. The bridge "constant density -> log density = archimedean place" = [C].

MANUSCRIPT STATUS: DRAFTED 2026-06-17 -> ../../T7.4-ApexZeroVarietyLeeYangToWeil-Draft1.md
(version 0.1, ~320 lines). Title "The Zero Variety of the Apex Generator: From the
Lee-Yang Lattice to Weil's Line"; labelled \heb{ל}7.4 (resolves T7 Conj 7.4 / settles
T7 §7.6 additive aspiration as no-go / realizes §7.6 provable target in-frame; number
is provisional, trivially renamable). Structure: abstract (Situation/Gap/Action/Result/
Harvest house leads) + cross-ref table + notation/tiers + §1 analytic class & strip &
Carlson-import + §2 counting law + §3 equal-spacing exact line (Thm 3.1, NEW) & no-go
(Thm 3.3) & c=phase (Prop 3.2) + §4 Newton-polygon variety (Thm 4.1, NEW keystone,
Cor 4.2-4.3) + §5 FE + §6 Ramanujan two-term tilt (Thm 6.1, NEW) + §7 tilt ladder &
Weil (Thm 7.1) + §8 CM purity (Thm 8.1) + §9 two-place ½ (Thm 9.1) + §10 innovation
chain & (H0') bridge (Thm 10.1) + §11 scope/firewall/forward-doors + App A C1-C12 cert
table + references. Tiers [P]/[A]/[C], firewall on the one [C] seam (missing-log =
archimedean place). NOTE: paper's own theorems are numbered by section (NOT "T1-T7" —
that collides with the ל-series). NEXT STEP on resume: (a) Leo's read/revise pass;
(b) optional build+visual-inspect PDF (build.ps1; affiliation line + linker per the
manuscript-build-pipeline memory); (c) assign final ל-number.

SISTER THREAD (do not merge into this paper): the (H0') / Connes-CvS work lives in
empirical/p_infinity/ (probe_cvs_weld.py, probe_archimedean_schur.py) + the 2nd note
C:\Projects\Connes\SecondNote-WeilForm-CvS-RealZeros-Draft1.md. C12 is the shared
bridge. Memory: project_apex_zero_variety_paper.md has the full log incl. the CvS
weld + the realness=(H1)/positivity=(H0') correction + the Suzuki [Su12] anchor.
================================================================================

## C1 — strip + completeness — PASS
- N=3,4,6, structured + random ledgers, all characters c.
- Argument-principle count == Newton-found count (completeness) in every case.
- Residual |M(zero)| ~ 1e-31.
- Every zero inside the provable strip  -log(N-1)/gap_bot <= Re <= log(N-1)/gap_top.
- Density spot-check: N3 ramp Delta_y=1.0986, T=12.37 -> (Delta/pi)T = 4.33 -> 4 zeros. OK.

## NEW THEOREM (discovered in C1, confirmed) — Equal-spacing exact line
If y is an arithmetic progression with common spacing a (i.e. x geometric),
then M(beta,c) = (1/N) sum_s (w*zeta^{-c})^s with w=e^{a beta}, zeta=e^{2pi i/N};
this is a geometric series, vanishing iff (w zeta^{-c})^N = 1 and w zeta^{-c} != 1,
i.e. iff |w| = 1  <=>  **Re beta = 0 EXACTLY**, for every c and every N.
Zeros at beta = 2pi i (k + offset_c)/(N a).
- Verified N=3,5,7: max|Re(beta)| over all c ~ 1e-31..1e-16; Im parts are exact
  integer multiples of 2pi/(Na) to ~1e-30.
- Generalizes T0 Prop 2.5 (N=2 cosh) and T7 Prop 6.2 to all N.
- Refines spine T4: the exact additive "critical line" is the MAXIMAL-SYMMETRY
  (equal-spacing) locus, a codim-(N-2) subvariety of ledger space — a symmetry
  phenomenon, not an arithmetic one. Generic ledgers push zeros off-axis into
  the strip (mean Re -> 0 but spread > 0). This is the honest no-go for an
  arithmetic additive critical line, now with an exact characterization.

## C2 — counting law n(T) ~ (Delta_y/pi) T — PASS
- Regression slope within <1% of Delta_y/pi for N4/5/6, geometric + ramp + random.
- Residuals n(T)-(Delta/pi)T bounded in O(1) (|.| < 1.8), NOT growing -> constant density.
- c-INDEPENDENCE confirmed: N5 ramp slopes over c = 0.5122/0.5102/0.5113/0.5113/0.5102
  (all = Delta/pi); finite-box counts differ by O(1) (boundary), density identical.
- On-line geometric ledger has the SAME density as off-line ledgers: density is set by
  support width Delta_y only, not by where the zeros sit. (Needed composite Gauss-
  Legendre contour, panel length 4, to keep the integer count clean up to T=320.)

## C3 — exact-line locus — PASS
- Geometric ledgers N=2..7, all c: found zeros match the exact set
  {2 pi i m/(aN): m != c mod N} to ~1e-30; max|Re beta| ~ 1e-30.
- Non-geometric controls ([1,2,3], [1,2,3,5]) are off-line (max|Re| 0.94, 0.38).
- CAUTION captured: [1,2,4] is secretly geometric (x2) -> on-line. The locus is
  EQUAL log-spacing, judged by spacings, not by "looks like a ramp".

## C4 — c is a phase/offset (cyclic-shift covariance) — PASS
- Exact: relabel x_s->x_{s+1} gives M_shift(beta,c)=zeta^c M(beta,c) (ratio err ~1e-30).
- Hence each mode's zero set is invariant under cyclic relabel (cross-residual ~1e-31).
- With C2 (density c-indep) + C3 (c removes residue class c from the lattice), c is
  pinned to the imaginary-offset / selection-rule role.

## C5 — approximate critical line / no-go (T4) — PASS
- Generic ledgers: mean Re(beta) -> 0 as T grows (e.g. -0.082->-0.026, +0.095->+0.027),
  RMS spread stays > 0 and bounded (~0.4-0.9) -> genuinely off-line.
- Geometric locus: spread 2e-30 (exact line).
- Arithmetic flavor: primes [2,3,5,7,11,13] gave the LARGEST off-line spread (0.92),
  squares the smallest (0.43) -> irregular log-spacing pushes hardest off the line.
- Reading: the Re=0 accumulation is forced by unitarity (equal |coeff|), approximate
  off the symmetry locus; an arithmetic critical line needs equal-modulus BROKEN
  (sqrt q Frobenius/Gauss weights), which is the function-field lift / bridge.

## C6 — complex sector = Newton polygon (T6) — PASS  [KEYSTONE]
- Complex frequencies y_s in C: zeros accumulate on rays PERPENDICULAR to the edges
  of conv{y_s} (indicator diagram), spacing 2pi/|edge|, density |edge|/2pi.
- N=2 complex: exact Prop 6.2 lattice (match ~1e-31), incl. uniform-modulus equator
  where the line rotates onto the REAL axis (Lee-Yang condensation: genuine real-beta
  vanishing / quantum-coherence singularity).
- N=3 complex: triangle hull -> 3 edge-normal ray families; far zeros align to predicted
  angles to ~0.012 rad (~0.7 deg); argument-principle count == found (8, 12); longest
  edge carries the most zeros.
- UNIFICATION: real ledger = degenerate hull (segment on R) = single imaginary-axis
  family = C2's law n(T)~Delta_y T/pi. This is the precise form of Conj 7.4's
  "structured subvariety", and it subsumes C1-C5 as the real (collapsed) case.

## C7 — functional equation (T5) — PASS
- Exact: conj M(conj beta, c) = M(beta, -c) (residuals ~1e-31, one == 0).
- Zero set of mode c = conjugate of mode (N-c); self-conjugate modes c in {0,N/2}
  have zeros symmetric about the real axis. Apex analog of an L-function FE.

## C8 — arithmetic bridge (the thesis) — PASS
- Units-indicator ledger on Z/N is 2-level -> via Ramanujan sums the apex is a
  TWO-TERM exponential sum, exactly solvable.
- c=0 zeros on the OFF-LINE arithmetic position Re* = log((N-phi(N))/phi(N))
  (residual ~1e-31), Im on odd multiples of pi. Re* GROWS along primorials:
  N=6 -> 0.6931, N=30 -> 1.0116, N=210 -> 1.2164.
- c!=0 zeros back on Re=0 (Ramanujan coeffs c_N(c), -c_N(c): equal modulus).
- Density CONSTANT Delta_y/pi (slope 0.3157 vs 0.3183), linear resid ~0.9; a
  T log T model misfits 3.8x worse -> NO log factor.
- BRIDGE READING: arithmetic moves the LINE POSITION via unequal coefficient
  moduli (here phi vs N-phi; the sqrt(q) Frobenius/Gauss weights are the deep
  version yielding Weil's 1/2). The zero DENSITY stays linear; zeta's
  (T/2pi)log T log cannot arise from a finite exponential sum. The missing log =
  the archimedean place (ties to T15 / P0 / N-series Archimedean operator).

## C9 — function-field apex lift: Weil's 1/2 = the sqrt(q) tilt — PASS  [PAYOFF]
- Change base ring Z/N -> F_q. Multiplicative-apex coefficients become Gauss /
  Jacobi sums. Verified |g(chi^a)| = sqrt(q) and |J(chi^a,chi^b)| = sqrt(q) to
  ~1e-29 for q=7,13,19,31,61,43 across N=3,5,7 (all 2g=(N-1)(N-2) pairs).
- The Jacobi sums ARE the Frobenius eigenvalues alpha_i; |alpha_i|=sqrt q is Weil's
  curve RH. Under T=q^{-s}:  Re s = log|alpha|/log q = log(sqrt q)/log q = 1/2 EXACTLY.
- N=3 worked zeta (Fermat cubic, g=1): brute #E(F_q) -> a_q -> Frobenius alpha;
  |alpha|=sqrt q, Re s=0.500000, alpha = -J(chi,chi) (match ~1e-16), and brute
  #E(F_{q^2}) = q^2+1-(alpha^2+conj^2) (63, 171) -- Frobenius confirmed on extension.
- THE TILT LADDER (one formula, three rungs of  Re = log|coeff|/log(base)):
      additive characters     |coeff| = 1      -> Re = 0     (trivial line; C2/C5)
      units-indicator         phi vs N-phi     -> arithmetic (C8; not special)
      function field          |coeff| = sqrt q -> Re = 1/2   (Weil; PROVABLE)
  The "1/2" is not mysterious: it is the weight-1 purity |alpha|=q^{1/2} of H^1 of
  the curve -- Frobenius SUPPLIES the sqrt(q) tilt that the additive apex (unitary
  coeffs) cannot, and that the archimedean zeta must manufacture. This realizes
  T7 7.6's concrete provable target.

## C10 — higher genus: Fermat quartic L-polynomial (g=3) — PASS
- Extends C9 from g=1 to g=3 (degree-6 L-poly). Built from brute #C(F_{q^n}), n=1,2,3
  (ff_ext.py F_{p^d} machinery, frequency-convolution, O(p^d)) + functional equation
  c_{6-k}=q^{3-k}c_k. FE genuinely TESTED: the completed poly predicts #C(F_{q^4})
  (e.g. q=13: p_4=-714) matching brute. All 6 |alpha_i|=sqrt q -> Re s=1/2.
- NEW INSIGHT (CM purity): the order-N apex eigenvalues are Weil numbers in the
  cyclotomic field Q(zeta_N) of the apex character -- GAUSSIAN INTEGERS a+bi with
  a^2+b^2=q for N=4 (q=13:-3+-2i, 17:1+-4i, 29:5+-2i, 37:1+-6i; Eisenstein Z[zeta_3]
  for N=3). Weil's 1/2 = norm-q purity in the CM field. Fermat-quartic Jacobian is
  CM -> spectrum collapses to one conjugate pair x3 (one critical-line height x3).
- Honest note: even-N eigenvalue<->Jacobi-sum dictionary carries a character
  normalization (point-count route is ground truth); |J|=sqrt q (C9) is the clean
  apex-coefficient modulus regardless.

## C11 — p-adic Newton polygon: companion to C6, the second place of 1/2 — PASS
- C6 = ARCHIMEDEAN Newton polygon (indicator of {y_s}, place infinity, the critical
  line). C11 = p-adic Newton polygon of the L-poly (lower hull of (k, v_p(c_k)),
  place p, Frobenius valuations). SAME eigenvalues, two places.
- THE 1/2 AT BOTH PLACES: |alpha|=q^{1/2} archimedean (every eigenvalue, Re s=1/2);
  AVERAGE p-adic Newton slope = g/2g = 1/2 = slope of the Hodge diagonal (0,0)->(2g,g).
- Ordinary (p=1 mod N, the Gauss-sum setting): Newton=Hodge, slopes {0^g,1^g}
  (verified cubic g=1 and quartic g=3). Supersingular (cubic p=2 mod 3, a_p=0):
  Newton=diagonal, EVERY slope=1/2 -- p-adic slopes literally equal the archimedean
  weight (the crystalline shadow of 1/2). Mazur "Newton >= Hodge" verified throughout.

## C12 — function-field innovation chain: the provable template for d(s)>0 — PASS
- Ports P infinity-F section 19's innovation chain to the place positivity is a THEOREM.
- The curve's Weil form is the real Toeplitz matrix of normalized point counts
  a_k = (q^k+1-N_k)/q^{k/2} = sum_i (alpha_i/sqrt q)^k. EXACT dictionary:
    innovation d(s) = Levinson-Durbin prediction error E_m;
    Gohberg-Krein/Schur params = reflection coefficients k_m;
    "factorizes outer, no inner factor" = |k_m| <= 1 (Schur/Szego);
    d(s)>0 for all s = Toeplitz PSD = (a_k) positive-definite = normalized Frobenius
       UNITARY = |alpha_i|=sqrt q = WEIL PURITY.
- REAL curves (cubic g=1 q=7..61; quartic g=3 q=13,17,29): |a_k|<=2g, Toeplitz PSD
  (min-eig ~1e-13), Schur |k_m|<=1, innovations E_m positive then ->0 at rank 2g
  (= "Weil process asymptotically deterministic", section 19.2 — from ABOVE, by purity).
- FAKE off-circle (eigenvalue pushed off |alpha|=sqrt q, FE preserved): |a_k| UNbounded
  (7.7, 61), Toeplitz min-eig O(1) negative (-8, -92), a Schur k_m>1 (1.06, 1.17), an
  innovation E_m<0 (-0.235, -1.08). The chain DETECTS the zero leaving the circle = (H0')
  failing, in the place it cannot.

### The extracted template (what archimedean (H0') must reproduce)
- (H0') in the solvable place IS Szego/Schur: d(s)>0 for all s <=> the Weil moment
  sequence is a SCHUR SEQUENCE (all reflection coefficients |k_m| <= 1) <=> a unitary
  normalized flow exists. This is the reflection-coefficient (contraction) form of (H0'),
  sharper/more local than the Rayleigh form — and it IS P infinity-F section 23's
  "contraction frame", here identified as the classical Schur algorithm.
- Frobenius hands the unitary over for FREE (Frob/sqrt q unitary, by Weil/Deligne =
  sqrt q-purity = the apex equal-modulus tilt); Q has no Frobenius -> must MANUFACTURE
  it via the Gamma-factor normalization of the scaling flow. That manufacture is RH.
- Structural difference located: the function field REACHES determinism (finite rank 2g,
  innovation hits exactly 0); the archimedean place has INFINITE rank -> innovation never
  reaches 0 -> (H0') is the limit statement "stays positive forever while ->0", exactly
  section 19's "approached from the positive side, never crossed". So the FF case fixes
  the FORM of the answer (per-step Schur contraction); the archimedean difficulty is the
  infinitude (every one of infinitely many Schur steps must stay in the disk).
- Implied next task: compute the ARCHIMEDEAN Schur parameters of QW_lambda (Toeplitz/Hankel
  moment structure of the CCM matrix) and test |k_m|<=1 — the contraction form of (H0'),
  matching section 23's frame, with C12 as the template.

================================================================
GATE: C1-C12 ALL PASS (run_all.py). numpy/mpmath/exact, deterministic, no torch.
Full ladder: additive no-go (C5) -> arithmetic intermediate (C8) -> function-field
theorem (C9 Weil 1/2) -> higher genus (C10, g=3, Q(zeta_N)-CM) -> two-place 1/2
(C11, archimedean |alpha|=sqrt q AND average p-adic slope 1/2).
================================================================

## Spine status after the suite
- T1 analytic class .......... C1 (entire, exp type; |M(it,c)|<=1)         PASS
- T2 strip confinement ....... C1 (|Re| <= log(N-1)/gap)                     PASS
- T3 counting law ............ C2 (n(T) = (Delta_y/pi)T + O(1), c-indep)     PASS
- T4 exact-line locus/no-go .. C3 (geom = exact line) + C5 (generic mean->0) PASS
       *** sharpened to a THEOREM beyond the papers (equal-spacing) ***
- T5 functional equation ..... C7 (conj M(conj b,c)=M(b,-c))                 PASS
- T6 Newton polygon (complex)  C6 (edge-normal rays; Prop 6.2 lift)          PASS
- T7 Carlson rigidity ........ imported from T7 Prop 5.7 (not re-probed)
- Bridge (conjectural limit) . C8 (arithmetic moves line; density stays linear;
                                   the log = archimedean gap)                PASS

## New theorems harvested (beyond T0/T7, for the paper)
1. EQUAL-SPACING EXACT-LINE THEOREM (C3): y arithmetic progression (x geometric)
   => M(beta,c) geometric in w=e^{a beta} => zeros exactly {2 pi i m/(aN): m!=c (N)},
   all on Re=0, every N, every c. Generalizes T0 Prop 2.5 / T7 Prop 6.2 (N=2 only).
2. NEWTON-POLYGON ZERO VARIETY (C6): complex-sector zeros = edge-normal rays of
   conv{y_s}; density per ray = edge/2pi; real ledger = degenerate segment = C2.
   Makes Conj 7.4's "structured subvariety" precise; unifies the whole suite.
3. RAMANUJAN 2-TERM REDUCTION + BRIDGE (C8): units-indicator apex is 2-term;
   critical line = equal-modulus phenomenon; arithmetic (phi/Ramanujan, sqrt q)
   sets line position; constant density => the log is the archimedean place.

## Methodology notes (gotchas captured)
- Argument-principle count needs COMPOSITE Gauss-Legendre (panel len ~4) to stay a
  clean integer up to large T; a single fixed-node rule drifts > 0.05 by T~300.
- Zero-set comparison must use nearest-neighbour / direct-evaluation residual, not
  sort-then-zip (unstable when Im ~ 0, e.g. uniform-modulus equator -> real axis).
- [1,2,4] is SECRETLY geometric (x2): the exact-line locus is EQUAL log-spacing,
  judged by spacings, not by "looks like a ramp".
