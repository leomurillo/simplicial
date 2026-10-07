# Iwasawa Invariants for CM Elliptic Curves at $j=0$ via the Simplicial Cubic Machinery — Assessment

**Leonardo Murillo Montero (assigned to Claude assistant)**

*Assessment draft — May 26, 2026*

---

> *The simplicial cubic rung (T27, T10 §5.1, T7 §5) is structurally adapted to the Eisenstein base $\mathbb{Z}[\zeta_3]$ — which is precisely the CM ring of $j=0$ elliptic curves. The question is whether that structural fit projects through the C-to-$p$-adic interface, and the honest answer is that it does not by itself. This document explains where the fit is real, where the gap is real, and what residual sub-target — if any — survives.*

---

## (a) Problem statement

Let $E/K$ be an elliptic curve over a number field with good reduction at a prime $p$. The **$p$-adic $L$-function** $L_p(E,s)$ is constructed as a measure on the Iwasawa algebra $\Lambda := \mathbb{Z}_p[[\mathrm{Gal}(K_\infty/K)]] \cong \mathbb{Z}_p[[T]]$, where $K_\infty$ is the cyclotomic $\mathbb{Z}_p$-extension of $K$. The two basic invariants extracted from the power series $L_p(E,T) = \sum a_n T^n \in \Lambda$ (after Mahler normalization) are:

- $\lambda(E,p) := \deg(\text{distinguished polynomial})$ — the number of zeros of $L_p$ in the open unit disk; equivalently, the order of vanishing at the trivial character on the cyclotomic tower.
- $\mu(E,p) := \min_n v_p(a_n)$ — the $p$-adic content of the leading Iwasawa expansion.

For **CM elliptic curves at $j=0$** the relevant family is
$$E_d: y^2 = x^3 + d, \qquad \mathrm{End}(E_d) \otimes \mathbb{Q} = \mathbb{Q}(\zeta_3),$$
with CM by the Eisenstein order $\mathbb{Z}[\zeta_3]$. The natural base is $K = \mathbb{Q}(\zeta_3)$; the $p$-adic theory works cleanly for primes $p > 3$ that **split** in $\mathbb{Z}[\zeta_3]$ (i.e., $p \equiv 1 \pmod 3$). Each such $p$ factors as $p = \pi \bar\pi$ in $\mathbb{Z}[\zeta_3]$, and one builds two anticyclotomic / cyclotomic $\mathbb{Z}_p$-towers, one at each place above $p$. The $p$-adic $L$-function $L_p(E_d, s)$ then interpolates Hecke $L$-values of cubic Grössencharaktere along this tower.

The structural target: explicit values (or upper bounds, or generic vanishing statements) for $\lambda(E_d, p), \mu(E_d, p)$ in terms of arithmetic data of $d$, $p$, and the conductor.

## (b) Classical status

The CM case at $j=0$ is among the most thoroughly worked in Iwasawa theory:

1. **Coates–Wiles (1977).** For CM elliptic curves over $\mathbb{Q}$ (covering both $j=0$ and $j=1728$), if $L(E,1) \ne 0$ then $E(\mathbb{Q})$ is finite — the first deep instance of BSD. Their proof constructs Eisenstein series on $\mathbb{Q}(\zeta_3)$ (resp. $\mathbb{Q}(i)$) and uses **elliptic units** as the analytic input.

2. **Rubin (1981, 1987, 1991).** Proved the **Iwasawa Main Conjecture for CM elliptic curves** (and more generally, for imaginary quadratic fields) at primes of good ordinary reduction. The Main Conjecture identifies the characteristic ideal of the Selmer group with the $p$-adic $L$-function as ideals in $\Lambda$. As a direct corollary, $\mathrm{ord}_T L_p$ equals the Selmer corank, hence (BSD-conjecturally) the rank.

3. **Greenberg (1994, 2001).** Refinements of Iwasawa invariants, including the conjecture (later proved in CM cases) that $\mu(E,p) = 0$ for ordinary primes, and the structure of $\lambda$ in terms of local invariants and Tamagawa numbers. Greenberg's formula:
$$\lambda(E, p) = r_{\mathrm{an}} + \sum_\ell s_\ell + (\text{Tate–Shafarevich contribution})$$
where $r_{\mathrm{an}}$ is the analytic rank and $s_\ell$ counts local terms.

4. **Pollack–Stevens, Pollack–Weston.** $p$-adic Hodge-theoretic refinements for supersingular primes (those $p \equiv 2 \pmod 3$ in our setting, since they are inert in $\mathbb{Z}[\zeta_3]$ — exactly the supersingular case for $E_d$). Pollack's plus/minus decomposition of $L_p$.

5. **Kato (2004).** Euler systems for modular forms; gives one divisibility direction of the Main Conjecture in full generality.

6. **Explicit tables.** For specific $(E_d, p)$ pairs, $\lambda$ and $\mu$ are computed by direct Iwasawa-algebra calculation (modular symbols / overconvergent cohomology / Pollack's algorithms). There is no closed-form formula in terms of $(d, p)$ alone; the values track subtle local invariants and Heegner-point heights.

**Summary of the classical situation.** The structural theory (Main Conjecture, characteristic ideal) is settled for ordinary $p$; the supersingular case is settled up to the plus/minus refinement; explicit numerical values are tabulated but resist closed-form expressions. A predictive formula for $\lambda(E_d, p)$ given $(d, p)$ in a closed combinatorial form would be a genuine contribution.

## (c) Simplicial alignment: where the cubic machinery genuinely fits

The simplicial framework at $m=3$ has three pieces of natural Eisenstein-base structure:

**(c.1) Base ring match.** T27's natural ambient is $\mathbb{Z}[\zeta_3]$, the Eisenstein integers (T27 §1.2). This is exactly $\mathrm{End}(E_d)$ for $j=0$ curves. The simplicial cubic Kummer clock $K_N^{(3)} = \mathbb{Q}(\zeta_3, \sqrt[3]{p}: p \le N)$ at primorial $N$ sits over the CM field. **This is not a coincidence to be discounted: both the cubic gauge corridor and the $j=0$ CM theory single out $\mathbb{Q}(\zeta_3)$ as the canonical cubic-Galois ambient.**

**(c.2) Hecke character orthogonality machinery.** T27 §4–§6 develops the cubic bilateral factorization $U^{(3)} W^{(3)} = D^{\mathrm{rad},3} V^{\mathrm{Gauss},3}$ over Hecke characters of $\mathbb{Z}[\zeta_3]$ modulo $\mathfrak{m} = N\mathbb{Z}[\zeta_3]$. The cubic Helmert–Gauss kernel (Theorem C)
$$T_\mathfrak{m}^{(3)}(n, a) = \varphi_3(\mathfrak{m}) \cdot \omega_\mathfrak{m}^{\mathrm{Tr}(a n^{-1})} \cdot \mathbf{1}_{(n,\mathfrak{m})=(1)}$$
expresses character orthogonality on Eisenstein units at primorial conductor. The CM $p$-adic $L$-function $L_p(E_d, s)$ interpolates Hecke $L$-values $L(\psi, 1)$ for cubic Grössencharaktere $\psi$ of $\mathbb{Z}[\zeta_3]$. **The simplicial cubic bilateral organizes exactly the right character family**, modulo the C-vs-$p$-adic shift addressed in (d).

**(c.3) Genuine spectral content at $m=3$.** The probe `probe_T27_output.txt` confirms T27 §7's structural claim: the cubic Gram $G^{(3)} = U^{(3)*}U^{(3)}$ is **not** identity (unlike $G^{(2)} = I$). At $N=30$, $G^{(3)}$ has 29 distinct eigenvalues spread in $[3.21, 4.02]$ with condition number $\approx 1.25$. The cubic-Galois richness is real, manifested as the non-trivial Christoffel-like kernel $G^{(3)}$ that the $m=2$ bilateral did not have. **At $m=3$ the bilateral does not collapse to Parseval** — this is genuine analytic content beyond change of basis, the structural lever T27 §7.2 identified.

**(c.4) Kummer cover at $m=3$.** T7 Theorem 5.2 gives the Galois statement: the cubic apex $\mathcal{M}_z(3,c)$ is a section of the $\rho_3$-twisted line bundle on $\mathbb{CP}^{N-1}$, with deck group $\mu_N$ acting by $\zeta \mapsto \zeta^{-3}$. The cover is non-trivial whenever $N \nmid 3$, i.e., for all primorial $N \ge 30$. **This is an algebraic-geometric structure on the cubic gauge that, in principle, could pair with the Selmer side of Iwasawa theory** (where Kummer cohomology $H^1(\mathrm{Gal}, E[p^\infty])$ is the central object). The pairing is purely formal at this stage.

**Candidate alignment statement (speculative).** *If* one could attach a $p$-adic interpolation $L_p^{(3)}(\psi, s)$ to the simplicial cubic Helmert–Hecke row sum $S_k^{(3)}(\psi)$, one would conjecture that the cubic Helmert–Gauss kernel $T_\mathfrak{m}^{(3)}(n, a)$ specializes at the trivial character to a sum that recovers the standard CM $p$-adic interpolation formula. This is a **structural conjecture**, not a theorem. The interpolation has not been constructed — and constructing it is the C-vs-$p$-adic gap.

## (d) The C-vs-$p$-adic obstruction

This is the central tractability question. Six points, ordered from softest to hardest.

**(d.1) The framework is built over $\mathbb{C}$.** Every object in T0, T7, T9, T9.4, T10, T27 — the apex generators $\mathcal{M}_x$, the Helmert vectors $h_k$, the Helmert-Fourier transfer matrices $U^{(3)}$, the Gauss sums $\tau_3(\psi, a)$, the Hecke characters $\psi$ — takes values in $\mathbb{C}$. The Parseval / Plancherel / unitarity structure is $L^2$ over $\mathbb{C}$.

**(d.2) The $p$-adic theory is built over $\mathbb{C}_p$ / $\mathbb{Z}_p$.** $L_p(E, s)$ is a measure-theoretic / power-series object on $\Lambda = \mathbb{Z}_p[[T]]$. The relevant analytic structure is **rigid analytic geometry** (Tate algebras), **$p$-adic Banach spaces**, and **$p$-adic modular forms** (overconvergent cohomology). The interpolation is at $p$-adic values of $s$, not complex ones.

**(d.3) The bridge has known forms — none of them obvious from simplicial structure.** The classical $C$-to-$p$-adic bridges in CM Iwasawa theory are:

  - **Eisenstein measure construction** (Coates–Wiles, Katz). One constructs a $p$-adic measure interpolating special values of complex Eisenstein series. This requires $p$-adic modular forms on $\mathbb{Q}(\zeta_3)$, $p$-adic CM periods, and an explicit Eisenstein measure on the Iwasawa algebra.
  - **Comparison theorem at CM points** (Katz, Hida). The complex and $p$-adic CM periods at $j=0$ are related by an explicit algebraicity statement, allowing complex Hecke $L$-values $L(\psi, 1)/\Omega_\infty$ to determine $p$-adic interpolation values $L_p(\psi, s)/\Omega_p$.
  - **Modular symbols / overconvergent cohomology** (Pollack–Stevens). The $p$-adic $L$-function is built as a distribution-valued modular symbol; this is purely a $p$-adic construction with no $C$-side input beyond the underlying modular form.

  **None of these bridges is naturally produced by the simplicial cubic apparatus.** The simplicial framework does not currently have:
  - $p$-adic modular forms attached to its closure maps.
  - A $p$-adic period $\Omega_p$ attached to its Kummer cover.
  - An interpolation rule attached to cubic Helmert–Gauss kernels at $p$-adic specializations.

**(d.4) The "natural conductor" mismatch.** T27 works at the **primorial cubic conductor** $\mathfrak{m} = N\mathbb{Z}[\zeta_3]$ with $N \in \{30, 210, 2310, \ldots\}$ — a product of small rational primes. Iwasawa theory works at conductor $\mathfrak{p}^n$ for a **single** prime $\mathfrak{p}$ above $p$, with $n \to \infty$ in the $p$-adic tower. The conductor structures are orthogonal: primorial-N is "broad and shallow" (many primes, each appearing once); Iwasawa-tower is "narrow and deep" (one prime, all powers). T27's BV-style estimates at primorial conductor are exactly the wrong shape for a single-prime $p$-adic tower. **This is a sharp structural mismatch.**

**(d.5) Gauss sums vs. elliptic units.** The simplicial cubic Gauss sums $\tau_3(\psi, a)$ over $\mathbb{Z}[\zeta_3]/\mathfrak{m}$ are *additive* objects — sums of additive characters weighted by multiplicative Hecke characters. CM Iwasawa theory at $j=0$ runs on **elliptic units** $\theta(\mathfrak{a}; z)$ — Robert / Kato units in $K_2$ of the modular curve, with explicit logarithmic derivatives feeding into $p$-adic $L$-values. Gauss sums and elliptic units occupy different sectors of the arithmetic; the Coates–Wiles argument specifically uses elliptic units, not Gauss sums. **There is no known bridge from cubic Hecke Gauss sums to elliptic units at the level of refined Iwasawa invariants.**

**(d.6) The structural lever, where it might cross.** T27's central observation is that $G^{(3)} \ne I$ encodes cubic-Galois content that does not exist at $m=2$. If one could show that the eigenvalues of $G^{(3)}$ (or some natural specialization of them) admit a **$p$-adic interpolation across primorial $N$ and a single prime $p$**, that would be the bridge. Currently, no such interpolation is known or even sketched. The $G^{(3)}$ spectrum at $N=30$ is a set of 29 transcendental real numbers (eigenvalues of a specific Christoffel kernel); there is no $p$-adic identity satisfied by them.

**Bottom line on the gap.** The C-vs-$p$-adic obstruction is **not a matter of polishing**: it requires building, from scratch, a $p$-adic interpolation theory for the simplicial cubic structures. This would be a multi-paper program comparable in scope to the Katz / Hida construction of $p$-adic modular forms — *itself* a major piece of arithmetic geometry. The simplicial cubic framework, as it stands, **does not bridge to $p$-adic Iwasawa invariants**.

## (e) Concrete sub-targets, ranked

If the framework is to engage Iwasawa theory at all, the realistic sub-targets are these:

**(e.1) Most defensible: cubic Hecke $L$-value identities at primorial $\mathfrak{m}$ on the $\mathbb{C}$ side.** T27 Theorem F gives the cubic-Galois-weighted quadratic form
$$\vec{a}^* W^{(3)*} G^{(3)} W^{(3)} \vec{a} = \sum_{k=1}^{N-1} \frac{\varphi_3(\mathfrak{m})^2 |\Pi_k^{(3)}(X; \mathfrak{m})|^2}{(Nk(1+k^2))^{2/3}}.$$
Specializing $\vec{a}$ to the vector of cubic Hecke $L$-values $L(\psi, 1)$ at primorial cubic conductor produces an **explicit complex identity** linking $\sum_\psi |L(\psi, 1)|^2$ (weighted by $G^{(3)}$) to a Helmert–axis prime sum. This is a $\mathbb{C}$-valued result; it does not give $\lambda, \mu$ but it does give **a primorial-conductor Hecke $L$-value moment formula at $\mathbb{Q}(\zeta_3)$** that the classical literature may not have in this exact form. *Probably tractable; modestly novel; not Iwasawa.*

**(e.2) Possibly tractable: a structural reformulation of Coates–Wiles via the cubic apex.** Coates–Wiles uses the apex of cubic Eisenstein series on $\mathbb{Q}(\zeta_3)$. The simplicial cubic apex generator $\mathcal{M}_z(3,c)$ on $\mathbb{CP}^{N-1}$ at $N = $ (conductor of Hecke character) is a candidate organizing object. The question: **does the cubic conductor selection rule $a_1 + a_2 + a_3 \equiv c \pmod N$ (T0 Theorem 3.5, T3) reproduce, or refine, the elliptic-unit identities Coates–Wiles uses?** This is a structural / philosophical question more than a computational one. If yes, it gives a "cubic-categorical" rephrasing of Coates–Wiles. If no, the cubic apex is parallel structure not connected by a theorem. *Worth a focused 1–2 page check; high payoff if it works, modest cost if not.*

**(e.3) Speculative: $\mu = 0$ heuristics from cubic Galois richness.** Greenberg's conjecture that $\mu(E_d, p) = 0$ for ordinary $p$ might admit a heuristic via cubic Helmert–Gauss kernel non-vanishing. The simplicial Helmert–Gauss kernel $T_\mathfrak{m}^{(3)}(n, a)$ is non-degenerate (a single non-zero exponential) on coprime classes; if this non-degeneracy is the C-shadow of a $p$-adic non-vanishing argument, one would have a heuristic for $\mu = 0$. **This is highly speculative; would need explicit $p$-adic reformulation.**

**(e.4) Unlikely: explicit $\lambda(E_d, p)$ computation.** As discussed in (d.4)–(d.5), the conductor structures are mismatched and the Gauss-sum-vs-elliptic-unit gap is sharp. **Not a realistic sub-target at this stage.**

## (f) Recommendation: do not pursue Iwasawa invariants as a main target; pursue (e.1)–(e.2) as side outputs only

**Primary recommendation: NO.** The simplicial program should not adopt CM Iwasawa invariants as a focused target. The C-vs-$p$-adic gap is structural and substantial. Bridging it would require building a $p$-adic interpolation theory for the simplicial apparatus from scratch — comparable in scope to constructing $p$-adic modular forms (Katz, Hida). This is a multi-year program in arithmetic geometry that is **orthogonal** to the simplicial program's distinctive tools (closure maps, Helmert ladders, conductor selection rules, Kummer covers on $\mathbb{CP}^{N-1}$).

The natural Eisenstein-base alignment (point c.1) is real but is **not sufficient**: it is a coincidence of arithmetic ambient, not a coincidence of analytic structure. Many objects live over $\mathbb{Z}[\zeta_3]$; only a few of them are CM $p$-adic $L$-functions. The cubic Hecke characters T27 organizes are *not* the cubic Grössencharaktere of CM elliptic curves — they are Dirichlet-like characters of $(\mathbb{Z}[\zeta_3]/\mathfrak{m})^\times$ at primorial composite conductor, not infinity-type characters of weight 1 at prime-power conductor. The naming overlap is misleading; the objects are different.

**Secondary recommendation: extract (e.1) and (e.2) as side outputs from existing T27.**

- **(e.1) Primorial cubic Hecke $L$-value moment identity.** T27 Theorem F, specialized to the Hecke $L$-value vector, gives an identity that is genuinely novel as a $\mathbb{C}$-side moment formula at primorial cubic conductor. It is one paragraph of additional commentary in T27 §7 — costs nothing extra, modest payoff. **Recommend writing as a Corollary in T27.**

- **(e.2) Structural reformulation of Coates–Wiles.** A focused 1–2 page check: do the cubic conductor selection rule and the cubic apex generator reproduce the formal structure of Coates–Wiles' Eisenstein-series argument? If yes, write as a short note titled "Cubic-categorical reading of Coates–Wiles." If no, file as a forward-door check that the connection is structurally absent. **Cost: 2–4 hours. Recommend doing once.**

**Tertiary recommendation: do not commit to (e.3) or anything more speculative.** The $\mu = 0$ heuristic would need a $p$-adic reformulation that does not currently exist. Speculating about it without that reformulation generates technical debt without payoff.

**Comparative tractability.** Compared to the residual [A3'] for RH (which is concrete, BV-shaped, has explicit constants $C^* \le 2.80$ from diez, and lives natively in the simplicial $\mathbb{C}$-side), CM Iwasawa invariants are **strictly less tractable** by the simplicial framework. [A3'] is the right shape for the framework's existing tools; Iwasawa invariants are not. The director's primary RH/[A3'] track has structural priority.

**One closing observation.** The fact that the cubic gauge corridor singles out $\mathbb{Q}(\zeta_3)$, and that CM-at-$j=0$ also singles out $\mathbb{Q}(\zeta_3)$, is genuine — both arise from the canonical cubic-Galois structure of $\mathbb{Z}/3$. The simplicial framework and CM theory are **structurally cousins**, but cousins working on different planes (real/complex statistics vs. $p$-adic arithmetic geometry). The natural bridge between them is **not** the simplicial cubic bilateral; it is whatever future paper constructs a $p$-adic interpolation theory on simplicial structures. That paper is not T27, not [A3'], and not the next 6–12 months of program time.

---

## Appendix: where this assessment could be wrong

To be honest about uncertainty:

1. **If a $p$-adic interpolation of $G^{(3)}$ eigenvalues exists.** I have not searched the literature for $p$-adic interpolations of Helmert / cubic Christoffel-like kernels. If such a thing exists in the work of Pollack, Greenberg, or in $p$-adic Hodge theory of cubic Galois representations, the assessment in (d.6) could be too pessimistic.

2. **If the Coates–Wiles Eisenstein-series argument has a cubic-conductor selection-rule reformulation.** I have not done the focused check of (e.2). If the cubic selection rule $a_1 + a_2 + a_3 \equiv c \pmod N$ does reproduce the formal Eisenstein argument, the simplicial framework would have a genuine connection to CM Iwasawa — not via $p$-adic interpolation, but via structural rephrasing. This is the most likely place where the assessment is too cautious.

3. **If primorial-conductor moments map to single-prime-tower limits.** There is a known limiting procedure (Iwasawa descent / Mahler interpolation) that takes Dirichlet-character sums at varying conductor to $p$-adic measures. Whether T27's primorial-N expansion admits this kind of limit is a $p$-adic-analyst question I have not investigated.

These three caveats notwithstanding, the structural mismatch in (d.1)–(d.5) is real and decisive: the simplicial framework, as it currently stands, is not a tool for computing Iwasawa $\lambda, \mu$ invariants. Recommendation stands: **do not pursue as main target; harvest (e.1)–(e.2) as side outputs only.**

---

*End of assessment.*
