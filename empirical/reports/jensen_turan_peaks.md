# (a) peaks side: Jensen / Turan / Laguerre-Polya for the Riemann xi

**Script:** `empirical/verify_jensen_turan_peaks.py`
**Context:** the peaks insight; (a) the archimedean forcing structure; ties dBN heat flow + moment work.
**Nature:** numerical (mpmath moments + numpy roots), labelled.

```text
(a) on the peaks side: the Jensen / Turan / Laguerre-Polya characterization of RH.

User's lens: in a sin wave we over-regard the ZEROS and treat the PEAKS as 'just amplitude',
but the peaks (extrema, f'=0) carry the reconstruction, and the derivative hierarchy
(f=0 zeros, f'=0 peaks, f''=0 inflections, ...) is the real structure.

That crystallizes into the classical PEAKS-side characterization of RH:
  RH  <=>  the Riemann xi is in the Laguerre-Polya class (a real-rooted entire limit)
       <=>  every Jensen polynomial J_{d,n} is HYPERBOLIC (all roots real)
       <=>  the Turan inequalities hold (coefficient log-concavity).
Real-rootedness is exactly 'f and f' interlace' -- peaks and zeros alternate (Rolle + reality),
the derivative hierarchy. This is the de Bruijn-Newman heat-flow's LP class (Pass-4's Phi), and
it is STRICTLY STRONGER than the moment/Hankel positivity (which is automatic, because the
Riemann kernel Phi(t) > 0): moments = amplitude (free); Jensen hyperbolicity = peaks (the RH content).

Setup. Phi(t) = sum_{m>=1} (2 pi^2 m^4 e^{9t/2} - 3 pi m^2 e^{5t/2}) e^{-pi m^2 e^{2t}}  (Phi>0, Polya).
xi-hat(z) = int_0^inf Phi(t) cos(zt) dt = sum_n (-1)^n a_n/(2n)! z^{2n},  a_n = int_0^inf t^{2n} Phi dt.
As a function of w=z^2:  G(w) = sum_n (gamma_n/n!) w^n,  gamma_n = (-1)^n a_n n!/(2n)!.
Jensen polynomial:  J_{d,n}(t) = sum_{k=0}^d C(d,k) gamma_{n+k} t^k.   RH <=> all J_{d,n} hyperbolic.
d=2 hyperbolicity = Turan: gamma_{n+1}^2 >= gamma_n gamma_{n+2}.

PART 1 (amplitude, automatic): a_n are Stieltjes moments of Phi>0 => Hankel(a) >= 0. NOT RH.
PART 2 (peaks, the RH content): Turan (d=2) and Jensen hyperbolicity (d=2,3,4) for low n.
        Known unconditional at low degree (Csordas-Norfolk-Varga d=2; Dimitrov-Lucas d=3;
        Griffin-Ono-Rolen-Zagier: each d hyperbolic for n large). We confirm + frame.

NUMERICAL (mpmath moments + numpy root-reality), labelled.

Phi-moments a_n = int t^{2n} Phi dt (all > 0 since Phi > 0):
  a_0=0.12428, a_1=0.00574299, a_2=0.000740712, a_3=0.000149824, a_4=4.02416e-5, a_5=1.32597e-5, a_6=5.11878e-6, a_7=2.24694e-6, a_8=1.09833e-6

================  PART 1 : amplitude = moment/Hankel positivity (automatic)  ========
  Hankel det D_0 = 0.12428   (>0)
  Hankel det D_1 = 5.9074e-5   (>0)
  Hankel det D_2 = 4.55765e-10   (>0)
  Hankel det D_3 = 1.12158e-16   (>0)
  All Hankel dets > 0: True  -- a_n is a Stieltjes moment sequence. This is the 'amplitude'
  condition; it is FREE (Phi>0) and is NOT RH.

================  PART 2 : peaks = Jensen hyperbolicity / Turan (the RH content)  ====
  Turan (d=2, log-concavity): gamma_{n+1}^2 >= gamma_n gamma_{n+2}  <=>  J_{2,n} hyperbolic
    n=0 : gamma_{n+1}^2 / (gamma_n gamma_{n+2}) = 1.0748439  OK
    n=1 : gamma_{n+1}^2 / (gamma_n gamma_{n+2}) = 1.0627437  OK
    n=2 : gamma_{n+1}^2 / (gamma_n gamma_{n+2}) = 1.0543033  OK
    n=3 : gamma_{n+1}^2 / (gamma_n gamma_{n+2}) = 1.0480505  OK
    n=4 : gamma_{n+1}^2 / (gamma_n gamma_{n+2}) = 1.0432125  OK
    n=5 : gamma_{n+1}^2 / (gamma_n gamma_{n+2}) = 1.0393451  OK
    n=6 : gamma_{n+1}^2 / (gamma_n gamma_{n+2}) = 1.0361743  OK
  Turan holds for all tested n: True   (known unconditional, Csordas-Norfolk-Varga 1986)

  Jensen hyperbolicity J_{d,n}(t) = sum_k C(d,k) gamma_{n+k} t^k  (all roots real?):
    d=2 : n0:R  n1:R  n2:R  n3:R  n4:R  n5:R  n6:R
    d=3 : n0:R  n1:R  n2:R  n3:R  n4:R  n5:R
    d=4 : n0:R  n1:R  n2:R  n3:R  n4:R
  (R = real-rooted/hyperbolic = peaks and zeros interlace; C = complex root present.)
  All tested Jensen polynomials hyperbolic: True

================  WHAT THIS IS  ================
Amplitude (moments/Hankel) is FREE: Phi>0 makes a_n a moment sequence, automatically.
The PEAKS (Jensen hyperbolicity / Turan log-concavity) are the RH content -- strictly
stronger, and exactly 'f and f' interlace' (the derivative hierarchy). Low-degree holds
unconditionally (CNV d=2, Dimitrov-Lucas d=3); RH = ALL degrees, and Griffin-Ono-Rolen-
Zagier force each degree d for n large -- the residual is LOW n, i.e. the DOMINANT
low-lying zeros = the biggest peaks. The de Bruijn-Newman heat flow (kernel Phi) preserves
the Laguerre-Polya/hyperbolic property; RH is whether it survives to t=0 (Pass-4).

So (a) on the peaks side: RH = forcing Jensen hyperbolicity (the peaks) at every degree,
with the moment/amplitude floor free and the residual concentrated at the dominant low
peaks. This is the archimedean object (xi) read through the derivative hierarchy, not the
zeros -- exactly the reframe: the peaks carry it.
```
