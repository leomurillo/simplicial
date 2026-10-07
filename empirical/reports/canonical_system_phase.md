# The Krein/de Branges canonical system for E_B = Xi + i Xi', and the monotone phase clock

**Script:** `empirical/verify_canonical_system_phase.py`
**Context:** the concrete next step on front (a)/(b); H(t)=P_phi rank-1 (>=0 free), RH <=> phi'>=0.
**Finding:** the canonical Hamiltonian is explicit; H(t)>=0 collapses to phase-clock monotonicity
phi'(x)>=0; phi(T)/pi = N(T) ties it to the integer count; the open step is the arithmetic clock.
**Nature:** numerical (mpmath), labelled.  NOT a proof (the non-circular clock construction = RH).

```text
Concrete next step: the Krein/de Branges canonical system H(t) for E_B = Xi + i Xi', and the
exact reduction of "H(t) >= 0 independent of RH" to a monotone phase clock -- tying fronts (a)+(b).

de Branges/Krein.  A canonical system  J dM/dt = z H(t) M,  J = [[0,-1],[1,0]],  with a 2x2 real
H(t) >= 0, builds a chain of de Branges spaces H(E_t) with E_t Hermite-Biehler; the spectrum is real
(<=> the entire function is in Laguerre-Polya) iff H(t) >= 0 along the chain.  For zeta the correct
HB associate (HPo Addendum E, [P] identities) is the DERIVATIVE-POLARIZED
        E_B(z) = Xi(z) + i Xi'(z),   Xi(z) = xi(1/2 + i z)  (real, even, order 1),
with  |E_B|^2 - |E_B^*|^2 = 4 |Xi|^2 Im m_B,  m_B = -Xi'/Xi.  RH <=> E_B Hermite-Biehler <=> m_B
Herglotz <=> the de Branges measure is real-supported.

KEY STRUCTURAL FACT (the canonical system, explicitly).  In its natural (phase) parametrization the
trace-normalized Hamiltonian of this chain is the RANK-1 PROJECTOR
        H(t) = [[cos^2 phi, sin phi cos phi], [sin phi cos phi, sin^2 phi]] = P_{phi(t)},
        phi(x) = -arg E_B(x) = -atan2(Xi'(x), Xi(x))  (the increasing de Branges phase),
        clock:  dt = phi'(x) dx.
H(t) = P_phi is >= 0 AUTOMATICALLY (eigenvalues 0 and 1).  So the ENTIRE content of "H(t) >= 0" is
that  dt = phi'(x) dx  is a VALID (non-negative) reparametrization, i.e.
        phi'(x) >= 0    (the phase clock is monotone)   <=>   RH.
Closed form:  phi'(x) = (Xi'^2 - Xi Xi'') / (Xi^2 + Xi'^2)  (= 1 exactly at each zero of Xi).

This unifies the two fronts:
  * FRONT (a): phi' is built from the log-curvature m_B = -Xi'/Xi (the additive/Kubo-Mori object); the
    clock lives in the additive geometry where the zeros are curvature currents.
  * FRONT (b): the clock COUNTS -- phi(T)/pi = (number of real zeros up to T) = N(T), an INTEGER.
    RH <=> phi monotone <=> phi(T)/pi = N(T) (RvM total).  The integer count is the clock.

So "construct H(t) >= 0 independent of RH" = "construct the monotone phase clock phi'(x) >= 0 from the
ARITHMETIC (primes), without assuming the zeros are real."  That is the one open step = RH.  This
probe makes H(t) and the clock explicit and verifies, numerically (RH holds in range), that
phi' >= 0 and phi(T)/pi = N(T).  NOT a proof: the arithmetic construction of the clock is open.

NUMERICAL (mpmath), labelled.

================  PART 1 : H(t)=P_phi is rank-1 (>=0 free); content = phi'(x) >= 0 (clock)  ====
  phi'(x) = (Xi'^2 - Xi Xi'')/(Xi^2 + Xi'^2)   (de Branges phase velocity; = RH when >= 0):
     x        phi'(x)       (>=0 ?)        eig(H)=eig(P_phi)
      3.0    0.04740271     OK        {0, 1}
      7.0    0.05519793     OK        {0, 1}
     10.0    0.078710509     OK        {0, 1}
   14.1347    0.99997085     OK        {0, 1}
     17.0    0.19611488     OK        {0, 1}
   21.022    0.99994015     OK        {0, 1}
     25.0    0.98734136     OK        {0, 1}
     30.0    0.51408651     OK        {0, 1}
     40.0    0.43004527     OK        {0, 1}
     50.0    1.2499989     OK        {0, 1}
  H(t)=P_phi has eigenvalues {0,1} >= 0 for ALL t (rank-1 projector) -- positivity is FREE.
  phi'(x) >= 0 on every tested point: True   (the clock is monotone <=> RH, here numerically true)

================  PART 2 : the phase clock COUNTS -- phi(T)/pi = N(T) (integer, front b)  ======
  number of sign changes of Xi on (0,T]  vs  N(T)=#zeros (mpmath nzeros): should be EQUAL (RH).
     T     sign-changes of Xi    N(T)=nzeros(T)    equal?
     20           1                   1           yes
     30           3                   3           yes
     40           6                   6           yes
     50          10                  10           yes
  -> the increasing phase phi = -arg E_B gains exactly pi per real zero, so phi(T)/pi counts
     the zeros = N(T), an INTEGER.  RH <=> phi monotone <=> phi(T)/pi = N(T) (RvM total).

================  PART 3 : the one open step, precisely  ================
The canonical system is EXPLICIT: H(t) = P_{phi(t)} (rank-1, >=0 free), clock dt = phi'(x) dx,
phi = -arg(Xi + i Xi').  Everything reduces to ONE inequality: phi'(x) >= 0 (monotone clock).
  * Front (a): phi' is a functional of the log-derivative m_B = -Xi'/Xi -- the additive/Kubo-Mori
    object whose boundary values are the zeros-as-currents.  The clock lives in the KM geometry,
    NOT the quadratic Bures weight |E_B|^{-2}=(Xi^2+Xi'^2)^{-1} (which smooths the zeros away).
  * Front (b): phi(T)/pi = N(T) is the INTEGER zero-count; the clock IS the integrality.
OPEN (= RH): construct the clock phi'(x) >= 0 from the ARITHMETIC (the primes / Euler product),
independently of assuming the zeros real.  Equivalently: a Krein Hamiltonian H(t) >= 0 whose
transfer matrix at t=infinity recovers (Xi, -Xi'), with positivity from a non-circular input.
The de Branges positivity is FREE (rank-1) and the count is an INTEGER (front b); the missing
piece is the MONOTONICITY of the arithmetic clock -- the additive (KM) phase velocity staying
non-negative -- which is exactly the self-adjointness of H = N_inf + V_arith.  Not crossed;
but the object is now explicit and the open inequality is a single, named, local one.
```
