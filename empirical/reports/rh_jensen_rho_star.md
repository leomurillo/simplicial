# Stress-test of the 'RH <=> rho* < 1' micro-claim on the Jensen cumulant head

**Script:** `empirical/verify_jensen_rho_star.py`  (extends `verify_jensen_lp.py` from k<=8 to k<=30).
**Purpose:** verify or refute a subagent's proposed rate criterion rho* = lim_d M(d)/M(d-1), M(d)=1-r_d(0).
**Nature:** numerical (mpmath dps 60); checks a claim, proves nothing about RH.

```text
STRESS-TEST of the subagent's micro-claim "RH <=> rho* < 1" on the Jensen cumulant head.

Setup (matched to verify_jensen_lp.py): Phi = Polya kernel; a_n = int_0^inf t^{2n} Phi dt (moments);
A_n = log a_n; C_n = log(n!/(2n)!) (archimedean Gamma engine); r_k(0) = |Delta^k A_0| / |Delta^k C_0|
(finite differences at the head n=0).  GOR / program frontier: RH <=> sup_{k>=3,n} r_k(n) < 1, and
R(0) := lim_{k->inf} r_k(0) is the dominant corner (the subagent extrapolated R(0) ~ 0.99972 from k<=8).
The subagent further proposed M(d) := 1 - r_d(0), rho* := lim_d M(d)/M(d-1), and claimed "RH <=> rho* < 1".

DOUBT (to test): if R(0) < 1 STRICTLY, then M(d) -> (1 - R(0)) > 0, a POSITIVE constant, so
M(d)/M(d-1) -> 1 necessarily; the rho* < 1 the subagent saw at k<=8 is just the transient while M(d)
is still falling toward its positive floor.  In that case "RH <=> rho* < 1" is INVERTED/ill-posed.
This script computes r_k(0) for k up to 30 at high precision and reads off the TRUE behavior:
  - does r_k(0) converge to a limit R(0), and is R(0) < 1, = 1, or > 1 ?
  - does M(d) -> a positive floor (=> rho* -> 1) or -> 0 ?
  - is rho* a meaningful RH separator, or an artifact ?

NUMERICAL (mpmath dps 60), honest: this CHECKS a subagent claim; it does not prove anything about RH.

Computing 33 Phi-moments at dps=60 ...
  a_0..a_4 = 0.12428, 0.00574299, 0.000740712, 0.000149824, 4.02416e-5
  all moments positive: True

================  r_k(0) = |Delta^k A_0| / |Delta^k C_0|, k = 2 .. 30  ================
    k     r_k(0)            M(k)=1-r_k(0)      M(k)/M(k-1)
     2   0.9343030457     0.065696954     
     3   0.9807386702     0.01926133     0.293185
     4   0.9919023851     0.0080976149     0.420408
     5   0.9959210737     0.0040789263     0.503719
     6   0.9977041672     0.0022958328     0.562852
     7   0.9986055849     0.0013944151     0.607368
     8   0.9991042692     0.00089573077     0.64237
     9   0.9993991305     0.00060086954     0.670815
    10   0.9995826791     0.00041732088     0.694528
    11   0.9997017408     0.0002982592     0.7147
    12   0.9997816329     0.00021836708     0.732139
    13   0.9998367893     0.00016321067     0.747414
    14   0.9998758063     0.00012419371     0.760941
    15   0.9999039948     9.6005235e-5     0.773028
    16   0.9999247404     7.5259583e-5     0.783911
    17   0.9999402609     5.9739116e-5     0.793774
    18   0.9999520437     4.7956339e-5     0.802763
    19   0.9999611077     3.8892324e-5     0.810994
    20   0.9999681641     3.1835899e-5     0.818565
    21   0.9999737177     2.6282261e-5     0.825554
    22   0.9999781324     2.1867585e-5     0.832028
    23   0.999981674     1.8325988e-5     0.838043
    24   0.9999845393     1.5460678e-5     0.843648
    25   0.9999868757     1.3124294e-5     0.848882
    26   0.9999887947     1.1205293e-5     0.853783
    27   0.9999903816     9.618399e-6     0.85838
    28   0.9999917022     8.297808e-6     0.862702
    29   0.9999928077     7.1923033e-6     0.866771
    30   0.9999937383     6.2616976e-6     0.870611

================  READ-OFF  ================
  last 7 r_k(0): 0.99998454, 0.99998688, 0.99998879, 0.99999038, 0.9999917, 0.99999281, 0.99999374
  last increments r_{k}(0)-r_{k-1}(0): 2.3364e-6, 1.919e-6, 1.5869e-6, 1.3206e-6, 1.1055e-6, 9.3061e-7
  trend of r_k(0) near k=30: still INCREASING
  max over k<=30: r_30(0) = 0.9999937383   (< 1)

  VERDICT on the subagent's 'RH <=> rho* < 1':
    M(k)/M(k-1) over the last few k: 0.84888, 0.85378, 0.85838, 0.8627, 0.86677, 0.87061
    M(k) = 1 - r_k(0) stays POSITIVE; if it tends to a positive floor (1 - R(0)) then
    M(k)/M(k-1) -> 1 by construction, so 'rho* < 1' is NOT an RH separator -- it is the
    transient decay of M toward its floor.  The honest invariant remains R(0) <= 1, a VALUE,
    not a rate.  (If instead r_k(0) crosses 1, RH-on-this-tower would be FALSE at finite k --
    decisive; watch the flag column above.)
```
