# The Localization: The Riemann Hypothesis Driven to Smooth Primorial Elliott–Halberstam

**Leonardo Murillo Montero**
*Independent researcher*
*June 8, 2026*

**Abstract.**
The Numbers series does not lower the difficulty of the Riemann Hypothesis; it **localizes** it. Every component of the cubic apparatus except one is discharged unconditionally, and the single residual is pinned to a precisely named analytic class: **smooth Elliott–Halberstam on friable primorial moduli** \(P_n\), i.e. the level of distribution \(\theta_0(p_n) = 1 - C^*/n \to 1\) holding *uniformly in \(n\)* with a fixed crossover constant \(C^* \le 2.80\). The honest statement is a one-directional **sufficient** reduction — discrete cubic positivity at \(P_n\) together with this level *implies* critical-line positivity — not an equivalence, and the open class is RH-equivalent in strength (N0: *conservation of difficulty, RH-hard \(\to\) primorial-EH-hard*). What the program contributes is therefore not a shorter problem but a **sharper one**: it discharges the major arc, the minor arc, the off-line sensitivity, the small primorials \(n \le 7\), and the entire unconditional apparatus (apex unitary, archimedean operator, two-channel Bures fiber, de Branges function \(E_B = \Xi + i\Xi'\), cubic Weil positivity, Estermann pair, variance bridge, function-field validation), leaving exactly one named obstruction whose location — the archimedean spectral realization, reached only in the \(n \to \infty\) limit — is identified but not removed.

**MSC 2020:** 11M26, 11N13, 11L05.
**Keywords:** Riemann Hypothesis, apex unitary, de Branges space, cubic Weil positivity, primorial Bombieri–Vinogradov, level of distribution, smooth Elliott–Halberstam, trilinear Kloosterman.

---

## 1. The Reduction (what is established, and in which direction)

Two of the three links below are unconditional equivalences with RH; the third is a **one-directional sufficient conditional**, and we mark it as such.

1. \(E_B(z) = \Xi(z) + i\Xi'(z)\) is Hermite–Biehler on \(\mathbb{C}_+\) (equivalently \(m_B = -\Xi'/\Xi\) is Herglotz). **\(\iff\) RH.**
2. The cubic Weil functional \(\operatorname{Re}\,\mathcal{C}_\zeta(g;\eta) \ge 0\) for all admissible test functions. **\(\iff\) RH.**
3. **(Sufficient bridge, one direction.)** Discrete cubic positivity at primorial modulus \(P_n\), *together with* primorial equidistribution at level \(\theta_0(p_n) = 1 - C^*/n\) holding uniformly in \(n\) with \(C^* \le 2.80\), **\(\Rightarrow\)** the critical-line positivity of (2).

- **(1) \(\iff\) (2)** is unconditional (apex archimedean operator + de Branges criterion; N4–N6). [P]
- **(2) \(\Rightarrow\) (1)** uses only off-line cluster analysis and bulk curvature (the \(\chi_3\)-twisted pair weight). [P]
- **(3) \(\Rightarrow\) (2)** is the discrete-to-continuous bridge (N0 §§5–6, diez Thm 4.3): its sole obligation is the stated level — *not* the continuous third moment, *not* Hardy–Littlewood. It is **not** an equivalence and is **not** known to be reachable from RH; it is the conditional input that, if supplied, closes the loop. [C, one-directional]

> **Caution on direction.** Item (3) is a hypothesis that *implies* RH-positivity, not a restatement of RH. The reverse — that RH yields this level — is *not* claimed and would itself be a smooth Elliott–Halberstam theorem. The literature treats Elliott–Halberstam and (G)RH as largely independent; the program's position is the weaker, correct one: *if* the primorial level holds uniformly, the apex bridge transfers discrete positivity to the line.

---

## 2. The Three-Arc Decomposition

The cubic functional decomposes into three arcs, mirroring the circle-method treatment of Goldbach via a mod-8 kernel (Washburn 2026):

- **Major arc** — singular-series main term. Unconditional, positive; certified \(+651.6\) on the canonical window (`probe_singular_series_triple.py`); discrete realization = the V-sector positivity at \(P_n\) (ocho §5). [P]
- **Minor arc** — mean-square (Matomäki–Radziwiłł–Tao 2016). Unconditional; Möbius autocorrelations cancel at square-root strength; divisor variance equidistributes past level \(1/2\). The variance bridge is in hand at every level \(< 1\). [P]
- **Medium arc** — the level \(\theta_0(p_n) = 1 - C^*/n\). This is **the obstruction**, bounded above by the Heath–Brown identity, the large sieve, per-prime Burgess, and trilinear Kloosterman (Bettin–Chandee, sharpened by Wright 2026 to \(Q \le X^{1/2 + 1/66 - \delta} \approx 0.515\)). [C]

The off-line sensitivity is the unconditional \(\chi_3\)-twisted pair correlation, anchored by \(L(1/2,\chi_3) = 0.4808\ldots > 0\) (LMFDB). [P]

It is **asserted by structural analogy**, not proved, that the medium arc *is* precisely the BV level; the proven content is that major and minor are in hand and that the medium arc is bounded by the trilinear-Kloosterman frontier. The lemma "medium arc \(\equiv\) the level" remains to be written.

---

## 3. Discharged Content (unconditional)

- **Apparatus.** Apex unitary and archimedean operator (N4–N6); two-channel Bures fiber \((\xi, L_{\chi_3})\); de Branges \(E_B\); cubic Weil positivity; Estermann polar pair; variance bridge. [P]
- **Small primorials \(n \le 7\).** Discharged at the fixed well-factorable ceiling \(\theta_* = 3/5\) (Maynard, triply-well-factorable). The required level \(1 - C^*/n \le 3/5\) is met by the *fixed* ceiling exactly up to the crossover \(n^* = C^*/(1-\theta_*) \approx 7\). [P]
- **Off-line teeth.** \(\chi_3\)-twisted pair weight, strictly negative. [P]
- **Major and minor arcs.** In hand (§2). [P]
- **Function-field validation.** Over \(\mathbb{F}_q\), arch-domination *is* Weil intersection positivity on \(C \times C\) (N7 §6): the reduction is sound — no reading of the main theorem fails in the model. This **validates the framing**; it does not transport to \(\mathbb{Q}\) (FH-type positivity is unconditional and therefore cannot contain RH). [P, validation only]

---

## 4. The Terminus (open) — and exactly why it is RH-strength

The residual is the large-\(n\) asymptotic: \(\theta_0(p_n) = 1 - C^*/n \to 1\) on friable moduli \(P_n\), i.e. **smooth Elliott–Halberstam, uniform in \(n\)**. Three points must be stated plainly, because they are where the synthesis is easily over-read:

1. **\(C^* \le 2.80\) is the crossover constant, not the target.** As a *fixed* bound it describes the *already-discharged* regime \(n \le 7\). The open content is the **uniform-in-\(n\)** statement, which is identical to \(\theta_0 \to 1\) at rate \(1/n\). "Prove \(C^* \le 2.80\)" is therefore not a finite computation; spelled out it reads "maintain \(C^* \le 2.80\) for all \(n\)," which *is* smooth EH.

2. **The fixed-level tools do not approach the target.** Wright (2026) at \(\approx 0.515\), Bettin–Chandee, Fouvry–Radziwiłł, Maynard's \(3/5\) ceiling — these are *fixed* levels. They discharge small \(n\). They do **not** move \(\theta_0\) toward \(1\). Progress on the fixed level and progress on the asymptotic are different problems; conflating them is a category error.

3. **The limit carries the archimedean place.** The bridge (item 3 of §1) needs "the level and nothing more" precisely because the archimedean content is hidden inside the \(n \to \infty\) limit of that level. By the No-Go (N11 §§6–7), the archimedean spectral realization — the fixed self-dual positive object over \(\mathbb{Q}\) whose collapse locus is the zeros — is **not finitely-prime-generable** and is open; over \(\mathbb{F}_q\) it is Weil's theorem, over \(\mathbb{Q}\) it is the missing \(\mathbb{F}_1\) self-product / Connes–Consani archimedean positivity. The \(n \to \infty\) primorial limit is exactly the route to that object. So the "frontier" is not a level-of-distribution number to be tuned; it is the archimedean realization wearing analytic-number-theory clothing.

N0's own ledger states the conclusion without hedging: **conservation of difficulty, RH-hard \(\to\) primorial-EH-hard.** The c\(_2\)-hunt (Option A) does not escape it — non-circular positivity = prime fluctuation = the same \(C^*\). The contribution is **localization**, not difficulty reduction.

---

## 5. Equivalent Geometric Readings

All are the same statement about the same measure (uniform archimedean domination):

- Curvature current of \(\log\xi\) confined to the critical line (Poincaré–Lelong, bulk dual-flatness).
- Bures–Poisson field \(u_B \ge 0\).
- Li ladder \(\lambda_n \ge 0\) for all \(n\).
- Generating function \(G(z)\) analytic on \(|z| < 1\).

These are equivalent *reformulations*; by N11 each is a *shadow* of the archimedean object, free where the function field or the on-axis line supplies it and open otherwise. Reformulation is not breach.

---

## 6. Status and Next Steps

This is a **structural localization**, not a proof, and not a reduction in difficulty. The apparatus is complete, verified, and validated over function fields; the open content is exactly one named analytic class, RH-equivalent in strength, with the archimedean obstruction located but not removed.

**What the program legitimately offers the field:** the single sharpest-localized frontier — discharge everything but one named class — together with every supporting certificate. That is worth publishing as a clean target.

**What it does not offer:** a shorter path. Anyone reading this should understand that proving the terminus *is* proving RH (modulo the unconditional bridge), and that the best current trilinear tools advance the fixed level, not the asymptotic.

**Recommended next paper.** A standalone localization note stating, in one unambiguous sentence: *RH follows from \(\theta_0(p_n) = 1 - C^*/n \to 1\) uniformly on friable primorial moduli, via the unconditional apex bridge.* Quantifier on \(C^*\) uniform in \(n\); the equivalence list reserved for (1)\(\iff\)(2) only; the bridge marked one-directional; the archimedean No-Go reconciled in one sentence.

---

**References** (selected)

- Numbers series [N0]–[N15], P∞, T-series (full apparatus).
- Connes–Consani (2006.13771; 2511.22755); Connes–Consani–Moscovici (2025).
- Estermann (1930), Burgess (1962), Matomäki–Radziwiłł–Tao (2016), Wright (2026), Bettin–Chandee, Fouvry–Radziwiłł, Maynard.
- Weil (1948), Deligne (1974) for function-field validation.

---

*This document is the corrected extraction and synthesis of the reduction from the series drafts (primarily N0; bridge direction from N7; No-Go from N11; off-line and apparatus from N4–N6, N13–N15). It states the result as the one-directional sufficient reduction the source papers actually prove, with the crossover constant \(C^*\) and the asymptotic target distinguished, and the archimedean obstruction located.*
