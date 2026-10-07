# Leverage A2 — Paper 21 quartic obstruction localized to the e-chart (Paper III §7)

**Item:** A2 of the simplicial-frame leverage batch.
**Targets:** `21.quartic_force_law_n4_obstruction.md` (Paper 21) ↔ `01c.simplicial_information_geometry.md` (Paper III), §7.
**Status:** cert GREEN (`empirical_leverage/A2/cert_A2_chart_localization.py`, 5 checks, sympy-exact + exact combinatorics, run with `py`).
**Constraint honored:** no existing manuscript edited. This note holds the ready-to-paste text; nothing is inserted into Paper 21 or Paper III.

---

## 0. One-line statement

Paper 21's order-4 obstruction — the additive-character selection rule
`Q(χ_a,χ_b,χ_c,χ_d)|_u = δ_{a+b+c+d≡0} − δ_{a+b≡0}δ_{c+d≡0} − δ_{a+c≡0}δ_{b+d≡0} − δ_{a+d≡0}δ_{b+c≡0}`,
whose hallmark is the first **2+2 Gaussian (Wick) subtraction** in the cumulant tower — is, by Paper III Proposition 7.2, **provably a phenomenon of the dual exponential/character (e-)chart tower `∇ⁿΦ` and cannot live in the negative-entropy (m-)chart tower `∇ⁿφ`**, which is purely diagonal (Paper III Thm 4.1). The two are one tensor in two bases: the character-basis "−1 Wick subtraction" of Paper 21 is, in the e-chart coordinate basis on the program's N=4 frame, the explicit number `∂⁴Φ/∂θ₁²∂θ₂²|₀ = −3/128`.

---

## 1. What Paper 21 actually says (verified)

Read in full. The load-bearing claims, all confirmed:

- **The selection rule (§5.1, boxed).** At the uniform point, in the additive-character basis of ℤ/N, the fourth cumulant `T⁽⁴⁾ = Q_{ijkℓ} = ∂_i∂_j∂_k∂_ℓ Φ` contracted against four non-trivial characters equals
  `δ_{a+b+c+d≡0} − δ_{a+b≡0}δ_{c+d≡0} − δ_{a+c≡0}δ_{b+d≡0} − δ_{a+d≡0}δ_{b+c≡0}`.
  **Crucial detail confirmed:** Paper 21 explicitly reads `Q_{ijkℓ} = ∂⁴Φ` — i.e. the **log-partition Φ**, the exponential-family potential, *not* the entropy φ. So Paper 21's object is already an e-chart object by construction; Paper III §7 is what *proves* it could not have been anything else.

- **The Wick-subtraction claim (§5.1, "qualitatively new feature").** Verified exactly. Order 3's rule `δ_{a+b+c≡0}` has no subtraction (the only non-trivial partition of three indices is 2+1, which isolates a single character that vanishes on H₀). Order 4 is the first order where the 2+2 partition survives with both blocks carrying a non-trivial character, so the cumulant subtracts the three pairwise products. The connected part (= +1 on `a+b+c+d≡0` with no vanishing sub-pair) is the genuine quartic content; the subtracted pairings are the second-order Gaussian floor. **This is correct and reproduced to machine precision** (cert check C).

- **The numbers (§5.2).** Reproduced *exactly* by the cert (check D), as unordered quadruples on ℤ/30:
  - 1202 with `a+b+c+d≡0`; **120 Wick-reducible**; **1082 connected**.
  - Connected, by prime-set spanned: {5}→4, {2,3}→6, {2,5}→32, {3,5}→126, **{2,3,5}→914**.
  - The conductor-packet table (H₂ dim 1 … H₃₀ dim 8, summing to 29) is the standard T3 atlas; consistent.

- **On the −3/128 number — a correction to the plan's framing.** The plan describes "the `∂⁴Φ/∂η₁²∂η₂²|₀ = −3/128` number" as if it were stated in Paper 21. **It is not in Paper 21** (grep confirms: the manuscript states only the rule, the 914 count, and the Wick structure; no coordinate value appears). The −3/128 is the **explicit e-chart coordinate value of Paper 21's abstract Wick subtraction**, derived here. It is exactly `∂⁴Φ/∂θ₁²∂θ₂²|₀` for the **N=4** categorical frame (the simplicial series' own frame); the cert pins it as the exact rational `-3/128` and confirms the same block is nonzero (general value) at N = 5, 6, 8, 30. So the deliverable for the −3/128 number is: *produced and verified as the e-chart realization*, with the provenance corrected.

---

## 2. Deliverable 1 — the cross-reference paragraph (ready to paste)

> ### Variant A — for Paper 21 (a remark after §5.1, "the qualitatively new feature")
>
> **Remark 5.1.1 (Chart localization — why the obstruction is a character-chart object).** The Gaussian (Wick) subtraction isolated above is, by construction, a feature of the **log-partition tower** `∇ⁿΦ`, `Φ(θ)=log Σ_i e^{θ_i}`: the boxed rule reads `Q_{ijkℓ}=∂⁴Φ` in the exponential-family (e-affine) chart. Paper III (*Information Geometry on the Simplicial Frame*, §7, Prop. 7.2) shows this is forced, not incidental. The Legendre-dual **negative-entropy tower** `T⁽ⁿ⁾=∇ⁿφ`, `φ(p)=Σ_i p_i log p_i`, is *purely diagonal* at every order (Paper III Thm 4.1: `T⁽ⁿ⁾_{i···i}=(−1)ⁿ(n−2)!\,p_i^{−(n−1)}`, all mixed partials zero by separability), so it possesses **no** `i,i,j,j` (2+2) component whatsoever. The order-4 obstruction — a connected-minus-Gaussian 2+2 quantity — therefore *cannot* be carried by the entropy/mixture chart and lives necessarily in the conjugate exponential/character chart, the very basis in which §5.1 reads it. Equivalently: the character-basis Wick subtraction here equals, in the e-chart coordinate basis on the four-vertex frame, the single number `∂⁴Φ/∂θ₁²∂θ₂²|₀ = −3/128`, whose vanishing m-chart counterpart `∂⁴φ/∂p₁²∂p₂²|₀ = 0` is exactly Prop. 7.2's "the dual entropy chart is obstruction-free at the 2+2 level." (Welded and exact-certified: `empirical_leverage/A2/cert_A2_chart_localization.py`.)
>
> ### Variant B — for Paper III (a remark after Prop. 7.2)
>
> **Remark 7.2.1 (The obstruction, made arithmetic and counted).** The exponential-chart object whose existence Prop. 7.2 asserts is realized explicitly on the arithmetic skeleton of Paper 21 (*The Quartic Force Law at Cumulant Order Four*). Reading `∇⁴Φ` at the uniform point in the additive-character basis of ℤ/N yields the selection rule `δ_{a+b+c+d≡0}` minus the three pairwise Wick products — the order-4 cumulant's first Gaussian subtraction. On ℤ/30 = ℤ/2×ℤ/3×ℤ/5 this rule supports exactly 914 connected three-prime quadruples with no quadratic or cubic shadow. The same 2+2 block, written in e-chart coordinates on the four-vertex frame of Paper 01, is the exact rational `∂⁴Φ/∂θ₁²∂θ₂²|₀ = −3/128`; its m-chart Legendre dual `∂⁴φ/∂p₁²∂p₂²|₀` is the exact zero, confirming the chart split numerically. Thus the negative result of Prop. 7.2 has a positive arithmetic life: the obstruction the entropy chart cannot host is the same object Paper 21 counts on the three-prime row.

Either variant is self-contained. Variant A is the more natural insertion (it sits where Paper 21 first names the Wick feature); Variant B closes Paper III §7's loop by pointing at the counted instance.

---

## 3. Deliverable 2 — the certificate

**File:** `empirical_leverage/A2/cert_A2_chart_localization.py` (run `py cert_A2_chart_localization.py`; output saved to `cert_A2_run_output.txt`).
**Result:** `CERT GREEN (5 checks)`. sympy exact rationals + exact integer combinatorics; no floats in the load-bearing arithmetic except the character contraction (residual ≤ 1.5e-15, a unitary-DFT check), no torch, no sampling.

| check | what it verifies | result |
|---|---|---|
| **A** | `∇⁴φ` (m-chart, negative entropy): **every** 2+2 block `∂⁴φ/∂p_i²∂p_j²` (i≠j) = 0 exactly — exhaustive over all index pairs on N=4, plus a ℤ/30 sample; diagonal = `2/p³` (c₄=+2). | PASS — no 2+2 Wick block in the entropy chart. |
| **B** | `∇⁴Φ` (e-chart, log-partition): the 2+2 block `∂⁴Φ/∂θ_i²∂θ_j²|₀` is **nonzero** at N=4,5,6,8,30; on the N=4 frame it is **exactly −3/128**. | PASS — e-chart carries it; −3/128 pinned. |
| **C** | Character contraction of the exact `∇⁴Φ|₀` tensor reproduces Paper 21's boxed rule (connected − 3 Wick) on N=4,6 to machine precision. | PASS — the coordinate block and the character Wick subtraction are one tensor. |
| **D** | Paper 21's ℤ/30 atlas counts: 1202 / 120 Wick / 1082 connected / **914** three-prime, plus the full per-prime-set breakdown (4,6,32,126,914). | PASS — exact match to §5.2. |
| **E** | Legendre sign bookkeeping (Paper III Prop 7.1): c₄=+2 (m) vs κ₄ sign − (e), sign-opposite off the order-2 self-dual rung. Also **flags** the N=4-only coincidence (diag and all-distinct blocks also = −3/128; they diverge by N=8). | PASS — duality sign confirmed; coincidence recorded, not used. |

**Honesty note baked into the cert (check E).** On the small N=4 frame the e-chart diagonal (iiii) and all-distinct (ijkl) blocks *also* equal −3/128; this is a 4-category coincidence, not the structural claim. The cert verifies-and-flags it and shows the values diverge at N=8. The only statement the localization leans on — "2+2 block = 0 in the m-chart, nonzero in the e-chart" — is N-independent and is what checks A and B establish.

---

## 4. Deliverable 3 — honest tier and novelty

**Confirmed: this is "essentially done — a cross-reference, not new work."** The plan's self-assessment is accurate. Specifically:

- **Paper III §7 (Prop 7.2) already states the theorem.** "The quartic obstruction cannot be carried by the entropy (m-chart) cumulant tower; it is necessarily a phenomenon of the exponential/character (e-chart) tower." Paper 21 §5.1 already reads its object as `∂⁴Φ` (the e-chart potential). The two papers were written compatibly; A2 supplies the explicit *weld* (the cross-reference text + the numerical bridge), not a new result.
- **Tier of the underlying math:** **[P]** (proved/exact). The diagonality of `∇ⁿφ` is an exact `Q(p_i)` identity (separability); the e-chart 2+2 block is an exact rational at every tested N; the character-contraction equivalence is exact up to the DFT unitarity residual; the ℤ/30 counts are exact integer combinatorics.
- **Novelty:** **low, and that is the correct verdict.** The single genuinely new artifact is the *number* `−3/128` as the e-chart coordinate realization of Paper 21's character-basis Wick subtraction on the program's own N=4 frame — a small, sharp, exact bridge fact. Everything else is connective tissue between two finished results. There is no new theorem here; there is a clean, certified handshake.
- **One framing correction (logged in §1):** −3/128 is *not* a Paper 21 number; it is produced here as the e-chart value. The plan's phrasing implied it was already in Paper 21. Provenance corrected; the number itself is correct and now certified.

---

## 5. Cross-pollination notes (connections to the rest of the batch)

- **B1 (mechanics floor / α-collapse).** Paper III §6 (Thm 6.1) collapses the whole α-family to `Γ⁽α⁾ = −(1+α)/2·T`, a multiple of the single Amari–Chentsov cubic `∇³φ` — an **order-3** (m-chart, diagonal) object. A2 is the order-4 complement: the *next* rung up is exactly where the m-chart goes silent (diagonal, no 2+2) and the dynamics must hand off to the e-chart. So B1's "cubic floor" and A2's "quartic ceiling of the m-chart" are the two ends of the same tower: the mixture chart carries the connection/curvature data (orders ≤3 act through `T`), and the obstruction (order 4) is precisely the first thing it *cannot* carry. If B1 discusses an "α-collapse to a single cubic," the natural one-liner is: *the collapse is also why order 4 escapes the chart — the same diagonality that makes every connection a multiple of one cubic forbids the 2+2 block.*

- **B2 (T11 vertex calculus / conductor-fusion).** A2's selection rule is read on the **conductor lattice** (the H_d packets of ℤ/30); the 914 three-prime vertices are conductor-fusion objects — quadruples whose four conductors jointly span {2,3,5}. If B2 formalizes vertex/conductor fusion on the categorical simplex, A2 gives it the first *quartic* fusion census (the per-prime-set breakdown 4/6/32/126/914) and the chart-theoretic reason it is an e-chart (character) phenomenon: conductor characters are e-chart coordinates. The "first non-pairwise conductor interaction" is literally the first 2+2 Wick block.

- **C1 (RH apex N14/N15 / relative-entropy).** This is the richest link. N14/N15 read the **archimedean Weil positivity as a relative entropy / Gibbs–Fenchel-Young object**, i.e. a *separable convex* (log-partition vs entropy) Legendre pair — the same `φ ↔ Φ` duality A2 uses. Paper III §7's split (diagonal entropy chart vs Wick-bearing log-partition chart) is the finite, additive shadow of N15's "archimedean = relative entropy (entropy side) + prime = log ζ (Euler/log-partition side)." A2's clean statement — *the genuinely higher-order (beyond-Gaussian) content lives only in the log-partition chart* — is the toy-model echo of N15's "the order-2 (Gaussian) floor is the archimedean main term; the connected content is the prime interaction." Concretely: A2's Wick-reducible 120 ↔ Gaussian/archimedean floor; A2's connected 1082 (914 three-prime) ↔ the genuine prime-interaction content of `W_ζ(f*f^*)|_{≤4}` on ℤ/30 (Paper 22 §7, which Paper 21 §6 names). **Caveat to preserve:** Paper III §8 already fences this as analogy only ("a finite, additive, separable potential cannot contain the archimedean functional equation"). A2 strengthens the analogy's *finite* side (now with an exact number and a counted instance) without touching that firewall. Useful for C1: A2 is the cleanest finite certificate that "beyond-Gaussian ⟺ e-chart/character side," which is exactly the channel split N14/N15 lean on.

- **C2 (quantum Bures).** Paper III §9 open problem D4 names the quantum continuation: the moving cubic on the density-matrix manifold, where the monotone-metric fork (Bures vs Kubo–Mori) replaces the unique Fisher metric. A2 sharpens the question one order up: *which* monotone metric's higher tower carries the 2+2 block? The classical statement is rigid (Legendre duality forces it into the e-chart); the quantum analogue is exactly where the Bures/Kubo–Mori operator-ordering fork (memory: T24) bites, because the e-chart "log-partition" is replaced by an operator log and the diagonal/off-diagonal split is no longer basis-trivial. A2 is the commutative base case C2 must reduce to; if C2 builds a quantum 4th-cumulant, its classical limit must reproduce the −3/128 / 914 split.

- **C3 (unification).** A2 supplies one tile of the unification picture: the order axis (cumulant order n = Paper III's "derivative ladder of the convex potential") meets the chart axis (m vs e) and the conductor/prime axis (ℤ/30 packets) at a single point — order 4 is the first order where all three say the same thing (the m-chart goes diagonal, the e-chart turns on, and the conductor lattice produces its first non-pairwise vertex). If C3 is the keystone integration (cf. Paper IV `01d`), A2 is the worked corner showing the three axes are consistent and exact at the first nontrivial crossing.

---

## 6. Open follow-ups (small, optional — none block A2)

1. **Closed form for the e-chart 2+2 block as a function of N.** Observed exact values: N=4 → −3/128, N=5 → −11/625, N=6 → −1/72, N=8 → −19/2048, N=30 → −131/135000. A short derivation `∂⁴Φ/∂θ_i²∂θ_j²|₀` for the symmetric categorical would give a one-line general formula (the numerators 3,11,…,131 and the N⁴-scaled denominators suggest a clean rational in N). Nice-to-have, not needed for the weld.
2. **Insert one of the §2 variants** into Paper 21 (Variant A) or Paper III (Variant B) when the manuscripts are next touched — but per the program's "papers lead, process in full" rule and the A2 constraint, that edit is deferred to the manuscript owner; this note is the staging.
3. **Hand the 914-vertex census to B2** if B2's conductor-fusion formalism wants a quartic test case; the per-prime-set breakdown is already exact in cert check D.
4. **(For C2)** state the quantum version of Prop 7.2 as a question: does the Kubo–Mori (dually-flat) member keep the 2+2 block in the e-chart while Bures smears it? This is the natural D4 + A2 merge.
