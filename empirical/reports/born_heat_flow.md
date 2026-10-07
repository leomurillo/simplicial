# Born-cone closure probe (RH-Pass3/4/5 Lock A): folded Xi Born ledger, trace, Apex gates

**Script:** `empirical/verify_born_heat_flow.py`
**Context:** RH <=> Lambda<=0 <=> the positive Born ledger of Xi_t survives heat removal t->0+;
Pass-5 Thm 16.2 makes the t=0 target the finite Hankel/Stieltjes gates H_n,J_n (mu_n=ell_{n+1}).
**Finding:** at the RH-true t=0 sample (true zeta zeros) the Born ledger B(x)=prod(1+gamma_k^{-2}x)
reproduces the RH-Pass3 section-14 cumulant table -- ell_2..ell_5 to <=1e-4 at K=200 zeros; ell_1
matches via the exact split -4+2.1497+1.8734=0.02310 (its K=200 partial undershoots, slow tail).
Trace ell_1 finite (no escape); bottom atom gamma_1^{-2} bounded from 0 (no dust); Apex gates
H_n,J_n are PSD by exact Gram construction (sum lambda_k v_k v_k^T), eig>=0 to conditioning floor.
The BINDING open
mode is PHASE LEAKAGE (a zero going complex at t->0): invisible to the trace/dust controls,
detected only by a finite Hankel gate (Pass-5 Lemma 16.4). No non-circular handle on Lambda<=0
from the Born/trace structure -- only Rodgers-Tao Lambda>=0 (the opposite inequality) is
unconditional; conservation of difficulty.
**Nature:** numerical/exact (mpmath, dps=30), labelled. NOT a proof (the t->0 closure IS RH).

```text
Born-cone closure probe (RH-Pass3/4/5 Lock A): the folded Xi Born ledger, its trace, and the
Apex Hankel/Stieltjes gates -- the EXACT objects the t->0+ no-loss step must deliver.

WHAT THIS IS.  RH-Pass4/5 reduce RH to "Lock A no-loss": for t > Lambda the heat-flowed Xi_t is
real-rooted, so its fold
    B_t(x) = Xi_t(i sqrt x)/Xi_t(0) = prod_k (1 + lambda_k(t) x),   lambda_k(t) = z_k(t)^{-2} > 0
is a POSITIVE Born factorization (Locks B,C FREE).  RH <=> this positive ledger survives heat removal
t->0+ inside the cone: (1) no trace escape sup_t ell_1(t)<inf, (2) no zero-dust tau_0({0})=0,
(3) no phase leakage (atoms stay real-positive), (4) no limit-order failure.  Rodgers-Tao (2018) give
Lambda>=0 (PROVEN, the OTHER inequality); RH <=> Lambda<=0 <=> the cone is retained to t=0.

Pass-5 Thm 16.2 makes the t=0 target EXPLICIT and finite: with mu_n := ell_{n+1} the folded cumulants
    ell_m = sum_rho z_rho^{-2m}      (unconditional Hadamard identity, z_rho the Xi-zeros),
RH  <=>  H_n = (mu_{a+b})_{0<=a,b<=n} >= 0  AND  J_n = (mu_{a+b+1})_{0<=a,b<=n} >= 0  for all n
     <=>  B'/B is a positive trace-weighted Stieltjes transform with no zero-dust.

THIS PROBE (numerical/exact, mpmath; NOT a proof -- the t->0 closure / all-n gate positivity IS RH):
  PART 0  get the true folded atoms lambda_k = gamma_k^{-2} from the genuine zeta zeros (t=0 sample).
  PART 1  BORN LEDGER & TRACE: B(x)=prod(1+lambda_k x); verify ell_m = sum lambda_k^m reproduces the
          Pass-3 section-14 cumulant table (ell_1~0.0231, ell_2~3.72e-5, ...); show trace ell_1<inf
          (no escape) and the bottom atom = gamma_1^{-2} bounded away from 0 (no dust).
  PART 2  APEX GATES at t=0: build H_n, J_n from mu_n=ell_{n+1} (truncated to K zeros) and report their
          minimum eigenvalues -- the Pass-5 Apex object.  Positive => the t=0 Born cone is occupied on
          the resolved window (RH-true sampling), i.e. the gates the no-loss step must keep positive.
  PART 3  the t>0 side & the binding failure mode: heat removal is the EASY direction WHILE zeros are
          real; the open content is that they STAY real through t=0 (Lambda<=0).  Identify the binding
          mode and state precisely why no trace/gate computation here is a non-circular handle.

HONESTY.  PART 0-2 sample at t=0 USING the true zeros (so positivity is RH-true by construction, not a
proof); they exhibit the exact target objects and confirm the algebra (cumulant table, Stieltjes form).
PART 3 states the irreducible gap.  Nothing here proves Lambda<=0.

===============  PART 0 : folded Born atoms lambda_k = gamma_k^{-2} (t=0, true zeros)  =====
  loading first 200 nontrivial zeta zeros gamma_k via mpmath.zetazero ...
  lowest atoms (= largest lambda):
     k=1  gamma_k=14.134725141735   lambda_k=gamma_k^{-2}=0.0050052441235941
     k=2  gamma_k=21.022039638772   lambda_k=gamma_k^{-2}=0.0022628215114696
     k=3  gamma_k=25.010857580146   lambda_k=gamma_k^{-2}=0.0015986111345899
     k=4  gamma_k=30.42487612586   lambda_k=gamma_k^{-2}=0.0010802949915558
     k=5  gamma_k=32.935061587739   lambda_k=gamma_k^{-2}=0.0009218983553513
  smallest used atom: lambda_200 = 6.36462e-6   (atoms DECREASE to 0; the bottom atom = gamma_1^{-2}
  is the LARGEST, bounded away from 0 -> no zero-dust at the top of the spectrum).

===============  PART 1 : Born ledger B(x)=prod(1+lambda_k x), trace, cumulant table  =====
  folded cumulant ell_m = sum_k lambda_k^m  vs  RH-Pass3 section-14 table:
     m     ell_m (this run, K=200)         Pass-3 table          rel.diff
     1   0.021044143520694   2.3104993e-2   0.0892
     2   3.7168815159436e-5   3.7172599e-5   0.000102
     3   1.4417391746061e-7   1.4417393e-7   8.7e-8
     4   6.6303168019081e-10   6.6303168e-10   2.88e-10
     5   3.2136641506163e-12   3.2136642e-12   1.54e-8
  -> ell_1 = TRACE = sum gamma_k^{-2}: partial(K=200)=0.021044144 UNDERSHOOTS the true 0.0231050 (slow
     tail); exact via Pass-3 split: ell_1^end + ell_1^inf + ell_1^zeta = -4 + 2.14966614 + 1.8734388
     = 0.0231050 -- FINITE either way (no trace escape).  m>=2 already match the table to <=1e-4.
  -> confirms B(x)=prod(1+gamma_k^{-2} x) and the trace identity ell_m = Tr(L_Xi^m) at the
     RH-true t=0 sample (algebra + Stieltjes form verified; ell_1 tail is a truncation artifact).

===============  PART 2 : Apex gates H_n, J_n at t=0 (Pass-5 Thm 16.2)  ====================
  mu_n := ell_{n+1};  H_n=(mu_{a+b}), J_n=(mu_{a+b+1}).  RH <=> H_n,J_n >=0 for ALL n.
  At the t=0 true-zero sample these MUST be >=0 (positivity is RH-true here by construction);
  we confirm it and report min-eigenvalues -- the finite objects the no-loss step must keep >=0.
       n   cond(H_n)     min eig H_n          min eig J_n        Gram PSD?
       0   1.0   0.0210441   3.71688e-5   yes (sum lam_k v_k v_k^T)
       1   2.68e+5   7.8525e-8   1.03795e-10   yes (sum lam_k v_k v_k^T)
       2   2.06e+11   1.02017e-13   8.06728e-17   yes (sum lam_k v_k v_k^T)
       3   4.31e+17   4.88534e-20   2.9506e-23   yes (sum lam_k v_k v_k^T)
       4   1.41e+24   1.49371e-26   8.45446e-30   yes (sum lam_k v_k v_k^T)
       5   5.78e+30   3.64248e-33   1.55376e-36   yes (sum lam_k v_k v_k^T)
  -> The H_n,J_n are PSD by EXACT construction (Gram sum of rank-1 lambda_k v_k v_k^T,
     lambda_k>0): that is the unconditional content.  Reported min-eigenvalues are >=0 down
     to the conditioning floor (cond(H_5)~1e30+; any |min eig| ~ 10^-(working dps) is noise,
     not a negative gate).  These H_n,J_n ARE the Pass-5 Apex gates; proving them >=0 for ALL
     n from the prime/Gamma jet F=B'/B (NOT from the zeros) is exactly RH.

===============  PART 3 : binding failure mode & non-circular handle (honest)  ============
  The four RH-Pass4 failure modes for the t->0+ Born limit, and their status:
    (1) TRACE ESCAPE   sup_t ell_1(t)=inf   -- EXCLUDED for t>0 by the L^2 kernel bound
                       (Pass-4 Thm 6.3: Tr L_{n,T,t} = Var of heat-smoothed ledger < inf).
    (2) POWER-SUM      lim p_m(t) != ell_m   -- this is the t>Lambda smoothed Plancherel /
        MISMATCH       explicit-formula identity (Pass-4 Thm 6.4); the conductor remainder
                       R_m^cond(n)=0 EXACTLY via the T3 selection rule sum(a_i-b_i)=0 mod P_n;
                       archimedean remainder = O(e^{-(m-1)T/2}).  Closed for fixed t>Lambda.
    (4) ZERO-DUST      tau_0({0})>0 (an e^{cx} factor) -- WASHED by B'/B -> 0 as x->+inf
                       (Pass-5 Lemma 12.1), once a positive Stieltjes rep is tied to B.
    (3) PHASE LEAKAGE  t=0 ledger EXITS the positive Born cone (a pair of zeros leaves the
                       real axis) -- NOT excluded by any of the above.   <== BINDING.

  BINDING MODE = PHASE LEAKAGE (3), equivalently Pass-5 'Born cone closure' (Plate IV).
  Why it is binding: (1),(2),(4) are all controlled for every t>Lambda and as remainders;
  they constrain MAGNITUDE (trace) and the s=0 edge (dust), neither of which sees a zero
  going complex.  A conjugate pair leaving R contributes a NEGATIVE/complex atom lambda=z^{-2}
  with bounded modulus -- ell_1 stays finite, no dust -- yet H_n loses positivity (Pass-5
  Lemma 16.4, the off-axis spectral isolator: a complex atom forces some finite Hankel gate
  H_n NOT >=0).  So the ONLY thing the no-loss step must secure is that NO atom goes complex
  as t crosses down through 0: exactly Lambda<=0.

  WHAT A PROOF OF NO-LOSS WOULD NEED: a positive cone retained ACROSS t=0 -- i.e. a Krein/
  de Branges canonical system H(t)>=0 with transfer matrix -> (Xi,-Xi') built from an input
  INDEPENDENT of assuming the zeros real (the arithmetic phase clock phi'>=0), OR equivalently
  the all-n gate positivity proved from the prime/Gamma jet F=B'/B (Pass-5 section 17.3), OR
  the archimedean local positivity (Connes-trace >= 0).  All three are RESTATEMENTS of RH.

  NON-CIRCULAR HANDLE on Lambda<=0 from the Born/trace structure?  NONE.  Positivity for
  t>Lambda + weak compactness reaches t=0 ONLY along a sequence t_j>Lambda with t_j->0, which
  EXISTS iff Lambda<=0 (Pass-5 section 15.1 Routes A-D are all circular for this reason).  The
  sole unconditional fact in this direction is Rodgers-Tao Lambda>=0 -- the OPPOSITE
  inequality.  The trace ledger is symmetric under a zero staying real vs going slightly
  complex at fixed small modulus, so it cannot break the marginality (the analytic face of
  Lambda=0 'RH barely true').  A handle must inject an arithmetic integrality / archimedean
  index NOT visible to the real-rooted t>0 flow -- conservation of difficulty, exactly.
```
