# First visibility attack: results and next proof target

17 October 2026

The standalone paper is `Collatz-Strict-Level-Improvement-Draft1.md`. It includes all proof dependencies rather than assuming attainment or positivity of the nonlinear eigenvector.

## Analytic results of this pass

1. The strict-increase argument extends to every k>=2. The finite eigenvector exists by Brouwer; the doubling cycle makes it positive. The policy minimum gives continuity and attainment without assuming monotonicity in the exponent parameter.
2. The retention formula simplifies exactly to R(gamma)=3(1-2^(-gamma))/(3/2)^gamma. Its derivative is at least log(4/3)>1/4 on [0,1], by an elementary inequality. This supplies an analytic replacement for the sampled derivative check.
3. The Haar gain is exactly H_k=(3/2)^gamma_k (1-rho_k)/3, rather than only bounded below by a multiple of the loss.
4. A correction descending to the previous residue level cannot have a positive visibility margin. This is proved by pairing the descended inequality with a critical lower-level policy's left eigenvector. It rules out all fixed low-digit correction formulas once the level is high enough.

## Computation

An independent implementation recomputed levels k=2 through 6 and solved the coordinate program Phi(v)>=v+epsilon*c, 0<=v<=c. Unrestricted vectors gave epsilon about 66–77% of the numerical G_k. Five saved vector pairs are in `empirical_01g/kl/visibility_potential_k*.npz`.

A separate verifier then checked 2,178 live-row inequalities using exact rational arithmetic and elementary series bounds for the two transcendental weights. All passed after reducing the trial epsilon by 10^(-9). These certify positive margins at the five specified rational exponent parameters, not at a certified enclosure of the exact critical exponents.

Restricted formulas depending only on old digits, only on v_3(r+1), or on the top digit together with one or two low digits gave zero numerical margin, except where the representation was already unrestricted at k=2. The old-digit failure is a theorem; the other failures are finite numerical observations.

## What this changes

The remaining task is not to make the left Perron vector approximately uniform. It is to construct a new-digit-dependent subeigenvector with a controlled positive margin. The finite coordinate certificate is another form of the original feasibility problem, so its existence at fixed levels is not by itself a new asymptotic theorem.

The next productive search should preserve the middle-digit carry information lost by the failed compact formulas. Candidate features include the transport of the revealed digit under repeated doubling and the alignment defect of the affine map 4x+1. Any fitted formula must be checked on levels not used to fit it. The success criterion is a symbolic bound surviving all levels, or a dyadic-block lower bound on visibility; a larger unrestricted optimization alone is insufficient.

## Literature and publication boundary

The accessible original Krasikov–Lagarias preprint explicitly states the strict-monotonicity question in Section 6, page 17 of the PDF: https://arxiv.org/pdf/math/0205002 . Its main feasibility theorem and inequalities were checked. The latest Nikpour–Rabbani full text remains unavailable in this session; the draft therefore does not claim established priority.

No external messages were sent and nothing was submitted. Existing manuscripts and checker files were left unchanged. This is a completed first paper-and-certificate research pass, not a proof that gamma_k tends to one.
