# Multiplicative vs additive: which basis carries the zeros?

**Script:** `empirical/verify_multiplicative_carries_zeros.py`
**Context:** the R1 inversion (singularize the discrete); Born-Helmert / P-series unification.
**Nature:** numerical (numpy + mpmath), labelled.

```text
The inversion test (singularize the discrete): does the MULTIPLICATIVE basis carry the
zeros where the ADDITIVE one fails?

Context. RH-Pass4 (Born-Helmert) reduces RH to a power-sum match between a finite prime
ledger and the folded-Xi cumulants ell_m = sum_gamma gamma^{-2m}. The DIRECT route used the
ADDITIVE-character ledger: bin Lambda(p^k)/p^{k/2} by residue mod N=30, take the DFT power
spectrum, match power sums to ell_m. It FAILED (probe_R1_findings): ~1e4x off, dominated by
parity / small-modulus (Chebyshev) structure -- additive characters of Z/N see residues, not
the multiplicative prime->zero structure. Diagnosis D5: the right basis is MULTIPLICATIVE
Dirichlet characters of (Z/N)^x.

This probe runs the inversion. The key refinement over R1's literal next-action: the zeros do
not live in a finite count of character Born-squares; they live in the FREQUENCY t of the
twisted von Mangoldt sum, which resonates at the L-function zeros (the explicit formula made
visible). Concretely  sum_{n<=X} chi(n) Lambda(n) n^{-1/2-it}  approximates -L'/L(1/2+it,chi),
whose poles are the zeros of L(s,chi).

PART A1. chi = principal (zeta): the prime sum peaks at the zeta zeros gamma_k.
PART A2. chi = chi_{-4} (mod 4): the twisted prime sum peaks at the L(s,chi_{-4}) zeros instead
         -- a DIFFERENT set -- so the multiplicative character SELECTS its own L-function.
PART B.  Reproduce the additive failure (R1): residue-binned DFT power spectrum, p0/ell1 ~ 1e4,
         parity dominance. The additive basis does not carry the zeros.

NUMERICAL (numpy + mpmath), labelled. Conclusions are peak alignment / a ratio, robust to it.

================  PART A1 : multiplicative (principal) sum resonates at zeta zeros  ====
  X = e^10; |sum Lambda(n) n^{-1/2-it}| (Riesz-smoothed); zeta zeros gamma_k for reference.
  top prime-sum peak locations : ['14.14', '21.00', '25.04', '30.38', '32.98', '37.56', '40.90']
  zeta zeros gamma_k           : ['14.13', '21.02', '25.01', '30.42', '32.94', '37.59', '40.92']
  near each gamma_k: peak offset = ['0.01', '0.02', '0.03', '0.04', '0.04'] ; peak/median = ['5.1', '5.0', '4.9', '4.8', '4.8']
  [A1] prime sum resonates at the zeta zeros (peaks aligned, contrast>2): True

================  PART A2 : chi_{-4} twist resonates at L(s,chi_{-4}) zeros instead  ===
  chi_{-4}-twisted prime-sum peaks   : ['6.04', '10.22', '13.02', '16.28', '18.38']
  L(s,chi_{-4}) zeros (|beta| minima): ['6.00', '10.25', '13.00', '16.25', '18.25']
  zeta zeros (for contrast)          : ['14.13', '21.02', '25.01', '30.42', '32.94']
  mean dist of twisted peaks to beta-zeros = 0.03 ; to zeta-zeros = 3.82
  [A2] the chi_{-4} character SELECTS L(s,chi_{-4}) (peaks track beta-zeros, not zeta): True

================  PART B : the additive residue-binned basis fails (R1 reproduction)  ==
  additive power-spectrum trace p0 = 310 ; ell_1 = sum gamma^{-2} = 0.01721
  p0 / ell_1 = 1.802e+04   (R1 reported ~1.8e4 -- the additive ledger does NOT encode zeros)
  conductor mass fractions: d=2:39%, d=3:19%, d=5:9%, d=6:17%, d=10:8%, d=15:4%, d=30:4%
  fraction in conductor-2 (parity) mode: 39%  (small-modulus/Chebyshev, not zeros)

================  THE INVERSION, SETTLED  ================
MULTIPLICATIVE basis CARRIES the zeros: the von Mangoldt sum sum Lambda(n) n^{-1/2-it}
resonates at the zeta zeros (A1), and twisting by chi_{-4} moves the resonance to
L(s,chi_{-4})'s zeros (A2) -- the character SELECTS its L-function. The ADDITIVE
residue-binned basis does NOT (B): p0/ell1 ~ 1e4, mass concentrated in the parity
(conductor-2) mode -- it sees small-modulus density, not the prime->zero structure.

This vindicates the inversion (singularize the discrete): the discrete/arithmetic
(multiplicative) basis is where the zeros live; the continuous/Fourier (additive)
basis only sees smooth density. Confirms R1's D5 and unifies with the P-series
multiplicative apex (P4/T8). Necessary, not sufficient: the zeros are CARRIED here,
but the POSITIVITY/forcing (RH) is still the archimedean residual -- now to be
forced from this correct (multiplicative/discrete) side, not approximated from the
smooth side that hit the conditioning wall.
```
