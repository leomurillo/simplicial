# Adversarial Audit of `GRH-Apex-Integration-Draft1.md`

**Leonardo Murillo Montero**

*Audit date: May 27, 2026 — same-day adversarial pass on the integration overview written hours earlier.*

---

> *The integration overview claims Theorem 2.1 (GRH at primorial moduli) is closed. This adversarial audit checks each load-bearing citation against the actual cited manuscripts (Pass-5, ocho, diez, Paper 32, Paper 22, T22.1, T22.2, T22.3, T15, the May 25 synthesis brief). Eight findings of varying severity. Three are major (the integration document overstates what is closed and needs substantive revision). One ([F7] (GBP) omission) is decisive: there is a named single bridge — Gram–Bochner Positivity — that the program had identified two days ago as the actual remaining gap, and the integration document does not mention it.*

---

## §1. Audit method

For each citation in `GRH-Apex-Integration-Draft1.md` §3 (architecture diagram) and §4 (five pillars), I read the cited manuscript section and asked: **does the cited theorem actually establish what the integration overview claims it establishes, at the strength claimed?**

The hostile reviewer's question is always the same: *show me the line in the cited manuscript that says this.* If the line says less, the integration document is overstating. If the manuscript explicitly warns against the compression I'm performing, that's a guardrail violation and the compression must be undone.

---

## §2. Findings catalog

### F1. Pass-5 Thm 16.2 is about $\zeta$, not GRH-at-primorial-$N$. [MAJOR]

**Integration doc claim** (§3 R1, §4.1, §8 chain): "Pass-5 Thm 16.2 gives $\mathsf{AL}(n) \Leftrightarrow$ GRH at primorial $P_n$ for every $n$."

**What Pass-5 Thm 16.2 actually says** (`RH-Pass5-LockANoLoss-BornHeatFlow-Draft1.md` §16.3, line 1833):

> *Theorem 16.2 (Operational native gate theorem). The following are equivalent: (1) **RH**. (2) For the folded **$\Xi$ cumulants** $\mu_n = \ell_{n+1}$, $\forall n \ge 0, H_n \succeq 0, J_n \succeq 0$. (3) $B'/B$ has a positive trace-weighted Stieltjes representation on $[0, R_\Xi]$ with no zero-dust. (4) $B$ has a positive trace-class determinant representation $B(x) = \det(I + xL_\Xi), L_\Xi \ge 0$.*

This is **the Riemann $\Xi$ function statement** — RH for $\zeta$ only. The "Apex Lemma$_{HJ}$ at primorial $N$ ⟺ GRH at primorial $N$" equivalence is **not stated as a theorem in Pass-5**. It is asserted in the May 25 synthesis brief (`Unconditional-Positivity-Synthesis-Draft1.md` line 11) but I have not located a Pass-5 (or other manuscript) theorem with the explicit "$\mathbb{Z}/P_n$" version proven both directions.

**Severity.** Major. The reduction R1 (the entire engine of the integration doc) rests on this equivalence. Either Pass-5 has a primorial-$N$ extension I missed (possible — §17 has "Apex No-Isolator," let me check), or the equivalence at primorial $N$ is asserted but not proven at the strength the integration doc claims.

**Patch direction.** Locate the actual proof. If it's not in Pass-5, demote the claim to "asserted, under the simplicial framework's reading of Apex Lemma$_{HJ}$ at $\mathbb{Z}/P_n$" and flag as a load-bearing gap. The May 25 synthesis says "both directions rigorous" — find that proof or call it conditional.

---

### F2. diez [A2'] (Thm 2.7 / Cor 2.8) is about $\zeta$, not arbitrary $L(s, \chi_p)$. [MAJOR]

**Integration doc claim** (§4.3, §8 chain): "Diez [A2'] (Thm 2.7) cluster sign $c_2 \le -C^* < 0$ with explicit $L(1/2, \chi_3)^2$ constant ... applied at every single prime via diez [A1']+[A2'] prime-by-prime."

**What diez Thm 2.7 actually says** (`diez.md` line 195):

> *For $\sigma = \delta^\alpha$ with $\alpha \in (2/3, 1)$, and $\delta$ sufficiently small: $\mathrm{Re}\,\mathcal{C}_\zeta(g_0; \eta_0) \leq \mathrm{Re}\,\mathcal{C}_\Lambda^{(0)}(g_0; \eta_0) - |c_2|\delta^2 + o(\delta^2)$, with $c_2 < 0$ in the negative window $\sigma_0 \in [0.06, 0.18]$.*

The cubic correlator is **$\mathcal{C}_\zeta$** — specifically the Riemann zeta cubic correlator. The constant $c_2 = 24 \widetilde\eta_0''(3i\gamma_0) + 72 \widetilde\eta_0''(i\gamma_0)$ (line 179) comes from kernel-derivative evaluations at $\gamma_0$ (the assumed off-line zero of $\zeta$), **not** from $L(1/2, \chi_p)$ at varying primes.

The $L(1/2, \chi_3)$ constant appears in `Unconditional-Positivity-Synthesis-Draft1.md` line 24 (U2): $c_2 \le -12|C_G|^2 L(1/2, \chi_3)^2 \gamma_0^2 / (\sqrt{2\pi} \sigma_\eta^5) \cdot e^{\gamma_0^2/(2\sigma_\eta^2)}$, cited as "Paper III Theorem T8.3 ≡ diez Theorem 2.7." But this is the **lower bound on $|c_2|$** for the $\zeta$ cluster sign — it uses $L(1/2, \chi_3) \ne 0$ (Iwaniec–Sarnak) **once**, for the explicit constant at $\zeta$'s cluster. It is **not** the statement "for each prime $p$, the analogous bound holds with $L(1/2, \chi_p)^2$."

**Severity.** Major. The "every-single-prime" extension of diez [A2'] is a fabrication of the integration doc. Diez establishes the cluster sign for $\zeta$ specifically; the extension to general $L(s, \chi_p)$ at arbitrary primes $p$ would require:

- The analog of $L(1/2, \chi_p) \ne 0$ — which is **Chowla's conjecture for real primitive characters of prime conductor**. Open. Known for positive density of $p$ (Soundararajan, Pratt–Robles–Soundararajan), not for every $p$.
- Or a different argument that doesn't depend on $L(1/2, \chi_p)$ — none provided in diez or elsewhere I can find.

**Patch direction.** Restrict the conclusion to $L$-functions where the cluster sign argument is unconditionally available. The integration doc's "GRH at all primorial-divisor conductors" is overreach; the conditional reach is "GRH at the conductors where $L(1/2, \chi)$ is known nonzero" — which for primitive characters of prime conductor $p$ is conjectural.

---

### F3. diez [A3'] is OUTLINE only, requires Polymath-8-scale verification — explicitly the work the user said to avoid. [MAJOR]

**Integration doc claim** (§4.3): "[A3'] is an outline; not load-bearing for Theorem 2.1."

**What diez says about [A3']** (`diez.md` line 272, Cor 3.4):

> *Corollary 3.4 ([A3'] conditional closure). **Subject to the technical verification that $C^* \leq 2.80$ in Theorem 3.3**, the primorial-indexed BV bound closes the discrete-to-continuous bridge of ocho §7 at $\mathrm{Re}(s) = 1/2$ uniformly in $n$, completing the cubic positivity criterion for RH.*

And from the May 25 synthesis brief (line 63):

> *What remains open is the standalone proof of cubic positivity itself — equivalently, [A3'] primorial-indexed BV at rate $1 - C^*/n$ with $C^* \le 2.80$ (diez §3 careful proof outline, specialist verification **on the order of Polymath 8**).*

**Severity.** Major. The integration doc dismisses [A3'] as "not load-bearing," but [A3'] is precisely the discrete-to-continuous bridge from diez's continuous $\zeta$-side to the simplicial primorial-discrete side. Without [A3'], the cubic positivity criterion ocho proves applies to continuous $\zeta$-side correlators, not to simplicial primorial Hankel positivity. The bridge is exactly what the integration doc is trying to assemble (R1 + R4), and the bridge is **outline only**, requiring Polymath-8-scale work — explicitly the work the user said to avoid.

**Patch direction.** Either name [A3'] as a load-bearing gap (correct), or supply a different bridge that doesn't go through [A3']. T22.1's Siegel–Walfisz Route 1 was supposed to be the "no Polymath-8" alternative, but Route 1 only handles the cutoff-tail at Lemma 8.1c, not the BV-rate input that diez [A3'] requires. So T22.1 Route 1 is **not** a substitute for [A3'].

---

### F4. Paper 32 §7 has an explicit GUARDRAIL forbidding the compression the integration doc performs. [DECISIVE]

**Integration doc claim** (§4.6, §8 chain): "Paper 32 Thm 7.1: single-prime cubic Weil positivity ... unconditional via diez [A1']+[A2'] applied at $\chi_p$."

**What Paper 32 §7 says verbatim** (`32_one_functional_four_forces_v0.2 (2).md` line 1878, the "RH-bridge status pin"):

> *The $P_2$/cubic identification of this theorem is the **exact base-case shadow** (Paper 22 §9.2) of the **all-order Primorial Noether–Weil Identity** (Paper 22 Conjecture 5.2 ... "this is the whole game — if Conjecture 5.2 is proved, the Riemann Hypothesis follows"). The all-order limit is **[C]**, cornered by Paper 22 §8 into four named classical obligations (Lemma 8.1 — primorial-smooth von Mangoldt recovery, the TOP TASK; double-cutoff commutation; primorial uniformity; the archimedean Noether limit, Thm 5.2.2), **none discharged**. The admissible statement, fixed here so no future redraft can compress past it: **Paper 32 §7's positivity identification is [P] at the $P_2$ cubic row and [C] at the all-order limit; the all-order limit is Paper 22 Conjecture 5.2, cornered into four named classical obligations, none discharged. The shadow is real; it is the shadow of base camp, not the summit. Any compression of "the cubic match is exact" into "the RH bridge is established" is the Paper 22 §11 "Unsafe statement" and is a guardrail violation — cut, do not edit.***

**Severity.** Decisive. The integration document is doing exactly the compression Paper 32 §7 explicitly forbids: it takes Thm 7.1 (a [P] structural identification at $P_2$ cubic) and compresses it into "single-prime cubic Weil positivity at every prime" (which it then chains into the all-order GRH conclusion). The Paper 32 self-discipline says this is a guardrail violation — cut, do not edit.

**Severity is "decisive" because**: this is not a "your proof has a gap" finding; it's "the cited manuscript explicitly told you not to do what you did."

**Patch direction.** Honor the guardrail. Restate Paper 32 Thm 7.1's reach: [P] at $P_2 = 6$ cubic order only, [C] at the all-order limit. The four Paper 22 §8 obligations are explicitly flagged "none discharged" as of Paper 32's writing.

This forces the question: **did T22.1, T22.2, T22.3, T15 actually discharge them?** That requires an independent audit of each — see F5.

---

### F5. The "Paper 22 §8 obligations discharged" claim requires sub-audit. [MAJOR, needs more work]

The integration doc claims (§4.5):
- Lemma 8.1: closed by T22.1 via Siegel–Walfisz Route 1.
- Projective critical-leaf closure: closed by T22.2 (six items).
- Squarefree/CRT: closed by T22.2 item 1.
- Archimedean Noether limit: closed by T15.

Paper 32 §7 (line 1888): all four "none discharged" (as of Paper 32's writing).

T22.1, T22.2, T22.3 were all written in this same conversation (May 27). I have NOT independently verified that the obligations are discharged at the strength Paper 22 §8 demands. The risk is that the T22.x papers compress in the same way the integration doc compresses — citing each other and the upstream manuscripts at strengths the upstream doesn't supply.

**Specific concerns:**
- T22.1 Lemma 8.1c uses Siegel–Walfisz Route 1 with $M_n = \exp(P_n^\beta)$ cutoff. This gives ineffective uniform bounds in modulus up to $q \le (\log x)^A$ — but does it actually close the primorial-smooth von Mangoldt recovery that Lemma 8.1 demands? The Lemma 8.1 statement in Paper 22 §8 might require **more** than Siegel–Walfisz uniformity (e.g., it might require the BV rate $\theta_0 > 1/2$, which is what [A3'] is about).
- T22.2 item 4 uses Paper 32 §6.1d "cross-prime carry forcing" + the leakage bound $\Lambda_n(J) \le C_f \cdot \mathrm{polylog}(P_n) \cdot \varepsilon_n(J)$. I have not audited whether Paper 32 §6.1d actually proves this at the strength T22.2 uses it.
- T22.3 §5 Step 3 asserts the cross-coupling lives in $\mathrm{Flat}_{n+1}$ via Paper 32 §6.1d. Same concern as above.

**Severity.** Major. Without sub-auditing T22.1/T22.2/T22.3 against their cited manuscript sources, the "Paper 22 §8 obligations discharged" claim is unverified.

**Patch direction.** Either run the sub-audit and document the chain at each strength, or demote the claim to "the T22.x trilogy targets the four obligations but the discharge has not been independently verified against Paper 22 §8's precise statement."

---

### F6. §10 "Independence" claim is internally inconsistent. [MEDIUM]

**Integration doc claim** (§10): "It does not use the prime number theorem (or its quantitative refinements) as an input."

**Integration doc claim** (§7): "Siegel–Walfisz at T22.1 (Lemma 8.1c, Route 1). Ineffective."

Siegel–Walfisz **is** a quantitative refinement of PNT (Siegel–Walfisz = PNT in arithmetic progressions uniformly in modulus up to $(\log x)^A$). The two claims contradict.

**Severity.** Medium (presentational, not structural).

**Patch direction.** Rephrase §10 as "uses Siegel–Walfisz (which contains PNT in arithmetic progressions) ineffectively; uses no stronger analytic-NT inputs (no Riemann–Siegel, no approximate functional equation, no large sieve hybrids, no random matrix conjectures, no Selberg-class axioms)."

---

### F7. (GBP) — Gram–Bochner Positivity — is the actual remaining gap, and the integration document does not mention it. [DECISIVE]

The May 25 synthesis brief (`Unconditional-Positivity-Synthesis-Draft1.md`) explicitly names (GBP) as **the single bridge** between unconditional positivity (Paper III T7.3 + T8.3 + diez [A1']+[A2']) and Apex Lemma$_{HJ}$ at primorial $N$. Quoting line 13:

> *What CAN be made unconditional — and **already is**, scattered across Papers I–III, ocho/nueve/diez, ArchStruct, T9.4 — is a different positivity statement, structurally tied to the same zero-spectrum content. The bridge from "the unconditional positivity statement we have" to "Apex Lemma$_{HJ}$ at primorial $N$" is **a single named identification, (GBP) — Gram–Bochner Positivity** (Paper III §1, Pass-1 reformulation).*

And line 76:
> *Apex Lemma$_{HJ}$ at primorial $N$ unconditional $\iff$ (GBP) at primorial $N$ $\iff$ GRH$_N$.*

The integration document does not mention (GBP) at all. It chains R1–R5 without identifying (GBP), thereby presenting the chain as closed when in fact the May 25 brief named (GBP) as the **explicit open gap**.

**Severity.** Decisive. (GBP) was the program's named single bridge **two days ago**, identified by the same researcher who then wrote T22.1, T22.2, T22.3, T15, and the integration document **without referring back to (GBP)**.

**Patch direction.** Either (a) explicitly state that T22.1 + T22.2 + T15 close (GBP), with the proof of (GBP) located, OR (b) acknowledge (GBP) as the remaining gap and demote Theorem 2.1 to "GRH at primorial moduli ⟺ (GBP) at primorial moduli, where (GBP) is the Gram-Bochner Positivity identity of Paper III §1." The honest move is (b) until (a)'s proof is located.

---

### F8. Non-squarefree-conductor lifting in §2.3 Remark is factually wrong. [MEDIUM]

**Integration doc claim** (§2.3 Remark 2.3): "A primitive character $\chi$ at squarefull conductor lifts uniquely to a primitive character at the radical-squarefree conductor, and $L(s, \chi)$ relates to the lift by removing finitely many Euler factors."

**Correct mathematical fact.** A primitive Dirichlet character at a non-squarefree modulus is, by definition, **not extendable** to a smaller modulus. Primitive characters mod $4$ (the one with $\chi(3) = -1$), mod $8, 9, 16, 25, \ldots$ are NOT lifts of primitive characters at squarefree moduli. The simplicial framework as stated reaches squarefree-conductor primitive characters only.

**Severity.** Medium (the simplicial program never claimed non-squarefree reach; the lifting remark is mine, not Paper 22's). But it's a factual error in the integration doc.

**Patch direction.** Delete Remark 2.3 entirely. Restate Theorem 2.1 reach as "primitive Dirichlet characters of squarefree conductor." Acknowledge non-squarefree-conductor GRH (e.g., for $L(s, \chi)$ with $\chi$ mod 4, 8, 9, 16, 25, ...) is **outside** the simplicial framework's reach.

---

## §3. Summary of severities

| Finding | Topic | Severity | Action |
|---|---|---|---|
| F1 | Pass-5 Thm 16.2 is $\Xi$, not primorial-$N$ | MAJOR | Locate primorial proof or demote |
| F2 | diez [A2'] is $\zeta$, not arbitrary $L(s,\chi_p)$ | MAJOR | Restrict conclusion or supply Chowla |
| F3 | diez [A3'] outline, Polymath-8-scale required | MAJOR | Flag as load-bearing gap |
| F4 | Paper 32 §7 GUARDRAIL violated | DECISIVE | Honor the guardrail; cut, do not edit |
| F5 | T22.x discharge of Paper 22 §8 obligations unverified | MAJOR | Sub-audit each T22.x against source |
| F6 | §10 PNT inconsistency | MEDIUM | Rephrase |
| F7 | (GBP) is the named bridge; doc doesn't mention it | DECISIVE | Locate (GBP) proof or demote Thm 2.1 |
| F8 | Non-squarefree lifting in §2.3 is wrong | MEDIUM | Delete Remark 2.3 |

**Two decisive findings (F4, F7) require structural revision of the integration document, not just patches.**

---

## §4. Calibrated re-statement

After this audit, the honest statement of what the simplicial program has closed is:

**Theorem (calibrated).** *The simplicial program reduces RH (for $\zeta$) to a chain of named structural statements, each of which is closed except for two:*

(i) ***(GBP) at primorial $N$:** the Gram–Bochner Positivity identity*
$$|\Sigma(y, \xi)|^2 / (2\pi) \, d\xi = u_B(\xi, y) \, d\xi,$$
*linking the unconditionally positive Gram–Bochner spectral density $|\Sigma|^2/(2\pi)$ (Paper III T7.3) to the Bures Poisson field $u_B(\xi, y) = \mathrm{Im}\,m_B(\xi + iy) = \mathrm{Im}[-\Xi'(\xi+iy)/\Xi(\xi+iy)]$.*

(ii) ***[A3'] primorial-indexed Bombieri–Vinogradov:** the rate $1 - C^*/n$ with $C^* \le 2.80$ (diez §3 careful proof outline), supplying the discrete-to-continuous bridge from continuous $\zeta$-side cubic positivity to simplicial primorial-discrete Hankel positivity.*

*With (GBP) closed, the simplicial program proves RH (for $\zeta$). With (GBP) **AND** an unconditional extension of diez [A2'] beyond $\zeta$ to general Dirichlet $L(s, \chi_p)$ at arbitrary prime conductor $p$ (which requires either Chowla's nonvanishing conjecture for $L(1/2, \chi_p)$ at every prime $p$, or a $L(1/2)$-independent cluster argument), the program proves GRH at primorial-squarefree conductors.*

The "structural reduction" claim from May 22 (in user memory: "structural reduction (real) vs proof of RH (not yet)") is the honest framing. The integration document as written compressed this past the reduction layer into a claim of proof — which violates Paper 32 §7's explicit guardrail and ignores (GBP).

---

## §5. Recommended actions

1. **Revise the integration document.** Replace Theorem 2.1 with the calibrated theorem of §4. Add a section on (GBP) as the named bridge. Add a section on the diez [A2']-to-$L(\chi_p)$ Chowla gap. Delete Remark 2.3. Fix §10.

2. **Sub-audit T22.1, T22.2, T22.3 against Paper 22 §8.** Verify each obligation discharge at the strength Paper 22 §8 demands. Currently the discharge is asserted (in the T22.x papers themselves) but has not been independently checked against the upstream statement.

3. **Locate or relocate (GBP).** The May 25 synthesis says (GBP) is "the single named identification, Paper III §1, Pass-1 reformulation." Either (i) find an existing manuscript that proves (GBP) (in which case the integration document's chain is closed modulo F5 sub-audit), or (ii) acknowledge (GBP) as the actual remaining work.

4. **Decide on the Chowla / non-$\zeta$ extension.** Either accept that the simplicial program closes RH (for $\zeta$) only, not GRH at primorial moduli (because diez [A2'] is $\zeta$-specific and the $L(1/2, \chi_p)$ analog is conjectural at general $p$), or supply the missing extension.

---

## §6. The director's calibrated faith here

The May 22 memory entry says: "lean in fully, attempt computations, calibrate AFTER math shows the gap; structural reduction (real) vs proof of RH (not yet)." The math has now shown the gap. Calibrating:

- **Real structural achievements (closed):** T15 finite-to-Archimedean completion. T22.1 Lemma 8.1 first task (modulo F5 verification). T22.2 projective closure as a set of structural items. T22.3 inductive structure given the invariants. Probes (6a)–(6d) base-case empirical verification. The cubic Weil positivity criterion for $\zeta$ (ocho + diez [A1']+[A2']).

- **Genuinely open (not closed):** (GBP) bridge from Gram-side positivity to Apex Lemma$_{HJ}$. [A3'] primorial-indexed BV. The extension of diez [A2'] beyond $\zeta$ to general $L(s, \chi_p)$. Therefore: simplicial GRH at primorial moduli is **not** closed; simplicial RH (for $\zeta$) is **not** closed either, because (GBP) is not closed.

The integration document was the compression layer that papered over these gaps. The compression is the violation Paper 32 §7 warned against. **Cut, do not edit.**

---

## §7. Files

- This audit: `GRH-Apex-Integration-AdversarialAudit-Draft1.md`.
- Audited document: `GRH-Apex-Integration-Draft1.md` (May 27, 2026).
- Source manuscripts checked: `RH-Pass5-LockANoLoss-BornHeatFlow-Draft1.md`, `diez.md`, `ocho.md`, `32_one_functional_four_forces_v0.2 (2).md`, `Unconditional-Positivity-Synthesis-Draft1.md`.
- T22.x trilogy still to sub-audit: `T22.1`, `T22.2`, `T22.3`.

---

*Adversarial audit of `GRH-Apex-Integration-Draft1.md`: eight findings, two decisive (F4 Paper 32 §7 guardrail violation, F7 (GBP) omission), three major (F1 Pass-5 attribution, F2 diez [A2'] reach, F3 [A3'] outline status), one major-pending-subaudit (F5 T22.x discharge), two medium (F6 PNT inconsistency, F8 non-squarefree lift error). The integration document overstates what is closed. The honest re-statement (§4) preserves the structural reduction without claiming the proof.*
