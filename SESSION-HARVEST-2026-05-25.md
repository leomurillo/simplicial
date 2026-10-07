# Session Harvest — May 25, 2026 (pre-compaction)

*Top-of-mind state of the simplicial program's GRH-attack work. Written before context compaction. Read first on resumption.*

---

## 1. Program-level status

### Four-axis framework — LOCKED

| Paper | Axis | Status |
|---|---|---|
| **T0** | gauge $\beta$ + label $c$ | locked |
| **T7 v2** | phase (Hopf/toric/Kummer cover) | locked, with §5 full Kummer-cover theorem and §6 qubit anchor |
| **T8 v3** | unit $\psi$ (multiplicative apex) | locked, with rigorous §4.3 apex bridge |
| **T9 v2** | Helmert-Fourier transfer matrix | locked, with Parseval-based unitarity |
| **T10 v3** | Kummer clock / m-power gauge | locked, with $N \mid m$ direction corrected throughout |

### Application sequence

| Paper | Delivers | Status |
|---|---|---|
| **T9.4 v2** | A5 (Helmert-Gauss decomposition) | locked, Bilateral $U \cdot W = D^{\mathrm{rad}} \cdot V^{\mathrm{Gauss}}$ + Kloosterman-like kernel |
| **T8.4 v1** | A4 (Stieltjes positivity of prime-side J) | **draft has a real gap — see §3 below**. Conditional Theorem E is true via signed-measure proof (§3.3); Lemma 6.4 is empirically false; §6–§7 machinery needs rework before v2 lock |

### Tier-A pending GRH-attack roadmap

| ID | Theorem | Status |
|---|---|---|
| A1 | Pass-8 Cesàro identity at all rungs | infrastructure ready (T8 + T9.4); focused application paper next |
| A2 | extend subagent A's N=6 to general primorial | needs T9.5 (spectral theory of $U$); then T7 §6.5 phase-twisted Lee-Yang generalization |
| **A3** | **Kummer cover at integer β** | **DELIVERED in T7 §5 Theorem 5.2** |
| A4 | $J^{\mathrm{prime,joint}}(N) \succeq 0$ unconditional | partially delivered: T8.4 has conditional Layer-3 proof via signed-measure (§3.3 of T8.4); unconditional Layer-1 still open |
| **A5** | **Helmert-Fourier prime-side at primorial** | **DELIVERED in T9.4 (Theorem D, Corollary 5.1)** |
| A6 | Bures / density-matrix apex (T13 forward) | not GRH-critical |
| C1 | LMFDB-completeness at primorial scale | external classical NT (Turing-method work) |

**Score: 2 fully delivered (A3, A5); 1 conditionally delivered (A4); 2 with complete infrastructure pending focused paper (A1, A2); 1 forward; 1 external.**

---

## 2. Empirical/numerical anchors built this session

### Joint primorial Apex Lemma verifications

- **`extend_GRH210_v6.py`** + **`zero_data_N210.py`** — full 48-L-function LMFDB coverage at N=210, dps=500. H_n, J_n PSD verified at every sampled n through 60.
- **`extend_GRH30_high_precision.py`** — N=30 (8 L-functions) at dps=300.

### Arch/prime decomposition probes

- **`probe_arch_prime_hankel.py`** — single-zeta antagonism documented.
- **`probe_arch_prime_N210_joint.py`** — joint primorial duality at N=210. Empirically: $J^{\mathrm{prime,joint}}(210) \succeq 0$ at every tested n with min LDL diag ~0.84. Strongest empirical signal in the program.
- **`probe_arch_theorem_verification.py`** — cross-N structural duality at N ∈ {1, 5, 6, 7, 15, 30, 210}.
- **`probe_arch_prime_N210_joint.py` companion**: showed $H^{\mathrm{prime}}$ indefinite, $H^{\mathrm{total}}$ PSD; $J^{\mathrm{arch}} \preceq 0$, $J^{\mathrm{prime}} \succeq 0$ — the structural duality.

### Apex-H attack probe

- **`probe_apex_H_attack.py`** — per-conductor decomposition at N=210. chi_105 sector dominates ($\mu_0^{\mathrm{prime,105}} = +116.90$ vs $\sum$ others $= -14$). Identified $\gamma_{\min}=0.141$ from chi_105(44).

### Two-axis (N, m) probe — THIS SESSION'S MAIN STRUCTURAL FINDING

- **`probe_two_axis_N_m.py`** — tested gauge rungs $m \in \{2, 4, 6\}$ at $N \in \{30, 210\}$, dps=600.
- **Finding: m=2 is structurally optimal.** Higher m doesn't add analytical content — at N=210, single-atom (chi_105(44)) dominance is asymptotically perfect (ratio 1.000000 at k=10) for all $m$. Higher m only concentrates dominance more, doesn't reveal new structure. Low-k multi-atom richness is maximized at m=2. **The program's focus on m=2 was correct from the start.** No missed simplicial power at higher rungs.

### T8.4 Lemma 6.4 falsification probes — THIS SESSION'S MAIN OPEN ISSUE

- **`probe_T8p4_lemma_6p4_Q_matrix.py`** (team-written): Q_re fails PSD at every n≥1 at N∈{30,210}. Axis sequence sign-flips at k ≈ 0.7N.
- **`probe_T8p4_lemma_6p4_variants.py`** (director-added): all variants (|Re|, |.|, |.|²) also fail PSD at n=1 via Cauchy-Schwarz violation.

---

## 3. T8.4 v1 status — the open issue

**T8.4 v1 has a real proof gap.** Lemma 6.4 (the kernel-positivity claim invoked by Theorem E §7.2) is empirically false. The conditional Theorem E itself remains true via the signed-measure argument in §3.3 (Corollary 3.3), but the §6–§7 machinery doesn't deliver the gap-closing argument as written.

**Documented in:** `T8.4-Lemma-6p4-Falsification-Note.md`

**Recommended fix for T8.4 v2 (Option 1 + Option 3 from the note):**
1. Route Theorem E §7.2's proof through Corollary 3.3 (signed-measure argument). This is rigorous and matches the editing-pass discipline §10's stated conditional level.
2. Reframe §6–§7's Helmert-Gauss machinery as forward target for the Layer-2 quantitative path (T8.4.1), not as the conditional proof itself.
3. Acknowledge in §10 that the conditional proof goes through §3.3, and that Lemma 6.4 as stated is empirically false; the right reformulation is open work.

**A4 is still delivered at Layer-3** (conditional on GRH$_N$) via the signed-measure proof. The honest framing T8.4 §10 already supplied is the right framing; only the §7.2 proof routing needs to change.

---

## 4. Foundational papers — cross-paper observations from inserts

### T9.4-PreviousPapersInsert.md
- Item 5 (Lemma 6.4 was sketched, now empirically falsified — see above)
- Item 6: T8 §6.2 has conductors of $\chi_4$ and $\chi_{-8}$ swapped at N=8. T8.4 doesn't invoke N=8 so doesn't propagate. Worth fixing in next T8 revision.
- Item 1: T9 §7.4 forward door is closed by T9.4 Theorem A. Worth noting in future T9 revision.

### T8.4-PreviousPapersInsert.md
- Item 5 substantive: Lemma 6.4 sketched. Falsification confirms the gap is real.
- Item 7: Recommends mirror probe at N=30 of `probe_arch_prime_N210_joint.py` for cross-N empirical anchor. Not yet done.
- Item 1: ArchStruct §7.3 Conjecture 7.3 closed conditionally by T8.4 Theorem E (via the §3.3 proof, not the §7.2 one).

---

## 5. Key directories and files

```
C:/Projects/simplicial/
├── T0–T10, T9.4 — locked foundational/application papers
├── T8.4-StieltjesPositivityPrimeMultiplicativeApex-Draft1.md — needs v2 rework
├── T8.4-Lemma-6p4-Falsification-Note.md — director's diagnostic
├── T8.4-PreviousPapersInsert.md, T9.4-PreviousPapersInsert.md — cross-paper observations
├── Arch-Structural-Theorems-Draft1.md — load-bearing arch structural theorems (Thm 1, Cor 2, Thm 3)
├── Arch-Prime-N210-Duality-Draft1.md — joint primorial duality writeup
├── Arch-Prime-Cancellation-Probe-Draft1.md — single-zeta antagonism
├── Apex-H-Attack-Draft1.md — Apex-H pending direction
├── GRH30-Apex-Verification-Note-Draft1.md — Draft 3 with N=30 + N=210 complete
├── PassFive-Section17-Audit-Draft1.md — Pass-5 §17 No-Isolator audit
├── zero_data_N210.py — full LMFDB zero data, all 48 L-functions
├── extend_GRH210_v6.py, extend_GRH30_high_precision.py — Apex Lemma verifications
├── probe_arch_prime_*.py — duality probes
├── probe_apex_H_attack.py — per-conductor prime decomposition
├── probe_two_axis_N_m.py — m-rung comparison (m=2 optimal)
├── probe_T8p4_lemma_6p4_*.py — Lemma 6.4 falsification probes
├── T9.4-DraftPrompt.md, T8.4-DraftPrompt.md — drafting prompts
```

---

## 6. Active decisions / direction

### Settled this session

1. **T7–T10 + T9.4 are locked.** Four-axis framework + first application paper.
2. **m=2 is the right gauge rung.** Two-axis probe confirms; no missed power.
3. **Subagent A's N=6 result + T7 §6.5's qubit phase-twisted Lee-Yang** is the simplicial-side geometric GRH analog. Generalization to primorial is A2 (via T9.5).
4. **A1 is the natural next application paper** after T8.4 v2 lock — uses T8 + T9.4 + (now) T8.4's signed-measure framework.
5. **T8.4 needs v2 rework** (Lemma 6.4 falsification) before launching A1.

### Open / next session

1. **T8.4 v2** — apply the fix from `T8.4-Lemma-6p4-Falsification-Note.md` (route Theorem E through §3.3 signed-measure proof; reframe §6–§7 as Layer-2 forward target).
2. **A1 (Pass-8 Cesàro at all rungs)** — focused application paper, draft prompt ready after T8.4 v2 locks.
3. **Mirror probe at N=30** — `probe_arch_prime_N30_joint.py` analogous to N=210, for cross-N empirical anchor.
4. **Then A2 / T9.5** — spectral theory of Helmert-Fourier matrix, extends subagent A's N=6 to general primorial.

---

## 7. Strategic posture

### What's structurally proven

- ArchStruct Theorem 1: joint arch is positive atomic measure on $(-\infty, 0)$ at primorial $N \ge 30$ — **unconditional**.
- ArchStruct Corollary 2: $H^{\mathrm{arch}} \succeq 0$, $J^{\mathrm{arch}} \preceq 0$ — **unconditional**.
- T7 §5 Theorem 5.2: Kummer cover deck-group action $\rho_m(\zeta) = \zeta^{-m}$, trivial iff $N \mid m$.
- T9.4 Theorem A: $S_k(\psi) = \sum_{j=0}^{k-1} \tau(\psi, j) - k\tau(\psi, k)$ — **unconditional algebraic identity**.
- T9.4 Theorem C: bilateral factorization $U \cdot W = D^{\mathrm{rad}} \cdot V^{\mathrm{Gauss}}$ — **unconditional**.
- T9.4 Corollary 5.1: Kloosterman-like kernel $T_N(n,a) = \varphi(N) \omega^{a n^{-1}}$ — **unconditional**.

### What's conditionally proven (RH/GRH$_N$)

- T8.4 Theorem E via signed-measure (§3.3 of T8.4): $J^{\mathrm{prime,joint}}(N) \succeq 0$ at primorial $N \ge 30$.

### What's empirically validated but unproven

- $J^{\mathrm{prime,joint}}(210) \succeq 0$ at every tested rung n ≤ 14 at dps=300 — independent of GRH.
- Apex Lemma$_{HJ}$ verified through n=60 at N=210 (full LMFDB coverage), conditional on LMFDB-completeness.
- Single-atom (chi_105(44)) dominance is asymptotically perfect at N=210 — the joint cumulants reduce to effectively rank-1 from moderate k.

### What's open

- **Apex-H** at primorial $N$ (the H side of Apex Lemma$_{HJ}$). Requires bounding $H^{\mathrm{prime}}$'s indefiniteness against $H^{\mathrm{arch}}$'s positivity gap. Forward target: T8.4.2 (Apex-H paper).
- **Unconditional A4** (without GRH$_N$ assumption): Lemma 6.4 was the attempted path; it failed. New approach needed.
- **Subagent A's N=6 generalization** to primorial (A2, via T9.5 spectral theory).

---

## 8. One-paragraph summary

The simplicial GRH-attack program has four locked foundational papers (T7–T10 + T9.4) implementing a four-axis apex framework (gauge × label × phase × unit). Two of seven Tier-A theorems are delivered unconditionally (A3 via T7 §5, A5 via T9.4); one is delivered conditionally on RH/GRH$_N$ via signed-measure argument (A4 via T8.4's Corollary 3.3, after a kernel-positivity attempt in Lemma 6.4 was empirically falsified — see falsification note). The strongest empirical anchor is `probe_arch_prime_N210_joint.py` showing $J^{\mathrm{prime,joint}}(210) \succeq 0$ at every tested rung. The two-axis (N, m) probe confirms m=2 is structurally optimal — no missed power at higher gauge rungs. T8.4 needs a v2 rework routing Theorem E's proof through the signed-measure argument (§3.3) rather than the falsified Lemma 6.4. After T8.4 v2 locks, the next application paper is A1 (Pass-8 Cesàro at all rungs) using the T8 + T9.4 infrastructure. The polymath/external dependency (C1: LMFDB completeness at primorial scale) is genuinely the last step.

— Director, May 25, 2026 (pre-compaction)
