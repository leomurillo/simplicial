# What is special about 9232?

Status: exact local arithmetic and finite capped-basin structure, not a universal Collatz mechanism or a novelty claim.

## A large jump in the height-restricted basin

Let B_H be the positive starting integers whose standard Collatz trajectories reach 1 without ever exceeding H. This is a finite set inside [1,H]. It can be computed without assuming Collatz by exploring the legal inverse branches from 1, retaining only vertices <=H:

    x -> 2x,
    x -> (x-1)/3 when x=4 mod 6.

The exploration visits finitely many vertices. Its output is exactly B_H: every inverse path certifies a forward path to 1 within the ceiling, and every such forward path can be reversed.

The exact audit gives

    |B_9231|=2367,
    |B_9232|=3946,
    |B_9232 minus B_9231|=1579.

So adding one permitted height admits 1579 starting integers, a 66.7% increase over the previous basin size. The new group forms about 40.0% of the enlarged basin. This group is precisely the peak-9232 group seen as an arc in the exponent plot. Its smallest seed is 27.

Every newly admitted start visits 9232. Apart from starting at 9232 itself, the preceding value must be 3077: the only standard predecessors of 9232 are 18464 (outside the ceiling) and (9232-1)/3=3077. An independent capped inverse exploration from 3077 recovers exactly the other 1578 starts.

In this precise finite sense, 9232 is a height bottleneck for a large predecessor tree. The high visual prominence is not merely an accident of plotting, although the convex arc shape is caused by normalization.

## Local arithmetic at the crest

The relevant identities are

    3*3077+1=9232=2^4*577.

The standard orbit therefore executes four halvings after that odd step. The following odd-only segment is

    3077 -> 577 -> 433 -> 325 -> 61 -> 23,

with respective halving exponents (4,2,2,4,3). The standard tail from 9232 reaches 1 in 34 steps and never exceeds 9232. Starting from 577, the remaining standard peak is only 1732.

For this five-odd-step word the exact affine formula is

    U_w(x)=(243x+5953)/32768,

on its exact domain x=3077 mod 65536. Hence for every k>=0,

    3077+65536k -> 23+486k

under those five odd steps, giving strict descent. This is a genuine infinite arithmetic family, not just one numerical trajectory. It does not imply that every starting integer eventually enters this residue class.

The four halvings themselves are not unique: v_2(3x+1)=4 holds for every odd x=5 mod 32. Nor does primality of 577 enter the affine or congruence argument. The significance comes from the whole path and the size/minimum of its capped predecessor group, not from the factorization of 9232 alone.

## Comparison with other height bottlenecks

| Height H | Basin before H | Basin at H | Newly admitted | Least new seed |
|---:|---:|---:|---:|---:|
| 16 | 4 | 10 | 6 | 3 |
| 52 | 17 | 29 | 12 | 7 |
| 160 | 64 | 77 | 13 | 15 |
| 9232 | 2367 | 3946 | 1579 | 27 |
| 13120 | 5403 | 5478 | 75 | 255 |
| 250504 | 98286 | 100045 | 1759 | 703 |

These selected examples are not an exhaustive ranking of jumps. They show that the same mechanism occurs elsewhere, while 9232 combines a very small seed with a large group and a pronounced basin jump. This explains its influence on several correlated normalized metrics.

## The proof-facing question

Write r(H)=min(B_H minus B_(H-1)) whenever that difference is nonempty. The largest peak exponent in that group is log(H)/log(r(H)). For H=9232, r(H)=27.

A uniform estimate such as H<=r(H)^alpha would control peaks of all trajectories already known to reach 1. It would not by itself prove that every integer belongs to some B_H: the definition excludes divergent or nontrivially periodic trajectories. That coverage assertion is still Collatz. To exclude divergence by a universal height bound, the bound must apply to every forward orbit, including hypothetical counterexamples, not just the known basin.

The promising object is the increasing family of capped inverse basins and its jumps. A proof must explain why their union covers every positive integer, rather than merely describe their large finite components.

Reproduce with `python empirical_01g/peak_bottleneck_audit.py`. The adjacent JSON stores exact counts and the local five-step residue-family audit.
