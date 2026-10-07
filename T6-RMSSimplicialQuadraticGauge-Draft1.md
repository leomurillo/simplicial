# \heb{ל}6 — The RMS-Simplicial Quadratic Gauge

**Leonardo Murillo Montero**

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 24, 2026*

## Abstract

**Situation.** The first five papers handed forward five structures: [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s native simplicial chart and square-root sphere reading of Fisher–Rao; [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126)'s scalar generator \(\Phi=\log Z\) and its cumulant tower; [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s cubic character selection rule \(a+b+c\equiv 0\pmod N\) on \(\mathbb Z/N\); [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s Helmert residue ladder, with the prime radical field clock \(K_N=\mathbb Q(\sqrt p:p\le N)\); and [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)'s harmonic reciprocal gauge, with \(A\) and \(H\) as polar partners around the self-dual \(G\).

**Gap.** The root-mean-square had been hiding in plain sight since [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872): the square-root sphere, the \(2\arccos\) Fisher–Rao distance, and the \(\sqrt{k(k+1)}\) Helmert normalizers are all \(L^2\)-phenomena. RMS is not a fifth average — it is the gauge of *squared substance*.

**Surprise.** RMS is the common mechanism behind both [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) and [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504). On the positive cone it gives Born closure; on the mean-zero Helmert ladder it gives the unit balances:

\[
p_i=\frac{x_i^2}{\sum_j x_j^2},\qquad e_k=\frac{h_k}{\sqrt{k(k+1)}}.
\]

The amplitude sphere and the radical ladder are two restrictions of one operation:

\[
\boxed{L^2\text{-normalize the ray.}}
\]

**Action.** We formalize RMS as the quadratic gauge \(R(x)=\sqrt{\tfrac1N\sum_i x_i^2}\) with section \(\sum_i z_i^2=N\), and prove five results:

1. **Quadratic Gauge Theorem.** For amplitude-like ledgers (positive ray, additive quadratic mass), RMS is the unique canonical gauge, with closure \(p_i\propto x_i^2\) and projective angle \(d_{FR}(p,q)=2\arccos\frac{x\cdot y}{\|x\|\|y\|}\).
2. **Power-Pair Parity Theorem.** The pair \((M_r,M_{-r})\) splits \(K_y(r)\) into even and odd cumulant ledgers; RMS is the \(r=2\) case.
3. **RMS–Conductor Mixing Theorem.** Square closure is quadratic convolution in the character basis: conductor packets mix by the selection rule \(a+b-c\equiv 0\pmod N\).
4. **RMS Radical Universality Theorem.** For \(N\ge 4\), RMS normalization of integer amplitude ledgers realizes every quadratic field \(\mathbb Q(\sqrt d)\); for \(N=2,3\) the missing fields are exactly the classical sum-of-squares obstructions.
5. **Born–Helmert Bridge Theorem.** The amplitude sphere and the unit Helmert ladder are the positive and centered faces of one \(L^2\)-normalization principle.

**Harvest.** The trilogy located the cubic as the first layer beyond Riemannian geometry; [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) hid primes inside \(\sqrt{k(k+1)}\); [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) turned harmonic skew into a scalar witness of odd cumulants. [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) names why the factor \(2\arccos\) was always meaningful: RMS lifts nonnegative coordinates onto amplitude rays, and Fisher–Rao distance is twice their spherical angle. The thesis:

\[
\boxed{\text{RMS is the gauge of amplitudes; amplitudes square into probability.}}
\]

**Keywords:** root mean square, RMS, quadratic gauge, Born rule, square closure, Fisher–Rao distance, \(2\arccos\), amplitude sphere, Helmert coordinates, radical fields, conductor packets, power means, cumulants, sum of squares, Lagrange four-square theorem.

---

## 0. The quadratic mean after harmony

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) completed the arithmetic-geometric-harmonic triad:

\[
A:\ x \text{ is affine},
\]

\[
G:\ \log x \text{ is affine},
\]

\[
H:\ x^{-1} \text{ is affine}.
\]

RMS asks a different question.

What if \(x\) is not mass, scale, or reciprocal cost?

What if \(x\) is amplitude?

Then the additive substance is not \(x\). It is \(x^2\).

The root-mean-square is

\[
R(x)=\sqrt{\frac1N\sum_i x_i^2}.
\]

Equivalently,

\[
R(x)^2=A(x^2).
\]

So RMS is arithmetic mean after the quadratic lift

\[
x\mapsto x^2.
\]

This is exactly the move [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) had already made:

\[
p_i=a_i^2.
\]

The new recognition is that [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s square-root map and [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s unit Helmert ladder are not separate tricks. They are both consequences of using the \(L^2\) gauge.

\[
\boxed{
\text{RMS is the simplicial gauge of squared substance.}
}
\]

---

## Notation

- \(\mathbb R_{>0}^N\): positive amplitude ledger.
- \(H_N\): mean-zero hyperplane \(\{q\in\mathbb R^N:\sum_iq_i=0\}\); same object denoted \(H_0\) in [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)–[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049), renamed to match [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) onward. (Distinct from the conductor packet \(H_d\) of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) below; disambiguated by index.)
- \(R(x)\): RMS, \(R(x)=\sqrt{\frac1N\sum_i x_i^2}\).
- \(M_r(x)\): power mean, \((\frac1N\sum_i x_i^r)^{1/r}\).
- \(G(x)\): geometric mean, \(M_0(x)\).
- \(S(x)\): square closure, \(S(x)_i=x_i^2/\sum_jx_j^2\).
- \(h_k\): unnormalized Helmert vector \((1,\ldots,1,-k,0,\ldots,0)\).
- \(e_k\): unit Helmert vector \(h_k/\sqrt{k(k+1)}\).
- \(\chi_a\): additive character on \(\mathbb Z/N\), \(\chi_a(r)=e^{2\pi iar/N}\).
- \(H_d\): [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) conductor packet of additive conductor \(d\).
- \(K_y(t)\): centered log-partition, \(K_y(t)=\log(\frac1N\sum_i e^{t y_i})\).
- \(\kappa_n\): \(n\)-th cumulant of the centered log-ledger \(y\).
- \(\operatorname{sf}(m)\): squarefree kernel of \(m\).

---

## 1. RMS as the quadratic gauge

Let

\[
x=(x_1,\ldots,x_N)\in\mathbb R_{>0}^N.
\]

The positive cone has a scale action

\[
x\mapsto cx,\qquad c>0.
\]

If only the ray \([x]\) matters, a gauge chooses one representative from that ray.

Arithmetic gauge chooses

\[
\sum_i z_i=N.
\]

Geometric gauge chooses

\[
\prod_i z_i=1.
\]

Harmonic gauge chooses

\[
\sum_i z_i^{-1}=N.
\]

RMS gauge chooses

\[
\sum_i z_i^2=N.
\]

The representative is

\[
z_i=\frac{x_i}{R(x)},
\qquad
R(x)=\sqrt{\frac1N\sum_i x_i^2}.
\]

This is the sphere section of the positive projective cone:

\[
\mathcal R_N=\{z\in\mathbb R_{>0}^N:\|z\|^2=N\}.
\]

It is literally the positive orthant of the sphere of radius \(\sqrt N\).

### Theorem 1.1. Quadratic Gauge Theorem

Let \(x\in\mathbb R_{>0}^N\) be an amplitude ledger, meaning:

1. only the positive ray \([x]\) matters;
2. observable mass is quadratic in amplitude;
3. total observable mass is additive:

\[
E(x)=\sum_i x_i^2.
\]

Then RMS is the unique positive scale gauge fixing total quadratic mass to \(N\). The induced probability closure is

\[
\boxed{
p_i=\frac{x_i^2}{\sum_jx_j^2}.
}
\]

**Proof.** A gauge representative has the form \(z=cx\) for some \(c>0\). Fixing total quadratic mass to \(N\) imposes

\[
\sum_i z_i^2=N.
\]

Therefore

\[
c^2\sum_i x_i^2=N,
\]

so

\[
c=\sqrt{\frac{N}{\sum_i x_i^2}}
=\frac1{R(x)}.
\]

Thus \(z=x/R(x)\), and this representative is unique.

The induced probability is normalized quadratic mass:

\[
p_i=\frac{z_i^2}{\sum_jz_j^2}
=\frac{z_i^2}{N}.
\]

Since \(z_i=x_i/R(x)\) and \(N R(x)^2=\sum_jx_j^2\),

\[
p_i=\frac{x_i^2}{\sum_jx_j^2}.
\]

\(\square\)

We call this map

\[
S(x)_i=\frac{x_i^2}{\sum_jx_j^2}
\]

the square closure or Born closure of the positive ledger.

---

## 2. The \(2\arccos\) theorem

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) showed that Fisher-Rao geometry on probability is sphere geometry on amplitudes. RMS gauge gives the direct projective statement.

Let \(x,y\in\mathbb R_{>0}^N\), and let

\[
p_i=S(x)_i=\frac{x_i^2}{\sum_jx_j^2},
\qquad
q_i=S(y)_i=\frac{y_i^2}{\sum_jy_j^2}.
\]

Let

\[
\hat x=\frac{x}{\|x\|},
\qquad
\hat y=\frac{y}{\|y\|}.
\]

Then

\[
p_i=\hat x_i^2,
\qquad
q_i=\hat y_i^2.
\]

The Bhattacharyya coefficient is

\[
\sum_i\sqrt{p_iq_i}
=\sum_i\hat x_i\hat y_i
=\frac{x\cdot y}{\|x\|\|y\|}.
\]

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s Fisher-Rao distance is

\[
d_{FR}(p,q)
=2\arccos\sum_i\sqrt{p_iq_i}.
\]

Therefore:

\[
\boxed{
d_{FR}(S(x),S(y))
=
2\arccos\frac{x\cdot y}{\|x\|\|y\|}.
}
\]

This is why the factor \(2\arccos\) matters.

The angle

\[
\theta(x,y)=\arccos\frac{x\cdot y}{\|x\|\|y\|}
\]

is the spherical angle between amplitude rays. Fisher-Rao distance is twice that angle:

\[
d_{FR}=2\theta.
\]

So the old positive-coordinate sphere intuition becomes the exact metric statement:

\[
\boxed{
\text{probability distance is twice amplitude-ray angle.}
}
\]

---

## 3. Centered RMS, variance, and the Helmert ladder

RMS has a second face: on centered ledgers it is standard deviation.

Let

\[
\bar x=A(x)=\frac1N\sum_i x_i.
\]

Then

\[
R(x)^2
=\frac1N\sum_i x_i^2
=\bar x^2+\frac1N\sum_i(x_i-\bar x)^2.
\]

Therefore

\[
\boxed{
R(x)^2=A(x)^2+\operatorname{Var}(x).
}
\]

Equivalently,

\[
\boxed{
\frac{R(x)^2}{A(x)^2}=1+\mathrm{CV}(x)^2.
}
\]

When \(q\in H_N\), \(\bar q=0\), so

\[
R(q)^2=\frac1N\|q\|^2.
\]

Thus RMS normalization on \(H_N\) is Euclidean unit normalization up to the fixed factor \(\sqrt N\).

This is exactly where [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s radical clock enters.

The unnormalized Helmert vector is

\[
h_k=(1,\ldots,1,-k,0,\ldots,0),
\qquad 1\le k<N,
\]

with \(k\) leading \(1\)s, a single \(-k\) at position \(k+1\), and \(N-k-1\) trailing zeros. Its length is

\[
\|h_k\|^2=k(k+1).
\]

Hence

\[
R(h_k)=\sqrt{\frac{k(k+1)}{N}}.
\]

RMS normalization gives

\[
\frac{h_k}{R(h_k)}
=
\sqrt N\,\frac{h_k}{\sqrt{k(k+1)}}
=\sqrt N\,e_k.
\]

So the normalizers are precisely the [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) constants

\[
\sqrt{k(k+1)}.
\]

The RMS gauge has therefore been present inside [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) all along.

---

## 4. Born-Helmert Bridge Theorem

### Theorem 4.1. Born-Helmert Bridge

The RMS gauge is the common \(L^2\)-normalization mechanism behind:

1. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s amplitude sphere and Born closure on \(\mathbb R_{>0}^N\);
2. [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s unit Helmert ladder and prime radical field clock on \(H_N\).

More precisely:

On the positive cone,

\[
x\mapsto \frac{x}{\|x\|}
\mapsto
p_i=\frac{x_i^2}{\sum_jx_j^2}
\]

is [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s amplitude-to-probability map.

On the Helmert ladder,

\[
h_k\mapsto \frac{h_k}{\|h_k\|}
=\frac{h_k}{\sqrt{k(k+1)}}
\]

is [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s unit ladder map.

Both are restrictions of \(L^2\)-normalization.

**Proof.** The positive-cone statement follows from Theorem 1.1: RMS normalization places \(x\) on the positive sphere and square closure gives \(p_i=x_i^2/\sum_jx_j^2\).

For the Helmert statement, compute

\[
\|h_k\|^2=k(k+1).
\]

Therefore the unit vector is

\[
e_k=\frac{h_k}{\sqrt{k(k+1)}}.
\]

This is exactly \(L^2\)-normalization on the mean-zero ladder.

Since RMS normalization differs from unit normalization only by the fixed ambient factor \(\sqrt N\),

\[
\frac{h_k}{R(h_k)}=\sqrt N\,e_k.
\]

Thus the positive amplitude sphere and the unit Helmert ladder are the same \(L^2\) operation applied to two different domains. \(\square\)

The radical part is immediate. The normalized ladder constants generate

\[
\mathbb Q\left(\sqrt{\operatorname{sf}(k(k+1))}:1\le k<N\right).
\]

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) proved this field is

\[
\boxed{
K_N=\mathbb Q(\sqrt p:p\le N,\ p\text{ prime}).
}
\]

So the bridge says: [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) sphere geometry and [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) radical arithmetic are two faces of RMS gauge.

\[
\boxed{
\begin{gathered}
\text{Sphere geometry and radical arithmetic}\\
\text{are two faces of RMS gauge.}
\end{gathered}
}
\]

---

## 5. The power-pair parity theorem

[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) proved the \(r=1\) case implicitly:

\[
M_1=A,
\qquad
M_{-1}=H.
\]

RMS demands the \(r=2\) case. The theorem is general.

For \(r\ne0\), define

\[
M_r(x)=\left(\frac1N\sum_i x_i^r\right)^{1/r}.
\]

Let

\[
y_i=\log x_i-\log G(x),
\]

so

\[
\sum_i y_i=0.
\]

Define

\[
K_y(t)=\log\left(\frac1N\sum_i e^{t y_i}\right)
\]

with Taylor expansion at \(0\)

\[
K_y(t)=\sum_{n\ge2}\frac{\kappa_n}{n!}t^n
\]

on its zero-free Taylor branch.

### Theorem 5.1. Power-Pair Parity

For every real \(r\ne0\),

\[
\boxed{
\log\frac{M_r(x)}{M_{-r}(x)}
=
\frac{K_y(r)+K_y(-r)}{r}.
}
\]

and

\[
\boxed{
\log\frac{M_r(x)M_{-r}(x)}{G(x)^2}
=
\frac{K_y(r)-K_y(-r)}{r}.
}
\]

When the Taylor branch of \(K_y\) contains \(\pm r\), these exact identities become

\[
\boxed{
\log\frac{M_r(x)}{M_{-r}(x)}
=
2\sum_{m\ge1}
\frac{\kappa_{2m}r^{2m-1}}{(2m)!}.
}
\]

and

\[
\boxed{
\log\frac{M_r(x)M_{-r}(x)}{G(x)^2}
=
2\sum_{m\ge1}
\frac{\kappa_{2m+1}r^{2m}}{(2m+1)!}.
}
\]

Thus \(M_r/M_{-r}\) is the even cumulant ledger, while \(M_rM_{-r}/G^2\) is the odd cumulant ledger.

**Proof.** Since \(x_i=G(x)e^{y_i}\),

\[
M_r(x)
=
G(x)\left(\frac1N\sum_i e^{r y_i}\right)^{1/r}.
\]

Therefore

\[
\log\frac{M_r(x)}{G(x)}
=\frac1rK_y(r).
\]

Similarly,

\[
\log\frac{M_{-r}(x)}{G(x)}
=-\frac1rK_y(-r).
\]

Subtracting gives

\[
\log\frac{M_r}{M_{-r}}
=\frac{K_y(r)+K_y(-r)}{r}.
\]

On the Taylor branch, odd powers cancel and even powers double:

\[
\frac{K_y(r)+K_y(-r)}{r}
=
2\sum_{m\ge1}
\frac{\kappa_{2m}r^{2m-1}}{(2m)!}.
\]

Adding gives

\[
\log\frac{M_rM_{-r}}{G^2}
=\frac{K_y(r)-K_y(-r)}{r}.
\]

On the Taylor branch, even powers cancel and odd powers double:

\[
\frac{K_y(r)-K_y(-r)}{r}
=
2\sum_{m\ge1}
\frac{\kappa_{2m+1}r^{2m}}{(2m+1)!}.
\]

\(\square\)

### RMS corollary

For \(r=2\),

\[
M_2=R,
\qquad
M_{-2}=\left(\frac1N\sum_i x_i^{-2}\right)^{-1/2}.
\]

Then, in the same local/formal Taylor sense,

\[
\log\frac{M_2}{M_{-2}}
=
2\kappa_2+\frac23\kappa_4+\frac4{45}\kappa_6+\cdots,
\]

and

\[
\log\frac{M_2M_{-2}}{G^2}
=
\frac43\kappa_3+\frac4{15}\kappa_5+\cdots.
\]

RMS therefore gives the \(r=2\) harmonic-skew detector. It amplifies the odd cumulant tower more strongly than the \(A/H\) pair.

---

## 6. RMS conductor mixing

Now identify the outcome labels with the cyclic group

\[
\mathbb Z/N.
\]

Let

\[
\chi_a(r)=e^{2\pi iar/N}
\]

be the additive characters. Expand an amplitude ledger as

\[
x(r)=\sum_{a\in\mathbb Z/N}\widehat x_a\chi_a(r),
\qquad
\widehat x_a=\frac1N\sum_r\overline{\chi_a(r)}x(r).
\]

Define square closure

\[
S(x)_r=\frac{x(r)^2}{\sum_sx(s)^2}.
\]

### Theorem 6.1. RMS-Conductor Mixing

The \(c\)-th character coefficient of \(S(x)\) is

\[
\boxed{
\widehat{S(x)}_c
=
\frac{1}{N\widehat{x^2}_0}
\sum_{a+b\equiv c}
\widehat x_a\widehat x_b.
}
\]

Thus a pair of input modes \(a,b\) can contribute to output mode \(c\) only when

\[
\boxed{
a+b-c\equiv0\pmod N.
}
\]

**Proof.** Squaring the character expansion gives

\[
x(r)^2
=
\sum_{a,b}\widehat x_a\widehat x_b\chi_a(r)\chi_b(r).
\]

Since characters multiply by adding indices,

\[
\chi_a(r)\chi_b(r)=\chi_{a+b}(r),
\]

we have

\[
x(r)^2=\sum_{a,b}\widehat x_a\widehat x_b\chi_{a+b}(r).
\]

The \(c\)-th coefficient is

\[
\widehat{x^2}_c
=
\frac1N\sum_r\overline{\chi_c(r)}x(r)^2.
\]

Substituting,

\[
\widehat{x^2}_c
=
\sum_{a,b}\widehat x_a\widehat x_b
\frac1N\sum_r\chi_{a+b-c}(r).
\]

By character orthogonality,

\[
\frac1N\sum_r\chi_{a+b-c}(r)
=
\begin{cases}
1,&a+b-c\equiv0\pmod N,\\
0,&\text{otherwise}.
\end{cases}
\]

Thus

\[
\widehat{x^2}_c
=
\sum_{a+b\equiv c}\widehat x_a\widehat x_b.
\]

Finally,

\[
S(x)=\frac{x^2}{\sum_sx(s)^2},
\qquad
\sum_sx(s)^2=N\widehat{x^2}_0.
\]

Therefore

\[
\widehat{S(x)}_c
=
\frac{\widehat{x^2}_c}{N\widehat{x^2}_0}
=
\frac{1}{N\widehat{x^2}_0}
\sum_{a+b\equiv c}
\widehat x_a\widehat x_b.
\]

\(\square\)

This is the gauge-map analogue of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049).

[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049):

\[
T(\chi_a,\chi_b,\chi_c)\ne0
\quad\Longleftrightarrow\quad
a+b+c\equiv0\pmod N.
\]

RMS square closure:

\[
\widehat{S(x)}_c \text{ receives from }(a,b)
\quad\Longleftrightarrow\quad
a+b-c\equiv0\pmod N.
\]

The minus sign appears because \(c\) is an output coefficient, paired against \(\overline{\chi_c}\).

### Corollary 6.2. Conductor packet mixing law

Let \(H_d\) be the conductor-\(d\) packet from [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049):

\[
H_d=\operatorname{span}\{\chi_a:\operatorname{cond}(\chi_a)=d\}.
\]

If

\[
\chi_a\in H_d,
\qquad
\chi_b\in H_e,
\]

then their square-closure product contributes to

\[
\chi_{a+b}.
\]

The output conductor

\[
f=\operatorname{cond}(\chi_{a+b})
\]

satisfies

\[
\boxed{
f\mid \operatorname{lcm}(d,e).
}
\]

Hence

\[
\boxed{
H_d\cdot H_e
\longrightarrow
\bigoplus_{f\mid\operatorname{lcm}(d,e)}H_f.
}
\]

**Proof.** Since

\[
\chi_{a+b}=\chi_a\chi_b,
\]

the order of \(\chi_{a+b}\) divides the least common multiple of the orders of \(\chi_a\) and \(\chi_b\). These orders are \(d\) and \(e\). \(\square\)

### Corollary 6.3. Prime-local conductor law

Let \(\ell\) be a prime divisor of \(N\). Write

\[
\alpha=v_\ell(d),
\qquad
\beta=v_\ell(e),
\qquad
\gamma=v_\ell(f).
\]

If \(\alpha\ne\beta\), then

\[
\boxed{
\gamma=\max(\alpha,\beta).
}
\]

If \(\alpha=\beta\), then cancellation may occur, and

\[
\boxed{
0\le\gamma\le\alpha.
}
\]

So unequal conductor depths cannot cancel. Equal conductor depths can interfere downward.

**Proof.** Work in the \(\ell\)-primary component of the character group. The \(\ell\)-part of \(\chi_a\) has order \(\ell^\alpha\), the \(\ell\)-part of \(\chi_b\) has order \(\ell^\beta\), and the \(\ell\)-part of \(\chi_{a+b}=\chi_a\chi_b\) has order \(\ell^\gamma\).

If \(\alpha>\beta\), then \(\chi_b^{\ell^{\alpha-1}}=1\), while \(\chi_a^{\ell^{\alpha-1}}\ne1\). Hence

\[
(\chi_a\chi_b)^{\ell^{\alpha-1}}\ne1,
\]

so the product still has \(\ell\)-depth \(\alpha\). Since Corollary 6.2 gives \(\gamma\le\max(\alpha,\beta)=\alpha\), we get \(\gamma=\alpha\). The case \(\beta>\alpha\) is symmetric. If \(\alpha=\beta\), the product has order dividing \(\ell^\alpha\), but the leading \(\ell^\alpha\)-parts may cancel, so any depth \(0\le\gamma\le\alpha\) can occur. \(\square\)

This is the packet law in its most useful local form.

---

## 7. RMS radical universality

For integer amplitude ledgers,

\[
x\in\mathbb Z_{\ge0}^N,
\]

RMS normalization introduces the radical

\[
R(x)=\sqrt{\frac{x_1^2+\cdots+x_N^2}{N}}.
\]

Equivalently,

\[
\frac{x_i}{R(x)}
=
\frac{\sqrt N\,x_i}{\sqrt{x_1^2+\cdots+x_N^2}}.
\]

Thus the radical field of the normalized coordinates is

\[
\mathbb Q\left(\sqrt{N S(x)}\right),
\qquad
S(x)=x_1^2+\cdots+x_N^2.
\]

### Theorem 7.1. RMS Radical Universality

For every squarefree \(d\ge1\) and every \(N\ge4\), there exists an integer ledger

\[
x\in\mathbb Z_{\ge0}^N
\]

such that RMS normalization generates

\[
\mathbb Q(\sqrt d).
\]

That is,

\[
\mathbb Q\left(\sqrt{N S(x)}\right)=\mathbb Q(\sqrt d).
\]

**Proof.** It is enough to choose

\[
S(x)=Nd,
\]

because then

\[
N S(x)=N^2d,
\]

and \(N^2\) is a square. Therefore

\[
\mathbb Q(\sqrt{N S(x)})
=
\mathbb Q(\sqrt{N^2d})
=
\mathbb Q(\sqrt d).
\]

By Lagrange's four-square theorem, every positive integer is a sum of four squares. Thus \(Nd\) can be written as

\[
Nd=a_1^2+a_2^2+a_3^2+a_4^2.
\]

For \(N=4\), take

\[
x=(a_1,a_2,a_3,a_4).
\]

For \(N>4\), pad with zeros:

\[
x=(a_1,a_2,a_3,a_4,0,\ldots,0).
\]

Then \(S(x)=Nd\), as required. \(\square\)

So:

\[
\boxed{
N\ge4:\quad
\text{RMS normalization realizes every quadratic field.}
}
\]

### Corollary 7.2. Two-square obstruction

For \(N=2\) and squarefree \(d\ge1\),

\[
\boxed{
N=2:\quad
\mathbb Q(\sqrt d)
\text{ appears iff }d\text{ has no prime }p\equiv3\pmod4.
}
\]

**Proof.** Here

\[
S=x_1^2+x_2^2,
\qquad
\mathbb Q(\sqrt{N S})=\mathbb Q(\sqrt{2S}).
\]

By the two-square theorem, an integer is a sum of two squares iff every prime \(p\equiv3\pmod4\) appears with even exponent.

If \(d\) has no such prime, choose \(S=2d\). Then \(S\) is a sum of two squares, because \(2d\) has no prime \(p\equiv3\pmod4\) to an odd exponent, and

\[
\mathbb Q(\sqrt{2S})
=\mathbb Q(\sqrt{4d})
=\mathbb Q(\sqrt d).
\]

Conversely, if \(\mathbb Q(\sqrt{2S})=\mathbb Q(\sqrt d)\), then \(2S\) and \(d\) have the same squareclass. Any prime \(p\equiv3\pmod4\) dividing \(d\) would therefore occur to odd exponent in \(S\), since \(p\ne2\), contradicting the two-square theorem. \(\square\)

### Corollary 7.3. Three-square obstruction

For \(N=3\) and squarefree \(d\ge1\),

\[
\boxed{
N=3:\quad
\mathbb Q(\sqrt d)
\text{ is missing iff }d\text{ is odd and }d\equiv5\pmod8.
}
\]

**Proof.** Here

\[
S=x_1^2+x_2^2+x_3^2,
\qquad
\mathbb Q(\sqrt{N S})=\mathbb Q(\sqrt{3S}).
\]

Legendre's three-square theorem says an integer is a sum of three squares iff it is not of the form

\[
4^a(8b+7).
\]

If \(d\) is not odd congruent to \(5\pmod8\), choose \(S=3d\). Then

\[
\mathbb Q(\sqrt{3S})
=\mathbb Q(\sqrt{9d})
=\mathbb Q(\sqrt d).
\]

The integer \(3d\) is not of the forbidden form: if \(d\) is even, then \(3d\) has exactly one factor of \(2\); if \(d\) is odd, the only forbidden residue is \(3d\equiv7\pmod8\), equivalently \(d\equiv5\pmod8\). Hence \(S=3d\) is represented by three squares.

Conversely, suppose \(d\) is odd and \(d\equiv5\pmod8\), and suppose \(\mathbb Q(\sqrt{3S})=\mathbb Q(\sqrt d)\). Then \(S\) has the squareclass of \(3d\). Let \(s=\operatorname{sf}(3d)\). If \(3\nmid d\), then \(s=3d\equiv7\pmod8\). If \(3\mid d\), write \(d=3e\); then \(e\equiv7\pmod8\) and \(s=e\). In either case \(s\equiv7\pmod8\), so

\[
S=sq^2
\]

for some integer \(q\). After removing the largest power of \(4\) from \(q^2\), the remaining odd part is still \(7\pmod8\). Thus \(S\) is of the forbidden form \(4^a(8b+7)\), contradicting Legendre's theorem. \(\square\)

Thus:

\[
\boxed{
\text{RMS radicals are controlled by classical quadratic-form arithmetic.}
}
\]

This is distinct from [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504).

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504):

\[
\sqrt{k(k+1)}
\quad\leadsto\quad
\mathbb Q(\sqrt p:p\le N).
\]

[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428):

\[
x_1^2+\cdots+x_N^2
\quad\leadsto\quad
\text{sum-of-squares universality for }N\ge4.
\]

---

## 8. Higher square closures and wave mixing

RMS corresponds to the exponent \(2\). But the same character mechanism applies to every integer exponent.

For \(m\ge2\), define

\[
S_m(x)_r=\frac{x(r)^m}{\sum_sx(s)^m}.
\]

Then the \(c\)-th coefficient receives contributions only from tuples

\[
(a_1,\ldots,a_m)
\]

satisfying

\[
\boxed{
a_1+\cdots+a_m-c\equiv0\pmod N.
}
\]

This is the \(m\)-wave gauge-map rule.

The case \(m=2\) is RMS square closure.

The case \(m=3\) has the same three-input modular shape as [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049)'s cubic tensor, but with an output mode:

\[
a+b+c-d\equiv0\pmod N.
\]

This suggests a general principle:

\[
\boxed{
\text{integer power closure creates convolution selection rules.}
}
\]

The cumulant tensors of [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) produce multilinear selection rules when read in the [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) character basis. The power gauges produce nonlinear map selection rules before tensor differentiation even begins.

---

## 9. What [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) adds to [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) through [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419)

The series ledger is:

- [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872): square-root sphere; Fisher-Rao as spherical amplitude geometry.
- [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126): \(\Phi=\log Z\); cumulant tower, metric, cubic vertex, and closure defects.
- [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049): character basis; conductor packets and cubic selection rule.
- [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504): Helmert ladder; mean removal, geometric gauge, and prime radical rungs.
- [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419): harmonic gauge; reciprocal closure, softmin, and even/odd cumulant parity.
- [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428): RMS gauge; Born closure, \(2\arccos\), conductor mixing, and radical universality.

[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) adds the quadratic observer:

\[
\boxed{
\text{amplitude is primal; probability is squared amplitude.}
}
\]

Against [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872):

\[
\text{RMS is the gauge that puts amplitudes on the sphere.}
\]

Against [\heb{ל}2](https://doi.org/10.5281/zenodo.20338126):

\[
\text{RMS is the }r=2\text{ sample of the power-mean cumulant corridor.}
\]

Against [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049):

\[
\text{RMS square closure creates the quadratic selection rule }a+b-c\equiv0.
\]

Against [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504):

\[
\text{RMS normalization of }h_k\text{ is unit Helmert normalization.}
\]

Against [\heb{ל}5](https://doi.org/10.5281/zenodo.20388419):

\[
\text{RMS has a reciprocal power-pair }M_2,M_{-2}\text{ that splits cumulants by parity.}
\]

The old positive-coordinate dream therefore has a precise modern form:

\[
\begin{gathered}
\text{nonnegative amplitude rays}
\xrightarrow{\text{RMS}}
\text{positive sphere}
\xrightarrow{\text{square}}
\text{probability simplex}\\
\xrightarrow{2\arccos}
\text{Fisher-Rao distance}.
\end{gathered}
\]

---

## 10. Theorems and forward program

The main RMS results above are theorem-level. Some of the former open doors are also now settled at the level needed here; the rest remain forward problems.

### Theorem 10.1. Quadratic closure is entropy-decreasing

Let \(p\) be a probability vector and define its square closure by

\[
S_2(p)_i=\frac{p_i^2}{\sum_jp_j^2}.
\]

Then

\[
H_{\mathrm{Shannon}}(S_2(p))\le H_{\mathrm{Shannon}}(p),
\]

with equality exactly when \(p\) is uniform on its support. Iterating \(S_2\) is the dyadic escort flow

\[
S_2^n(p)_i=\frac{p_i^{2^n}}{\sum_jp_j^{2^n}},
\]

so the flow concentrates on the maximal-coordinate support.

**Proof.** Sort the nonzero coordinates of \(p\) in descending order:

\[
p_1\ge p_2\ge\cdots\ge p_s>0.
\]

Write \(q=S_2(p)\), and for an initial segment let

\[
A_k=\sum_{i\le k}p_i,
\qquad
B_k=\sum_{i>k}p_i,
\qquad
C_k=\sum_{i\le k}p_i^2,
\qquad
D_k=\sum_{i>k}p_i^2.
\]

The \(k\)-th partial sum of \(q\) is

\[
Q_k=\sum_{i\le k}q_i=\frac{C_k}{C_k+D_k}.
\]

Since every entry in the first segment is at least every entry in the tail,

\[
\frac{C_k}{A_k}
=\frac{\sum_{i\le k}p_i^2}{\sum_{i\le k}p_i}
\ge
\frac{\sum_{i>k}p_i^2}{\sum_{i>k}p_i}
=\frac{D_k}{B_k},
\]

with the tail-free case being trivial. Therefore

\[
C_kB_k\ge A_kD_k,
\]

which is equivalent to

\[
\frac{C_k}{C_k+D_k}\ge A_k.
\]

Thus every initial partial sum of \(q\) is at least the corresponding partial sum of \(p\), so \(q\) majorizes \(p\). Shannon entropy is Schur-concave, hence

\[
H_{\mathrm{Shannon}}(q)\le H_{\mathrm{Shannon}}(p).
\]

If equality holds, strict Schur-concavity forces \(q=p\). For every positive coordinate, this means \(p_i^2/Z=p_i\), where \(Z=\sum_jp_j^2\), hence every nonzero \(p_i\) equals \(Z\). Thus \(p\) is uniform on its support. The converse is immediate, and the iteration formula follows by induction. \(\square\)

In character space, each iteration doubles convolution depth. Thus the winner-take-all dynamics of square closure has a finite-mode conductor-mixing description.

### Remark 10.2. Helmert-Fourier entries are settled at entry level

The entry-level transfer between the Helmert ladder and the Fourier character basis is settled by [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504): each normalized Helmert-Fourier coefficient factors as radical Helmert normalization times cyclotomic conductor data.

Thus the former entry-factorization question should not remain open in [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428). What remains open is packet-level structure.

### Forward Problem 10.3. Packet-level Helmert-Fourier transfer geometry

The unit Helmert vectors \(e_k\) and the character packets of [\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) are both orthogonal ways to read \(H_N\), but they expose different arithmetic:

\[
\text{Helmert}\to\text{radical normalizers},
\qquad
\text{Fourier}\to\text{conductor packets}.
\]

The open problem is to describe the full change-of-basis matrix over conductor packets: block behavior, Gauss-sum structure, real packet splitting, and the way radical normalization interacts with cyclotomic data.

### Forward Problem 10.4. Quadratic-form ladder arithmetic on \(A_{N-1}\)

RMS normalization of arbitrary integer ledgers is controlled by sums of \(N\) squares. RMS normalization restricted to the root lattice

\[
A_{N-1}=\{q\in\mathbb Z^N:\sum_iq_i=0\}
\]

is controlled by the quadratic form

\[
\|q\|^2=\sum_iq_i^2.
\]

The squareclasses represented by this root-lattice form should have their own universality threshold and local obstruction theory, distinct from unrestricted sums of squares.

This would be the radical arithmetic of centered integer balances, not arbitrary amplitudes.

### Forward Problem 10.5. From pure complex amplitudes to mixed-state dephasing

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) and [\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) use positive real amplitudes. The pure-state complex extension is no longer the unresolved part of the story; it is the next sector, continued in [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442). There the positive orthant is replaced by complex projective space, and square closure becomes

\[
p_i=\frac{|z_i|^2}{\sum_j|z_j|^2}.
\]

The \(2\arccos\) Fisher-Rao distance becomes the real-positive restriction of the projective metric, and conductor mixing acquires phase-sensitive interference terms on the complex amplitude bundle.

The remaining forward problem is the mixed-state version: replace pure amplitudes \(z\) by density matrices, replace modulus restriction by the dephasing channel, and formulate the corresponding apex generator using a regularized matrix logarithm. That is where Bures geometry, quantum Fisher information, and rank-deficient boundary behavior enter.

### Remark 10.6. Phase-average disambiguation

For series readers, the phrase "phase-average" should be read with care. The classical face of the complex theory is obtained by modulus restriction, or operational dephasing:

\[
z\longmapsto |z|
\longmapsto
\left(\frac{|z_i|^2}{\sum_j|z_j|^2}\right)_i.
\]

It is not the Haar average of the apex generator over the relative-phase torus. A genuine torus average is a different operation: it annihilates the nonzero integer phase modes rather than returning the real-positive apex. Thus, unless an actual phase integral is displayed, "phase-averaged" in the series should mean "phase-erased by modulus restriction" rather than "averaged over all phases."

### Forward Problem 10.7. Power-gauge hierarchy

Theorems 5.1 and 10.1 settle two structural pieces of the hierarchy: \(M_r,M_{-r}\) split the cumulant tower by parity, and \(r=2\) produces entropy-decreasing square closure. The positive integer closure diagonal is also theorem-level: integer \(r=m\) gives \(m\)-fold character convolution with selection rule

\[
a_1+\cdots+a_m\equiv c\pmod N.
\]

Negative integer samples are the same positive-integer theorem applied to the reciprocal ledger \(u_i=1/x_i\), not a new polynomial rule in the original Fourier coefficients \(\widehat x\). The pure-state complex \(m\)-power cover is continued in [\heb{ל}7](https://doi.org/10.5281/zenodo.20392442).

The remaining problem is to organize the parts that are not yet one calculus: non-integer \(\beta\), branched complex gauges, the moment-side logarithmic branch data, and the denominator arithmetic of negative samples.

\[
r=1:\ \text{mass gauge},
\qquad
r=0:\ \text{scale gauge},
\]

\[
r=-1:\ \text{reciprocal gauge},
\qquad
r=2:\ \text{amplitude/energy gauge}.
\]

### Forward Problem 10.8. Simplicial area and volume gauges

The older nonnegative-coordinate program emphasized products of components as area, volume, and higher content. RMS suggests a dual principle: before products measure content, RMS fixes amplitude radius.

There should be a clean relation between:

1. product gauges such as \(G(x)=1\);
2. quadratic gauges such as \(R(x)=1\); and
3. simplex-volume forms on the positive coordinate frame.

This may connect the old "optimist plane" intuition to Aitchison geometry, Fisher-Rao geometry, and exterior algebra on \(H_N\).

---

## 11. Worked example: \(N=4\)

Let

\[
x=(1,2,3,4).
\]

Then

\[
R(x)=\sqrt{\frac{1+4+9+16}{4}}
=\sqrt{\frac{30}{4}}
=\frac{\sqrt{30}}{2}.
\]

RMS normalization gives

\[
\frac{x}{R(x)}
=
\frac{2}{\sqrt{30}}(1,2,3,4).
\]

Square closure gives

\[
p=\left(\frac1{30},\frac4{30},\frac9{30},\frac{16}{30}\right).
\]

The radical field is

\[
\mathbb Q(\sqrt{N S(x)})
=
\mathbb Q(\sqrt{4\cdot30})
=
\mathbb Q(\sqrt{30}).
\]

Now compare the first Helmert vector in \(N=4\):

\[
h_1=(1,-1,0,0).
\]

Its RMS is

\[
R(h_1)=\sqrt{\frac2{4}}=\frac1{\sqrt2}.
\]

RMS normalization gives

\[
\frac{h_1}{R(h_1)}
=\sqrt2(1,-1,0,0)
=2e_1,
\]

since

\[
e_1=\frac{(1,-1,0,0)}{\sqrt2}.
\]

The fixed factor \(2=\sqrt N\) is ambient. The nontrivial radical is \(\sqrt2\), exactly as [\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) said.

For

\[
h_3=(1,1,1,-3),
\]

\[
\|h_3\|^2=12,
\qquad
e_3=\frac{h_3}{\sqrt{12}}.
\]

The radical is

\[
\sqrt{12}=2\sqrt3.
\]

Thus \(N=4\) generates

\[
K_4=\mathbb Q(\sqrt2,\sqrt3).
\]

The same RMS operation produced both:

1. the Born probability \(p_i\propto x_i^2\);
2. the Helmert radical constants \(\sqrt2,\sqrt3\).

That is the bridge in coordinates.

---

## 12. Coda

The mean sequence is now no longer a list of averages.

It is a list of observers.

\[
\begin{array}{ccl}
A &:& \text{mass observer},\\
G &:& \text{scale observer},\\
H &:& \text{reciprocal observer},\\
R &:& \text{amplitude observer}.
\end{array}
\]

Arithmetic mean removes additive displacement.

Geometric mean removes multiplicative scale.

Harmonic mean removes reciprocal bottleneck.

RMS removes quadratic energy.

The RMS entry is special because it closes the loop back to the beginning.

[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s square-root sphere was already the RMS gauge in disguise.

[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504)'s unit Helmert ladder was already the RMS gauge in disguise.

[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) names the disguise:

\[
\boxed{
\text{\(L^2\)-normalization.}
}
\]

On positive amplitudes, it gives:

\[
\text{sphere}\to\text{square closure}\to\text{Fisher-Rao}.
\]

On mean-zero balances, it gives:

\[
\text{unit Helmert}\to\sqrt{k(k+1)}\to\text{prime radical field clock}.
\]

On cyclic labels, it gives:

\[
\text{square closure}\to a+b-c\equiv0\to\text{conductor mixing}.
\]

On integer ledgers, it gives:

\[
\text{sums of squares}\to\text{quadratic field universality for }N\ge4.
\]

So the final line is:

\[
\boxed{
\text{RMS is where amplitude geometry, conductor arithmetic, and radical measurement meet.}
}
\]

This is why \(2\arccos\) was meaningful.

The angle was waiting for the square.

---

## Acknowledgments

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) during the development of this paper. The collaborations were intellectually substantive: AI partners contributed insights, proposed theorems and conjectures, surfaced relevant literature, verified derivations, and iterated on exposition. I acknowledge this use transparently; the selection of which contributions to keep and the responsibility for the mathematical content are mine.

---

## References and Anchors

- Murillo Montero, L. (2026). *[\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) — Identifying 3: The Native Simplicial Chart.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20336872](https://doi.org/10.5281/zenodo.20336872).
- Murillo Montero, L. (2026). *[\heb{ל}2](https://doi.org/10.5281/zenodo.20338126) — Identifying 3: The Cumulant Tower as Effective Action.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20338126](https://doi.org/10.5281/zenodo.20338126).
- Murillo Montero, L. (2026). *[\heb{ל}3](https://doi.org/10.5281/zenodo.20339049) — Identifying 3: Character Orthogonality on the Conductor Lattice.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20339049](https://doi.org/10.5281/zenodo.20339049).
- Murillo Montero, L. (2026). *[\heb{ל}4](https://doi.org/10.5281/zenodo.20383504) — The Helmert-Simplicial Residue Ladder.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20383504](https://doi.org/10.5281/zenodo.20383504).
- Murillo Montero, L. (2026). *[\heb{ל}5](https://doi.org/10.5281/zenodo.20388419) — The Harmonic-Simplicial Dual Gauge.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20388419](https://doi.org/10.5281/zenodo.20388419).
- Murillo Montero, L. (2026). *[\heb{ל}6](https://doi.org/10.5281/zenodo.20392428) — The RMS-Simplicial Quadratic Gauge.* Zenodo preprint (this work; concept DOI, resolves to latest version), DOI [10.5281/zenodo.20392428](https://doi.org/10.5281/zenodo.20392428).
- Murillo Montero, L. (2026). *[\heb{ל}7](https://doi.org/10.5281/zenodo.20392442) — Complex Amplitudes and the Quantum Sector of the Apex.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20392442](https://doi.org/10.5281/zenodo.20392442).
- Murillo Montero, L. (2025). *A New Model for Any-Dimensional Space.* Unpublished early draft.
- Helmert, F. R. (1876). *Die Genauigkeit der Formel von Peters zur Berechnung des wahrscheinlichen Beobachtungsfehlers directer Beobachtungen gleicher Genauigkeit.* Astronomische Nachrichten, 88, 113–132. [Wikipedia: Helmert transformation](https://en.wikipedia.org/wiki/Helmert_transformation).
- Aitchison, J. (1986). *The Statistical Analysis of Compositional Data.* Monographs on Statistics and Applied Probability. London: Chapman and Hall. ISBN 978-0-412-28060-3. [DOI: 10.1007/978-94-009-4109-0](https://doi.org/10.1007/978-94-009-4109-0).
- Hardy, G. H., Littlewood, J. E., and Pólya, G. (1934). *Inequalities.* Cambridge: Cambridge University Press. 2nd ed., 1952; Cambridge Mathematical Library reissue, 1988. ISBN 978-0-521-35880-4. (Chapters II–III on the power-mean inequalities.)
- Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry.* Translations of Mathematical Monographs, Vol. 191. Providence, RI: American Mathematical Society. ISBN 978-0-8218-0531-2. [AMS page](https://bookstore.ams.org/mmono-191).
- Serre, J.-P. (1973). *A Course in Arithmetic.* Graduate Texts in Mathematics, Vol. 7. New York: Springer-Verlag. ISBN 978-0-387-90040-7. [DOI: 10.1007/978-1-4684-9884-4](https://doi.org/10.1007/978-1-4684-9884-4). (Chapter IV on sums of squares and the local–global theorems used in §7.)
- Grosswald, E. (1985). *Representations of Integers as Sums of Squares.* New York: Springer-Verlag. ISBN 978-0-387-96126-2. [DOI: 10.1007/978-1-4613-8566-0](https://doi.org/10.1007/978-1-4613-8566-0).
- Lagrange, J.-L. (1770). *Démonstration d'un théorème d'arithmétique.* Nouveaux Mémoires de l'Académie Royale des Sciences et Belles-Lettres de Berlin. (Four-square theorem, used in §7.1.)
- Legendre, A.-M. (1798). *Essai sur la Théorie des Nombres.* Paris: Duprat. (Three-square theorem, used in Cor. 7.3.)
- Boyd, S. and Vandenberghe, L. (2004). *Convex Optimization.* Cambridge: Cambridge University Press. ISBN 978-0-521-83378-3. (§3.1.5 on log-sum-exp / softmax, the cumulant generator viewpoint used in Thm. 5.1.) [Free PDF](https://web.stanford.edu/~boyd/cvxbook/).
- Marshall, A. W., Olkin, I., and Arnold, B. C. (2011). *Inequalities: Theory of Majorization and Its Applications.* 2nd ed. Springer Series in Statistics. New York: Springer. ISBN 978-0-387-40087-7. [DOI: 10.1007/978-0-387-68276-1](https://doi.org/10.1007/978-0-387-68276-1). (Majorization and Schur-concavity, used in Thm. 10.1.)
