# \heb{ל}5 — The Harmonic-Simplicial Dual Gauge

**Leonardo Murillo Montero**

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 24, 2026*

## Abstract

**Situation.** The first four papers handed forward four structures: [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s native simplicial chart (keep the redundant coordinate, work in the mean-zero hyperplane, read Fisher–Rao through the square-root sphere); [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s scalar generator \(\Phi=\log Z\) and its categorical cumulant tower; [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s arithmetic substrate, where the cubic vertex obeys \(a+b+c\equiv 0\pmod N\) in the character basis of \(\mathbb Z/N\); and [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s Helmert residue ladder, which on unit normalization exposes the prime square-root field clock \(K_N=\mathbb Q(\sqrt p:p\le N)\). Arithmetic and geometric means entered as gauges — yet the classical triad \(H\le G\le A\) is still missing its reciprocal face.

**Surprise.** The harmonic mean is not a third unrelated average. It is the polar partner of arithmetic mean, with geometric mean as the self-dual mirror between them:

\[
A(x)=\frac{1}{H(x^{-1})},\qquad G(x^{-1})=\frac{1}{G(x)}.
\]

\(A\) is affine in \(x\); \(H\) in \(x^{-1}\); \(G\) in \(\log x\). One ladder, three observers.

**Action.** We formalize the three gauge sections \(\sum_i x_i=N,\ \prod_i x_i=1,\ \sum_i x_i^{-1}=N\) of the positive projective cone, and define the reciprocal closure

\[
p_i^\vee=\frac{x_i^{-1}}{\sum_j x_j^{-1}}=\frac{H(x)}{N\,x_i}.
\]

Harmonic normalization is then ordinary simplicial closure applied to \(x^{-1}\), and the Helmert ladder reads three ways: arithmetic gaps, geometric log-ratios, and harmonic reciprocal gaps.

**Result.** In centered log coordinates \(y_i=\log x_i-\tfrac1N\sum_j\log x_j\) with \(K_y(t)=\log\!\bigl(\tfrac1N\sum_i e^{ty_i}\bigr)\), arithmetic and harmonic means sample the same cumulant generator at opposite temperatures:

\[
\log\frac{A(x)}{G(x)}=K_y(1),\qquad \log\frac{G(x)}{H(x)}=K_y(-1).
\]

Adding and subtracting splits the spread into a parity pair — an even-cumulant ledger and an odd-cumulant ledger:

\[
\log\frac{A(x)}{H(x)}=2\!\sum_{m\ge1}\!\frac{\kappa_{2m}}{(2m)!},\qquad
\log\frac{A(x)\,H(x)}{G(x)^2}=2\!\sum_{m\ge1}\!\frac{\kappa_{2m+1}}{(2m+1)!}=\frac{\kappa_3}{3}+O(\|y\|^5).
\]

Combined with [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s character orthogonality, the harmonic skew \(\log(AH/G^2)\) becomes a scalar witness for the conductor-coupled cubic content \(a+b+c\equiv 0\pmod N\) — the first genuinely information-geometric and arithmetic layer.

**Harvest.** [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s square-root sphere gains a dual simplex from reciprocal closure; [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s log-partition tower gains a softmax/softmin mirror; [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s radical arithmetic gains a denominator-arithmetic counterpart through lcm support and \(p\)-adic reciprocal sums. The thesis:

\[
\boxed{\text{harmony is the simplicial ladder viewed through reciprocal closure.}}
\]

**Keywords:** harmonic mean, reciprocal closure, simplicial coordinates, positive cone, Helmert coordinates, power means, cumulants, softmax/softmin, Fisher–Rao geometry, conductor packets, denominator arithmetic, \(p\)-adic valuation.

---

## 0. The missing reciprocal face

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) ended with a gauge machine.

Additive ledgers use arithmetic mean removal:

\[
q\mapsto q-\bar q\mathbf 1.
\]

Positive ledgers use geometric mean removal:

\[
x_i\mapsto \frac{x_i}{G(x)}.
\]

Taking logs turns the second operation into the first:

\[
\log\frac{x_i}{G(x)}
=\log x_i-\frac1N\sum_j\log x_j.
\]

So geometric mean entered [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) not as a decorative average, but as the multiplicative gauge that lands in the same mean-zero space.

But the classical chain is

\[
H(x)\le G(x)\le A(x).
\]

If \(A\) and \(G\) have already become structural, \(H\) should not be left behind as a numerical afterthought.

The harmonic mean is

\[
H(x)=\frac{N}{\sum_i x_i^{-1}}.
\]

That definition is already telling us what to do:

\[
\boxed{
H(x)^{-1}=A(x^{-1}).
}
\]

The harmonic mean is the arithmetic mean seen after reciprocal inversion.

This is the door [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) opens.

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) through [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) mostly asked what happens when probability mass, log weight, and Euclidean measurement are carried through the native simplicial chart. [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) asks what happens when the observable is naturally reciprocal before it ever becomes a probability.

That is the world of rates and periods, resistance and conductance, cost and capacity, latency and throughput, denominators and divisibility, bottlenecks and rare events.

The reciprocal observer is not an optional second opinion. It sees the boundary from the other side.

---

## Notation

- \(\mathbb R_{>0}^N\): positive \(N\)-slot ledger.
- \(\mathbf 1_N\): the all-ones vector.
- \(H_N\): mean-zero hyperplane \(\{q\in\mathbb R^N:\sum_i q_i=0\}\); same object denoted \(H_0\) in [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049), renamed to match [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504). (Distinct from the harmonic mean \(H(x)\), the partial harmonic mean \(H_k\), and the conductor-packet symbol \(H_d\) of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049); disambiguated by argument and index.)
- \(A(x)\): arithmetic mean, \(A(x)=\frac1N\sum_i x_i\).
- \(G(x)\): geometric mean, \(G(x)=(\prod_i x_i)^{1/N}\).
- \(H(x)\): harmonic mean, \(H(x)=N/\sum_i x_i^{-1}\).
- \(R(x)\): reciprocal involution, \(R(x)_i=x_i^{-1}\).
- \(\operatorname{cl}(w)\): closure by sum, \(\operatorname{cl}(w)_i=w_i/\sum_j w_j\).
- \(p^\vee\): reciprocal-closed or harmonic-dual probability, \(p^\vee=\operatorname{cl}(x^{-1})\).
- \(h_k\): unnormalized Helmert vector \((1,\ldots,1,-k,0,\ldots,0)\).
- \(e_k\): unit Helmert vector \(h_k/\sqrt{k(k+1)}\).
- \(A_k,G_k,H_k\): means of the first \(k\) entries \(x_1,\ldots,x_k\).
- \(y\): centered log-ledger, \(y_i=\log x_i-\frac1N\sum_j\log x_j\).
- \(K_y(t)\): directional log-partition, \(K_y(t)=\log(\frac1N\sum_i e^{t y_i})\).
- \(\kappa_n\): \(n\)-th cumulant of the values \(y_i\) under the uniform measure.

---

## 1. Three gauges on the positive cone

Let

\[
x=(x_1,\ldots,x_N)\in\mathbb R_{>0}^N.
\]

The positive cone has a shared-scale action:

\[
x\mapsto c x,\qquad c>0.
\]

The projective object is the ray

\[
[x]=\{c x:c>0\}.
\]

A gauge is a rule that chooses one representative from each positive ray.

There are three natural gauge sections:

\[
\mathcal A_N=\{x:A(x)=1\}
=\left\{x:\sum_i x_i=N\right\},
\]

\[
\mathcal G_N=\{x:G(x)=1\}
=\left\{x:\prod_i x_i=1\right\},
\]

and

\[
\mathcal H_N=\{x:H(x)=1\}
=\left\{x:\sum_i x_i^{-1}=N\right\}.
\]

Each positive ray intersects each section exactly once:

\[
x\mapsto \frac{x}{A(x)},\qquad
x\mapsto \frac{x}{G(x)},\qquad
x\mapsto \frac{x}{H(x)}.
\]

The first is primal affine. The second is log affine. The third is reciprocal affine.

### Proposition 1.1. Arithmetic and harmonic gauges are reciprocal partners

The reciprocal involution

\[
R(x)_i=x_i^{-1}
\]

exchanges the arithmetic and harmonic sections:

\[
R(\mathcal A_N)=\mathcal H_N,
\qquad
R(\mathcal H_N)=\mathcal A_N.
\]

The geometric section is fixed as a set:

\[
R(\mathcal G_N)=\mathcal G_N.
\]

**Proof.** If \(A(x)=1\), then \(\sum_i x_i=N\). For \(z=R(x)\),

\[
\sum_i z_i^{-1}=\sum_i x_i=N,
\]

so \(z\in\mathcal H_N\). The reverse implication is the same calculation applied twice, since \(R^2=\mathrm{id}\).

If \(G(x)=1\), then

\[
G(R(x))=\left(\prod_i x_i^{-1}\right)^{1/N}
=G(x)^{-1}=1.
\]

\(\square\)

This is the first structural fact.

\[
\boxed{
A \text{ and } H \text{ are polar partners; } G \text{ is self-dual.}
}
\]

The harmonic mean is not below the geometric mean because it is inferior. It is below because it lives on the reciprocal side of the cone.

---

## 2. Harmonic closure and the dual simplex

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) begins with the probability simplex:

\[
\Delta^{N-1}=\left\{p\in\mathbb R_{\ge0}^N:\sum_i p_i=1\right\}.
\]

Any positive ledger \(x\) determines a primal probability by ordinary closure:

\[
p_i=\operatorname{cl}(x)_i
=\frac{x_i}{\sum_j x_j}.
\]

Harmonic mean gives a second probability:

\[
p_i^\vee
=\operatorname{cl}(x^{-1})_i
=\frac{x_i^{-1}}{\sum_j x_j^{-1}}.
\]

Since

\[
H(x)=\frac{N}{\sum_j x_j^{-1}},
\]

we can write

\[
\boxed{
p_i^\vee=\frac{H(x)}{N x_i}.
}
\]

Thus harmonic gauge removal

\[
z_i=\frac{x_i}{H(x)}
\]

is equivalent to ordinary simplex closure of the reciprocal coordinates, because

\[
z_i^{-1}=\frac{H(x)}{x_i}=N p_i^\vee,
\]

and therefore

\[
\sum_i z_i^{-1}=N.
\]

The harmonic section is the inverse image of the ordinary mean-one simplex under reciprocal inversion.

### Definition 2.1. Reciprocal closure

For \(p\in\Delta^{N-1}\) with all \(p_i>0\), define

\[
p^\vee_i
=\frac{p_i^{-1}}{\sum_j p_j^{-1}}.
\]

We call \(p^\vee\) the reciprocal closure, or harmonic dual, of \(p\).

### Proposition 2.2. Reciprocal closure is an involution

For every interior simplex point \(p\),

\[
(p^\vee)^\vee=p.
\]

**Proof.** Let \(S=\sum_j p_j^{-1}\). Then

\[
p_i^\vee=\frac{p_i^{-1}}{S}.
\]

Taking reciprocals gives

\[
(p_i^\vee)^{-1}=S p_i.
\]

Closing again by sum,

\[
(p^\vee)^\vee_i
=\frac{S p_i}{\sum_j S p_j}
=p_i.
\]

\(\square\)

So reciprocal closure is a genuine symmetry of the open simplex. It is not linear, and it does not preserve the flat mixture geometry globally. But it fixes the uniform point

\[
u=\left(\frac1N,\ldots,\frac1N\right),
\]

and its first-order action is simple.

### Proposition 2.3. At the uniform, reciprocal closure is antipodal on \(H_N\)

Let \(v\in H_N\), so \(\sum_i v_i=0\), and set

\[
p(\varepsilon)=u+\varepsilon v.
\]

Then

\[
p(\varepsilon)^\vee
=u-\varepsilon v
+\varepsilon^2\left(N v_i^2-\|v\|^2\right)_{i=1}^N
+O(\varepsilon^3).
\]

In particular,

\[
D(p\mapsto p^\vee)_u=-\mathrm{id}_{H_N}.
\]

**Proof.** Since \(u_i=1/N\),

\[
p_i(\varepsilon)^{-1}
=\frac{N}{1+N\varepsilon v_i}
=N\left(1-N\varepsilon v_i+N^2\varepsilon^2v_i^2+O(\varepsilon^3)\right).
\]

Summing over \(i\) and using \(\sum_i v_i=0\),

\[
\sum_i p_i(\varepsilon)^{-1}
=N^2+N^3\varepsilon^2\sum_i v_i^2+O(\varepsilon^3).
\]

Dividing numerator by denominator gives

\[
p_i(\varepsilon)^\vee
=\frac1N-\varepsilon v_i
+\varepsilon^2\left(Nv_i^2-\sum_jv_j^2\right)
+O(\varepsilon^3).
\]

\(\square\)

This is the [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) statement in reciprocal form:

\[
\boxed{
\text{near the uniform, harmonic duality is central inversion on the mean-zero space.}
}
\]

The first-order geometry is the same \(H_N\). The second-order correction is where reciprocal curvature enters.

---

## 3. The three Helmert readings

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s ladder vector is

\[
h_k=(1,\ldots,1,-k,0,\ldots,0),
\qquad
1\le k<N,
\]

with \(k\) leading \(1\)s, a single \(-k\) at position \(k+1\), and \(N-k-1\) trailing zeros. Its unit version is

\[
e_k=\frac{h_k}{\sqrt{k(k+1)}}.
\]

The same vector can query \(x\), \(\log x\), or \(x^{-1}\).

Let

\[
A_k=A(x_1,\ldots,x_k),
\]

\[
G_k=G(x_1,\ldots,x_k),
\]

and

\[
H_k=H(x_1,\ldots,x_k).
\]

Then:

\[
e_k\cdot x
=\sqrt{\frac{k}{k+1}}\left(A_k-x_{k+1}\right),
\]

\[
e_k\cdot \log x
=\sqrt{\frac{k}{k+1}}
\log\frac{G_k}{x_{k+1}},
\]

and

\[
e_k\cdot x^{-1}
=\sqrt{\frac{k}{k+1}}
\left(\frac1{H_k}-\frac1{x_{k+1}}\right).
\]

### Proposition 3.1. One integer ladder, three gauges

The Helmert ladder has the following three gauge readings:

\[
\boxed{
\text{arithmetic balance}
=
\text{difference of arithmetic centers};
}
\]

\[
\boxed{
\text{geometric balance}
=
\text{log-ratio of geometric centers};
}
\]

\[
\boxed{
\text{harmonic balance}
=
\text{difference of reciprocal harmonic centers}.
}
\]

**Proof.** Direct contraction gives

\[
h_k\cdot x
=\sum_{i=1}^k x_i-kx_{k+1}
=k(A_k-x_{k+1}).
\]

Dividing by \(\sqrt{k(k+1)}\) gives the arithmetic formula.

For logs,

\[
h_k\cdot\log x
=\sum_{i=1}^k\log x_i-k\log x_{k+1}
=k\log\frac{G_k}{x_{k+1}}.
\]

For reciprocals,

\[
h_k\cdot x^{-1}
=\sum_{i=1}^k\frac1{x_i}-\frac{k}{x_{k+1}}
=k\left(\frac1{H_k}-\frac1{x_{k+1}}\right).
\]

Again divide by \(\sqrt{k(k+1)}\). \(\square\)

This is the harmonic ladder in its simplest form.

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) found:

\[
\text{sequential log-ratio balance}
=
\text{geometric mean of the past versus the next part}.
\]

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) adds:

\[
\begin{aligned}
\text{sequential reciprocal balance}
&=\text{harmonic mean of the past}\\
&\quad\text{versus the next part, in reciprocal units}.
\end{aligned}
\]

The integer incidence skeleton has not changed. The observer changed.

---

## 4. Softmax, softmin, and the cumulant mirror

Now pass to log coordinates.

Let

\[
y_i=\log x_i-\log G(x).
\]

Then

\[
\sum_i y_i=0,
\qquad
G(e^y)=1.
\]

Define the directional log-partition

\[
K_y(t)=\log\left(\frac1N\sum_i e^{t y_i}\right).
\]

This is [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s categorical log-partition restricted to the one-dimensional direction \(y\), with the uniform base measure.

Since \(y\) is centered,

\[
K_y(0)=0,
\qquad
K_y'(0)=0.
\]

The derivatives

\[
\kappa_n=K_y^{(n)}(0)
\]

are the cumulants of the values \(y_1,\ldots,y_N\) under the uniform distribution.

### Proposition 4.1. Arithmetic and harmonic means are softmax and softmin

For any positive \(x\),

\[
\log\frac{A(x)}{G(x)}=K_y(1),
\]

and

\[
\log\frac{G(x)}{H(x)}=K_y(-1).
\]

**Proof.** Since \(x_i=G(x)e^{y_i}\),

\[
A(x)=G(x)\frac1N\sum_i e^{y_i},
\]

so

\[
\log\frac{A(x)}{G(x)}
=\log\left(\frac1N\sum_i e^{y_i}\right)
=K_y(1).
\]

Similarly,

\[
H(x)^{-1}
=\frac1N\sum_i x_i^{-1}
=G(x)^{-1}\frac1N\sum_i e^{-y_i}.
\]

Thus

\[
\frac{G(x)}{H(x)}
=\frac1N\sum_i e^{-y_i},
\]

and therefore

\[
\log\frac{G(x)}{H(x)}
=K_y(-1).
\]

\(\square\)

Arithmetic mean is the log-sum-exp of \(y\). Harmonic mean is the negative log-sum-exp of \(-y\). In machine-learning language:

\[
\boxed{
A/G \text{ is softmax size; } G/H \text{ is softmin size.}
}
\]

Geometric mean is the center because it subtracts the first cumulant.

### Theorem 4.2. The arithmetic-harmonic contrast separates even and odd cumulants

With \(y\), \(K_y\), and \(\kappa_n\) as above,

\[
\log\frac{A(x)}{H(x)}
=K_y(1)+K_y(-1)
=2\sum_{m\ge1}\frac{\kappa_{2m}}{(2m)!},
\]

and

\[
\log\frac{A(x)H(x)}{G(x)^2}
=K_y(1)-K_y(-1)
=2\sum_{m\ge1}\frac{\kappa_{2m+1}}{(2m+1)!}.
\]

The identities involving \(K_y(\pm1)\) are exact finite-dimensional identities. The displayed cumulant sums use the Taylor branch of \(K_y\) at \(0\); they are convergent when \(\pm1\) lies in that zero-free Taylor domain, and otherwise should be read as formal/local cumulant expansions.

In particular,

\[
\log\frac{A(x)H(x)}{G(x)^2}
=\frac{\kappa_3}{3}
+\frac{\kappa_5}{60}
+\frac{\kappa_7}{2520}
+\cdots.
\]

**Proof.** Since \(K_y(0)=K_y'(0)=0\),

\[
K_y(t)=\sum_{n\ge2}\frac{\kappa_n}{n!}t^n.
\]

By Proposition 4.1,

\[
\log\frac{A(x)}{H(x)}
=\log\frac{A(x)}{G(x)}
+\log\frac{G(x)}{H(x)}
=K_y(1)+K_y(-1).
\]

The odd powers cancel and the even powers double:

\[
K_y(1)+K_y(-1)
=2\sum_{m\ge1}\frac{\kappa_{2m}}{(2m)!}.
\]

Likewise,

\[
\log\frac{A(x)H(x)}{G(x)^2}
=\log\frac{A(x)}{G(x)}
-\log\frac{G(x)}{H(x)}
=K_y(1)-K_y(-1).
\]

The even powers cancel and the odd powers double:

\[
K_y(1)-K_y(-1)
=2\sum_{m\ge1}\frac{\kappa_{2m+1}}{(2m+1)!}.
\]

\(\square\)

This is the central theorem of [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419).

The ordinary chain

\[
H\le G\le A
\]

knows spread. But the pair \((A,H)\) around \(G\) knows parity.

\[
\boxed{
\log(A/H) \text{ is the even cumulant ledger.}
}
\]

\[
\boxed{
\log(AH/G^2) \text{ is the odd cumulant ledger.}
}
\]

The first even term is variance:

\[
\log\frac{A}{H}
=\kappa_2+O(\|y\|^4).
\]

The first odd term is cubic:

\[
\log\frac{AH}{G^2}
=\frac{\kappa_3}{3}+O(\|y\|^5).
\]

So [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) recovers the trilogy's load-bearing threshold by a scalar comparison of means.

[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) says: the third cumulant is the first invariant beyond the metric.

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) says: the third cumulant is the first obstruction to arithmetic and harmonic means sitting symmetrically around the geometric mean in log scale.

---

## 5. The conductor rule inside harmonic skew

Now give the index set the cyclic structure of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049):

\[
\{0,1,\ldots,N-1\}=\mathbb Z/N.
\]

Let

\[
\chi_a(r)=e^{2\pi i ar/N}
\]

be the additive characters, and expand a centered log-ledger as

\[
y(r)=\sum_{a\ne0}\widehat y_a\chi_a(r).
\]

The third cumulant under the uniform measure is

\[
\kappa_3
=\frac1N\sum_{r\in\mathbb Z/N}y(r)^3.
\]

Using character orthogonality,

\[
\frac1N\sum_{r\in\mathbb Z/N}
\chi_a(r)\chi_b(r)\chi_c(r)
=
\begin{cases}
1,&a+b+c\equiv0\pmod N,\\
0,&\text{otherwise}.
\end{cases}
\]

Therefore

\[
\kappa_3
=
\sum_{\substack{a,b,c\ne0\\a+b+c\equiv0\pmod N}}
\widehat y_a\widehat y_b\widehat y_c.
\]

Combining with Theorem 4.2 gives:

\[
\boxed{
\log\frac{A(x)H(x)}{G(x)^2}
=
\frac13
\sum_{\substack{a,b,c\ne0\\a+b+c\equiv0\pmod N}}
\widehat y_a\widehat y_b\widehat y_c
+O(\|y\|^5).
}
\]

This is [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s selection rule seen through harmonic mean.

The cubic vertex was previously a tensor:

\[
T(\chi_a,\chi_b,\chi_c)\ne0
\quad\Longleftrightarrow\quad
a+b+c\equiv0\pmod N.
\]

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) says the same rule controls the leading scalar asymmetry

\[
AH/G^2.
\]

This is a useful compression:

\[
\boxed{
\text{harmonic skew is a scalar detector of conductor-coupled cubic content.}
}
\]

The tensor is still the real object. The scalar is a witness.

---

## 6. Harmonic Fisher geometry

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) reads probability through square-root amplitudes:

\[
a_i=\sqrt{p_i}.
\]

The harmonic dual probability is

\[
p_i^\vee=\frac{x_i^{-1}}{\sum_jx_j^{-1}}.
\]

So the harmonic amplitude is

\[
a_i^\vee
=\sqrt{p_i^\vee}
=\sqrt{\frac{H(x)}{N x_i}}.
\]

This is just [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) applied after reciprocal closure.

The map

\[
x\mapsto a^\vee
\]

sends a positive ledger to the positive orthant of the unit sphere, but it weights small coordinates heavily. If \(x_i\) is tiny, \(p_i^\vee\) is large. If \(x_i\) is huge, \(p_i^\vee\) is small.

Thus harmonic Fisher geometry is the geometry of reciprocal salience.

In log coordinates \(y_i=\log x_i\), the dual probabilities are

\[
p_i^\vee(y)
=\frac{e^{-y_i}}{\sum_j e^{-y_j}}.
\]

This is softmax applied to \(-y\), i.e. softmin applied to \(y\).

Define the harmonic potential

\[
\Psi_H(y)=\log H(e^y).
\]

Up to the harmless constant \(\log N\),

\[
\Psi_H(y)
=-\log\sum_i e^{-y_i}.
\]

Therefore

\[
\frac{\partial \Psi_H}{\partial y_i}
=p_i^\vee(y).
\]

The Hessian is

\[
\frac{\partial^2 \Psi_H}{\partial y_i\partial y_j}
=-\left(\delta_{ij}p_i^\vee-p_i^\vee p_j^\vee\right).
\]

So \(\Psi_H\) is concave, and

\[
-\nabla^2\Psi_H
=\operatorname{diag}(p^\vee)-p^\vee p^{\vee T}
\]

is the Fisher information matrix of the dual distribution.

This is the [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) tower with signs alternating under reciprocal inversion:

\[
\boxed{
\text{harmonic geometry is the softmin cumulant tower.}
}
\]

The metric is familiar. The observer is reversed.

---

## 7. Denominator arithmetic

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) exposed a radical arithmetic.

The unit Helmert vectors require

\[
\sqrt{k(k+1)}.
\]

As \(N\) grows, these normalizers generate

\[
K_N=\mathbb Q(\sqrt p:p\le N,\ p\text{ prime}).
\]

Prime rungs are exactly the rungs where unit measurement forces a new quadratic generator.

Harmonic mean exposes a different arithmetic.

Let

\[
x_1,\ldots,x_N\in\mathbb Z_{>0}.
\]

Let

\[
L=\operatorname{lcm}(x_1,\ldots,x_N).
\]

Then

\[
\sum_i\frac1{x_i}
=\frac1L\sum_i\frac{L}{x_i}.
\]

Define

\[
D=\sum_i\frac{L}{x_i}.
\]

Then

\[
\boxed{
H(x)=\frac{N L}{D}.
}
\]

For every prime \(p\), as a rational valuation,

\[
v_p(H(x))=v_p(N)+v_p(L)-v_p(D).
\]

This is not the same arithmetic as [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s squarefree radical field.

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) asks:

\[
\text{which square roots are forced by unit length?}
\]

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) asks:

\[
\text{which denominators are forced by reciprocal summation?}
\]

Examples:

1. For \(x=(2,3,5)\),

\[
L=30,
\qquad
D=15+10+6=31,
\]

so

\[
H(x)=\frac{90}{31}.
\]

The prime \(31\) is not in the entries. It appears from the reciprocal sum.

2. For \(x=(6,10,15)\),

\[
L=30,
\qquad
D=5+3+2=10,
\]

so

\[
H(x)=\frac{3\cdot30}{10}=9.
\]

Here the reciprocal denominator cancels completely.

3. For \(x=(2,4,8)\),

\[
L=8,
\qquad
D=4+2+1=7,
\]

so

\[
H(x)=\frac{24}{7}.
\]

A dyadic ladder produces a denominator \(7\), because reciprocal addition creates a Mersenne-like residue.

This is the harmonic arithmetic:

\[
\boxed{
\text{lcm support plus additive reciprocal cancellation.}
}
\]

The primes in [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) are field generators. The primes in [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) are denominator obstructions.

They are not the same clock. They are dual clocks.

---

## 8. Bin centers and reciprocal measurement

An empirical clue from histogram analysis: the harmonic mean can be the right center value inside bin boundaries.

This is exactly what the gauge story predicts.

Let a bin have endpoints

\[
0<a<b.
\]

A center is not absolute. A center is the pullback of an affine midpoint in the coordinate where the bin is linear.

If the linear coordinate is \(x\), then

\[
c_A=\frac{a+b}{2}.
\]

If the linear coordinate is \(\log x\), then

\[
c_G=\exp\left(\frac{\log a+\log b}{2}\right)
=\sqrt{ab}.
\]

If the linear coordinate is \(1/x\), then

\[
\frac1{c_H}
=\frac12\left(\frac1a+\frac1b\right),
\]

so

\[
c_H=\frac{2ab}{a+b}.
\]

That is the harmonic mean.

Thus the harmonic bin center is correct when the bin is flat in reciprocal coordinate.

This happens whenever the additive quantity is not \(x\), but \(1/x\): period versus frequency, resistance versus conductance, latency versus throughput, cost versus capacity.

The moral is:

\[
\boxed{
\text{choosing a mean is choosing the affine coordinate of observation.}
}
\]

Arithmetic says \(x\) is affine.

Geometric says \(\log x\) is affine.

Harmonic says \(1/x\) is affine.

---

## 9. What [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) adds to [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) through [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)

The previous papers handed forward four structures:

| Paper | Object | What it exposed |
|---|---|---|
| [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) | Native simplicial chart | Probability as a simplex, Fisher-Rao as square-root sphere geometry. |
| [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) | \(\Phi=\log Z\) | The cumulant tower: position, metric, cubic vertex, closure defects. |
| [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) | Character basis of \(\mathbb Z/N\) | Conductor packets and the cubic selection rule. |
| [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) | Helmert residue ladder | Mean removal, geometric gauge, and prime radical rungs. |

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) adds:

| Paper | Object | What it exposes |
|---|---|---|
| [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) | Harmonic reciprocal gauge | Reciprocal closure, softmin geometry, odd/even cumulant splitting, and denominator arithmetic. |

The contrast is precise.

### Against [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) says:

\[
p_i=a_i^2
\]

turns the simplex into the positive orthant of a sphere.

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) says:

\[
p_i^\vee=\frac{p_i^{-1}}{\sum_jp_j^{-1}},
\qquad
a_i^\vee=\sqrt{p_i^\vee},
\]

does the same after reciprocal closure.

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) sees mass. [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) sees reciprocal salience.

Near the uniform, reciprocal closure is just \(-\mathrm{id}\) on \(H_N\). Away from the uniform, it bends toward the boundary and reverses dominance: small primal coordinates become large dual coordinates.

### Against [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)

[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) says:

\[
\Phi(y)=\log\sum_i e^{y_i}
\]

generates the categorical cumulant tower.

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) says the two sides of the mean triad are

\[
\log(A/G)=K_y(1),
\qquad
\log(G/H)=K_y(-1).
\]

So arithmetic and harmonic means sample the same cumulant generator at opposite temperatures.

Even cumulants measure the total \(A/H\) spread.

Odd cumulants measure the asymmetry of \(A\) and \(H\) around \(G\).

The cubic is the first harmonic skew.

### Against [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)

[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) says the cubic tensor in the character basis obeys

\[
a+b+c\equiv0\pmod N.
\]

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) says this same selection rule is the leading term of

\[
\log(AH/G^2).
\]

The tensor selection rule becomes a scalar skew detector.

### Against [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) says the geometric mean is multiplicative gauge removal:

\[
x\mapsto x/G(x).
\]

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) says the harmonic mean is reciprocal gauge removal:

\[
x\mapsto x/H(x),
\qquad
\sum_i \left(\frac{x_i}{H(x)}\right)^{-1}=N.
\]

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s normalized ladder exposes radical residue:

\[
\sqrt{k(k+1)}
\quad\leadsto\quad
\mathbb Q(\sqrt p:p\le N).
\]

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)'s reciprocal ledger exposes denominator residue:

\[
H(x)=\frac{N\operatorname{lcm}(x_i)}
{\sum_i\operatorname{lcm}(x_i)/x_i}.
\]

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) is square classes. [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) is reciprocal sums.

Together:

\[
\boxed{
\begin{gathered}
\text{Radical arithmetic and denominator arithmetic}\\
\text{are the two number-theoretic shadows of measurement choice.}
\end{gathered}
}
\]

---

## 10. The power-mean corridor

The three means are not isolated. They sit inside the power-mean family:

\[
M_r(x)=\left(\frac1N\sum_i x_i^r\right)^{1/r},
\qquad r\ne0,
\]

with

\[
M_0(x)=G(x).
\]

In log coordinates \(y_i=\log x_i\),

\[
\log M_r(e^y)
=\frac1r\log\left(\frac1N\sum_i e^{r y_i}\right).
\]

Thus

\[
\log\frac{M_r(x)}{G(x)}
=\frac1r K_y(r).
\]

The derivative with respect to \(y_i\) is

\[
\frac{\partial}{\partial y_i}\log M_r(e^y)
=\frac{e^{r y_i}}{\sum_j e^{r y_j}}.
\]

These are escort probabilities:

\[
p_i^{(r)}
=\frac{x_i^r}{\sum_j x_j^r}.
\]

The three special values are

\[
r=1:\quad p_i^{(1)}=\frac{x_i}{\sum_jx_j}
\quad\text{ordinary closure},
\]

\[
r=0:\quad p_i^{(0)}=\frac1N
\quad\text{geometric center},
\]

\[
r=-1:\quad p_i^{(-1)}=\frac{x_i^{-1}}{\sum_jx_j^{-1}}
\quad\text{reciprocal closure}.
\]

This corridor reframes the program:

\[
\boxed{
\text{arithmetic and harmonic are opposite escort observers; geometric is the neutral observer.}
}
\]

Positive \(r\) emphasizes large coordinates. Negative \(r\) emphasizes small coordinates. The limit \(r=0\) forgets magnitude and remembers only the log-gauge center.

The harmonic mean is not the end of the story. It is the first full step into the negative-temperature side of the gauge family.

---

## 11. Theorems and forward program

The results above opened several doors. Some are theorem-level consequences of the cumulant expansion; the remaining items are forward problems for the harmonic gauge.

### Theorem 11.1. Harmonic skew is the odd-cumulant detector

For centered log-ledgers \(y\), define

\[
\mathcal S_H(y)=\log\frac{A(e^y)H(e^y)}{G(e^y)^2}.
\]

Then

\[
\mathcal S_H(y)
=\log\frac{A(e^y)H(e^y)}{G(e^y)^2}
=K_y(1)-K_y(-1)
=2\sum_{m\ge0}\frac{\kappa_{2m+1}}{(2m+1)!}.
\]

Since \(y\) is centered, \(\kappa_1=0\), and the leading term is

\[
\mathcal S_H(y)=\frac13 T(y,y,y)+O(\|y\|^5),
\]

where \(T\) is the Amari-Chentsov cubic tensor at the uniform.

**Proof.** Theorem 4.2 gives

\[
\log\frac{A(e^y)H(e^y)}{G(e^y)^2}=K_y(1)-K_y(-1).
\]

Expanding \(K_y(t)=\sum_{n\ge1}\kappa_n t^n/n!\) and subtracting the value at \(-t\) cancels the even cumulants and doubles the odd cumulants. Since \(y\) is centered, \(\kappa_1=0\). At the uniform, the third cumulant is the cubic tensor \(T\), so \(\kappa_3=T(y,y,y)\). \(\square\)

Thus the harmonic skew is not only a diagnostic candidate. It is the scalar odd-cumulant detector selected by the arithmetic-harmonic pair.

### Theorem 11.2. Power-pair parity along the escort corridor

For the escort family

\[
p_i^{(r)}=\frac{x_i^r}{\sum_jx_j^r},
\]

the local Taylor expansion of \(K_y(r)\) at \(r=0\) satisfies

\[
K_y(r)+K_y(-r)=2\sum_{m\ge1}\frac{\kappa_{2m}r^{2m}}{(2m)!},
\]

and

\[
K_y(r)-K_y(-r)=2\sum_{m\ge0}\frac{\kappa_{2m+1}r^{2m+1}}{(2m+1)!}.
\]

The pair \(r=\pm1\) is the harmonic pair: arithmetic and harmonic closure are opposite escort observers, with the geometric gauge at \(r=0\).

**Proof.** Write

\[
K_y(r)=\sum_{n\ge1}\frac{\kappa_n r^n}{n!}
\]

as a local Taylor series around \(r=0\). Adding the series at \(r\) and \(-r\) cancels odd powers; subtracting them cancels even powers. The centered condition gives \(\kappa_1=0\), but the displayed odd formula is written in the uniform parity form. \(\square\)

### Forward Problem 11.3. Denominator-conductor dictionary

The conductor packets of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) classify additive character support by divisors \(d\mid N\). The Fourier-Mellin framing supplies this conductor side of the dictionary. The harmonic arithmetic of [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) classifies reciprocal ledgers by lcm support and denominator residues

\[
D=\sum_i\frac{L}{x_i}.
\]

The open problem is to describe a packet-level relation between:

1. additive conductor packets in cyclic label space; and
2. \(p\)-adic behavior of reciprocal sums over those packets.

The dictionary is not equality, and the conductor side alone does not determine reciprocal denominators. The open part is to relate mode support to local denominator obstruction without collapsing additive Fourier data and \(p\)-adic reciprocal data into the same object.

### Remark 11.4. No denominator oracle claim

The lcm support and \(p\)-adic bottlenecks exposed by harmonic normalization are structural diagnostics, not a promised faster factorization method or denominator sieve. Their value is representational: they show where reciprocal closure makes local denominator obstruction visible inside the simplicial ledger.

### Forward Problem 11.5. Reciprocal closure and alpha-connections

Proposition 2.3 proves that reciprocal closure acts as \(-\mathrm{id}_{H_N}\) at the uniform. Globally, if

\[
y_i=\log p_i-\frac1N\sum_j\log p_j,
\]

then reciprocal closure gives \(C(p)_i\propto p_i^{-1}\propto e^{-y_i}\), so the centered log-ledger of \(C(p)\) is \(-y\). Hence cumulants transform by

\[
\kappa_n(C(p))=(-1)^n\kappa_n(p).
\]

The remaining problem is not this parity statement, but its connection-theoretic meaning: express reciprocal closure cleanly in the \(\alpha\)-connection family of information geometry, ideally as an exchange between the \(+\alpha\) and \(-\alpha\) viewpoints after an appropriate gauge change.

### Forward Problem 11.6. Harmonic ladders for reciprocal networks

Whenever the natural composition law is reciprocal, the harmonic Helmert ladder should be tested as the correct balance system.

Candidates include parallel resistances, throughput bottlenecks, latency aggregation, frequency-period duality, and rates in renewal processes.

The test is simple: if \(1/x\) is additive, use the harmonic ladder.

### Forward Problem 11.7. Negative escort arithmetic

Theorem 11.2 settles the parity decomposition of the escort corridor. The negative integer samples also have a settled selection-rule interpretation: the sample \(r=-m\) is the positive \(m\)-closure of the reciprocal ledger \(u_i=1/x_i\), so its modular convolution rule is the positive rule applied to \(\widehat u\), not a new polynomial rule in \(\widehat x\).

The unresolved arithmetic question is what happens to denominator, radical, and support data as the gauge sample crosses \(r=0\).

Positive \(r\) amplifies numerator support. Negative \(r\) amplifies denominator support. The neutral sample \(r=0\) erases both into the uniform log-gauge center.

The forward problem is to describe this transition in a way that relates radical residues, denominator residues, and entropy-like escort flows without collapsing their distinct arithmetic roles.

---

## 12. Worked example: the [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) ledger through the harmonic lens

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) used

\[
x=(2,3,4,5).
\]

The arithmetic mean is

\[
A(x)=\frac{2+3+4+5}{4}=\frac72.
\]

The geometric mean is

\[
G(x)=(2\cdot3\cdot4\cdot5)^{1/4}=120^{1/4}.
\]

The harmonic mean is

\[
H(x)
=\frac4{\frac12+\frac13+\frac14+\frac15}
=\frac4{77/60}
=\frac{240}{77}.
\]

So

\[
\frac{A}{H}
=\frac{7/2}{240/77}
=\frac{539}{480}.
\]

This is the even cumulant spread.

The harmonic skew is

\[
\frac{AH}{G^2}
=
\frac{(7/2)(240/77)}{\sqrt{120}}
=
\frac{840}{77\sqrt{120}}.
\]

It is close to \(1\), meaning that \(A\) and \(H\) sit nearly symmetrically around \(G\) on log scale for this ledger.

Now apply the first harmonic Helmert balance.

For \(k=1\),

\[
e_1=\frac{(1,-1,0,0)}{\sqrt2},
\]

and

\[
e_1\cdot x^{-1}
=\frac1{\sqrt2}\left(\frac12-\frac13\right)
=\frac1{6\sqrt2}.
\]

For \(k=2\),

\[
H_2=H(2,3)=\frac{12}{5},
\]

and

\[
e_2\cdot x^{-1}
=\sqrt{\frac23}\left(\frac1{H_2}-\frac14\right)
=\sqrt{\frac23}\left(\frac5{12}-\frac14\right)
=\frac16\sqrt{\frac23}.
\]

For \(k=3\),

\[
H_3=H(2,3,4)=\frac{36}{13},
\]

and

\[
e_3\cdot x^{-1}
=\sqrt{\frac34}\left(\frac1{H_3}-\frac15\right)
=\frac{\sqrt3}{2}\left(\frac{13}{36}-\frac15\right)
=\frac{29\sqrt3}{360}.
\]

The same ledger that [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) reconstructed by arithmetic mean packets now has a reciprocal balance packet. The coordinates are small because the entries are not far apart reciprocally.

If one entry were near zero, the harmonic packet would flare immediately.

That is its job.

---

## 13. Coda

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) said:

\[
\text{do not delete the redundant coordinate.}
\]

[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) said:

\[
\text{one scalar functional generates the tower.}
\]

[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) said:

\[
\text{the cubic vertex is where arithmetic first speaks.}
\]

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) said:

\[
\text{do not normalize the ladder too early.}
\]

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) says:

\[
\boxed{
\text{do not decide too early which side of a quantity is primal.}
}
\]

If \(x\) is primal, arithmetic mean is the affine gauge.

If \(\log x\) is primal, geometric mean is the affine gauge.

If \(1/x\) is primal, harmonic mean is the affine gauge.

The triad is not a list of averages. It is a coordinate theorem:

\[
\begin{array}{ccl}
x &\longrightarrow& A,\\
\log x &\longrightarrow& G,\\
x^{-1} &\longrightarrow& H.
\end{array}
\]

The geometric mean is the mirror. Arithmetic and harmonic are the two sides.

Through that mirror, the old trilogy reappears in new form:

\[
\text{square-root sphere}
\quad\leftrightarrow\quad
\text{dual square-root sphere},
\]

\[
\text{softmax}
\quad\leftrightarrow\quad
\text{softmin},
\]

\[
\text{cubic tensor}
\quad\leftrightarrow\quad
\text{harmonic skew},
\]

\[
\text{radical residues}
\quad\leftrightarrow\quad
\text{denominator residues}.
\]

The harmonic mean therefore does not merely join the program.

It turns the program around.

And from the other side, the same simplicial object is still there:

\[
H_N,
\qquad
h_k,
\qquad
\Phi,
\qquad
a+b+c\equiv0,
\qquad
\sqrt{k(k+1)}.
\]

Only the observer changed.

That is the harmony.

---

## Acknowledgments

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) during the development of this paper. The collaborations were intellectually substantive: AI partners contributed insights, proposed theorems and conjectures, surfaced relevant literature, verified derivations, and iterated on exposition. I acknowledge this use transparently; the selection of which contributions to keep and the responsibility for the mathematical content are mine.

---

## References and Anchors

- Murillo Montero, L. (2026). *[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) — Identifying 3: The Native Simplicial Chart.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20336872](https://doi.org/10.5281/zenodo.20336872).
- Murillo Montero, L. (2026). *[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) — Identifying 3: The Cumulant Tower as Effective Action.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20338126](https://doi.org/10.5281/zenodo.20338126).
- Murillo Montero, L. (2026). *[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — Identifying 3: Character Orthogonality on the Conductor Lattice.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20339049](https://doi.org/10.5281/zenodo.20339049).
- Murillo Montero, L. (2026). *[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) — The Helmert-Simplicial Residue Ladder.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20383504](https://doi.org/10.5281/zenodo.20383504).
- Murillo Montero, L. (2026). *[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) — The Harmonic-Simplicial Dual Gauge.* Zenodo preprint (this work; concept DOI, resolves to latest version), DOI [10.5281/zenodo.20388419](https://doi.org/10.5281/zenodo.20388419).
- Helmert, F. R. (1876). *Die Genauigkeit der Formel von Peters zur Berechnung des wahrscheinlichen Beobachtungsfehlers directer Beobachtungen gleicher Genauigkeit.* Astronomische Nachrichten, 88, 113–132. [Wikipedia: Helmert transformation](https://en.wikipedia.org/wiki/Helmert_transformation).
- Aitchison, J. (1986). *The Statistical Analysis of Compositional Data.* Monographs on Statistics and Applied Probability. London: Chapman and Hall. ISBN 978-0-412-28060-3. Reprinted 2003 by Blackburn Press. [DOI: 10.1007/978-94-009-4109-0](https://doi.org/10.1007/978-94-009-4109-0).
- Hardy, G. H., Littlewood, J. E., and Pólya, G. (1934). *Inequalities.* Cambridge: Cambridge University Press. 2nd ed., 1952; Cambridge Mathematical Library reissue, 1988. ISBN 978-0-521-35880-4. (Chapters II–III on the power-mean inequalities and the \(A \ge G \ge H\) chain.)
- Pawlowsky-Glahn, V., Egozcue, J. J., and Tolosana-Delgado, R. (2015). *Modeling and Analysis of Compositional Data.* Statistics in Practice. Chichester: John Wiley & Sons. ISBN 978-1-118-44306-4. [DOI: 10.1002/9781119003144](https://doi.org/10.1002/9781119003144).
- Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry.* Translations of Mathematical Monographs, Vol. 191. Providence, RI: American Mathematical Society. ISBN 978-0-8218-0531-2. [AMS page](https://bookstore.ams.org/mmono-191).
- Serre, J.-P. (1973). *A Course in Arithmetic.* Graduate Texts in Mathematics, Vol. 7. New York: Springer-Verlag. ISBN 978-0-387-90040-7. [DOI: 10.1007/978-1-4684-9884-4](https://doi.org/10.1007/978-1-4684-9884-4).
- Boyd, S. and Vandenberghe, L. (2004). *Convex Optimization.* Cambridge: Cambridge University Press. ISBN 978-0-521-83378-3. (§3.1.5 on log-sum-exp / softmax as the standard cumulant generator viewpoint.) [Free PDF](https://web.stanford.edu/~boyd/cvxbook/).
- Tsallis, C. (2009). *Introduction to Nonextensive Statistical Mechanics: Approaching a Complex World.* New York: Springer. ISBN 978-0-387-85358-1. (Escort distributions \(p^{(r)}\) and their \(r\)-deformed entropies.) [DOI: 10.1007/978-0-387-85359-8](https://doi.org/10.1007/978-0-387-85359-8).
