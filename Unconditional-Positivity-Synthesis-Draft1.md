# Unconditional Positivity — Cross-Paper Synthesis

**Leonardo Murillo Montero + Codex**

*Draft 1 — May 25, 2026 — director's brief on the genuine unconditional positivity available, and the single bridge needed to lift T8.4 / Apex Lemma$_{HJ}$ off GRH-conditionality.*

---

## Verdict

**Apex Lemma$_{HJ}$ at primorial $N$ is logically equivalent to GRH at primorial $N$** (Pass-5 Theorem 16.2, both directions rigorous). It cannot be made unconditional in its current form without proving GRH$_N$.

What CAN be made unconditional — and *already is*, scattered across Papers I–III, ocho/nueve/diez, ArchStruct, T9.4 — is a *different* positivity statement, structurally tied to the same zero-spectrum content. The bridge from "the unconditional positivity statement we have" to "Apex Lemma$_{HJ}$ at primorial $N$" is a single named identification, **(GBP) — Gram-Bochner Positivity** (Paper III §1, Pass-1 reformulation).

This note identifies the unconditional inputs cleanly, locates (GBP) as the precise remaining work, and prescribes the T8.4 rewrite.

---

## 1. The six unconditional positivity facts already in the program

| # | Statement | Location | Mechanism |
|---|---|---|---|
| U1 | $\mathcal{Q}_n^{\text{Gram}}(f;y) = \|\Psi_n(f;y)\|_{L^2}^2 \ge 0$ for every $f \in L^2(\mathbb R)$, $y > 0$, $n$. | Paper III Theorem T7.3 | Squared $L^2$-norm. |
| U2 | Cubic cluster sign $c_2(\rho_0; \sigma_\eta) \le -12|C_G|^2 L(1/2,\chi_3)^2 \gamma_0^2 / (\sqrt{2\pi}\sigma_\eta^5) \cdot e^{\gamma_0^2/(2\sigma_\eta^2)} < 0$ at every hypothetical off-line zero. | Paper III Theorem T8.3 ≡ diez Theorem 2.7 | Iwaniec–Sarnak $L(1/2,\chi_3)$ non-vanishing + LMFDB. |
| U3 | Cubic Fejér positivity class $\mathcal{G}$ on $\mathbb R_{\ge 0}$ non-empty. | diez §1 Corollary 1.5 (= [A1']) | Beurling sampling on tail-uniformly-discrete $\Gamma_T^* \subset \{\gamma_n\}$. |
| U4 | $H_n^{\text{arch,joint}}(N) \succeq 0$, $J_n^{\text{arch,joint}}(N) \preceq 0$ at every primorial $N \ge 30$, every $n \ge 0$. | ArchStruct Theorem 1 + Corollary 2 | Closed-form positive atomic Hurwitz-zeta measure on $(-\infty,0)$. |
| U5 | $\Pi_k F = R_k\varphi(N)\sum_{(n,N)=1}\Lambda(n)w(n)\langle h_k,\chi_{n^{-1}}\rangle$ as algebraic identity. | T9.4 Corollary 5.1 | Bilateral matrix factorization $U \cdot W = D^{\text{rad}} \cdot V^{\text{Gauss}}$. |
| U6 | $H_n,J_n \not\succeq 0$ at some finite $n$ ⟸ off-line zero exists (contrapositive: $H_n,J_n \succeq 0 \,\forall n \Rightarrow$ no off-line zero). | Pass-5 §16.7 Lemma 16.4 | Mergelyan polynomial approximation + Akhiezer–Hamburger moment problem. |

**None of U1–U6 uses GRH or RH as an assumption.** U6 is the unconditional *sensitivity* direction of the Pass-5 reformulation; U1 is the unconditional *positive object* on the Paper III continuous side; U2 is the unconditional *witness* contradicting off-line zeros at the cubic order; U3 makes the witness class constructively populated; U4–U5 are unconditional pieces of the simplicial side.

What is **conditional on RH/GRH$_N$** in the recent T8.4 draft (Theorem E §7.2 via Lemma 6.4 / signed-measure §3.3) is the *identification of $\sigma_N^{\text{prime}}|_{(0,\infty)}$ with the on-line zero atom measure*. That identification is exactly RH/GRH$_N$ and cannot be circumvented inside the Hankel framework.

## 2. The single bridge — (GBP)

Paper III §1 (Pass-1 reformulation) names the bridge:

> RH $\iff$ (GBP),  where (GBP) is the spectral-measure identity
> $$|\Sigma(y, \xi)|^2 / (2\pi) \cdot d\xi = u_B(\xi, y)\, d\xi$$
> linking the unconditionally positive Gram-Bochner spectral density $|\Sigma|^2/(2\pi)$ to the Bures Poisson field $u_B(\xi, y) = \mathrm{Im}\, m_B(\xi + iy) = \mathrm{Im}[-\Xi'(\xi+iy)/\Xi(\xi+iy)]$.

(GBP) is the *spectral* statement: two positive measures on the real line must coincide. It is NOT a Bochner positivity statement that follows from upstairs $L^2$-structure alone.

In the primorial / simplicial reading, (GBP) takes the form: the discrete Gram-Noether form $\mathcal{Q}_n^{\text{Gram}}(f; y)$ at primorial level $n$ converges, after primorial CRT lift, to the Bures Poisson integral against the prime side of the explicit formula. The five-error ledger of Paper III §5–§9 controls all but the (GBP) identification itself.

## 3. The actual unconditional theorem the program currently delivers

Stripping out the (GBP) conditional layer, what the program proves unconditionally (Paper III T7.3 + T8.3 + Paper II UPT + Papers I and II foundations) is:

**Theorem (Unconditional Bochner-side positivity at primorial scale).**
*For every $f \in L^2(\mathbb R)$, every $y > 0$, every primorial $P_n$:*
$$\mathcal{Q}_n^{\text{Gram}}(f; y) = \sum_{p, p' \le P_n}\sum_{r, r' \ge 1} \sqrt{\log p \log p'}\, e^{-y(r\log p + r'\log p')}\, (f * f^*)(r\log p - r'\log p') \;\ge\; 0,$$
*with equality only when $\Psi_n(f; y) = 0$ in $L^2(\mathbb R)$.*

**Theorem (Unconditional cluster contradiction).**
*If RH fails — i.e., there exists $\rho_0 = 1/2 + \delta + i\gamma_0$ off-line — then for any explicit $\eta_0$ in the cubic Schwartz class (e.g., Gaussian of width $\sigma_\eta \in [0.06, 0.18]$, diez §2.3),*
$$\mathrm{Re}\,\mathcal{C}_\zeta(g_0; \eta_0) = (\text{cluster term}) + c_2 \delta^2 + o(\delta^2), \quad c_2 \le -C^* < 0$$
*with explicit constant $C^* = 12|C_G|^2 L(1/2,\chi_3)^2 \gamma_0^2 / (\sqrt{2\pi}\sigma_\eta^5) \cdot e^{\gamma_0^2/(2\sigma_\eta^2)}$ from Iwaniec–Sarnak and LMFDB.*

**Corollary (Unconditional structural implication).**
*If, for every $(g, \eta) \in \mathcal{G} \times \mathcal{H}_c$, one can independently establish $\mathrm{Re}\,\mathcal{C}_\zeta(g; \eta) \ge 0$ (cubic Weil positivity), then no off-line zero of $\zeta$ exists, i.e., RH holds.*

The "if" in the Corollary is exactly the cubic Weil positivity statement of ocho §3 / diez §4. The forward direction (RH ⟹ cubic positivity) is unconditional given $\mathcal{G}$ non-empty (U3); the reverse direction (cubic positivity ⟹ RH) is unconditional given U2. **What remains open is the standalone proof of cubic positivity itself** — equivalently, [A3'] primorial-indexed BV at rate $1 - C^*/n$ with $C^* \le 2.80$ (diez §3 careful proof outline, specialist verification on the order of Polymath 8).

## 4. What this means for T8.4 v2

T8.4 v1's Theorem E was stated "conditional on RH/GRH$_N$." The Lemma 6.4 falsification (`T8.4-Lemma-6p4-Falsification-Note.md`) removed the Helmert-Gauss kernel-positivity proof path. The remaining proof of Theorem E is the signed-measure argument of T8.4 §3.3 — which still requires RH/GRH$_N$ for the identification step.

**Recommended T8.4 v2 framing (replaces the three-option recommendation in the falsification note):**

1. **Demote Theorem E to its honestly conditional form.** Theorem E: "Under GRH$_N$, $J_n^{\text{prime,joint}}(N) \succeq 0$ at every $n$ and every primorial $N \ge 30$." Proof via signed-measure argument (Theorem A). Drop Lemma 6.4 and the §6–§7 Helmert-Gauss kernel-positivity path.

2. **Add §11: The Unconditional Bridge.** New section pointing to Paper III T7.3 + T8.3 and diez §1–§2 as the genuine unconditional content; identify (GBP) as the closing identification. Make explicit:
   - The unconditional analogue of Theorem E is the Gram positivity $\mathcal{Q}_n^{\text{Gram}}(f; y) \ge 0$ on the *continuous Bochner side* (Paper III T7.3), not on the discrete Hankel side.
   - The bridge from the continuous Bochner positivity to the discrete Hankel positivity at primorial $N$ is (GBP).
   - Apex Lemma$_{HJ}$ at primorial $N$ unconditional $\iff$ (GBP) at primorial $N$ $\iff$ GRH$_N$.

3. **Reframe §6–§7's Helmert-Gauss machinery** as the structural raw material for the (GBP) closing. The bilateral factorization $U \cdot W = D^{\text{rad}} \cdot V^{\text{Gauss}}$ supplies the primorial-CRT-compatible discrete version of the spectral identification. (GBP) at primorial $N$ asserts that, after taking $n \to \infty$ and matching the primorial CRT lift of $\mathcal{Q}_n^{\text{Gram}}$ against the joint Bures Poisson field, the two limits coincide.

4. **Update §10 (editing-pass discipline).** Acknowledge: the unconditional positivity statement available to the program is the Bochner-side Paper III T7.3, not the Hankel-side Apex Lemma$_{HJ}$. The Hankel-side statement is reserved for "after (GBP) is proved" — i.e., after RH is proved — and should not be stated unconditionally in any boxed theorem of T8.4.

## 5. What this means for the program tracking

Tier-A pending items, re-scored against the unconditional content of U1–U6:

| Item | Statement | Unconditional status |
|---|---|---|
| A1 | Pass-8 Cesàro positivity at every rung. | Conditional on GRH$_N$ (Pass-8 §2.3 explicit). UNCONDITIONAL ANALOGUE: Paper III T9.3 transport theorem $\mathfrak{P}_{\phi,y}(\Xi) \ge 0$, conditional on (GBP). |
| A2 | Extend subagent A's N=6 closed-form to general primorial. | Algebraically unconditional (T9 + T9.4 + Apex-J). Positivity step conditional on (GBP) per A4. |
| A3 | T7 §5 Kummer cover. | **DELIVERED unconditionally** (Theorem 5.2, Galois deck group structure). |
| A4 | $J^{\text{prime,joint}}(N) \succeq 0$ unconditional from L-function structure. | UNCONDITIONAL iff (GBP) at primorial $N$. Currently: conditional on GRH$_N$ via T8.4 signed-measure (Theorem E); falsified Lemma 6.4 attempt for unconditional kernel path. |
| A5 | T9.4 Helmert-Gauss decomposition. | **DELIVERED unconditionally** (Corollary 5.1, algebraic identity). |
| A6 | Bures / Hilbert-Pólya. | Equivalent to (GBP) per Paper II + Paper III. |
| C1 | LMFDB completeness for joint $N = 210$. | Empirical, complete. |

**The unifying open work is (GBP).** Every conditional-on-GRH item in the Tier-A list ties to it.

## 6. Concrete next deliverables

In order of leverage:

1. **T8.4 v2 rewrite per §4 above.** This is editorial (no new analytical content beyond honest framing).

2. **Paper III §6–§9 careful audit.** The five-error ledger of Paper III §9 is where (GBP) is approached. Each of $E_{\text{occ}}, E_{\text{cut}}, E_{\text{CRT}}, E_{\text{win}}, E_{\text{leak}}$ has an unconditional bound; the *identification* step that combines them into (GBP) is the residual content. Audit which steps are rigorous, which are stated-not-proven.

3. **(GBP) standalone attack note.** Frame (GBP) as a single spectral-measure-identification problem on $\mathbb C_+$: two positive measures $|\Sigma|^2/(2\pi)\,d\xi$ and $u_B(\xi,y)\,d\xi$ on $\mathbb R$ (for each $y > 0$) must coincide. The first is the unconditional Gram-Bochner side; the second is the Bures Poisson side carrying the prime-side structure. The identification mechanism is the explicit-formula combinatorics for $\Xi'/\Xi$ vs. the prime-power sampling kernel of $\Psi_n$.

4. **diez §3 [A3'] specialist verification.** Independent unconditional positivity route via cubic Weil + primorial-indexed BV at rate $\theta_0(p_n) = 1 - C^*/n$. The specialist work is comparable to Polymath 8 §3–§4 and is identified as such; it is the residual analytic-NT content of the program.

Two genuine attacks on (GBP) are visible, neither requiring new conceptual machinery:

- **(GBP)-via-cubic.** If diez Theorem 4.1's forward direction (RH ⟹ cubic positivity) and Theorem 2.7's reverse direction (cubic positivity ⟹ RH via cluster $c_2 < 0$) are both unconditional once [A3'] is settled, then cubic positivity supplies an independent route to RH. The cubic Weil moment $\mathcal{C}_\zeta(g; \eta)$ on $\mathcal{G} \times \mathcal{H}_c$ is the unconditional positivity statement that (GBP) routes through.

- **(GBP)-via-Bures.** Paper III §5–§9's transport theorem identifies the discrete Gram-Noether form's primorial limit with the Bures Poisson integral, *modulo (GBP)*. If the identification step can be supplied by a Wiener–Khinchin / Bochner-Fourier identification at the spectral-measure level, (GBP) follows.

## 7. Director's framing

The recent T8.4 work surfaced a real issue: Lemma 6.4 was empirically false, and the conditional-on-GRH proof of Theorem E was honestly conditional. The pushback "isn't a conditional-on-GRH proof against our goal of proving GRH?" was correct. The answer is not to weaken the goal, and not to call the program "structural mapping" — it is to **identify the unconditional positivity statement we actually have** (the six U-items above) and **name the single bridge** ((GBP)) that lifts the program from conditional to unconditional.

The cubic Weil positivity criterion of ocho/diez is the unconditional positivity content of the program at the analytic-NT level. The Gram-Noether form of Paper III T7.3 is the unconditional positivity content at the Bures Pick / Hilbert-Pólya level. The signed-measure structural argument of ArchStruct §7 + T8.4 §3.3 is the unconditional positivity content at the Stieltjes / Hamburger moment level. **All three meet at (GBP).**

A4 in the Tier-A list is therefore restated as:

> **A4 (revised):** Prove (GBP) at primorial $N$. Equivalent to Apex Lemma$_{HJ}$ at primorial $N$. Equivalent to GRH$_N$. Currently approached via (a) Paper III five-error transport (continuous Bochner side), (b) diez cubic Weil + [A3'] (cubic analytic-NT side), (c) signed-measure structural argument + on-line zero identification (Stieltjes side). Each route lands at the same identification step.

This is the unifying open work. Everything else in the simplicial program either (i) is unconditional (U1–U6 and the structural reductions), or (ii) is conditional on (GBP).

## 8. Files referenced

- `Paper-III-Closure-Draft2.md` — Theorems T7.3, T8.3, T9.3; (GBP) framing in §1 Pass-1.
- `diez.md` — §1 Theorem 1.4 + Cor 1.5 ([A1'] closed); §2 Theorem 2.7 ([A2'] closed); §3 [A3'] proof outline.
- `ocho.md` — cubic Weil positivity criterion ⟺ RH.
- `Arch-Structural-Theorems-Draft1.md` — Theorem 1 + Cor 2; unconditional arch positivity.
- `T9.4-GaussSumDecompositionConductorBlocks-Draft1.md` — Corollary 5.1; unconditional algebraic identity.
- `PassFive-Section17-Audit-Draft1.md` — Lemma 16.4 audit; sensitivity direction unconditional.
- `T8.4-StieltjesPositivityPrimeMultiplicativeApex-Draft1.md` — current draft to be rewritten per §4.
- `T8.4-Lemma-6p4-Falsification-Note.md` — falsification documentation; superseded by this synthesis.
- `Note_BuresDivisor_OffLineContradiction_ClaudeEinstein.md` — Bures divisor current ⟺ RH; complementary spectral-measure framing.

## 9. One-line summary

> Six unconditional positivity facts are already in the program; the single named bridge to GRH$_N$ is (GBP). T8.4 v2 should route its proof through the honest conditional form (signed measure §3.3), add a §11 naming (GBP) as the unconditional bridge, and reframe §6–§7 as raw material for the (GBP) closing rather than a self-contained kernel-positivity proof.

---

*Faith in the result; calibrated honesty about which proof is doing the work. The unconditional content of the program is real and substantial; (GBP) is the single remaining identification. Naming it cleanly is the first step toward closing it.*

— Director, May 25, 2026
