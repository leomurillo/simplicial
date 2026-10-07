# \heb{ל}23 — CRT Tensor Factorization: Cross-Prime Interaction as Entanglement in the Computational Basis

**Leonardo Murillo Montero — leonardo.murillo@gmail.com**

*Preprint, version 0.1 (scoping draft) — May 28, 2026*

*DOI to be assigned upon deposit.*

---

> *Coprimality is a tensor product. Interaction is entanglement seen in one frame.*

---

## Abstract

**Situation.** [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4 develops the *cross-prime interaction* stratum of the additive apex: for $N=\prod_i p_i^{a_i}$ the Chinese Remainder Theorem (CRT) splits $\mathbb Z/N$ over prime axes, the centered log-ledger acquires a canonical ANOVA / Möbius decomposition $y=\sum_A y_A$, and the Fourier–Mellin generator $\mathcal M_x$ Euler-factorizes across the axes iff the mixed strata $y_A$ ($|A|\ge 2$) vanish — equivalently iff the cross-prime *higher-order interaction information* (Han 1980, McGill 1954, Yeung 1991) vanishes ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorems 4.4, 4.5, 4.7). Separately, [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1 conjectures (Conjecture 7.1) an *entanglement monotone from the apex* on tensor products $\mathbb C^N\otimes\mathbb C^M$, defined as the obstruction-norm of $\mathcal M_z$ to the product-state factorization $\mathcal M_{u\otimes v}=\mathcal M_u\cdot\mathcal M_v$.

**Gap.** These two constructions are the same object viewed from two frames, and neither paper says so. This note establishes the identification, marks its exact domain, and isolates the precise surplus that genuine entanglement carries beyond it.

**Action.** We prove: (1) for coprime $N=N_1N_2$ the CRT ring isomorphism $\mathbb Z/N\cong\mathbb Z/N_1\times\mathbb Z/N_2$ is, at the level of complex amplitudes, a canonical unitary $\mathbb C^N\cong\mathbb C^{N_1}\otimes\mathbb C^{N_2}$ that intertwines the character bases and the two apex generators; (2) on the open torus $\Omega=(\mathbb C^\times)^{N_1N_2}$ a pure state is a product state $u\otimes v$ **iff** its centered complex log-ledger is separable across the prime axes, so the [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1 product-state factorization formula **is** [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 4.4 under the CRT–tensor dictionary; (3) the signed cross-prime interaction information is exactly the classical, fixed-computational-basis shadow of entanglement entropy, equal to it on the Schmidt frame and only there.

**Result.** *Cross-prime interaction information $=$ entanglement in the CRT basis.* The equivalence "$E_{\mathrm{apex}}(z)=0\iff z$ unentangled" is **exact** for pure states on $\Omega$ in the computational basis. The level sets, however, differ: interaction information and $E_{\mathrm{apex}}$ are **not** local-unitary invariants, whereas entanglement entropy is. The discrepancy is precisely the local-unitary orbit — the basis-independence that classical interaction information cannot see. Entanglement entropy equals the bipartite interaction information evaluated in the *Schmidt* basis.

**Harvest.** The "entanglement monotone from the apex" of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) Conjecture 7.1 is, in its computational-basis half, already a theorem — it is [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4 relabelled. What remains genuinely conjectural is exactly the local-unitary completion: passing from a frame-tethered functional with the right zero set to a frame-free monotone with the right level sets. We sharpen Conjecture 7.1 accordingly (§5).

**Keywords:** Chinese Remainder Theorem, tensor product, entanglement entropy, Schmidt decomposition, interaction information, ANOVA / Möbius decomposition, mutual information, local unitary invariance, computational basis, categorical-simplex apex.

---

## Cross-references from prior papers

| Cited result | Used for |
|---|---|
| [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4.3 Proposition 4.3 (domain CRT factorization) | Linear-algebra lift to the tensor isomorphism, \hyperlink{stmt:1-1}{Proposition~1.1} |
| [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4.3 Theorem 4.4 (separability $\Leftrightarrow$ Euler factorization) | Identified with the product-state factorization, \hyperlink{stmt:2-2}{Theorem~2.2} |
| [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4.4 Theorem 4.5 / §4.4 Theorem 4.7 (ANOVA; cumulant separability; interaction information) | Signed shadow of entanglement entropy, \hyperref[sec:3]{§3} |
| [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1 (product-state factorization; Conjecture 7.1) | Sharpened in \hyperref[sec:5]{§5}; bridged in \hyperref[sec:2]{§2} |
| [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §3.6 Proposition 3.6 (modulus–phase splitting of $\mathcal M_z$) | Complex-ledger separability on $\Omega$, \hyperlink{stmt:2-1}{Lemma~2.1} |
| [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) (character orthogonality on $\mathbb Z/N$) | Character-basis intertwining, \hyperlink{stmt:1-1}{Proposition~1.1} |

---

## Notation

We carry the notation of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) and [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442).

| Symbol | Meaning |
|---|---|
| $N=N_1N_2$ | Composite dimension; **coprime** factorization $\gcd(N_1,N_2)=1$ unless stated otherwise. |
| $s\leftrightarrow(s_1,s_2)$ | CRT label correspondence, $s_i=s\bmod N_i$. |
| $\{\lvert s\rangle\}$ | Computational (CRT) basis of $\mathbb C^N$. |
| $\chi_c$ | Additive character of $\mathbb Z/N$, $\chi_c(s)=e^{2\pi i cs/N}$. |
| $\mathcal M_z(\beta,c)$ | Apex generator, $\frac1N\sum_s e^{\beta y_s(z)}\overline{\chi_c(s)}$ ([\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) Def. 3.4). |
| $y_s(z)$ | Centered complex log-ledger, $\log z_s-\frac1N\sum_j\log z_j$. |
| $y=\sum_A y_A$ | ANOVA / Möbius decomposition over prime axes ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Thm. 4.5). |
| $\Omega$ | Nowhere-vanishing amplitudes $(\mathbb C^\times)^N$. |
| $z=u\otimes v$ | Product state, $z_{(s_1,s_2)}=u_{s_1}v_{s_2}$, $u\in\mathbb C^{N_1}$, $v\in\mathbb C^{N_2}$. |
| $\sigma_k$ | Schmidt coefficients of $z\in\mathbb C^{N_1}\otimes\mathbb C^{N_2}$. |
| $S_{\mathrm{ent}}(z)$ | Entanglement entropy $-\sum_k\sigma_k^2\log\sigma_k^2$. |
| $\mathbb I(z)$ | Cross-prime interaction information of the Born ledger (see §3). |
| $E_{\mathrm{apex}}(z)$ | $L^2$ obstruction-norm of $\mathcal M_z$ to product factorization ([\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) Conj. 7.1). |

Throughout, "computational basis," "CRT basis," and "fixed frame" are synonyms: the basis $\{\lvert s\rangle=\lvert s_1\rangle\otimes\lvert s_2\rangle\}$ in which $\mathcal M_z$ is defined.

---

## 1. The CRT = tensor-factorization correspondence {#sec:1}

[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 4.3 records CRT as a ring isomorphism of *label sets*, $\mathbb Z/N\cong\prod_i\mathbb Z/p_i^{a_i}$, dualizing to a product of character groups. We lift it one level, to the complex amplitude space carrying the apex.

\hypertarget{stmt:1-1}{}
**Proposition 1.1 (CRT is a unitary tensor factorization).** Let $N=N_1N_2$ with $\gcd(N_1,N_2)=1$, and let $\Phi:\mathbb Z/N\xrightarrow{\sim}\mathbb Z/N_1\times\mathbb Z/N_2$, $s\mapsto(s_1,s_2)$, be the CRT isomorphism. The linear map
$$U_{\mathrm{CRT}}:\mathbb C^N\longrightarrow\mathbb C^{N_1}\otimes\mathbb C^{N_2},\qquad \lvert s\rangle\longmapsto\lvert s_1\rangle\otimes\lvert s_2\rangle,$$
is a unitary isomorphism with the following compatibilities:

(a) *(Character intertwining.)* Under the dual CRT isomorphism $\widehat{\mathbb Z/N}\cong\widehat{\mathbb Z/N_1}\times\widehat{\mathbb Z/N_2}$, $c\leftrightarrow(c_1,c_2)$, the additive characters tensor-factor,
$$\chi_c(s)=\chi^{(N_1)}_{c_1}(s_1)\,\chi^{(N_2)}_{c_2}(s_2),\qquad U_{\mathrm{CRT}}\,\chi_c=\chi^{(N_1)}_{c_1}\otimes\chi^{(N_2)}_{c_2}.$$

(b) *(Apex-index factorization of the domain.)* The index space $(\beta,c)\in\mathbb C\times\widehat{\mathbb Z/N}$ of $\mathcal M_z$ factors as $(\beta,c_1,c_2)\in\mathbb C\times\widehat{\mathbb Z/N_1}\times\widehat{\mathbb Z/N_2}$, with the **single** Mellin variable $\beta$ shared (it is dual to global scale, not to a prime axis).

(c) *(Born compatibility.)* $U_{\mathrm{CRT}}$ is a permutation of computational-basis vectors, hence preserves all moduli; the Born map and the dephasing channel commute with $U_{\mathrm{CRT}}$.

**Proof.** $\Phi$ is a bijection of index sets, so $U_{\mathrm{CRT}}$ maps an orthonormal basis to an orthonormal basis and is unitary. (a) is the dual statement of the ring isomorphism: $\chi_c(s)=e^{2\pi i cs/N}$ and, writing $c$ and $s$ through CRT, $cs/N\equiv c_1s_1/N_1+c_2s_2/N_2\pmod 1$ by coprimality (this is exactly [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Proposition 4.3 dualized). (b) is immediate from $\widehat{G\times H}\cong\widehat G\times\widehat H$; the Mellin variable $\beta$ couples to the centered log-ledger $y$, which is a function on the *single* group and is not split by CRT. (c) holds since $U_{\mathrm{CRT}}\lvert s\rangle=\lvert s_1\rangle\otimes\lvert s_2\rangle$ permutes basis kets. $\square$

\hypertarget{stmt:1-2}{}
**Remark 1.2 (Where coprimality is load-bearing — the domain mark).** As *vector spaces*, $\mathbb C^{N_1N_2}\cong\mathbb C^{N_1}\otimes\mathbb C^{N_2}$ for **any** $N_1,N_2$ (both have dimension $N_1N_2$). What requires $\gcd(N_1,N_2)=1$ is the *canonical labelling* of that tensor product by a single cyclic group $\mathbb Z/N$ via CRT, and hence the intertwining (a)–(b) of the **arithmetic** structure (characters, conductor index, apex generator). This is the precise hinge between the two papers:

- **[\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) reading (two-particle).** The tensor product $\mathbb C^{N_1}\otimes\mathbb C^{N_2}$ with labels $(s_1,s_2)\in\mathbb Z/N_1\times\mathbb Z/N_2$ and bi-conductor $(c_1,c_2)$ is intrinsic and well-defined for *all* $N_1,N_2$. It is "two particles."
- **[\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) reading (single composite $N$).** A single $\mathbb Z/N$ apex with one conductor index $c\in\widehat{\mathbb Z/N}$, split into prime axes.

These two readings **coincide** — the single-$N$ apex *is* the two-particle apex — **iff** $\gcd(N_1,N_2)=1$, since only then is $\widehat{\mathbb Z/N}\cong\widehat{\mathbb Z/N_1}\times\widehat{\mathbb Z/N_2}$. For $\gcd(N_1,N_2)=d>1$, the two-particle apex of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) still exists but is **not** a CRT factorization of any single $\mathbb Z/N$ apex: there is no $c\in\widehat{\mathbb Z/N}$ whose conductor splits as $(c_1,c_2)$. **Coprimality is exactly the condition under which "tensor product of two cyclic apexes" $=$ "CRT split of one cyclic apex."**

> **CRT $=$ tensor factorization, on the nose, for coprime factors: $U_{\mathrm{CRT}}:\mathbb C^N\xrightarrow{\sim}\mathbb C^{N_1}\otimes\mathbb C^{N_2}$ intertwines characters, conductor index, and apex generator. The single shared Mellin variable $\beta$ is the global-scale gauge; it is not a prime axis and does not split.**

---

## 2. Product state $\Leftrightarrow$ separable ledger {#sec:2}

\hypertarget{stmt:2-1}{}
**Lemma 2.1 (Complex-ledger separability $\Leftrightarrow$ product amplitude).** Let $N=N_1N_2$ (coprime) and let $z\in\Omega=(\mathbb C^\times)^N$ have centered complex log-ledger $y_s(z)=\log z_s-\frac1N\sum_j\log z_j$, computed on a fixed branch of $\log$ on $\Omega$. The following are equivalent:

(i) $z$ is a product state: $z=u\otimes v$ for some $u\in(\mathbb C^\times)^{N_1}$, $v\in(\mathbb C^\times)^{N_2}$, i.e. $z_{(s_1,s_2)}=u_{s_1}v_{s_2}$;

(ii) $y(z)$ is **separable across the two prime axes**: $y_{(s_1,s_2)}(z)=y^{(1)}_{s_1}+y^{(2)}_{s_2}$, i.e. $y_A=0$ for $|A|\ge 2$ in the ANOVA decomposition ([\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Definition 4.6).

Both modulus and phase separate simultaneously.

**Proof.** *(i)$\Rightarrow$(ii).* If $z_{(s_1,s_2)}=u_{s_1}v_{s_2}$ then $\log z_{(s_1,s_2)}=\log u_{s_1}+\log v_{s_2}$ (branch-additive on $\Omega$ up to a global $2\pi i$ constant absorbed by centering). The global mean splits:
$$\tfrac1N{\textstyle\sum_{s_1,s_2}}\log z=\tfrac1{N_1}{\textstyle\sum_{s_1}}\log u_{s_1}+\tfrac1{N_2}{\textstyle\sum_{s_2}}\log v_{s_2}=\overline{\log u}+\overline{\log v}.$$
Hence $y_{(s_1,s_2)}=(\log u_{s_1}-\overline{\log u})+(\log v_{s_2}-\overline{\log v})=:y^{(1)}_{s_1}+y^{(2)}_{s_2}$, each of zero marginal. By [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) Proposition 3.6 the real (modulus) and imaginary (argument) parts split termwise, so both moduli and phases are separable.

*(ii)$\Rightarrow$(i).* If $y_{(s_1,s_2)}=y^{(1)}_{s_1}+y^{(2)}_{s_2}$ then $\log z_{(s_1,s_2)}=y^{(1)}_{s_1}+y^{(2)}_{s_2}+\overline{\log z}$. Exponentiate and set $u_{s_1}:=\exp(y^{(1)}_{s_1}+\tfrac12\overline{\log z}+a)$, $v_{s_2}:=\exp(y^{(2)}_{s_2}+\tfrac12\overline{\log z}-a)$ for any constant $a$; then $z_{(s_1,s_2)}=u_{s_1}v_{s_2}$, a product state. $\square$

\hypertarget{stmt:2-2}{}
**Theorem 2.2 (The bridge: four equivalent statements).** Let $N=N_1N_2$ (coprime) and $z\in\Omega$ a pure state with apex generator $\mathcal M_z(\beta,c)$. The following are equivalent:

1. $z=u\otimes v$ is a **product state** (Schmidt rank $1$; unentangled across the $\mathbb C^{N_1}\!\otimes\!\mathbb C^{N_2}$ cut);
2. the centered complex log-ledger $y(z)$ is **separable** across the prime axes;
3. the apex generator **Euler-factorizes**, $\mathcal M_z(\beta,(c_1,c_2))=\mathcal M^{(N_1)}_u(\beta,c_1)\,\mathcal M^{(N_2)}_v(\beta,c_2)$ for all $(\beta,c_1,c_2)$;
4. the **cross-prime higher-order interaction information vanishes** identically: $\Delta_y(\beta)\equiv 0$ in [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 4.7.

Consequently, $E_{\mathrm{apex}}(z)=0\iff z$ is unentangled (for pure states on $\Omega$).

**Proof.** $(1)\Leftrightarrow(2)$ is Lemma 2.1. $(2)\Leftrightarrow(3)\Leftrightarrow(4)$ is [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorems 4.4 and 4.7, transported through $U_{\mathrm{CRT}}$ by Proposition 1.1: the character factorization (a) is precisely what turns separability of $y$ into the product factorization of $\mathcal M_z$. The final clause is the definition of $E_{\mathrm{apex}}$ as the obstruction norm to factorization (3): it vanishes iff (3) holds iff (by $(1)\Leftrightarrow(3)$) $z$ is a product state, which for pure states is exactly unentangled. $\square$

\hypertarget{stmt:2-3}{}
**Corollary 2.3 ([\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1 $=$ [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 4.4).** The product-state factorization formula displayed in [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1,
$$\mathcal M_{u\otimes v}(\beta,(c_1,c_2))=\mathcal M^{(N_1)}_u(\beta,c_1)\,\mathcal M^{(N_2)}_v(\beta,c_2),$$
is, under $U_{\mathrm{CRT}}$ for coprime $N_1,N_2$, *literally* the $(\Leftarrow)$ direction of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 4.4 (separable ledger $\Rightarrow$ Euler factorization). The "categorical-simplex measurement of entanglement" of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1 and the "cross-prime interaction stratum" of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4 are one stratum, presented in two frames. $\square$

> **Product state $\Leftrightarrow$ separable ledger $\Leftrightarrow$ Euler-factorized apex $\Leftrightarrow$ vanishing cross-prime interaction information. The non-factorization of $\mathcal M_z$ that [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1 reads as entanglement is exactly the cross-prime interaction content that [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4 reads as ANOVA mixed strata.**

---

## 3. Cross-prime interaction $=$ entanglement in the CRT basis {#sec:3}

Theorem 2.2 aligns the *vanishing loci*. We now align the *values*, and find exactly where they part.

### 3.1 The two scalars

For a pure state $z$ (normalized) with Born distribution $p_{(s_1,s_2)}=|z_{(s_1,s_2)}|^2$:

- **Entanglement entropy** $S_{\mathrm{ent}}(z)=-\sum_k\sigma_k^2\log\sigma_k^2$, $\{\sigma_k^2\}$ the Schmidt spectrum (eigenvalues of the reduced density matrix $\rho_1=\operatorname{tr}_2|z\rangle\langle z|$). This is **local-unitary invariant**: $S_{\mathrm{ent}}(U\!\otimes\!V\,z)=S_{\mathrm{ent}}(z)$ for all $U\in U(N_1)$, $V\in U(N_2)$.
- **Cross-prime interaction information** $\mathbb I(z)$: for the bipartite ($k=2$) case, the mutual information of the Born distribution in the computational basis,
$$\mathbb I(z)=I(S_1;S_2)_p=\sum_{s_1,s_2}p_{(s_1,s_2)}\log\frac{p_{(s_1,s_2)}}{p^{(1)}_{s_1}p^{(2)}_{s_2}}\ge 0,$$
the order-$2$ Taylor content of $\Delta_y$ in [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) Theorem 4.7. This is **not** local-unitary invariant: it depends on $\{|z_s|^2\}$, hence on the frame.

### 3.2 The Schmidt-frame identity

\hypertarget{stmt:3-1}{}
**Proposition 3.1 (Entanglement entropy is interaction information in the Schmidt frame).** Let $z=\sum_k\sigma_k\,a_k\otimes b_k$ be a Schmidt decomposition. In the *local Schmidt bases* $\{a_k\}\subset\mathbb C^{N_1}$, $\{b_\ell\}\subset\mathbb C^{N_2}$, the Born distribution is diagonal, $p_{(k,\ell)}=\sigma_k^2\,\delta_{k\ell}$, and its mutual information equals the entanglement entropy:
$$I(S_1;S_2)_{p}^{\,\mathrm{Schmidt}}=H(\sigma^2)+H(\sigma^2)-H(\sigma^2)=H(\sigma^2)=S_{\mathrm{ent}}(z).$$

**Proof.** In the Schmidt frame $|z\rangle=\sum_k\sigma_k|a_k\rangle|b_k\rangle$, so $p_{(k,\ell)}=|\langle a_k|\langle b_\ell|z\rangle|^2=\sigma_k^2\delta_{k\ell}$. Marginals $p^{(1)}_k=p^{(2)}_k=\sigma_k^2$. Then $H(S_1)=H(S_2)=H(S_1,S_2)=H(\{\sigma_k^2\})$ (the joint is supported on the diagonal with the same weights), and $I=H(S_1)+H(S_2)-H(S_1,S_2)=H(\{\sigma_k^2\})=S_{\mathrm{ent}}$. $\square$

\hypertarget{stmt:3-2}{}
**Theorem 3.2 (Interaction information $=$ entanglement in the CRT basis; exact domain).** For a pure state $z\in\Omega$ on coprime $N=N_1N_2$, the cross-prime interaction information $\mathbb I(z)$ is the value of the entanglement-entropy functional read in the **fixed computational (CRT) basis** rather than in the Schmidt basis. In particular:

(a) *(Zero set, exact.)* $\mathbb I(z)=0\iff E_{\mathrm{apex}}(z)=0\iff S_{\mathrm{ent}}(z)=0\iff z$ unentangled. (Theorem 2.2.)

(b) *(Coincidence locus.)* $\mathbb I(z)=S_{\mathrm{ent}}(z)$ **iff** the CRT basis is a Schmidt basis of $z$ (Proposition 3.1).

(c) *(Frame defect.)* In general $\mathbb I(z)\ne S_{\mathrm{ent}}(z)$, and the gap $S_{\mathrm{ent}}(z)-\mathbb I(z)$ is generated by the local-unitary orbit: $\mathbb I$ varies over $\{(U\!\otimes\!V)z:U,V\}$ while $S_{\mathrm{ent}}$ is constant on it.

**Proof.** (a) is Theorem 2.2 plus the fact that for a pure state $S_{\mathrm{ent}}=0\iff$ Schmidt rank $1\iff$ product. (b) is Proposition 3.1: aligning the computational and Schmidt frames makes the two scalars equal; conversely if they are equal for the structural reason of Proposition 3.1 the Born distribution is diagonal in the local bases, which characterizes the Schmidt frame (up to degeneracy relabelling). (c) $S_{\mathrm{ent}}$ is LU-invariant (spectral function of $\rho_1$); $\mathbb I$ is a function of $\{|z_s|^2\}$, which a generic $U\otimes V$ changes; hence $\mathbb I$ is non-constant on the LU orbit whose $S_{\mathrm{ent}}$ is fixed. $\square$

### 3.3 The signed, multipartite refinement

For $k\ge 3$ prime axes (e.g. $N=2\cdot 3\cdot 5=30$), the higher-order interaction information of Han/McGill/Yeung is **signed** (positive $=$ redundancy, negative $=$ synergy), whereas a single bipartite entanglement entropy is non-negative. The classical shadow therefore carries *strictly finer* sign data than any one bipartition number: it resolves the lattice of all axis-subsets $A\subseteq\{1,\dots,k\}$, not one cut. This is a feature, not a discrepancy — it is the multipartite-entanglement bookkeeping that no single $S_{\mathrm{ent}}$ encodes — but it confirms that "interaction information" and "an entanglement entropy" are not synonyms even on the vanishing locus once $k\ge 3$: the right quantum partner of the *signed* interaction lattice is the lattice of bipartite/multipartite entanglement entropies across all axis cuts, read in the Schmidt frame of each cut.

> **$S_{\mathrm{ent}}$ is the Schmidt-frame value of the same functional whose computational-frame value is $\mathbb I$. They share a zero set exactly; they share a value only when the CRT basis diagonalizes the Schmidt decomposition. The signed multipartite interaction lattice refines a single entanglement number.**

---

## 4. Domain and gap, stated honestly {#sec:4}

**Domain where the identification is EXACT.** All three of the following must hold:

1. **Coprime factors**, $\gcd(N_1,N_2)=1$ (Remark 1.2): only then is the single $\mathbb Z/N$ apex the two-particle tensor apex.
2. **Computational (CRT) basis** fixed: $\mathbb I$ and $E_{\mathrm{apex}}$ are frame-tethered (Theorem 3.2c).
3. **Pure states on $\Omega$** (all amplitudes nonzero): Lemma 2.1's $\log$ is single-valued and additive; the exact zero-set equivalence of Theorem 2.2 holds.

On this domain: *product state $\Leftrightarrow$ separable ledger $\Leftrightarrow$ vanishing interaction information $\Leftrightarrow$ unentangled*, and the entanglement entropy equals the interaction information **iff** the CRT basis is a Schmidt basis.

**The gap to genuine entanglement** is exactly the basis-independence that $\mathbb I$ lacks. Three concrete faces:

- **(G1) Local-unitary invariance.** Genuine entanglement is invariant under $U(N_1)\times U(N_2)$; $\mathbb I$ and $E_{\mathrm{apex}}$ are not. They agree on the *vanishing* locus (product states are LU-stable) but their *level sets* differ. A genuine monotone is the LU-completion $\min_{U,V}$ (equivalently the Schmidt-frame value) — the basis-free object Theorem 3.2c isolates.
- **(G2) Boundary / zero amplitudes.** Off $\Omega$ (some $z_s=0$, e.g. the Bell state $\tfrac1{\sqrt2}(|00\rangle+|11\rangle)$ with $z_{01}=z_{10}=0$), the centered log-ledger has $-\infty$ entries and Lemma 2.1 needs the closure. The Schmidt-rank picture is the invariant completion there; interaction information must be taken as a limit.
- **(G3) Mixed states.** For $\rho$ mixed, quantum separability ("convex mixture of products") is strictly weaker than Born-independence: a classically correlated *diagonal* $\rho$ is quantum-separable yet has non-zero diagonal interaction information, while off-diagonal coherence is invisible to the diagonal $\mathbb I$ entirely. This is the deepest face of basis-independence; it is the province of the Bures / quantum-Fisher door [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.2 (Conjecture 7.2), **not** of §7.1.

> **The honest one-liner: *interaction information $=$ entanglement in the CRT basis.* Exact in the computational basis for coprime, pure, nowhere-vanishing states; the surplus carried by genuine entanglement is precisely basis-independence (local-unitary invariance), which the classical shadow does not see.**

---

## 5. Recommendation and the sharpened Conjecture 7.1 {#sec:5}

**Merge or new paper.** *Do not physically merge.* [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4 is load-bearing inside [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) (it defines the conductor-axis arithmetic and the $N=6$ structural anchor) and must stay; [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1 is one entry in a deliberately unnumbered forward-door catalog and would unbalance §7 if promoted in place. The bridge result draws on **both** papers' machinery (ANOVA / interaction information from [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985); tensor / Hopf / Schmidt from [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442)) plus new content (the LU-invariance gap, the Schmidt-frame identity). It is a first-class cross-cutting identification and belongs in **its own short paper — this one, \heb{ל}23** — citing [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4 and [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1 rather than absorbing either. Then [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) Conjecture 7.1 is sharpened to cite \heb{ל}23.

**Number.** Free integer \heb{ל}-slots are $23,24,25,26$ ($\heb{ל}0$–$\heb{ל}22$ and $\heb{ל}27$–$\heb{ל}33$ are occupied; $\heb{ל}8$–$\heb{ל}18$ noted taken in [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7). We take the lowest, **\heb{ל}23**. (If the program prefers to signal the bridge as a child of [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442), the decimal slot \heb{ל}7.1 is available and follows the \heb{ל}8.4 / \heb{ל}9.4 / \heb{ל}22.x convention; we recommend the integer slot because the result is co-parented by [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) and introduces a new cross-cutting identity rather than extending one parent.)

**Proposed sharpened replacement for [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1, Conjecture 7.1.** Replace the loose conjecture with a *theorem-plus-conjecture* pair that separates the now-proved computational-basis half from the genuinely open LU-invariant half:

> **Theorem 7.1a (Computational-basis entanglement readout; proved in [\heb{ל}23](#)).** For coprime $N,M$ the CRT unitary $U_{\mathrm{CRT}}:\mathbb C^{NM}\xrightarrow{\sim}\mathbb C^N\otimes\mathbb C^M$ intertwines the apex generators, and on the open torus $\Omega$ the following are equivalent for a pure state $z$: (i) $z=u\otimes v$ is a product state; (ii) the centered complex log-ledger is separable; (iii) $\mathcal M_z$ factorizes as $\mathcal M_u\cdot\mathcal M_v$; (iv) the cross-prime interaction information of [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) §4 vanishes. Hence the obstruction-norm $E_{\mathrm{apex}}(z)$ vanishes **iff** $z$ is unentangled, and $E_{\mathrm{apex}}$ (equivalently the interaction information) is the entanglement-entropy functional read in the fixed computational basis: it equals $S_{\mathrm{ent}}(z)$ exactly when the computational basis is a Schmidt basis of $z$.

> **Conjecture 7.1b (Local-unitary completion to a monotone).** The local-unitary–minimized obstruction-norm $E^\star_{\mathrm{apex}}(z):=\min_{U\in U(N),\,V\in U(M)}E_{\mathrm{apex}}\big((U\otimes V)z\big)$ is an entanglement monotone that recovers von-Neumann-entropy-style entanglement on the Schmidt decomposition; the minimizing frame is a Schmidt frame, at which $E^\star_{\mathrm{apex}}$ reduces to the interaction information of the Schmidt-basis Born distribution. The basis-independence supplied by the $\min$ over local unitaries is exactly the genuine-quantum content absent from the fixed-basis interaction information.

This keeps the [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.1 door open where it is genuinely open (the LU-invariant monotone, 7.1b) while recording that its computational-basis content (7.1a) is now a theorem, with the proof in \heb{ל}23.

---

## 6. Forward doors {#sec:6}

- **D1 — The LU-invariant monotone (Conjecture 7.1b).** Is $E^\star_{\mathrm{apex}}$ a full entanglement monotone (non-increasing under LOCC), and does the $\min$ define a computable Schmidt-frame selector? This is the genuine quantum surplus.
- **D2 — Multipartite synergy $\leftrightarrow$ multi-cut entanglement.** Match the signed interaction-information lattice ($k\ge 3$ prime axes, anchor $N=30$) to the lattice of Schmidt-frame entanglement entropies across all axis cuts; locate "synergy $<0$" in the entanglement-of-cuts picture.
- **D3 — Mixed states / Bures.** Fuse with [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) §7.2 (Conjecture 7.2): the off-diagonal coherence that diagonal interaction information misses (G3) is the Bures-metric content; quantum separability vs Born-independence is the mixed-state gap.
- **D4 — Non-coprime degeneration.** For $\gcd(N_1,N_2)=d>1$ the single-apex/two-particle identification fails (Remark 1.2); describe the partial CRT (over the coprime part) and the $d$-fold residual coupling as a controlled break of the bridge.

---

## References

- McGill, W. J. (1954). Multivariate information transmission. *Psychometrika* 19, 97–116. [DOI: 10.1007/BF02289159](https://doi.org/10.1007/BF02289159).
- Han, T. S. (1980). Multiple mutual informations and multiple interactions in frequency data. *Information and Control* 46, 26–45. [DOI: 10.1016/S0019-9958(80)90478-7](https://doi.org/10.1016/S0019-9958(80)90478-7).
- Yeung, R. W. (1991). A new outlook on Shannon's information measures. *IEEE Trans. Inform. Theory* 37, 466–474. [DOI: 10.1109/18.79902](https://doi.org/10.1109/18.79902).
- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge Univ. Press. (Schmidt decomposition; entanglement entropy; local-unitary invariance.)
- Bengtsson, I., & Życzkowski, K. (2017). *Geometry of Quantum States*, 2nd ed. Cambridge Univ. Press.
- [\heb{ל}0](https://doi.org/10.5281/zenodo.20423985) — Gauge Selection and the Fourier–Mellin Apex of the Categorical Simplex (§4: CRT cross-prime interaction).
- [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — Character Orthogonality and the Conductor Lattice.
- [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) — Complex Amplitudes and the Quantum Sector of the Apex (§7.1: entanglement door).
