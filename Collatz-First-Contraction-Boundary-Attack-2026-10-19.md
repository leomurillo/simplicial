# First-contraction boundary: a false lemma removed and an exact finite theorem

Status: the all-contracting-word margin conjecture is false. The first-contraction bound below is proved; its finite certificate covers all positive odd starts at crossing lengths up to 1,000. Neither universal coefficient crossing nor Collatz is proved. This is not claimed as a record or a new literature result.

## 1. A counterexample missed by the word census

The older `empirical/reports/collatz_margin_theorem_candidate.md` proposed q_w>=0 for every contracting word, where r_w is its least positive exact-cylinder representative and q_w=(r_w-U_w(r_w))/2.

Take the odd-only word

    w=(4,1,1,1,1,2,2,1,2,1,1,2,1,1,1,2,3).

Its exact data are

    m=17, S=27, A=3^17=129140163,
    C=1106233681, D=2^27-3^17=5077565,
    r=165, U_w(r)=167, q=-1.

The full odd trajectory is

    165,31,47,71,107,161,121,91,137,103,155,233,175,263,395,593,445,167.

The cylinder modulus is 2^28 and 165 is its least positive representative. Thus a multiplier below one need not give descent even at the first positive point of a cylinder. The earlier census ended at word length 12 and could not detect this example. Random words with large mean exponent are also poorly targeted to near-neutral slopes.

A second example disproves the proposed universal append-one positivity step itself:

    w=(1,1,2,1,1,2,6,1,1,1,1,2,2,1,2,1,1),
    r=231, U_w(r)=233, m=17, S=27, C=1441352971, q=-1.

Its 16-step parent has the same representative 231, endpoint 155, margin 38, and positive D. The last step has zero lift digit and sends 155 to 233, so the margin drops by (155+1)/4=39. Both parent and child are contracting. The suffix-monotonicity theorem for appended exponents >=2 remains valid; universal control of the exponent-1 channel is false.

Both examples have already descended before the displayed endpoint. They do not refute a first-descent statement.

## 2. Keep the minimum, not only the endpoint

For a word w with prefixes F_j(n)=(3^j n+C_j)/2^{S_j}, its no-descent domain is the exact cylinder intersected with

    n <= min_{j: 2^{S_j}>3^j} C_j/(2^{S_j}-3^j).

This prefix minimum cannot be replaced by the last ratio. In the 165 example the first step is already a descent. Any legitimate non-descent search prunes that path immediately for that seed.

For n>1 odd, define its odd-step coefficient crossing kappa(n) as the least m>=1 for which 2^{S_m}>3^m, or infinity if none exists. Before this crossing every affine prefix has slope greater than one and positive intercept, and hence exceeds n. Thus the first crossing is the first possible place for descent, though descent there is not automatic from the slope alone.

This connects with Terras's coefficient stopping-time conjecture. Rozier and Terracol study contracting-coefficient paths whose endpoints do not descend, calling them paradoxical sequences. They explicitly distinguish these from failures at first descent. Their principal convention is the shortcut map, so our odd-step checkpoint assertion should not be silently identified with equality of the shortcut stopping times. Source: https://arxiv.org/html/2502.00948v2 .

## 3. A sharp word-independent bound at first crossing

Put L_j=floor(log_2(3^j)), with L_0=0, and define the integers

    B_0=0,
    B_m=3 B_(m-1)+2^{L_(m-1)},
    d_m=2^{L_m+1}-3^m > 0.

No numerical logarithms are needed: L_j is the bit length of 3^j minus one.

**Theorem 1.** If m is the first coefficient crossing of a positive odd integer n and U^m(n)>=n, then

    n <= C_m/(2^{S_m}-3^m) <= B_m/d_m.                 (1)

**Proof.** For 1<=j<m, non-crossing implies 2^{S_j}<3^j and hence S_j<=L_j. Expanding the affine numerator gives

    C_m=sum_{j=0}^{m-1} 3^{m-1-j} 2^{S_j}
       <=sum_{j=0}^{m-1} 3^{m-1-j} 2^{L_j}=B_m.

At crossing S_m>=L_m+1, so 2^{S_m}-3^m>=d_m. Finally U^m(n)>=n is exactly n(2^{S_m}-3^m)<=C_m. Combining proves (1). QED.

The envelope is sharp as a bound over formal first-crossing exponent words: prescribe S_j=L_j for 1<=j<m and S_m=L_m+1. Consecutive differences are positive integers, so this is a genuine admissible exponent word, and its C and D are B_m and d_m. This does not say its least positive representative realizes a no-descent exception.

Also B_m/3^m=(1/3)sum_{j<m} 2^{L_j}/3^j <=m/3, with strict inequality for m>=2. Thus, writing delta_m=d_m/3^m,

    B_m/d_m <= m/(3 delta_m).                          (2)

The dangerous lengths are those where 3^m lies close below a power of two. The finite certificate retains the exact d_m, not a rounded logarithmic estimate.

## 4. A finite theorem for all starting integers

**Computer-assisted Theorem 2.** For every positive odd n>1 whose first odd-step coefficient crossing occurs by m=1,000, the crossing endpoint is strictly smaller than n.

**Finite reduction.** Direct integer recurrence gives

    max_{1<=m<=1000} floor(B_m/d_m)=238670,

attained at m=971, where L_m+1=1539. Theorem 1 excludes every larger n from being a counterexample. For the 119,334 odd seeds 3<=n<=238670, the verifier computes the actual first crossing and checks strict descent. All pass; the largest observed first crossing is at 85 odd steps. Therefore no exceptional seed exists, irrespective of its size, for any first crossing by step 1,000. This is a bounded-crossing theorem, not a bound of 1,000 on all coefficient stopping times.

Some record values of floor(B_m/d_m) are:

| m | Exact bound |
|---:|---:|
| 17 | 108 |
| 41 | 867 |
| 147 | 4862 |
| 306 | 72058 |
| 971 | 238670 |

The bound at m=17 also explains why 165->167 cannot be a first-crossing exception: it exceeds the maximal permitted seed 108. Its prior contraction is essential.

Reproduce with `python empirical_01g/first_contraction_boundary_certificate.py`. The script uses only integers, checks both counterexamples, and saves its records and exact maximizing numerator/denominator to the adjacent JSON file.

## 5. A boundary-strip concentration requirement

The envelope can be refined without discarding the path. At a first crossing put

    Delta_j=L_j-S_j>=0,   a_j=2^{L_j}/3^j,   0<=j<m.

These integers Delta_j measure distance from the coefficient boundary, and

    C_m/3^m=(1/3) sum_{j<m} a_j 2^{-Delta_j}.          (4)

For an integer h>=1 let N_h count the indices with Delta_j<h. Since a_j<=1,

    C_m/3^m <= (1/3)[N_h+(m-N_h)2^{-h}].              (5)

Consequently any first-crossing failure of descent must satisfy

    N_h >= [3n delta - m 2^{-h}]/[1-2^{-h}],
    delta=(2^{S_m}-3^m)/3^m>0.                        (6)

This is a proved necessary concentration condition. When its right side is positive, failure requires sufficiently many prefixes in a thin strip near the coefficient boundary. It yields a path-dependent sufficient descent test by reversing (6) strictly. When the right side is negative the condition is vacuous; it cannot be promoted to a uniform positive-density assertion. The especially small gaps between powers of 2 and 3 are exactly where this loss of force matters.

## 6. What could close the proof

For odd n>1 the two outstanding assertions are:

1. A coefficient crossing occurs at a finite time.
2. At some crossing, the full affine correction is repaid.

The first-crossing strategy would settle both if, for every n>238670, one could prove a finite crossing at an m satisfying

    n*d_m>B_m.                                       (3)

The bounded seeds already descend by the exact audit. Equation (3) is a sufficient target, not an established fact or a necessary consequence of Collatz. The sharper word-dependent inequality n(2^{S_m}-3^m)>C_m could work even when (3) fails.

In the crystal language, the coefficient is determined by the 2- and 3-directions, but the affine numerator and the exact residue representative must be estimated jointly. The present bound controls the numerator using first-crossing geometry. It does not control the orbit's first-crossing time or prevent exceptional concentration near the small gaps d_m.

There is no justification for asserting that all paths eventually cross simply because each finite expanding pattern ends. Nor can shrinking measure of the surviving cylinders exclude every positive integer. Further proof work should target a deterministic bound tying the actual first crossing to n and d_m, while preserving the prefix minimum. Proving q_w>=0 for every contracting word is no longer a viable target.
