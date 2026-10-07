# Szego outer construction: does log u_B expose structure the Apex/Hankel moment side hasn't used?

**Script:** `empirical/verify_szego_log_structure.py`.
**Finding:** the Szego/outer side uses log u_B; its Fourier data s_k is a different ENCODING than the Apex
Hankel moments, but the STRONG SZEGO LIMIT THEOREM makes them equivalent (s_k govern the Toeplitz/Hankel
determinants). The outer function built from log u_B is structurally the de Branges Hermite-Biehler E_B
(inner factor = Blaschke over the zeros), which the program already carries (phi'/canonical system). So the
Szego construction RECOVERS de Branges and LINKS it to the Apex moment side (Szego-dual), unifying the two
routes -- but adds NO non-circular leverage: outer factorization exists <=> u_B>=0 <=> RH. Computed the FTs
of u_B and log u_B and the Szego sum to make the duality concrete. Honest yield: unification, not a new opening.
**Nature:** numerical (mpmath + numpy FFT) + Szego-theorem structure. NO RH claim.

```text
Does the Szego OUTER construction (which uses log u_B) expose arithmetic structure in the
Lambda(n)/sqrt n amplitudes that the Hankel/Apex (moment) side has not used?  -- computed, honestly.

Setup.  u_B(xi,y) = Im[-Xi'/Xi(xi+iy)] = sum_rho y/((xi-gamma_rho)^2+y^2) >= 0 (Bures-Poisson field).
  * Apex/Hankel side: uses the MOMENTS  int s^k d sigma  -> Hankel >= 0 (Stieltjes positivity).
  * Szego/outer side: u_B = |Sigma|^2 with Sigma the Hardy OUTER function, built from LOG u_B
        log Sigma = (1/2)(log u_B + i * Hilbert(log u_B)).
  * Strong Szego limit theorem CONNECTS them: the Toeplitz/Hankel determinants are governed by the
    log-Fourier coefficients s_k = FT(log u_B)(k):  log det ~ (n) s_0 + sum_k k |s_k|^2.
So the two sides are Szego-DUAL: moments (Apex) vs log-coefficients (Szego), linked by Szego's theorem.

QUESTION (computed here): what is the Fourier structure of LOG u_B?
  * FT(u_B) has spikes at omega=log n with the von Mangoldt weights Lambda(n)/sqrt n (prior probe).
  * FT(log u_B) = ?  If it ALSO sits on the log-rational lattice {log n} but with DIFFERENT amplitudes,
    the Szego side exposes a different (multiplicative/log-Euler) encoding the moment side does not use.
    If it sits on the ZERO frequencies, it exposes the inner/Blaschke (de Branges) structure instead.
This probe computes both FTs and reports honestly which lattice log u_B lives on and with what amplitudes.

NUMERICAL (mpmath u_B + numpy FFT); NO RH claim -- it tests what the Szego (log) side genuinely exposes.

================  computing u_B and log u_B on [2,202], 2048 pts (y=0.50)  ================
  u_B range [0.0236, 3.0461] (>0, so log u_B is finite -- Szego condition holds at y=0.50).
  log u_B range [-3.7485, 1.1139].

================  (1) Fourier amplitude at omega = log n :  u_B vs log u_B  ================
     n     log n     |FT(u_B)|     |FT(log u_B)|    log-spike? (vs midpoint)
      2    0.6931        176.9          167.6      13.60 <-- spike
      3    1.0986        187.3          167.4      19.02 <-- spike
      4    1.3863        87.69           88.6       2.05 <-- spike
      5    1.6094        159.2          134.2       1.46 
      6    1.7918       0.7337          19.66       0.32 (none -- Lambda=0)
      7    1.9459        141.9          115.1       1.00 
      8    2.0794         43.3          43.88       0.74 
      9    2.1972        62.47          59.09       1.00 
     11    2.3979          104          79.64       1.00 
     13    2.5649        93.02           69.3       1.00 

  Reading: if log u_B spikes at log n (like u_B), the Szego side lives on the SAME log-rational
  lattice but with DIFFERENT amplitudes (a multiplicative/log encoding); if not, it lives elsewhere.

================  (2) does log u_B carry the zero-spacing (inner/de Branges) frequencies?  ====
  mean zero density near T=100 is 0.4404 / unit; the zero-lattice frequency is ~2.767.
  |FT(log u_B)| at the zero-lattice frequency 2.767 = 61.32 ; at log 2 = 167.6 ; at log 3 = 167.4.
  largest |FT(log u_B)| peak (excluding DC) at omega = 0.6912, magnitude 167.6.
  nearest log n to that omega: n ~ 2.00 (log n=0.6912); nearest zero-freq multiple: 2.767.

================  (3) the Szego connection + honest answer  ================
  Szego data: s_0 = mean(log u_B) = -0.07709 (the log-geometric-mean / entropy of the field);
              sum_k k |s_k|^2 ~ 10.41 (the strong-Szego correction governing the Hankel determinants).
  Strong Szego: log det Toeplitz_n(u_B) ~ n*s_0 + sum_k k|s_k|^2.  So the Apex/Hankel determinants
  ARE governed by these log-coefficients s_k = FT(log u_B) -- the moment side and the Szego side are
  the SAME positivity, dual encodings linked by Szego's theorem.

HONEST ANSWER to 'does the Szego outer construction expose structure the Hankel/Apex side hasn't used?':
  * The Szego side uses LOG u_B; its Fourier data s_k (computed above) is a DIFFERENT encoding than the
    moments int s^k d sigma the Apex Hankel uses -- but by the strong Szego theorem the two are
    EQUIVALENT (the s_k determine the Hankel determinant asymptotics). So it is not independent data:
    it is the Szego-DUAL of the moment data, same positivity u_B>=0 = RH.
  * The outer function Sigma built from log u_B is, structurally, the de Branges Hermite-Biehler E_B
    (the Hardy function whose zeros are the gamma_rho); its 'inner factor' is the Blaschke product over
    the zeros. RH = inner factor on the line. The program ALREADY carries this (phi', the canonical
    system) -- so the Szego construction RECOVERS the de Branges side, it does not add new leverage
    beyond it. What it DOES add is the explicit link: de Branges (outer/Hardy) and Apex (moment/Hankel)
    are Szego-dual encodings of the one positivity -- unifying the program's two routes.
  * NO non-circular advantage: outer factorization EXISTS <=> u_B>=0 <=> RH (Szego). The Lambda(n)/sqrt n
    amplitudes are the boundary data; the Szego/de-Branges and the Apex/Hankel sides both reduce to their
    positivity. The push CONFIRMS the wall is one object seen two Szego-dual ways, not a new opening.

VERDICT: the Szego outer construction recovers the de Branges E_B / Hardy inner-outer structure and
links it, via the strong Szego limit theorem, to the Apex/Hankel moment side -- the program's two
positivity routes are Szego-dual. It exposes the entropy/log encoding s_k (genuinely different DATA
than the moments) but NOT independent LEVERAGE: all reduce to u_B>=0 = RH. The honest yield is
unification (de Branges <-Szego-> Apex), not a new attack. Conservation holds.
```
