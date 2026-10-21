# The single bridge (GBP), made concrete; the convergence of all RH routes onto GRH_N

**Script:** `empirical/verify_gbp_bridge.py`  (reads the Direction B roadmap + Unconditional-Positivity-Synthesis).
**Finding:** every RH route the program built -- Paper 22 Lemma 8.1c, Direction B (B-2) arch dominance,
(GBP) |Sigma|^2=u_B, front (a), Selberg/Siegel -- converges to ONE bridge = Apex Lemma_HJ at primorial N
= GRH_N (proven equivalent, Pass-5 Thm 16.2). UNCONDITIONAL + real: the arch side is a positive atomic
measure (Thm 1, H_n^arch>=0 verified), |Sigma|^2>=0 free, the Bures Poisson field u_B=Im[-Xi'/Xi(xi+iy)]
>=0 <=> RH (computed, positive at tested heights). (GBP) forces the free Gram positivity onto u_B>=0=RH;
the residual is the IDENTIFICATION = the explicit formula = GRH_N. No solo shortcut. Genuine work: (B-1)
C*<=2.80 (Polymath), the (GBP) five-error audit. NO RH claim; the contribution is locating + concretizing.
**Nature:** numerical (mpmath) + literature synthesis; conservation confirmed, the bridge made concrete.

```text
The single bridge, made concrete: (GBP) = "the unconditional Gram positivity equals the Bures Poisson
field", and the convergence of ALL the program's RH routes onto it (= GRH_N).

The director's brief (Unconditional-Positivity-Synthesis) states it outright: Apex Lemma_HJ at primorial N
<=> GRH_N (Pass-5 Thm 16.2, both directions rigorous); the single remaining identification is

   (GBP):   |Sigma|^2/(2 pi) d_xi   =   u_B(xi, y) d_xi   on R, for each y>0,

where the LHS is the UNCONDITIONAL Gram-Bochner spectral density (a squared norm, >= 0 for free) and
   u_B(xi,y) = Im m_B(xi+iy),   m_B(z) = -Xi'/Xi(z),   Xi(z)=xi(1/2+iz)   (the Bures Poisson / Herglotz field).
Because |Sigma|^2 >= 0 unconditionally, the IDENTIFICATION forces u_B >= 0; and u_B(xi,y) >= 0 for all xi and
all y>0  <=>  m_B is Herglotz  <=>  Xi has no zero off the real xi-axis  <=>  RH. So (GBP) routes the free
positivity of the Gram side onto the zeros. The residual is exactly the IDENTIFICATION (the explicit formula
Xi'/Xi vs the prime-power sampling kernel of Psi_n) -- which is GRH_N, conserved.

CONVERGENCE (every route this program built ends here, one wall):
  * Paper 22 Lemma 8.1c : uniform character PNT mod P_n  =  no Siegel zero / GRH-family.
  * Direction B (B-2)  : arch Hankel (Thm 1 positive atomic measure, UNCONDITIONAL) must dominate the
                          indefinite prime Hankel  <=>  GRH_N.
  * (GBP) (this note)  : |Sigma|^2 = u_B  =>  u_B >= 0  =  RH.
  * front (a) / Selberg-Siegel / Lehmer : the average->individual / no-exceptional-zero guarantee.
  ALL are GRH_N. The arch/Gram positivity is REAL and unconditional (Thm 1: positive atomic measure on
  (-inf,0); |Sigma|^2 >= 0); the single missing step is the identification = the prime side = GRH_N.

THIS PROBE: (A) compute u_B(xi,y) = Im[-Xi'/Xi(xi+iy)] on a grid near the first zeros; verify u_B >= 0
  (Herglotz = RH-up-to-height) and that it is the POSITIVE POISSON FIELD of the zeros (a positive kernel
  per zero, peaks at xi=gamma_k); exhibit that an off-axis zero would drive u_B < 0 (the only way RH fails).
  (B) verify the arch side is an explicit POSITIVE atomic measure (Thm 1): atoms -4/(2m+1)^2, its Hankel
  H_n^arch >= 0 -- the unconditional half. (C) the honest verdict: one bridge, RH-equivalent, no shortcut.
NUMERICAL (mpmath); NO claim RH is proved -- this LOCATES and CONCRETIZES the single bridge.

================  PART A: u_B(xi,y) = Im[-Xi'/Xi(xi+iy)]  -- the (GBP) Bures Poisson field  ===
  y=1.0 : u_B over a xi-grid (should be >= 0 everywhere -- Herglotz/RH -- peaking at the zeros):
     xi        u_B(xi,y)        near zero?
        8.0    0.06963674        
    14.1347    1.06714         <- zero gamma=14.13472
       17.0    0.2245168        
     21.022    1.134521         <- zero gamma=21.02204
     25.011    1.159727         <- zero gamma=25.01086
       28.0    0.3643848        
       33.0    1.261855        
     min u_B over grid = 0.0696367  (>= 0: RH-consistent at this height; the field is the positive
     Poisson sum of the zeros).  An off-axis zero z0 (Im z0 != 0) gives -Xi'/Xi ~ -1/(z-z0),
     whose Im DIPS BELOW 0 near z0 -- so u_B>=0 everywhere is EXACTLY 'no off-axis zero' = RH.

  y=0.5 : u_B over a xi-grid (should be >= 0 everywhere -- Herglotz/RH -- peaking at the zeros):
     xi        u_B(xi,y)        near zero?
        8.0    0.03509953        
    14.1347    2.033772         <- zero gamma=14.13472
       17.0    0.118514        
     21.022    2.068873         <- zero gamma=21.02204
     25.011    2.081803         <- zero gamma=25.01086
       28.0    0.1960306        
       33.0    2.108048        
     min u_B over grid = 0.0350995  (>= 0: RH-consistent at this height; the field is the positive
     Poisson sum of the zeros).  An off-axis zero z0 (Im z0 != 0) gives -Xi'/Xi ~ -1/(z-z0),
     whose Im DIPS BELOW 0 near z0 -- so u_B>=0 everywhere is EXACTLY 'no off-axis zero' = RH.

  Poisson-field check: u_B(gamma_1, y) should grow like 1/y as y->0 (the kernel spike at the zero):
     y=1.0 : u_B(gamma_1,y) = 1.06714   (y*u_B = 1.06714 -> the residue/weight at the zero)
     y=0.5 : u_B(gamma_1,y) = 2.033773   (y*u_B = 1.01689 -> the residue/weight at the zero)
     y=0.25 : u_B(gamma_1,y) = 4.016912   (y*u_B = 1.00423 -> the residue/weight at the zero)
  => u_B is the positive Poisson field of the zero spectrum: the (GBP) RHS, >= 0 iff RH.

================  PART B: the arch side is an explicit POSITIVE atomic measure (Thm 1)  =======
  ArchStruct Thm 1: mu_k^{arch,joint}(N) = sum_{m>=0} M_{2m+1} (-4/(2m+1)^2)^k = int s^k dsigma_N^arch,
  a POSITIVE atomic measure on (-inf,0) with atoms s_m=-4/(2m+1)^2 and masses M_{2m+1}>=0 (for
  primorial N>=30, since M_1=-2+2 N_E>=0). Hence H_n^arch >= 0, J_n^arch <= 0 -- UNCONDITIONAL (Cor 2).
  Demonstrate (uniform masses M=1, the structural skeleton): the atoms and the Hankel positivity.
     first atoms s_m = -4/(2m+1)^2 : -4.0, -0.44444, -0.16, -0.081633, -0.049383 ...
     n=3 : H_n^arch (Hankel of the positive atomic measure) lambda_min = 0.00116322  (>=0: positive)
     n=5 : H_n^arch (Hankel of the positive atomic measure) lambda_min = 2.00032e-9  (>=0: positive)
     n=7 : H_n^arch (Hankel of the positive atomic measure) lambda_min = 8.26133e-17  (>=0: positive)
  => the arch Hankel is positive semidefinite (Stieltjes: Hankel of a positive measure). This is the
  UNCONDITIONAL half of Apex Lemma_HJ; the prime-side dominance is the GRH_N-equivalent residual.

================  PART C: one bridge, RH-equivalent -- the honest verdict  ================
CONVERGENCE (confirmed across the program, this session):
   Paper 22 Lemma 8.1c (uniform character PNT mod P_n, no Siegel)  =
   Direction B (B-2) arch-dominance (arch positive Hankel dominates the indefinite prime side)  =
   (GBP) |Sigma|^2 = u_B  (free Gram positivity forced onto u_B>=0)  =
   front (a) statistical->individual  =  Selberg lambda_1>=1/4  =  Lehmer individual repulsion
   =  Apex Lemma_HJ at primorial N  =  GRH_N.   (Pass-5 Thm 16.2: rigorous both directions.)

WHAT IS UNCONDITIONAL AND REAL (the program's genuine content):
  * the arch side is an explicit POSITIVE atomic measure (Thm 1) -> H_n^arch>=0 (verified PART B);
  * the Gram-Bochner side |Sigma|^2>=0 is a squared norm (free);
  * the Bures Poisson field u_B is the de Branges/Herglotz object, u_B>=0 <=> RH (PART A);
  * U1-U6 (six unconditional positivity facts) + the finite primorial tower (cubic..quintic, the
    cross-prime cancellation general theorem, finite leakage extinction) -- all settled this session.

WHERE CONSERVATION BITES (the single bridge, no shortcut):
  (GBP) = the IDENTIFICATION |Sigma|^2 = u_B = the explicit formula (Xi'/Xi vs the prime-power kernel
  Psi_n) = the arch-dominates-prime step = uniform-no-Siegel mod P_n. It is RH/GRH_N, PROVEN
  equivalent (not conjectured). No non-circular move closes it; that is conservation of difficulty,
  and the director's brief states it: 'cannot be made unconditional without proving GRH_N'.

THE HONEST ATTACK SURFACE (genuine work, none a solo closure):
  1. (B-1) primorial-indexed BV at theta_0=1-C*/n, verify C* <= 2.80 (diez sec 3) -- Polymath-8-scale
     specialist analytic NT; the smooth/primorial moduli admit Zhang/Polymath dispersion beyond 1/2,
     but theta_0->1 as n->inf is the Elliott-Halberstam/GRH limit.
  2. the (GBP) five-error identification audit (Paper III sec 9: E_occ,E_cut,E_CRT,E_win,E_leak):
     each has an unconditional bound; the step COMBINING them into (GBP) is the residual -- audit
     which steps are rigorous vs stated-not-proven, to isolate the precise identification gap.
  3. community / Polymath engagement (the roadmap's own conclusion: 'Go Polymath').

VERDICT: the program has done the maximal honest thing -- cornered RH to ONE named, RH-equivalent
bridge (GBP)=GRH_N, with substantial UNCONDITIONAL scaffolding (arch positivity, the finite tower,
U1-U6) assembled around it. There is no solo shortcut to close it. The genuine next moves are the
Polymath (B-1) constant and the (GBP) five-error audit -- real work, not a closure. Conservation holds.
```

## Addendum (2026-10-07): re-scope after the quasi-GRH half-plane (OpenAI 2026)

Input, tier [A]: OpenAI, *The Quasi-Riemann Hypothesis* (30 Sep 2026, github.com/openai/math, family 003,
Thm 1.1).  Every Dirichlet L(s,chi) is zero-free in Re s > 7/8, uniformly in the modulus.  It is
model-generated, and OpenAI reports Lean formalization.  The functional equation then gives
1/8 <= beta <= 7/8 for every nontrivial zero, with no exceptional (Siegel) zero for any q.

**This report.**  The identification "Paper 22 Lemma 8.1c = uniform character PNT mod P_n = no Siegel
zero / GRH-family" is CORRECTED.  8.1c needs only a fixed half-plane theta < 1, not GRH.  It is now [A] on
OpenAI 2026 (Paper 22 Proposition 8.1c': |psi(X,chi) - delta X| << X^(7/8) log^2(P_n X)).  So 8.1c no
longer converges onto the GRH_N bridge.  The other routes listed (Direction B arch dominance, (GBP)
|Sigma|^2 = u_B, u_B >= 0) concern zeros ON the critical line and are untouched.  The bridge = GRH_N = RH
residual stands for them.  Also, "conservation confirmed" is withdrawn as a summary: one of the routes
collapsed onto a strip statement, which is a strictly easier target.
