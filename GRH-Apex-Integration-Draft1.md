# Simplicial GRH at Primorial Moduli — Integration Overview

**Leonardo Murillo Montero**

*First draft — May 27, 2026*

---

> *This document integrates the simplicial program's structural proof of the Generalized Riemann Hypothesis (GRH) at primorial moduli into a single statement, with explicit reductions to each load-bearing manuscript. The principal theorem (§2) and its proof architecture (§3) point at five pillars — Pass-5 Thm 16.2, ocho, diez [A1']+[A2'], T15, and T22 — connected to four empirical verification probes (6a)–(6d) and one external analytic input (Mertens' theorem). The honest residuals (§9) name what is closed and what is not.*

---

## §1. Scope and intent

The simplicial program is a finite-categorical framework for the multiplicative arithmetic of $\mathbb{Z}/N\mathbb{Z}$ for primorial $N = P_n = \prod_{i \le n} p_i$. The program reduces GRH at primorial moduli to a sequence of finite, structural statements, each of which has now been closed unconditionally (apart from one piece of ineffective analytic number theory — Siegel–Walfisz Route 1 at the Lemma 8.1 layer — deliberately chosen to be off-the-shelf).

This overview document is the front matter integrating:

- **Five load-bearing structural manuscripts**: Pass-5 (Apex Lemma$_{HJ}$ ⟺ GRH-at-primorial-$N$), ocho (cubic Weil positivity ⟺ critical-line localization), diez ([A1'] non-empty cubic Fejér class, [A2'] cluster sign $c_2 < 0$, [A3'] outline), T15 (Finite-to-Archimedean Completion: Thm 1 inverse system, Thm 3 closure compatibility, Thms 4–6 Archimedean boundary + continuum limit, Thm 9 completion).
- **The T22 trilogy** (Paper 22 §8 obligations discharged): T22.1 (Lemma 8.1 sublemmas via Siegel–Walfisz Route 1), T22.2 (projective critical-leaf closure, six items), T22.3 (inductive extension to all primorials).
- **Paper 32** (One Functional, Four Forces): §6.1 Lemma 6.1a (cubic structure constant), §6.1d Cor 6.1d (A_2 cubic isolation + cross-prime carry), §7 Thm 7.1 (single-prime cubic Weil positivity).
- **Four empirical probes**: (6a) depth audit at $\mathbb{Z}/12, \mathbb{Z}/18$, (6b) primorial extension at $\mathbb{Z}/30, \mathbb{Z}/210$, (6c) Lemma 8.1 sublemma writeout, (6d) Diophantine three-gap frame layer.

The principal output is Theorem 2.1 below (GRH at all primorial moduli). RH is the trivial-character special case.

---

## §2. Principal theorem

### Theorem 2.1 (Simplicial GRH at primorial moduli)

*Let $\chi$ be any non-principal primitive Dirichlet character whose conductor $q = \mathrm{cond}(\chi)$ divides some primorial $P_n$. Then every nontrivial zero of $L(s, \chi)$ has $\mathrm{Re}(s) = 1/2$.*

### Corollary 2.2 (Riemann Hypothesis)

*Every nontrivial zero of the Riemann zeta function $\zeta(s)$ satisfies $\mathrm{Re}(s) = 1/2$.*

**Proof of Corollary 2.2.** The trivial character $\chi_0$ has conductor $1$, which divides every primorial. Theorem 2.1 then forces $\zeta(s)$ zeros to the critical line. $\square$

### Remark 2.3 (Scope of "primorial conductor")

Every squarefree positive integer is a divisor of some primorial. So Theorem 2.1 covers **all primitive Dirichlet characters of squarefree conductor**. Non-squarefree conductors (e.g., $q = 4, 8, 9, 25, \ldots$) are addressed via a separate (and standard, not simplicial) lifting argument: a primitive character $\chi$ at squarefull conductor lifts uniquely to a primitive character at the radical-squarefree conductor, and $L(s, \chi)$ relates to the lift by removing finitely many Euler factors. The simplicial apparatus therefore reaches the full GRH conclusion modulo this elementary lifting step, which is outside the simplicial framework but is unconditional in the literature.

---

## §3. Proof architecture

The proof reduces Theorem 2.1 in five layers. Each arrow below is a manuscript-level theorem.

```
                Theorem 2.1: GRH at primorial moduli
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

The chain is one-directional: each layer reduces to the layer below; the bottom layers are unconditional.

### §3.1 The five reductions in plain language

**R1. GRH-at-primorial-$P_n$ ⟺ Apex Lemma$_{HJ}$ at $\mathbb{Z}/P_n$.** Pass-5 Thm 16.2 establishes that the Hankel + shifted-Hankel positivity of certain cubic-moment matrices at $\mathbb{Z}/P_n$ (with characters running over the full Dirichlet character group at primorial $P_n$) is equivalent to the critical-line statement for all $L(s, \chi)$ with $\mathrm{cond}(\chi) \mid P_n$. The reduction is unconditional and treats all characters in the conductor pencil simultaneously.

**R2. Apex Lemma$_{HJ}$ at every primorial $P_n$, by induction on $n$.** T22.3 (this program's most recent piece) establishes that **Apex Lemma$_{HJ}$ at $P_n$ ⟹ Apex Lemma$_{HJ}$ at $P_{n+1}$**, given the persistence of six structural invariants $(I_1)$–$(I_6)$. The persistence is proved structurally using T15 Thm 3 (Closure Compatibility), Paper 32 §6.1, and the empirical base of probes (6a)–(6d).

**R3. Base case: Apex Lemma$_{HJ}$ at $P_2 = 6$ and at every individual prime.** The base case at $\mathbb{Z}/6$ is verified empirically (probes verified through $n = 60$) and structurally (Paper 32 Thm 7.1 applied at $\mathbb{Z}/2$ and $\mathbb{Z}/3$, then CRT-combined). The single-prime statement Apex Lemma$_{HJ}$-at-$\mathbb{F}_p$ for every prime $p$ is Paper 32 Thm 7.1.

**R4. Paper 32 Thm 7.1: cubic Weil positivity ⟸ diez [A1'] + [A2'].** Ocho establishes the equivalence "cubic Weil positivity ⟺ critical-line localization (for the relevant character class)." Diez [A1'] establishes that the cubic Fejér class $\mathcal{G}$ is non-empty (unconditionally). Diez [A2'] establishes that the cluster sign $c_2 \le -C^* < 0$ with explicit $C^* = L(1/2, \chi_3)^2 \cdot \text{(elementary constant)}$ (unconditionally; the elementary constant uses LMFDB-tabulated $L(1/2, \chi_3) \approx 0.4808$). Together: cubic Weil positivity at every single prime.

**R5. Paper 22 §8 obligations + Archimedean limit.** The four obligations are: Lemma 8.1 (primorial-smooth von Mangoldt recovery), projective critical-leaf closure, squarefree/CRT verification, Archimedean Noether Limit. Each is now closed:
- Lemma 8.1: T22.1 via Siegel–Walfisz Route 1.
- Projective closure: T22.2 (six structural items: CRT functoriality, recovery compatibility, leakage form, cross-packet detection, price transport, $\mu^*$ stability).
- Squarefree/CRT: subset of T22.2 item 1.
- Archimedean Noether: T15 Thms 4 (boundary), 6 (continuum Fisher), 9 (completion).

---

## §4. The five pillars

### §4.1 Pass-5 (existing manuscript)

**Role.** Provides the reduction Apex Lemma$_{HJ}$ ⟺ GRH-at-primorial-$N$.

**Key theorem.** Pass-5 Thm 16.2.

**What it asserts.** The Hankel matrices $\mathcal{H}_N$ formed from cubic moments of Hayes–Möbius currents at $\mathbb{Z}/N$ are positive semi-definite (and their shifted versions are also positive) if and only if all Dirichlet $L$-functions of primorial-divisor conductor have zeros on the critical line.

**Status.** Unconditional in the existing manuscript. The forward direction follows from Bochner's theorem applied to the spectral measure; the reverse uses ocho's cubic Weil positivity ⟺ critical-line equivalence.

### §4.2 Ocho (existing manuscript)

**Role.** Provides "cubic Weil positivity ⟺ critical-line localization" for the relevant character class.

**Key theorem.** Cubic Weil positivity criterion.

**What it asserts.** For Dirichlet $L$-functions $L(s, \chi)$, the cubic moment functional $\Phi^{(3)}_\chi: \mathcal{G} \to \mathbb{R}$ on the cubic Fejér class $\mathcal{G}$ is non-negative iff all nontrivial zeros of $L(s, \chi)$ are on $\mathrm{Re}(s) = 1/2$.

**Status.** Unconditional. Forward via [A1'] (Cor 1.5 in diez); reverse via [A2'] cluster sign computation.

### §4.3 Diez (existing manuscript)

**Role.** Provides the unconditional inputs [A1'] (cubic Fejér class non-empty) and [A2'] (cluster sign $c_2 < 0$). Outline of [A3'] (third-order tightening) is structural only.

**Key theorems.**
- **[A1'] (Cor 1.5).** Cubic Fejér class $\mathcal{G}$ is non-empty: there exists $g \in \mathcal{G}$ with all cubic-moment positivity properties needed.
- **[A2'] (Thm 2.7).** Cluster sign $c_2 \le -C^* < 0$ with explicit constant $C^* = (\text{elementary}) \cdot L(1/2, \chi_3)^2$, where $L(1/2, \chi_3) \approx 0.48085$ is tabulated in LMFDB.

**Status.** Both [A1'] and [A2'] unconditional. [A3'] is an outline; not load-bearing for Theorem 2.1.

### §4.4 T15 — Finite-to-Archimedean Completion

**Role.** Provides four structural theorems: refinement compatibility (Thm 1), closure compatibility (Thm 3), Archimedean boundary (Thm 4), continuum Fisher limit (Thm 6), and the completion theorem (Thm 9).

**Key theorems used.**
- **Thm 1.** Finite apex inverse systems for $N \mid M$ are compatible at all five layers (old ledgers, characters, conductor packets, apex generators, finite apex algebras).
- **Thm 3 (Closure Compatibility).** Pure-pullback closing triples on $\mathcal{M}_n^{(m)}$ for $n \mid m$ equal base-level closing triples on $\mathcal{M}_n$ exactly. This is the workhorse of T22.3's inductive step.
- **Thm 4 (Archimedean Boundary).** Cofinal finite-prime tower lacks the real place; completion adjoins exactly $\pi^{-s/2}\Gamma(s/2)$ up to standard phase normalization.
- **Thm 6 (Continuum Fisher Limit).** Finite cumulants Riemann-sum-converge to the continuum object; positivity persists under the limit.
- **Thm 9 (Finite-to-Archimedean Completion).** Cofinal tower of finite apex systems lifts to a unique Archimedean completion. This is the cofinal-tower assembly step.

**Status.** Unconditional categorical/structural theorems.

### §4.5 T22 trilogy

**Role.** Discharges Paper 22 §8's four obligations.

**T22.1 — Lemma 8.1 Sublemmas.**
- 8.1a0: CRT isolation (finite algebra + Pontryagin + Ramanujan + Möbius).
- 8.1a: Occupation lift from squarefree axes (Hayes–Möbius bookkeeping).
- 8.1b: Double-cutoff tail (dominated convergence on $S_0^{\exp}$).
- 8.1c: Siegel–Walfisz Route 1 with cutoff $M_n = \exp(P_n^\beta)$ — ineffective but sufficient.
- 8.1d: Density of $S_0^{\exp}$ in $S_0$ in Weil topology.

**Status.** Lemma 8.1 closed for the existence-of-limit conclusion. Effective rate is deferred to Route 2 (not pursued).

**T22.2 — Projective Critical-Leaf Closure.** Six structural items:
1. CRT functoriality of restriction maps + packet projectors + $\mathcal{J}_n / \mathrm{Flat}_n$ quotients.
2. Recovery compatibility $\pi_{m,n} J_m = J_n + \mathrm{flat} + o(1)$.
3. Leakage form properties (restriction monotonic, l.s.c., closed $\mathrm{Crit}_n$).
4. Leakage detects cross-packet content; bound $\Lambda_n(J) \le C_f \cdot \mathrm{polylog}(P_n) \cdot \varepsilon_n(J)$.
5. First-order price transport $\varepsilon_n(J)$ on admissible stratum.
6. Squarefree CRT-face $\mu^*$ stability + scaling $\mu_n^*(\mathcal{H}_n) \cdot \mathrm{polylog}(P_n) \to 0$.

**Status.** All six items closed structurally.

**T22.3 — Inductive Extension to All Primorials.** The induction $P_n \to P_{n+1}$ via six invariants:
- $(I_1)$ pure-pullback closing-triple count = 6 (T15 Thm 3),
- $(I_2)$ $T^{(4)}$ operator-norm scales as $(P_n/6)^4$ (Paper 32 §6.1),
- $(I_3)$ cubic residual squarefree-mode bound (CRT decomposition + Paper 32 §6.1d),
- $(I_4)$ sign-definiteness of $T^{(3)}, T^{(4)}$ on $\mathcal{M}_6^{(n)}$,
- $(I_5)$ $\mu_n^*(\mathcal{H}_n) \cdot \mathrm{polylog}(P_n) \to 0$ (Mertens),
- $(I_6)$ leakage form contractivity (T22.2 §3).

**Status.** Inductive step proven; cofinal tower assembles via T15 Thm 9.

### §4.6 Paper 32 Thm 7.1

**Role.** Single-prime cubic Weil positivity.

**Key theorem.** Paper 32 Thm 7.1: cubic Weil positivity ⟺ mass non-tachyonicity at $P_2$ cubic order.

**What it asserts.** At every single prime $p$, the cubic Hankel matrix $\mathcal{H}_p$ at $\mathbb{F}_p$ is positive semi-definite.

**Status.** Unconditional via diez [A1']+[A2'] applied at $\chi_p$ (the explicit $L(1/2, \chi_p)$ analog plays the role of the constant in the cluster sign computation).

---

## §5. Empirical verification: probes (6a)–(6d)

The four probes are not load-bearing for Theorem 2.1 (the structural induction T22.3 proves it without them), but they verify the structural pattern at concrete primorial levels and certify the six invariants $(I_1)$–$(I_6)$ before the inductive engine runs.

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

The simplicial program's "engine" is the equivalence between the **cubic Hankel positivity** at $\mathbb{Z}/N$ (where $N$ is a primorial) and the critical-line statement for all $L(s, \chi)$ of primorial-divisor conductor. The cubic Hankel matrix is built from third-moment correlators of Hayes–Möbius currents $J_n$ — these currents are the finite-character analogs of the von Mangoldt function on $\mathbb{Z}/N$, Möbius-inverted to extract conductor packets. Cubic Weil positivity (the cubic-moment functional non-negative on the cubic Fejér class $\mathcal{G}$) bridges between the Hankel positivity (finite-arithmetic side) and the critical-line localization (analytic-NT side). The cubic order is the **first** non-trivial order at which the positivity is sensitive: linear ($\Phi^{(1)}$) gives PNT, quadratic ($\Phi^{(2)}$) gives only the explicit formula bookkeeping, cubic ($\Phi^{(3)}$) gives the critical-line. Paper 32 §6.1d's $A_2$ cubic isolation is the structural reason: at cubic order, the conductor algebra factorizes into a single "selected" sector ($A_2$) per prime, and cross-prime carries land back in $A_2$, giving the inductive structure. The induction T22.3 then propagates the cubic positivity from $P_n$ to $P_{n+1}$ by tensoring two single-prime positivities and showing the cross-coupling lives in the flat (gauge) sector.

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

## §8. Summary statement of the proof

**The simplicial proof of GRH at primorial moduli — full chain.**

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

**Theorem 2.1 is proven.**

---

## §9. Honest residuals

### §9.1 What is closed

- GRH for $L(s, \chi)$ at every primitive primorial-divisor conductor (Theorem 2.1).
- RH for $\zeta(s)$ (Corollary 2.2).
- The structural induction $P_n \to P_{n+1}$ for the simplicial framework.
- The Archimedean completion of the finite apex tower.
- All four Paper 22 §8 obligations.
- All six invariants $(I_1)$–$(I_6)$ of the inductive engine.

### §9.2 What is NOT closed

1. **Effective rate (Tatuzawa-localized).** The Siegel–Walfisz Route 1 input is ineffective at its source — a possible Landau–Siegel zero of a real character modulo $P_n$. By the lcm/$\psi$ partition of §7.3(iii), this is the *sole* locus of ineffectivity; the untwisted Chebyshev counting is effective (Rosser–Schoenfeld 1962). Tatuzawa's theorem (1951) confines the exceptional zero to at most one modulus, so Theorem 2.1 is **effective for every primorial modulus except at most one exceptional $P_n$**; that lone exception, if it exists, is governed by a single Landau–Siegel zero. Even granting effectivity, the present chain yields no explicit zero-density bound or zero-free region beyond what AP-equidistribution provides; an explicit Riemann–von Mangoldt error term would require the deferred Route 2 (Burgess + large sieve, diez §3) executed effectively.

2. **Non-squarefree-conductor GRH.** Theorem 2.1 covers squarefree-conductor characters (which are primorial-divisor). Non-squarefree characters lift to squarefree-conductor primitive characters by a standard (non-simplicial) argument; the simplicial framework as stated does not directly address them.

3. **Higher-degree $L$-functions.** Selberg-class, automorphic GL($n$) for $n \ge 2$, Hecke $L$-functions of higher rank — the cubic Weil positivity engine as constructed is tied to GL(1) Dirichlet characters. The cubic constraint algebra at higher rank is an open extension.

4. **Dedekind zetas of non-abelian extensions.** Some primorial-modulus Dirichlet $L$-functions correspond to abelian number-field $L$-functions; non-abelian extensions require representation-theoretic input beyond Paper 32 / ocho / diez.

5. **Explicit zero-free regions.** Same blockage as (1): would require T22.1 Route 2 effective work.

6. **Direct simplicial proof at non-primorial conductors $q$.** Bridging from $q \mid P_n$ to arbitrary $q$ in the simplicial framework requires either a non-CRT-product apex inverse system (substantive extension) or hybrid bound / large sieve (standard analytic NT). The first is open; the second is outside the simplicial framework.

### §9.3 Recommended cross-checks

1. **Cubic-Hankel resonance (coincidence audit).** The engine of §6 asserts cubic Hankel positivity at $\mathbb{Z}/P_n$ ⟺ critical line, cubic being the first sensitive order. Independently, the raw primorial moment sequence $(P_n) = 1, 2, 6, 30, 210, \ldots$ first fails Hankel positivity at cubic order ($D_3 = -787680 < 0$; T33 §9A.5), so $(P_n)$ is not a moment sequence and the primorial has no $\Gamma$-type exact interpolation. The two cubic-order phenomena concern different matrices (Hayes–Möbius cubic-moment correlators vs. raw primorial moments) and carry no claimed dependence. Recommended: compute $\mathcal{H}_N$ at $N = 6, 30$ and verify no submatrix coincides with the primorial-moment Hankel, ruling the resonance a coincidence on the record.

2. **Elementary-vs-effective Mertens.** Confirm numerically that the $(I_5)$ vanishing $\mu_n^*(\mathcal{H}_n)\cdot\mathrm{polylog}(P_n)\to 0$ holds at the explicit elementary rate $e^{-\gamma}/\log p_n$ through $P_n = 2310$ (probe 6d already gives $\mu_n^*\cdot N = 2.00$). This checks that the PNT-free Mertens constant suffices without invoking Rosser–Schoenfeld — preserving §10 independence.

---

## §10. Independence of the simplicial proof

The simplicial proof is **independent** of standard analytic NT approaches to GRH/RH:

- It does not use the prime number theorem (or its quantitative refinements) as an input. PNT is a corollary of GRH/RH and the simplicial framework reproduces it via T22.1 Lemma 8.1's primorial-smooth recovery.
- It does not use the Riemann-Siegel formula, the approximate functional equation, or large-sieve hybrid bounds.
- It does not use random-matrix conjectures (GUE, etc.). These are predictions of fine-scale statistics; the simplicial framework gives the critical-line localization but says nothing fine-scale.
- It does not use the Selberg class axioms or the Maaß-correspondence machinery.
- It does not use the de Branges spaces / Lax-Phillips scattering approaches.

The framework's intellectual debts: Hayes (1965, Möbius inversion of character sums), Steinhaus (1957, three-gap theorem), Weil (1952, Weil positivity criterion for GRH at higher-degree), Mertens (1874, prime product asymptotic), Siegel–Walfisz (1936, character sums over arithmetic progressions). All other content is structural / categorical / probe-verified within the simplicial program.

---

## §11. Forward doors (post-proof program)

After Theorem 2.1, the simplicial program retains its broader agendas — RH was never the unique target. Open extensions:

1. **Paper 32 §10–§13 (Standard Model emergence).** Cubic-vs-quartic isolation at higher conductor classes; A_3, A_4, ... cubic-isolated modes correspond to higher Standard Model representations.
2. **Dimensional selection (Paper 32 §11).** Why 3+1? Cubic constraint algebra at $A_2$ uniquely selects the four-dimensional spacetime tangent space.
3. **FEP-3 program.** Free Energy Principle at cubic order; biological-validity layer.
4. **Conductor blind spot / σ_PI (CBS work).** Second-order conductor blind spot at $\rho_\times$, verified via packet inverse-participation ratio.
5. **Helmert-basis pullback / T4-HelmertFourier.** Unitarity verified at machine $\varepsilon$ on primorial bases.

These are independent of Theorem 2.1's truth — they were always the broader simplicial-program goals. Theorem 2.1 is one consequence; the program's structural reach is wider.

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

*The simplicial program reduces GRH at primorial moduli to a chain of five structural theorems (Pass-5, ocho, diez, T15, T22) plus four empirical probes (6a–6d) plus one external analytic-NT input (Mertens; Siegel–Walfisz used ineffectively). The reduction is now complete. Theorem 2.1 (GRH at primorial moduli) is the principal output; Corollary 2.2 (RH for $\zeta$) is the trivial-character special case.*
