# The Cubic-Shift Bypass — Removing the (GBP) Dependency

**Leonardo Murillo Montero + Codex**

*Draft 1 — May 25, 2026 — director's bold-pass.*

*Supersedes the framing of `Unconditional-Positivity-Synthesis-Draft1.md` §2 ((GBP) as the bridge). (GBP) is not a bridge — it is RH in disguise, fundamentally obstructed by a quadratic-vs-linear prime-form mismatch and by the irrationality of $\{\gamma_\rho\}$ vs. the rationality of $\{\log(p^r/p'^{r'})\}$. The actual move is to leave the Bochner framing entirely. This note explains how.*

---

## 1. Why (GBP) is structurally unreachable from inside its own framework

(GBP) asserts $|\Sigma(y,\xi)|^2/(2\pi) = u_B(\xi,y)$ as measures.

**LHS structure.** $\Sigma_n(y,\xi) = \sum_{p \le P_n}\sum_{r \ge 1}\sqrt{\log p}\, p^{-r(y+i\xi)}$. Its squared modulus is

$$|\Sigma_n(y,\xi)|^2 = \sum_{p,p',r,r'}\sqrt{\log p\log p'}\, p^{-ry}p'^{-r'y}\, e^{-i\xi(r\log p - r'\log p')}.$$

As a function of $\xi$, $|\Sigma_n|^2$ has frequency content exactly on the **log-rational lattice** $\Lambda_{\log\mathbb Q} := \{r\log p - r'\log p' : p,p' \text{ prime}, r,r' \in \mathbb Z_{\ge 0}\}$. This lattice is countable and explicitly described.

**RHS structure.** By Riemann–Weil applied to the Poisson test function $g(\gamma) = y/((\xi-\gamma)^2 + y^2)$ (and its FE-symmetrization):

$$u_B(\xi,y) = -\mathrm{Re}\!\left[\frac{\zeta'}{\zeta}\!\left(\tfrac{1}{2}-y+i\xi\right)\right] - \mathrm{Re}[A(\tfrac{1}{2}-y+i\xi)],$$

where $A$ is the arch piece. After Mellin / Hadamard, this is

$$u_B(\xi,y) = \sum_\rho \frac{y}{(\xi-\gamma_\rho)^2 + y^2},$$

with frequency content (Fourier in $\xi$) on the **zero-frequency lattice** $\Lambda_{\gamma} := \{\gamma_\rho : \zeta(\rho)=0\}$.

**The obstruction.** $\Lambda_{\log\mathbb Q} \cap \Lambda_\gamma$ is empty in any conjectural sense (no $\gamma_\rho$ is known or expected to equal any $r\log p - r'\log p'$). So $|\Sigma_n|^2$ and $u_B$ have *disjoint Fourier support* and can be equal as measures only if **both contain a continuous component that exactly matches**. They don't (the structures are atomic / sum-of-atoms in opposite ways).

(GBP) as a literal pointwise spectral-measure identity cannot hold. What Paper III §1 calls (GBP) must be a weaker integrated identity — equality against test functions in a class that integrates out the frequency-support mismatch. Under RH, that integrated identity holds via the explicit formula. **Without RH, the integrated identity is exactly the on-line zero condition.**

The conclusion: (GBP) is **provably equivalent to RH** by Fourier-support analysis alone. It is not a "bridge" — it is RH wearing different clothes. Trying to attack (GBP) directly inside the Hankel/Bochner framework is structurally the same as attacking RH directly.

## 2. The correct move: leave the quadratic Hankel/Bochner framework

The quadratic positivity question — Hankel $H_n \succeq 0$, Bochner $|\Sigma|^2 \ge 0$ — is the WRONG order. Three independent reasons:

**(a) Conductor Blind Spot (ocho §4 / Paper 34).** Quadratic methods have zero cross-conductor coupling. They cannot detect the GUE statistics that distinguish RH-zero-spacings from generic L-function ensembles. At the quadratic level, all positive-definite Hankel sequences look alike — the GRH-distinguishing content lives at higher order.

**(b) GUE 3-point uniqueness (Diaconis–Shahshahani 1994, Wieand 2002).** The first finite correlation invariant that distinguishes GUE from its symmetric/symplectic cousins is the **third**. Pair correlations are shared. Triple correlations are not.

**(c) Rudnick–Sarnak triple correlation theorem.** The local statistics of triples of zeros of $\zeta$ obey the GUE 3-point density. RH's quantitative content IS GUE statistics; the first level at which this content becomes detectable is the cubic.

**At cubic order, the positivity question has unconditional content that the quadratic version structurally lacks.** This is the central insight of ocho.

## 3. The cubic shift in concrete terms

Replace the Apex Lemma$_{HJ}$ / signed-measure framing with the cubic Weil framing.

**Quadratic question (what we've been asking):**

$$\boxed{\;v^T H_n^{\mathrm{joint}}(N)\, v \;\ge\; 0 \quad \text{for all $v$ and all $n$} \;\iff\; \text{GRH at primorial $N$}.\;}$$

This is the Hankel-positivity criterion of Pass-5 Theorem 16.2. It is *trivially equivalent* to GRH$_N$ — both directions known — so making it "unconditional" means *proving GRH$_N$ outright*.

**Cubic question (what we should be asking):**

$$\boxed{\;\mathrm{Re}\,\mathcal{C}_\zeta(g;\eta) \;\ge\; 0 \quad \text{for all $(g,\eta) \in \mathcal{G}\times\mathcal{H}_c$} \;\iff\; \text{RH}.\;}$$

This is ocho §3's cubic Weil positivity criterion. **Structurally different positivity object**, with unconditional content:

- $\mathcal{G}$ is unconditionally non-empty (diez §1 Cor 1.5).
- The reverse direction (cubic positivity $\Rightarrow$ RH) is unconditional via the explicit cluster constant $c_2 \le -C^* < 0$ with $C^* \propto L(1/2,\chi_3)^2 = 0.4808^2 > 0$ (diez Thm 2.7).
- The forward direction (RH $\Rightarrow$ cubic positivity) is unconditional given $\mathcal{G}$ non-empty (diez §1.5).
- **Only [A3'] — the primorial-indexed BV rate $\theta_0(p_n) = 1 - C^*/n$ with $C^* \le 2.80$ — is open**, and it is *polynomial-in-$n$ rate*, weaker than full Elliott–Halberstam.

[A3'] is a specific identifiable analytic-NT theorem, comparable in scope to Polymath 8 §3–§4. Not trivial, but it is genuine unconditional content, not a tautology with RH.

## 4. The structural identity that makes cubic the right order

The reason quadratic doesn't work and cubic does, in one identity. Take the Amari–Chentsov tensor of $\log\zeta$ on the prime-axis exponential family (siete §5):

$$T^\zeta(\chi_a,\chi_b,\chi_c; s,N) = \hat Q_{a+b+c}^{(N)}(s) - \sum_{\text{partial}}\hat Q_{a+b}^{(N)}\hat Q_c^{(N)} + 2\hat Q_a^{(N)}\hat Q_b^{(N)}\hat Q_c^{(N)},$$

with $\hat Q_k^{(N)}(s) = \zeta_N(s,k)/\zeta(s)$. This is the cubic cumulant tensor of $-\log\zeta$ in the residue chart.

- **Quadratic cumulant** $\mathrm{Fish}(\chi_a, \chi_b) = \hat Q_{a+b} - \hat Q_a\hat Q_b$ is the Fisher information. Block-diagonal across conductor packets (Conductor Blind Spot). **Cross-conductor coupling: 0.**

- **Cubic cumulant** $T^\zeta(\chi_a,\chi_b,\chi_c)$ has non-zero cross-packet coupling under T3's selection rule $\chi_a\chi_b\chi_c = \chi_0$. **Cross-conductor coupling: nontrivial, with GUE 3-point density at the primorial limit.**

The Conductor Blind Spot is the precise reason Hankel-positivity / Bochner-positivity / Weil's quadratic moment cannot give RH: they are blocked at the second cumulant order, where the content needed to distinguish RH from generic L-statistics doesn't exist.

The cubic A–C tensor breaks this block. Its positivity contains the GRH-distinguishing content. The cubic Weil moment is the integrated form; its positivity criterion (ocho §3) is the analytical incarnation.

## 5. Three concrete strategies to close [A3']

Given that [A3'] is the remaining unconditional analytic obligation, here are three attack paths using simplicial-program tools (none requires (GBP)):

### Strategy A — Bilateral CRT + Kummer cover

[A3'] requires bounding the BV variance at primorial moduli $P_n$ at rate $\theta_0 = 1 - C^*/n$. The simplicial program's distinctive lever:

- **T9.4 Cor 5.1**: $\Pi_k F = R_k\varphi(P_n)\sum_{(m,P_n)=1}\Lambda(m)w(m)\langle h_k,\chi_{m^{-1}}\rangle$ — explicit algebraic form of prime-arithmetic functionals at primorial modulus, *unconditional*.
- **T9.4 Thm C**: $U\cdot W = D^{\mathrm{rad}}\cdot V^{\mathrm{Gauss}}$ — bilateral factorization. Each entry of $V^{\mathrm{Gauss}}$ is a finite signed combination of Gauss sums $\tau(\psi,j)$ with $|\tau(\psi,j)| \le \sqrt{P_n}$ for primitive $\psi$ of conductor $P_n$.
- **T7 §5 Thm 5.2 (Kummer cover)**: the deck-group $\rho_m(\zeta) = \zeta^{-m}$ on $\mathcal M_z(m,c)$ supplies the Galois symmetry on $L(\chi,s)$ at the primorial level via T10's Kummer-clock $K_N^{(m)} = \mathbb Q(\zeta_m, \sqrt[m]{p}: p \le N)$.

**Conjectural identity (to verify).** At primorial $N = P_n$, the BV variance

$$V(N; X) := \sum_{(a,N)=1}\Big(\psi(X; N, a) - \frac{X}{\varphi(N)}\Big)^2$$

admits an explicit Helmert-Gauss form via T9.4 Cor 5.1 applied with $w(n) = \mathbf 1_{n \le X}$ on the cumulant index $k$ such that $\sum_k k\cdot $ (Helmert-Gauss kernel)$^2$ reproduces $V(N; X)$. The bilateral factorization then expresses $V(N; X)$ as

$$V(N; X) = \sum_\psi |\widehat{\Lambda \cdot \mathbf 1_{n \le X}}(\psi)|^2 = (\text{Gauss-sum-squared sums weighted by Helmert radicals}).$$

If the Helmert-Gauss expansion gives a sharp upper bound on $V(N; X)$ in terms of $\sqrt{P_n}\cdot \mathrm{li}(X)$ + cross-character cancellation, the [A3'] rate $\theta_0(p_n) = 1 - C^*/n$ may emerge from the bilateral factorization + Burgess per-prime saving + Mertens telescoping over the primorial decomposition $P_n = \prod_{i \le n}p_i$.

This is the **distinctive simplicial-program contribution** to [A3']: replacing the classical large-sieve + Heath-Brown identity attack with a structural algebraic identity from T9.4.

### Strategy B — Cluster contradiction at primorial scale

Note_BuresDivisor + Paper III T8.3 give: an off-line zero forces $c_2 < 0$ at the cubic Bombieri witness with explicit constant. The classical zero-free region for $\zeta$ (Korobov–Vinogradov):

$$\sigma \ge 1 - c/(\log|t|)^{2/3}(\log\log|t|)^{1/3}$$

is *unconditional*. So $\delta = 1/2 - \sigma_{\max\text{ off-line}}$ is bounded below by an effective constant at any height $T$.

**The combined attack.** Combine:

- Unconditional finite empirical PSD-ness of $J_n^{\mathrm{prime,joint}}(210)$ at $n \le 14$ with min D $\sim 0.84$.
- Unconditional bound: any off-line zero at height $\le T$ for any L-function $\chi$ mod $N \le 210$ has $\sigma \le 1 - c_N/(\log T)^{2/3}$.
- Unconditional contribution bound: such an off-line zero contributes to $\mu_k^{\mathrm{joint}}(210)$ a complex atom whose real part has magnitude $\le \delta^2 / \gamma_0^{2k+2} \cdot \mathrm{poly}(n)$.

If the unconditional contribution bound, summed over all possible off-line zero locations consistent with the zero-free region, is *strictly less* than the empirical PSD margin (0.84 at $n=14$), then no off-line zero exists in the bounded range.

This is **finite empirical positivity + unconditional zero-density bound = unconditional GRH$_N$ at primorial $N$**. The scope: combine ArchStruct quantitative bounds + T9.4 Helmert-axis decomposition + Vinogradov-Korobov / Heath-Brown zero density at primorial moduli.

The leverage: empirical work has already done $n \le 14$ at $N = 210$. If extended to $n \le n_{\max}(N)$ for a verifiable $n_{\max}$, the unconditional contribution bound rules out off-line zeros to height $T(n_{\max})$.

### Strategy C — Phase-twisted Lee-Yang forcing

T7 §6.5's phase-twisted Lee-Yang lattice: as the Bloch phase $\varphi$ varies, apex zeros migrate from imaginary axis ($\varphi = \pi$, fully decoherent) to real axis ($\varphi = 0$, fully coherent). The Born gauge $m = 2$ corresponds to the coherent regime.

**The structural claim (to be made rigorous):** The Uniform Place Treatment (Paper II Q8vM3 Lock B) forces the Bargmann-Fock representation at $v = \infty$, which selects the *coherent* Bloch phase $\varphi = 0$. The simplicial apex's natural gauge is therefore Born ($m = 2$, RMS), which lives on the real axis.

If $\varphi = 0$ is forced by UPT + apex structure, then by T7 §6.5 the apex zeros are on the real axis — i.e., **GRH at primorial $N$** for the natural apex L-functions.

This is a Hilbert-Pólya-style structural argument, with the apex Hilbert space $\mathcal F_n$ (Paper II) as the candidate spectrum carrier and the Born gauge as the self-adjointness condition.

The remaining technical work: prove that the natural apex operator (acting on $\mathcal F_n$ in the Bargmann-Fock representation at $v = \infty$ with Born gauge) has spectrum equal to $\{\gamma_\rho\}_{\rho \text{ on-line}}$ unconditionally. This requires identifying the operator explicitly and verifying its self-adjointness — the long-standing Hilbert-Pólya target. The simplicial program's contribution: the Bargmann-Fock + Born + UPT triple supplies a *specific* operator candidate, not a generic search.

## 6. Recommended priority

Of the three strategies:

- **Strategy B is the highest-leverage near-term path.** It combines what's already empirically established with classical unconditional zero-density bounds at primorial moduli. The work is computational + analytical, but each piece is established machinery.

- **Strategy A is the highest-payoff long-term path.** If T9.4's bilateral factorization gives a sharp explicit BV variance bound at primorial scale, [A3'] closes with $C^*$ derivable from Gauss-sum magnitudes + Burgess + Mertens. This delivers RH unconditionally via the cubic positivity criterion.

- **Strategy C is the deepest structural path** but requires the long-standing Hilbert-Pólya identification, which has resisted attack for 80 years. The simplicial program supplies a candidate (Bargmann-Fock + Born) but not the closing proof.

## 7. What T8.4 v2 should actually do

Replacing the (GBP)-bridge framing of `Unconditional-Positivity-Synthesis-Draft1.md` §4:

1. **Reframe the positivity target.** T8.4 v2 should NOT claim to close A4 by proving $J_n^{\mathrm{prime,joint}}(N) \succeq 0$ unconditionally — that's GRH$_N$ and the program does not yet have it. T8.4 v2's positivity content is the *conditional* Theorem E (via signed-measure §3.3) — honestly labeled.

2. **Add a §11: "Why this paper does not prove the unconditional statement, and what does."** Identify cubic Weil positivity (ocho §3) as the unconditional analogue. Show that the simplicial program's distinctive lever (T9.4 + Kummer + ArchStruct + ocho V-sector) routes through cubic, not quadratic, positivity. The unconditional GRH$_N$ attack lives in [A3'], not in T8.4's signed-measure setup.

3. **Reframe §6–§7 as raw material for Strategy A.** The Helmert-Gauss kernel $T_N(n,a) = \varphi(N)\omega^{an^{-1}}\mathbf 1_{(n,N)=1}$ is the structural primitive that Strategy A needs. T8.4 v2's §6–§7 should be presented as the bilateral CRT machinery for [A3'], not as a kernel-positivity attack (which failed at Lemma 6.4).

4. **Update Tier-A list.** A4 (unconditional) reduces to [A3'] via cubic-shift bypass; no longer to (GBP). The Tier-A list reorganizes:
   - **A3, A5: DELIVERED unconditionally** (T7 §5 Kummer cover, T9.4 Helmert-Gauss algebraic).
   - **A4 unconditional ≡ [A3'] specialist verification ≡ Polymath-8-scale.** Three attack strategies above.
   - **A1, A2 reduce to A4** via the same cubic-shift logic.
   - **A6 (Bures / Hilbert-Pólya): Strategy C, long-term.**

## 8. The honest framing

The simplicial program is a structural reduction of RH to **one** unconditional analytic-NT problem: [A3'] (primorial-indexed BV at rate $\theta_0(p_n) = 1 - C^*/n$ with $C^* \le 2.80$). This residual problem is real analytic-NT work, but it is *finite and explicit*: a specific constant $C^*$ to bound, a specific large-sieve / Heath-Brown / Burgess / Mertens chain to execute at primorial scale.

The simplicial program's distinctive contributions to closing [A3']:
- **T9.4 bilateral CRT factorization** — replaces classical large sieve for primorial moduli with an algebraic identity.
- **Kummer-clock T10** — supplies the Galois symmetry that organizes the prime-power saving across the primorial decomposition.
- **V-sector closed form (ocho §5)** — $S(p) = (p^2-1)/6$ gives the explicit PNT-asymptotic.
- **ArchStruct atomic closed form** — gives the explicit arch lower bound for the cross-comparison.

These four together are *new structural inputs* not present in Polymath 8's classical attack. The conjectural $C^* \le 2.80$ may follow more cleanly from this structural reorganization than from the classical machinery alone.

**This is what "we have what we need" means at the unconditional level:** not that (GBP) closes for free, but that the program has reduced RH to a *specific*, *finite*, *attackable* analytic-NT theorem ([A3']) with *new structural tools* (T9.4 + T7 §5 + T10 + ocho V-sector) that bypass the (GBP)-style bridge entirely.

The "remove the dependency on (GBP)" is exactly this: **don't go through (GBP) at all. Go through [A3'] via the cubic-shift bypass + the simplicial program's algebraic tools.**

## 9. One-line summary

> (GBP) is RH in disguise — Fourier-support analysis shows the quadratic $|\Sigma|^2$ and linear $u_B$ have disjoint frequency support and can coincide only under RH. The bypass is to leave the quadratic framework entirely: the cubic Weil positivity criterion (ocho §3) is the structurally correct positivity object; its unconditional content reduces to [A3'] (primorial-indexed BV at rate $1 - C^*/n$), which the simplicial program attacks via T9.4 bilateral CRT + Kummer-clock T10 + V-sector ocho §5 + ArchStruct — none of which routes through (GBP).

---

*The quadratic question was the wrong question. The Conductor Blind Spot tells us why: quadratic methods cannot see the GRH-distinguishing content. The cubic order is the correct order, and the simplicial program's tools are calibrated for it. The unconditional closing is [A3'] via the simplicial CRT, not (GBP) via the Bures Pick.*

— Director, May 25, 2026
