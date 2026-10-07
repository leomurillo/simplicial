# BSD via the Simplicial m=3 Cubic Kummer Clock — Structural Assessment

**Leonardo Murillo Montero (assessment prepared by Claude Opus 4.7)**

*Draft 1 — May 26, 2026*

---

> *The simplicial m=3 cubic Kummer clock lives over Q(zeta_3) and aggregates finite-order Hecke characters of (Z[zeta_3]/m)^* at primorial conductor. BSD for CM elliptic curves at j=0 lives over Q(zeta_3) and concerns a Grossencharacter of infinity type (1,0). The arithmetic ambient overlaps; the L-function families do not. This assessment is calibratedly negative on pursuit, with a single focused sub-target where the framework's distinctive cubic-Galois content might deliver something genuinely new at s = 1.*

---

## (a) Problem statement (BSD precisely)

Let $E/\mathbb{Q}$ be an elliptic curve. Its Hasse–Weil $L$-function
$$L(E, s) = \prod_p L_p(E, s) = \sum_{n \ge 1} a_n(E)\, n^{-s},$$
defined initially for $\mathrm{Re}(s) > 3/2$, admits analytic continuation to $\mathbb{C}$ (Wiles–Breuil–Conrad–Diamond–Taylor 1995–2001 modularity, for $\mathbb{Q}$). The **Birch–Swinnerton-Dyer conjecture** has two parts:

**(BSD-1, weak form).** The order of vanishing of $L(E, s)$ at $s = 1$ equals the rank of the Mordell–Weil group $E(\mathbb{Q})$:
$$\mathrm{ord}_{s = 1} L(E, s) = \mathrm{rank}\, E(\mathbb{Q}).$$

**(BSD-2, refined form).** The leading Taylor coefficient at $s = 1$ has the explicit shape
$$\frac{1}{r!}\frac{d^r L}{ds^r}(E, 1) \;=\; \frac{\Omega_E \cdot \mathrm{Reg}(E) \cdot \prod_p c_p \cdot |\Sha(E/\mathbb{Q})|}{|E(\mathbb{Q})_{\text{tors}}|^2},$$
where $\Omega_E$ is the real period, $\mathrm{Reg}(E)$ is the Néron–Tate regulator, $c_p$ are Tamagawa numbers, $|\Sha|$ is the (conjecturally finite) order of the Tate–Shafarevich group, and $|E(\mathbb{Q})_{\text{tors}}|$ is the torsion order.

**The CM j=0 family.** The assignment focuses on the family
$$E_d:\; y^2 = x^3 + d, \quad d \in \mathbb{Z} \setminus \{0\}.$$
Every member has $j$-invariant zero and complex multiplication by $\mathbb{Z}[\zeta_3]$. By a theorem of Deuring (1953) extended by Shimura, the $L$-function factors as
$$L(E_d, s) = L(s, \psi_d) \cdot L(s, \bar{\psi}_d),$$
where $\psi_d$ is a **Hecke Grossencharacter** of $\mathbb{Q}(\zeta_3)$ of **infinity type** $(1, 0)$ — i.e., $\psi_d(\alpha) \cdot \bar{\alpha} = \alpha \cdot |\alpha|$-style scaling on principal ideals — with finite-order twist by a Dirichlet character of $(\mathbb{Z}[\zeta_3]/\mathfrak{f}_d)^\times$ depending on $d$.

The conductors $N(E_d)$ for $d$ a sixth-power-free integer concentrate on divisors of $432 = 2^4 \cdot 3^3$ (when $d$ has only the bad primes $2, 3$) and more generally on $2^a \cdot 3^b \cdot \prod p_i^{c_i}$ for $p_i \mid d$. **They are not primorial.**

---

## (b) Classical status

The CM j=0 case is one of the best-understood corners of BSD.

**Rank 0 (Coates–Wiles 1977).** For CM elliptic curves over $\mathbb{Q}$ (in particular all $E_d$ at $j = 0$), if $L(E, 1) \ne 0$, then $E(\mathbb{Q})$ is finite. This established BSD-1 in rank 0 *unconditionally* for the CM family well before the proof for the general case (Kolyvagin 1989, conditional on modularity, made unconditional 1994). Rubin (1981, 1987) sharpened this via the **Iwasawa main conjecture** for imaginary-quadratic-field CM curves, controlling $\Sha$ via $p$-adic L-function arithmetic — for CM by $\mathbb{Z}[\zeta_3]$, this gives BSD-2 modulo powers of small primes.

**Rank 1 (Gross–Zagier 1986 + Kolyvagin 1989).** For CM (and all modular) elliptic curves with analytic rank exactly 1, Gross–Zagier's formula expresses $L'(E, 1)$ in terms of the height of a Heegner point, and Kolyvagin's Euler system shows this Heegner point generates a finite-index subgroup of $E(\mathbb{Q})$. Hence BSD-1 holds in rank 1.

**Rank $\ge 2$: open.** Even for CM curves, the analytic-rank-$\ge 2$ case is wide open. The strongest results (Zhang, Bhargava–Skinner–Zhang on average rank) are statistical, not curve-by-curve.

**$\Sha$ finiteness.** Open in general; known only in rank 0 and rank 1 (Kato, Skinner–Urban for non-CM; Rubin for CM; conditional on Iwasawa main conjecture in some cases).

For the $E_d$ family specifically, ranks 0, 1, 2, 3 are all attested; the analytic rank is known to match the algebraic rank for hundreds of thousands of $d$ values via numerical experiments (Stein's tables, LMFDB). **No structural reformulation has shifted the open boundary at rank $\ge 2$.**

---

## (c) Simplicial framework alignment at m = 3

### What fits

The arithmetic ambient $\mathbb{Q}(\zeta_3) = \mathbb{Q}(\sqrt{-3})$ is exactly the base over which:
- T10 defines the cubic Kummer clock $K_N^{(3)} = \mathbb{Q}(\zeta_3, \sqrt[3]{p}: p \le N)$.
- T27 builds the cubic bilateral factorization $U^{(3)} W^{(3)} = D^{\mathrm{rad},3} V^{\mathrm{Gauss},3}$.
- The cubic A–C tensor of siete §5 admits its natural Hecke-L-function dual.

So the **base field** is correctly matched. The cubic Galois richness $[\mathbb{Q}(\zeta_3):\mathbb{Q}] = 2$ with the additional cubic Kummer tower is in place. The cubic Gram structure $G^{(3)}$ (probe_T27_output.txt: spectrum [3.21, 4.02], condition 1.25, deviation from identity 12.98 in Frobenius norm) is the structural lever T27 §7 identified for going beyond Parseval.

### What does not fit — three structural obstructions

**Obstruction 1: Conductor mismatch.** T27 fixes the cubic conductor at the **primorial cubic lift** $\mathfrak{m} = N \cdot \mathbb{Z}[\zeta_3]$ for $N \in \{30, 210, 2310, \ldots\}$. The conductors $\mathfrak{f}_d$ of the Grossencharacters $\psi_d$ are supported on $\{(1-\zeta_3), (2), p_d\}$ where $p_d$ collects the bad primes of $E_d$ — these are **divisor lattices of $d$**, not primorial sweeps. The simplicial framework's "primorial sweep" structure — the indexing principle of the [A3'] residual, of audit ξ, of the conductor packets — does not match the curve-by-curve conductor structure of BSD.

**Obstruction 2: Infinity-type mismatch (load-bearing).** This is the central structural objection. T27's $W^{(3)}$ aggregates over the **finite-order character group** $\widehat{C_{\mathfrak{m}}^{(3)}} = \widehat{(\mathbb{Z}[\zeta_3]/\mathfrak{m})^\times}$ — finite, of order $\varphi_3(\mathfrak{m})$, all characters of finite order. The Grossencharacters $\psi_d$ governing $L(E_d, s)$ are **of infinity type $(1, 0)$**: they include a non-trivial archimedean factor $\psi_\infty(\alpha) = \alpha/|\alpha|$ (or $\alpha$ itself, depending on normalization) that is **not of finite order**. They live in the dual of the idele class group $C_{\mathbb{Q}(\zeta_3)} = \mathbb{A}_{\mathbb{Q}(\zeta_3)}^\times / \mathbb{Q}(\zeta_3)^\times$, which is an infinite-dimensional Lie group, not a finite group. T27's algebraic apparatus is calibrated for the **ray class group** at fixed finite conductor; extending it to infinity-type characters requires building a separate transfer matrix from the unitary characters of the archimedean place into the same simplicial axes.

This is not a technical inconvenience that can be patched. It is the difference between Dirichlet $L$-functions (finite-order characters of $(\mathbb{Z}/N)^\times$, where the simplicial framework's tools natively live) and Hecke $L$-functions of *positive* infinity type (which include the entire family of motivic $L$-functions of weight $\ne 0$, including all elliptic-curve L-functions). The simplicial cubic bilateral $V^{\mathrm{Gauss},3}_{k,\psi}$ at row $k$ is a *finite* sum of cubic Gauss sums over a *finite* unit group; for $\psi_d$ of infinity type $(1, 0)$, there is no such finite Gauss-sum representative.

**Obstruction 3: Positivity is calibrated at $s = 1/2$, BSD's analytic content is at $s = 1$.** This was flagged in the assignment but bears restatement. The cubic Weil positivity criterion of ocho §3, the cubic Bombieri witness §3.2.1, and the cubic Fejér class $\mathcal{G}$ are all anchored at the critical line $\mathrm{Re}(s) = 1/2$, where the functional equation pairs $s \leftrightarrow 1 - s$. The cubic A–C tensor of siete §5 exists at all $s$, but its **positivity properties** — the load-bearing structural content the program has developed — are at the symmetric point. BSD-1 (the order-of-vanishing statement) is at $s = 1$, which is the *edge* of the critical strip $1/2 < \mathrm{Re}(s) < 1$ for the Hecke L-function (whose functional equation is $s \leftrightarrow 1 - s$ for the GL$_1$ Hecke L over Q, but $s \leftrightarrow 2 - s$ for the weight-2 modular form $f_E$). The simplicial framework has nothing calibrated to detect orders of vanishing at $s = 1$.

### Partial fit: the cubic A–C tensor at s = 1

The cubic A–C tensor $T^\zeta(\chi_a, \chi_b, \chi_c; s, N)$ exists at every $s$, and via Gauss-sum duality (siete §6) it factors through products $L(s, \psi_1) L(s, \psi_2) L(s, \psi_3) / \zeta(s)^3$ with the selection rule $\psi_1 \psi_2 \psi_3 = $ trivial. **At $s = 1$, $\zeta(s)$ has a simple pole**, so the tensor has structural singularities; the natural object would be $T^\zeta \cdot \zeta(s)^3$ at $s = 1$, which is regular and detects the **leading L-value product** structurally.

This partial fit could in principle be lifted to detect, at $s = 1$, the product $L(1, \psi_1) L(1, \psi_2) L(1, \psi_3)$ for finite-order character triples whose product is trivial. The cubic order would then encode the **product of class numbers** (via Dirichlet's class-number formula relating $L(1, \chi)$ to class numbers of imaginary quadratic fields) rather than ranks of elliptic curves. This is interesting but it is **not BSD**.

---

## (d) Tractability vs RH via the same framework

This section answers the load-bearing question honestly.

**Where RH sits in the program (as of 2026-05-22, per project_rh_structural_reduction memory file).** Five papers (siete–ocho–nueve–diez–once), 14 empirical probes, [A1'] and [A2'] proved at referee level (diez §1, §2), [A3'] reduced to a primorial-indexed Bombieri–Vinogradov estimate at rate $\theta_0(p_n) = 1 - C^*/n$ with $C^* \le 2.80$ conjectural. The program's "structural reduction" is real: RH is equivalent to a single explicit polynomial-rate EH refinement on squarefree primorial moduli (ocho §7.3 "careful proof outline in diez §3").

The framework is **calibrated** for this question: the cubic Weil positivity, the Fejér class $\mathcal{G}$, the conductor selection rule, the discrete primorial witness $\mathrm{pure}_V(P_n) = 2 + (1/6)\sum_{i=3}^n(p_i^2 - 1)$, the discrete-to-continuous bridge at PNT precision, and the cubic A–C tensor of $\log\zeta$ all converge at $s = 1/2$ on the joint product $\Xi_N$ at primorial $N$. Every piece of machinery the program has built lands on RH naturally. The residual analytic content [A3'] is open but not unboundedly so.

**Where BSD-CM-j=0 would sit in the program.** Four observations:

1. **The classical baseline is much higher than for RH.** For RH, all attacks before the simplicial program have been at the quadratic order (Bombieri's Weil-criterion, Selberg, Levinson, Conrey, Riemann–Siegel, Heath-Brown moments) — the cubic order is genuinely a new structural level. For BSD-CM-j=0 in rank 0 and rank 1, Coates–Wiles + Rubin + Gross–Zagier + Kolyvagin have already closed the problem. Adding cubic-Galois structural content to a problem already classically resolved gives marginal value at best.

2. **The open case (rank $\ge 2$) is structurally harder than the closed cases, not easier.** For rank $\ge 2$, the natural object becomes $L^{(2)}(E, 1)$ — the second derivative — and Heegner-point methods break down because the natural Heegner point lives in $E(K)$ for $K$ a CM imaginary quadratic, and Gross–Zagier expresses $L'(E, 1)$ via this point, not $L''(E, 1)$. The simplicial framework's machinery at cubic order would need to detect a **second-order zero at $s = 1$**, which requires Taylor-expanding the cubic A–C tensor around $s = 1$ rather than around $s = 1/2$. The program has done no such expansion.

3. **The infinity-type obstruction (c-2 above) is rigid.** Even if one tried to retool the cubic bilateral $W^{(3)}$ to incorporate the archimedean character $\psi_\infty(\alpha) = \alpha/|\alpha|$, the resulting transfer matrix would no longer have the **closed-form cubic Gauss-sum structure** of T27 Theorem A — the load-bearing identity. The simplicial program's calculations all depend critically on the finiteness of $W^{(3)*}W^{(3)} = \varphi_3(\mathfrak{m}) I_{\varphi_3(\mathfrak{m})}$, which is a finite-group-orthogonality identity. Extending to continuous infinity-type characters introduces a Plancherel measure and integral kernels in place of finite sums — qualitatively different machinery.

4. **The conductor mismatch (c-1 above) means primorial-sweep methods give no immediate purchase.** The framework's organizing principle — "do everything at primorial conductor $N \in \{30, 210, 2310, \ldots\}$, prove a primorial-indexed BV bound, then take $N \to \infty$" — does not naturally apply to BSD where each $E_d$ has its own fixed (non-primorial) conductor.

**Honest verdict.** RH-via-simplicial is in a state where one residual analytic statement ([A3'] = polynomial-rate EH on primorial moduli) closes the chain, and that statement has a "careful proof outline" already (diez §3). BSD-CM-j=0 via simplicial m=3 is in a state where even the algebraic substrate (T27's $W^{(3)}$) does not natively contain the relevant L-functions; the open cases (rank $\ge 2$) are harder than the closed ones, not easier; and the framework's positivity machinery is calibrated for the wrong $s$. **BSD via the simplicial framework is less tractable than RH via the same framework, by a wide margin.**

---

## (e) Concrete sub-target

If the director nevertheless wishes to test the framework against an analytic-NT problem with a different structural texture from RH, the most defensible focused target is **not** BSD itself but a closely-related one for which the simplicial cubic tools are *natively* calibrated:

### Sub-target candidate: A cubic-bilateral identity for $L(1, \psi)$ on finite-order cubic Hecke characters at primorial cubic conductor

**Statement (proposed):** Let $\mathfrak{m} = N \cdot \mathbb{Z}[\zeta_3]$ for primorial $N$. For every primitive **finite-order** Hecke character $\psi$ of $(\mathbb{Z}[\zeta_3]/\mathfrak{m})^\times$, T27's cubic bilateral factorization gives an exact identity
$$L(1, \psi) \;=\; \frac{1}{N(\mathfrak{m})}\sum_{k=1}^{N-1} R_k^{(3)} \cdot S_k^{(3)}(\psi) \cdot \mathcal{R}_k^{(3)}(\psi),$$
where $S_k^{(3)}(\psi)$ is the cubic Helmert-Hecke row sum (T27 Theorem A) and $\mathcal{R}_k^{(3)}(\psi)$ is an explicit residue weight at $s = 1$ derived from the cubic-Galois eigenstructure of $G^{(3)} = U^{(3)*}U^{(3)}$.

**Why this is a defensible target:**

- It is **at $s = 1$**, but for **finite-order** Hecke characters where the L-function is regular at $s = 1$ (unlike $\zeta_{\mathbb{Q}(\zeta_3)}$ which has a pole), so the analytic content is a *value* not a *vanishing order*.
- It is the natural cubic analog of Dirichlet's class number formula $L(1, \chi) = \frac{2\pi h}{w \sqrt{|D|}}$ (for non-trivial $\chi$ mod $D$, imaginary case), with the simplicial cubic-Galois weights playing the role of the explicit class-number / period combination.
- It would give a **new explicit formula** for cubic class numbers of $\mathbb{Q}(\zeta_3)$-ray class fields at primorial cubic conductor, expressed via the cubic Helmert-Gauss-Hecke ladder.
- It is **structurally adjacent to BSD** without being BSD: the class-number formula at $s = 1$ for finite-order Hecke characters is the GL$_1$-cuspidal analog of the BSD statement (Tamagawa number conjecture at the GL$_1$ level).
- It would test whether T27's non-trivial Gram $G^{(3)}$ supplies the kind of "genuinely new analytic content beyond Parseval" that the cubic-vs-quadratic comparison promised — at $s = 1$, where the L-value lives, rather than at $s = 1/2$, where positivity lives.

**Tractability.** The identity follows by Mellin-transforming T27 Theorem D ("cubic-side prime functional decomposition") with weight $w(n) = 1/N(n)$ at $s = 1$ and using analytic continuation of the cubic Helmert-Hecke kernel. The residue weight $\mathcal{R}_k^{(3)}(\psi)$ is the cubic-Gauss-sum analog of the classical Gauss-sum prefactor in Dirichlet's class-number formula. This is **bounded analytic-number-theory work**, on the order of two to three weeks of focused calculation, comparable to T9.4 in scope.

**What it would NOT achieve.** It would *not* address BSD for elliptic curves, because $\psi_d$ for $E_d$ is of infinity type $(1, 0)$, not finite order. The identity would live one structural level "below" BSD: at the GL$_1$ class-number-formula level rather than the GL$_2$ modular-form level. Whether the framework can be lifted from GL$_1$ to GL$_2$-Hecke (i.e., from finite-order to infinity-type-$(1,0)$ characters) is a much harder forward question that this sub-target does *not* attempt to settle.

---

## (f) Recommendation

**Do not pursue BSD via the simplicial m=3 framework as a primary target.**

Justification, in order of decreasing weight:

1. **The classical state of BSD-CM-j=0 leaves no first-order opening.** Coates–Wiles (rank 0), Gross–Zagier–Kolyvagin (rank 1), and Rubin's Iwasawa main conjecture have closed the cases the framework's tools would naturally address. The open cases (rank $\ge 2$, $\Sha$ finiteness in general) are not aligned with what the cubic Kummer clock provides.

2. **The infinity-type obstruction is structural, not technical.** T27's $W^{(3)}$ is a finite-group-orthogonality construction. The Grossencharacters $\psi_d$ are not in the finite Hecke-character group T27 aggregates. Patching this requires building an entirely new transfer matrix over the idele class group of $\mathbb{Q}(\zeta_3)$ — comparable in scope to the original construction of T9 and T27 combined.

3. **The positivity machinery is at the wrong $s$.** Ocho/diez's cubic Weil positivity is at $s = 1/2$. BSD's analytic content is at $s = 1$. No piece of the program's positivity stack carries over without re-derivation.

4. **The conductor mismatch defeats the primorial-sweep organizing principle.** The framework's distinctive structural lever — primorial conductor $N \to \infty$, with $\mathrm{pure}_V(P_n) \sim n^3(\log n)^2/18$ as the discrete witness — has no analog for the $E_d$ family.

5. **Opportunity cost.** The RH program is at "one residual statement away" with a proof outline (diez §3) in hand. Pursuing BSD via the same tools would divert attention from closing [A3'] (the polynomial-rate EH bound, structurally reducible to Polymath-8-scale work) toward building entirely new infrastructure to address questions that classical methods have already settled in the available cases.

**Calibrated alternative.** If the director wishes to demonstrate that the cubic bilateral has *additional* applications beyond RH, the sub-target of §(e) — an explicit class-number formula for finite-order cubic Hecke characters at primorial cubic conductor — is a tractable, structurally-adjacent test. It would:

- Verify that T27's non-trivial Gram $G^{(3)}$ delivers content beyond Parseval at $s = 1$ (the L-value side), not only at $s = 1/2$ (the positivity side);
- Produce a new, explicit identity within the framework's natural calibration;
- Take roughly 2–3 weeks rather than the indefinite timeline implied by a full BSD attack;
- Leave the RH closure path uninterrupted.

This sub-target should be approached as **demonstration**, not as a load-bearing piece of the program. If it works cleanly, it strengthens the case that the cubic Kummer clock has the structural content T27 §10 claimed. If it fails or reduces to a known identity, that itself is informative — it would localize where the simplicial framework genuinely adds analytic content versus where it reproduces classical machinery in new notation.

---

## Bottom line

BSD for CM elliptic curves at $j = 0$ over $\mathbb{Q}(\zeta_3)$ at primorial cubic conductor *looks* like an exact fit for the simplicial m=3 rung because the base fields match. On closer inspection, three independent structural obstructions — conductor mismatch, infinity-type mismatch, and positivity at the wrong $s$ — break the apparent alignment. The classical state of the problem in the cases the framework could plausibly reach (rank 0 and 1) is fully resolved; the open cases (rank $\ge 2$, $\Sha$ finiteness) are precisely the cases the framework's positivity machinery does not address. Pursuit is not recommended. A focused two-to-three-week sub-target on a finite-order class-number formula at primorial cubic conductor is the most defensible nearby alternative if the director wishes to exercise the cubic bilateral's $s = 1$ content without disturbing the RH closure path.

---

*— Assessment prepared by Claude Opus 4.7, May 26, 2026, in dialogue with the simplicial program's m=3 rung papers (T10, T27), ocho's cubic positivity criterion, and the recent diagnostic probes (probe_T27, probe_T27_m6, probe_universal_W). The structural objections concentrated on infinity-type mismatch (the load-bearing one) were identified by direct comparison of T27 §4's finite-Hecke-character setup with the Grossencharacter $\psi_d$ of $E_d$. The recommendation is calibrated honesty: the framework's RH calibration is sharp, its BSD alignment is illusory, and the director's time is better spent closing [A3'].*
