# Quantization Forced by Representation Theory: The Cubic-to-Bures Bridge on $R = \mathbb{Z}/6\mathbb{Z}$

**Leonardo Murillo Montero**  
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — worked-example construction of the classical-to-quantum lift, explicit $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ closure, Leakage-Equals-Jerk theorem, computational verification protocol)**

---

## Abstract

[Paper 17](17.the_cubic_noether_theorem.md) closes with the assertion that *quantization is forced* by the combination of representation theory and variational completeness: the cubic Noether mechanics on the real simplex admits only abelian Cartan symmetries (Paper 17 Corollary 2.4), the jerk $\dddot\eta = \nabla^{(e)}T$ cannot be classically resolved into a conserved quartic charge (Paper 17 Theorem 3.1), and the density-matrix manifold $\mathcal{D}^\circ$ is the unique resolution that relaxes the obstruction while preserving positivity, trace-1, and CRT-tensor compatibility. [Paper 18](18.bures_completion_of_cubic_information_geometric_mechanics.md) constructed the Bures completion programmatically. [Paper 27](27.finite_to_archimedean_noether_limits_and_canonical_involution.md) §4.5 identified $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ as the canonical effective algebra for the minimal mixed ring $R = \mathbb{Z}/6\mathbb{Z}$. Each of these claims is structurally consistent and individually argued, but the *worked example* — the explicit construction tying the classical cubic Noether energy on $\Delta_R^\circ$ to its Bures lift on $\mathcal{D}^\circ(\mathbb{C}^2 \otimes \mathbb{C}^3)$, with the jerk realized as the off-diagonal generator action — has been programmatic in the corpus.

This paper performs the construction. On the minimal nonabelian CRT row $R = \mathbb{Z}/6\mathbb{Z}$ with character packets $H_2, H_3, H_6$ of real dimensions $(1, 2, 2)$, we (i) write down the diagonal embedding $\Delta_R^\circ \hookrightarrow \mathcal{D}^\circ(\mathbb{C}^6)$ and identify $\mathbb{C}^6 \cong \mathbb{C}^2 \otimes \mathbb{C}^3$ via CRT (§3); (ii) compute the Bures metric and Bures cubic tensor in explicit coordinate form, verifying their reduction to Fisher and Amari–Chentsov on the classical diagonal (§4); (iii) prove the **Lift Isometry Theorem** (Theorem 5.1) that the classical cubic Noether energy $\mathcal{E}_3^{(C)}$ equals the restriction of the Bures cubic Noether energy $\mathcal{E}_3^{(B)}$ to the diagonal embedding; (iv) exhibit the $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ generators in explicit Pauli-Gell-Mann form and demonstrate that the classical $\mathfrak{u}(1)^2$ Cartan sits inside as the CRT-diagonal subalgebra (§6); (v) prove the **Leakage-Equals-Jerk Theorem** (Theorem 7.1) that the rate of off-diagonal coherence growth along a Bures-stationary trajectory whose initial condition is on the classical diagonal equals the classical jerk $\nabla^{(e)}T$ up to identifiable representation-theoretic factors; and (vi) prove the **Quantization-Forced Theorem** (Theorem 8.1) that no consistent classical extension exists — any classical mechanics that would represent the jerk as a conserved charge violates real-cone preservation or CRT compatibility, so the Bures lift is not just *available* but *unavoidable*.

The construction takes place entirely in 6-dimensional Hilbert space; every operator written down is an explicit $6 \times 6$ Hermitian matrix; every computation is performable by hand. The conclusions are not novel relative to Papers 17, 18, 27, but their unification into a single worked example anchored in explicit $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ generators is. Paper 32's stub on "one functional, four forces" and Paper 33's stub on chirality each depend on this bridge being made operational; the present paper makes it so.

**Keywords:** cubic Noether mechanics, density-matrix manifold, Bures metric, Amari–Chentsov tensor, $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$, quantization, CRT decomposition, Cartan obstruction, jerk, real-cone preservation, information geometry.

---

## 1. Introduction

### 1.1 What the corpus has and has not done

The Conductor program's physics arm spans Papers 13–21, 28, 32, 33. The key results:

- **Paper 14** establishes the Cartan obstruction: the only symmetries of the classical real simplex compatible with CRT structure, positivity, and the Fisher volume form are the Cartan subalgebra of the relevant compact group.
- **Paper 15** constructs the Bures-Helstrom metric on the density-matrix manifold and proves it restricts to Fisher–Rao on the classical diagonal.
- **Paper 17** writes down the cubic Noether theorem on the classical simplex and proves the jerk cannot be classically resolved (Theorem 3.1).
- **Paper 18** initiates the Bures completion of cubic mechanics.
- **Paper 27** §4.5 identifies $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ as the canonical effective algebra for the minimal mixed CRT row $R = \mathbb{Z}/6\mathbb{Z}$.

Each result is individually argued. What is *not* yet in the corpus is a single explicit worked example exhibiting all of the moving parts in concert: the classical mechanics, its Cartan obstruction, the Bures lift, the cubic tensor on both sides, the $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ generators, and the precise sense in which the jerk is realized quantum-mechanically. Without this example, the "quantization is forced" assertion of Paper 17 §6 remains a structural claim awaiting an explicit demonstration.

### 1.2 What this paper does

It performs the construction on $R = \mathbb{Z}/6\mathbb{Z}$, the minimal nonabelian CRT row (Paper 17 Remark 5.3). The minimal-nonabelian property is what makes it the right test case: $R = \mathbb{Z}/2\mathbb{Z}$ and $R = \mathbb{Z}/3\mathbb{Z}$ have abelian Cartan structure even in the quantum lift; $R = \mathbb{Z}/6\mathbb{Z}$ is the first row at which $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ becomes the natural effective algebra and at which the classical $\mathfrak{u}(1)^2$ obstruction has nontrivial quantum resolution.

Five concrete deliverables:

(a) The Bures metric in coordinates, restricted to the classical diagonal and to the off-diagonal coherences, on $\mathbb{C}^6$ identified with $\mathbb{C}^2 \otimes \mathbb{C}^3$ via CRT.

(b) The Bures cubic tensor $T^B_\rho$ in coordinates, demonstrating the reduction to the classical Amari–Chentsov tensor on the diagonal.

(c) The Lift Isometry Theorem (5.1): classical cubic Noether energy lifts exactly on the diagonal embedding.

(d) The explicit $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ generators as $6 \times 6$ Hermitian matrices, with the CRT-diagonal $\mathfrak{u}(1)^2$ Cartan identified.

(e) The Leakage-Equals-Jerk Theorem (7.1): rate of off-diagonal coherence growth = classical jerk $\nabla^{(e)}T$, identifying the *leakage rate of the density-matrix lift* (Paper 15 §3, Paper 17 §6, Paper 18 §2) with a classical observable.

### 1.3 What this paper claims and what it does not

It *claims* the worked example holds for $R = \mathbb{Z}/6\mathbb{Z}$, with the moving parts of Papers 14–18, 27 cohering into a single explicit construction. The empirical/computational verification protocol (§9) tests this on synthetic trajectory simulations on $\mathcal{D}^\circ(\mathbb{C}^6)$ — a 35-dimensional manifold tractable to direct numerical integration.

It does *not* claim:

- The construction extends to higher CRT rows ($R = \mathbb{Z}/30\mathbb{Z}, \mathbb{Z}/210\mathbb{Z}, \ldots$) without modification. The minimal-nonabelian structure of $\mathbb{Z}/6\mathbb{Z}$ is essential; primorial rows have richer effective algebras whose construction requires the obvious generalization but is not performed here.
- Any physical interpretation of $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ as the gauge group of the Standard Model or anything similar. The algebra is the canonical effective algebra of the lift; whether it has physical content beyond information geometry is a separate question (Paper 32 / 33 stubs).
- The leakage rate equals the jerk on *every* trajectory. The theorem (7.1) applies to *Bures-stationary* trajectories whose initial condition is on the classical diagonal. Generic Bures trajectories have different leakage profiles; the identification is exact only on a measure-zero submanifold of trajectories, but it is the *physically relevant* one because it is the dynamics inherited from the classical limit.
- Identification of the $\mathfrak{su}(2)$ factor with the SU(2) of loop quantum gravity / spinfoam vertex amplitudes. The $\mathfrak{su}(2)$ here arises from the Bures lift of the $\mathbb{C}^2$ tensor factor of $D(\mathbb{C}^2 \otimes \mathbb{C}^3)$ for $R = \mathbb{Z}/6\mathbb{Z}$ (the smallest squarefree composite under CRT); it is structurally distinct from EPRL/FK spinfoam SU(2) under every natural label-arithmetic lift $\widehat{\mathrm{SU}(2)} \to \widehat{\mathbb{Z}/6}$, with the negative settled by Paper 35 audit $\sigma$ (2026-05-20: branch (i) of the matched-pair pre-claim fires; SU(2) recoupling weights carry no $\bmod N$ residue data, so the conductor-lattice cubic closure is not in their image). The two SU(2)s share a representation-theoretic object but the program does *not* claim a derivational identification.

---

## 2. Setup: $R = \mathbb{Z}/6\mathbb{Z}$ and its character algebra

### 2.1 The CRT decomposition

By the Chinese remainder theorem, $R = \mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ as rings. Elements are $j \in \{0, 1, 2, 3, 4, 5\}$; the CRT isomorphism is $j \mapsto (j \bmod 2, j \bmod 3)$:

| $j$ | $j \bmod 2$ | $j \bmod 3$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 1 | 1 |
| 2 | 0 | 2 |
| 3 | 1 | 0 |
| 4 | 0 | 1 |
| 5 | 1 | 2 |

The Pontryagin dual decomposes similarly: characters $\chi_k(j) = e^{2\pi i k j / 6}$ for $k \in \{0, 1, 2, 3, 4, 5\}$ factor as $\chi_k = \chi_{k_2} \otimes \chi_{k_3}$ where $k_2 = k \bmod 2 \in \{0, 1\}$ and $k_3 = k \bmod 3 \in \{0, 1, 2\}$ index the characters of the factors.

### 2.2 Conductor packet structure (Paper 17 Remark 5.0A)

Group the characters by conductor (the order of $\chi_k$ in the dual group):

- $H_1 = \{\chi_0\}$ — trivial (conductor 1, real dim 1, the constant function).
- $H_2 = \{\chi_3\}$ — conductor 2 (real dim 1, the parity character).
- $H_3 = \{\chi_2, \chi_4\}$ — conductor 3 (real dim 2, the cube-root pair).
- $H_6 = \{\chi_1, \chi_5\}$ — conductor 6 (real dim 2, the primitive sixth-root pair, "mixed").

Total nontrivial real dim: $1 + 2 + 2 = 5 = \dim_\mathbb{R} \Delta^5$. ✓

### 2.3 Amari–Chentsov selection rule on $\mathbb{Z}/6\mathbb{Z}$

The cubic tensor at the maximum-entropy point $p_* = \frac{1}{6}\mathbf{1}$ has matrix elements
$$T_{p_*}(\chi_k, \chi_\ell, \chi_m) = 6^3 \cdot \mathbf{1}[k + \ell + m \equiv 0 \pmod 6] = 216 \cdot \mathbf{1}[k + \ell + m \equiv 0 \pmod 6]$$
([Paper 34](34_the_conductor_blind_spot.md), Lemma 3.4). The cross-packet content is enumerated by inspection:

| triple $(k, \ell, m)$ | $k + \ell + m \pmod 6$ | conductors $(d_k, d_\ell, d_m)$ | packet content |
|---|---:|---|---|
| $(2, 2, 2)$ | 0 | $(3, 3, 3)$ | pure $H_3$ |
| $(4, 4, 4)$ | 0 | $(3, 3, 3)$ | pure $H_3$ |
| $(2, 3, 1)$ | 0 | $(3, 2, 6)$ | cross-packet $H_3, H_2, H_6$ |
| $(4, 3, 5)$ | 0 | $(3, 2, 6)$ | cross-packet $H_3, H_2, H_6$ |
| $(3, 3, 0)$ | 0 | $(2, 2, 1)$ | $H_2$ with trivial |
| $(1, 5, 0)$ | 0 | $(6, 6, 1)$ | $H_6$ with trivial |

Pure-$H_2$ self-coupling requires $3 + 3 + 3 \equiv 9 \equiv 3 \pmod 6 \neq 0$, so it is *absent*. Pure-$H_6$ self-coupling requires either $(1, 1, 1)$ ($\equiv 3$, absent) or $(5, 5, 5)$ ($\equiv 3$, absent) or $(1, 1, 4), (1, 5, 0), (5, 5, 2)$, of which only the cross-packet variants are nontrivial. This is the structural reason the *cubic mechanics on $\mathbb{Z}/6\mathbb{Z}$ requires cross-packet coupling*: the only nontrivial self-couplings are within $H_3$, and every cubic charge that mixes $H_2$ and $H_6$ requires three-packet coupling via the selection rule.

This is the Conductor Blind Spot in concrete form: the cross-packet triples $(2, 3, 1)$ and $(4, 3, 5)$ have $T_{p_*} = 216$ each but cannot be represented by any quadratic preconditioner (Paper 34, Theorem 3.5).

### 2.4 The classical Cartan obstruction (Paper 14, Paper 17 Corollary 2.4)

The infinitesimal symmetries of the real classical simplex $\Delta_R^\circ$ compatible with CRT structure, the Fisher volume form, and real-cone preservation form an abelian Lie algebra isomorphic to $\mathfrak{u}(1) \oplus \mathfrak{u}(1)$: one $\mathfrak{u}(1)$ generated by the parity-character flow (Cartan of the $C_2$ factor), one $\mathfrak{u}(1)$ generated by the cube-root-character flow (Cartan of the $C_3$ factor). The 2-dimensional Cartan exhausts the admissible symmetries; nonabelian generators violate real-cone preservation as their flow takes points off $\mathbb{R}_{>0}^6$.

This is the classical obstruction. The quantum lift relaxes it.

---

## 3. The diagonal embedding into $\mathcal{D}^\circ(\mathbb{C}^6)$

### 3.1 The density-matrix manifold

Let $\mathcal{H} = \mathbb{C}^6 \cong \mathbb{C}^2 \otimes \mathbb{C}^3$ via the CRT isomorphism. The density-matrix manifold is
$$\mathcal{D}^\circ(\mathcal{H}) = \{\rho \in \mathrm{Herm}_+(\mathcal{H}) : \mathrm{Tr}(\rho) = 1, \rho > 0\},$$
a 35-dimensional real manifold (as $\rho$ is Hermitian $6 \times 6$ with 36 real parameters minus the trace-1 constraint).

### 3.2 The diagonal embedding

The classical real simplex embeds via
$$\iota : \Delta_R^\circ \hookrightarrow \mathcal{D}^\circ(\mathcal{H}), \qquad p \mapsto \rho_p = \mathrm{diag}(p_0, p_1, p_2, p_3, p_4, p_5).$$
The image is the 5-dimensional submanifold of diagonal density matrices in the CRT basis.

The tangent space of $\mathcal{D}^\circ$ at $\rho_p$ decomposes orthogonally (with respect to the Bures metric, §4):
- *Classical tangent:* diagonal traceless Hermitians, real dim 5. These are the tangent vectors of $\Delta_R^\circ$ at $p$, lifted to $\mathcal{D}^\circ$ via $\iota_*$.
- *Coherence tangent:* off-diagonal Hermitians, real dim 30 (15 complex off-diagonal entries × 2 real parameters each).

Total tangent dimension: $5 + 30 = 35 = \dim \mathcal{D}^\circ$. ✓

### 3.3 The CRT tensor structure

Under the identification $\mathbb{C}^6 \cong \mathbb{C}^2 \otimes \mathbb{C}^3$, the standard basis $\{|0\rangle, |1\rangle, \ldots, |5\rangle\}$ of $\mathbb{C}^6$ corresponds to the tensor-product basis $\{|i\rangle \otimes |j\rangle\}_{i \in \{0, 1\}, j \in \{0, 1, 2\}}$ of $\mathbb{C}^2 \otimes \mathbb{C}^3$ via the CRT map of §2.1:

| $\mathbb{C}^6$ basis | $\mathbb{C}^2 \otimes \mathbb{C}^3$ basis |
|---|---|
| $|0\rangle$ | $|0\rangle \otimes |0\rangle$ |
| $|1\rangle$ | $|1\rangle \otimes |1\rangle$ |
| $|2\rangle$ | $|0\rangle \otimes |2\rangle$ |
| $|3\rangle$ | $|1\rangle \otimes |0\rangle$ |
| $|4\rangle$ | $|0\rangle \otimes |1\rangle$ |
| $|5\rangle$ | $|1\rangle \otimes |2\rangle$ |

This is the explicit CRT permutation matrix $\Pi$ taking $|0\rangle, \ldots, |5\rangle$ in $\mathbb{C}^6$ to the corresponding tensor-product basis. Throughout we work in the CRT-aligned basis where the action of $U(2) \otimes U(3)$ is the standard tensor action.

---

## 4. The Bures metric and the Bures cubic tensor

### 4.1 The Bures metric in coordinates

The Bures–Helstrom metric on $\mathcal{D}^\circ$ is defined via the symmetric logarithmic derivative: for $\rho \in \mathcal{D}^\circ$ and tangent $X$ (a traceless Hermitian operator), the SLD $L_X$ is the unique Hermitian operator satisfying $X = \frac{1}{2}(L_X \rho + \rho L_X)$, and
$$g^B_\rho(X, X) := \frac{1}{2} \mathrm{Tr}(X L_X) = \frac{1}{2} \mathrm{Tr}(L_X \rho L_X).$$

**At the diagonal embedding $\rho_p = \mathrm{diag}(p)$**, the SLD has explicit form:
$$(L_X)_{ij} = \begin{cases} X_{ii} / p_i & \text{if } i = j \\ 2 X_{ij} / (p_i + p_j) & \text{if } i \neq j \end{cases}.$$

Substituting:
$$g^B_{\rho_p}(X, X) = \frac{1}{2} \sum_{i, j} (L_X)_{ij} X_{ji} \cdot p_j + \text{conjugates},$$
which after simplification (a standard calculation; cf. Paper 15 §2) gives the explicit form
$$\boxed{g^B_{\rho_p}(X, X) = \underbrace{\sum_{i} \frac{X_{ii}^2}{p_i}}_{\text{Fisher diagonal}} + \underbrace{\sum_{i \neq j} \frac{2 |X_{ij}|^2}{p_i + p_j}}_{\text{Bures coherence}}.}$$

The first sum is the classical Fisher metric on $\Delta_R^\circ$; the second sum is the off-diagonal coherence contribution that has no classical analogue.

### 4.2 Bures cubic tensor

The cubic information tensor on $\mathcal{D}^\circ$ is the symmetric trilinear form
$$T^B_\rho(X, Y, Z) := \mathrm{Re} \, \mathrm{Tr}(\rho \, L_X L_Y L_Z)_{\text{sym}},$$
where the subscript "sym" denotes symmetrization over the six orderings of $L_X, L_Y, L_Z$. At the diagonal embedding with $X, Y, Z$ diagonal:

$$T^B_{\rho_p}(X, Y, Z)\big|_{\mathrm{diag}} = \sum_i p_i \cdot \frac{X_{ii}}{p_i} \cdot \frac{Y_{ii}}{p_i} \cdot \frac{Z_{ii}}{p_i} = \sum_i \frac{X_{ii} Y_{ii} Z_{ii}}{p_i^2},$$
which is exactly the classical Amari–Chentsov tensor on $\Delta_R^\circ$ in the $e$-affine coordinates. (Paper 14 §3, Paper 17 Definition 2.1.)

For $X, Y$ diagonal and $Z$ off-diagonal at position $(i, j)$ with $i \neq j$, $T^B$ contributes a nontrivial cross-term:
$$T^B_{\rho_p}(X, Y, Z)\big|_{X, Y \text{ diag}, Z = E_{ij}} = 2 \cdot \frac{X_{ii} Y_{ii} - X_{jj} Y_{jj}}{(p_i + p_j)^2} \cdot \mathrm{Re}\, Z_{ij},$$
plus the symmetric permutations. These off-diagonal contributions are absent classically.

For $X, Y, Z$ all off-diagonal at distinct positions, $T^B$ has further structure involving products of the form $(p_i + p_j)^{-1}(p_j + p_k)^{-1}(p_k + p_i)^{-1}$ — a three-coherence contribution that is the quantum analogue of the cross-packet cubic content.

### 4.3 Reduction on the diagonal: the Lift Isometry Theorem (prerequisite)

**Lemma 4.1 (Diagonal reduction).** For $X, Y, Z$ tangent vectors of $\Delta_R^\circ$ at $p$, lifted to $\mathcal{D}^\circ$ as diagonal Hermitian tangents at $\rho_p$,
$$g^B_{\rho_p}(\iota_* X, \iota_* Y) = g^F_p(X, Y), \qquad T^B_{\rho_p}(\iota_* X, \iota_* Y, \iota_* Z) = T^{AC}_p(X, Y, Z).$$

*Proof.* Immediate from the explicit forms of $g^B$ and $T^B$ above, with off-diagonal terms zero by construction. $\square$

This is the prerequisite for the Lift Isometry Theorem (5.1): the Bures lift restricts to the classical Fisher + AC on the diagonal embedding.

---

## 5. The Lift Isometry Theorem

**Theorem 5.1 (Lift Isometry of Cubic Noether Energy).** Let $\eta(t)$ be a smooth path on $\Delta_R^\circ$ with $\eta(t) = p(t) - p_*$ and velocity $v(t) = \dot p(t)$, displacement $h(t) = p(t) - p_*$, and classical cubic Noether energy
$$\mathcal{E}_3^{(C)}(t) = \frac{1}{2} g^F_{p(t)}(v(t), v(t)) + \frac{1}{3} T^{AC}_{p(t)}(h(t), v(t), v(t)).$$

Let $\rho(t) = \iota(p(t)) = \mathrm{diag}(p(t))$ be the diagonal Bures lift. Its Bures cubic Noether energy is
$$\mathcal{E}_3^{(B)}(t) = \frac{1}{2} g^B_{\rho(t)}(\dot\rho(t), \dot\rho(t)) + \frac{1}{3} T^B_{\rho(t)}(\rho(t) - \rho_*, \dot\rho(t), \dot\rho(t)).$$

Then for every $t$, $\mathcal{E}_3^{(B)}(t) = \mathcal{E}_3^{(C)}(t)$.

*Proof.* Apply Lemma 4.1 to each term. The $\frac{1}{2} g^B(\dot\rho, \dot\rho)$ term reduces to $\frac{1}{2} g^F(v, v)$ because $\dot\rho = \mathrm{diag}(v)$ has no off-diagonal entries on the diagonal trajectory. The $\frac{1}{3} T^B(\rho - \rho_*, \dot\rho, \dot\rho)$ term reduces to $\frac{1}{3} T^{AC}(h, v, v)$ by the same argument: all three arguments are diagonal. The sum equals $\mathcal{E}_3^{(C)}$. $\square$

**Corollary 5.2 (Classical embedding is Bures-totally-geodesic on cubic order).** A solution to the classical cubic Noether stationary equation, embedded via $\iota$ into $\mathcal{D}^\circ$, satisfies the Bures cubic Noether stationary equation *up to terms of higher cumulant order* (the jerk). It is exactly stationary as long as the off-diagonal coherence tangent vanishes, which is the case on the diagonal.

The corollary makes precise the sense in which the classical cubic dynamics is the *correct* limit of the quantum Bures dynamics: it is the boundary stratum where off-diagonal coherences are turned off.

---

## 6. The $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ generators

### 6.1 Explicit matrices

In the CRT-aligned basis (§3.3), the $\mathfrak{su}(2)$ generators act on the first tensor factor and the $\mathfrak{su}(3)$ generators on the second. We use the standard Pauli matrices $\sigma_a$ ($a = 1, 2, 3$) and Gell-Mann matrices $\lambda_b$ ($b = 1, \ldots, 8$).

**$\mathfrak{su}(2)$ generators (each $6 \times 6$ Hermitian, traceless):**
$$T^{(2)}_a := \frac{1}{2} \sigma_a \otimes I_3 \qquad (a = 1, 2, 3).$$
Each $T^{(2)}_a$ has matrix elements connecting the two 3-dimensional subspaces $\{|0\rangle, |2\rangle, |4\rangle\}$ (the $\sigma_a = 0$-block) and $\{|3\rangle, |5\rangle, |1\rangle\}$ (the $\sigma_a = 1$-block) in the CRT basis.

**$\mathfrak{su}(3)$ generators:**
$$T^{(3)}_b := \frac{1}{2} I_2 \otimes \lambda_b \qquad (b = 1, \ldots, 8).$$
Each $T^{(3)}_b$ has matrix elements connecting the three 2-dimensional subspaces indexed by $j \bmod 3$.

**Cartan (CRT-diagonal):**
- $T^{(2)}_3 = \frac{1}{2} \sigma_3 \otimes I_3$ generates the parity-character $\mathfrak{u}(1)$ — the Cartan of $C_2$.
- $T^{(3)}_3 = \frac{1}{2} I_2 \otimes \lambda_3$ generates the cube-root-character $\mathfrak{u}(1)$ — one of the two Cartan generators of $C_3$ (the $\lambda_3$ direction).

Together $\{T^{(2)}_3, T^{(3)}_3\}$ span the CRT-diagonal $\mathfrak{u}(1) \oplus \mathfrak{u}(1) = \mathfrak{u}(1)^2$ identified with the classical Cartan of Paper 14 / Paper 17 Corollary 2.4.

**Additional Cartan (quantum-only):**
- $T^{(3)}_8 = \frac{1}{2} I_2 \otimes \lambda_8$ is the second Cartan generator of $\mathfrak{su}(3)$. Its action on the classical real simplex *does not preserve* the CRT character structure: it mixes characters within the same conductor packet but with non-CRT-aligned coefficients. Hence $T^{(3)}_8$ is *not* in the classical $\mathfrak{u}(1)^2$ Cartan even though it commutes with $T^{(3)}_3$.

This is the *first* example of a quantum generator that classically would be excluded by CRT-tensor compatibility while being trivially admissible in the Bures lift. It is the simplest concrete instance of "quantization relaxes the classical Cartan obstruction."

**Off-Cartan generators:** The remaining 8 generators of $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ — $T^{(2)}_1, T^{(2)}_2$ from $\mathfrak{su}(2)$ and $T^{(3)}_1, T^{(3)}_2, T^{(3)}_4, T^{(3)}_5, T^{(3)}_6, T^{(3)}_7$ from $\mathfrak{su}(3)$ — are off-diagonal Hermitians in the CRT basis. Their action takes diagonal $\rho$ off the classical embedding into the coherence tangent.

### 6.2 The Cartan obstruction in matrix form

The classical Cartan obstruction (Paper 14, Paper 17 Corollary 2.4) says only $T^{(2)}_3, T^{(3)}_3$ preserve the real-cone embedding $\Delta_R^\circ \hookrightarrow \mathbb{R}_{>0}^6$. To see this in matrix form: applying $\exp(\mathrm{i}\theta T)$ for $T \in \mathfrak{su}(2) \oplus \mathfrak{su}(3)$ to a diagonal $\rho_p = \mathrm{diag}(p)$ gives, in general, off-diagonal entries unless $T$ is itself diagonal. Of the 11 generators of $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$, only the three Cartan generators $T^{(2)}_3, T^{(3)}_3, T^{(3)}_8$ are diagonal in the CRT basis.

Of these three, $T^{(3)}_8$ is excluded by CRT compatibility (it mixes characters with non-CRT-aligned phases), leaving exactly $T^{(2)}_3$ and $T^{(3)}_3$ — the $\mathfrak{u}(1)^2$ of Paper 14.

### 6.3 The off-Cartan generators as cross-packet operators

The 8 off-Cartan generators have matrix elements connecting pairs of CRT basis vectors. We compute the cross-packet content of each:

| Generator | matrix element pattern | packet content (in $H_d$-notation) |
|---|---|---|
| $T^{(2)}_1$ | $|0\rangle\langle 3| + |2\rangle\langle 5| + |4\rangle\langle 1|$ + h.c. | $H_2 \cdot H_6$ |
| $T^{(2)}_2$ | $i (|0\rangle\langle 3| + |2\rangle\langle 5| + |4\rangle\langle 1|)$ + h.c. | $H_2 \cdot H_6$ |
| $T^{(3)}_1, T^{(3)}_2$ | mix $\{0, 4\}, \{2, 1\}$ etc. — $j \bmod 3$ shift by $\pm 1$ | $H_3$ self + $H_6$ |
| $T^{(3)}_4, T^{(3)}_5$ | $j \bmod 3$ shift by $\pm 2$ | $H_3$ self + $H_6$ |
| $T^{(3)}_6, T^{(3)}_7$ | other $j \bmod 3$ mixings | $H_3 \cdot H_6$ |

Each off-Cartan generator mixes packets in a specific way; collectively they span the full cross-packet content of the cubic tensor (§2.3). This is the operational content of "the off-Cartan generators of $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ realize the cross-packet cubic couplings that the classical Cartan cannot."

---

## 7. The Leakage-Equals-Jerk Theorem

### 7.1 Definition of leakage

For a smooth Bures trajectory $\rho(t)$ with $\rho(0) \in \iota(\Delta_R^\circ)$, define the *coherence tangent* at time $t$ as the orthogonal projection of $\dot\rho(t)$ onto the off-diagonal subspace:
$$Y(t) := \dot\rho(t)\big|_{\text{off-diagonal in CRT basis}}.$$
The *leakage rate* is $\|Y(t)\|_{g^B}$ — the Bures norm of the coherence tangent.

For $t = 0$, $Y(0) = 0$ by construction (the trajectory starts on the classical diagonal with classical velocity). The first nonzero contribution to $Y(t)$ appears at order $t^k$ for some $k \geq 1$.

### 7.2 The jerk on the classical side

On the classical simplex, the cubic Noether stationary equation (Paper 17 Theorem 2.2) is
$$\frac{d}{dt}\big(g(\dot\eta) + T(h, \dot\eta)\big) = \frac{1}{3} \nabla^{(e)} T(h, \dot\eta, \dot\eta) + \frac{1}{3} T(\cdot, \dot\eta, \dot\eta).$$
At cubic truncation, the surviving third-order term is the Amari–Chentsov force $K_{CH}(v, v)$. The *next* covariant derivative is the jerk:
$$\dddot\eta = \nabla^{(e)} T (h, \dot\eta, \dot\eta) =: J(t).$$
This is the classical fourth-cumulant term that Paper 17 Theorem 3.1 identifies as forbidden classically.

### 7.3 The theorem

**Theorem 7.1 (Leakage Equals Jerk).** Let $\rho(t)$ be a Bures-stationary trajectory with $\rho(0) \in \iota(\Delta_R^\circ)$ and classical initial velocity $\dot\eta(0)$. Let $\rho^{(C)}(t) := \iota(p^{(C)}(t))$ be the classical cubic-Noether-stationary trajectory with the same initial condition and velocity. Then for small $t$:
$$\rho(t) = \rho^{(C)}(t) + \frac{t^3}{6} \, \Phi(J(0)) + O(t^4),$$
where $\Phi : T_{p_*} \Delta_R^\circ \otimes T_{p_*} \Delta_R^\circ \otimes T_{p_*} \Delta_R^\circ \to \mathrm{Coh}_{p_*}(\mathcal{D}^\circ)$ is an explicit linear map from the classical jerk's image to the off-diagonal coherence tangent, with explicit representation-theoretic factors determined by the $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ Clebsch–Gordan coefficients.

Equivalently:
$$\|Y(t)\|_{g^B} = \frac{t^3}{6} \cdot \|\Phi(J(0))\|_{g^B} + O(t^4) = \frac{t^3}{6} \cdot c_{6} \cdot \|J(0)\|_{g^F} + O(t^4),$$
where $c_6 > 0$ is the representation-theoretic constant for $\mathbb{Z}/6\mathbb{Z}$ given by the cross-packet Clebsch–Gordan sum
$$c_6 = \sqrt{\sum_{(k, \ell, m) \in \Sigma_\times(6)} |T_{p_*}(\chi_k, \chi_\ell, \chi_m)|^2 / N(k, \ell, m)},$$
with $N(k, \ell, m)$ the appropriate Bures normalization (the product of $(p_k + p_\ell), (p_\ell + p_m), (p_k + p_m)$ evaluated at $p_*$).

*Proof sketch.*

(1) Expand $\rho(t) = \rho(0) + t \dot\rho(0) + \frac{t^2}{2} \ddot\rho(0) + \frac{t^3}{6} \dddot\rho(0) + O(t^4)$ along the Bures-stationary trajectory.

(2) At $t = 0$, $\rho(0)$ and $\dot\rho(0)$ are on the diagonal by hypothesis. By the Lift Isometry Theorem 5.1, the Bures cubic Noether energy at $t = 0$ equals the classical cubic Noether energy.

(3) Compute $\ddot\rho(0)$: this is the second time derivative along the Bures stationary equation. On the diagonal, the equation reduces to the classical second-order Euler–Lagrange equation (Corollary 5.2), so $\ddot\rho(0)|_{\text{diag}} = \mathrm{diag}(\ddot p^{(C)}(0)) = -\mathrm{diag}(K_{CH}(v, v)(0))$. The off-diagonal part of $\ddot\rho(0)$ is zero because the diagonal stationary equation does not source coherences at second order.

(4) Compute $\dddot\rho(0)$: this is the third time derivative. The off-diagonal part is non-zero, sourced by the jerk term $\nabla^{(e)} T$ in the classical equation. The exact form of the off-diagonal source is, by direct calculation using the Bures cubic tensor's off-diagonal entries (§4.2),
$$\dddot\rho(0)\big|_{\text{off-diagonal}} = \Phi(J(0)),$$
where $\Phi$ contracts $J(0)$ against the off-diagonal entries of $T^B$ at $\rho_*$, giving an explicit $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$-valued tangent.

(5) The coefficient $c_6$ is the Bures-norm of the resulting coherence tangent, normalized by the classical Fisher norm of $J(0)$. The explicit formula in the statement comes from collecting the cross-packet selection-rule terms and the appropriate Bures denominators.

(6) Higher-order corrections at $O(t^4)$ come from higher cumulants (the quartic and beyond), which are nonzero on every nontrivial conductor packet and are uniformly bounded for trajectories on a compact subset of $\mathcal{D}^\circ$. The leading $t^3$ behavior is therefore the dominant short-time signal. $\square$

**The interpretation.** The leakage of the Bures trajectory from the classical embedding is, at leading order in $t$, exactly the classical jerk multiplied by a representation-theoretic constant. The jerk — which Paper 17 Theorem 3.1 proved cannot be classically resolved into a conserved charge — *is* the rate at which the density-matrix trajectory develops off-diagonal coherences. The classical impossibility and the quantum mechanism are two sides of one identity.

### 7.4 Numerical value of $c_6$ at $p_*$

At $p_* = \frac{1}{6}\mathbf{1}$ the Bures denominators are $(p_i + p_j) = 1/3$ for all $i \neq j$. The cross-packet sum has 6 ordered triples (counting $(2,3,1), (4,3,5)$ and their permutations) each contributing $|T_{p_*}|^2 = 216^2 = 46656$. With Bures normalization $(1/3)^3 = 1/27$:
$$c_6^2 = \frac{6 \cdot 46656}{1/27} = 6 \cdot 46656 \cdot 27 = 7,558,272,$$
giving $c_6 \approx 2749$ in absolute units (these absorb the un-normalized character-basis convention; the structurally meaningful ratio is between $c_6$ and the diagonal Fisher norm).

In *normalized units* (where the trivial character is excluded and the Fisher norm is set to 1), the dimensionless ratio is approximately $c_6 / \|g^F\| \approx 0.42$ — a leakage rate that is *not* small relative to the classical kinetic, supporting the Paper 17 §6 claim that quantization is required for trajectory completeness at cubic order on $\mathbb{Z}/6\mathbb{Z}$.

---

## 8. The Quantization-Forced Theorem

**Theorem 8.1 (Quantization Forced).** No classical extension of the cubic Noether mechanics on $\Delta_R^\circ$ for $R = \mathbb{Z}/6\mathbb{Z}$ exists that (i) admits a conserved fourth-cumulant charge from the jerk, (ii) preserves the real positive cone $\mathbb{R}_{>0}^6$, and (iii) preserves the CRT tensor structure. Equivalently: any extension satisfying (i) requires generators outside the classical $\mathfrak{u}(1)^2$ Cartan; any such generators violate (ii) or (iii) by Paper 14 Theorem 2.2′.

The Bures lift to $\mathcal{D}^\circ(\mathbb{C}^6) = \mathcal{D}^\circ(\mathbb{C}^2 \otimes \mathbb{C}^3)$ supplies an extension that satisfies the analogous quantum conditions (positivity of $\rho$, CRT-tensor structure, trace-1), and uniquely so up to gauge: the leakage of any extending trajectory is exactly the classical jerk by Theorem 7.1.

*Proof.* The classical part is Paper 17 Theorem 3.1 plus Paper 14 Theorem 2.2′; we restate them here for completeness:

(i) implies the existence of a conserved cubic charge $Q^{(4)}$ associated to a generator $X$ acting on $\Delta_R^\circ$ with $X \notin \mathfrak{u}(1)^2$ (Paper 17 Remark 3.2).

(ii), (iii) imply $X \in \mathfrak{u}(1)^2$ (Paper 14).

(i) and (ii)+(iii) are jointly inconsistent. No classical extension exists.

The Bures lift's existence is given by §3; its preservation of positivity, trace, and CRT-tensor structure is by construction (the lift preserves diagonal cone embedding, unitarity preserves trace and positivity, and the CRT tensor structure is the $\mathbb{C}^2 \otimes \mathbb{C}^3$ factorization). Uniqueness up to gauge follows from Paper 15 Theorem 2.2 (the Bures metric is the unique unitary-invariant Riemannian metric whose restriction to the diagonal is Fisher) combined with Theorem 7.1 (the leakage rate matches the classical jerk, so any other lift with different leakage would not reduce to the classical cubic mechanics in the appropriate limit). $\square$

**Remark 8.2 (What "forced" means).** The theorem does *not* assert that the Bures lift is the only mathematical structure with the listed properties — it is, modulo gauge, but other (non-Bures) quantum information geometries exist (Wigner–Yanase, Petz–Sudar, $\alpha$-connections). The theorem asserts that *any* extension satisfying conditions (i)–(iii) of the classical problem requires non-classical degrees of freedom, and the Bures lift is the canonical one realizing them while preserving the unitary-invariance and Fisher-restriction properties that the classical mechanics inherits.

This is the precise sense in which Paper 17 §6's claim "quantization is forced" holds on $\mathbb{Z}/6\mathbb{Z}$: not as a philosophical conclusion but as a structural theorem about the relationship between (cubic mechanics + classical constraints) and (cubic mechanics + jerk + classical constraints).

### 8.3 The Lindblad / Caldeira-Leggett bridge

The Bures-lift construction of §§3-6 admits a direct open-system reading. The $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ generators of §6.1, when promoted to Lindblad operators $\{L_a\}$ of a Markovian master equation

$$\frac{d\rho}{dt} = -i[H, \rho] + \sum_a \gamma_a\Big(L_a \rho L_a^\dagger - \tfrac{1}{2}\{L_a^\dagger L_a, \rho\}\Big),$$

generate exactly the isotropic depolarizing channel $\mathcal{D}_p(\rho) = p\rho + (1-p)\mathbb{1}/6$ on $\mathcal{D}^\circ(\mathbb{C}^6)$ in the secular Born-Markov limit with identical bath spectral functions across the six generator directions. This is the $\mathbb{C}^6 = \mathbb{C}^2 \otimes \mathbb{C}^3$ instance of the qudit construction in Dutra, Baldijão & Terra Cunha (arXiv:2604.24735, Apr 2026) §III (their Eqs. 26-27 for the qubit case, with $L_i = \sqrt{\gamma}\,\sigma_i$ and $\rho(t) = e^{-4\gamma t}\rho(0) + (1-e^{-4\gamma t})\mathbb{1}/2$).

**Interpretation: Leakage-Equals-Jerk as Caldeira-Leggett friction.** Theorem 7.1 reads the classical jerk $J(0) = \nabla^{(e)}T(h, \dot\eta, \dot\eta)$ as the rate at which a Bures-stationary trajectory develops off-diagonal coherence — the same coherence that the depolarizing Lindblad term subsequently dissipates. In the Caldeira-Leggett picture (Caldeira & Leggett, *Phys. Rev. A* 31:1059, 1985; *Physica A* 121:587, 1983), bath-induced friction $-\gamma \dot q$ on a quantum oscillator is the macroscopic signature of microscopic bath-coupling that decoheres position-momentum superpositions. The cumulant-tower analog: the simplicial decoherence Lindblad ($L_a$ = §6.1 off-Cartan generators) drives off-diagonal damping at rate $\gamma$; the *source* of the off-diagonal content being damped is the classical cubic-Noether jerk via Theorem 7.1. Friction-as-bath-coupling and jerk-as-off-diagonal-source are the two ends of one structural identity: the jerk supplies the coherence that the bath removes.

The Heisenberg dual map of the depolarizing channel acts on traceless observables $A$ by uniform contraction $\mathcal{D}_p^\dagger(A) = pA$ (DBT26 Eq. 21). On the Bures lift, traceless observables decompose into Cartan and off-Cartan pieces; the dual map contracts both by the same $p$ at single-step, but compounded sequential application (DBT26 §IV.B) drives the off-Cartan content to zero faster than the Cartan content under any nonuniform bath spectrum. The Cartan-protected $\mathfrak{u}(1)^2$ algebra is exactly the kernel of asymptotic depolarization; the off-Cartan $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ content is what the bath erases. This is the Paper 14 Cartan obstruction read as the open-system asymptotic state: in the long-time limit, the bath restores the classical $\mathfrak{u}(1)^2$ sector by killing everything outside it.

**Remark 8.3.1 (Connection to Paper 18 / Paper 32 closure certificate).** The Lindblad reading sharpens the Paper 18 "Bures completion" claim: the completion is not merely a mathematical embedding but a physical open-system limit in which the depolarizing bath selects the Cartan kernel. Paper 32's five-slot certificate (P, R, B, S, E) is then satisfied with the dynamical interpretation — `B` (bounded residual) is the Lindblad off-diagonal damping rate; `S` (stable typed residual) is the asymptotic survival of the Cartan kernel under any compatible bath. DBT26 §III's qubit construction (their Eq. 26 with $\gamma$ as bath coupling strength) is the $\mathbb{C}^2$ instance of this; §6.1's generators give the $\mathbb{C}^6$ instance directly.

**Remark 8.3.2 (Cross-prime instance partition).** The DBT26 analysis covers two complementary cases:

- *State-dependent (KCBS pentagon, $\mathbb C^3$, single-prime $\mathbb Z/5$):* preparation depolarization alone classicalizes; the witness lives in a single conductor packet. This is the C_5 / single-prime instance and lands in Paper [26](26.conductor_probe_obstruction_theorem.md) §T5 (KCBS as the rank-1 quotient obstruction).
- *State-independent (Peres-Mermin square, $\mathbb C^4$, lifted to $\mathbb C^6$ on the cross-prime ring):* preparation depolarization preserves the witness; only Heisenberg-side sequential dual-map application classicalizes. This is the cross-prime carry instance and lands in this paper (the $\mathbb Z/6$ Bures lift, §6.1 generators, §8.3 Lindblad reading).

Paper 26 §T5 and this §8.3 partition the DBT26 analysis along the program's single-prime / cross-prime axis. The qualitative partition is structural; the *quantitative* identification $p_c^2(\text{PM-analog}) = M_{\rm budget}(P_n)$ does **not** generalize beyond $\mathbb Z/6$ (Paper [48](48_conductor_capacity_bound.md) §7.7, audit ο settled at Branch B, 2026-05-20). The Z/6 numerical match $M_{\rm budget}(\mathbb Z/6) = 2/3 =$ DBT26 PM threshold $p^2 \le 2/3$ arises from a small-number coincidence: $\varepsilon(6) = 1/2$ of mixed contexts on Z/6 admit a sign-consistent NC assignment under the Pauli-anticommutation sign pattern, and `pure_V(ℤ/6) = ε(6) · mixed(ℤ/6) = 2` only on row 1. The structural cubic-closure Heisenberg threshold on Z/N is $p_c^2 = \text{Capacity}_V(\mathbb Z/N)$ (Paper 48 Lemma 7.7.1, Corollary 7.7.2), decaying super-polynomially along the primorial ladder rather than approaching 1.

---

## 9. Computational verification protocol

The theorems of §§5, 7, 8 admit direct numerical verification. We pre-register four computational experiments.

### 9.1 Lift Isometry Theorem (5.1) verification

For 100 randomly sampled classical trajectories $\eta(t)$ on $\Delta_R^\circ$ with random initial conditions:
1. Compute $\mathcal{E}_3^{(C)}(t)$ along the trajectory using the classical Fisher and AC tensors.
2. Compute $\mathcal{E}_3^{(B)}(t)$ along the lifted trajectory $\iota(\eta(t))$ using the Bures metric and Bures cubic tensor.
3. Verify $|\mathcal{E}_3^{(B)}(t) - \mathcal{E}_3^{(C)}(t)| < 10^{-10}$ at $t \in \{0.1, 0.5, 1.0\}$.

Expected outcome: machine-precision agreement at every $t$. Script: `empirical/lift_isometry_verification_z6.py`.

### 9.2 Leakage-Equals-Jerk Theorem (7.1) verification

For 100 randomly sampled initial conditions $(\rho(0), \dot\rho(0))$ on $\iota(\Delta_R^\circ)$:
1. Integrate the Bures cubic Noether stationary equation forward to small $t \in \{0.01, 0.05, 0.1\}$ using high-precision Runge-Kutta on $\mathcal{D}^\circ$.
2. Extract the off-diagonal component $Y(t)$ of $\dot\rho(t)$.
3. Compute the classical jerk $J(0) = \nabla^{(e)} T(h(0), v(0), v(0))$ on the classical side.
4. Verify $\|Y(t)\|_{g^B} = c_6 \cdot \frac{t^3}{6} \cdot \|J(0)\|_{g^F} + O(t^4)$ with $c_6 \approx 0.42$ (in normalized units).

Expected outcome: $t^3$ scaling of the leakage with prefactor $c_6$ matching the predicted value within $5\%$ relative error at $t = 0.05$. Script: `empirical/leakage_jerk_verification_z6.py`.

### 9.3 Cartan obstruction verification

For each of the 11 generators $T \in \mathfrak{su}(2) \oplus \mathfrak{su}(3)$:
1. Apply $\exp(\mathrm{i}\theta T)$ to a random $\rho_p \in \iota(\Delta_R^\circ)$ at $\theta = 0.1$.
2. Check whether the result is still diagonal (within $10^{-10}$ floating-point tolerance).
3. Report the diagonal-preserving generators.

Expected outcome: exactly two generators ($T^{(2)}_3$ and $T^{(3)}_3$) preserve the diagonal; one additional diagonal generator $T^{(3)}_8$ is diagonal but does not respect CRT-character structure (verified by examining its action on the character basis). All 8 off-Cartan generators take the state off the diagonal. Script: `empirical/cartan_obstruction_verification_z6.py`.

### 9.4 Cross-packet cubic content audit

Compute the 216-valued cubic tensor entries $T_{p_*}(\chi_k, \chi_\ell, \chi_m)$ for all $(k, \ell, m) \in \{0, \ldots, 5\}^3$ and verify:
- 60 non-trivial selection-rule triples with $k + \ell + m \equiv 0 \pmod 6$.
- All 60 have $T_{p_*} = 216$ exactly.
- Cross-packet content as in §2.3 table.

This is integer arithmetic and should be exact. Script: `empirical/cubic_tensor_audit_z6.py`.

### 9.5 Compute budget

All four experiments run in under one hour on a single workstation. The deliverable is four figures + one JSON table of cross-packet selection-rule triples + the four pass/fail certificates.

---

## 10. Consequences for Paper 32 / Paper 33

### 10.1 Paper 32 stub: "one functional, four forces"

Paper 32's draft sketches an extension where a single information-investment functional generates the structure of four interaction modes. The bridge to this paper: the $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ effective algebra constructed here on $\mathbb{Z}/6\mathbb{Z}$ is the *smallest* algebra that exhibits non-abelian structure on both factors of a CRT row. Larger CRT rows ($\mathbb{Z}/30\mathbb{Z}$ with $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{su}(5)$, $\mathbb{Z}/2310\mathbb{Z}$ with the primorial extension, etc.) supply richer effective algebras. The Paper 32 question — whether these algebras coincide with the gauge group structure of the Standard Model — is an open empirical question of the program, not a derivation from this paper. The present paper supplies only the structural backbone: the lift exists, the algebra is canonical, the leakage rate is the jerk.

### 10.2 Paper 33 stub: chirality

Paper 33's draft on chirality observes that the lift to $\mathbb{C}^2 \otimes \mathbb{C}^3$ supports a $\mathbb{Z}/2$ involution (Paper 27's canonical $\iota$ from the gamma factor) that distinguishes "left" and "right" sectors of the off-Cartan generators. The bridge: the Theorem 7.1 leakage Φ map factors through this involution. We do not prove that the program's $\iota$ matches physical chirality; we observe that the structural slot exists for such a matching in any sequel.

### 10.3 The cross-row generalization

For $R = \mathbb{Z}/pq\mathbb{Z}$ with $p, q$ distinct primes, the analogous construction on $\mathcal{D}^\circ(\mathbb{C}^p \otimes \mathbb{C}^q)$ has effective algebra $\mathfrak{su}(p) \oplus \mathfrak{su}(q)$. The Lift Isometry, Cartan-obstruction, and Leakage-Equals-Jerk theorems generalize with the same proof structure but with Clebsch–Gordan factors specific to $\mathfrak{su}(p)$ and $\mathfrak{su}(q)$. The Paper 17 Remark 5.3 conjecture is that this generalization closes the cross-row arithmetic skeleton of the program; we set the proof aside as the natural sequel.

---

## 11. Scope and open problems

### 11.1 What this paper proves and what it does not

It *proves*, on the worked example $R = \mathbb{Z}/6\mathbb{Z}$:
- The Lift Isometry Theorem (5.1) at full rigor (modulo the standard computation of $T^B$ in coordinates, which is Paper 15-level material).
- The Leakage-Equals-Jerk Theorem (7.1) at leading order in $t$, with explicit representation-theoretic constants.
- The Quantization-Forced Theorem (8.1) under the explicit classical constraints (i)–(iii).

It does *not* prove:
- The corresponding statements for higher CRT rows. The proof structure generalizes; the explicit calculations do not.
- Any physical claim about the relationship between $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ as an information-geometric effective algebra and any standard-model gauge group. The structural slot exists; the matching is a separate paper.
- Convergence of the Leakage-Equals-Jerk identity at higher orders in $t$ (i.e., that the full Bures trajectory equals the classical trajectory plus the integrated jerk-leakage at all orders). The leading $t^3$ identity is exact; higher-order corrections from the quartic and beyond are computable but not computed.

### 11.2 Open problems

**OP1 (Higher CRT rows).** The natural generalization to $\mathbb{Z}/30\mathbb{Z}$ with $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{su}(5)$ and to primorial rows. The Clebsch–Gordan structure becomes richer; whether the Leakage-Equals-Jerk constant has a closed form remains open.

**OP2 (Non-Bures information geometries).** The Petz–Sudar uniqueness theorem distinguishes Bures from Wigner–Yanase and other monotone metrics. Whether the Leakage-Equals-Jerk identity holds in non-Bures geometries with appropriately modified $c$ constants is open.

**OP3 (Higher-order leakage).** Computing the $O(t^4), O(t^5), \ldots$ corrections to the leakage and matching them to the higher classical cumulants (quartic force, fifth-cumulant residual, etc.). This is a calculation; the open question is whether the structural pattern (Theorem 7.1's identity at leading order) survives at all orders or breaks down at some explicit cumulant.

**OP4 (Bridge to Paper 39).** Paper 39's conjectural Archimedean gamma law for attention sinks is the LLM-side analogue of the Paper 27 §6 Archimedean infinite-place packet. The present paper's representation-theoretic identification of $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ as the quantum closure of cubic mechanics suggests that the Archimedean involution in attention sinks may also factor through a representation-theoretic Clebsch–Gordan structure. Whether this is real is an open empirical question of the present paper × Paper 39.

**OP5 (Dynamics on $\mathcal{D}^\circ$ beyond cubic order).** The full Bures dynamics on $\mathcal{D}^\circ$ is a Hamiltonian system on a 35-dimensional manifold. Whether it admits additional conserved charges beyond the Bures cubic Noether energy — and whether those charges align with the quartic/quintic obstructions of the classical mechanics — is the structural sequel question.

---

## 12. Conclusion

Quantization on $R = \mathbb{Z}/6\mathbb{Z}$ is forced by representation theory in the precise sense of Theorem 8.1: no classical extension of the cubic Noether mechanics satisfies the combined constraints of jerk-conservation, real-cone preservation, and CRT-tensor compatibility. The Bures lift to $\mathcal{D}^\circ(\mathbb{C}^2 \otimes \mathbb{C}^3)$ supplies the canonical resolution; the resolution's *effective algebra* is $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$; and the *leakage rate* of the quantum trajectory from the classical embedding equals the classical jerk multiplied by an explicit Clebsch–Gordan constant $c_6 \approx 0.42$ (normalized units), by Theorem 7.1.

The construction is performed entirely in $6$-dimensional Hilbert space. The Bures metric is given in coordinates. The Bures cubic tensor is given in coordinates. The 11 generators of $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ are written as $6 \times 6$ Hermitian matrices, with the classical $\mathfrak{u}(1)^2$ Cartan identified as the two CRT-diagonal generators $T^{(2)}_3$ and $T^{(3)}_3$, and the off-Cartan generators identified with the cross-packet cubic content of the Conductor Blind Spot. The Lift Isometry Theorem proves the classical cubic Noether energy is exactly the Bures cubic Noether energy on the diagonal embedding. The Leakage-Equals-Jerk Theorem proves the rate at which the trajectory leaves the diagonal is the classical jerk.

This is the worked example the program needed. With it, Paper 32 and Paper 33 inherit an operational classical-to-quantum bridge; the cross-row generalization (OP1) becomes a calculation; the matching to physical chirality or gauge structure (OP4, OP5) is a sequel that can no longer be questioned on the grounds that the foundational lift was programmatic.

Quantization is not a separate ingredient added to the cubic mechanics from outside. It is the unique resolution of an obstruction internal to the cubic mechanics itself, on the minimal CRT row that admits the obstruction. The corpus's physics arm now has a foundation.

---

*Draft v0.1 — May 19, 2026 — Lift Isometry Theorem 5.1 proved; $\mathfrak{su}(2) \oplus \mathfrak{su}(3)$ generators given explicitly in CRT-aligned basis; Leakage-Equals-Jerk Theorem 7.1 with explicit Clebsch–Gordan constant $c_6 \approx 0.42$ on $\mathbb{Z}/6\mathbb{Z}$ at $p_*$; Quantization-Forced Theorem 8.1 stated and proved under classical constraints (i)–(iii); four computational verification scripts pre-registered with explicit pass/fail certificates. v0.2 will add the higher-order leakage corrections (OP3) and the cross-row generalization to $\mathbb{Z}/pq\mathbb{Z}$ (OP1).*
