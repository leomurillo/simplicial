# Attempt to prove W_H tends to zero

Status: no proof obtained. The limit identity and the transfer identities below are proved. The candidate pointwise contraction mechanism fails. Do not cite the necessary concentration balance as sufficient for Collatz.

## 1. What can be proved about the limit

Let B_H be the capped basin of 1 and w(n)=1/[n(n+1)]. The sets B_H increase. Put B=union_H B_H and A=N_positive minus B. Then A is exactly the set of starts that never reach 1.

**Theorem 1.**

    lim_{H->infinity} W_H = sum_{n in A} 1/[n(n+1)].   (1)

**Proof.** The indicators 1_{n not in B_H} decrease pointwise to 1_{n in A}. They are dominated by the summable weights w(n), whose total is 1. Dominated convergence for the series gives (1). Equivalently, one may separate a finite initial sum and use the uniform tail bound sum_{n>N}w(n)=1/(N+1). QED.

Every summand on the right is strictly positive. Consequently proving that the limit vanishes requires excluding every element of A. Neither monotonicity nor dominated convergence supplies that exclusion; they identify the limit but do not set it to zero.

## 2. Test the natural inverse transfer

Stop the standard map at 1. For states m>=2 define the killed inverse transfer

    (Kf)(m)=sum_{n>=2 : T(n)=m} f(n).

For m>=5 the exact inverse formula is

    (Kw)(m)=w(2m)+1_{m=4 mod 6} w((m-1)/3).

Dividing by w(m) gives

    R(m)=(m+1)/[2(2m+1)]
          +1_{m=4 mod 6} 9m(m+1)/[(m-1)(m+2)].       (2)

Off the live residue class, R(m) approaches 1/4. On it, R(m) approaches 37/4, which is 9.25. Thus this weight is not pointwise contracting; the inverse odd branch overwhelms the halving branch on some rows. The issue persists at arbitrarily large m, so discarding a finite verified range does not repair it.

## 3. No fixed even iterate repairs pointwise contraction

**Proposition 2.** For every r>=1 and arbitrarily large positive n,m,

    T^{2r}(n)=m,
    (K^{2r}w)(m)/w(m) > (3/2)^{2r}>1.                (3)

**Proof.** Choose any positive integer L and put

    n=2^{r+1}L-1,   m=2*3^r L-1.

The first r odd-only steps all have exactly one halving, since their successive odd values are 3^j 2^{r+1-j} L-1, which are 3 mod 4 for j<r. They never reach 1 and use 2r standard steps. Hence their contribution alone gives (K^{2r}w)(m)>=w(n). Writing lambda=(3/2)^r, we have m+1=lambda(n+1) and m>lambda*n. Therefore

    w(n)/w(m)=m(m+1)/[n(n+1)]>lambda^2.

Letting L grow makes both states arbitrarily large. QED.

In particular there is no k>=1 and q<1 with K^k w<=q w pointwise: positivity would imply K^{2k}w<=q^2 w, contradicting (3). This does not rule out adaptive methods, different weights, or decay of the particular initial distribution. It rules out this specific uniform pointwise route.

## 4. A hypothetical exceptional set must balance the live rows

If A is nonempty, membership is invariant under the forward map and under all legal inverse branches. Summing nonnegative series therefore gives

    sum_{m in A} (Kw)(m)=sum_{m in A} w(m)=W_infinity. (4)

Let M=min A. The small starts are directly verified to converge, so we may suppose M>=5. Normalize w on A to a probability distribution pi(m)=w(m)/W_infinity. Equations (2) and (4) imply

    E_pi[R(m)]=1.                                    (5)

Let p=pi({m:m=4 mod 6}). Rewrite the two coefficients as

    a(m)=1/4+1/(8m+4),
    b(m)=9+18/(m^2+m-2).

Then (5) is exactly 1=E_pi[a]+E_pi[b 1_live]. In particular

    [1-(1/4+1/(8M+4))]/[9+18/(M^2+M-2)] <= p < 1/12. (6)

These inequalities follow from bounding a,b on m>=M. Thus any nonempty exceptional set with a large least member must put a very precise fraction of its weighted mass on the live rows, close to 1/12 from below.

This is a necessary balance, not a contradiction. One cannot replace pi by a uniform distribution on residue classes: pi is supported on the unknown exceptional set and may be highly nonuniform. Proving that the actual arithmetic forbids this balance would be new input, and is not accomplished here.

## 5. Finite estimates and the remaining gap

The verifier computes rigorous rational intervals for W_H at selected finite heights. It uses denominator 2^100, rounds each positive summand downward, and adds one unit per summand to obtain an upper bound. The infinite tail is exactly 1/(H+1) and is included. This avoids interpreting floating-point cancellation as a zero deficit.

Such estimates only bound W_infinity from above. An arbitrarily large finite verification does not establish its value is zero. A nonempty exceptional set with a sufficiently large minimum could have extremely small, but still positive, weight.

The proof attempt therefore stops at an identifiable failure: inverse branching does not yield a uniform contraction for w, and the remaining weighted live-row balance is compatible with the inequalities established so far. The universal weighted-coverage estimate from the preceding note remains unproved.

Reproduce with `python empirical_01g/weighted_basin_contraction_audit.py`. Its JSON contains exact row ratios, 90 expanding-path checks, and rational intervals for four finite ceilings.
