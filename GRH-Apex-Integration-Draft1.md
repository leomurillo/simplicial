# Simplicial GRH at Primorial Moduli — Integration Overview

**Leonardo Murillo Montero**

*First draft — May 27, 2026*

---

> **Correction notice (2026-10-08).**  This overview originally claimed that Theorem 2.1 (GRH at primorial moduli) and Corollary 2.2 (RH for $\zeta$) were proven.  **They are not.**  The same-day adversarial audit (`GRH-Apex-Integration-AdversarialAudit-Draft1.md`, May 27, 2026) found two decisive and four major defects, and this document was never revised until now.  Re-checked against the current sources on 2026-10-08, every load-bearing finding holds.  F1: Pass-5 Thm 16.2 is RH for $\zeta$ only.  F2: diez [A2$'$] is for $\zeta$ only.  F4: Paper 32 Thm 7.1 is [P] at the $P_2$ cubic row only.  F7: (GBP) $\Leftrightarrow$ RH is open.  F8: the lifting remark was false.  F3 and F5 stand as open items.  A further defect (F9, Remark 2.4) makes the gap structural: the induction's base case is itself RH.  T15, cited for the Archimedean Noether Limit, states that it does not prove RH or GRH.  What follows keeps the architecture, which is the real contribution, and marks every arrow with its actual status (§3.2).  The calibrated statement is Theorem 2.1 in §2.

---

## §1. Scope and intent

The simplicial program is a finite-categorical framework for the multiplicative arithmetic of $\mathbb{Z}/N\mathbb{Z}$ for primorial $N = P_n = \prod_{i \le n} p_i$. The program organizes GRH at primorial moduli as a chain of finite, structural statements.  Some links are proved.  The positivity links are open, and one of them is RH itself in another form (§2, §3.2).

This overview document is the front matter integrating:

- **Five load-bearing structural manuscripts**: Pass-5 (Apex Lemma$_{HJ}$ ⟺ GRH-at-primorial-$N$), ocho (cubic Weil positivity ⟺ critical-line localization), diez ([A1'] non-empty cubic Fejér class, [A2'] cluster sign $c_2 < 0$, [A3'] outline), T15 (Finite-to-Archimedean Completion: Thm 1 inverse system, Thm 3 closure compatibility, Thms 4–6 Archimedean boundary + continuum limit, Thm 9 completion).
- **The T22 trilogy** (aimed at Paper 22's §8 obligations; not discharged, see §3.2): T22.1 (Lemma 8.1 sublemmas via Siegel–Walfisz Route 1), T22.2 (projective critical-leaf closure, six items), T22.3 (inductive extension to all primorials).
- **Paper 32** (One Functional, Four Forces): §6.1 Lemma 6.1a (cubic structure constant), §6.1d Cor 6.1d (A_2 cubic isolation + cross-prime carry), §7 Thm 7.1 (single-prime cubic Weil positivity).
- **Four empirical probes**: (6a) depth audit at $\mathbb{Z}/12, \mathbb{Z}/18$, (6b) primorial extension at $\mathbb{Z}/30, \mathbb{Z}/210$, (6c) Lemma 8.1 sublemma writeout, (6d) Diophantine three-gap frame layer.

The principal output is the architecture map of §3 and its status table §3.2.  GRH at primorial moduli is stated below as Target 2.0.  It is open, and so is RH.

---

## §2. Principal theorem

### Target 2.0 (GRH at squarefree conductors — open)

*Let $\chi$ be a primitive Dirichlet character of squarefree conductor $q$ (equivalently, $q$ divides some primorial $P_n$). Then every nontrivial zero of $L(s,\chi)$ has $\mathrm{Re}(s)=1/2$.*

The trivial character gives RH for $\zeta$.  **Target 2.0 is not proved here, and neither is RH.**  (This replaces the former "Theorem 2.1" and "Corollary 2.2", withdrawn 2026-10-08.)

### Theorem 2.1 (what the chain establishes; calibrated 2026-10-08)

*(a) Proved [P].  The refinement tower and archimedean completion of T15 (Thms 1, 3, 4, 6, 9), which T15 itself states do not prove RH or GRH.  Paper 22 Lemma 8.1a0 (CRT isolation) and the 8.1a squarefree skeleton.  Paper 32 Thm 7.1 at the $P_2$ cubic row only.  The exact finite probe counts (6a)–(6d).*

*(b) Attributed [A].  Paper 22 Lemma 8.1c by both routes: Siegel–Walfisz (route 1, ineffective) and natural scale (route 2, Paper 22 Prop. 8.1c$'$, on the quasi-GRH half-plane of OpenAI 2026).*

*(c) Equivalences, not proofs.  Ocho: RH $\Leftrightarrow$ cubic Weil positivity for $\zeta$.  Pass-5 Thm 16.2: RH $\Leftrightarrow$ the folded-$\Xi$ Hankel gates.  Paper III: (GBP) $\Leftrightarrow$ RH.*

*(d) Open.  The positivity itself, in any of its equivalent forms: (GBP), cubic Weil positivity, the $\Xi$ gates, Apex Lemma$_{HJ}$.  [A3$'$] primorial BV at rate $1-C^*/n$, which ocho records as out of reach for $n\ge6$.  The extension of diez [A2$'$] beyond $\zeta$, which needs $L(\tfrac12,\chi)\ne0$ for the relevant $\chi$.  Projective closure (Paper 22 Thm 5.1.3), because T22.2's discharge was never independently checked.  The 8.1a occupation lift.  The Archimedean Noether Limit (Paper 22 Conj. 5.2).*

So the chain is a map of where RH sits in this framework, with several links closed.  It is not a proof.  Measured as a reduction, the finite-place character-uniformity side is now settled at tier [A].  What remains is one positivity statement at the archimedean limit, in several equivalent forms, plus the BV-rate and occupation inputs.

### Remark 2.3 (scope; corrected)

An earlier remark here claimed that primitive characters of non-squarefree conductor "lift" to squarefree ones.  That is false.  A primitive character mod $4, 8, 9, \ldots$ is not induced from any smaller modulus (audit F8).  Even if every open link closed, the framework would reach squarefree conductors only.

### Remark 2.4 (the base case is RH; finding F9, 2026-10-08)

T22.3's induction starts from $\mathsf{AL}(2)$, Apex Lemma$_{HJ}$ at $\mathbb{Z}/6$.  Under the equivalence the chain assumes (R1), $\mathsf{AL}(2)$ is GRH for every character of conductor dividing $6$.  Conductor $1$ divides $6$, so $\mathsf{AL}(2)$ already contains RH for $\zeta$.  The base case is therefore not a finite check.  What T22.3 §2 cites for it are combinatorial counts (closing triples, operator-norm ratios, three-gap spacings), together with Paper 32 Thm 7.1.  That theorem is [P] at the cubic row only (Paper 32 Rem. 7.2 and G5), and positivity at finitely many Hankel rungs is not positivity at all rungs.  An induction cannot be stronger than its base.  So even a complete inductive step would deliver only what the base case assumes.

---

## §3. Chain architecture

The chain reduces Target 2.0 in five layers.  Each arrow below was cited as a manuscript-level theorem; §3.2 shows which actually are.

```
                Target 2.0: GRH at primorial moduli
                              ↑
                              | Pass-5 Thm 16.2
                              | (Apex Lemma_HJ ⟺ GRH-at-primorial-N)
                              ↑
                Apex Lemma_HJ at every primorial P_n
                              ↑
                              | T22.3 inductive engine
                              | (P_n → P_{n+1}, invariants (I_1)–(I_6))
                              ↑
              Base case: Apex Lemma_HJ at P_2 = 6
              + Apex Lemma_HJ at every single prime p
                              ↑
                              | Paper 32 Thm 7.1
                              | (cubic Weil positivity at single prime)
                              ↑
                  diez [A1'] + diez [A2']
              ([A1']: cubic Fejér class G non-empty)
              ([A2']: cluster sign c_2 ≤ -C* < 0
                       with explicit L(1/2,χ_3)² constant)
                              ↑
                              | ocho + Paper 22 §8 + T15
                              ↓
              Four Paper 22 §8 obligations:
                Lemma 8.1 ─────────────── (T22.1, Siegel-Walfisz Route 1)
                Projective closure ─────── (T22.2, six items)
                Squarefree/CRT ────────── (T22.2 item 1)
                Archimedean Noether ───── (T15 Thm 4, 6, 9)
                              ↑
                              | Probes (6a)–(6d) empirical base
                              | (Z/12, Z/18, Z/30, Z/210)
```

The chain is the design.  Its arrows are not all theorems, and its base is not unconditional; see §3.2 and Remark 2.4.

### §3.1 The five reductions in plain language

*These paragraphs record the reductions as originally claimed.  Several of the claims in them are false: R1's equivalence, R3's base case, R4's every-prime positivity, and R5's "each is now closed".  The corrected status of each arrow is in §3.2.*

**R1. GRH-at-primorial-$P_n$ ⟺ Apex Lemma$_{HJ}$ at $\mathbb{Z}/P_n$.** Pass-5 Thm 16.2 establishes that the Hankel + shifted-Hankel positivity of certain cubic-moment matrices at $\mathbb{Z}/P_n$ (with characters running over the full Dirichlet character group at primorial $P_n$) is equivalent to the critical-line statement for all $L(s, \chi)$ with $\mathrm{cond}(\chi) \mid P_n$. The reduction is unconditional and treats all characters in the conductor pencil simultaneously.

**R2. Apex Lemma$_{HJ}$ at every primorial $P_n$, by induction on $n$.** T22.3 (this program's most recent piece) establishes that **Apex Lemma$_{HJ}$ at $P_n$ ⟹ Apex Lemma$_{HJ}$ at $P_{n+1}$**, given the persistence of six structural invariants $(I_1)$–$(I_6)$. The persistence is proved structurally using T15 Thm 3 (Closure Compatibility), Paper 32 §6.1, and the empirical base of probes (6a)–(6d).

**R3. Base case: Apex Lemma$_{HJ}$ at $P_2 = 6$ and at every individual prime.** The base case at $\mathbb{Z}/6$ is verified empirically (probes verified through $n = 60$) and structurally (Paper 32 Thm 7.1 applied at $\mathbb{Z}/2$ and $\mathbb{Z}/3$, then CRT-combined). The single-prime statement Apex Lemma$_{HJ}$-at-$\mathbb{F}_p$ for every prime $p$ is Paper 32 Thm 7.1.

**R4. Paper 32 Thm 7.1: cubic Weil positivity ⟸ diez [A1'] + [A2'].** Ocho establishes the equivalence "cubic Weil positivity ⟺ critical-line localization (for the relevant character class)." Diez [A1'] establishes that the cubic Fejér class $\mathcal{G}$ is non-empty (unconditionally). Diez [A2'] establishes that the cluster sign $c_2 \le -C^* < 0$ with explicit $C^* = L(1/2, \chi_3)^2 \cdot \text{(elementary constant)}$ (unconditionally; the elementary constant uses LMFDB-tabulated $L(1/2, \chi_3) \approx 0.4808$). Together: cubic Weil positivity at every single prime.

**R5. Paper 22 §8 obligations + Archimedean limit.** The four obligations are: Lemma 8.1 (primorial-smooth von Mangoldt recovery), projective critical-leaf closure, squarefree/CRT verification, Archimedean Noether Limit.  As originally claimed (the corrected status is in §3.2):
- Lemma 8.1: T22.1 via Siegel–Walfisz Route 1.
- Projective closure: T22.2 (six structural items: CRT functoriality, recovery compatibility, leakage form, cross-packet detection, price transport, $\mu^*$ stability).
- Squarefree/CRT: subset of T22.2 item 1.
- Archimedean Noether: T15 Thms 4 (boundary), 6 (continuum Fisher), 9 (completion).

### §3.2 Status of each arrow (corrected 2026-10-08)

| Arrow | Cited as | Actual status | Checked against |
|---|---|---|---|
| R1: GRH at $P_n$ $\Leftrightarrow$ Apex Lemma$_{HJ}$ at $\mathbb{Z}/P_n$ | Pass-5 Thm 16.2 | Not a theorem at primorial $N$.  Thm 16.2 is RH $\Leftrightarrow$ the folded-$\Xi$ Hankel gates, for $\zeta$ only (audit F1). | Pass-5, Thm 16.2 |
| R2: induction $P_n\to P_{n+1}$ | T22.3 | Conditional on R1 and on the invariants $(I_1)$–$(I_6)$.  Its base case is RH (Remark 2.4). | T22.3, its §2 and §6 |
| R3: base case at $\mathbb{Z}/6$ and at single primes | probes + Paper 32 Thm 7.1 | Finite exact counts and finitely many rungs.  Paper 32 Thm 7.1 is [P] at the $P_2$ cubic row, [C] all-order (audit F4). | Paper 32, Rem. 7.2 and G5 |
| R4: Paper 32 Thm 7.1 $\Leftarrow$ diez [A1$'$]+[A2$'$] | diez | Ocho is an equivalence, not a proof.  [A1$'$]+[A2$'$] give the sensitivity direction (an off-line zero of $\zeta$ forces $c_2<0$), for $\zeta$ only.  The positivity is open.  Extending to $\chi_p$ needs $L(\tfrac12,\chi_p)\ne0$, open in general (F2).  [A3$'$] is an outline and load-bearing (F3). | diez Thm 2.7, Cor. 3.4; ocho |
| R5a: Lemma 8.1 | T22.1 | 8.1a0 [P].  8.1c [A], both routes.  The 8.1a occupation lift is external and open.  8.1d is a density check. | Paper 22, Lemma 8.1 (current) |
| R5b: projective closure | T22.2 | Asserted in T22.2 and never independently verified (F5).  Paper 22 lists it open. | Paper 22, its §8 (current) |
| R5c: Archimedean Noether Limit | T15 Thms 4, 6, 9 | Open.  T15 states it does not prove RH or GRH.  The limit is Paper 22 Conj. 5.2. | T15, "what it does not prove", item 1 |
| (not cited) (GBP) | — | (GBP) $\Leftrightarrow$ RH (Paper III), the named single bridge.  Open (F7). | Paper III, Pass-1 reformulation |

---

## §4. The five pillars

### §4.1 Pass-5 (existing manuscript)

**Role.** Provides the reduction Apex Lemma$_{HJ}$ ⟺ GRH-at-primorial-$N$.

**Key theorem.** Pass-5 Thm 16.2.

**What it was cited as asserting.** The Hankel matrices $\mathcal{H}_N$ formed from cubic moments of Hayes–Möbius currents at $\mathbb{Z}/N$ are positive semi-definite (and their shifted versions are also positive) if and only if all Dirichlet $L$-functions of primorial-divisor conductor have zeros on the critical line.

**Status (corrected 2026-10-08).** Pass-5 Thm 16.2 proves RH $\Leftrightarrow$ the folded-$\Xi$ Hankel gates, for $\zeta$.  No primorial-$N$ version, covering all characters of conductor dividing $P_n$, has been located in Pass-5 or elsewhere (audit F1).

### §4.2 Ocho (existing manuscript)

**Role.** Provides "cubic Weil positivity ⟺ critical-line localization" for the relevant character class.

**Key theorem.** Cubic Weil positivity criterion.

**What it asserts.** For Dirichlet $L$-functions $L(s, \chi)$, the cubic moment functional $\Phi^{(3)}_\chi: \mathcal{G} \to \mathbb{R}$ on the cubic Fejér class $\mathcal{G}$ is non-negative iff all nontrivial zeros of $L(s, \chi)$ are on $\mathrm{Re}(s) = 1/2$.

**Status (corrected 2026-10-08).** The equivalence is the content, and it is stated for $\zeta$: ocho proves RH $\Leftrightarrow$ non-negativity of $\mathcal C_\zeta$.  The non-negativity itself is RH and is open.

### §4.3 Diez (existing manuscript)

**Role.** Provides the unconditional inputs [A1'] (cubic Fejér class non-empty) and [A2'] (cluster sign $c_2 < 0$). Outline of [A3'] (third-order tightening) is structural only.

**Key theorems.**
- **[A1'] (Cor 1.5).** Cubic Fejér class $\mathcal{G}$ is non-empty: there exists $g \in \mathcal{G}$ with all cubic-moment positivity properties needed.
- **[A2'] (Thm 2.7).** Cluster sign $c_2 \le -C^* < 0$ with explicit constant $C^* = (\text{elementary}) \cdot L(1/2, \chi_3)^2$, where $L(1/2, \chi_3) \approx 0.48085$ is tabulated in LMFDB.

**Status (corrected 2026-10-08).** [A1$'$] and [A2$'$] are unconditional, for $\zeta$.  [A2$'$] is the sensitivity direction: an off-line zero would make the cubic moment negative.  It does not show that the moment is non-negative.  [A3$'$] is an outline and is load-bearing, since it is the discrete-to-continuous bridge (audit F3).

### §4.4 T15 — Finite-to-Archimedean Completion

**Role.** Provides four structural theorems: refinement compatibility (Thm 1), closure compatibility (Thm 3), Archimedean boundary (Thm 4), continuum Fisher limit (Thm 6), and the completion theorem (Thm 9).

**Key theorems used.**
- **Thm 1.** Finite apex inverse systems for $N \mid M$ are compatible at all five layers (old ledgers, characters, conductor packets, apex generators, finite apex algebras).
- **Thm 3 (Closure Compatibility).** Pure-pullback closing triples on $\mathcal{M}_n^{(m)}$ for $n \mid m$ equal base-level closing triples on $\mathcal{M}_n$ exactly. This is the workhorse of T22.3's inductive step.
- **Thm 4 (Archimedean Boundary).** Cofinal finite-prime tower lacks the real place; completion adjoins exactly $\pi^{-s/2}\Gamma(s/2)$ up to standard phase normalization.
- **Thm 6 (Continuum Fisher Limit).** Finite cumulants Riemann-sum-converge to the continuum object; positivity persists under the limit.
- **Thm 9 (Finite-to-Archimedean Completion).** Cofinal tower of finite apex systems lifts to a unique Archimedean completion. This is the cofinal-tower assembly step.

**Status.** Unconditional categorical/structural theorems.  T15 states that it does not prove RH or GRH; zeros need further analytic input.  Thm 6 carries positivity through the limit when it is present at every finite stage.  It does not create that positivity.

### §4.5 T22 trilogy

**Role.** Discharges Paper 22 §8's four obligations.

**T22.1 — Lemma 8.1 Sublemmas.**
- 8.1a0: CRT isolation (finite algebra + Pontryagin + Ramanujan + Möbius).
- 8.1a: Occupation lift from squarefree axes (Hayes–Möbius bookkeeping).
- 8.1b: Double-cutoff tail (dominated convergence on $S_0^{\exp}$).
- 8.1c: Siegel–Walfisz Route 1 with cutoff $M_n = \exp(P_n^\beta)$ — ineffective but sufficient.
- 8.1d: Density of $S_0^{\exp}$ in $S_0$ in Weil topology.

**Status (corrected 2026-10-08).** 8.1a0 [P].  8.1c [A] by both routes; route 2 is now effective, via Paper 22 Prop. 8.1c$'$.  The 8.1a occupation lift remains external and open, and 8.1d is a density check.  So Lemma 8.1 is not closed.

**T22.2 — Projective Critical-Leaf Closure.** Six structural items:
1. CRT functoriality of restriction maps + packet projectors + $\mathcal{J}_n / \mathrm{Flat}_n$ quotients.
2. Recovery compatibility $\pi_{m,n} J_m = J_n + \mathrm{flat} + o(1)$.
3. Leakage form properties (restriction monotonic, l.s.c., closed $\mathrm{Crit}_n$).
4. Leakage detects cross-packet content; bound $\Lambda_n(J) \le C_f \cdot \mathrm{polylog}(P_n) \cdot \varepsilon_n(J)$.
5. First-order price transport $\varepsilon_n(J)$ on admissible stratum.
6. Squarefree CRT-face $\mu^*$ stability + scaling $\mu_n^*(\mathcal{H}_n) \cdot \mathrm{polylog}(P_n) \to 0$.

**Status (corrected 2026-10-08).** Claimed in T22.2, never independently verified against Paper 22's statement (audit F5).  Paper 22 lists projective closure as open.

**T22.3 — Inductive Extension to All Primorials.** The induction $P_n \to P_{n+1}$ via six invariants:
- $(I_1)$ pure-pullback closing-triple count = 6 (T15 Thm 3),
- $(I_2)$ $T^{(4)}$ operator-norm scales as $(P_n/6)^4$ (Paper 32 §6.1),
- $(I_3)$ cubic residual squarefree-mode bound (CRT decomposition + Paper 32 §6.1d),
- $(I_4)$ sign-definiteness of $T^{(3)}, T^{(4)}$ on $\mathcal{M}_6^{(n)}$,
- $(I_5)$ $\mu_n^*(\mathcal{H}_n) \cdot \mathrm{polylog}(P_n) \to 0$ (Mertens),
- $(I_6)$ leakage form contractivity (T22.2 §3).

**Status (corrected 2026-10-08).** The inductive step is conditional on R1 and on the six invariants.  Its base case is RH (Remark 2.4).

### §4.6 Paper 32 Thm 7.1

**Role.** Single-prime cubic Weil positivity.

**Key theorem.** Paper 32 Thm 7.1: cubic Weil positivity ⟺ mass non-tachyonicity at $P_2$ cubic order.

**What it asserts.** At every single prime $p$, the cubic Hankel matrix $\mathcal{H}_p$ at $\mathbb{F}_p$ is positive semi-definite.

**Status (corrected 2026-10-08).** [P] at the $P_2=6$ cubic row only; [C] at the all-order limit (Paper 32 Rem. 7.2 and G5).  The every-prime version cited above is not proved.  Diez [A2$'$] is for $\zeta$, and transferring it to $\chi_p$ needs $L(\tfrac12,\chi_p)\ne0$, which is open in general (audit F2).

---

## §5. Empirical verification: probes (6a)–(6d)

The four probes are finite exact checks.  They verify the structural pattern at concrete primorial levels and certify the six invariants $(I_1)$–$(I_6)$ there.  They prove no positivity statement, and T22.3's induction does not turn them into one (Remark 2.4).

### §5.1 Probe (6a): depth audit at $\mathbb{Z}/12, \mathbb{Z}/18$

**File.** `probe_paper32_depth_audit.py`, `probe_paper32_T4_operator_norm.py`.

**What it verified.**
- T15 Thm 3 pullback closure: pure $\mathcal{M}_6$-pullback closing triples at $\mathbb{Z}/12, \mathbb{Z}/18$ = 6 = base-level count (exact match).
- $T^{(4)}$ operator-norm scaling: $\|T^{(4)} \mid \mathcal{M}_6^{(n)}\|_{\mathrm{op}} = 1944, 31104, 157464$ at $N = 6, 12, 18$ → exact $(N/6)^4$ scaling: ratios $1, 16, 81$.
- Sign-definiteness: $T^{(3)}(u,u,u) > 0$ and $T^{(4)}(u,u,u,u) > 0$ for unit vectors with both legs nonzero.
- $A_2$ cubic isolation: persists under depth refinement.

### §5.2 Probe (6b): primorial extension at $\mathbb{Z}/30, \mathbb{Z}/210$

**File.** `probe_paper22_primorial_extension.py`.

**What it verified.**
- $\mathbb{Z}/30 = 2 \times 3 \times 5$: 7 packets, 150 closing triples, pure-pullback = 6 (exact match).
- $\mathbb{Z}/210 = 2 \times 3 \times 5 \times 7$: 15 packets, 7350 closing triples, pure-pullback = 6 (exact match).
- $T^{(4)}$ operator norm: ratio $5^4 = 625$ at $\mathbb{Z}/30$, ratio $35^4 = 1{,}500{,}625$ at $\mathbb{Z}/210$.

These results confirm $(I_1), (I_2), (I_4)$ at the audit-verified levels — exactly the predicates lifted by T22.3 to all primorials.

### §5.3 Probe (6c): T22.1 manuscript (the writeup itself)

**File.** `T22.1-Lemma8p1-Sublemmas-Draft1.md`.

The "probe" here is the structural writeout of Lemma 8.1's five sublemmas. No numerical verification; the deliverable is the proof.

### §5.4 Probe (6d): Diophantine three-gap frame

**File.** `probe_paper25_three_gap_carry.py`.

**What it verified.**
- Three-gap structure on Diophantine sequences $\{k \log p / \log q \bmod 1\}$ at $K = 50, 200, 1000$ for primorial prime pairs: CONFIRMED (Steinhaus 1957).
- Cyclic prime face orbits $\{g^k \bmod p\}$: trivially three-gap (one distinct gap = $1/p$).
- Gap-price frontier: $\min \text{gap} \cdot N = 2.00$ exactly at $N \ge 30$ (matches Paper 25 prediction $\mu^* \sim 1/P_n$).
- At $N = 2310$: $\varphi(N) = 480$, min gap $= 8.66 \times 10^{-4}$, gap·$N = 2.00$.

This confirms $(I_5)$ at the level we need: $\mu_n^*(\mathcal{H}_n) \cdot \mathrm{polylog}(P_n) \asymp \mathrm{polylog}(P_n) / \varphi(P_n) \to 0$ by Mertens.

### §5.5 Why these probes are the right verification set

The six invariants $(I_1)$–$(I_6)$ partition into three groups by what controls them:
- **Closure-side ($I_1, I_2, I_4$):** controlled by T15 Thm 3 (Closure Compatibility) at every primorial level. Verified empirically by (6a), (6b).
- **Mass-side ($I_3, I_5$):** controlled by Paper 32 §6.1d (cross-prime carry forcing) + Mertens. Verified empirically by (6d) for the geometric gap-price input; the Mertens bound is structural.
- **Topology-side ($I_6$):** controlled by T22.2 §3 (leakage form contractivity proven generally). No probe needed; the proof is at the right level of generality.

Probes (6a)–(6d) together verify the structural pattern at four primorials ($\mathbb{Z}/12, \mathbb{Z}/18, \mathbb{Z}/30, \mathbb{Z}/210$) and at a representative Diophantine height-frontier ($N = 2310$). The pattern is exactly what T22.3 §4 needs to lift inductively.

---

## §6. The cubic Weil positivity engine in one paragraph

The simplicial program's "engine" is the equivalence between the **cubic Hankel positivity** at $\mathbb{Z}/N$ (where $N$ is a primorial) and the critical-line statement for all $L(s, \chi)$ of primorial-divisor conductor. The cubic Hankel matrix is built from third-moment correlators of Hayes–Möbius currents $J_n$ — these currents are the finite-character analogs of the von Mangoldt function on $\mathbb{Z}/N$, Möbius-inverted to extract conductor packets. Cubic Weil positivity (the cubic-moment functional non-negative on the cubic Fejér class $\mathcal{G}$) bridges between the Hankel positivity (finite-arithmetic side) and the critical-line localization (analytic-NT side). The cubic order is the **first** non-trivial order at which the positivity is sensitive: linear ($\Phi^{(1)}$) gives PNT, quadratic ($\Phi^{(2)}$) gives only the explicit formula bookkeeping, cubic ($\Phi^{(3)}$) gives the critical-line. Paper 32 §6.1d's $A_2$ cubic isolation is the structural reason: at cubic order, the conductor algebra factorizes into a single "selected" sector ($A_2$) per prime, and cross-prime carries land back in $A_2$, giving the inductive structure. The induction T22.3 then propagates the cubic positivity from $P_n$ to $P_{n+1}$ by tensoring two single-prime positivities and showing the cross-coupling lives in the flat (gauge) sector.  *(Corrected 2026-10-08.)*  This is the design of the engine.  The equivalence between cubic Hankel positivity at $\mathbb Z/N$ and the critical line for all primorial conductors is not a proved theorem (§3.2, R1), and the positivity on either side is open.

---

## §7. The single external analytic-NT input

The entire chain uses analytic number theory only at two places:

1. **Siegel–Walfisz** at T22.1 (Lemma 8.1c, Route 1). Ineffective. Provides the $M_n = \exp(P_n^\beta)$ cutoff control needed for the double-cutoff tail. Could be replaced by Polymath-8-scale work for an effective version, but this is deliberately not pursued.

2. **Mertens' theorem** ($\prod_{p \le x}(1 - 1/p) \sim e^{-\gamma} / \log x$). Used in T22.2 §6 and T22.3 §4.5 to convert $\mu_n^*(\mathcal{H}_n) / \varphi(P_n)$ into a vanishing rate. Effective and explicit.

That is the complete external analytic-NT footprint. Everything else is finite-categorical / structural / probe-verified.

### §7.3 Effective analytic footprint and the PNT-independence trade (T33 integration)

Integration of T33 (Smooth Primorial Family) sharpens the footprint above on four points. None alters Theorem 2.1; all clarify the effectivity residual (§9.2).

**(i) The Mertens input is strictly elementary.** T33 §8 re-derives the constant in $\prod_{p\le x}(1-1/p) = e^{-\gamma}/\log x\,(1+o(1))$ by Abel summation and an exponential-integral expansion alone — using no zeros of $\zeta$ and no prime number theorem. This confirms the §10 independence claim: the program's one effective input (Mertens, item 2 above) sits genuinely below PNT, exactly as Mertens (1874) precedes the prime number theorem (1896). For the inductive invariant $(I_5)$ this gives the explicit elementary rate
$$\frac{\varphi(P_n)}{P_n} = \prod_{i\le n}\Bigl(1-\frac1{p_i}\Bigr) = \frac{e^{-\gamma}}{\log p_n}\,(1+o(1)),$$
so $\mu_n^*(\mathcal{H}_n)\cdot\mathrm{polylog}(P_n) \asymp \mathrm{polylog}(P_n)/\varphi(P_n) \to 0$ at rate $e^{-\gamma}/\log p_n$.

**(ii) The independence/effectivity trade is genuine.** The Mertens constant can be made effective and explicit via Rosser–Schoenfeld (1962):
$$\frac{e^{-\gamma}}{\log x}\Bigl(1 - \frac{1}{\log^2 x}\Bigr) < \prod_{p\le x}\Bigl(1-\frac1p\Bigr) < \frac{e^{-\gamma}}{\log x}\Bigl(1 + \frac{1}{\log^2 x}\Bigr), \qquad x > 285.$$
But the sharp $1/\log^2 x$ rate of Rosser–Schoenfeld rests on PNT-level zero data; importing it **forfeits** the §10 independence. The choice is between the PNT-free elementary Mertens estimate — whose error term is effective but weak, preserving §10 — and the sharp Rosser–Schoenfeld rate, which sacrifices §10. This concerns only the *sharpness* of the Mertens constant and is **independent of the program's effectivity residual**, which is Siegel–Walfisz alone (§9.2(1)). This document defaults to the PNT-free estimate.

**(iii) The recovery object is the lcm; ineffectivity localizes to one term.** By T33 §9A.4 the primorial-smooth von Mangoldt object recovered in Lemma 8.1 (T22.1) is
$$\psi(x) = \log\,\mathrm{lcm}(1, 2, \ldots, \lfloor x\rfloor) = \sum_{n\le x}\Lambda(n),$$
with the exact, elementary identity $\psi(x) - \vartheta(x) = \sum_{k\ge 2}\vartheta(x^{1/k})$. This partitions Lemma 8.1's analytic content: the *untwisted* Chebyshev counting ($\psi, \vartheta$) is effective (Chebyshev; Rosser–Schoenfeld), while the *arithmetic-progression twist* $\psi(x; P_n, a)$ is the **sole** locus of Siegel–Walfisz, hence the sole source of ineffectivity. The cutoff $M_n = \exp(P_n^\beta)$ places $q = P_n \le (\log M_n)^{1/\beta}$ inside the Siegel–Walfisz range, so the only obstruction to effectivity is a possible Landau–Siegel zero of a real character modulo $P_n$. By Tatuzawa (1951) this exceptional zero occurs for at most one modulus; the ineffectivity is therefore confined to at most one exceptional primorial (see the sharpened §9.2(1)).

**(iv) A noticed resonance (not a proof ingredient).** The engine of §6 is the equivalence "cubic Hankel positivity at $\mathbb{Z}/P_n$ ⟺ critical line," cubic being the first order sensitive to the localization. Independently, T33 §9A.5 records that the raw primorial moment sequence $(P_n) = 1, 2, 6, 30, 210, \ldots$ first fails Hankel positivity at cubic order: $D_0 = 1,\ D_1 = 2,\ D_2 = 24,\ D_3 = -787680 < 0$. Hence $(P_n)$ is not a moment sequence and the primorial admits no $\Gamma$-style exact interpolation. The two cubic-order phenomena concern **different** matrices — Hayes–Möbius cubic-moment correlators versus raw primorial moments — and no logical dependence is claimed. The coincidence is flagged for the cross-check of §9.3.

---

## §8. Summary of the chain as designed (not a proof)

**The designed chain for GRH at primorial moduli.**  Read each $\Leftarrow$ as "would follow from"; §3.2 gives the actual status.

(Theorem 2.1 $\Leftarrow$) Apex Lemma$_{HJ}$ at every primorial $P_n$ [via Pass-5 Thm 16.2]
$\Leftarrow$ Apex Lemma$_{HJ}$ at $P_2$ + inductive step [via T22.3 Thm 5.1]
$\Leftarrow$ Apex Lemma$_{HJ}$ at every single prime [via T22.3 induction base + step]
$\Leftarrow$ Paper 32 Thm 7.1 at every single prime [via Paper 32 §7]
$\Leftarrow$ ocho cubic Weil positivity criterion [via ocho main equivalence]
$\Leftarrow$ diez [A1'] (Cor 1.5) + diez [A2'] (Thm 2.7) [via diez explicit constructions, unconditional]

Pillars supporting each step:

- **R1 (GRH ⟺ Apex):** Pass-5 Thm 16.2.
- **R2 (induction):** T22.3 (uses T15 Thm 3 + Paper 32 §6.1 + Paper 32 §6.1d).
- **R3 (base case):** Probe (6a)+(6b) empirical at $P_2$ and refinements + Paper 32 Thm 7.1 at single primes + diez prime-by-prime.
- **R4 (single-prime positivity):** Paper 32 Thm 7.1 ⟸ diez [A1']+[A2'].
- **R5 (Paper 22 §8 obligations):** T22.1 (Lemma 8.1) + T22.2 (projective closure, six items) + T15 (Archimedean Noether limit via Thms 4, 6, 9).

The single external analytic input: Siegel–Walfisz at T22.1 (ineffective) + Mertens (effective, explicit).

**Target 2.0 is not proven, and neither is RH.**  The closed links are listed in Theorem 2.1, and the open ones in §3.2.  (Until 2026-10-08 this line read "Theorem 2.1 is proven".  That claim is withdrawn.)

---

## §9. Honest residuals

### §9.1 What is closed

- The refinement tower and archimedean completion of T15.  These are structural; T15 disclaims RH and GRH.
- Paper 22 Lemma 8.1a0 [P], the 8.1a squarefree skeleton [P], and Lemma 8.1c [A] by both routes.
- Paper 32 Thm 7.1 at the $P_2$ cubic row [P].
- The exact finite probe counts (6a)–(6d).
- The equivalences of ocho, Pass-5 Thm 16.2 and Paper III.  These are reformulations of RH, not proofs of it.

(The former list here claimed GRH at primorial conductors, RH for $\zeta$, the archimedean completion of the apex tower, and all four Paper 22 obligations.  Those claims are withdrawn; see §2 and §3.2.)

### §9.2 What is NOT closed

0. **Target 2.0 and RH.**  Both are open.  The positivity at the core of the chain, in any of its equivalent forms, is RH (§2, §3.2).  The remaining items below are the open links.

1. **Effective rate (Tatuzawa-localized).** The Siegel–Walfisz Route 1 input is ineffective at its source — a possible Landau–Siegel zero of a real character modulo $P_n$. By the lcm/$\psi$ partition of §7.3(iii), this is the *sole* locus of ineffectivity; the untwisted Chebyshev counting is effective (Rosser–Schoenfeld 1962). Tatuzawa's theorem (1951) confines the exceptional zero to at most one modulus, so Theorem 2.1 is **effective for every primorial modulus except at most one exceptional $P_n$**; that lone exception, if it exists, is governed by a single Landau–Siegel zero. Even granting effectivity, the present chain yields no explicit zero-density bound or zero-free region beyond what AP-equidistribution provides; an explicit Riemann–von Mangoldt error term would require the deferred Route 2 (Burgess + large sieve, diez §3) executed effectively.

2. **Non-squarefree-conductor GRH.** Theorem 2.1 covers squarefree-conductor characters (which are primorial-divisor). Non-squarefree characters lift to squarefree-conductor primitive characters by a standard (non-simplicial) argument; the simplicial framework as stated does not directly address them.

3. **Higher-degree $L$-functions.** Selberg-class, automorphic GL($n$) for $n \ge 2$, Hecke $L$-functions of higher rank — the cubic Weil positivity engine as constructed is tied to GL(1) Dirichlet characters. The cubic constraint algebra at higher rank is an open extension.

4. **Dedekind zetas of non-abelian extensions.** Some primorial-modulus Dirichlet $L$-functions correspond to abelian number-field $L$-functions; non-abelian extensions require representation-theoretic input beyond Paper 32 / ocho / diez.

5. **Explicit zero-free regions.** Same blockage as (1): would require T22.1 Route 2 effective work.

**Update (2026-10-07), affecting items (1) and (5), tier [A].**  Route 2 is now discharged externally.  The input is the quasi-GRH half-plane $\operatorname{Re}s>7/8$ for every Dirichlet $L$-function: OpenAI 2026, *The Quasi-Riemann Hypothesis*, `github.com/openai/math`, family 003.  It is model-generated; OpenAI reports a Lean formalization.  Paper 22, Proposition 8.1c$'$, derives $|\psi(X,\chi)-\delta X|\ll X^{7/8}\log^2(P_nX)$ for every $\chi$ modulo $d\mid P_n$, with effective constants.  This gives Lemma 8.1c at natural scale, $M_n\ge(\log P_n)^{16+\varepsilon}$.  So the ineffectivity of item (1) and its Tatuzawa caveat are removed: no exceptional $P_n$ is possible, since every real zero has $\beta\le7/8$.  The "explicit zero-free region" of item (5) is the strip $\tfrac18\le\beta\le\tfrac78$ itself.  It comes from 003, not from this chain, and it says nothing about $\beta=\tfrac12$.  This update changes only the effectivity residual.  It does not supply, or bear on, the claims of §9.1.

6. **Direct simplicial proof at non-primorial conductors $q$.** Bridging from $q \mid P_n$ to arbitrary $q$ in the simplicial framework requires either a non-CRT-product apex inverse system (substantive extension) or hybrid bound / large sieve (standard analytic NT). The first is open; the second is outside the simplicial framework.

### §9.3 Recommended cross-checks

1. **Cubic-Hankel resonance (coincidence audit).** The engine of §6 asserts cubic Hankel positivity at $\mathbb{Z}/P_n$ ⟺ critical line, cubic being the first sensitive order. Independently, the raw primorial moment sequence $(P_n) = 1, 2, 6, 30, 210, \ldots$ first fails Hankel positivity at cubic order ($D_3 = -787680 < 0$; T33 §9A.5), so $(P_n)$ is not a moment sequence and the primorial has no $\Gamma$-type exact interpolation. The two cubic-order phenomena concern different matrices (Hayes–Möbius cubic-moment correlators vs. raw primorial moments) and carry no claimed dependence. Recommended: compute $\mathcal{H}_N$ at $N = 6, 30$ and verify no submatrix coincides with the primorial-moment Hankel, ruling the resonance a coincidence on the record.

2. **Elementary-vs-effective Mertens.** Confirm numerically that the $(I_5)$ vanishing $\mu_n^*(\mathcal{H}_n)\cdot\mathrm{polylog}(P_n)\to 0$ holds at the explicit elementary rate $e^{-\gamma}/\log p_n$ through $P_n = 2310$ (probe 6d already gives $\mu_n^*\cdot N = 2.00$). This checks that the PNT-free Mertens constant suffices without invoking Rosser–Schoenfeld — preserving §10 independence.

---

## §10. Independence of the simplicial proof

The chain is designed to be independent of standard analytic-NT approaches to GRH/RH:

- It uses Siegel–Walfisz, which contains the prime number theorem in progressions, ineffectively in Lemma 8.1c route 1.  It uses the quasi-GRH half-plane of OpenAI 2026 in route 2, and no stronger analytic input.  The earlier claim that it uses no PNT at all contradicted §7 (audit F6).
- It does not use the Riemann-Siegel formula, the approximate functional equation, or large-sieve hybrid bounds.
- It does not use random-matrix conjectures (GUE, etc.). These are predictions of fine-scale statistics; the framework targets the critical-line localization (open) and says nothing fine-scale.
- It does not use the Selberg class axioms or the Maaß-correspondence machinery.
- It does not use the de Branges spaces / Lax-Phillips scattering approaches.

The framework's intellectual debts: Hayes (1965, Möbius inversion of character sums), Steinhaus (1957, three-gap theorem), Weil (1952, Weil positivity criterion for GRH at higher-degree), Mertens (1874, prime product asymptotic), Siegel–Walfisz (1936, character sums over arithmetic progressions). All other content is structural / categorical / probe-verified within the simplicial program.

---

## §11. Forward doors

The simplicial program's broader agendas do not depend on Target 2.0; RH was never the unique target. Open extensions:

1. **Paper 32 §10–§13 (Standard Model emergence).** Cubic-vs-quartic isolation at higher conductor classes; A_3, A_4, ... cubic-isolated modes correspond to higher Standard Model representations.
2. **Dimensional selection (Paper 32 §11).** Why 3+1? Cubic constraint algebra at $A_2$ uniquely selects the four-dimensional spacetime tangent space.
3. **FEP-3 program.** Free Energy Principle at cubic order; biological-validity layer.
4. **Conductor blind spot / σ_PI (CBS work).** Second-order conductor blind spot at $\rho_\times$, verified via packet inverse-participation ratio.
5. **Helmert-basis pullback / T4-HelmertFourier.** Unitarity verified at machine $\varepsilon$ on primorial bases.

These are independent of Target 2.0; they were always the broader simplicial-program goals.  Target 2.0 is one aim, and the program's structural reach is wider.

---

## §12. Files (manuscript inventory)

**This document.**
- `GRH-Apex-Integration-Draft1.md` — integration overview.

**T22 trilogy.**
- `T22.1-Lemma8p1-Sublemmas-Draft1.md` — Lemma 8.1 sublemmas.
- `T22.2-Paper22-Second-Task-Closure-Draft1.md` — projective critical-leaf closure (six items).
- `T22.3-InductiveExtension-AllPrimorials-Draft1.md` — inductive extension to all primorials.

**T15.**
- `T15-FiniteToArchimedeanCompletion-Draft1.md` — finite-to-Archimedean completion (Thms 1–10).

**Probes (audit base).**
- `probe_paper32_depth_audit.py` — (6a) cubic depth audit at $\mathbb{Z}/12, \mathbb{Z}/18$.
- `probe_paper32_T4_operator_norm.py` — (6a) quartic operator norm.
- `probe_paper22_primorial_extension.py` — (6b) primorial extension at $\mathbb{Z}/30, \mathbb{Z}/210$.
- `probe_paper25_three_gap_carry.py` — (6d) Diophantine three-gap frame.

**Existing manuscripts (cited).**
- Pass-5 (`RH-Pass5*`) — Lock A + Born Heat Flow; §16 Thm 16.2.
- Ocho — cubic Weil positivity criterion.
- Diez — [A1'], [A2'], [A3'].
- Paper 11 — Hayes–Möbius currents.
- Paper 22 — primorial cumulant Noether theory; §5 Thm 5.1.3, §8 four obligations, Conj 5.2.
- Paper 25 — first-order pricing + Diophantine frame layer.
- Paper 32 — one functional, four forces; §6.1, §6.1d, §7 Thm 7.1.
- T33 — Smooth Primorial Family; §8 (smooth Mertens, elementary derivation), §9A.4 (lcm $= e^{\psi}$ recovery object), §9A.5 (moment obstruction $D_3 < 0$).

---

## §13. References

- Hayes, D. R. (1965). The expression of a polynomial as a sum of three irreducibles. *Acta Arith.* 11, 461–488. [Hayes–Möbius character bookkeeping]
- Mertens, F. (1874). Ein Beitrag zur analytischen Zahlentheorie. *J. reine angew. Math.* 78, 46–62. [$\prod (1 - 1/p)$ asymptotic]
- Murillo Montero, L. (2026). T15 — Finite-to-Archimedean Completion.
- Murillo Montero, L. (2026). T22.1 — Lemma 8.1 Sublemmas.
- Murillo Montero, L. (2026). T22.2 — Paper 22 §8 Second Task: Projective Critical-Leaf Closure.
- Murillo Montero, L. (2026). T22.3 — Inductive Extension of (6a)–(6d) Audits to All Primorials.
- Murillo Montero, L. (2026). Paper 11 — Hayes–Möbius currents and primorial cumulant lifts.
- Murillo Montero, L. (2026). Paper 22 — Primorial Cumulant Noether Theory and the Riemann Hypothesis.
- Murillo Montero, L. (2026). Paper 25 — First-Order Pricing and the Diophantine Frame Layer.
- Murillo Montero, L. (2026). Paper 32 — One Functional, Four Forces.
- Murillo Montero, L. (2026). Pass-5 (RH-Pass5) — Lock A No-Loss + Born Heat Flow.
- Murillo Montero, L. (2026). Ocho — Cubic Weil Positivity Criterion.
- Murillo Montero, L. (2026). Diez — [A1'], [A2'], [A3'].
- Murillo Montero, L. (2026). T33 — The Smooth Primorial Family: Bohr–Mollerup, Wielandt, and the Constant Tower of the Prime Ladder.
- Rosser, J. B., Schoenfeld, L. (1962). Approximate formulas for some functions of prime numbers. *Illinois J. Math.* 6, 64–94. [Effective Mertens / Chebyshev bounds; the $x > 285$ two-sided Mertens product estimate]
- Siegel, C. L. (1935). Über die Klassenzahl quadratischer Zahlkörper. *Acta Arith.* 1, 83–86.
- Steinhaus, H. (1957). Three-gap theorem (Steinhaus conjecture). [Verified by Sós 1958, Świerczkowski 1958.]
- Tatuzawa, T. (1951). On a theorem of Siegel. *Jap. J. Math.* 21, 163–178. [Effective lower bound for $L(1,\chi)$, real primitive $\chi$, with at most one exceptional modulus]
- Walfisz, A. (1936). Zur additiven Zahlentheorie. II. *Math. Z.* 40, 592–607.
- Weil, A. (1952). Sur les "formules explicites" de la théorie des nombres premiers. *Comm. Sém. Math. Univ. Lund (Festskrift M. Riesz)*, 252–265.
- LMFDB Collaboration (2026). $L$-function and modular forms database. https://lmfdb.org. [Source of $L(1/2, \chi_3) \approx 0.48085$ tabulated constant.]

---

*The simplicial program organizes GRH at primorial moduli as a chain through five structural pillars (Pass-5, ocho, diez, T15, T22), four finite probes, and two external analytic inputs (Siegel–Walfisz; the half-plane of OpenAI 2026).  Several links are proved (Theorem 2.1).  The positivity at the core of the chain is RH in another form and is open.  So are [A3$'$], the occupation lift, projective closure and the Archimedean Noether Limit.  Target 2.0 and RH are not proved here (corrected 2026-10-08; the earlier closing line claimed both).*
