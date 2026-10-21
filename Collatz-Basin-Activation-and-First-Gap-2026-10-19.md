# Basin activation and the first-gap obstruction

Status: exact activation theorem and finite census through height one million. This attack does not prove universal coverage. The weighted criterion below is explicitly an equivalent reformulation with an unproved sufficient estimate, not a new solution.

## 1. Activation has an exact local rule

Use the standard Collatz map, stopped on first reaching 1. Let B_H be the set of starts whose stopped trajectories reach 1 while remaining <=H. Put B_1={1}. Let A_H=B_H minus B_(H-1).

**Theorem 1.** For H>1:

* If H is odd, A_H is empty.
* If H is even, A_H is nonempty exactly when H/2 belongs to B_(H-1).
* In that case A_H is obtained by adding H and recursively adding its legal predecessors <=H that are not already in B_(H-1).

Legal predecessors of x are 2x and, if x=4 mod 6, (x-1)/3; exclude the odd predecessor 1 because the stopped map treats 1 as terminal.

**Proof.** Any newly admitted trajectory must visit H. For odd H>1 the next value is 3H+1>H, which is impossible. For even H it next visits H/2. If H/2 subsequently revisited H before reaching 1, determinism would give a cycle avoiding 1; therefore it must reach 1 entirely below H. This proves necessity. Conversely a path from H/2 below H certifies H, and every bounded predecessor path to H also becomes certified. Reversing all such paths proves the recursive description. QED.

**Corollary 2.** For H>4, a jump admitting more than one start is possible only at H=4 mod 12.

**Proof.** The only predecessor of H inside [1,H] besides the exceptional already-admitted terminal case is (H-1)/3, requiring H=4 mod 6. Also H cannot be twice an odd number >1: the next two steps would send H to H/2 and then 3H/2+1>H. Thus 4 divides H. Combining the congruences gives H=4 mod 12. QED.

The congruence is necessary, not sufficient. The actual activation test remains whether H/2 already belongs to the smaller basin. This is why prime factorization of the crest alone cannot determine the jump.

## 2. A terminating construction of every finite basin

Increase H one at a time. If H is even and H/2 is marked, mark H and propagate backwards through legal predecessors below the ceiling. Otherwise add nothing. Each vertex is marked at most once. Maintain also

    mu(H)=min{n>=1 : n not in B_H}.

This algorithm never follows an unbounded forward trajectory and never assumes Collatz. Its finite output is certified by explicit paths to 1. The implementation checked every ceiling through one million and independently compared eight selected outputs with full capped inverse searches.

| Ceiling H | Basin size | First missing start mu(H) |
|---:|---:|---:|
| 160 | 77 | 27 |
| 9231 | 2367 | 27 |
| 9232 | 3946 | 255 |
| 13120 | 5478 | 447 |
| 250504 | 100045 | 1819 |
| 500000 | 198411 | 1819 |
| 1000000 | 397068 | 1819 |

Here missing means missing under that height ceiling, not nonconvergent. In particular 1819 reaches 1, but its peak is 1276936, beyond these last ceilings.

The largest tested jump that did not advance the first gap occurs at H=975400: 848 new starts are admitted, but mu stays at 1819. Thus even conspicuous jumps cannot be treated as automatic progress toward the earliest missing integer.

At 9232, in contrast, the same event both admits a large group and moves the first gap from 27 to 255. This distinction explains its particular importance in the plot.

## 3. The universal quantifier is visible

**Proposition 3.** Collatz is equivalent to mu(H)->infinity as H->infinity.

**Proof.** If every start reaches 1, any finite set of starts has a finite maximum of its finite peak heights, so eventually every member of that set lies in B_H. Conversely, if mu(H) tends to infinity, every fixed n lies in some B_H and therefore reaches 1. QED.

Unbounded basin size is much weaker: powers of two alone already give unbounded size. Even a large positive proportion of covered starts need not include every fixed integer. A proof must prevent a permanent first gap, rather than only produce more admitted starts.

For a hypothetical permanent first gap n, all smaller integers eventually lie in a common finite B_H. If the orbit of n ever descended below n, its finite prefix plus that smaller integer's certified tail would put n in a larger basin, a contradiction. Thus a permanent gap is a genuine non-descending orbit, either eventually cycling away from 1 or escaping every finite ceiling. The earlier distinct-path repayment bound applies to the nonrepeating case, but does not force surplus growth by itself.

## 4. A first-gap-sensitive weight

Assign each integer the positive weight w(n)=1/[n(n+1)], whose total over n>=1 is 1. Define

    W_H=1-sum_{n in B_H} w(n)
       =sum_{n<=H, n not in B_H} w(n)+1/(H+1).

This is an exactly computable finite expression, including the full tail. It satisfies

    1/[mu(H)(mu(H)+1)] <= W_H <= 1/mu(H).

Hence W_H->0 is equivalent to Collatz. A fixed missing integer retains a fixed positive weight; adding many large starts cannot conceal it.

The exact gain at activation is

    W_(H-1)-W_H=sum_{n in A_H} 1/[n(n+1)].

With eta_H=(W_(H-1)-W_H)/W_(H-1), one has 0<=eta_H<1 and

    W_H=W_1 product_{h=2}^H(1-eta_h).

Since W_1=1/2, the product vanishes exactly when sum eta_h diverges. This is a restatement of the missing theorem, not evidence that it holds. It does identify why the size of A_H is the wrong quantity by itself: the activation must carry weight relevant to the persistent missing starts.

One sufficient, currently unproved, estimate would be

    sum_{H<n<=cH} sum_{r in A_n} w(r) >= epsilon_H W_H

along a geometric sequence of ceilings H, for fixed c>1, with sum epsilon_H=infinity and 0<=epsilon_H<1. This would force W to zero. No uniform estimate of this kind follows from the activation congruence or the finite census.

## 5. What the attack achieved

The bottleneck picture now has an exact growth rule, an arithmetic restriction on all multi-start jumps, and a concrete way to track the first gap. The computation rejects a tempting shortcut: large basin jumps can keep missing the earliest uncovered start. The remaining task is a deterministic weighted-coverage estimate, or a direct argument that a permanent first gap cannot survive. Neither is proved here.

Reproduce with `python empirical_01g/capped_basin_growth.py`. The JSON records all first-gap changes, mass records, snapshots, and the largest tested jump without first-gap progress.
