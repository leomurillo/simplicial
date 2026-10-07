# Front (b): the integrality that would force R(0) < 1 strict

**Script:** `empirical/verify_integrality_forcing.py`
**Context:** front (b); the third input = an integer-valued count (Hasse gap / spectral count).
**Finding:** function-field margin 4q-a^2 is an integer >= 1 (strict); number-field 1-R(0) has no
integer floor; the candidate third input is the integer zero-count N(T) = #eigenvalues of front (a)'s H.
**Nature:** exact integer point counts + mpmath; labelled.  NOT a proof.

```text
Front (b): the integrality that would force the marginal R(0) <= 1 to be STRICT (R(0) < 1).

Diagnosis (from the proof-strategy synthesis): soft/analytic methods are symmetric under RH-true/false
near the line, hence MARGINAL (R(0) ~ 0.9999, never strict).  A proof needs a THIRD input that breaks
the symmetry.  Over function fields that input is INTEGRALITY: integer point counts -> integer
Frobenius trace a -> the Hasse bound a^2 <= 4q is an INTEGER inequality, so its violation would be a
NEGATIVE INTEGER (<= -1) -- strictness is automatic, the margin can never be a tiny positive number.

PART A -- the function-field integer protection (the template, [P] in-house, P4/פWeil):
  Fermat cubic C: x^3+y^3+z^3=0 over F_q.  a = q+1 - #C(F_q) (integer, exact point count).
  RH-for-the-curve = |alpha|=sqrt(q) <=> 4q - a^2 >= 0 (Hasse).  The margin 4q-a^2 is an INTEGER >= 1
  for ordinary q -- it CANNOT be marginal.  And q = N(J) = a'^2 - a'b' + b'^2 (Eisenstein-integer
  norm of the Jacobi sum): sqrt(q) is an ALGEBRAIC identity, not an analytic limit.

PART B -- the number-field count integrality (the candidate third input; Turing / Lefschetz analogue):
  N(T) = #{zeros up to T} is an INTEGER.  Riemann-von Mangoldt: N(T) = theta(T)/pi + 1 + S(T), with
  theta the Riemann-Siegel theta (the archimedean/Gamma phase, NON-integer/continuous) and
  S(T) = (1/pi) arg zeta(1/2+iT) the fluctuation.  The integer count is the rigidity: at each zero N
  jumps by +1.  RH <=> (on-line count) = (total count) for all T.  Since both are INTEGERS, an
  analytic near-miss |on-line - total| < 1 would force EXACT equality (this is Turing's method, which
  proves RH in finite ranges).  The obstruction to all T is a uniform S(T) bound -- which is RH.

PART C -- contrast + unification with front (a):
  function field: margin 4q-a^2 is an INTEGER >= 1 (strict, protected).
  number field:   1 - R(0) ~ 0.0003 (cumulant corner) -- CONTINUOUS, -> 0, NO integer floor; and the
  primorial Hankel minor D_3 = -787680 is an integer but NEGATIVE (the smooth primorial is the wrong
  object, P6).  The third input = an integer-valued spectral count: front (a)'s operator H, if
  self-adjoint, makes N(T) = #eigenvalues an integer automatically -- the integrality IS the operator.
  Fronts (a) and (b) are the same: the operator supplies the integer count; the count rigidity forces
  the marginal R(0) < 1 strict; both = RH.

NUMERICAL/EXACT (mpmath + exact integer point counts), labelled.  NOT a proof.

================  PART A : function field -- the Hasse margin is an INTEGER >= 1  ==========
   q   type        #C(F_q)   a=q+1-#C   4q-a^2 (margin, INTEGER)   q=a'^2-a'b'+b'^2 (Eisenstein)
   5   inert(ss)       6       +0          20  (>=1, strict)        (inert: q=N(q))
   7   split(ord)      9       -1          27  (>=1, strict)        -3^2--3*-2+-2^2=7
  11   inert(ss)      12       +0          44  (>=1, strict)        (inert: q=N(q))
  13   split(ord)      9       +5          27  (>=1, strict)        -4^2--4*-3+-3^2=13
  17   inert(ss)      18       +0          68  (>=1, strict)        (inert: q=N(q))
  19   split(ord)     27       -7          27  (>=1, strict)        -5^2--5*-3+-3^2=19
  23   inert(ss)      24       +0          92  (>=1, strict)        (inert: q=N(q))
  29   inert(ss)      30       +0         116  (>=1, strict)        (inert: q=N(q))
  31   split(ord)     36       -4         108  (>=1, strict)        -6^2--6*-5+-5^2=31
  37   split(ord)     27      +11          27  (>=1, strict)        -7^2--7*-4+-4^2=37
  43   split(ord)     36       +8         108  (>=1, strict)        -7^2--7*-6+-6^2=43
  -> the positivity margin 4q-a^2 is a NON-NEGATIVE INTEGER; for ordinary q it is >= 1.
     It cannot be a tiny positive number: integrality makes RH-for-the-curve STRICT.
     (Supersingular q==2 mod 3: a=0 exactly, margin=4q.)  And q is an Eisenstein-integer
     norm -> sqrt(q) is an algebraic identity, not an analytic limit.

================  PART B : number field -- the zero count N(T) is an INTEGER  ==============
  N(T) = theta(T)/pi + 1 + S(T):  smooth archimedean phase (continuous) + integer count.
    T      N(T)=#zeros(int)   theta(T)/pi + 1 (smooth, NON-int)    S(T)=N - smooth
     30         3            3.564877444            -0.564877
     50        10            9.422914422            0.577086
    100        29            29.0024099            -0.0024099
    200        79            79.19328035            -0.19328
    500       269            269.5867309            -0.586731
  -> N(T) is an INTEGER; the smooth archimedean term is not; S(T) is the fluctuation that
     snaps the total to an integer.  The integer count is the rigidity (Turing's method:
     |on-line count - N(T)| < 1  =>  EXACT equality  =>  RH in that range).  The uniform-in-T
     version (a global S(T) bound) is RH -- the integer floor exists, the analytic bound is open.

================  PART C : the contrast, and why fronts (a)+(b) are one  ================
  function field:  margin = 4q - a^2  is an INTEGER >= 1   (strict, integer-protected).
  number field:    1 - R(0) ~ 0.0003  (cumulant corner)    CONTINUOUS, -> 0, NO integer floor;
                   primorial Hankel D_3 = -787680 is an integer but NEGATIVE (wrong object, P6).

  The third input that breaks the RH-true/false symmetry = an INTEGER-VALUED count.  Over F_q
  it is the Lefschetz/point count (Frobenius an endomorphism).  Over Q it is the spectral count
  N(T) = #eigenvalues of the Hilbert-Polya operator H (front a): if H is self-adjoint, N(T) is
  automatically an integer, and (on-line count)=(total count) is an INTEGER equality that a
  near-miss upgrades to exact.  So:
    FRONT (a) supplies the operator;  FRONT (b) = its integer spectral count is the integrality;
    the count rigidity forces the marginal R(0) < 1 to be STRICT.  Both fronts = the SAME RH.
  The archimedean integrality is the integer zero-count -- the number-field shadow of the
  function-field Lefschetz integer point count.  NOT a proof: the uniform analytic bound that
  would let integrality close it (global S(T), or self-adjointness of H) is RH itself.
```
