# T11 - The Apex Vertex Calculus

**Finite Feynman Rules for the Cumulant-Gauge Tower**

**Leonardo Murillo Montero**

*First draft - May 26, 2026*

---

> *The obstruction to closure is not dynamical noise. It is conductor fusion.*

---

## Abstract

**Situation.** T0 named the Fourier-Mellin apex
\[
\mathcal M_x(\beta,c)=\frac1N\sum_{s\in\mathbb Z/N}e^{\beta y_s}\overline{\chi_c(s)}
\]
as the two-axis generator of the lamed-series: Taylor jets in \(\beta\) give the cumulant/tensor tower, while integer samples of \(\beta\) give the power-closure gauge hierarchy. T2 identified the cumulant tower as an effective action. T3 proved that the cubic Amari-Chentsov vertex obeys the additive selection rule \(a+b+c\equiv0\pmod N\). T8 gave the multiplicative analog on Dirichlet characters. T9 gave the Helmert-Fourier transfer matrix between the dimensional and conductor bases. T10 swept the integer gauge corridor and placed the closure diagonal in its Kummer arithmetic ambient.

**Gap.** The series has several named vertices but not yet the vertex calculus itself. The cubic rule of T3 is one case of a general \(n\)-leg conservation law. The conductor packets of T3 are not merely a decomposition; they fuse under the same vertex law. The projection residuals that appear in applications are not ad hoc errors; they are exactly the boundary of a packet set under conductor fusion.

**Action.** We prove three structure theorems. First, the **Apex Feynman Rule Theorem**: every Taylor coefficient and every integer closure sample of the apex is computed by finite character-conservation vertices; moments are finite diagrams and cumulants are their connected parts by Mobius inversion on the partition lattice. Second, the **Conductor Fusion Theorem**: packet products are determined prime-locally by \(p\)-adic cancellation of character indices. Third, the **Projection-Closure Theorem**: a projected packet sector closes under an \(n\)-leg apex interaction if and only if it is fusion-closed; otherwise the universal residual support of the projected interaction is its conductor-fusion boundary. We finish with the minimal fusion completion corollary.

**Result.** Four core claims:

1. **Finite apex vertices.** The \(n\)-leg vertex with input characters \(a_1,\ldots,a_n\) and output \(c\) is
\[
V_n(a_1,\ldots,a_n;c)=\mathbf 1[a_1+\cdots+a_n\equiv c\pmod N].
\]

2. **Connected diagrams.** The cumulant vertex is the connected part of the moment vertex, obtained by Mobius inversion over set partitions.

3. **Conductor fusion.** If \(H_d\) is the conductor-\(d\) packet, then \(H_{d_1}\star\cdots\star H_{d_n}\) decomposes into conductor packets according to prime-local cancellation rules.

4. **Projection closure.** For \(H_S=\bigoplus_{d\in S}H_d\), the projected \(n\)-vertex closes on \(H_S\) exactly when \(S\) is closed under \(n\)-fold conductor fusion. The universal leakage support is not an analytic afterthought; it is the fusion boundary \(\partial_n S\).

**Harvest.** T11 turns the lamed-series into a finite arithmetic perturbation theory. T2's effective action supplies the generating functional; T3's cubic selection rule becomes the \(n=3\) vertex; T8 is the multiplicative-sector version; T9 is the basis-transfer Jacobian; T10 supplies the gauge-rung arithmetic. The application slogan is now a theorem:
\[
\boxed{\text{every projected simplex theory leaks exactly through its conductor-fusion boundary.}}
\]

**Keywords:** apex generator, cumulant tower, finite Feynman rules, character conservation, conductor packets, conductor fusion, Mobius inversion, connected diagrams, projection closure, packet boundary, finite Fourier analysis, categorical effective action.

---

## Cross-references from prior papers

| Cited result | Used for |
|---|---|
| T0 Definition 3.1 (structured apex \(\mathcal M_x(\beta,c)\)) | Base object of the vertex calculus |
| T0 Theorems 3.3 and 3.5 (moment and closure diagonals) | Recovered as Theorem 2.1 |
| T2 (cumulant tower as effective action) | Connected-diagram interpretation |
| T3 (character basis and cubic selection rule) | \(n=3,c=0\) case of Theorem 2.1 |
| T4 (Helmert ladder) | Downstream basis transfer via T9; not needed in proofs |
| T5/T6 (harmonic and RMS gauges) | Low-rung samples of the gauge corridor |
| T8 (multiplicative apex) | Parallel multiplicative vertex rule in Section 6 |
| T9 (Helmert-Fourier transfer matrix) | Basis transfer of vertices; forward door |
| T10 (Kummer clock and \(m\)-power hierarchy) | Integer gauge closure diagonal |

---

## Notation

Let \(G=\mathbb Z/N\). We write addition in \(G\) modulo \(N\). Let
\[
\chi_a(s)=e^{2\pi ias/N},\qquad a,s\in G,
\]
and for \(f:G\to\mathbb C\) define
\[
\widehat f_a=\frac1N\sum_{s\in G}f(s)\overline{\chi_a(s)},\qquad
f(s)=\sum_{a\in G}\widehat f_a\chi_a(s).
\]

For a positive ledger \(x:G\to\mathbb R_{>0}\), define the centered log-ledger
\[
y_s=\log x_s-\frac1N\sum_{t\in G}\log x_t.
\]
Then \(\widehat y_0=0\). The structured apex is
\[
\mathcal M_x(\beta,c)=\frac1N\sum_{s\in G}e^{\beta y_s}\overline{\chi_c(s)}
=\widehat{e^{\beta y}}_c.
\]

The additive conductor of \(\chi_a\) is
\[
\operatorname{cond}(a)=\frac{N}{\gcd(a,N)}
\]
with the convention \(\operatorname{cond}(0)=1\). The conductor packet is
\[
H_d=\operatorname{span}_{\mathbb C}\{\chi_a:\operatorname{cond}(a)=d\}.
\]
The nontrivial mean-zero character space is
\[
H=\bigoplus_{\substack{d\mid N\\ d>1}}H_d.
\]

When \(N=\prod_p p^{A_p}\), we write \(v_p(\cdot)\) for the \(p\)-adic valuation.

---

## 1. Why a vertex calculus is needed

T3 proved the cubic selection rule:
\[
T(\chi_a,\chi_b,\chi_c)\ne0
\quad\Longleftrightarrow\quad
a+b+c\equiv0\pmod N.
\]
This was the first place the arithmetic of the labels became visible inside the information-geometric tensor tower. But the proof did not use anything special about \(3\) except the order of the tensor. It used only:

1. characters multiply by adding indices;
2. character orthogonality kills every nontrivial total index.

Those are \(n\)-leg facts. T11 therefore upgrades the cubic rule into a full finite vertex calculus.

The guiding dictionary is:

| Order | Vertex reading |
|---|---|
| \(n=2\) | propagator / Fisher metric / quadratic response |
| \(n=3\) | Amari-Chentsov cubic interaction |
| \(n=4\) | first closure-defect / quartic self-interaction |
| general \(n\) | finite \(n\)-wave interaction with character conservation |
| moments | all finite diagrams |
| cumulants | connected finite diagrams |
| conductor packets | arithmetic charge sectors |
| projection residual | conductor-fusion boundary |

This is finite. There are no integrals, ultraviolet divergences, or analytic continuation requirements in the core theorem. All sums are over finite groups.

---

## 2. The Apex Feynman Rule Theorem

### 2.1 Product-convolution identity

For \(f,g:G\to\mathbb C\),
\[
\widehat{fg}_c=\sum_{a+b\equiv c}\widehat f_a\widehat g_b.
\]
Iterating gives
\[
\widehat{f^n}_c=
\sum_{a_1+\cdots+a_n\equiv c}
\widehat f_{a_1}\cdots\widehat f_{a_n}.
\]

This is the finite Fourier theorem behind the entire paper.

### Theorem 2.1. Apex Feynman Rule Theorem

For every \(n\ge0\) and \(c\in G\),
\[
\partial_\beta^n\mathcal M_x(0,c)
=
\sum_{\substack{a_1,\ldots,a_n\in G\\
a_1+\cdots+a_n\equiv c}}
\widehat y_{a_1}\cdots\widehat y_{a_n}.
\]
Equivalently, the \(n\)-leg apex vertex with output \(c\) is
\[
V_n(a_1,\ldots,a_n;c)
=
\mathbf 1[a_1+\cdots+a_n\equiv c\pmod N].
\]

For integer \(m\ge1\),
\[
\mathcal M_x(m,c)
=G(x)^{-m}\widehat{x^m}_c
=G(x)^{-m}
\sum_{a_1+\cdots+a_m\equiv c}
\widehat x_{a_1}\cdots\widehat x_{a_m}.
\]
Negative integer \(m\) obeys the same rule after replacing \(x\) by the reciprocal ledger \(u_s=x_s^{-1}\).

**Proof.** Expand the apex:
\[
\mathcal M_x(\beta,c)=\widehat{e^{\beta y}}_c
=\sum_{n\ge0}\frac{\beta^n}{n!}\widehat{y^n}_c.
\]
Taking \(n\) derivatives at \(\beta=0\) gives
\[
\partial_\beta^n\mathcal M_x(0,c)=\widehat{y^n}_c.
\]
Apply the iterated product-convolution identity with \(f=y\). This proves the Taylor vertex rule.

For integer \(m\ge1\), since \(x_s=e^{\log x_s}=G(x)e^{y_s}\), we have
\[
e^{m y_s}=G(x)^{-m}x_s^m.
\]
Therefore
\[
\mathcal M_x(m,c)=\widehat{e^{my}}_c=G(x)^{-m}\widehat{x^m}_c.
\]
Apply product-convolution to \(x^m\). The negative case is the positive case applied to \(u=x^{-1}\). \(\square\)

### 2.2 Connected vertices and cumulants

Let
\[
Z_y(\beta)=\mathcal M_x(\beta,0)=\frac1N\sum_s e^{\beta y_s},
\qquad
K_y(\beta)=\log Z_y(\beta).
\]
Let \(\mu_n=\widehat{y^n}_0\) and let \(\kappa_n=K_y^{(n)}(0)\). Then the standard moment-cumulant formula is
\[
\kappa_n
=
\sum_{\pi\in\Pi_n}
(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}\mu_{|B|},
\]
where \(\Pi_n\) is the lattice of set partitions of \(\{1,\ldots,n\}\).

Substituting the Fourier rule for each block gives the connected vertex:
\[
V_n^{\mathrm{conn}}(a_1,\ldots,a_n)
=
\sum_{\pi\in\Pi_n}
(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}
\mathbf 1\!\left[\sum_{i\in B}a_i\equiv0\pmod N\right].
\]
Hence
\[
\kappa_n
=
\sum_{a_1,\ldots,a_n\in G}
V_n^{\mathrm{conn}}(a_1,\ldots,a_n)
\widehat y_{a_1}\cdots\widehat y_{a_n}.
\]

This is the finite connected-diagram rule.

**Corollary 2.2. The birth of closure defect.** Since \(\widehat y_0=0\), singleton blocks vanish. The order \(n=3\) connected vertex is the first genuinely interacting odd vertex, while \(n=4\) is the first order where disconnected pairings must be subtracted from a nontrivial moment. Thus the fourth cumulant is not an arbitrary "next tensor"; it is the first connected correction after quadratic propagation and cubic interaction have both appeared.

---

## 3. Conductor fusion

The vertex rule is entry-level. It tells us when a specific tuple of character indices contributes. T11 also needs the packet-level rule: if inputs live in conductor packets \(H_{d_i}\), which output packets can appear?

### 3.1 Definition

For divisor packets \(d_1,\ldots,d_n\mid N\), define their \(n\)-fold fusion support by
\[
\mathsf{Fuse}(d_1,\ldots,d_n)
=
\{\operatorname{cond}(a_1+\cdots+a_n):
\operatorname{cond}(a_i)=d_i\}.
\]
Equivalently,
\[
H_{d_1}\star\cdots\star H_{d_n}
=
\bigoplus_{d\in\mathsf{Fuse}(d_1,\ldots,d_n)}H_d,
\]
where \(\star\) denotes packet support under pointwise character product.

### Theorem 3.1. Conductor Fusion Theorem

Let \(N=\prod_p p^{A_p}\). For each input packet \(d_i\), write
\[
\alpha_{i,p}=v_p(d_i),\qquad
B_p=\max_i\alpha_{i,p},\qquad
m_p=\#\{i:\alpha_{i,p}=B_p\}.
\]
The possible output packet \(d=\prod_p p^{\gamma_p}\) is determined prime by prime as follows:
\[
\gamma_p\in
\begin{cases}
\{0\}, & B_p=0,\\
\{B_p\}, & p\text{ odd and }m_p=1,\\
\{0,1,\ldots,B_p\}, & p\text{ odd and }m_p\ge2,\\
\{B_p\}, & p=2\text{ and }m_p\text{ odd},\\
\{0,1,\ldots,B_p-1\}, & p=2\text{ and }m_p\text{ even}.
\end{cases}
\]
The global fusion support is exactly the set of products \(\prod_p p^{\gamma_p}\) with each local exponent allowed.

**Proof.** By character multiplication,
\[
\chi_{a_1}\cdots\chi_{a_n}=\chi_{a_1+\cdots+a_n}.
\]
Thus conductor fusion is the problem of determining the possible conductors of sums of indices.

Work prime-locally at \(p^A\). An index \(a_i\) has local conductor \(p^{\alpha_i}\) iff
\[
v_p(a_i)=A-\alpha_i,
\]
with \(\alpha_i=0\) corresponding to \(a_i\equiv0\pmod {p^A}\). Let \(B=\max_i\alpha_i\), \(m=\#\{i:\alpha_i=B\}\), and \(r=A-B\). The \(m\) maximal-conductor terms have valuation \(r\); all other terms have valuation \(>r\). Hence
\[
a_1+\cdots+a_n
=
p^r(u_1+\cdots+u_m+pW),
\]
where each \(u_j\) is a \(p\)-adic unit.

If \(B=0\), all terms are zero modulo \(p^A\), so the output exponent is \(0\).

If \(m=1\), one leading unit remains and no leading cancellation is possible. Thus the output valuation is \(r\), so \(\gamma=B\).

If \(p\) is odd and \(m\ge2\), sums of \(m\) units can be chosen to have any \(p\)-adic valuation from \(0\) through \(B\) after factoring \(p^r\). Therefore the output exponent can be \(B,B-1,\ldots,0\).

If \(p=2\), every unit is odd. A sum of an odd number of odd units is odd, so if \(m\) is odd no leading cancellation occurs and \(\gamma=B\). A sum of an even number of odd units is even, and choices of odd units realize every cancellation depth from \(1\) through \(B\) after factoring \(2^r\); therefore \(\gamma\in\{0,\ldots,B-1\}\).

The Chinese remainder theorem makes the prime-local choices independent, so global conductors are exactly the products of locally allowed exponents.

Finally, if one index of conductor \(d\) is attainable, then every index of conductor \(d\) is attainable: multiplication by a unit in \((\mathbb Z/N)^\times\) preserves all input conductors and acts transitively on indices of fixed conductor. Thus the entire packet \(H_d\) appears. \(\square\)

### 3.2 Reading the theorem

Conductor fusion is controlled by the highest local depth present among the inputs. If the highest-depth leg is unique, it survives. If several highest-depth legs appear, cancellation can lower conductor depth. The prime \(2\) is special because parity blocks cancellation when the number of highest-depth odd units is odd.

This is why cubic behavior at \(N=6\) is not symmetric between the \(2\)-axis and the \(3\)-axis:

- three conductor-2 legs have odd \(2\)-maximal multiplicity, so they remain conductor 2 and cannot close to the gauge packet;
- three conductor-3 legs at the odd prime \(3\) can cancel to conductor 1, allowing the pure \(A_3\) cubic closures.

---

## 4. Projection closure

Let \(S\) be a set of nontrivial conductor packets. Define
\[
H_S=\bigoplus_{d\in S}H_d,\qquad
\Pi_S:H\to H_S.
\]
The question is whether an \(n\)-leg apex interaction closes on \(H_S\). The answer is purely arithmetic.

### Theorem 4.1. Projection-Closure Theorem for Apex Vertices

The sector \(H_S\) is closed under the order-\(n\) apex interaction iff
\[
d_1,\ldots,d_n\in S
\quad\Longrightarrow\quad
\mathsf{Fuse}(d_1,\ldots,d_n)\subseteq S\cup\{1\}.
\]
The packet \(1\) is the trivial gauge packet and is ignored when working in the mean-zero tangent space.

If the condition fails, then for every choice of inputs the projected residual
\[
(1-\Pi_S)(u_1\cdots u_n),\qquad u_i\in H_S,
\]
is supported inside the conductor-fusion boundary
\[
\partial_n S
=
\bigcup_{d_1,\ldots,d_n\in S}
\mathsf{Fuse}(d_1,\ldots,d_n)\setminus(S\cup\{1\}).
\]
Conversely, every packet in \(\partial_n S\) is attained by some choice of character inputs. Thus \(\partial_n S\) is the exact universal residual support of the projected \(n\)-vertex.

**Proof.** Every \(u_i\in H_S\) has Fourier expansion
\[
u_i=\sum_{\operatorname{cond}(a_i)\in S}\widehat u_{i,a_i}\chi_{a_i}.
\]
Their pointwise product is
\[
u_1\cdots u_n
=
\sum_{a_1,\ldots,a_n}
\widehat u_{1,a_1}\cdots\widehat u_{n,a_n}
\chi_{a_1+\cdots+a_n}.
\]
Thus the possible output packets are exactly the packets in
\[
\mathsf{Fuse}(d_1,\ldots,d_n),\qquad d_i=\operatorname{cond}(a_i).
\]
If every such output lies in \(S\cup\{1\}\), then the nontrivial output lies in \(H_S\), so the projected interaction closes.

Conversely, suppose some \(d\in\mathsf{Fuse}(d_1,\ldots,d_n)\setminus(S\cup\{1\})\) with all \(d_i\in S\). By definition of fusion, choose indices \(a_i\) with \(\operatorname{cond}(a_i)=d_i\) and \(\operatorname{cond}(a_1+\cdots+a_n)=d\). Taking \(u_i=\chi_{a_i}\), the product is
\[
u_1\cdots u_n=\chi_{a_1+\cdots+a_n}\in H_d,
\]
which has nonzero component outside \(H_S\). Thus \(H_S\) is not closed.

The support statement follows from the same expansion: all residual terms have conductor in the displayed boundary, and every boundary packet occurs for some choice of input characters by definition of fusion. Therefore the boundary is not necessarily the support of every special input tuple; it is the exact universal support of the projected interaction operator. \(\square\)

\[
\boxed{\text{projection closure } \Longleftrightarrow \text{ fusion closure}.}
\]
\[
\boxed{\text{universal projection residual support }=\text{ conductor-fusion boundary}.}
\]

---

## 5. Minimal fusion completion

The Projection-Closure Theorem has a useful closure operator.

### Definition 5.1. \(n\)-fusion closure

For a packet set \(S\), define \(\operatorname{Cl}_n(S)\) to be the smallest packet set containing \(S\) such that
\[
d_1,\ldots,d_n\in \operatorname{Cl}_n(S)
\quad\Longrightarrow\quad
\mathsf{Fuse}(d_1,\ldots,d_n)\subseteq \operatorname{Cl}_n(S)\cup\{1\}.
\]

Equivalently, start with \(S_0=S\) and iterate
\[
S_{r+1}
=
S_r\cup
\left(
\bigcup_{d_1,\ldots,d_n\in S_r}\mathsf{Fuse}(d_1,\ldots,d_n)
\right)\setminus\{1\}.
\]
Since the divisor set of \(N\) is finite, the process stabilizes.

### Corollary 5.2. Minimal Fusion Completion

For fixed \(N\) and \(n\):

1. \(H_S\) is an order-\(n\) closed packet subtheory iff \(\operatorname{Cl}_n(S)=S\).
2. If \(S\) is not closed, the first leakage lies in \(\partial_n S\).
3. The iterated leakage completion is \(H_{\operatorname{Cl}_n(S)}\), the smallest order-\(n\) packet sector containing \(H_S\) on which the apex interaction closes.
4. Fusion-closed packet sets are closed under intersection and therefore form a meet-semilattice.

**Proof.** Items (1)-(3) follow directly from Definition 5.1 and Theorem 4.1. For (4), if \(S\) and \(S'\) are fusion-closed and \(d_1,\ldots,d_n\in S\cap S'\), then their fusion support lies in both \(S\cup\{1\}\) and \(S'\cup\{1\}\), hence in \((S\cap S')\cup\{1\}\). Thus \(S\cap S'\) is fusion-closed. \(\square\)

In application language: if a projected theory leaks, T11 gives the smallest hidden sector one must add. No dynamics need to be guessed.

---

## 6. Worked example: \(N=6\)

Let \(N=6=2\cdot3\). The nontrivial additive conductor packets are
\[
A_2=H_2=\operatorname{span}\{\chi_3\},\qquad
A_3=H_3=\operatorname{span}\{\chi_2,\chi_4\},\qquad
M=H_6=\operatorname{span}\{\chi_1,\chi_5\}.
\]
Take
\[
S=\{2,3\},\qquad H_S=A_2\oplus A_3.
\]

At cubic order, the exact closing multisets in \(\{1,2,3,4,5\}\) are
\[
\{2,2,2\},\quad
\{4,4,4\},\quad
\{1,1,4\},\quad
\{2,5,5\},\quad
\{1,2,3\},\quad
\{3,4,5\}.
\]
The two pure \(A_3\) triples close inside \(S\). The \(A_2\)-leg triples force an \(M\)-leg. The pure \(A_2\) candidate fails:
\[
3+3+3=9\equiv3\not\equiv0\pmod6.
\]

By Theorem 4.1,
\[
\partial_3\{2,3\}=\{6\}.
\]
Therefore every cubic projection residual from the \(A_2\oplus A_3\) sector is supported on \(M=H_6\).

This is the clean mathematical statement behind the application slogan:

\[
\boxed{
\text{on the \(N=6\) cubic row, the non-unit sector leaks exactly into the unit-indexed full-conductor packet.}
}
\]

### 6.1 Why this is a theorem, not numerology

At \(N=6\), the full-conductor additive indices are
\[
\{1,5\}=(\mathbb Z/6)^\times.
\]
Thus the residual packet \(M=H_6\) is indexed by the multiplicative units. But T11's theorem does not depend on the physical name of the residual. It says:

1. choose a packet sector \(S\);
2. compute its conductor-fusion boundary;
3. the projected residual has exactly that support.

The \(N=6\) unit/nonunit split is one case of this general rule.

---

## 7. Multiplicative parallel

T8 introduced the multiplicative apex on units:
\[
\mathcal D_x(\beta,\psi)
=
\frac{1}{\varphi(N)}
\sum_{s\in(\mathbb Z/N)^\times}x_s^\beta\overline{\psi(s)},
\qquad
\psi\in\widehat{(\mathbb Z/N)^\times}.
\]
The additive vertex rule
\[
a_1+\cdots+a_n\equiv c\pmod N
\]
has the multiplicative analog
\[
\psi_1\cdots\psi_n=\psi.
\]

Thus all three T11 structures have multiplicative-sector analogs:

| Additive sector | Multiplicative sector |
|---|---|
| character indices \(a\in\mathbb Z/N\) | Dirichlet characters \(\psi\in\widehat{(\mathbb Z/N)^\times}\) |
| conservation \(a_1+\cdots+a_n=c\) | conservation \(\psi_1\cdots\psi_n=\psi\) |
| conductor packets \(H_d\) | primitive/imprimitive Dirichlet conductor strata |
| additive fusion | multiplicative character-product fusion |
| Gauss sums | bridge between sectors |

The full bilateral theory belongs to the T8.3 forward door. T11 supplies the additive packet calculus on which that bilateral theory should rest.

---

## 8. What T11 does not claim

T11 is deliberately pure framework.

It does not claim a physical field theory, a spacetime theory, quantum gravity, Standard Model structure, or a Bures/density-matrix result. Those may be downstream applications of the packet calculus, but they are not needed for the theorems here.

The theorem-level output of T11 is narrower and stronger:

\[
\boxed{
\text{the lamed-series has a finite arithmetic perturbation theory.}
}
\]

Every later application should first specify:

1. the modulus \(N\);
2. the interaction order \(n\);
3. the packet sector \(S\);
4. the fusion boundary \(\partial_nS\);
5. the interpretation, if any, of the retained sector and the residual sector.

The interpretation is optional. The fusion boundary is not.

---

## 9. Forward doors

### 9.1 Packet-subtheory classification

For fixed \(N\) and \(n\), classify all fusion-closed packet sets \(S\). This is a finite combinatorial problem on the divisor lattice of \(N\). The classification gives all packet subtheories that close at order \(n\).

### 9.2 Primorial fusion tables

Compute the full cubic and quartic fusion tables for
\[
N=6,\quad 30,\quad 210.
\]
These are the first squarefree primorial rows with two, three, and four prime axes. T11 predicts that the residual sectors are determined by their fusion boundaries, but the packet table should be written explicitly.

### 9.3 Helmert transfer of vertices

Use T9's Helmert-Fourier matrix \(U\) to transfer the vertex tensors from character coordinates to Helmert coordinates. The character basis gives conservation laws; the Helmert basis gives triangular dimensional balances. Their equality is the arithmetic Jacobian view of T9 at tensor level.

### 9.4 Newton-Hankel closure of the gauge corridor

T11 treats all orders formally. A separate paper should prove that the infinite tower is finite-rank: for an \(N\)-slot ledger, finitely many power sums determine the rest. That is the natural T12.

### 9.5 Bilateral Pontryagin vertex calculus

Combine T11's additive vertex calculus with T8's multiplicative vertex calculus through Gauss sums. This is the packet-level version of the additive/multiplicative bridge.

---

## 10. Coda

T3 found the line
\[
a+b+c\equiv0\pmod N.
\]
T11 says that line was the first visible face of a general machine.

The apex generator does not merely store means, cumulants, and closures. It supplies finite vertices. The conductor packets do not merely organize characters. They fuse. A projected theory does not merely fail to close. It leaks through a computable arithmetic boundary.

The one-sentence apex of T11:

> **The obstruction to closure is not dynamical noise; it is conductor fusion.**

---

## References and anchors

Brillinger, D. R. (1975). *Time Series: Data Analysis and Theory.* Holt, Rinehart and Winston. (Moment-cumulant identities.)

Lang, S. (2002). *Algebra.* Revised third edition. Graduate Texts in Mathematics 211. Springer. (Finite abelian groups, characters, valuations.)

Murillo Montero, L. (2026). *T0 - Gauge Selection and the Fourier-Mellin Simplex.* First draft, May 24, 2026.

Murillo Montero, L. (2026). *T2 - The Cumulant Tower as Effective Action.* Zenodo preprint.

Murillo Montero, L. (2026). *T3 - Character Orthogonality on the Conductor Lattice.* Zenodo preprint.

Murillo Montero, L. (2026). *T8 - The Multiplicative Apex and Finite Dirichlet Polynomials.* First draft, May 25, 2026.

Murillo Montero, L. (2026). *T9 - The Helmert-Fourier Transfer Matrix.* First draft, May 25, 2026.

Murillo Montero, L. (2026). *T10 - The Kummer Clock and the m-Power Gauge Hierarchy.* First draft, May 25, 2026.
