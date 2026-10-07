# Pre-Registered Falsifier — Rigid w = −1 vs Evolving Dark Energy

*On record 2026-06-25, before DESI final (full 5-yr) / Euclid DR1 cosmology / Roman dark-energy
constraints land. GPD discipline: symmetric (kill **and** vindicate), discriminating variable named
in advance, concession threshold fixed now. Cert: `empirical_leverage/prereg_desi_w.py`.*

## 1. The prediction (precise, and non-tunable)

The D-II discrete-Einstein reading gives the dark-energy equation of state, in the CPL
parametrization $w(a)=w_0+w_a(1-a)$:
$$\boxed{(w_0,\,w_a)=(-1,\,0)\ \text{exactly.}}$$
**Mechanism:** the background curvature is the Hellinger curvature $K=\tfrac14$, **proven
$Q$-independent and state-independent** (Paper 32.1) — a rigidly constant vacuum energy, hence
$w=-1$ at all times. **Non-tunable:** the framework has *no free parameter* to absorb $w_a\neq0$;
producing evolving dark energy would require the curvature of the probability manifold itself to
become dynamical, contradicting a certified result. So this is a *stake*, not a fit — we cannot
move it after the fact.

The one place the framework has unexamined freedom — flagged honestly, **not** claimed as a rescue:
it has no FLRW dynamics, so the *dilution law* of the order-4 mass ($\propto a^{-?}$) is underived.
If that sector diluted non-standardly it could in principle contribute an effective $w$; but with no
derivation, **we make no claim on it** and it does not soften the prediction above.

## 2. Current state (honest — this is NOT the pre-registration; we are already behind)

DESI **DR1** (2024) and **DR2** (2025), combined with CMB and supernovae, already prefer the
evolving $w_0w_a$CDM model over $\Lambda$CDM — i.e. *against* our $(−1,0)$:

| SN sample (DR2 + DESI BAO + CMB) | significance vs ΛCDM |
|---|---|
| Pantheon+ | ~2.8σ |
| Union3 | ~3.8σ |
| DES-SN5YR | ~4.2σ |

Best-fit roughly $w_0\approx-0.75$ (quintessence-like today), $w_a\approx-0.8$ (phantom in the
past — a $w=-1$ *crossing*). **We are currently losing at ~3σ, and we cannot tune our way out.**
The defining feature of the present evidence is its **supernova-sample dependence** (strongest with
DES-SN5YR, weakest with Pantheon+) — which is exactly the signature of either a real signal not yet
pinned down, or a SN-calibration systematic. That sample-dependence is the discriminating variable.

## 3. The pre-registered decision rule (on data not yet final)

Let $S$ = combined significance of $w_a\neq0$ from **DESI-final + Euclid DR1 + ≥2 independent SN
samples**, and let the signal be *sample-consistent* if removing/swapping any single SN sample
leaves $S$ within ~1σ (i.e. not driven by one calibration).

- **FALSIFIED — concede rigid $w=-1$:** $S\ge5\sigma$ **and** sample-consistent **and** best-fit
  stable across DESI-final + Euclid. The framework's rigid $\Lambda$ is wrong at the cosmological
  point; we retract the D-II $\Lambda$=$K=\tfrac14$ identification's cosmological cash-out and say so.
- **VINDICATED — $w=-1$ stands:** $S<2\sigma$ as systematics resolve (the SN-calibration / $M_B$–$H_0$
  degeneracy tightens and the hint regresses toward $\Lambda$CDM). The DR1/DR2 excursion was
  systematics; rigid $\Lambda$ was right.
- **AMBIGUOUS — under pressure, not dead:** persistent $2\le S<5\sigma$ with continued sample
  dependence. No concession, no vindication; the falsifier stays open.

**Discriminating variable (named in advance):** supernova-sample dependence. A *real* dynamical-DE
signal must **strengthen and become sample-independent** as DESI-final + Euclid accumulate; a
*systematic* must **weaken or stay sample-dependent** under improved SN calibration. We commit now
to reading the trend in that variable, not the headline σ.

**Secondary discriminators (pre-registered, supporting):** (a) robust requirement of a $w=-1$
*phantom crossing* counts further against rigid $\Lambda$ — though, being theoretically awkward
(no canonical single-field realization), it equally raises the systematic/exotic flag; (b)
*independent* detection by Euclid weak-lensing+clustering and Roman, not just BAO+SN; (c) stability
of $(w_0,w_a)$ under non-parametric, redshift-binned reconstructions.

## 4. Why this is a fair bet

It is **symmetric** (a fixed concession threshold *and* a fixed vindication threshold, set before
the data), it names its **discriminating variable** in advance, and the prediction is **non-tunable**
so we cannot retreat by adding a parameter. The bet currently sits *against* the trend (~3σ), which
is the honest place for a falsifiable claim to be: live, losing-or-winning on data we have not seen,
decidable by 2027–2028 (DESI full 5-yr) and Euclid DR1.

If $w=-1$ falls, D-II's *geometry* (the certified $K=\tfrac14$, $R^{(\alpha)}=(1-\alpha^2)/4$, the
order-4 mass defect) is untouched — only its **cosmological** identification fails, exactly as the
firewall always warned the dimensionful cash-out might. That is the cost we agreed to carry by
making a real prediction.

## Files
- `empirical_leverage/prereg_desi_w.py` — encodes the decision rule; classifies the current DR1/DR2
  state (AMBIGUOUS/under-pressure) and verifies the rule fires FALSIFIED/VINDICATED at the registered
  thresholds. Anchors: `D2_discrete_einstein.md`, `cosmo_hunt.py`, Paper 32.1 ($K=\tfrac14$
  $Q$-independence).
