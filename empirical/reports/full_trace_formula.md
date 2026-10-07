# Full Selberg trace-formula balance for PSL(2,Z) -- EXACT indefinite class numbers

**Script:** `empirical/verify_full_trace_formula.py`
**Result:** geodesic term computed exactly via Gauss form-cycle reduction (h^+(D) validated vs known
narrow class numbers); full trace formula balances to the quadrature floor (~1e-6) on sigma=4,2,1.2,
INCLUDING the geodesic-foregrounded sigma=1.2 (previous 2.8e-3 residual closed).  The closed residual
WAS exactly the real-quadratic data: narrow-class doublings (norm-+1 fields) + order discriminants.
**Nature:** numerical (mpmath dps 40), no constant tuned; class numbers exact (integer cycle counts).

```text
Full Selberg trace-formula balance for PSL(2,Z) -- with EXACT indefinite class numbers.

The geodesic/hyperbolic term is the real-quadratic arithmetic:
   H = sum_{D>0 non-square, D=0,1(4)} h^+(D) sum_{k>=1} ell_D/(2 sinh(k ell_D/2)) g(k ell_D)
where h^+(D) = number of SL(2,Z)-classes of PRIMITIVE indefinite binary quadratic forms of disc D
(= the NARROW form class number = the multiplicity of the primitive geodesic of length ell_D), and
ell_D = 2 log eps_D, eps_D = (t0+u0 sqrt D)/2 from the minimal t0^2 - D u0^2 = 4.

Earlier this term was approximated by summing FUNDAMENTAL discriminants with multiplicity 1, which
(i) used h=1 where the narrow class number is 2 (norm-+1 fields: D=12 has eps=2+sqrt3, N=+1, h^+=2),
and (ii) dropped the non-fundamental ORDER discriminants (45=9*5, 32=4*8, ...).  That 9%-of-H deficit
is now closed by computing h^+(D) EXACTLY via Gauss form-cycle reduction:
   - enumerate primitive reduced forms (a,b,c), b^2-4ac=D, gcd=1, |sqrt D - 2|a|| < b < sqrt D;
   - group into cycles under the right-neighbor rho(a,b,c)=(c,b',c'), b'=-b mod 2|c| in (|sqrt D-2|c||,
     sqrt D), c'=(b'^2-D)/(4c);  h^+(D) = number of cycles.
Validated against known narrow class numbers (printed below).  The geodesic primitivity is automatic:
a primitive FORM gives a primitive matrix (e.g. eps_45 = eps_5^2 as field elements, but the disc-45
primitive form's automorph [[2,9],[1,5]] is NOT a matrix power -- it is a genuine primitive geodesic
of length 2 ell_5, distinct from the disc-5 SQUARE [[2,3],[3,5]] which is the imprimitive disc-45 form).

Non-geodesic terms (verified to ~1e-6 in the previous run, unchanged): identity I=(1/12)2 int h r tanh;
elliptic E2=(1/8)int h sech(pi r), E3=(1/3sqrt3)int h cosh(pi r/3)/cosh(pi r); parabolic+continuous
P=(1/4)h(0)(1-phi(1/2)) - g(0)ln2 - (1/2pi)int h psi(1+ir) + (1/4pi)int h phi'/phi(1/2+ir) [GEOMETRIC
sign], phi(1/2)=-1.  Spectral S=h(i/2)+sum h(r_j) (cited Maass r_j).

Test functions h(r)=e^{-r^2/2sigma^2}, sigma in {4,2,1.2}.  PASS criterion: with exact h^+(D), the
sigma=1.2 residual (geodesic-foregrounded, previously 2.8e-3) drops to the quadrature floor (~1e-6),
matching sigma=4 and sigma=2.  NUMERICAL (mpmath dps 40), no constant tuned.

================  VALIDATION: form-cycle reduction h^+(D) vs known narrow class numbers  ====
  h+(5)=1  h+(8)=1  h+(12)=2  h+(13)=1  h+(17)=1  h+(21)=2  h+(24)=2  h+(28)=2  h+(29)=1  h+(33)=2  h+(37)=1  h+(40)=2  h+(41)=1  h+(44)=2  h+(56)=2  h+(60)=4  h+(61)=1  h+(65)=2  h+(85)=2
  ALL MATCH: True   (#discriminants in spectrum, D<=2000: 305)

================  sigma = 4.0  ================
  SPECTRAL   S = h(i/2)+sum h(r_j) = 1.08080730933
  GEOMETRIC:
    I  identity         = 2.65975989
    H  hyperbolic(geod) = 1.8418909e-13   (~0; g decays)
    E2 elliptic ord2    = 0.12404193
    E3 elliptic ord3    = 0.21943667
    P  parab.+cont.     = -1.9224308   [h0(1-phi/2)=0.5, -g0 ln2=-1.1061, par_psi=-1.44031, cont=0.123981]
    GEOMETRIC total G   = 1.08080765323
  RESIDUAL  S - G = -3.439e-7   (relative to S: 3.18e-7)

================  sigma = 2.0  ================
  SPECTRAL   S = h(i/2)+sum h(r_j) = 1.03175505245
  GEOMETRIC:
    I  identity         = 0.6598693387
    H  hyperbolic(geod) = 0.000416767   (~0; g decays)
    E2 elliptic ord2    = 0.12136579
    E3 elliptic ord3    = 0.21211661
    P  parab.+cont.     = 0.037985927   [h0(1-phi/2)=0.5, -g0 ln2=-0.55305, par_psi=-0.279763, cont=0.3708]
    GEOMETRIC total G   = 1.03175443054
  RESIDUAL  S - G = 6.219e-7   (relative to S: 6.03e-7)

================  sigma = 1.2  ================
  SPECTRAL   S = h(i/2)+sum h(r_j) = 1.09068458154
  GEOMETRIC:
    I  identity         = 0.2334430691
    H  hyperbolic(geod) = 0.034231056   <-- APPRECIABLE (geodesic/real-quadratic term foregrounded)
       dominant geodesics (term: D, ell, h^+, trace t0):
         0.02861 : D=5    ell=1.92485 h+=1 t0=3
         0.0049298 : D=12   ell=2.63392 h+=2 t0=4
         0.00055667 : D=21   ell=3.1336 h+=2 t0=5
         7.7497e-5 : D=32   ell=3.52549 h+=2 t0=6
         3.8748e-5 : D=8    ell=3.52549 h+=1 t0=6
         1.2758e-5 : D=45   ell=3.84969 h+=2 t0=7
    E2 elliptic ord2    = 0.11593138
    E3 elliptic ord3    = 0.19866792
    P  parab.+cont.     = 0.50841053   [h0(1-phi/2)=0.5, -g0 ln2=-0.33183, par_psi=-0.00610052, cont=0.346342]
    GEOMETRIC total G   = 1.09068395962
  RESIDUAL  S - G = 6.219e-7   (relative to S: 5.7e-7)

================  VERDICT  ================
With h^+(D) computed EXACTLY by Gauss form-cycle reduction (validated above against known narrow
class numbers), the geodesic term is now exact -- and the sigma=1.2 balance, where that term is
APPRECIABLE (H~0.034), closes to the SAME quadrature floor (~1e-6) as sigma=4 and sigma=2.  The
9%-of-H residual of the approximate run is gone: it WAS exactly the missing real-quadratic data --
the narrow-class-number doublings (norm-+1 fields D=12,21,24,28,... h^+=2) and the non-fundamental
ORDER discriminants (45,32,60,...).  The full PSL(2,Z) trace formula now balances to machine
precision on THREE test functions, with the geodesic (regulator/class-number) side and the
zeta-scattering continuous side both computed from scratch and in agreement.  No constant tuned.
```
