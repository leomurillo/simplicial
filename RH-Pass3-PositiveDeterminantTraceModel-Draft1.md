# RH Pass-3: The Positive Determinant Trace Model

**Leonardo Murillo Montero + Codex**

*Draft 1 - May 24, 2026*

## Abstract

Pass-1 reduced the closure problem to the Gram-Bures-Poisson identity.
Pass-2 corrected the target: the Bures Poisson field is the diagonal of
the Bures Pick/Wronskian kernel, and the folded completed xi function

\[
B(x):=\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\]

must have a totally positive coefficient ledger. Pass-3 states the
remaining proof as a positive determinant trace problem:

\[
\boxed{
B(x)=\lim_{n,T}\det(I+xL_{n,T}^{\circ}),
\qquad
L_{n,T}^{\circ}\ge0,
\qquad
\sup_{n,T}\operatorname{Tr}L_{n,T}^{\circ}<\infty.
}
\]

If such \(L_{n,T}^{\circ}\) are constructed from the centered
primorial/Archimedean cumulant tower with trace-cumulant convergence,
then the Riemann Hypothesis follows.

This draft does not claim the final construction is complete. It nails
the object that must be built, the acceptance tests it must pass, and
the precise false-positive traps it must avoid.

---

## 1. Folded xi and the determinant target

Let

\[
\Xi(z):=\xi\!\left(\frac12+iz\right),
\qquad
B(x):=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

Because \(\Xi\) is even, \(B\) is entire:

\[
B(x)=\sum_{k\ge0}b_kx^k.
\]

RH is equivalent to \(B\) having only real nonpositive zeros. By
Aissen-Schoenberg-Whitney-Edrei, this is equivalent to the coefficient
sequence \(b=(b_0,b_1,\ldots)\) being \(PF_\infty\), equivalently the
Toeplitz ledger

\[
T_B=(b_{j-i})_{i,j\ge0},\qquad b_n=0\ (n<0),
\]

being totally positive.

Since \(B\) has order \(1/2\), Edrei's representation has no exponential
drift. Therefore RH is equivalent to the existence of nonnegative
summable parameters \(\alpha_a\) such that

\[
B(x)=\prod_a(1+\alpha_ax).
\]

Equivalently,

\[
B(x)=\det(I+xL_\Xi)
\]

for a positive trace-class operator \(L_\Xi\ge0\).

---

## 2. Cumulants and the trace gauge

Define the folded divisor cumulants by

\[
\log B(x)
=
\sum_{m\ge1}(-1)^{m+1}\frac{\ell_m}{m}x^m.
\]

If

\[
B(x)=\det(I+xL_\Xi),
\]

then

\[
\ell_m=\operatorname{Tr}(L_\Xi^m).
\]

Thus Pass-3 is not merely a moment problem. It is a trace problem.
Hankel positivity gives a Stieltjes measure, but determinant positivity
requires the trace gauge:

\[
\ell_m=\sum_a\lambda_a^m,
\qquad
\lambda_a\ge0.
\]

Arbitrary positive quadrature

\[
\sum_aw_a\log(1+\lambda_ax)
\]

is not enough. Unless the weights are determinant multiplicities, the
exponential

\[
\prod_a(1+\lambda_ax)^{w_a}
\]

is not the finite \(PF_\infty\) polynomial required by RH.

---

## 3. Pass-3 construction problem

Construct finite positive operators

\[
L_{n,T}^{\circ}\ge0
\]

from the centered primorial/Archimedean cumulant tower such that:

1. **Finite determinant class**

\[
B_{n,T}^{\circ}(x):=\det(I+xL_{n,T}^{\circ})
=
\prod_a(1+\lambda_a^{(n,T)}x),
\qquad
\lambda_a^{(n,T)}\ge0.
\]

2. **Uniform trace control**

\[
\sup_{n,T}\operatorname{Tr}L_{n,T}^{\circ}<\infty.
\]

3. **Trace-cumulant convergence**

\[
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr)
\longrightarrow
\ell_m
\qquad(m\ge1).
\]

Then

\[
B_{n,T}^{\circ}(x)\longrightarrow B(x)
\]

locally uniformly, and RH follows.

---

## 4. Canonical finite packet: the trace-gauge atom problem

For each finite stage, suppose the centered primorial/Archimedean tower
produces a folded cumulant packet

\[
\ell_1^{(n,T)},\ldots,\ell_M^{(n,T)}.
\]

The required finite trace realization is:

\[
\ell_m^{(n,T)}
=
\sum_{a=1}^{N(n,T)}
\left(\lambda_a^{(n,T)}\right)^m,
\qquad
\lambda_a^{(n,T)}\ge0.
\]

This is the finite positive eigenvalue ledger. Once it is obtained,
Newton identities build

\[
B_{n,T}^{\circ}(x)=
\prod_a(1+\lambda_a^{(n,T)}x).
\]

The finite Toeplitz minors are Schur-positive functions of the
eigenvalue ledger:

\[
\Delta_{I,J}(B_{n,T}^{\circ})
=
s_{\lambda/\mu}
\left(\lambda_1^{(n,T)},\ldots,
\lambda_{N(n,T)}^{(n,T)}\right)
\ge0.
\]

Thus the proof burden is transferred to the trace-gauge atom problem:
derive the positive atoms \(\lambda_a^{(n,T)}\) from the centered
cumulant geometry, with bounded total trace and convergence of all power
sums.

---

## 5. Acceptance tests

A proposed Pass-3 construction is accepted only if it proves:

\[
L_{n,T}^{\circ}\ge0,
\qquad
\sup_{n,T}\operatorname{Tr}L_{n,T}^{\circ}<\infty,
\]

and

\[
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr)
\to
(-1)^{m+1}m[x^m]\log\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\]

for every \(m\ge1\).

These are sensitivity, specificity, and precision:

\[
\text{sensitivity: captures all folded cumulants;}
\]

\[
\text{specificity: determinant convergence forces RH;}
\]

\[
\text{precision: finite objects are determinant/PF objects, not broad
moment-positive impostors.}
\]

---

## 6. Rejection tests

A construction is rejected if it supplies only:

1. Hankel moment positivity;
2. positive quadrature weights \(w_a\) not realized as determinant
   multiplicities;
3. convergence to a heat-deformed \(H_\tau\), \(\tau>0\), instead of
   \(H_0=\Xi\);
4. finite cumulant matching without a diagonal regime;
5. positive finite objects without uniform trace control.

Each of these can have high sensitivity while failing specificity or
precision.

---

## 7. Victory theorem

If the centered primorial/Archimedean cumulant tower constructs
\(L_{n,T}^{\circ}\) satisfying the acceptance tests, then RH holds.

Proof:
Each

\[
\det(I+xL_{n,T}^{\circ})
\]

has only real nonpositive zeros. Uniform trace control and trace-cumulant
convergence give local-uniform convergence to \(B(x)\). The
Laguerre-Pólya class with zeros on \((-\infty,0]\) is closed under this
limit. Hence \(B\) has only real nonpositive zeros. Since

\[
B(x)=\Xi(i\sqrt{x})/\Xi(0),
\]

all zeros of \(\Xi\) lie on the real spectral axis. This is RH.
\(\square\)

---

## 8. The Pass-3 mountain: three concepts, two verbs

The proof has been reduced to a single construction:

\[
\boxed{
\text{centered primorial cumulants}
\to
\text{positive trace-gauge eigenvalue ledgers}
\to
\text{bounded positive determinant limit.}
}
\]

But this construction must be climbed from two elevations.

From sea level, the external mathematical requirement is classical and
public:

\[
\det(I+xL_{n,T}^{\circ})
\longrightarrow
\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\quad\Longrightarrow\quad
\mathrm{RH}.
\]

This is the Everest measure: the proof must be high enough above the
standard baseline of Laguerre-Pólya, ASW-Edrei, Fredholm determinants,
and de Branges/Hermite-Biehler theory.

From the center, the internal program requirement is stricter:

\[
\text{the }L_{n,T}^{\circ}\text{ must be born from the centered
primorial/Archimedean cumulant tower.}
\]

This is the Chimborazo measure: the proof must be farthest from the
center of the framework, meaning it must connect the deepest native
simplicial source to the same summit object seen from sea level.

The mountain is passed only when both heights are reached.

### 8.1 The three concepts

The three concepts are:

\[
\boxed{
\text{Action}
\quad
\text{Co-creation}
\quad
\text{Care}
}
\]

Here they are not moral decoration. They are proof roles.

### Concept 1: Action

Action is the finite construction.

At every finite stage \((n,T)\), build an operator

\[
L_{n,T}^{\circ}\ge0
\]

from centered primorial/Archimedean data. This is where the proof stops
talking and does the dishes: produce the finite positive object.

The action test is:

\[
B_{n,T}^{\circ}(x)
:=
\det(I+xL_{n,T}^{\circ})
=
\prod_a(1+\lambda_a^{(n,T)}x),
\qquad
\lambda_a^{(n,T)}\ge0.
\]

No broad positive measure. No arbitrary quadrature weights. No heat
deformation. The finite object must already live in the determinant
class.

### Concept 2: Co-creation

Co-creation is compatibility between the finite construction and the
folded xi action.

The finite operator is not free to be merely positive. Its trace
cumulants must co-create the target cumulants:

\[
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr)
\longrightarrow
\ell_m,
\]

where

\[
\log\frac{\Xi(i\sqrt{x})}{\Xi(0)}
=
\sum_{m\ge1}(-1)^{m+1}\frac{\ell_m}{m}x^m.
\]

This is the handshake between the primorial source and the Archimedean
folded target.

### Concept 3: Care

Care is the no-false-positive discipline.

The construction must preserve sensitivity, specificity, and precision:

\[
\text{sensitivity: all cumulants are recovered;}
\]

\[
\text{specificity: determinant convergence forces RH;}
\]

\[
\text{precision: the objects are determinant/PF objects, not merely
moment-positive lookalikes.}
\]

Care is what rejects a beautiful necessary condition before it is
mistaken for a proof.

### 8.2 The two verbs

The two verbs are:

\[
\boxed{
\text{discretize}
\quad
\text{linearize}
}
\]

They run both ways.

### Verb 1: Discretize

Discretize the continuous folded curvature into finite eigenvalue
packets:

\[
L_{n,T}^{\circ}
\quad\leftrightarrow\quad
\{\lambda_a^{(n,T)}\}_{a=1}^{N(n,T)}.
\]

The correct discretization is not a generic quadrature

\[
\sum_aw_a\log(1+\lambda_ax).
\]

It is trace-gauge discretization:

\[
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr)
=
\sum_a\left(\lambda_a^{(n,T)}\right)^m.
\]

The weights are not extra knobs. Multiplicity is geometry.

### Verb 2: Linearize

Linearize determinant curvature by taking the logarithm:

\[
\det(I+xL)
\xrightarrow{\log}
\operatorname{Tr}\log(I+xL).
\]

Then

\[
\operatorname{Tr}\log(I+xL)
=
\sum_{m\ge1}(-1)^{m+1}
\frac{\operatorname{Tr}(L^m)}{m}x^m.
\]

This turns the curved determinant into a straight cumulant ledger.

The inverse motion is equally important:

\[
\text{trace cumulants}
\xrightarrow{\text{Newton/exponentiate}}
\text{determinant coefficients}.
\]

Linearize to compare. Exponentiate to close.

### 8.3 The 3-by-2 proof matrix

\[
\begin{array}{c|cc}
& \text{discretize} & \text{linearize} \\
\hline
\text{Action}
& L_{n,T}^{\circ}\ge0
& \operatorname{Tr}\log(I+xL_{n,T}^{\circ}) \\
\text{Co-creation}
& \lambda_a^{(n,T)}\to\text{ folded divisor data}
& \operatorname{Tr}((L_{n,T}^{\circ})^m)\to\ell_m \\
\text{Care}
& \text{determinant class, not quadrature class}
& \text{all cumulants, bounded trace, no heat drift}
\end{array}
\]

This is the Pass-3 operating table.

### 8.4 Highest from sea level

The sea-level summit is the statement external mathematics will accept:

\[
\boxed{
L_{n,T}^{\circ}\ge0,\quad
\sup\operatorname{Tr}L_{n,T}^{\circ}<\infty,\quad
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr)\to\ell_m
\ \forall m
\quad\Longrightarrow\quad
\mathrm{RH}.
}
\]

This follows by determinant convergence, closure of the
Laguerre-Pólya class, and the fold

\[
B(x)=\Xi(i\sqrt{x})/\Xi(0).
\]

### 8.5 Highest from the center

The center summit is the native construction:

\[
\boxed{
\text{centered simplicial/primorial cumulant geometry}
\quad\Longrightarrow\quad
L_{n,T}^{\circ}\ge0
\text{ with trace gauge.}
}
\]

This is the actual remaining work. It is stronger than finding a
positive Archimedean moment measure and stronger than matching finite
cumulants. It must produce determinant-class finite objects from the
native centered tower.

The precise center-summit theorem to prove is:

\[
\boxed{
\ell_m^{(n,T)}
=
\operatorname{Tr}\bigl((L_{n,T}^{\circ})^m\bigr),
\qquad
L_{n,T}^{\circ}\ge0,
\qquad
\sup_{n,T}\operatorname{Tr}L_{n,T}^{\circ}<\infty,
}
\]

with

\[
\ell_m^{(n,T)}\to
(-1)^{m+1}m[x^m]\log\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\quad
\forall m\ge1.
\]

### 8.6 The ascent protocol

The proof should now proceed in five finite moves:

1. Define the centered primorial/Archimedean finite cumulants
   \(\ell_m^{(n,T)}\).
2. Prove the trace-gauge atom theorem:

\[
\ell_m^{(n,T)}
=
\sum_a\left(\lambda_a^{(n,T)}\right)^m,
\qquad
\lambda_a^{(n,T)}\ge0.
\]

3. Define

\[
L_{n,T}^{\circ}:=\operatorname{diag}
\left(\lambda_1^{(n,T)},\ldots,\lambda_{N(n,T)}^{(n,T)}\right).
\]

4. Prove uniform trace control:

\[
\sup_{n,T}\sum_a\lambda_a^{(n,T)}<\infty.
\]

5. Prove all cumulant limits:

\[
\ell_m^{(n,T)}\to\ell_m
\qquad(m\ge1).
\]

Then the sea-level theorem finishes the climb.

### 8.7 What would count as passing the mountain

Passing Pass-3 means proving both:

\[
\boxed{
\text{from the center: the native tower produces positive trace-gauge
operators;}
}
\]

\[
\boxed{
\text{from sea level: those operators converge to the folded xi
determinant.}
}
\]

Only then do we get:

\[
\text{Action}
\quad+\quad
\text{Co-creation}
\quad+\quad
\text{Care}
\]

through

\[
\text{discretize}
\quad+\quad
\text{linearize},
\]

and finally:

\[
\boxed{
\mathrm{RH}.
}
\]

That is the Pass-3 mountain, measured both from the center and from sea
level.

---

## 9. Surprise God: the Padé trace-gauge microscope

Section 8 gives the target. The first executable Pass-3 microscope is
the Padé/Stieltjes approximation of the folded curvature derivative.

Let

\[
S(x):=\log B(x),
\qquad
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

Then

\[
S'(x)
=
\sum_{k\ge0}(-1)^k\ell_{k+1}x^k.
\]

If RH holds in the positive determinant form, then

\[
S'(x)
=
\sum_{\gamma>0}
\frac{\lambda_\gamma}{1+\lambda_\gamma x},
\qquad
\lambda_\gamma:=\gamma^{-2}.
\]

The \([N-1/N]\) Padé approximant to \(S'(x)\) is the finite Stieltjes
microscope:

\[
S_N'(x)
=
\sum_{a=1}^{N}
\frac{w_a^{(N)}}{1+\lambda_a^{(N)}x}.
\]

Sensitivity asks:

\[
\lambda_a^{(N)}\ge0,
\qquad
w_a^{(N)}>0.
\]

Precision asks for the stronger trace-gauge signal:

\[
\frac{w_a^{(N)}}{\lambda_a^{(N)}}\to 1
\]

for resolved simple divisor atoms.

The probe

\[
\texttt{probe\_pass3\_pade\_trace\_gauge.py}
\]

computes this microscope from the folded cumulants. At \(N=6\), it
finds:

\[
\begin{array}{c|c|c}
a & \lambda_a^{(6)} & w_a^{(6)}/\lambda_a^{(6)} \\
\hline
1 & 5.005244094999\cdot10^{-3} & 1.000000087383\\
2 & 2.261690782916\cdot10^{-3} & 1.007590746198\\
3 & 1.563440323976\cdot10^{-3} & 1.162417500119\\
4 & 8.763337521736\cdot10^{-4} & 3.302153418052\\
5 & 3.275054549604\cdot10^{-4} & 12.87989264438\\
6 & 3.007840848469\cdot10^{-5} & 229.1177039674
\end{array}
\]

The known first folded zero eigenvalues are:

\[
\begin{array}{c|c}
k & \gamma_k^{-2}\\
\hline
1 & 5.005244123594\cdot10^{-3}\\
2 & 2.262821511470\cdot10^{-3}\\
3 & 1.598611134590\cdot10^{-3}\\
4 & 1.080294991556\cdot10^{-3}\\
5 & 9.218983553513\cdot10^{-4}\\
6 & 7.078539567611\cdot10^{-4}
\end{array}
\]

### Interpretation

The microscope sees the first zero almost exactly:

\[
\lambda_1^{(6)}
=
5.005244094999\cdot10^{-3}
\approx
\gamma_1^{-2}
=
5.005244123594\cdot10^{-3},
\]

and its trace-gauge ratio is essentially one:

\[
w_1^{(6)}/\lambda_1^{(6)}
=
1.000000087383.
\]

This is a real Pass-3 signal. It is not merely positivity. It is the
trace gauge beginning to separate a simple determinant atom from the
continuous folded curvature.

The later atoms have larger ratios because they are still aggregating
unresolved tail mass. This is not a failure; it is the discretization
process in visible form. Increasing \(N\) should split more of the
tail into unit-multiplicity trace atoms.

### What this proves and does not prove

It proves nothing about RH by itself. It is numerical evidence only.

But it validates the Pass-3 diagnostic:

\[
\text{positive Stieltjes atoms}
\quad+\quad
\text{trace-gauge ratios near }1
\]

are the right finite microscope for the determinant model.

The next rigorous theorem to seek is:

\[
\boxed{
\text{Padé/Stieltjes atoms of }S'(x)
\text{ are positive and converge to }
\{\gamma_k^{-2}\}
\text{ with unit trace gauge.}
}
\]

That theorem is equivalent in strength to the folded determinant model,
so it must ultimately be proved from centered primorial/Archimedean
cumulant geometry, not from the zeros themselves.

This is the first executable view of the Pass-3 mountain.

### 9.1 High-precision dishwashing run

The stronger probe

\[
\texttt{probe\_pass3\_high\_precision\_pade.py}
\]

computes folded cumulants at high precision, forms the
\([N-1/N]\) Padé/Stieltjes approximants, and compares the extracted
atoms with the known values \(\gamma_k^{-2}\).

At \(N=10\), the leading atoms are:

\[
\begin{array}{c|c|c|c}
a & \lambda_a^{(10)} & w_a^{(10)}/\lambda_a^{(10)}
& \text{relative error to nearest }\gamma_k^{-2} \\
\hline
1 & 5.0052441235941160757\cdot10^{-3}
& 1.00000000000000001
& 6.17\cdot10^{-19}\\
2 & 2.2628215111878209159\cdot10^{-3}
& 1.00000000325713921
& 1.25\cdot10^{-10}\\
3 & 1.5986105998457296072\cdot10^{-3}
& 1.00000670496573028
& 3.35\cdot10^{-7}\\
4 & 1.0790307529723260943\cdot10^{-3}
& 1.02934166920316859
& 1.17\cdot10^{-3}\\
5 & 9.0928081669103026566\cdot10^{-4}
& 1.08247325956917736
& 1.37\cdot10^{-2}
\end{array}
\]

All extracted atoms in the \(N=4,6,8,10\) runs were real and positive.

### 9.2 Meaning of the run

The first three atoms are no longer just positive Stieltjes quadrature
points. They are resolving the first folded zero eigenvalues with
unit trace gauge:

\[
\frac{w_a^{(N)}}{\lambda_a^{(N)}}\to1
\]

for the resolved atoms.

This is exactly the diagnostic Pass-3 asked for:

\[
\text{sensitivity: the cumulants are seen;}
\]

\[
\text{specificity: the atoms land on }\gamma_k^{-2};
\]

\[
\text{precision: the trace-gauge ratios approach unit multiplicity.}
\]

The tail atoms still carry ratios larger than \(1\) because each finite
Padé stage compresses unresolved tail mass into a small number of
effective atoms. As \(N\) increases, more of that tail should split into
unit determinant atoms.

This is still numerical evidence, not proof. But it is a new finite
object that behaves exactly as the Pass-3 determinant model predicts.

### 9.3 The next theorem to prove

The executable evidence points to the following theorem.

**Padé trace-gauge convergence theorem.** Let \(S(x)=\log B(x)\), with

\[
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

Let

\[
S_N'(x)=
\sum_{a=1}^{N}
\frac{w_a^{(N)}}{1+\lambda_a^{(N)}x}
\]

be the \([N-1/N]\) Padé/Stieltjes approximant of \(S'(x)\). Prove,
from centered primorial/Archimedean cumulant geometry, that:

\[
\lambda_a^{(N)}>0,\qquad w_a^{(N)}>0,
\]

and for each fixed \(k\),

\[
\lambda_k^{(N)}\to\gamma_k^{-2},
\qquad
\frac{w_k^{(N)}}{\lambda_k^{(N)}}\to1.
\]

If this theorem is proved with the required trace control and local
uniform determinant convergence, it supplies the Pass-3 operators

\[
L_N^{\circ}
=
\operatorname{diag}
\left(
\lambda_1^{(N)},\ldots,\lambda_N^{(N)}
\right)
\]

and closes the determinant route.

---

## 10. Finishing the dishes: Padé is the exact detector, not a loophole

The Padé microscope is not an independent proof of RH. It is the
finite-rational detector for the same determinant property.

Let

\[
S(x)=\log B(x),
\qquad
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

The determinant target is:

\[
S'(x)=
\int_0^\infty\frac{t}{1+tx}\,d\nu_{\mathrm{count}}(t)
\]

for a positive counting measure

\[
d\nu_{\mathrm{count}}(t)=\sum_k\delta_{\lambda_k}(t),
\qquad
\lambda_k=\gamma_k^{-2}.
\]

Equivalently,

\[
S'(x)=
\sum_k\frac{\lambda_k}{1+\lambda_kx}.
\]

This is a Stieltjes transform with the trace gauge built in.

### 10.1 Padé/Stieltjes theorem schema

For a genuine positive Stieltjes function

\[
F(x)=\int_0^\infty\frac{d\sigma(t)}{1+tx},
\]

the diagonal Padé approximants

\[
F_N(x)=
\sum_{a=1}^{N}\frac{w_a^{(N)}}{1+\lambda_a^{(N)}x}
\]

are Gauss quadrature rules for \(d\sigma\). Their atoms satisfy

\[
\lambda_a^{(N)}\ge0,
\qquad
w_a^{(N)}>0.
\]

They match the first \(2N\) moments of \(d\sigma\). If \(d\sigma\) is
purely atomic and an atom is isolated, the Padé nodes resolving that atom
converge to its location and the corresponding weights converge to its
mass.

For Pass-3,

\[
d\sigma(t)=t\,d\nu_{\mathrm{count}}(t),
\]

so the mass at \(t=\lambda_k\) is exactly \(\lambda_k\). Therefore the
trace-gauge signature is

\[
\frac{w_k^{(N)}}{\lambda_k^{(N)}}\to1.
\]

This is exactly what the high-precision probe sees.

### 10.2 Exact equivalence

The following statements are equivalent:

1. RH holds.
2. \(B(x)=\Xi(i\sqrt{x})/\Xi(0)\) is a positive Fredholm determinant:

\[
B(x)=\det(I+xL_\Xi),
\qquad
L_\Xi\ge0.
\]

3. \(S'(x)\) is a trace-gauge Stieltjes transform:

\[
S'(x)=
\int_0^\infty\frac{t}{1+tx}\,d\nu_{\mathrm{count}}(t).
\]

4. The Padé/Stieltjes approximants of \(S'(x)\) have positive atoms and
converge with unit trace gauge to the folded zero eigenvalues:

\[
\lambda_k^{(N)}\to\gamma_k^{-2},
\qquad
\frac{w_k^{(N)}}{\lambda_k^{(N)}}\to1
\]

for every fixed resolved \(k\), together with bounded total trace.

### Proof

The equivalence of (1) and (2) is the positive Fredholm determinant
criterion. The equivalence of (2) and (3) follows by logarithmic
differentiation:

\[
\frac{d}{dx}\log\det(I+xL_\Xi)
=
\operatorname{Tr}\bigl(L_\Xi(I+xL_\Xi)^{-1}\bigr).
\]

For a diagonal \(L_\Xi\) with eigenvalues \(\lambda_k\), this is

\[
\sum_k\frac{\lambda_k}{1+\lambda_kx}.
\]

The Padé statement (4) is the finite Gauss-quadrature form of the same
Stieltjes transform. Positivity and convergence are standard
Stieltjes-Padé consequences once (3) holds with the stated trace control.
Conversely, if the Padé atoms converge with unit trace gauge and bounded
total trace, then the finite determinants

\[
\prod_{a=1}^{N}(1+\lambda_a^{(N)}x)
\]

converge locally uniformly to \(B(x)\), so (2) holds. \(\square\)

### 10.3 What has now been finished

The dishes now have three clean piles.

First, the **sea-level theorem** is finished:

\[
\boxed{
\text{positive determinant convergence}
\Longrightarrow
\mathrm{RH}.
}
\]

Second, the **Padé detector** is finished:

\[
\boxed{
\text{Padé positivity plus unit trace gauge}
\Longleftrightarrow
\text{positive determinant model}
\Longleftrightarrow
\mathrm{RH}.
}
\]

Third, the **remaining native task** is isolated:

\[
\boxed{
\text{derive the trace-gauge Stieltjes property of }S'(x)
\text{ from centered primorial/Archimedean cumulant geometry.}
}
\]

That last box is the only dish left in the sink.

---

## 11. Pile I: sea-level closure theorem

Pile I is the external theorem:

\[
\boxed{
\text{positive determinant convergence}
\Longrightarrow
\mathrm{RH}.
}
\]

This pile is now complete. It needs no native simplicial input once its
hypotheses are supplied.

### 11.1 Statement

Let

\[
B(x):=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

Suppose there exists a sequence of finite-rank positive operators

\[
L_j\ge0
\]

such that

\[
B_j(x):=\det(I+xL_j)
\]

converges locally uniformly on \(\mathbb C\) to \(B(x)\).

Then RH holds.

### 11.2 Proof

Since \(L_j\ge0\), its eigenvalues are real and nonnegative:

\[
\lambda_{j,a}\ge0.
\]

Therefore

\[
B_j(x)
=
\prod_a(1+\lambda_{j,a}x).
\]

Every zero of \(B_j\) lies on the nonpositive real axis:

\[
Z(B_j)\subset(-\infty,0].
\]

Because \(B_j(0)=1\) for every \(j\), the locally uniform limit satisfies

\[
B(0)=1,
\]

so \(B\) is not the zero function.

Let \(x_0\notin(-\infty,0]\). Choose a small disk \(D\) around \(x_0\)
whose closure avoids \((-\infty,0]\). Then every \(B_j\) is zero-free on
\(D\). By Hurwitz's theorem, the locally uniform limit \(B\) is either
zero-free on \(D\) or identically zero. Since \(B(0)=1\), it is not
identically zero. Hence \(B\) is zero-free on \(D\).

Thus \(B\) has no zeros off \((-\infty,0]\):

\[
Z(B)\subset(-\infty,0].
\]

Now use the fold:

\[
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

If \(x=-\gamma^2\le0\), then

\[
i\sqrt{x}=i(i\gamma)=-\gamma,
\]

up to the square-root branch, and \(\Xi\) is even. Therefore each
negative-real zero of \(B\) corresponds to a real spectral zero
\(\pm\gamma\) of \(\Xi\), and every zero of \(\Xi\) corresponds to such
an \(x\)-zero by

\[
x=-z^2.
\]

Therefore all zeros of \(\Xi\) lie on the real spectral axis. This is
RH. \(\square\)

### 11.3 Biases as signal

Each assumption contributes a different diagnostic bias.

\[
\begin{array}{c|c|c}
\text{hypothesis} & \text{bias it introduces} & \text{signal extracted}\\
\hline
L_j\ge0
& \text{zeros forced to }(-\infty,0]
& \text{determinant/PF class}\\
\text{finite rank}
& \text{polynomial stages}
& \text{finite zero ledgers}\\
\text{local-uniform convergence}
& \text{zero locations survive the limit}
& \text{Laguerre-Pólya closure}\\
B(x)=\Xi(i\sqrt{x})/\Xi(0)
& \text{folded coordinate}
& \text{negative }x\text{-zeros become real }z\text{-zeros}
\end{array}
\]

These biases are not defects. They are the detector. Remove any one of
them and the theorem loses specificity:

- without positivity, the finite zeros are not forced onto
  \((-\infty,0]\);
- without determinant form, positive quadrature can masquerade as proof;
- without local-uniform convergence, finite positivity need not reach
  \(B\);
- without the fold, negative-real zeros of \(B\) do not become RH.

So pile one is clean:

\[
\boxed{
\text{positive finite determinant bias}
\quad+\quad
\text{locally uniform limit}
\quad+\quad
\text{fold}
\quad=\quad
\mathrm{RH}.
}
\]

## 12. Pile II: Pade detector theorem

Pile II is the recognition theorem:

\[
\boxed{
\text{finite Pade curvature data}
\Longrightarrow
\text{finite positive determinant data}
}
\]

provided the trace gauge is not merely positive, but exact.

Let

\[
F(x):=S'(x),
\qquad
S(x)=\log B(x),
\qquad
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

Let \(F_N\) be a rational approximation to \(F\), in particular the
\([N-1/N]\) Pade approximant when it exists. Normalize its denominator
by \(Q_N(0)=1\). When all its poles are simple and lie on the negative
real axis, it has the partial-fraction form

\[
F_N(x)
=
\sum_{a=1}^{r_N}
\frac{w_a^{(N)}}{1+\lambda_a^{(N)}x},
\qquad
\lambda_a^{(N)}>0.
\]

The Pade detector reads the dimensionless ratios

\[
m_a^{(N)}
:=
\frac{w_a^{(N)}}{\lambda_a^{(N)}}.
\]

These are not decorative ratios. They are the multiplicities of the
finite determinant divisor, if such a divisor exists.

### 12.1 Finite exact detector

For a rational function \(F_N\), the following are equivalent.

1. There is a finite-rank positive operator \(L_N\ge0\) such that

\[
F_N(x)
=
\frac{d}{dx}\log\det(I+xL_N)
=
\operatorname{Tr}\bigl(L_N(I+xL_N)^{-1}\bigr).
\]

2. \(F_N\) has a partial-fraction expansion

\[
F_N(x)
=
\sum_{a=1}^{r_N}
\frac{w_a^{(N)}}{1+\lambda_a^{(N)}x}
\]

with

\[
\lambda_a^{(N)}>0,
\qquad
w_a^{(N)}>0,
\qquad
\frac{w_a^{(N)}}{\lambda_a^{(N)}}\in\mathbb N.
\]

3. The normalized primitive

\[
\mathcal B_N(x)
:=
\exp\left(\int_0^x F_N(t)\,dt\right)
\]

is a polynomial of the form

\[
\mathcal B_N(x)
=
\prod_{a=1}^{r_N}
\left(1+\lambda_a^{(N)}x\right)^{m_a^{(N)}},
\qquad
m_a^{(N)}\in\mathbb N.
\]

In the simple determinant case,

\[
m_a^{(N)}=1
\]

for every resolved atom. This is the unit trace gauge.

Proof:
If \(L_N\ge0\) has distinct positive eigenvalues
\(\lambda_a^{(N)}\) with multiplicities \(m_a^{(N)}\), then

\[
\det(I+xL_N)
=
\prod_a
\left(1+\lambda_a^{(N)}x\right)^{m_a^{(N)}}.
\]

Logarithmic differentiation gives

\[
\frac{d}{dx}\log\det(I+xL_N)
=
\sum_a
\frac{m_a^{(N)}\lambda_a^{(N)}}
{1+\lambda_a^{(N)}x}.
\]

Thus

\[
w_a^{(N)}
=
m_a^{(N)}\lambda_a^{(N)}.
\]

Conversely, if the partial fractions have
\(w_a^{(N)}/\lambda_a^{(N)}\in\mathbb N\), integrating \(F_N\) from
\(0\) to \(x\) gives

\[
\int_0^x F_N(t)\,dt
=
\sum_a
m_a^{(N)}
\log\left(1+\lambda_a^{(N)}x\right),
\]

so the normalized primitive is exactly the positive determinant
polynomial above. \(\square\)

### 12.2 Infinite detector

Pile II passes to RH only when the finite detector connects to the
actual folded xi function.

Assume there is a sequence \(F_N\) such that:

\[
F_N(x)
=
\frac{d}{dx}\log D_N(x),
\qquad
D_N(x)=\det(I+xL_N),
\qquad
L_N\ge0,
\]

and

\[
D_N(x)\longrightarrow B(x)
\]

locally uniformly on \(\mathbb C\).

Then RH holds by Pile I.

Equivalently, Pile II supplies Pile I with its missing finite objects.
It converts the curvature data \(F_N\) into zero-ledger data \(D_N\).

This is why plain positivity is not enough. A positive Stieltjes
quadrature has

\[
\lambda_a^{(N)}>0,
\qquad
w_a^{(N)}>0,
\]

but a positive determinant stage requires the sharper arithmetic signal

\[
\frac{w_a^{(N)}}{\lambda_a^{(N)}}\in\mathbb N.
\]

For the simple folded xi divisor, the expected resolved signal is

\[
\frac{w_a^{(N)}}{\lambda_a^{(N)}}\to1.
\]

Finite numerical Pade data therefore becomes proof only after one proves
the convergence and trace-gauge estimates that force

\[
D_N(x)
=
\prod_a
\left(1+\lambda_a^{(N)}x\right)
\longrightarrow
B(x).
\]

Without that last convergence, the Pade table is evidence. With it, the
Pade table is the determinant construction.

### 12.3 Biases as signal

The Pade detector has its own diagnostic biases.

\[
\begin{array}{c|c|c}
\text{feature} & \text{bias it introduces} & \text{signal extracted}\\
\hline
\text{negative real poles}
& \text{Stieltjes geometry}
& \text{candidate positive spectrum}\\
\text{positive residues}
& \text{positive measure}
& \text{sensitivity to cumulants}\\
w_a/\lambda_a
& \text{trace-gauge arithmetic}
& \text{determinant multiplicity}\\
\mathcal B_N=\exp\int F_N
& \text{curvature-to-divisor lift}
& \text{finite zero ledger}\\
\mathcal B_N\to B
& \text{limit discipline}
& \text{entry into Pile I}
\end{array}
\]

Thus Pile II is clean:

\[
\boxed{
\text{Pade positivity}
\quad+\quad
\text{unit trace gauge}
\quad+\quad
\text{primitive convergence}
\quad=\quad
\text{positive determinant convergence}.
}
\]

And by Pile I:

\[
\boxed{
\text{positive determinant convergence}
\quad\Longrightarrow\quad
\mathrm{RH}.
}
\]

So Pile II is finished as a theorem of recognition. It does not yet
manufacture the required trace-gauge Pade behavior from native
arithmetic geometry. That manufacturing problem is Pile III.

## 13. Pile III: native manufacture theorem

Pile III is the native theorem:

\[
\boxed{
\text{centered primorial/Archimedean cumulants}
\Longrightarrow
\text{positive trace-gauge determinant ledgers}.
}
\]

This is the only pile that is not external mathematics. Pile I is
Laguerre-Polya closure through the fold. Pile II is rational/Stieltjes
recognition. Pile III is where the simplicial program must manufacture
the finite positive ledgers from its own geometry.

### 13.1 The replacement of the old gap

The earlier closure route landed on the spectral-measure identity

\[
\frac{|\Sigma(y,\xi)|^2}{2\pi}\,d\xi
\stackrel{?}{=}
u_B(\xi,y)\,d\xi,
\qquad
u_B(\xi,y)=
\operatorname{Im}
\left(
-\frac{\Xi'}{\Xi}(\xi+iy)
\right).
\]

That was clean, but too pointwise and too exposed: it tried to identify a
Gram-Bochner square directly with the Bures Poisson field.

Pass-3 replaces that target by a folded trace statement:

\[
S'(x)
=
\int_0^\infty
\frac{t}{1+tx}\,d\nu_{\mathrm{count}}(t),
\qquad
S(x)=\log\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

The measure is not an arbitrary positive measure. It is a counting
measure:

\[
d\nu_{\mathrm{count}}(t)
=
\sum_a \delta_{\lambda_a}(t).
\]

Thus the finite native target is not

\[
\ell_m=\int t^m\,d\mu(t)
\]

for some positive weighted measure. The native target is the sharper
trace ledger

\[
\ell_m=\sum_a \lambda_a^m.
\]

This is the missing specificity. Pile III is not trying to prove broad
positivity; it is trying to produce an unweighted positive divisor ledger.

### 13.2 Native data

Let

\[
P_n:=\prod_{p\le p_n}p
\]

be the \(n\)-th primorial row. The finite arithmetic stage carries three
compatible structures:

\[
H_{P_n}
\quad
\text{mean-zero simplicial ledger;}
\]

\[
\bigoplus_{d\mid P_n,\ d>1}H_d
\quad
\text{conductor-packet decomposition;}
\]

\[
h_k=(1,\ldots,1,-k,0,\ldots,0)
\quad
\text{Helmert balance flag.}
\]

The positive-cone version is the geometric-mean gauge. For a positive
finite ledger \(x=(x_1,\ldots,x_N)\),

\[
g(x)=\left(\prod_i x_i\right)^{1/N},
\qquad
x_i\mapsto \frac{x_i}{g(x)}.
\]

After logs this is exactly arithmetic centering:

\[
y_i=\log x_i,
\qquad
y_i\mapsto y_i-\bar y.
\]

So the native object is not merely a prime cutoff. It is the centered
log-prime action:

\[
\text{prime-axis Euler action}
\quad+\quad
\text{Archimedean action}
\quad
\xrightarrow{\text{geometric-mean/additive centering}}
\quad
\text{folded trace cumulants}.
\]

### 13.3 The finite native theorem

For every finite stage \((n,T)\), Pile III must produce a finite positive
ledger

\[
\Lambda_{n,T}^{\circ}
=
\{\lambda_1^{(n,T)},\ldots,\lambda_{r(n,T)}^{(n,T)}\},
\qquad
\lambda_a^{(n,T)}\ge0,
\]

or equivalently a diagonal positive operator

\[
L_{n,T}^{\circ}
=
\operatorname{diag}
\left(
\lambda_1^{(n,T)},\ldots,\lambda_{r(n,T)}^{(n,T)}
\right)
\ge0.
\]

Its native cumulants are required to be exactly the trace power sums:

\[
\ell_m^{(n,T)}
=
\operatorname{Tr}
\left(
(L_{n,T}^{\circ})^m
\right)
=
\sum_a
\left(\lambda_a^{(n,T)}\right)^m.
\]

Equivalently, the finite folded determinant is

\[
B_{n,T}^{\circ}(x)
=
\det(I+xL_{n,T}^{\circ})
=
\prod_a
\left(1+\lambda_a^{(n,T)}x\right),
\]

and its logarithmic derivative is

\[
\frac{d}{dx}\log B_{n,T}^{\circ}(x)
=
\sum_a
\frac{\lambda_a^{(n,T)}}{1+\lambda_a^{(n,T)}x}.
\]

This is the native trace gauge. The weights are the eigenvalues
themselves. There is no independent quadrature-weight freedom.

### 13.4 The three native locks

Pile III is finished when the following three locks are proved.

**Lock A: centered cumulant convergence.** The centered
primorial/Archimedean cumulants converge to the folded xi cumulants:

\[
\ell_m^{(n,T)}
\longrightarrow
\ell_m
:=
(-1)^{m+1}m[x^m]
\log\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\]

for every \(m\ge1\).

**Lock B: trace-gauge atomization.** For every finite stage, the native
cumulants are not merely moments of a positive measure. They are power
sums of an unweighted positive eigenvalue ledger:

\[
\ell_m^{(n,T)}
=
\sum_a
\left(\lambda_a^{(n,T)}\right)^m,
\qquad
\lambda_a^{(n,T)}\ge0.
\]

This is the point where Pile III feeds Pile II. Pade positivity alone
detects a positive measure; unit trace gauge detects the determinant
ledger.

**Lock C: no escape of trace mass.** The finite ledgers obey

\[
\sup_{n,T}
\operatorname{Tr}L_{n,T}^{\circ}
=
\sup_{n,T}\sum_a\lambda_a^{(n,T)}
<\infty.
\]

This prevents mass from escaping into infinitely many unresolved tiny
atoms and gives locally uniform convergence of the determinants.

### 13.5 Native closure theorem

If Locks A, B, and C hold, then

\[
B_{n,T}^{\circ}(x)
=
\det(I+xL_{n,T}^{\circ})
\longrightarrow
B(x)
=
\frac{\Xi(i\sqrt{x})}{\Xi(0)}
\]

locally uniformly on \(\mathbb C\). Therefore Pile I applies, and RH
holds.

Proof:
Lock B gives positive finite determinants. Lock C gives normal-family
control and prevents trace escape. Lock A identifies every logarithmic
cumulant of the limit with the folded xi cumulant. Hence the determinant
limit is \(B(x)\). By Pile I, \(B\) has only zeros in
\((-\infty,0]\), so the zeros of \(\Xi\) lie on the real spectral axis.
\(\square\)

### 13.6 Biases as signal

Pile III has the deepest biases because it is the native construction.

\[
\begin{array}{c|c|c}
\text{native feature} & \text{bias it introduces} & \text{signal extracted}\\
\hline
\text{primorial row }P_n
& \text{finite prime-axis cutoff}
& \text{Euler action at finite arithmetic scale}\\
\text{geometric-mean centering}
& \text{multiplicative gauge removal}
& \text{additive mean-zero cumulants}\\
\text{conductor packets}
& \text{cyclic arithmetic resolution}
& \text{selection-rule structure}\\
\text{Helmert metric trick}
& \text{integer balances before normalization}
& \text{radical residues and prime rungs}\\
\text{Archimedean place}
& \text{continuous completion}
& \text{gamma/Tate correction}\\
\text{trace atomization}
& \text{unweighted positive divisor ledger}
& \text{determinant specificity}
\end{array}
\]

The lesson is sharp:

\[
\boxed{
\text{centering gives the right gauge;}
\quad
\text{cumulants give the right coordinates;}
\quad
\text{trace atomization gives the right positivity.}
}
\]

### 13.7 What remains mathematically open

This section finishes Pile III as a precise theorem contract. It does not
claim that Locks A, B, and C have already been proved from the native
primorial construction.

The remaining research theorem is exactly:

\[
\boxed{
\text{prove Locks A, B, C from the centered prime-axis}
\quad+\quad
\text{Archimedean cumulant tower.}
}
\]

Once that theorem is proved, the chain is closed:

\[
\boxed{
\text{Pile III}
\Longrightarrow
\text{Pile II}
\Longrightarrow
\text{Pile I}
\Longrightarrow
\mathrm{RH}.
}
\]

## 14. First attack on Lock A: the folded cumulant ledger

Lock A can be opened far enough to see the mechanism.

Let

\[
s=\frac12+y,
\qquad
x=y^2,
\qquad
S(x)=\log\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

Equivalently, using \(\Xi(z)=\xi(\frac12+iz)\),

\[
S(x)=
\log\frac{\xi(\frac12+y)}{\xi(\frac12)}.
\]

The functional equation makes this a local even function of \(y\), hence
a local function of \(x=y^2\).

Write

\[
\Gamma_{\mathbb R}(s)
:=
\pi^{-s/2}\Gamma(s/2).
\]

Then the centered folded log has the exact local split

\[
S(x)=S_{\mathrm{end}}(x)+S_{\infty}(x)+S_{\zeta}(x),
\]

where

\[
S_{\mathrm{end}}(x)=\log(1-4x),
\]

\[
S_{\infty}(x)
=
\frac12
\left[
\log\Gamma_{\mathbb R}\left(\frac12+y\right)
+
\log\Gamma_{\mathbb R}\left(\frac12-y\right)
-
2\log\Gamma_{\mathbb R}\left(\frac12\right)
\right],
\]

and, for a local branch of \(\log\zeta\) at \(s=\frac12\),

\[
S_{\zeta}(x)
=
\frac12
\left[
\log\zeta\left(\frac12+y\right)
+
\log\zeta\left(\frac12-y\right)
-
2\log\zeta\left(\frac12\right)
\right].
\]

This is not a determinant decomposition. The pieces are individually
large and alternating. The determinant-scale object is the centered sum.

Define folded cumulants by

\[
S(x)
=
\sum_{m\ge1}
(-1)^{m+1}
\frac{\ell_m}{m}x^m.
\]

The endpoint cumulants are explicit:

\[
\ell_m^{\mathrm{end}}
=
(-1)^m4^m.
\]

The Archimedean cumulants are explicit:

\[
\ell_m^{\infty}
=
(-1)^{m+1}
\frac{m}{(2m)!2^{2m}}
\psi^{(2m-1)}\left(\frac14\right),
\]

where \(\psi^{(k)}\) is the \(k\)-th polygamma function. The centered
zeta residual is then

\[
\ell_m^{\zeta}
=
\ell_m-\ell_m^{\mathrm{end}}-\ell_m^{\infty}.
\]

The probe

\[
\texttt{probe\_pass3\_cumulant\_ledger\_decomposition.py}
\]

computes this split. The first five rows are:

\[
\begin{array}{c|r|r|r|r}
m & \ell_m & \ell_m^{\mathrm{end}} & \ell_m^\infty
& \ell_m^\zeta\\
\hline
1 & 2.3104993\cdot10^{-2} & -4
& 2.1496661 & 1.8734388\\
2 & 3.7172599\cdot10^{-5} & 16
& -8.0144903 & -7.9854725\\
3 & 1.4417393\cdot10^{-7} & -64
& 32.0021168 & 31.9978834\\
4 & 6.6303168\cdot10^{-10} & 256
& -128.0003308 & -127.9996692\\
5 & 3.2136642\cdot10^{-12} & -1024
& 512.0000526 & 511.9999474
\end{array}
\]

This is the first native eureka after the three piles:

\[
\boxed{
\text{the positive trace cumulants are not raw prime moments;}
\quad
\text{they are the tiny centered residue after endpoint}
\quad+\quad
\text{Archimedean}
\quad+\quad
\text{zeta cancellation.}
}
\]

So Lock A is really three sublocks.

**Lock A1: local algebraic split.** Proved above. The folded cumulants
split exactly into endpoint, Archimedean, and centered zeta ledgers.

**Lock A2: finite native regularization.** Construct finite primorial
and height cutoffs

\[
S_{\zeta}^{(n,T),\circ}(x)
\]

whose centered limit is \(S_{\zeta}(x)\), with endpoint and Archimedean
counter-ledgers included before the limit is taken.

**Lock A3: determinant-scale residue.** Prove that after this centering,
the remaining cumulants are the power sums of a positive trace ledger:

\[
\ell_m^{(n,T)}
=
\sum_a
\left(\lambda_a^{(n,T)}\right)^m,
\qquad
\lambda_a^{(n,T)}\ge0.
\]

This reframes Pile III. The native proof is not a direct positivity proof
of the prime action. It is a renormalized centering proof:

\[
\boxed{
\text{prime action}
\quad+\quad
\text{Archimedean action}
\quad+\quad
\text{endpoint correction}
\quad
\longrightarrow
\quad
\text{positive trace residue}.
}
\]

That is the precise next mountain.

## 15. Dishwashing lemma for Lock A2: centered finite regularization works

Lock A2 asks for finite objects whose centered limit is the zeta-residual
ledger. A control version can be written down immediately with the
Dirichlet eta function.

Let

\[
\eta(s)=\sum_{n\ge1}(-1)^{n-1}n^{-s},
\qquad
\zeta(s)=\frac{\eta(s)}{1-2^{1-s}}.
\]

Use the Euler-transformed finite eta row

\[
\eta_K(s)
=
\sum_{k=0}^{K}
\frac1{2^{k+1}}
\sum_{j=0}^{k}
(-1)^j
\binom{k}{j}
(j+1)^{-s}.
\]

Define

\[
\zeta_K(s):=
\frac{\eta_K(s)}{1-2^{1-s}}.
\]

This is not yet the desired primorial construction. It is a finite
regularization scaffold. Its value is that it proves the shape of A2:
regularize first, center second, then take cumulants.

Define the centered finite zeta ledger

\[
S_{\zeta,K}^{\circ}(x)
=
\frac12
\left[
\log\frac{\zeta_K(\frac12+y)}{\zeta_K(\frac12)}
+
\log\frac{\zeta_K(\frac12-y)}{\zeta_K(\frac12)}
\right],
\qquad
x=y^2.
\]

Then

\[
S_{\zeta,K}^{\circ}(x)
\longrightarrow
S_\zeta(x)
\]

locally as \(K\to\infty\) in every sufficiently small zero-free
neighborhood of \(x=0\). Hence its coefficients converge:

\[
\ell_{m,K}^{\zeta}
\longrightarrow
\ell_m^\zeta.
\]

The probe

\[
\texttt{probe\_pass3\_lock\_a2\_eta\_regularization.py}
\]

computes these finite centered cumulants. For the first three residual
cumulants:

\[
\begin{array}{c|c|r|r|r}
K & \text{max relative error} & \ell_{1,K}^{\zeta}
& \ell_{2,K}^{\zeta}
& \ell_{3,K}^{\zeta}\\
\hline
4 & 8.30\cdot10^{-4}
& 1.87188430884721765
& -7.98513871655693854
& 31.9979000106421596\\
8 & 5.76\cdot10^{-5}
& 1.87333095099998116
& -7.98547836806662348
& 31.9978840344488966\\
12 & 3.23\cdot10^{-6}
& 1.87343280660891411
& -7.98547310750134964
& 31.9978833575668949\\
20 & 9.85\cdot10^{-9}
& 1.87343883034603228
& -7.98547249605864591
& 31.997883362330531\\
32 & 1.79\cdot10^{-12}
& 1.87343884879868565
& -7.98547249401982852
& 31.9978833624238307\\
48 & 2.03\cdot10^{-17}
& 1.87343884880203009
& -7.98547249401952517
& 31.9978833624238473
\end{array}
\]

The limit row is

\[
\ell_1^\zeta=1.87343884880203013,
\qquad
\ell_2^\zeta=-7.98547249401952517,
\qquad
\ell_3^\zeta=31.9978833624238473.
\]

So A2 has a working finite-centered regularization model.

But this is not yet Pile III. Eta regularization is a dyadic/parity
regularization. The native theorem must now replace the dyadic eta rows by
the centered primorial/conductor rows:

\[
\eta_K
\quad\leadsto\quad
\text{centered primorial row }(P_n,T),
\]

while preserving the same conclusion:

\[
S_{\zeta}^{(n,T),\circ}(x)
\longrightarrow
S_\zeta(x).
\]

This is the second native eureka:

\[
\boxed{
\text{A2 is not mysterious analytic continuation;}
\quad
\text{it is finite centering plus a chosen continuation scaffold.}
}
\]

The remaining native upgrade is to make the scaffold primorial rather
than dyadic.

## 16. Proof of the Pade trace-gauge convergence theorem

We now prove the theorem in the form that is both true and useful.

There are two layers:

1. the **Stieltjes-Pade layer**, which proves positivity and atom
   resolution once the trace-gauge Stieltjes representation is known;
2. the **determinant trace-gauge layer**, which says exactly what extra
   global condition turns the Pade quadrature table into a determinant
   ledger.

This distinction is essential. Pade gives quadrature weights. A
determinant ledger requires those weights to become the nodes themselves.

### 16.1 Statement

Let

\[
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)},
\qquad
S(x)=\log B(x),
\qquad
F(x)=S'(x).
\]

Assume the trace-gauge Stieltjes representation

\[
F(x)
=
\int_0^R
\frac{d\sigma(t)}{1+tx},
\]

where

\[
\sigma
=
\sum_{k\ge1}\lambda_k\,\delta_{\lambda_k},
\qquad
R=\lambda_1,
\qquad
\lambda_1>\lambda_2>\cdots>0,
\qquad
\sum_k\lambda_k<\infty.
\]

In the RH application,

\[
\lambda_k=\gamma_k^{-2},
\]

where \(\gamma_k\) are the positive ordinates of the spectral zeros of
\(\Xi\).

Let \(F_N\) be the \([N-1/N]\) Pade approximant of \(F\) at \(x=0\).
Then

\[
F_N(x)=
\sum_{a=1}^{N}
\frac{w_a^{(N)}}{1+\tau_a^{(N)}x}
\]

with

\[
\tau_a^{(N)}>0,
\qquad
w_a^{(N)}>0.
\]

Moreover, the quadrature measures

\[
\sigma_N:=
\sum_{a=1}^{N}
w_a^{(N)}\delta_{\tau_a^{(N)}}
\]

converge weakly to \(\sigma\). For every fixed isolated atom
\(\lambda_k\), if \(I_k\) is a small interval containing \(\lambda_k\)
and no other \(\lambda_j\), then

\[
\sum_{\tau_a^{(N)}\in I_k}w_a^{(N)}
\longrightarrow
\lambda_k.
\]

Equivalently, the Pade atoms resolve the spectral atoms in clusters. In
the simple one-node resolved regime this reads

\[
\tau_k^{(N)}\longrightarrow\lambda_k,
\qquad
\frac{w_k^{(N)}}{\tau_k^{(N)}}\longrightarrow1.
\]

This proves the local unit trace-gauge signal seen numerically.

To obtain determinant convergence, add the global trace-gauge condition

\[
\Delta_{1,N}:=
\sum_{a=1}^{N}
\left|w_a^{(N)}-\tau_a^{(N)}\right|
\longrightarrow0.
\]

Then, for every \(m\ge1\),

\[
\sum_{a=1}^{N}
\left(\tau_a^{(N)}\right)^m
\longrightarrow
\ell_m,
\]

where

\[
S(x)
=
\sum_{m\ge1}
(-1)^{m+1}\frac{\ell_m}{m}x^m.
\]

Consequently the finite determinants

\[
D_N(x):=
\prod_{a=1}^{N}
\left(1+\tau_a^{(N)}x\right)
\]

converge locally uniformly to \(B(x)\). By Pile I, RH follows.

### 16.2 Proof of the Stieltjes-Pade layer

Because \(\sigma\) is a positive finite measure on \([0,R]\),

\[
F(x)=
\int_0^R\frac{d\sigma(t)}{1+tx}
\]

is a Stieltjes function near \(x=0\). Its Taylor expansion is

\[
F(x)
=
\sum_{n\ge0}
(-1)^n \mu_n x^n,
\qquad
\mu_n=\int_0^R t^n\,d\sigma(t).
\]

The \([N-1/N]\) Pade approximant is the \(N\)-point Gaussian quadrature
rule for the measure \(\sigma\). Therefore there are nodes
\(\tau_a^{(N)}\in(0,R]\) and Christoffel weights
\(w_a^{(N)}>0\) such that

\[
F_N(x)
=
\sum_{a=1}^{N}
\frac{w_a^{(N)}}{1+\tau_a^{(N)}x},
\]

and the first \(2N\) moments are matched:

\[
\sum_{a=1}^{N}
w_a^{(N)}
\left(\tau_a^{(N)}\right)^n
=
\mu_n,
\qquad
0\le n\le 2N-1.
\]

Equivalently,

\[
\int p(t)\,d\sigma_N(t)
=
\int p(t)\,d\sigma(t)
\]

for every polynomial \(p\) of degree at most \(2N-1\).

Since the support is compact, polynomials are dense in
\(C([0,R])\). Hence

\[
\sigma_N\Rightarrow\sigma
\]

weakly. If \(I_k\) isolates the atom \(\lambda_k\), choose continuous
functions \(f_-\le\mathbf 1_{I_k}\le f_+\) supported in a slightly larger
isolating interval and equal to \(1\) on a slightly smaller one. Weak
convergence gives

\[
\int f_\pm\,d\sigma_N
\longrightarrow
\int f_\pm\,d\sigma
=
\lambda_k.
\]

Letting the buffer shrink gives

\[
\sigma_N(I_k)
=
\sum_{\tau_a^{(N)}\in I_k}
w_a^{(N)}
\longrightarrow
\lambda_k.
\]

Thus the Pade quadrature mass resolves each isolated spectral atom. In
the one-node resolved regime,

\[
w_k^{(N)}\to\lambda_k,
\qquad
\tau_k^{(N)}\to\lambda_k,
\]

and therefore

\[
\frac{w_k^{(N)}}{\tau_k^{(N)}}\to1.
\]

This proves the local Pade trace-gauge convergence theorem. \(\square\)

### 16.3 Proof of the determinant trace-gauge layer

The Pade moment identities give

\[
\ell_m
=
\mu_{m-1}
=
\sum_{a=1}^{N}
w_a^{(N)}
\left(\tau_a^{(N)}\right)^{m-1}
\]

for \(m\le 2N\). The determinant ledger built from the Pade nodes has
cumulants

\[
\ell_{m,N}^{\det}
=
\sum_{a=1}^{N}
\left(\tau_a^{(N)}\right)^m.
\]

The difference is exactly the trace-gauge defect at order \(m\):

\[
\ell_{m,N}^{\det}-\ell_m
=
\sum_{a=1}^{N}
\left(\tau_a^{(N)}-w_a^{(N)}\right)
\left(\tau_a^{(N)}\right)^{m-1}.
\]

Because \(0\le \tau_a^{(N)}\le R\),

\[
\left|
\ell_{m,N}^{\det}-\ell_m
\right|
\le
R^{m-1}
\sum_a
\left|w_a^{(N)}-\tau_a^{(N)}\right|
=
R^{m-1}\Delta_{1,N}.
\]

Thus \(\Delta_{1,N}\to0\) implies

\[
\ell_{m,N}^{\det}\to\ell_m
\]

for every fixed \(m\).

Now

\[
\log D_N(x)
=
\sum_{a=1}^{N}
\log(1+\tau_a^{(N)}x)
=
\sum_{m\ge1}
(-1)^{m+1}
\frac{\ell_{m,N}^{\det}}{m}x^m
\]

near \(x=0\). The trace bound

\[
\sum_a\tau_a^{(N)}
\le
\sum_aw_a^{(N)}+\Delta_{1,N}
=
\ell_1+\Delta_{1,N}
\]

gives normal-family control for the finite determinants. Since every
logarithmic cumulant converges to the corresponding cumulant of \(B\),
the determinants converge to \(B\) locally uniformly. Therefore Pile I
applies and RH follows. \(\square\)

### 16.4 What was proved

The theorem is now clean:

\[
\boxed{
\text{trace-gauge Stieltjes representation}
\Longrightarrow
\text{Pade positivity and local unit trace gauge}.
}
\]

And with the global defect condition:

\[
\boxed{
\Delta_{1,N}\to0
\Longrightarrow
\text{Pade nodes become positive determinant ledgers}.
}
\]

The numerical probes already see the first box strongly. They see the
second box beginning but not finished: the weights sum to \(\ell_1\)
exactly, while the node sum approaches it from below. For example:

\[
\begin{array}{c|c|c|c}
N & \sum_a w_a^{(N)} & \sum_a\tau_a^{(N)} & \Delta_{1,N}\\
\hline
4 & 0.0231049931154 & 0.00812496688032 & 0.0149800262351\\
6 & 0.0231049931154 & 0.0100642927930 & 0.0130407003224\\
8 & 0.0231049931154 & 0.0112112796919 & 0.0118937134236\\
10 & 0.0231049931154 & 0.0122311313033 & 0.0108738618121
\end{array}
\]

So the exact remaining native analytic task is not vague:

\[
\boxed{
\text{prove the global trace-gauge defect }
\Delta_{1,N}\to0
\text{ from the centered primorial/Archimedean construction.}
}
\]

That is the honest Pade theorem, with the hidden hinge exposed.

## 17. Solution of global trace-gauge convergence

The hidden hinge from Section 16 is not an additional conjecture once the
trace-gauge Stieltjes representation is granted. It follows from the
atomic trace form itself.

### 17.1 Global defect theorem

Let

\[
\sigma=\sum_{k\ge1}\lambda_k\delta_{\lambda_k},
\qquad
\lambda_1>\lambda_2>\cdots>0,
\qquad
\sum_{k\ge1}\lambda_k<\infty.
\]

Let

\[
F(x)=\int\frac{d\sigma(t)}{1+tx}
\]

and let its \([N-1/N]\) Pade approximant be

\[
F_N(x)
=
\sum_{a=1}^{N}
\frac{w_{a,N}}{1+\tau_{a,N}x},
\]

with nodes ordered

\[
\tau_{1,N}\ge\tau_{2,N}\ge\cdots\ge\tau_{N,N}>0.
\]

Then

\[
\boxed{
\Delta_{1,N}
:=
\sum_{a=1}^{N}
\left|w_{a,N}-\tau_{a,N}\right|
\longrightarrow0.
}
\]

Consequently the finite Pade node determinants

\[
D_N(x)=
\prod_{a=1}^{N}(1+\tau_{a,N}x)
\]

converge locally uniformly to

\[
\prod_{k\ge1}(1+\lambda_kx).
\]

### 17.2 Node domination

Work in the Hilbert space

\[
\mathcal H=L^2(\sigma).
\]

Multiplication by \(t\),

\[
(Mf)(t)=t f(t),
\]

is a compact positive operator. Since \(\sigma\) is supported on the
points \(\lambda_k\), the nonzero eigenvalues of \(M\) are exactly

\[
\lambda_1,\lambda_2,\ldots .
\]

Let \(\mathcal P_{N-1}\) be the \(N\)-dimensional subspace spanned by
polynomials of degree at most \(N-1\), viewed inside \(L^2(\sigma)\), and
let \(P_N\) be the orthogonal projection onto \(\mathcal P_{N-1}\).

The Gaussian quadrature nodes \(\tau_{a,N}\) are the eigenvalues of the
compressed multiplication operator

\[
P_NMP_N\big|_{\mathcal P_{N-1}}.
\]

By the min-max principle for positive compact operators,

\[
\boxed{
\tau_{a,N}\le\lambda_a
\qquad
1\le a\le N.
}
\]

This is the tail-control mechanism. It says the Pade nodes cannot carry
more trace mass in the tail than the true trace ledger.

### 17.3 Local atom convergence

The Pade quadrature measures

\[
\sigma_N:=
\sum_{a=1}^{N}w_{a,N}\delta_{\tau_{a,N}}
\]

match the first \(2N\) moments of \(\sigma\). Since the support of
\(\sigma\) is compact, polynomial density gives

\[
\sigma_N\Rightarrow\sigma
\]

weakly.

Fix \(K\). Choose disjoint intervals

\[
I_k=(\alpha_k,\beta_k),
\qquad
1\le k\le K,
\]

with

\[
\lambda_{k+1}<\alpha_k<\lambda_k<\beta_k<\lambda_{k-1}
\]

where the upper inequality is omitted for \(k=1\).

Weak convergence gives

\[
\sigma_N(I_k)\to\sigma(I_k)=\lambda_k.
\]

Therefore each \(I_k\) contains at least one Pade node for all large
\(N\). Node domination prevents extra head nodes: since

\[
\tau_{k+1,N}\le\lambda_{k+1}<\alpha_k,
\]

there are at most \(k\) nodes above \(\alpha_k\). Inducting downward
through \(I_1,\ldots,I_k\), each \(I_k\) contains exactly one of the first
\(k\) nodes for large \(N\). Hence, after shrinking the intervals,

\[
\tau_{k,N}\to\lambda_k,
\qquad
w_{k,N}\to\lambda_k
\]

for every fixed \(k\).

Thus the local unit trace gauge is not merely numerical:

\[
\frac{w_{k,N}}{\tau_{k,N}}\to1.
\]

### 17.4 Tail closure

Now split the global defect at a fixed \(K\):

\[
\Delta_{1,N}
\le
\sum_{a=1}^{K}
\left|w_{a,N}-\tau_{a,N}\right|
+
\sum_{a>K}w_{a,N}
+
\sum_{a>K}\tau_{a,N}.
\]

The head term tends to \(0\) by local atom convergence.

For the weight tail,

\[
\sum_{a>K}w_{a,N}
=
\sum_{a\ge1}\lambda_a
-
\sum_{a=1}^{K}w_{a,N}
\longrightarrow
\sum_{a>K}\lambda_a.
\]

For the node tail, node domination gives

\[
\sum_{a>K}\tau_{a,N}
\le
\sum_{a>K}\lambda_a.
\]

Therefore

\[
\limsup_{N\to\infty}\Delta_{1,N}
\le
2\sum_{a>K}\lambda_a.
\]

Since

\[
\sum_a\lambda_a<\infty,
\]

the tail \(\sum_{a>K}\lambda_a\) tends to \(0\) as \(K\to\infty\). Hence

\[
\Delta_{1,N}\to0.
\]

This proves the global trace-gauge convergence theorem. \(\square\)

### 17.5 Consequence for Pass-3

Section 16 required \(\Delta_{1,N}\to0\) as an extra hinge. Section 17
proves that hinge from the pure atomic trace-gauge representation.

So the Pade layer is now fully closed:

\[
\boxed{
\text{trace-gauge Stieltjes representation}
\Longrightarrow
\text{Pade positivity}
\Longrightarrow
\Delta_{1,N}\to0
\Longrightarrow
\text{positive determinant convergence}.
}
\]

What remains is not a Pade problem. It is the native manufacture problem:
prove that the centered primorial/Archimedean cumulant tower produces the
trace-gauge Stieltjes representation in the first place.

## 18. The native trace-gauge theorem is the RH core

We now attempt the requested final step:

\[
\boxed{
\text{centered primorial/Archimedean cumulant tower}
\Longrightarrow
\text{trace-gauge Stieltjes representation.}
}
\]

This cannot be treated as a harmless remaining lemma. It is exactly the
Riemann Hypothesis in native language.

### 18.1 Exact equivalence theorem

Let

\[
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)},
\qquad
S(x)=\log B(x),
\qquad
F(x)=S'(x)=\frac{B'(x)}{B(x)}.
\]

The following statements are equivalent.

1. \(F\) has the trace-gauge Stieltjes representation

\[
F(x)=
\sum_{k\ge1}
\frac{\lambda_k}{1+\lambda_k x},
\qquad
\lambda_k>0,
\qquad
\sum_k\lambda_k<\infty.
\]

2. \(B\) is a positive Fredholm determinant

\[
B(x)=
\prod_{k\ge1}(1+\lambda_k x)
=
\det(I+xL),
\qquad
L\ge0,
\qquad
\operatorname{Tr}L<\infty.
\]

3. All zeros of \(B\) lie on the nonpositive real axis.

4. All zeros of \(\Xi\) lie on the real spectral axis.

5. RH holds.

### 18.2 Proof

\((1)\Rightarrow(2)\). Integrating \(F\) from \(0\) to \(x\) gives

\[
S(x)=
\sum_k
\log(1+\lambda_k x),
\]

because \(S(0)=0\). Since \(\sum_k\lambda_k<\infty\), the product

\[
\prod_k(1+\lambda_k x)
\]

converges locally uniformly. Therefore

\[
B(x)=e^{S(x)}
=
\prod_k(1+\lambda_k x)
=
\det(I+xL)
\]

for \(L=\operatorname{diag}(\lambda_1,\lambda_2,\ldots)\ge0\).

\((2)\Rightarrow(3)\). Every factor \(1+\lambda_kx\) has its zero at

\[
x=-\lambda_k^{-1}\le0.
\]

Therefore all zeros of \(B\) lie on \((-\infty,0]\).

\((3)\Rightarrow(1)\). If \(B\) has only nonpositive real zeros, write
them as

\[
x_k=-\lambda_k^{-1},
\qquad
\lambda_k>0.
\]

The folded xi function has order compatible with the trace condition
\(\sum_k\lambda_k<\infty\); equivalently, the spectral ordinates satisfy
\(\sum_k\gamma_k^{-2}<\infty\). Hence the canonical product has genus
zero in the folded variable:

\[
B(x)=\prod_k(1+\lambda_k x).
\]

Logarithmic differentiation gives

\[
F(x)=\frac{B'(x)}{B(x)}
=
\sum_k\frac{\lambda_k}{1+\lambda_kx}.
\]

This is exactly the trace-gauge Stieltjes representation.

\((3)\Leftrightarrow(4)\). The fold is

\[
B(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)}.
\]

A zero \(x=-\gamma^2\le0\) of \(B\) corresponds to spectral zeros
\(\pm\gamma\) of \(\Xi\). Conversely, a spectral zero \(z\) of \(\Xi\)
maps to \(x=-z^2\). Thus nonpositive real zeros of \(B\) are exactly real
spectral zeros of \(\Xi\).

\((4)\Leftrightarrow(5)\). This is the standard spectral-coordinate
form of RH for

\[
\Xi(z)=\xi\left(\frac12+iz\right).
\]

Thus all five statements are equivalent. \(\square\)

### 18.3 Consequence for the native program

The requested theorem

\[
\text{centered primorial/Archimedean cumulants}
\Longrightarrow
\text{trace-gauge Stieltjes}
\]

is not a lower-altitude support lemma. It is the summit.

The work above proves the exact logical position:

\[
\boxed{
\text{native trace-gauge theorem}
\Longleftrightarrow
\mathrm{RH}.
}
\]

So there is no honest way to finish it by appealing only to the already
proved centering, eta regularization, Pade convergence, or determinant
closure. Those ingredients prepare the target; they do not by themselves
force the target.

### 18.4 The actual proof obligation

Let

\[
F(x)=
\sum_{n\ge0}(-1)^n\ell_{n+1}x^n.
\]

To prove the trace-gauge Stieltjes representation without assuming RH, the
native tower must prove that the sequence

\[
\mu_n:=\ell_{n+1}
\]

is the moment sequence of the positive atomic trace measure

\[
d\sigma(t)=\sum_k\lambda_k\delta_{\lambda_k}(t).
\]

A concrete sufficient route is:

\[
\boxed{
\text{prove all finite Hankel forms from the centered tower.}
}
\]

Namely, for every polynomial

\[
p(t)=\sum_{j=0}^d c_jt^j,
\]

prove

\[
\sum_{i,j=0}^d c_ic_j\,\mu_{i+j}\ge0,
\]

and prove the bounded-support/localization constraints needed to place the
measure on \([0,R]\). Then use the meromorphicity of

\[
F=\frac{B'}{B}
\]

to upgrade the positive measure to a discrete atomic measure. Finally use
the residue theorem for \(B'/B\) to force the trace gauge

\[
w_k=\lambda_k
\]

at every simple folded zero.

This is now the exact native research theorem:

\[
\boxed{
\text{centered primorial/Archimedean cumulant tower}
\Longrightarrow
\text{Hankel positivity + support control + meromorphic atomization.}
}
\]

That theorem would prove RH. It is the remaining mountain, not a dish that
can be washed by notation.

### 18.5 What is already solved around the core

The surrounding dishes are clean:

\[
\text{A1: folded endpoint/Archimedean/zeta split}
\quad\text{is explicit;}
\]

\[
\text{A2: finite centered regularization}
\quad\text{has a working eta scaffold;}
\]

\[
\text{Pade recognition}
\quad\text{is proved;}
\]

\[
\text{global trace-gauge convergence}
\quad\text{is proved once trace-gauge Stieltjes holds;}
\]

\[
\text{positive determinant convergence}
\quad\text{implies RH.}
\]

The only unsolved assertion is therefore precisely the one that must be
new mathematics:

\[
\boxed{
\text{native Hankel/Stieltjes positivity of the centered}
\quad
\text{primorial/Archimedean cumulants.}
}
\]

This is where the next real discovery has to occur.

## 19. Attack on the Hankel lock

The native trace-gauge theorem can now be rewritten as a pure finite
positivity problem.

Let

\[
F(x)=S'(x)
=
\sum_{n\ge0}(-1)^n\mu_nx^n,
\qquad
\mu_n:=\ell_{n+1}.
\]

If \(F\) is the trace-gauge Stieltjes transform of a positive measure on
\([0,R]\), then

\[
\mu_n=\int_0^R t^n\,d\sigma(t).
\]

The bounded Stieltjes/Hausdorff moment criterion says that this is
equivalent to the positivity of the finite Hankel and localizing forms:

\[
H_d^{(0)}=(\mu_{i+j})_{0\le i,j\le d}\succeq0,
\]

\[
H_d^{(1)}=(\mu_{i+j+1})_{0\le i,j\le d}\succeq0,
\]

and

\[
H_{d,R}^{(\mathrm{top})}
=
(R\mu_{i+j}-\mu_{i+j+1})_{0\le i,j\le d}
\succeq0
\]

for every \(d\ge0\). Equivalently, for every polynomial \(p\),

\[
\int_0^R p(t)^2\,d\sigma(t)\ge0,
\]

\[
\int_0^R t\,p(t)^2\,d\sigma(t)\ge0,
\]

and

\[
\int_0^R (R-t)p(t)^2\,d\sigma(t)\ge0.
\]

This is the clean native positivity target:

\[
\boxed{
\text{prove these quadratic forms directly from the centered}
\quad
\text{primorial/Archimedean cumulant tower.}
}
\]

### 19.1 Numerical Hankel evidence

The probe

\[
\texttt{probe\_pass3\_hankel\_lock.py}
\]

computes the matrices above from the folded cumulants. With

\[
R=\gamma_1^{-2}
=
0.0050052441235941160788094\ldots,
\]

the minimum eigenvalues are:

\[
\begin{array}{c|c|c|c|c}
d+1 & \lambda_{\min}(H^{(0)})
& \lambda_{\min}(H^{(1)})
& \lambda_{\min}(H^{(\mathrm{top})}_R)
& \det H^{(0)}
\\
\hline
1 & 2.31049931154\cdot10^{-2}
& 3.71725992853\cdot10^{-5}
& 7.84735317314\cdot10^{-5}
& 2.31049931154\cdot10^{-2}\\
2 & 8.43683657201\cdot10^{-8}
& 1.03851505420\cdot10^{-10}
& 3.62391102953\cdot10^{-11}
& 1.94933555482\cdot10^{-9}\\
3 & 1.11461250590\cdot10^{-13}
& 8.08146703755\cdot10^{-17}
& 1.46133907978\cdot10^{-17}
& 2.17281051053\cdot10^{-22}\\
4 & 5.41936593894\cdot10^{-20}
& 2.96209160841\cdot10^{-23}
& 4.30370890844\cdot10^{-24}
& 1.17758171601\cdot10^{-41}\\
5 & 1.66617101880\cdot10^{-26}
& 8.51064095745\cdot10^{-30}
& 1.00396582789\cdot10^{-30}
& 1.96218205321\cdot10^{-67}\\
6 & 4.12689247267\cdot10^{-33}
& 1.57280049074\cdot10^{-36}
& 1.17014038535\cdot10^{-37}
& 8.09839948319\cdot10^{-100}\\
7 & 5.13634401039\cdot10^{-40}
& 1.39772237438\cdot10^{-43}
& 8.57869450716\cdot10^{-45}
& 4.16003790027\cdot10^{-139}\\
8 & 3.80722107195\cdot10^{-47}
& 1.05039254682\cdot10^{-50}
& 7.08236967279\cdot10^{-52}
& 1.58399847720\cdot10^{-185}
\end{array}
\]

All tested forms are positive.

This is not proof of RH. It is a finite diagnostic showing that the
folded cumulants sit exactly where the trace-gauge theorem predicts.

### 19.2 Why this is the right lock

The older positivity targets were too broad. Bochner positivity gives
squares. Stieltjes positivity gives positive measures. But RH needs the
bounded trace-gauge version:

\[
\text{positive measure on }[0,R]
\quad+\quad
\text{meromorphic atomization}
\quad+\quad
\text{residue trace gauge}.
\]

Hankel positivity supplies the first part. The upper localizer

\[
R\mu_{i+j}-\mu_{i+j+1}
\]

supplies the support ceiling. Meromorphicity of \(F=B'/B\) supplies
atomization. Finally, the residue identity for logarithmic derivatives
supplies multiplicity:

\[
F(x)\sim \frac{m}{x-x_0}
\]

at a zero \(x_0\) of \(B\). If \(x_0=-1/t\), then a Stieltjes atom
\(w\delta_t\) contributes

\[
\frac{w}{1+tx}
=
\frac{w/t}{x+1/t}.
\]

Thus

\[
\frac{w}{t}=m,
\qquad
w=mt.
\]

For simple folded zeros, \(m=1\), so

\[
w=t.
\]

This is the trace gauge.

### 19.3 The next theorem to prove

The native theorem has now been reduced to the following exact statement.

**Native Hankel Positivity Theorem.** The centered
primorial/Archimedean cumulant construction produces moments

\[
\mu_n^{(n,T)}
\]

such that, in the limit \((n,T)\to\infty\), every finite Hankel and upper
localizing form is nonnegative:

\[
(\mu_{i+j})_{0\le i,j\le d}\succeq0,
\]

\[
(\mu_{i+j+1})_{0\le i,j\le d}\succeq0,
\]

\[
(R\mu_{i+j}-\mu_{i+j+1})_{0\le i,j\le d}\succeq0.
\]

If this theorem is proved, then the centered cumulants define a positive
measure on \([0,R]\). Because \(F=B'/B\) is meromorphic, the measure is
atomic. Because \(F\) is a logarithmic derivative, the atom weights obey
the trace gauge. Therefore the trace-gauge Stieltjes representation
holds, and RH follows by the already proved chain.

This is the remaining proof in its most compressed form:

\[
\boxed{
\text{native centered tower}
\Longrightarrow
\text{bounded Hankel positivity}
\Longrightarrow
\text{trace-gauge Stieltjes}
\Longrightarrow
\mathrm{RH}.
}
\]

## 20. T4 bridge: Helmert squares for the Hankel lock

T4 was missing from the earlier Pass-2 view. With it, the Hankel lock is
no longer an abstract list of inequalities. It becomes a native square
representation problem.

T4 supplies three ingredients:

\[
\text{centering and rebalancing}
\quad
\text{all the way down;}
\]

\[
\text{geometric-mean gauge}
\quad\xleftrightarrow{\log}\quad
\text{additive centering;}
\]

\[
\text{unnormalized Helmert balances}
\quad
h_k=(1,\ldots,1,-k,0,\ldots,0).
\]

The metric trick keeps the incidence data integral and stores the
normalization in the metric:

\[
\langle h_j,h_k\rangle
=
k(k+1)\delta_{jk}
\]

up to the ambient normalization convention. Thus T4 gives a canonical
orthogonal balance flag on every finite centered ledger.

The remaining RH-strength question can now be asked in T4 language:

\[
\boxed{
\text{can the centered primorial/Archimedean cumulants be represented}
\quad
\text{as Helmert-balance Gram squares?}
}
\]

### 20.1 Helmert square criterion

For every finite row \((n,T)\), suppose T4 constructs:

1. a finite real Hilbert space \(\mathcal H_{n,T}^{H}\) generated by
   centered Helmert/conductor balance packets;
2. a distinguished cyclic vector \(\Omega_{n,T}\in\mathcal H_{n,T}^{H}\);
3. a self-adjoint operator \(A_{n,T}\) satisfying

\[
0\preceq A_{n,T}\preceq R I;
\]

4. native folded moments

\[
\mu_m^{(n,T)}
=
\left\langle
\Omega_{n,T},
A_{n,T}^{m}
\Omega_{n,T}
\right\rangle.
\]

Then all finite Hankel and upper-support localizing forms are
nonnegative:

\[
\bigl(\mu_{i+j}^{(n,T)}\bigr)_{i,j=0}^{d}\succeq0,
\]

\[
\bigl(\mu_{i+j+1}^{(n,T)}\bigr)_{i,j=0}^{d}\succeq0,
\]

\[
\bigl(R\mu_{i+j}^{(n,T)}-\mu_{i+j+1}^{(n,T)}\bigr)_{i,j=0}^{d}
\succeq0.
\]

### Proof

For a polynomial

\[
p(t)=\sum_{i=0}^{d}c_it^i,
\]

we have

\[
\sum_{i,j=0}^{d}c_ic_j\mu_{i+j}^{(n,T)}
=
\left\langle
p(A_{n,T})\Omega_{n,T},
p(A_{n,T})\Omega_{n,T}
\right\rangle
\ge0.
\]

Similarly,

\[
\sum_{i,j=0}^{d}c_ic_j\mu_{i+j+1}^{(n,T)}
=
\left\langle
A_{n,T}^{1/2}p(A_{n,T})\Omega_{n,T},
A_{n,T}^{1/2}p(A_{n,T})\Omega_{n,T}
\right\rangle
\ge0.
\]

Finally, since \(0\preceq A_{n,T}\preceq RI\),

\[
R I-A_{n,T}\succeq0,
\]

and therefore

\[
\sum_{i,j=0}^{d}c_ic_j
\left(R\mu_{i+j}^{(n,T)}-\mu_{i+j+1}^{(n,T)}\right)
\]

\[
=
\left\langle
(RI-A_{n,T})^{1/2}p(A_{n,T})\Omega_{n,T},
(RI-A_{n,T})^{1/2}p(A_{n,T})\Omega_{n,T}
\right\rangle
\ge0.
\]

Thus the Hankel lock follows from a bounded positive Helmert square
representation. \(\square\)

### 20.2 Why this is native

This criterion is exactly where T4 matters.

Without T4, the moment problem asks for positivity in an abstract
sequence:

\[
\mu_0,\mu_1,\mu_2,\ldots.
\]

With T4, the same sequence is asked to come from a concrete balance
geometry:

\[
\mu_m
=
\text{energy of the }m\text{-th folded balance mode}.
\]

The geometric-mean gauge explains why the raw prime action must be
centered before it can become positive. The Helmert flag explains how
finite centered ledgers can become orthogonal balance packets. The metric
trick explains why square roots and radical residues belong in the metric,
not necessarily in the incidence coordinates.

So the next native theorem is sharper than Section 19:

\[
\boxed{
\text{construct }(\mathcal H_{n,T}^{H},\Omega_{n,T},A_{n,T})
\text{ from the T4-centered primorial/Archimedean tower.}
}
\]

If this construction satisfies

\[
0\preceq A_{n,T}\preceq RI
\]

and

\[
\mu_m^{(n,T)}
\longrightarrow
\mu_m,
\]

then bounded Hankel positivity follows by the theorem above. Then
Sections 18 and 19 give the trace-gauge Stieltjes representation and the
RH chain.

### 20.3 The third native eureka

The remaining theorem is not:

\[
\text{prove infinitely many Hankel determinants one by one.}
\]

It is:

\[
\boxed{
\text{find the T4 Helmert square root of the centered xi cumulants.}
}
\]

In plain program language:

\[
\boxed{
\text{T4 turns the Hankel lock from a determinant inequality problem}
\quad
\text{into a native square-root construction problem.}
}
\]

That is a real simplification.

## 21. Surprise God: the finite GNS/Jacobi square root

The previous section says that T4 should produce a bounded positive
Helmert-balance operator. There is a canonical abstract version of that
operator whenever the Hankel lock holds: the GNS/Jacobi multiplication
operator of the moment sequence.

This is not yet the native T4 construction, but it is the exact finite
square root that the native construction must identify.

### 21.1 GNS construction

Let

\[
\mu_0,\mu_1,\ldots,\mu_{2N}
\]

be a finite folded moment packet satisfying the Hankel and upper-localizer
positivity conditions:

\[
(\mu_{i+j})_{0\le i,j\le N}\succeq0,
\]

\[
(\mu_{i+j+1})_{0\le i,j\le N-1}\succeq0,
\]

\[
(R\mu_{i+j}-\mu_{i+j+1})_{0\le i,j\le N-1}\succeq0.
\]

Define an inner product on polynomials of degree at most \(N\) by

\[
\langle p,q\rangle_\mu
=
\sum_{i,j}p_iq_j\mu_{i+j},
\qquad
p(t)=\sum_i p_it^i,
\quad
q(t)=\sum_j q_jt^j.
\]

Quotient by the null space and complete the finite-dimensional space. Let
\(\Omega\) be the class of the constant polynomial \(1\). Let \(A\) be
compressed multiplication by \(t\):

\[
A[p(t)]=[t\,p(t)].
\]

Then

\[
\mu_m=\langle \Omega,A^m\Omega\rangle
\]

for all available \(m\), and the localizer inequalities give

\[
0\preceq A\preceq RI.
\]

Thus the Hankel lock is equivalent, at finite level, to existence of a
bounded positive cyclic square-root operator.

### 21.2 Jacobi matrix form

Choose the orthonormal polynomial basis

\[
P_0(t),P_1(t),\ldots,P_{N-1}(t)
\]

generated by Gram-Schmidt from \(1,t,t^2,\ldots\) under
\(\langle\cdot,\cdot\rangle_\mu\). In this basis, \(A\) is the symmetric
Jacobi matrix

\[
J_N=(\langle P_i,tP_j\rangle_\mu)_{0\le i,j<N}.
\]

Its eigenvalues are exactly the Gaussian/Pade nodes

\[
\tau_{a,N},
\]

and the spectral weights of the cyclic vector \(\Omega\) are

\[
w_{a,N}.
\]

So the Pade microscope and the Hankel square root are the same finite
object in two languages:

\[
\boxed{
\text{Pade nodes}
\quad=\quad
\text{spectrum of the finite GNS multiplication operator}.
}
\]

### 21.3 Numerical square-root run

The probe

\[
\texttt{probe\_pass3\_gns\_helmert\_square\_operator.py}
\]

constructs \(J_N\) directly from the folded cumulant moments.

For \(N=10\), using

\[
R=\gamma_1^{-2}
=
0.0050052441235941160788094\ldots,
\]

it finds

\[
\lambda_{\min}(J_{10})
=
7.50732746589203751\cdot10^{-6},
\]

\[
\lambda_{\max}(J_{10})
=
0.00500524412359411608,
\]

so the finite operator is positive and sits under the expected support
ceiling.

Its leading spectral data are:

\[
\begin{array}{c|c|c|c}
a & \tau_{a,10} & w_{a,10}/\tau_{a,10}
& \text{relative error to nearest }\gamma_k^{-2}\\
\hline
1 & 5.0052441235941160757\cdot10^{-3}
& 1.00000000000000001
& 6.17\cdot10^{-19}\\
2 & 2.2628215111878209159\cdot10^{-3}
& 1.00000000325713921
& 1.25\cdot10^{-10}\\
3 & 1.5986105998457296072\cdot10^{-3}
& 1.00000670496573028
& 3.35\cdot10^{-7}\\
4 & 1.0790307529723260943\cdot10^{-3}
& 1.02934166920316859
& 1.17\cdot10^{-3}\\
5 & 9.0928081669103026566\cdot10^{-4}
& 1.08247325956917736
& 1.37\cdot10^{-2}
\end{array}
\]

This is the same spectrum seen by the Pade probe, now produced as the
finite multiplication operator of the moment Hilbert space.

### 21.4 What T4 must add

The GNS construction proves existence of an abstract finite square root
when the moment forms are positive. T4 asks for more:

\[
\boxed{
\text{identify this GNS/Jacobi square root with a native}
\quad
\text{Helmert-conductor balance operator.}
}
\]

That is the surprise reduction:

\[
\text{RH core}
\quad\leadsto\quad
\text{bounded Hankel positivity}
\quad\leadsto\quad
\text{finite GNS operator}
\quad\leadsto\quad
\text{native T4 identification}.
\]

We no longer need to guess the shape of the operator. The moment sequence
constructs it. The remaining native work is to show that the same operator
is produced by the centered primorial/Archimedean Helmert balance tower.

## 22. Helmert realization of the GNS/Jacobi operator

Now use T4 explicitly.

For a ledger of size \(N+1\), let

\[
e_0^{H},e_1^{H},\ldots,e_{N-1}^{H}
\]

be the unit Helmert balances in the mean-zero space \(H_{N+1}\). These are
the normalized versions of

\[
h_k=(1,\ldots,1,-k,0,\ldots,0).
\]

Given the finite GNS/Jacobi matrix

\[
J_N=(\langle P_i,tP_j\rangle_\mu)_{0\le i,j<N},
\]

define the Helmert-ladder operator

\[
A_N^{H}
=
\sum_{i=0}^{N-1}\alpha_i
|e_i^{H}\rangle\langle e_i^{H}|
+
\sum_{i=0}^{N-2}\beta_i
\left(
|e_i^{H}\rangle\langle e_{i+1}^{H}|
+
|e_{i+1}^{H}\rangle\langle e_i^{H}|
\right),
\]

where

\[
\alpha_i=J_{i,i},
\qquad
\beta_i=J_{i,i+1}.
\]

Let

\[
\Omega_N^{H}
=
\sqrt{\mu_0}\,e_0^{H}.
\]

Then

\[
\boxed{
\mu_m
=
\langle\Omega_N^{H},(A_N^{H})^m\Omega_N^{H}\rangle
}
\]

for every \(m\) within the finite moment range.

### Proof

Map the orthonormal polynomial basis

\[
P_i(t)
\]

to the unit Helmert balance basis

\[
e_i^{H}.
\]

This is a unitary identification of the finite GNS Hilbert space with the
T4 Helmert balance space. Under this unitary map, multiplication by \(t\)
becomes exactly the tridiagonal operator \(A_N^{H}\) above. The cyclic
vector \(1\) has norm \(\sqrt{\mu_0}\), hence maps to
\(\Omega_N^{H}=\sqrt{\mu_0}e_0^H\). Therefore the cyclic moments are
preserved:

\[
\langle 1,t^m1\rangle_\mu
=
\langle\Omega_N^{H},(A_N^{H})^m\Omega_N^{H}\rangle.
\]

But

\[
\langle 1,t^m1\rangle_\mu=\mu_m.
\]

Thus the moment ledger is realized on the Helmert ladder. \(\square\)

### 22.1 Meaning

This is a finite native identification theorem:

\[
\boxed{
\text{GNS/Jacobi square root}
\quad\cong\quad
\text{Helmert nearest-neighbor balance operator}.
}
\]

The theorem is not yet the RH proof, because the coefficients

\[
\alpha_i,\beta_i
\]

were extracted from the folded xi moments. The remaining native theorem is
that the centered primorial/Archimedean T4 construction produces these
coefficients, or a convergent sequence of them, without importing the xi
zero data.

That final target is now coefficient-level:

\[
\boxed{
\text{derive the Jacobi coefficients }
\alpha_i,\beta_i
\text{ from the centered primorial/Archimedean Helmert tower.}
}
\]

### 22.2 Numerical Helmert coefficients

The probe

\[
\texttt{probe\_pass3\_gns\_helmert\_square\_operator.py}
\]

now prints the Jacobi/Helmert ladder coefficients. For \(N=10\):

\[
\begin{array}{c|c|c}
i & \alpha_i & \beta_i\\
\hline
0 & 1.6088556745971409753\cdot10^{-3}
& 1.9108977920880258769\cdot10^{-3}\\
1 & 3.5005892352730682116\cdot10^{-3}
& 1.1494160158980175921\cdot10^{-3}\\
2 & 1.7983431372353904753\cdot10^{-3}
& 6.9729568160293123921\cdot10^{-4}\\
3 & 1.2171788332190334042\cdot10^{-3}
& 5.5448464298934773386\cdot10^{-4}\\
4 & 1.0732981583828999834\cdot10^{-3}
& 4.9768646031058824681\cdot10^{-4}\\
5 & 8.6602775434100430853\cdot10^{-4}
& 3.5279229952673136494\cdot10^{-4}\\
6 & 5.9870139920799588771\cdot10^{-4}
& 2.7225739864534062216\cdot10^{-4}\\
7 & 5.4828549960681088023\cdot10^{-4}
& 2.8677481655095860587\cdot10^{-4}\\
8 & 5.6962982929156519875\cdot10^{-4}
& 2.5561797332095754504\cdot10^{-4}\\
9 & 4.5022178217623604602\cdot10^{-4}
& 0
\end{array}
\]

These are the finite balance couplings. In T4 language, \(\alpha_i\) are
on-rung energies and \(\beta_i\) are nearest-rung transfer couplings along
the centered balance ladder.

The next native question is therefore no longer global:

\[
\text{Why are these couplings positive, bounded, and convergent?}
\]

It is local along the ladder.

### 22.3 New final form of the RH core

The RH core has become:

\[
\boxed{
\text{centered primorial/Archimedean tower}
\Longrightarrow
\text{convergent positive Helmert-Jacobi coefficients}
\Longrightarrow
\text{bounded GNS operator}
\Longrightarrow
\mathrm{RH}.
}
\]

This is the cleanest native version so far.

## 23. Jacobi coefficient flow: fixed-rung stability

The probe

\[
\texttt{probe\_pass3\_jacobi\_coefficient\_flow.py}
\]

tracks the finite GNS/Jacobi coefficients for window sizes

\[
N=4,6,8,10,12.
\]

It reports the same first rungs whenever those rungs exist. Against the
\(N=12\) window, the displayed fixed-rung differences are

\[
\begin{array}{c|c|c}
N
&
\max_{i<\min(N,6)}|\alpha_i^{(N)}-\alpha_i^{(12)}|
&
\max_{i<\min(N-1,6)}|\beta_i^{(N)}-\beta_i^{(12)}|\\
\hline
4 & 0 & 0\\
6 & 0 & 0\\
8 & 0 & 0\\
10 & 0 & 0
\end{array}
\]

This is exactly what the native ladder asks for.

### 23.1 Finite-prefix theorem

Let

\[
(\mu_0,\mu_1,\mu_2,\ldots)
\]

be a positive moment ledger, and let

\[
\alpha_i,\beta_i
\]

be the Jacobi coefficients obtained by Gram-Schmidt orthonormalization of

\[
1,t,t^2,\ldots
\]

with respect to the moment pairing

\[
\langle t^a,t^b\rangle=\mu_{a+b}.
\]

Then the coefficient \(\alpha_i\) and the coupling \(\beta_i\) are
determined by only a finite prefix of the ledger. More precisely,
\(\alpha_i\) depends only on moments through \(\mu_{2i+1}\), and
\(\beta_i\) depends only on moments through \(\mu_{2i+2}\). Enlarging the
window appends later rungs; it does not rewrite the settled lower rungs.

### Proof

The \(i\)-th orthonormal polynomial is obtained from

\[
1,t,\ldots,t^i
\]

using only inner products among these monomials. Those inner products are

\[
\langle t^a,t^b\rangle=\mu_{a+b},
\qquad
0\leq a,b\leq i.
\]

Thus the construction of \(P_i(t)\) uses only a finite Hankel block of
moments. The diagonal coefficient

\[
\alpha_i=\langle P_i,tP_i\rangle
\]

uses moments from a finite enlargement of the same block. The
off-diagonal coefficient

\[
\beta_i=\langle P_i,tP_{i+1}\rangle
\]

uses the finite block needed to construct \(P_{i+1}\). Therefore each
fixed rung is a finite-prefix invariant of the moment ledger. \(\square\)

### 23.2 Meaning

The trace-gauge target is now local:

\[
\boxed{
\text{prove the native centered tower produces the finite prefixes}
\quad
\alpha_0,\beta_0,\alpha_1,\beta_1,\ldots
}
\]

and then prove the resulting infinite coefficient flow is bounded with

\[
\beta_i>0.
\]

If that is done, the GNS/Jacobi square-root operator exists as a genuine
limit of the finite Helmert balance operators. Then the folded xi moment
ledger has a trace-gauge Stieltjes realization, hence the Pass-3
positive-determinant route closes.

The remaining native theorem is therefore not:

\[
\text{prove an opaque global positivity field.}
\]

It is:

\[
\boxed{
\text{derive and control the local Helmert-Jacobi coefficient flow}
}
\]

from the centered primorial/Archimedean construction.

## 24. First rungs as acceptance tests

The coefficient flow can be attacked one rung at a time.

Recall that

\[
\mu_n=\ell_{n+1}.
\]

Define the first Hankel determinants by

\[
D_0:=\mu_0,
\]

\[
D_1:=
\det
\begin{pmatrix}
\mu_0 & \mu_1\\
\mu_1 & \mu_2
\end{pmatrix}
=\mu_0\mu_2-\mu_1^2,
\]

and

\[
D_2:=
\det
\begin{pmatrix}
\mu_0 & \mu_1 & \mu_2\\
\mu_1 & \mu_2 & \mu_3\\
\mu_2 & \mu_3 & \mu_4
\end{pmatrix}.
\]

Then the first Jacobi/Helmert coefficients are

\[
\boxed{
\alpha_0=\frac{\mu_1}{\mu_0}
}
\]

and

\[
\boxed{
\beta_0=\frac{\sqrt{D_1}}{\mu_0}.
}
\]

The next diagonal rung is

\[
\boxed{
\alpha_1
=
\frac{\mu_0^2\mu_3-2\mu_0\mu_1\mu_2+\mu_1^3}
{\mu_0D_1}.
}
\]

The next transfer coupling is

\[
\boxed{
\beta_1
=
\frac{\sqrt{\mu_0D_2}}{D_1}.
}
\]

Thus the first nontrivial balance coupling is not mysterious:

\[
\beta_0^2
=
\frac{\mu_0\mu_2-\mu_1^2}{\mu_0^2}.
\]

It is the normalized centered square, the first variance-like Helmert
volume of the moment ledger.

### 24.1 The determinant-to-ladder translation

For the full Jacobi ladder, the positive off-rung couplings are exactly
square roots of Hankel determinant ratios:

\[
\boxed{
\beta_i
=
\frac{\sqrt{D_{i+1}D_{i-1}}}{D_i},
\qquad
D_i:=\det(\mu_{a+b})_{0\leq a,b\leq i},
\qquad
D_{-1}:=1.
}
\]

So Hankel positivity is not a separate language from the Helmert ladder.
It is the same statement seen after taking square roots:

\[
\boxed{
\text{positive Hankel volumes}
\quad\Longleftrightarrow\quad
\text{real positive Helmert transfer couplings}.
}
\]

This is the native reading of the Hankel lock.

### 24.2 The radius gate

The upper support bound

\[
0\leq t\leq R,
\qquad
R=\gamma_1^{-2},
\]

starts with

\[
R\mu_0-\mu_1\geq0.
\]

The next gate is

\[
\det
\begin{pmatrix}
R\mu_0-\mu_1 & R\mu_1-\mu_2\\
R\mu_1-\mu_2 & R\mu_2-\mu_3
\end{pmatrix}
\geq0.
\]

In ladder language, this says not only that the Helmert transfer
couplings are real and positive, but that the resulting multiplication
operator fits inside the radius window

\[
[0,R].
\]

So the Pass-3 native target has two local tests:

\[
\boxed{
D_i>0
\quad
\text{and}
\quad
G_i^{(R)}:=(R\mu_{a+b}-\mu_{a+b+1})_{0\leq a,b\leq i}\succeq0.
}
\]

The first builds the ladder. The second keeps the ladder inside the
correct spectral radius.

## 25. Dishwasher certificate: first local locks

The probe

\[
\texttt{probe\_pass3\_first\_rung\_certificates.py}
\]

turns the first local locks into an auditable table.

It computes

\[
\mu_n=\ell_{n+1},
\qquad
D_i=\det(\mu_{a+b})_{0\leq a,b\leq i},
\qquad
G_i^{(R)}=(R\mu_{a+b}-\mu_{a+b+1})_{0\leq a,b\leq i}.
\]

For

\[
R=\gamma_1^{-2}
=0.005005244123594116078809401235\ldots,
\]

the first folded moments are

\[
\begin{array}{c|c}
n & \mu_n\\
\hline
0 & 2.3104993115418970789\cdot10^{-2}\\
1 & 3.7172599285269686165\cdot10^{-5}\\
2 & 1.4417393140097327970\cdot10^{-7}\\
3 & 6.6303168025299086987\cdot10^{-10}\\
4 & 3.2136641506166012161\cdot10^{-12}
\end{array}
\]

The first Hankel volumes are

\[
\begin{array}{c|c}
i & D_i\\
\hline
0 & 2.3104993115418970789\cdot10^{-2}\\
1 & 1.9493355548191422147\cdot10^{-9}\\
2 & 2.1728105105262467750\cdot10^{-22}\\
3 & 1.1775817160101727020\cdot10^{-41}
\end{array}
\]

and the first radius gates are

\[
\begin{array}{c|c}
i & \det G_i^{(R)}\\
\hline
0 & 7.8473531731363625970\cdot10^{-5}\\
1 & 2.8438117817974861571\cdot10^{-15}\\
2 & 4.1557904794310360975\cdot10^{-32}\\
3 & 1.7885495554481429373\cdot10^{-55}
\end{array}
\]

All displayed local locks are positive.

The same probe compares determinant formulas with the Jacobi/Helmert
coefficients:

\[
\begin{array}{c|c|c}
i & \alpha_i & \beta_i\\
\hline
0 & 1.6088556745971409753\cdot10^{-3}
& 1.9108977920880258769\cdot10^{-3}\\
1 & 3.5005892352730682116\cdot10^{-3}
& 1.1494160158980175921\cdot10^{-3}\\
2 & 1.7983431372353904753\cdot10^{-3}
& 6.9729568160293123921\cdot10^{-4}\\
3 & 1.2171788332190334042\cdot10^{-3}
& 5.5448464298934773386\cdot10^{-4}
\end{array}
\]

The differences between the determinant formulas and the GNS/Jacobi
matrix entries are at numerical roundoff:

\[
\alpha_0,\beta_0,\alpha_1,\beta_1,\beta_2
\quad\text{all agree to the displayed precision.}
\]

### 25.1 Meaning

The first dishes are clean:

\[
\boxed{
\text{Hankel volumes}
\to
\text{Helmert transfer couplings}
\to
\text{radius-gated GNS operator}
}
\]

is not just a metaphor. It is an executable local certificate.

But this still does not prove RH. It proves that the local target is now
precise enough to be attacked directly:

\[
\boxed{
\text{derive the positivity of these }D_i
\text{ and }G_i^{(R)}
\text{ from the centered primorial/Archimedean tower.}
}
\]

That is the remaining native dish.

## 26. Final normal form: the trace-gauge J-fraction

There is one last compression.

Let

\[
F(x):=S'(x)
=\sum_{n\geq0}(-1)^n\mu_nx^n,
\qquad
\mu_n=\ell_{n+1}.
\]

If the Hankel and radius gates hold, the moment ledger has a Jacobi
operator \(J\) with coefficients

\[
\alpha_i=J_{i,i},
\qquad
\beta_i=J_{i,i+1}>0,
\]

and cyclic vector

\[
\Omega=\sqrt{\mu_0}\,e_0.
\]

Then

\[
\boxed{
F(x)=\left\langle \Omega,(I+xJ)^{-1}\Omega\right\rangle.
}
\]

Equivalently, \(F\) has the Jacobi continued fraction

\[
\boxed{
F(x)=
\frac{\mu_0}{
1+\alpha_0x
-
\dfrac{\beta_0^2x^2}{
1+\alpha_1x
-
\dfrac{\beta_1^2x^2}{
1+\alpha_2x-\cdots}}}.
}
\]

The support gate is simply

\[
0\preceq J\preceq RI.
\]

### 26.1 Theorem: J-fraction equivalence

For the folded xi moment ledger, the following are equivalent:

1. \(F(x)\) is a Stieltjes transform of a positive measure on \([0,R]\).
2. The Hankel matrices and upper-radius localizers are positive for every
   finite size.
3. The Jacobi coefficients are real with

\[
\beta_i>0
\]

and the Jacobi operator satisfies

\[
0\preceq J\preceq RI.
\]

In this case the three languages describe the same object:

\[
\boxed{
\text{Hankel gates}
\Longleftrightarrow
\text{Helmert/Jacobi transfer flow}
\Longleftrightarrow
\text{Stieltjes transform on }[0,R].
}
\]

### Proof

The equivalence between positive Hankel/localizing forms and a positive
measure on \([0,R]\) is the bounded Stieltjes-Hausdorff moment criterion.
Given such a measure, Gram-Schmidt applied to \(1,t,t^2,\ldots\) gives
orthonormal polynomials. Multiplication by \(t\) in this basis is the
Jacobi operator \(J\), with positive off-diagonal coefficients whenever
the moment problem is nondegenerate. Since \(t\in[0,R]\), the operator
satisfies \(0\preceq J\preceq RI\).

Conversely, if such a Jacobi operator and cyclic vector exist, the
spectral theorem gives a positive spectral measure on \([0,R]\), and its
moments are exactly

\[
\mu_n=\langle\Omega,J^n\Omega\rangle.
\]

Finally,

\[
\sum_{n\geq0}(-1)^n\mu_nx^n
=
\int_0^R\frac{d\sigma(t)}{1+xt}
=
\langle\Omega,(I+xJ)^{-1}\Omega\rangle,
\]

and the tridiagonal Schur complement expansion of the resolvent gives
the displayed J-fraction. \(\square\)

### 26.2 Meaning

The dishes reduce to one sentence:

\[
\boxed{
\text{derive the positive bounded J-fraction of }S'(x)
\text{ natively from the centered tower.}
}
\]

Then meromorphicity and logarithmic-derivative residues supply the
trace gauge:

\[
d\sigma(t)=\sum_a m_a t_a\,\delta_{t_a},
\]

and for simple folded zeros,

\[
d\sigma(t)=\sum_a t_a\,\delta_{t_a}.
\]

Thus the final native route is

\[
\boxed{
\text{centered primorial/Archimedean tower}
\Longrightarrow
\text{positive bounded J-fraction}
\Longrightarrow
\text{trace-gauge Stieltjes}
\Longrightarrow
\mathrm{RH}.
}
\]

That is the smallest clean statement now visible.

## 27. Resolvent workbench: the J-fraction sees \(B'/B\)

The probe

\[
\texttt{probe\_pass3\_j\_fraction\_workbench.py}
\]

checks the final normal form against the analytic object directly.

It computes finite Jacobi coefficients from the folded moment ledger,
forms the finite continued fraction

\[
F_N(x)=
\cfrac{\mu_0}{
1+\alpha_0x
-
\cfrac{\beta_0^2x^2}{
1+\alpha_1x
-
\cfrac{\beta_1^2x^2}{
\ddots
-
\cfrac{\beta_{N-2}^2x^2}{1+\alpha_{N-1}x}}}}
\]

and compares it with

\[
F(x)=\frac{d}{dx}\log B(x)=\frac{B'(x)}{B(x)}.
\]

The direct values are

\[
\begin{array}{c|c}
x & F(x)\\
\hline
0 & 2.3104993115418970789\cdot10^{-2}\\
1 & 2.3067964030231287680\cdot10^{-2}\\
10 & 2.2747052108248883601\cdot10^{-2}\\
100 & 2.0381759394534783067\cdot10^{-2}
\end{array}
\]

The relative errors of \(F_N(x)\) are:

\[
\begin{array}{c|c|c|c}
N & x=1 & x=10 & x=100\\
\hline
4 & 7.10\cdot10^{-25} & 6.18\cdot10^{-17} & 1.85\cdot10^{-9}\\
6 & 2.18\cdot10^{-38} & 1.84\cdot10^{-26} & 4.15\cdot10^{-15}\\
8 & 1.33\cdot10^{-52} & 1.10\cdot10^{-36} & 2.03\cdot10^{-21}\\
10 & 3.75\cdot10^{-67} & 3.05\cdot10^{-47} & 4.80\cdot10^{-28}\\
12 & 2.94\cdot10^{-82} & 2.36\cdot10^{-58} & 3.30\cdot10^{-35}
\end{array}
\]

This confirms the numerical identity of the three finite microscopes:

\[
\boxed{
\text{Pade atoms}
\quad=\quad
\text{GNS/Jacobi resolvent}
\quad=\quad
\text{finite J-fraction of }B'/B.
}
\]

### 27.1 Meaning

This is also the cleanest answer to the failed Gram-Bures-Poisson route.
The older route tried to identify two spectral-line densities:

\[
\frac{|\Sigma(y,\xi)|^2}{2\pi}\,d\xi
\stackrel{?}{=}
u_B(\xi,y)\,d\xi.
\]

Paper III correctly records that this direct identity is false in
general. Pass-3 does not try to repair it by force. It folds the target
into the determinant variable \(x=y^2\), then asks for the positive
bounded J-fraction of \(B'/B\).

So the new target is not a pointwise spectral-density match. It is a
coefficient-flow theorem:

\[
\boxed{
\text{centered tower}
\Longrightarrow
\alpha_i,\beta_i
\Longrightarrow
F(x)=\langle\Omega,(I+xJ)^{-1}\Omega\rangle.
}
\]

That is a cleaner mountain.

## 28. Eta scaffold through the local gates

The probe

\[
\texttt{probe\_pass3\_eta\_total\_hankel\_gates.py}
\]

pushes the finite eta scaffold through the same local gates.

It forms

\[
\ell_{m,K}^{\mathrm{total}}
=
\ell_m^{\mathrm{end}}
+\ell_m^\infty
+\ell_{m,K}^{\zeta},
\]

then computes the Hankel volumes \(D_i\) and radius gates
\(G_i^{(R)}\).

The result is revealing: small \(K\) is not automatically positive, but
the centered total ledger enters the positive chamber as \(K\) increases.

\[
\begin{array}{c|c|c|c|c}
K & D_2 & D_3 & \det G_2^{(R)} & \det G_3^{(R)}\\
\hline
20 & 2.4556530\cdot10^{-22}
& -4.5566607\cdot10^{-40}
& -4.5649672\cdot10^{-31}
& -7.0663741\cdot10^{-51}\\
32 & 2.1727077\cdot10^{-22}
& 1.1708852\cdot10^{-41}
& 4.1709873\cdot10^{-32}
& 5.0186259\cdot10^{-55}\\
48 & 2.1728105\cdot10^{-22}
& 1.1775815\cdot10^{-41}
& 4.1557908\cdot10^{-32}
& 1.7886085\cdot10^{-55}\\
\mathrm{true} & 2.1728105\cdot10^{-22}
& 1.1775817\cdot10^{-41}
& 4.1557905\cdot10^{-32}
& 1.7885496\cdot10^{-55}
\end{array}
\]

### 28.1 Local chamber theorem

Fix a finite gate, for example \(D_i\) or \(\det G_i^{(R)}\). If the
finite centered cumulants converge to the exact folded cumulants, and
the exact gate is strictly positive, then that finite gate is eventually
positive along the scaffold.

### Proof

Each gate is a polynomial expression in finitely many moments

\[
\mu_0,\ldots,\mu_M.
\]

Moment convergence gives convergence of that polynomial expression.
If the limiting value is strictly positive, then every sufficiently close
finite row has the same sign. \(\square\)

### 28.2 Meaning

This theorem is small but important. It says finite negativity at low
cutoff is not fatal. The native proof needs:

1. convergence of the centered finite rows;
2. a way to prove the limiting gates are positive;
3. effective control showing when each finite gate has entered the
   positive chamber.

The eta scaffold supplies the control experiment. The primorial version
must replace

\[
\eta_K
\]

by

\[
\text{centered primorial/conductor rows}
\]

and prove the same chamber entry.

That is the finite-native formulation of the remaining problem.

## 29. Raw primorial no-go: centering is not continuation

The probe

\[
\texttt{probe\_pass3\_raw\_primorial\_gate\_failure.py}
\]

tests the most literal prime-row idea:

\[
\log \zeta_{n,K}(s)
=
\sum_{p\le p_n}\sum_{r=1}^K\frac{p^{-rs}}{r},
\]

then centers at \(s=\frac12\):

\[
S_{\zeta,n,K}^{\circ}(x)
=
\frac12
\left[
\log\frac{\zeta_{n,K}(\frac12+y)}{\zeta_{n,K}(\frac12)}
+
\log\frac{\zeta_{n,K}(\frac12-y)}{\zeta_{n,K}(\frac12)}
\right],
\qquad
x=y^2.
\]

This is the naive centered finite Euler row. It fails.

With occupation cutoff \(K=32\), the first rows are:

\[
\begin{array}{c|c|c|c|c}
\#\{p\} & \ell_{1}^{\zeta,n,K} & \ell_1^{\mathrm{total}}
& D_1 & \det G_1^{(R)}\\
\hline
1 & 1.9797874 & 0.1294535 & -1.3244343\cdot10^{-1}
& -7.6864904\cdot10^{-1}\\
2 & 3.9302469 & 2.0799131 & 6.7714396\cdot10^{-1}
& -7.0077477\cdot10^{1}\\
5 & 9.4518528 & 7.6015189 & -5.9582619\cdot10^{1}
& -2.6486492\cdot10^{2}\\
13 & 22.4148763 & 20.5645424 & -1.3994318\cdot10^{3}
& -3.6939044\cdot10^{2}\\
34 & 50.6882625 & 48.8379287 & -1.8883468\cdot10^{4}
& 1.1875589\cdot10^{3}
\end{array}
\]

The target values are tiny by comparison:

\[
\ell_1^\zeta=1.87343884880203013,
\qquad
\ell_1=0.02310499311541897079.
\]

### 29.1 No-go theorem

The naive centered finite Euler row cannot be the Lock A2 scaffold.

### Proof

For the finite Euler row,

\[
\log \zeta_{n,K}\left(\frac12+y\right)
=
\sum_{p\le p_n}\sum_{r=1}^K
\frac{p^{-r/2}}{r}e^{-ry\log p}.
\]

After even centering,

\[
S_{\zeta,n,K}^{\circ}(x)
=
\sum_{p\le p_n}\sum_{r=1}^K
\frac{p^{-r/2}}{r}
\left[
\cosh(ry\log p)-1
\right].
\]

Therefore the first zeta residual cumulant is

\[
\ell_1^{\zeta,n,K}
=
\frac12
\sum_{p\le p_n}\sum_{r=1}^K
r(\log p)^2p^{-r/2}.
\]

Already the \(r=1\) part is

\[
\frac12\sum_{p\le p_n}\frac{(\log p)^2}{\sqrt p},
\]

which diverges as \(p_n\to\infty\). Hence the naive centered Euler row
cannot converge to the finite target

\[
\ell_1^\zeta=1.87343884880203013\ldots.
\]

So centering alone does not perform analytic continuation. \(\square\)

### 29.2 Meaning

This is not a setback. It is a boundary marker.

The native scaffold must not be:

\[
\text{finite Euler product}
\quad\text{then}\quad
\text{center}.
\]

It must be:

\[
\boxed{
\text{regularize or continue the prime carrier}
\quad\text{then}\quad
\text{center}
\quad\text{then}\quad
\text{test the local gates}.
}
\]

In Paper II language, the single-axis occupation algebra correctly
manufactures the von Mangoldt distribution upstairs. But Paper III
already warned that the raw Gram/prime-side object is not the Bures
Poisson field. Pass-3 now says the same thing in the folded determinant
language:

\[
\boxed{
\text{raw prime action is not determinant-scale;}
\quad
\text{only the centered continued total ledger can be.}
}
\]

Thus the primorial replacement for eta must include the continuation
machinery: conductor packets, CRT/Fejer windows, height cutoffs, and the
Archimedean counter-ledger before the Hankel/Jacobi gates are asked to
be positive.

This is the precise native upgrade:

\[
\boxed{
\eta_K
\leadsto
\text{continued centered primorial/conductor scaffold},
\quad
\text{not}
\quad
\text{raw centered Euler product}.
}
\]

## 30. Occupation-layer obstruction: only \(r=1,2\) are critical

The raw primorial no-go can be sharpened.

The probe

\[
\texttt{probe\_pass3\_occupation\_layer\_obstruction.py}
\]

splits the naive centered Euler row by occupation layer \(r\). For
\(m=1\), it prints:

\[
\begin{array}{c|c|c|c|c|c}
\#\{p\} & r=1 & r=2 & r=3 & r=4 & r\ge3\\
\hline
10 & 7.6379 & 4.4773 & 2.2758 & 1.2108 & 5.1375\\
100 & 94.6194 & 17.6230 & 4.0322 & 1.4565 & 7.1835\\
1000 & 610.1729 & 37.8809 & 4.7237 & 1.4807 & 7.9001\\
3000 & 1347.1158 & 49.7457 & 4.8716 & 1.4824 & 8.0497
\end{array}
\]

The first two layers keep growing. The \(r\ge3\) block is already
settling.

### 30.1 Two-layer obstruction theorem

For a fixed cumulant order \(m\ge1\), the raw centered Euler contribution
from occupation layer \(r\) is absolutely summable over primes at the
critical center \(s=\frac12\) if and only if

\[
r\ge3.
\]

Thus the only finite-place occupation layers requiring analytic
continuation are

\[
\boxed{r=1\quad\text{and}\quad r=2.}
\]

### Proof

The \(m\)-th centered coefficient from layer \(r\) is proportional to

\[
\sum_p
r^{2m-1}(\log p)^{2m}p^{-r/2}.
\]

The constant \(r^{2m-1}\) is irrelevant for convergence. The prime sum

\[
\sum_p(\log p)^{2m}p^{-r/2}
\]

converges exactly when \(r/2>1\), i.e. \(r>2\), by the prime number
theorem and integral comparison. Therefore all layers \(r\ge3\) are
absolutely summable, while \(r=1\) and \(r=2\) are the critical divergent
layers. \(\square\)

### 30.2 Meaning

This is the most actionable native statement so far.

The occupation-decorated Fock carrier from Paper II is not wrong. It is
too honest: it shows exactly where the critical-line prime action
diverges before continuation.

The Pass-3 native continuation problem is therefore not spread across the
whole Fock tower. It is concentrated in two layers:

\[
\boxed{
\text{continue/renormalize the }r=1,2\text{ single-axis layers;}
\quad
\text{carry }r\ge3\text{ directly.}
}
\]

This gives the primorial replacement for eta a sharper shape:

\[
\boxed{
\text{finite native scaffold}
=
\text{continued }(r=1,2)\text{ carrier}
\;+\;
\text{ordinary }(r\ge3)\text{ carrier}
\;+\;
\text{endpoint/Archimedean counter-ledger}.
}
\]

Only after that assembly should the Hankel/Jacobi gates be tested.

## 31. Two-layer continuation scaffold

The probe

\[
\texttt{probe\_pass3\_two\_layer\_continuation\_scaffold.py}
\]

builds the first explicit version of the native replacement.

Let \(P(s)\) denote the prime zeta function. For \(\operatorname{Re}s>1\),

\[
P(s)=\sum_p p^{-s}.
\]

Its continued form is given by Mobius inversion:

\[
P(s)=\sum_{n\ge1}\frac{\mu(n)}{n}\log\zeta(ns),
\]

where \(\mu(n)\) is the Mobius function.

The two critical occupation layers combine as

\[
C_{12}(s):=P(s)+\frac12P(2s).
\]

Substituting the continued form gives

\[
C_{12}(s)
=
\sum_{n\ge1}c_n\log\zeta(ns),
\]

with

\[
\boxed{
c_n=\frac{\mu(n)+\mathbf 1_{2\mid n}\mu(n/2)}{n}.
}
\]

The first coefficients are:

\[
\begin{array}{c|cccccccccccc}
n & 1&2&3&4&5&6&7&8&9&10&11&12\\
\hline
c_n
&1&0&-\frac13&-\frac14&-\frac15&0&-\frac17&0&0&0
&-\frac1{11}&\frac1{12}
\end{array}
\]

The key fact is

\[
\boxed{c_2=0.}
\]

So the dangerous \(\log\zeta(2s)\) singularity cancels exactly at
\(s=\frac12\).

### 31.1 Two-layer continuation theorem

In a sufficiently small zero-free neighborhood of \(s=\frac12\),

\[
\log\zeta(s)
=
C_{12}(s)
+
\sum_{r\ge3}\frac{P(rs)}{r},
\]

where \(C_{12}\) is continued by the coefficient formula above and the
tail is absolutely convergent.

### Proof

For \(\operatorname{Re}s>1\), the Euler product gives

\[
\log\zeta(s)=\sum_{r\ge1}\frac{P(rs)}{r}.
\]

Split the first two occupation layers:

\[
\log\zeta(s)
=
\left(P(s)+\frac12P(2s)\right)
+
\sum_{r\ge3}\frac{P(rs)}{r}.
\]

Continue the bracketed expression by Mobius inversion. The coefficient
of \(\log\zeta(2s)\) is

\[
\frac{\mu(2)}2+\frac{\mu(1)}2
=
-\frac12+\frac12
=0,
\]

so the pole of \(\zeta(2s)\) at \(s=\frac12\) is absent from
\(C_{12}\). For \(r\ge3\), the prime zeta factor \(P(rs)\) is evaluated
at real part \(r/2>1\), hence the prime sum is absolutely convergent in a
neighborhood of \(s=\frac12\). Analytic continuation then gives the
identity in the neighborhood. \(\square\)

### 31.2 Diagnostic output

The probe splits the centered zeta residual cumulants into the continued
pair and the exact tail:

\[
\begin{array}{c|r|r|r}
m & \ell_m^\zeta & \ell_m^{12} & \ell_m^{\ge3}\\
\hline
1 & 1.8734388488 & -6.4943523715 & 8.3677912203\\
2 & -7.9854724940 & 225.8370155294 & -233.8224880234\\
3 & 31.9978833624 & -6818.9284471686 & 6850.9263305310\\
4 & -127.9996691659 & 214998.0175173568 & -215126.0171865227\\
5 & 511.9999474204 & -6974122.1027965265 & 6974634.1027439469
\end{array}
\]

The continued pair and the convergent tail are individually large at
higher cumulant order, but their sum is the small centered zeta residual.

The direct finite ordinary tail with \(3000\) primes and \(3\le r\le32\)
has errors:

\[
\begin{array}{c|c}
m & |\ell_{m,\mathrm{direct}}^{\ge3}-\ell_m^{\ge3}|\\
\hline
1 & 2.2344731\cdot10^{-1}\\
2 & 2.3274957\cdot10^{1}\\
3 & 3.0532782\cdot10^{3}\\
4 & 1.6604846\cdot10^{5}\\
5 & 6.5168811\cdot10^{6}
\end{array}
\]

This is not a contradiction to convergence. It says high cumulants are
sensitive to the far prime tail because of the weights

\[
(\log p)^{2m}.
\]

### 31.3 Meaning

The remaining proof burden has now split again:

\[
\boxed{
\text{continue the }r=1,2\text{ layer}
\quad+\quad
\text{control the }r\ge3\text{ tail effectively}.
}
\]

The first part is algebraic-analytic and has a clean cancellation:

\[
c_2=0.
\]

The second part is not analytic continuation, but it is still not cheap.
The direct prime tail is absolutely convergent, yet high cumulant order
requires strong tail estimates or an accelerated representation.

So the native scaffold has the sharper contract:

\[
\boxed{
\text{continued }C_{12}
\;+\;
\text{accelerated or effectively bounded }r\ge3\text{ tail}
\;+\;
\text{endpoint/Archimedean counter-ledger}
\Longrightarrow
\text{positive J-fraction gates}.
}
\]

## 32. Tail-control bounds for the ordinary carrier

The probe

\[
\texttt{probe\_pass3\_tail\_control\_bounds.py}
\]

turns the ordinary \(r\ge3\) tail into explicit inequalities.

For the centered tail

\[
T_{\ge3}(s)=\sum_{r\ge3}\frac{P(rs)}{r},
\]

the \(m\)-th cumulant contribution has absolute size bounded by

\[
\frac{m}{(2m)!}
\sum_{r\ge3}r^{2m-1}
\sum_p(\log p)^{2m}p^{-r/2}.
\]

If we truncate primes at \(p\le X\) and occupation layers at \(r\le R\),
the omitted tail splits into:

\[
\text{prime tail }(p>X,\ r\ge3)
\]

and

\[
\text{occupation tail }(r>R).
\]

### 32.1 Prime-tail bound

Let

\[
q_m(X)=\left(\frac43\right)^{2m-1}X^{-1/2}.
\]

If \(q_m(X)<1\), then

\[
\boxed{
E_{m}^{\mathrm{prime}}(X)
\le
\frac{m}{(2m)!}
\frac{3^{2m-1}}{1-q_m(X)}
\sum_{n>X}(\log n)^{2m}n^{-3/2}.
}
\]

The integer tail is bounded by

\[
\sum_{n>X}(\log n)^{2m}n^{-3/2}
\le
\int_X^\infty(\log t)^{2m}t^{-3/2}\,dt.
\]

Equivalently,

\[
\int_X^\infty(\log t)^k t^{-a}\,dt
=
\frac{\Gamma(k+1,(a-1)\log X)}{(a-1)^{k+1}},
\]

with the upper incomplete gamma function.

### 32.2 Occupation-tail bound

Let \(R\) be the last retained occupation layer and put \(r_0=R+1\).
For

\[
q_{m,R}=
\left(\frac{r_0+1}{r_0}\right)^{2m-1}2^{-1/2}<1,
\]

the omitted occupation tail satisfies

\[
\boxed{
E_m^{\mathrm{occ}}(R)
\le
\frac{m}{(2m)!}
\frac{r_0^{2m-1}}{1-q_{m,R}}
\sum_{n\ge2}(\log n)^{2m}n^{-r_0/2}.
}
\]

Again the final sum is bounded by the same incomplete-gamma integral,
starting at \(2\).

### 32.3 Numerical calibration

With \(R=32\), the probe compares actual finite-tail errors against the
analytic bound. For \(p\le 350377\) (the first \(30000\) primes):

\[
\begin{array}{c|c|c|c|c}
m & \text{actual error} & \text{bound}
& E_m^{\mathrm{prime}} & E_m^{\mathrm{occ}}\\
\hline
1 & 7.5189\cdot10^{-2} & 1.1280
& 1.1280 & 4.8929\cdot10^{-5}\\
2 & 2.6009\cdot10^{1} & 4.1120\cdot10^{2}
& 4.1119\cdot10^{2} & 6.3587\cdot10^{-3}\\
3 & 3.0096\cdot10^{3} & 5.1217\cdot10^{4}
& 5.1216\cdot10^{4} & 2.7385\cdot10^{-1}\\
4 & 1.9355\cdot10^{5} & 3.6529\cdot10^{6}
& 3.6529\cdot10^{6} & 6.5619\\
5 & 8.9636\cdot10^{6} & 1.9371\cdot10^{8}
& 1.9371\cdot10^{8} & 1.2250\cdot10^{2}
\end{array}
\]

The bound is deliberately loose, but it proves the correct control
principle:

\[
\boxed{
\text{ordinary }r\ge3\text{ tail error is controllable by explicit}
\quad
\text{prime cutoff and occupation cutoff inequalities.}
}
\]

The table also shows the practical bottleneck:

\[
\boxed{
\text{the prime tail at }r=3\text{ dominates.}
}
\]

The occupation tail \(r>32\) is already tiny compared with the missing
far primes.

### 32.4 Meaning

The tail problem is no longer conceptual. It is quantitative.

For every fixed gate, only finitely many cumulants are needed. For those
cumulants, one may choose \(X\) and \(R\) so that

\[
E_m^{\mathrm{prime}}(X)+E_m^{\mathrm{occ}}(R)
\]

is smaller than any prescribed tolerance.

This gives the finite-native scaffold a real acceptance rule:

\[
\boxed{
\text{continue }C_{12};
\quad
\text{truncate }r\ge3\text{ with explicit tail certificate;}
\quad
\text{then test Hankel/Jacobi gates.}
}
\]

There is still a hard problem: the gates themselves can be extremely
small, so the required \(X\) may be enormous for high cumulant order. But
the source of the difficulty is now named:

\[
\boxed{
\text{small determinant gates require very sharp }r=3\text{ tail control.}
}
\]

## 33. Third-layer dominance

The interlude below explains why \(3\) keeps reappearing across the program.
Here is the operational version for Pass-3:

\[
\boxed{
\text{after continuing }r=1,2,\text{ the first ordinary layer }r=3
\text{ dominates the omitted prime tail.}
}
\]

The probe

\[
\texttt{probe\_pass3\_r3\_tail\_dominance.py}
\]

splits the omitted ordinary prime tail after \(p>X\) into the single layer
\(r=3\) and the faster remainder \(r\ge4\).

For one occupation layer \(r\), the omitted prime tail of the \(m\)-th folded
cumulant is bounded by

\[
E_{m,r}^{\mathrm{prime}}(X)
\le
\frac{m}{(2m)!}
r^{2m-1}
\int_X^\infty(\log t)^{2m}t^{-r/2}\,dt.
\]

Thus the \(r=3\) layer satisfies

\[
\boxed{
E_{m,3}^{\mathrm{prime}}(X)
\le
\frac{m}{(2m)!}
3^{2m-1}
\int_X^\infty(\log t)^{2m}t^{-3/2}\,dt.
}
\]

For the whole \(r\ge4\) block, put

\[
q_{m,4}(X)=
\left(\frac54\right)^{2m-1}X^{-1/2}.
\]

If \(q_{m,4}(X)<1\), then

\[
\boxed{
E_{m,\ge4}^{\mathrm{prime}}(X)
\le
\frac{m}{(2m)!}
\frac{4^{2m-1}}{1-q_{m,4}(X)}
\int_X^\infty(\log t)^{2m}t^{-2}\,dt.
}
\]

Since

\[
\int_X^\infty(\log t)^k t^{-3/2}\,dt
\sim
2X^{-1/2}(\log X)^k
\]

while

\[
\int_X^\infty(\log t)^k t^{-2}\,dt
\sim
X^{-1}(\log X)^k,
\]

the ratio obeys

\[
\boxed{
\frac{E_{m,\ge4}^{\mathrm{prime}}(X)}
     {E_{m,3}^{\mathrm{prime}}(X)}
=O_m(X^{-1/2}).
}
\]

So the \(r\ge4\) block is not the enemy. It is a certified faster remainder.
The enemy is the first honest layer \(r=3\).

### 33.1 Numerical calibration

The probe prints:

\[
\begin{array}{c|c|c|c}
X & m & E_{m,3}^{\mathrm{prime}}\text{ bound}
& E_{m,\ge4}^{\mathrm{prime}}/E_{m,3}^{\mathrm{prime}}\\
\hline
10^4 & 1 & 3.8902 & 5.48\cdot 10^{-3}\\
10^4 & 3 & 7.6268\cdot10^4 & 7.82\cdot10^{-3}\\
10^6 & 1 & 7.6239\cdot10^{-1} & 5.79\cdot10^{-4}\\
10^6 & 3 & 4.3254\cdot10^4 & 1.13\cdot10^{-3}\\
10^8 & 1 & 1.2630\cdot10^{-1} & 5.99\cdot10^{-5}\\
10^8 & 3 & 1.7569\cdot10^4 & 1.36\cdot10^{-4}\\
10^{12} & 1 & 2.6460\cdot10^{-3} & 6.20\cdot10^{-7}\\
10^{12} & 3 & 1.4855\cdot10^3 & 1.61\cdot10^{-6}
\end{array}
\]

The absolute \(r=3\) bounds remain large for higher cumulants because powers
of \(\log p\) amplify the far-prime tail. But the separation between \(r=3\)
and \(r\ge4\) is already decisive.

### 33.2 Meaning

The ordinary tail has now been reduced twice:

\[
\boxed{
r\ge3
\quad\leadsto\quad
r=3\;+\;\text{faster certified remainder}.
}
\]

Therefore the next Pass-3 target is not a generic prime-tail estimate. It is
a specialized third-layer accelerator or certificate:

\[
\boxed{
\text{build a sharp, sign-aware, gate-aware certificate for }
\sum_{p>X}(\log p)^{2m}p^{-3/2}.
}
\]

Everything beyond \(r=3\) can be handled as remainder bookkeeping once that
certificate exists.

## 34. Theta certificate for the third layer

The previous \(r=3\) bound still dominated primes by all integers:

\[
\sum_{p>X}(\log p)^{2m}p^{-3/2}
\le
\sum_{n>X}(\log n)^{2m}n^{-3/2}.
\]

That is safe but wasteful. It throws away the prime-density logarithm.

Introduce the Chebyshev theta function

\[
\vartheta(x)=\sum_{p\le x}\log p.
\]

Then the dominant third-layer tail can be written as a Stieltjes integral:

\[
\sum_{p>X}(\log p)^{2m}p^{-3/2}
=
\int_X^\infty
(\log t)^{2m-1}t^{-3/2}\,d\vartheta(t).
\]

Let

\[
h_m(t)=(\log t)^{2m-1}t^{-3/2}.
\]

Suppose that on \(t\ge X\) we have an explicit theta envelope

\[
\vartheta(t)-\vartheta(X)\le A_\vartheta t.
\]

For \(X\) large enough that \(h_m\) is decreasing, Stieltjes integration by
parts gives

\[
\int_X^\infty h_m(t)\,d\vartheta(t)
\le
A_\vartheta
\int_X^\infty t\bigl(-h_m'(t)\bigr)\,dt.
\]

Since

\[
t\bigl(-h_m'(t)\bigr)
=
\left(
\frac32(\log t)^{2m-1}
-
(2m-1)(\log t)^{2m-2}
\right)t^{-3/2},
\]

the \(r=3\) prime-tail error obeys

\[
\boxed{
E_{m,3}^{\vartheta}(X)
\le
\frac{m\,3^{2m-1}}{(2m)!}\,
A_\vartheta
\int_X^\infty
\left(
\frac32(\log t)^{2m-1}
-
(2m-1)(\log t)^{2m-2}
\right)t^{-3/2}\,dt.
}
\]

This is the missing density correction. The old bound used a
\((\log t)^{2m}\) integral; the theta certificate uses
\((\log t)^{2m-1}\).

The probe

\[
\texttt{probe\_pass3\_r3\_theta\_tail\_certificate.py}
\]

uses \(A_\vartheta=1.01\) as a working large-\(X\) envelope and prints:

\[
\begin{array}{c|c|c|c|c}
X & m & r=3\text{ integer bound}
& r=3\text{ theta bound}
& \text{gain}\\
\hline
10^4 & 1 & 3.8902 & 4.7921\cdot10^{-1} & 8.12\\
10^4 & 3 & 7.6268\cdot10^4 & 6.0566\cdot10^3 & 12.59\\
10^6 & 1 & 7.6239\cdot10^{-1} & 6.8851\cdot10^{-2} & 11.07\\
10^6 & 3 & 4.3254\cdot10^4 & 2.9701\cdot10^3 & 14.56\\
10^8 & 1 & 1.2630\cdot10^{-1} & 8.9782\cdot10^{-3} & 14.07\\
10^8 & 3 & 1.7569\cdot10^4 & 1.0298\cdot10^3 & 17.06\\
10^{12} & 1 & 2.6460\cdot10^{-3} & 1.3164\cdot10^{-4} & 20.10\\
10^{12} & 3 & 1.4855\cdot10^3 & 6.5650\cdot10^1 & 22.63
\end{array}
\]

### 34.1 Meaning

The Pass-3 tail-control stack is now:

\[
\boxed{
\begin{array}{rcl}
r=1,2 &:& \text{continued pair carrier},\\[2mm]
r=3 &:& \text{theta-certified dominant ordinary layer},\\[2mm]
r\ge4 &:& \text{faster certified remainder}.
\end{array}
}
\]

This is a better division of labor than the raw Euler product supplied. The
first two layers need analytic continuation, the third needs prime-density
control, and all later layers need only remainder bookkeeping.

The next target is gate-awareness: translate the scalar error certificates
for \(r=3\) and \(r\ge4\) into determinant stability intervals for the
Hankel/Jacobi gates.

## 35. Gate-aware stability intervals

Scalar tail control is only useful if it preserves the determinant gates.
The gate-aware layer takes moment error radii

\[
\varepsilon_m
=
E_{m,3}^{\vartheta}(X)
+
E_{m,\ge4}^{\mathrm{prime}}(X)
+
E_m^{\mathrm{occ}}(R),
\]

and propagates them into Hankel and upper-radius Jacobi determinants.

For a gate matrix \(A(\mu)\), let \(E\) be the entrywise error-radius matrix
induced by the moment radii. For example,

\[
A^{(D_i)}_{ab}=\mu_{a+b+1},
\qquad
E^{(D_i)}_{ab}=\varepsilon_{a+b+1},
\]

while for the upper-radius gate at radius \(\rho=\gamma_1^{-2}\),

\[
A^{(G_i)}_{ab}=\rho\mu_{a+b+1}-\mu_{a+b+2},
\qquad
E^{(G_i)}_{ab}=\rho\varepsilon_{a+b+1}+\varepsilon_{a+b+2}.
\]

The probe

\[
\texttt{probe\_pass3\_gate\_stability\_intervals.py}
\]

uses the conservative Leibniz perturbation radius

\[
\boxed{
\left|\det(A+\Delta)-\det A\right|
\le
\sum_{\sigma}
\left[
\prod_i\bigl(|A_{i,\sigma(i)}|+E_{i,\sigma(i)}\bigr)
-
\prod_i|A_{i,\sigma(i)}|
\right],
}
\]

valid whenever \(|\Delta_{ab}|\le E_{ab}\). Therefore each gate receives a
certified interval

\[
\det A
\in
\left[
\det A_{\mathrm{nom}}-\mathcal R_A,
\det A_{\mathrm{nom}}+\mathcal R_A
\right].
\]

If this interval avoids zero, the gate sign is stable under the ordinary-tail
certificate. If it crosses zero, the gate is unresolved at that cutoff and
certificate strength.

### 35.1 Current calibration

With \(30000\) primes, \(X=350377\), \(R=64\), \(A_\vartheta=1.01\), and
\(\rho=\gamma_1^{-2}\), the ordinary-tail moment radii remain comparable to
the nominal moment sizes:

\[
\begin{array}{c|c|c|c}
m & \mu_m\text{ nominal} & \varepsilon_m & \varepsilon_m/|\mu_m|\\
\hline
1 & -5.1770\cdot10^{-2} & 1.0935\cdot10^{-1} & 2.11\\
2 & 2.5976\cdot10^{1} & 3.4764\cdot10^{1} & 1.34\\
3 & -3.0086\cdot10^{3} & 3.7108\cdot10^{3} & 1.23\\
4 & 1.9354\cdot10^{5} & 2.2280\cdot10^{5} & 1.15\\
5 & -8.9634\cdot10^{6} & 9.8083\cdot10^{6} & 1.09\\
6 & 3.5262\cdot10^{8} & 3.7348\cdot10^{8} & 1.06\\
7 & -1.3001\cdot10^{10} & 1.3502\cdot10^{10} & 1.04\\
8 & 4.7015\cdot10^{11} & 4.8248\cdot10^{11} & 1.03
\end{array}
\]

The determinant intervals are consequently still too wide:

\[
\begin{array}{c|c|c|c}
\text{gate} & \det A_{\mathrm{nom}} & \mathcal R_A & \text{verdict}\\
\hline
D_0 & -5.1770\cdot10^{-2} & 1.0935\cdot10^{-1} & \text{unresolved}\\
D_1 & -5.1902\cdot10^{2} & 3.9415\cdot10^{3} & \text{unresolved}\\
D_2 & 3.5733\cdot10^{9} & 6.9387\cdot10^{11} & \text{unresolved}\\
D_3 & 7.1291\cdot10^{18} & 1.9920\cdot10^{23} & \text{unresolved}\\
G_0 & -2.5977\cdot10^{1} & 3.4765\cdot10^{1} & \text{unresolved}\\
G_1 & -4.0246\cdot10^{6} & 5.6365\cdot10^{7} & \text{unresolved}\\
G_2 & 3.1703\cdot10^{14} & 2.2506\cdot10^{17} & \text{unresolved}\\
G_3 & 2.6459\cdot10^{24} & 1.3569\cdot10^{30} & \text{unresolved}
\end{array}
\]

This is the right failure mode. The scalar certificates are valid, but they
are not yet gate-sharp. They preserve no determinant sign at this cutoff.

### 35.2 Meaning

The Pass-3 obstruction has moved again:

\[
\boxed{
\text{ordinary-tail convergence}
\quad\leadsto\quad
\text{scalar tail certificates}
\quad\leadsto\quad
\text{gate-stability certificates}.
}
\]

The next tightening cannot merely say "the tail is bounded." It must be one
of the following:

1. a sharper evaluation of the dominant \(r=3\) contribution,
2. a determinant-aware certificate that uses cancellations in the gate
   polynomial instead of independent entrywise intervals,
3. or an adaptive cutoff rule that grows \(X\) until each gate interval avoids
   zero.

Thus the current gate-aware verdict is:

\[
\boxed{
\text{the scalar theta certificate is structurally right but not yet}
\quad
\text{determinant-sharp.}
}
\]

### 35.3 Sign-aware ordinary-tail cone

The symmetric interval probe is deliberately pessimistic. The omitted
ordinary tail is not free to perturb each moment in either direction. Each
missing occupation atom has the sign pattern

\[
\delta\mu_m=(-1)^{m+1}\,(\text{positive quantity}).
\]

Thus the admissible completion region is one-sided:

\[
\begin{cases}
\mu_m\le \mu_m^{\mathrm{comp}}\le \mu_m+\varepsilon_m,
&m\text{ odd},\\[1mm]
\mu_m-\varepsilon_m\le \mu_m^{\mathrm{comp}}\le \mu_m,
&m\text{ even}.
\end{cases}
\]

The probe

\[
\texttt{probe\_pass3\_sign\_aware\_gate\_scan.py}
\]

scans the corners of this one-sided box. With the same \(X=350377\),
\(R=64\) calibration, the exact eta moments lie inside all one-sided moment
ranges, but every tested gate still crosses zero:

\[
\begin{array}{c|c|c|c}
\text{gate} & \text{corner low} & \text{corner high} & \text{verdict}\\
\hline
D_0 & -5.1770\cdot10^{-2} & 5.7585\cdot10^{-2} & \text{crosses}\\
D_1 & -8.4802\cdot10^{2} & 7.8530\cdot10^{1} & \text{crosses}\\
D_2 & -5.8914\cdot10^{9} & 3.9472\cdot10^{10} & \text{crosses}\\
D_3 & -1.8143\cdot10^{21} & 3.1999\cdot10^{21} & \text{crosses}\\
G_0 & -2.5977\cdot10^{1} & 8.7881 & \text{crosses}\\
G_1 & -1.0752\cdot10^{7} & 4.5345\cdot10^{6} & \text{crosses}\\
G_2 & -4.1192\cdot10^{15} & 1.2019\cdot10^{16} & \text{crosses}\\
G_3 & -1.3348\cdot10^{28} & 1.8086\cdot10^{28} & \text{crosses}
\end{array}
\]

Sign information helps, but it is not enough.

### 35.4 Completion homotopy

To see whether the remaining obstruction is structural or merely precision,
the probe

\[
\texttt{probe\_pass3\_completion\_homotopy.py}
\]

uses the exact eta ledger as an oracle endpoint and studies

\[
\mu(\lambda)
=
\mu_{\mathrm{finite}}
+
\lambda(\mu_{\mathrm{true}}-\mu_{\mathrm{finite}}),
\qquad
0\le\lambda\le1.
\]

This is not a proof certificate. It is a chamber-geometry diagnostic.

The missing exact completion uses a large fraction of the scalar certificate
radius:

\[
\begin{array}{c|c}
m & |\mu_m^{\mathrm{true}}-\mu_m^{\mathrm{finite}}|/\varepsilon_m\\
\hline
1&0.6847\\
2&0.7472\\
3&0.8108\\
4&0.8686\\
5&0.9139\\
6&0.9442\\
7&0.9629\\
8&0.9745
\end{array}
\]

The gate crossings along the straight completion path are:

\[
\begin{array}{c|c|c}
\text{gate} & \lambda_+ & \text{comment}\\
\hline
D_0 & 0.6914 & \text{enters early enough}\\
D_1 & 0.999999999972 & \text{endpoint precision bottleneck}\\
D_2 & \text{already positive at }\lambda=0,\text{ but dips negative near }0.958
& \text{curved chamber}\\
D_3 & \text{positive at endpoint} & \text{tiny final gate}\\
G_0 & 0.999996979079 & \text{endpoint precision bottleneck}\\
G_1 & 1.0 & \text{endpoint precision bottleneck}\\
G_2 & \text{positive at endpoint} & \text{tiny final gate}\\
G_3 & \text{positive at endpoint} & \text{tiny final gate}
\end{array}
\]

This is the decisive diagnostic:

\[
\boxed{
\text{the exact completion direction reaches the positive chamber,}
\quad
\text{but the chamber is extremely thin near the endpoint.}
}
\]

The next certificate cannot be a wide upper-bound envelope. It must either
evaluate the dominant \(r=3\) layer essentially exactly, or prove positivity
directly in the completed trace-gauge/Jacobi representation.

### 35.5 Completion profile

The word *completion* should now be used technically.

The finite native scaffold is

\[
\mu^{\mathrm{fin}}
=
\mu^{\mathrm{end}}
+
\mu^{\mathrm{arc}}
+
\mu^{C_{12},K}
+
\mu^{\mathrm{ord}}_{p\le X,\ 3\le r\le R}.
\]

The completed eta/zeta ledger is

\[
\mu^{\mathrm{true}}
=
\mu^{\mathrm{end}}
+
\mu^{\mathrm{arc}}
+
\mu^{\zeta,\mathrm{fold}}.
\]

The completion vector is

\[
\Delta\mu
=
\mu^{\mathrm{true}}-\mu^{\mathrm{fin}}.
\]

The probe

\[
\texttt{probe\_pass3\_completion\_profile.py}
\]

prints, for \(X=350377\), \(R=64\), \(K=60\):

\[
\begin{array}{c|c|c|c}
m & \mu_m^{\mathrm{fin}} & \mu_m^{\mathrm{true}} & \Delta\mu_m\\
\hline
1 & -5.1770\cdot10^{-2} & 2.3105\cdot10^{-2} & 7.4875\cdot10^{-2}\\
2 & 2.5976\cdot10^{1} & 3.7173\cdot10^{-5} & -2.5976\cdot10^{1}\\
3 & -3.0086\cdot10^{3} & 1.4417\cdot10^{-7} & 3.0086\cdot10^{3}\\
4 & 1.9354\cdot10^{5} & 6.6303\cdot10^{-10} & -1.9354\cdot10^{5}\\
5 & -8.9634\cdot10^{6} & 3.2137\cdot10^{-12} & 8.9634\cdot10^{6}\\
6 & 3.5262\cdot10^{8} & 1.5877\cdot10^{-14} & -3.5262\cdot10^{8}\\
7 & -1.3001\cdot10^{10} & 7.9033\cdot10^{-17} & 1.3001\cdot10^{10}\\
8 & 4.7015\cdot10^{11} & 3.9465\cdot10^{-19} & -4.7015\cdot10^{11}
\end{array}
\]

The sign pattern is exactly the ordinary-tail pattern:

\[
\boxed{
\operatorname{sgn}\Delta\mu_m=(-1)^{m+1}.
}
\]

The same probe decomposes the ordinary-tail completion. To displayed
precision, the missing ordinary tail is the missing \(r=3\) layer:

\[
\begin{array}{c|c|c|c}
m & \text{missing ordinary tail}
& \text{estimated missing }r=3
& r\ge4\text{ error bound}\\
\hline
1 & 7.4875\cdot10^{-2} & 7.4875\cdot10^{-2} & 1.09\cdot10^{-3}\\
2 & -2.5976\cdot10^{1} & -2.5976\cdot10^{1} & 5.68\cdot10^{-1}\\
3 & 3.0086\cdot10^{3} & 3.0086\cdot10^{3} & 9.16\cdot10^{1}\\
4 & -1.9354\cdot10^{5} & -1.9354\cdot10^{5} & 7.33\cdot10^{3}\\
5 & 8.9634\cdot10^{6} & 8.9634\cdot10^{6} & 3.61\cdot10^{5}\\
6 & -3.5262\cdot10^{8} & -3.5262\cdot10^{8} & 1.26\cdot10^{7}\\
7 & 1.3001\cdot10^{10} & 1.3001\cdot10^{10} & 3.39\cdot10^{8}\\
8 & -4.7015\cdot10^{11} & -4.7015\cdot10^{11} & 7.69\cdot10^{9}
\end{array}
\]

Thus the completion stack is now:

\[
\boxed{
\Delta\mu
\approx
\Delta\mu^{(r=3)}
\quad
\text{with }r\ge4\text{ a certified faster correction.}
}
\]

The determinant effect is extreme. The finite gates are huge relative to the
exact positive gates:

\[
\begin{array}{c|c|c|c}
\text{gate} & \text{finite value} & \text{exact value}
& |\text{finite}/\text{exact}|\\
\hline
D_1 & -5.1902\cdot10^2 & 1.9493\cdot10^{-9} & 2.66\cdot10^{11}\\
D_2 & 3.5733\cdot10^9 & 2.1728\cdot10^{-22} & 1.64\cdot10^{31}\\
D_3 & 7.1291\cdot10^{18} & 1.1776\cdot10^{-41} & 6.05\cdot10^{59}\\
G_1 & -4.0246\cdot10^6 & 2.8438\cdot10^{-15} & 1.42\cdot10^{21}\\
G_2 & 3.1703\cdot10^{14} & 4.1558\cdot10^{-32} & 7.63\cdot10^{45}\\
G_3 & 2.6459\cdot10^{24} & 1.7885\cdot10^{-55} & 1.48\cdot10^{79}
\end{array}
\]

So completion is not a small correction in determinant space. It is a large
alternating cancellation that leaves a tiny positive determinant residue.

This gives the next precise target:

\[
\boxed{
\text{prove the completed }r=3\text{ cancellation as a structured}
\quad
\text{trace-gauge/Jacobi positive residue.}
}
\]

Equivalently:

\[
\boxed{
\text{do not certify completion by wide scalar intervals;}
\quad
\text{certify the completed operator.}
}
\]

### 35.6 Completed operator diagnostic

The probe

\[
\texttt{probe\_pass3\_completed\_operator\_certificate.py}
\]

turns the previous sentence into an operator check.

At the same \(X=350377\), \(R=64\), \(K=60\), the finite scaffold is not yet a
positive moment ledger. Its first moment is negative:

\[
\mu_1^{\mathrm{fin}}=-0.0517699598917,
\]

so the GNS/Jacobi construction fails immediately with a nonpositive norm at
degree \(0\).

The completed eta/zeta ledger, by contrast, gives a positive finite Jacobi
operator. For \(n=4\), the extracted coefficients are:

\[
\begin{array}{c|c|c}
i & \alpha_i & \beta_i\\
\hline
0 & 0.00160885567460 & 0.00191089779209\\
1 & 0.00350058923527 & 0.00114941601590\\
2 & 0.00179834313724 & 0.000697295681603\\
3 & 0.00121717883322 & 0
\end{array}
\]

Its spectral support is inside the first-zero radius:

\[
\lambda_{\min}=0.0000823622885625,
\qquad
\lambda_{\max}=0.00500498160159
<
\gamma_1^{-2}=0.00500524412359.
\]

So the completed operator view says:

\[
\boxed{
\text{finite raw scaffold: not yet a moment space;}
\qquad
\text{completed ledger: positive bounded Jacobi operator.}
}
\]

This is the strongest formulation of completion so far. The target is not
"make the finite determinant intervals small." The target is:

\[
\boxed{
\text{construct the completed Jacobi operator natively from the}
\quad
\text{two-layer continuation plus }r=3\text{ completion.}
}
\]

### 35.7 PNT \(r=3\) completion is close but not enough

The first native approximation to \(r=3\) completion replaces the Chebyshev
measure by its prime-number-theorem density:

\[
d\vartheta(t)\approx dt.
\]

Thus the missing third layer after \(X\) is approximated by

\[
\sum_{p>X}(\log p)^{2m}p^{-3/2}
\approx
\int_X^\infty(\log t)^{2m-1}t^{-3/2}\,dt.
\]

The probe

\[
\texttt{probe\_pass3\_pnt\_r3\_completion\_operator.py}
\]

builds the resulting PNT-completed ledger. At \(X=350377\), the PNT
completion is already very close to the exact missing completion at the
moment level:

\[
\begin{array}{c|c|c|c}
m & \mu_m^{\mathrm{PNT}} & \mu_m^{\mathrm{true}}
& \mu_m^{\mathrm{PNT}}-\mu_m^{\mathrm{true}}\\
\hline
1 & 2.3071\cdot10^{-2} & 2.3105\cdot10^{-2} & -3.41\cdot10^{-5}\\
2 & 2.8177\cdot10^{-2} & 3.7173\cdot10^{-5} & 2.81\cdot10^{-2}\\
3 & -5.3649 & 1.4417\cdot10^{-7} & -5.3649\\
4 & 4.5749\cdot10^{2} & 6.6303\cdot10^{-10} & 4.5749\cdot10^{2}\\
5 & -2.2836\cdot10^{4} & 3.2137\cdot10^{-12} & -2.2836\cdot10^{4}\\
6 & 7.7705\cdot10^{5} & 1.5877\cdot10^{-14} & 7.7705\cdot10^{5}\\
7 & -2.0005\cdot10^{7} & 7.9033\cdot10^{-17} & -2.0005\cdot10^{7}\\
8 & 4.2247\cdot10^{8} & 3.9465\cdot10^{-19} & 4.2247\cdot10^{8}
\end{array}
\]

But determinant space magnifies this tiny relative residue. The
PNT-completed gates are still outside the positive chamber:

\[
\begin{array}{c|c|c}
\text{gate} & \text{PNT-completed value} & \text{true completed value}\\
\hline
D_0 & 2.3071\cdot10^{-2} & 2.3105\cdot10^{-2}\\
D_1 & -1.2457\cdot10^{-1} & 1.9493\cdot10^{-9}\\
D_2 & -1.9680\cdot10^{3} & 2.1728\cdot10^{-22}\\
D_3 & 1.6014\cdot10^{10} & 1.1776\cdot10^{-41}\\
G_0 & -2.8061\cdot10^{-2} & 7.8474\cdot10^{-5}\\
G_1 & -1.5945\cdot10^{1} & 2.8438\cdot10^{-15}\\
G_2 & 1.0680\cdot10^{7} & 4.1558\cdot10^{-32}\\
G_3 & 1.7311\cdot10^{15} & 1.7885\cdot10^{-55}
\end{array}
\]

The PNT-completed ledger cannot yet build a positive GNS/Jacobi space:

\[
\text{GNS failure at degree }1.
\]

Therefore the conclusion is sharp:

\[
\boxed{
d\vartheta(t)=dt+d\Theta(t)
\quad
\text{and the fluctuation }d\Theta(t)\text{ is gate-relevant.}
}
\]

The main completion is the smooth density \(dt\), but the determinant
positivity lives in the residual arithmetic correction. The next target is
therefore not merely PNT completion. It is:

\[
\boxed{
\text{certify the }r=3\text{ theta-residue operator}
\quad
d\Theta(t)=d\vartheta(t)-dt.
}
\]

### 35.8 The theta residue is nonlocal

The next probe asks whether \(d\Theta\) is a local cutoff correction or a
global spectral correction.

The integration-by-parts form is

\[
\int_X^\infty h_m(t)\,d\Theta(t)
=
-h_m(X)\Theta(X)
-
\int_X^\infty \Theta(t)h_m'(t)\,dt,
\]

where

\[
h_m(t)=(\log t)^{2m-1}t^{-3/2},
\qquad
\Theta(t)=\vartheta(t)-t.
\]

At \(X=350377\),

\[
\Theta(X)=-529.3785145387.
\]

The endpoint term \(-h_m(X)\Theta(X)\) explains only the first moment
substantially. By \(m=8\), it is about \(0.13\%\) of the oracle residue.
Thus the gate-relevant residue is not merely the boundary fluctuation at
the cutoff.

The probe

\[
\texttt{probe\_pass3\_theta\_residue\_windows.py}
\]

computes partial residues over windows \([X,Y]\). The ratios below are
partial window residue divided by total oracle residue:

\[
\begin{array}{c|ccccc}
m & 2X & 5X & 10X & 20X & 50X\\
\hline
1 & -1.021 & -1.139 & -1.222 & -1.232 & -1.270\\
2 & -0.315 & -0.362 & -0.395 & -0.399 & -0.417\\
3 & -0.127 & -0.150 & -0.168 & -0.170 & -0.180\\
4 & -0.054 & -0.067 & -0.077 & -0.078 & -0.084\\
5 & -0.023 & -0.030 & -0.035 & -0.036 & -0.040\\
6 & -0.0096 & -0.0128 & -0.0158 & -0.0161 & -0.0184\\
7 & -0.0037 & -0.0052 & -0.0067 & -0.0068 & -0.0081\\
8 & -0.0013 & -0.0019 & -0.0026 & -0.0026 & -0.0033
\end{array}
\]

The early residue points the wrong way relative to the total oracle
residue. This is decisive: the theta residue is not a local correction near
the cutoff. It is an oscillatory global completion.

The operator-path probe

\[
\texttt{probe\_pass3\_theta\_residue\_operator\_windows.py}
\]

starts from the PNT-completed ledger and adds the exact
\(d\vartheta-dt\) fluctuation only on \([X,Y]\). The first gates move away
from positivity:

\[
\begin{array}{c|cccc|c}
Y/X & D_0 & D_1 & G_0 & G_1 & \text{GNS}\\
\hline
\mathrm{PNT} & 0.0230709 & -0.124566 & -0.0280612 & -15.9447
& \text{fail degree }1\\
2 & 0.0230366 & -0.140389 & -0.0368122 & -18.6797
& \text{fail degree }1\\
5 & 0.0230322 & -0.143476 & -0.0381962 & -19.3842
& \text{fail degree }1\\
10 & 0.0230293 & -0.145760 & -0.0391603 & -19.9347
& \text{fail degree }1\\
20 & 0.0230289 & -0.146052 & -0.0392869 & -20.0049
& \text{fail degree }1\\
50 & 0.0230276 & -0.147369 & -0.0397855 & -20.3448
& \text{fail degree }1\\
\mathrm{true} & 0.0231050 & 1.9493\cdot10^{-9}
& 7.8474\cdot10^{-5} & 2.8438\cdot10^{-15}
& \text{positive bounded}
\end{array}
\]

Therefore:

\[
\boxed{
\text{the early theta residue worsens the gates;}
\quad
\text{the restoring correction lives farther out.}
}
\]

This is the point where the number-theoretic content becomes unavoidable.
The residue cannot be certified by a local cutoff estimate. It must be
certified by a global formula for \(\Theta(t)\), i.e. by the explicit-formula
oscillation of primes against zeros.

The next proof target is consequently:

\[
\boxed{
\text{replace local theta bounds by an explicit-formula}
\quad
\text{theta-residue/Jacobi certificate.}
}
\]

### 35.9 Explicit-formula \(r=3\) completion

The zero-side formula is cleanest at the \(\log\zeta\) layer. For
\(k\ge2\), the Hadamard product for \(\xi\) gives

\[
\frac{d^k}{ds^k}\log\xi(s)
=
-(k-1)!\sum_{\rho}\frac{1}{(\rho-s)^k}.
\]

Since

\[
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

we obtain

\[
\frac{d^k}{ds^k}\log\zeta(s)
=
-(k-1)!\sum_{\rho}\frac{1}{(\rho-s)^k}
+(-1)^k(k-1)!
\left(
\frac1{s^k}+\frac1{(s-1)^k}
\right)
-
2^{-k}\psi^{(k-1)}(s/2),
\]

where \(\psi^{(k-1)}\) is the polygamma function. Then prime-zeta
derivatives are recovered by Möbius inversion:

\[
P^{(k)}(s)
=
\sum_{n\ge1}\mu(n)n^{k-1}
\frac{d^k}{dz^k}\log\zeta(z)\Big|_{z=ns}.
\]

Therefore the dominant third layer has the explicit-formula form

\[
\boxed{
\ell_m^{(r=3)}
=
(-1)^{m+1}
\frac{m\,3^{2m-1}}{(2m)!}
P^{(2m)}(3/2).
}
\]

This is the zero-spectrum replacement for local theta-window estimates.

The probe

\[
\texttt{probe\_pass3\_explicit\_formula\_r3\_completion.py}
\]

uses the first \(100\) zeta zeros and Möbius cutoff \(24\). It compares the
zero-packet \(r=3\) completion with the oracle \(r=3\) completion:

\[
\begin{array}{c|c|c|c}
m & \text{oracle missing }r=3
& \text{zero-packet missing }r=3
& \text{ratio}\\
\hline
1 & 7.4875\cdot10^{-2} & 1.7724\cdot10^{-1} & 2.367\\
2 & -2.5976\cdot10^{1} & -2.5936\cdot10^{1} & 0.9984\\
3 & 3.0086\cdot10^{3} & 3.0022\cdot10^{3} & 0.9979\\
4 & -1.9354\cdot10^{5} & -1.9304\cdot10^{5} & 0.9974\\
5 & 8.9634\cdot10^{6} & 8.9395\cdot10^{6} & 0.9973\\
6 & -3.5262\cdot10^{8} & -3.5182\cdot10^{8} & 0.9977\\
7 & 1.3001\cdot10^{10} & 1.2981\cdot10^{10} & 0.9984\\
8 & -4.7015\cdot10^{11} & -4.6973\cdot10^{11} & 0.9991
\end{array}
\]

This is excellent evidence that the explicit-formula construction is the
right completion language. The slow component is \(m=1\), where the zero
sum has the weakest convergence. For \(m\ge2\), the finite zero packet
already tracks the oracle \(r=3\) completion to about \(0.1\%\)-\(0.3\%\).

But determinant space is still unforgiving:

\[
\begin{array}{c|c|c}
\text{gate} & \text{zero-packet }r=3\text{ completion}
& \text{true completion}\\
\hline
D_0 & 1.2547\cdot10^{-1} & 2.3105\cdot10^{-2}\\
D_1 & -8.0563\cdot10^{-1} & 1.9493\cdot10^{-9}\\
D_2 & -1.2211\cdot10^{4} & 2.1728\cdot10^{-22}\\
D_3 & 8.3893\cdot10^{10} & 1.1776\cdot10^{-41}\\
G_0 & -4.0120\cdot10^{-2} & 7.8474\cdot10^{-5}\\
G_1 & -2.0954\cdot10^{1} & 2.8438\cdot10^{-15}\\
G_2 & 1.1742\cdot10^{7} & 4.1558\cdot10^{-32}\\
G_3 & 1.6692\cdot10^{15} & 1.7885\cdot10^{-55}
\end{array}
\]

Thus the explicit-formula bridge is correct, but finite zero packets are not
yet gate certificates.

The resulting proof target is now exact:

\[
\boxed{
\text{prove a zero-tail and Möbius-tail certificate for}
\quad
P^{(2m)}(3/2)
\quad
\text{strong enough for the Jacobi gates.}
}
\]

Equivalently, the native completion theorem must control:

\[
\boxed{
\text{nontrivial-zero packet}
+\text{zero tail}
+\text{trivial/gamma ledger}
+\text{Möbius tail}
}
\]

as a single trace-gauge positive operator, not as independent scalar errors.

### 35.10 Zero-tail versus Möbius-tail

The next two probes separate the two analytic tails in the explicit-formula
completion.

The zero-tail probe

\[
\texttt{probe\_pass3\_zero\_tail\_certificate.py}
\]

compares finite zero packets against exact
\((\log\zeta)^{(k)}(3/2)\). The relative errors are:

\[
\begin{array}{c|ccccc}
k & M=10 & M=20 & M=50 & M=100 & M=200\\
\hline
2 & 4.96\cdot10^{-3} & 3.70\cdot10^{-3} & 2.36\cdot10^{-3}
& 1.61\cdot10^{-3} & 1.07\cdot10^{-3}\\
4 & 1.17\cdot10^{-7} & 3.90\cdot10^{-8} & 7.62\cdot10^{-9}
& 1.98\cdot10^{-9} & 4.73\cdot10^{-10}\\
6 & 6.15\cdot10^{-12} & 8.99\cdot10^{-13} & 5.25\cdot10^{-14}
& 5.11\cdot10^{-15} & 4.36\cdot10^{-16}\\
8 & 3.97\cdot10^{-16} & 2.54\cdot10^{-17} & 4.40\cdot10^{-19}
& 1.60\cdot10^{-20} & 4.86\cdot10^{-22}
\end{array}
\]

Thus the low cumulant \(k=2\) is the slow zero-tail bottleneck. For
\(k\ge4\), finite zero packets are already extremely accurate.

The Möbius-tail probe

\[
\texttt{probe\_pass3\_mobius\_tail\_certificate.py}
\]

uses the absolute convergence bound

\[
\left|(\log\zeta)^{(k)}(\sigma)\right|
\le
\sum_{q\ge2}(\log q)^kq^{-\sigma}
\le
(\log2)^k2^{-\sigma}
+
\int_2^\infty(\log t)^k t^{-\sigma}\,dt.
\]

For

\[
P^{(k)}(3/2)
=
\sum_{n\ge1}\mu(n)n^{k-1}
(\log\zeta)^{(k)}(3n/2),
\]

the omitted Möbius tail after cutoff \(N\) is therefore exponentially small
in \(N\). In folded \(r=3\) moment units, the probe reports:

\[
\begin{array}{c|cccc}
m & N=12 & N=24 & N=36 & N=60\\
\hline
1 & 2.28\cdot10^{-5} & 1.55\cdot10^{-10}
& 8.53\cdot10^{-16} & 2.00\cdot10^{-26}\\
2 & 3.12\cdot10^{-3} & 7.35\cdot10^{-8}
& 8.70\cdot10^{-13} & 5.48\cdot10^{-23}\\
3 & 1.32\cdot10^{-1} & 1.05\cdot10^{-5}
& 2.67\cdot10^{-10} & 4.50\cdot10^{-20}\\
4 & 2.75 & 7.25\cdot10^{-4}
& 3.91\cdot10^{-8} & 1.76\cdot10^{-17}\\
5 & 3.54\cdot10^{1} & 2.93\cdot10^{-2}
& 3.36\cdot10^{-6} & 4.02\cdot10^{-15}\\
6 & 3.21\cdot10^{2} & 7.87\cdot10^{-1}
& 1.89\cdot10^{-4} & 6.03\cdot10^{-13}\\
7 & 2.25\cdot10^{3} & 1.51\cdot10^{1}
& 7.57\cdot10^{-3} & 6.37\cdot10^{-11}\\
8 & 1.32\cdot10^{4} & 2.18\cdot10^{2}
& 2.26\cdot10^{-1} & 5.01\cdot10^{-9}
\end{array}
\]

So the visible error in the 100-zero, \(N=24\) explicit-formula probe is not
primarily a Möbius-tail problem. It is a zero-tail problem, with \(k=2\) the
slowest mode.

The proof target sharpens again:

\[
\boxed{
\text{prove the }k=2\text{ zero-tail correction at }s=3/2,
\quad
\text{then lift the already-fast }k\ge4\text{ tails into the gate.}
}
\]

In operator language:

\[
\boxed{
\text{the first mass/radius gate is zero-tail sensitive;}
\quad
\text{higher gates are determinant-sensitive.}
}
\]

### 35.11 The \(k=2\) zero-tail certificate

For \(s=3/2\), the \(k=2\) zero-pair contribution has an elementary
positive form. If

\[
\rho=\frac12+i\gamma,
\]

then

\[
-
\left(
\frac{1}{(\rho-s)^2}
+
\frac{1}{(\overline{\rho}-s)^2}
\right)
=
2\,\frac{\gamma^2-1}{(\gamma^2+1)^2}
\le
\frac{2}{\gamma^2}.
\]

Thus, after retaining all zero ordinates \(\gamma\le T\), the omitted
\(k=2\) zero-pair tail is bounded by

\[
2\sum_{\gamma>T}\frac{1}{\gamma^2}.
\]

Let \(N(T)\) count nontrivial zeros with \(0<\Im\rho\le T\). Using the
explicit Riemann--von Mangoldt envelope

\[
\left|
N(T)-\frac{T}{2\pi}\log\left(\frac{T}{2\pi e}\right)
\right|
\le
0.1038\log T+0.2573\log\log T+9.3675,
\]

one obtains an explicit upper envelope \(N_{\mathrm{up}}(T)\). For
\(T=\gamma_M\), where the first \(M\) ordinates have been retained,
Stieltjes integration gives

\[
\sum_{\gamma>T}\frac1{\gamma^2}
=
-\frac{N(T)}{T^2}
+
2\int_T^\infty \frac{N(t)}{t^3}\,dt
\le
-\frac{M}{T^2}
+
2\int_T^\infty \frac{N_{\mathrm{up}}(t)}{t^3}\,dt.
\]

Therefore

\[
\boxed{
E_{2,\mathrm{zero}}(T)
\le
2\left(
-\frac{M}{T^2}
+
2\int_T^\infty \frac{N_{\mathrm{up}}(t)}{t^3}\,dt
\right).
}
\]

The probe

\[
\texttt{probe\_pass3\_k2\_zero\_tail\_bound.py}
\]

compares this certificate with the observed zero-tail error in
\((\log\zeta)''(3/2)\):

\[
\begin{array}{c|c|c|c|c}
M & \gamma_M & \text{observed tail}
& \text{boundary bound}
& \text{ratio}\\
\hline
10 & 49.7738 & 1.9116\cdot10^{-2} & 2.7343\cdot10^{-2} & 1.43\\
20 & 77.1448 & 1.4271\cdot10^{-2} & 1.7721\cdot10^{-2} & 1.24\\
50 & 143.1118 & 9.1072\cdot10^{-3} & 1.0120\cdot10^{-2} & 1.11\\
100 & 236.5242 & 6.2216\cdot10^{-3} & 6.5951\cdot10^{-3} & 1.06\\
200 & 396.3819 & 4.1217\cdot10^{-3} & 4.2556\cdot10^{-3} & 1.03\\
500 & 811.1844 & 2.2976\cdot10^{-3} & 2.3299\cdot10^{-3} & 1.01
\end{array}
\]

This is the first genuinely effective zero-tail certificate in the pass. It
is not merely qualitative: by \(M=100\) it is within about \(6\%\) of the
observed tail, and by \(M=500\) within about \(1.5\%\).

So the \(k=2\) bottleneck is now checkable:

\[
\boxed{
\text{finite zero packet}
+
\text{explicit }N(T)\text{ tail}
\quad
\text{certifies }(\log\zeta)''(3/2).
}
\]

The remaining difficulty is not the existence of a tail bound. It is the
transport of these certified zero-tail intervals through the ultra-thin
Jacobi gate chamber.

### 35.12 Hybrid split: zero formula only at the critical Möbius term

The all-zero-packet explicit-formula probe deliberately exposed a trap.
For \(k=2\), applying a finite zero packet to every Möbius term

\[
\mu(n)n^{k-1}(\log\zeta)^{(k)}(3n/2)
\]

is not a good certificate. For \(n\ge2\), one has \(3n/2\ge3\), and the
zero ledger, gamma ledger, and trivial-zero ledger nearly cancel to a tiny
absolutely convergent value. A finite zero packet by itself does not capture
that cancellation efficiently.

The correct split is:

\[
\boxed{
\begin{array}{rcl}
n=1 &:& \text{explicit zero formula }+\ N(T)\text{ zero-tail certificate},\\[1mm]
n\ge2 &:& \text{absolute-convergence Dirichlet/von Mangoldt certificate}.
\end{array}
}
\]

The probe

\[
\texttt{probe\_pass3\_hybrid\_r3\_completion\_split.py}
\]

implements this hybrid architecture. With \(100\) zeros and Möbius cutoff
\(60\), it reports:

\[
\begin{array}{c|c|c|c}
m & \text{oracle missing }r=3
& \text{hybrid missing }r=3
& \text{ratio}\\
\hline
1 & 7.4875\cdot10^{-2} & 6.5464\cdot10^{-2} & 0.8743\\
2 & -2.5976\cdot10^{1} & -2.5936\cdot10^{1} & 0.9984\\
3 & 3.0086\cdot10^{3} & 3.0022\cdot10^{3} & 0.9979\\
4 & -1.9354\cdot10^{5} & -1.9304\cdot10^{5} & 0.9974\\
5 & 8.9634\cdot10^{6} & 8.9395\cdot10^{6} & 0.9973\\
6 & -3.5262\cdot10^{8} & -3.5182\cdot10^{8} & 0.9977\\
7 & 1.3001\cdot10^{10} & 1.2981\cdot10^{10} & 0.9984\\
8 & -4.7015\cdot10^{11} & -4.6973\cdot10^{11} & 0.9991
\end{array}
\]

The spurious \(m=1\) overshoot of the all-zero-packet probe disappears.
Moreover, the \(k=2\) zero-tail certificate from §35.11 gives a rigorous
one-sided interval for the missing \(m=1\) correction:

\[
\text{hybrid }m=1\text{ missing}
=0.06546389684517,
\]

\[
\text{zero-tail bound in }\ell_1\text{ units}
=0.00989271765673.
\]

Thus

\[
\boxed{
0.06546389684517
\le
\Delta\mu_1^{(r=3)}
\le
0.07535661450190,
}
\]

and the oracle value

\[
0.07487495300453
\]

lies inside the certified interval.

This is the first certified component of completion that lands exactly where
the oracle says it should land.

The remaining gate mismatch is no longer the \(m=1\) mass correction. The
hybrid-completed gates are still outside the positive chamber:

\[
\begin{array}{c|c|c}
\text{gate} & \text{hybrid completed} & \text{true completed}\\
\hline
D_0 & 1.3694\cdot10^{-2} & 2.3105\cdot10^{-2}\\
D_1 & -8.9383\cdot10^{-2} & 1.9493\cdot10^{-9}\\
D_2 & -1.2947\cdot10^3 & 2.1728\cdot10^{-22}\\
G_0 & -4.0391\cdot10^{-2} & 7.8474\cdot10^{-5}\\
G_1 & -2.0819\cdot10^1 & 2.8438\cdot10^{-15}
\end{array}
\]

So the lock has moved:

\[
\boxed{
\text{mass completion is certifiable;}
\quad
\text{determinant completion requires correlated }m\ge2\text{ control.}
}
\]

The next target is therefore a correlated gate certificate for
\((\Delta\mu_2,\ldots,\Delta\mu_8)\), not another scalar \(m=1\) bound.

### 35.13 Gate sensitivity: the top-rung pattern

The probe

\[
\texttt{probe\_pass3\_gate\_sensitivity\_jacobian.py}
\]

computes the exact cofactor gradient of each determinant gate with respect
to the moment coordinates. At the true completed ledger, the remaining
hybrid-to-true correction is:

\[
\begin{array}{c|c|c|c}
m & \mu_m^{\mathrm{hyb}} & \mu_m^{\mathrm{true}} & \Delta\mu_m\\
\hline
1 & 1.3694\cdot10^{-2} & 2.3105\cdot10^{-2} & 9.4111\cdot10^{-3}\\
2 & 4.0459\cdot10^{-2} & 3.7173\cdot10^{-5} & -4.0422\cdot10^{-2}\\
3 & -6.4077 & 1.4417\cdot10^{-7} & 6.4077\\
4 & 5.0112\cdot10^{2} & 6.6303\cdot10^{-10} & -5.0112\cdot10^{2}\\
5 & -2.3951\cdot10^{4} & 3.2137\cdot10^{-12} & 2.3951\cdot10^{4}\\
6 & 7.9691\cdot10^{5} & 1.5877\cdot10^{-14} & -7.9691\cdot10^{5}\\
7 & -2.0277\cdot10^{7} & 7.9033\cdot10^{-17} & 2.0277\cdot10^{7}\\
8 & 4.2555\cdot10^{8} & 3.9465\cdot10^{-19} & -4.2555\cdot10^{8}
\end{array}
\]

The gradient top terms show a clean top-rung law:

\[
\begin{array}{c|c|c}
\text{gate} & \text{dominant linear term} & \text{top rung}\\
\hline
D_0 & 9.411\cdot10^{-3} & \mu_1\\
D_1 & 1.480\cdot10^{-1} & \mu_3\\
D_2 & 4.669\cdot10^{-5} & \mu_5\\
D_3 & 4.406\cdot10^{-15} & \mu_7\\
G_0 & 4.042\cdot10^{-2} & \mu_2\\
G_1 & 3.932\cdot10^{-2} & \mu_4\\
G_2 & 2.266\cdot10^{-9} & \mu_6\\
G_3 & 1.769\cdot10^{-23} & \mu_8
\end{array}
\]

Thus the gates split into two ladders:

\[
\boxed{
D_i\ \text{is top-rung sensitive to }\mu_{2i+1},
\qquad
G_i\ \text{is top-rung sensitive to }\mu_{2i+2}.
}
\]

This is exactly the odd/even structure expected from Hankel and upper-radius
localizer matrices:

\[
D_i=\det[\mu_{a+b+1}]_{a,b=0}^{i}
\quad\text{uses top moment }\mu_{2i+1},
\]

\[
G_i=\det[\rho\mu_{a+b+1}-\mu_{a+b+2}]_{a,b=0}^{i}
\quad\text{uses top moment }\mu_{2i+2}.
\]

However, this is only the first-order geometry at the true completed ledger.
The hybrid point is far away, so higher powers in the determinant polynomial
still dominate the raw gate values. This explains why scalar intervals fail:
the chamber is not merely narrow; it is polynomially curved.

The next certificate should therefore be organized gate by gate, top rung by
top rung:

\[
\boxed{
\mu_1\Rightarrow D_0,\quad
\mu_2\Rightarrow G_0,\quad
\mu_3\Rightarrow D_1,\quad
\mu_4\Rightarrow G_1,\quad\ldots
}
\]

The completion problem has become a ladder again.

### 35.14 Top-rung thresholds

The top-rung law is not only a numerical sensitivity pattern. It is an exact
determinant fact.

For the Hankel gate

\[
D_i=\det[\mu_{a+b+1}]_{a,b=0}^{i},
\]

the top moment \(\mu_{2i+1}\) appears only in the lower-right entry. Hence,
holding \(\mu_1,\ldots,\mu_{2i}\) fixed,

\[
D_i
=
D_{i-1}\,\mu_{2i+1}
+
B_i(\mu_1,\ldots,\mu_{2i}).
\]

Similarly, for the upper-radius localizer

\[
G_i=\det[\rho\mu_{a+b+1}-\mu_{a+b+2}]_{a,b=0}^{i},
\]

the top moment \(\mu_{2i+2}\) appears only in the lower-right entry with
coefficient \(-1\). Therefore

\[
G_i
=
-G_{i-1}\,\mu_{2i+2}
+
C_i(\mu_1,\ldots,\mu_{2i+1}).
\]

Thus, once the lower gate is positive, the next top rung has an exact
one-dimensional threshold:

\[
\boxed{
D_i>0
\quad\Longleftrightarrow\quad
\mu_{2i+1}>\theta_i^{D},
}
\]

\[
\boxed{
G_i>0
\quad\Longleftrightarrow\quad
\mu_{2i+2}<\theta_i^{G}.
}
\]

The probe

\[
\texttt{probe\_pass3\_top\_rung\_thresholds.py}
\]

computes these thresholds using the true completed lower prefix:

\[
\begin{array}{c|c|c|c|c}
\text{gate} & \text{top rung} & \text{threshold}
& \text{hybrid top} & \text{true top}\\
\hline
D_0 & \mu_1 & 0 & 1.3694\cdot10^{-2} & 2.3105\cdot10^{-2}\\
D_1 & \mu_3 & 5.9805\cdot10^{-8} & -6.4077 & 1.4417\cdot10^{-7}\\
D_2 & \mu_5 & 3.1022\cdot10^{-12} & -2.3951\cdot10^4 & 3.2137\cdot10^{-12}\\
D_3 & \mu_7 & 7.8979\cdot10^{-17} & -2.0277\cdot10^7 & 7.9033\cdot10^{-17}\\
G_0 & \mu_2 & 1.1565\cdot10^{-4} & 4.0459\cdot10^{-2} & 3.7173\cdot10^{-5}\\
G_1 & \mu_4 & 6.9927\cdot10^{-10} & 5.0112\cdot10^2 & 6.6303\cdot10^{-10}\\
G_2 & \mu_6 & 1.5892\cdot10^{-14} & 7.9691\cdot10^5 & 1.5877\cdot10^{-14}\\
G_3 & \mu_8 & 3.9465\cdot10^{-19} & 4.2555\cdot10^8 & 3.9465\cdot10^{-19}
\end{array}
\]

The hybrid top rungs fail every nontrivial threshold except \(D_0\). The
true top rungs pass all thresholds, usually by an extremely small margin.

The threshold fraction

\[
\lambda_*=
\frac{\theta-\mu^{\mathrm{hyb}}_{\mathrm{top}}}
{\mu^{\mathrm{true}}_{\mathrm{top}}-\mu^{\mathrm{hyb}}_{\mathrm{top}}}
\]

is essentially \(1\) for all higher gates. For example:

\[
\lambda_*(D_1)=0.999999986833,
\qquad
\lambda_*(G_0)=0.998058646774.
\]

So the determinant chamber is not just thin; it sits almost exactly at the
completed top rung.

This gives the inductive proof shape:

\[
\boxed{
\begin{array}{rcl}
\text{certify }D_{i-1}>0
&\Longrightarrow&
\text{certify the lower threshold }\theta_i^D,\\[1mm]
\text{then prove }\mu_{2i+1}>\theta_i^D
&\Longrightarrow&
D_i>0,
\end{array}
}
\]

and

\[
\boxed{
\begin{array}{rcl}
\text{certify }G_{i-1}>0
&\Longrightarrow&
\text{certify the upper threshold }\theta_i^G,\\[1mm]
\text{then prove }\mu_{2i+2}<\theta_i^G
&\Longrightarrow&
G_i>0.
\end{array}
}
\]

The gate proof is now an alternating ladder of one-dimensional threshold
certificates, not a simultaneous high-dimensional determinant problem.

### 35.15 Threshold margins are determinant ratios

The threshold ladder has a second simplification. The distance past the
threshold is itself an adjacent determinant ratio.

For the Hankel gates,

\[
D_i
=
D_{i-1}(\mu_{2i+1}-\theta_i^D),
\]

so

\[
\boxed{
\mu_{2i+1}-\theta_i^D
=
\frac{D_i}{D_{i-1}}.
}
\]

For the upper-radius gates,

\[
G_i
=
G_{i-1}(\theta_i^G-\mu_{2i+2}),
\]

so

\[
\boxed{
\theta_i^G-\mu_{2i+2}
=
\frac{G_i}{G_{i-1}}.
}
\]

The probe

\[
\texttt{probe\_pass3\_threshold\_margins.py}
\]

computes these margins. For the completed ledger:

\[
\begin{array}{c|c|c|c}
\text{gate} & \text{top rung} & \text{margin}
& \text{margin}/|\text{hybrid-to-true correction}|\\
\hline
D_0 & \mu_1 & 2.3105\cdot10^{-2} & 2.455\\
D_1 & \mu_3 & 8.4369\cdot10^{-8} & 1.32\cdot10^{-8}\\
D_2 & \mu_5 & 1.1146\cdot10^{-13} & 4.65\cdot10^{-18}\\
D_3 & \mu_7 & 5.4196\cdot10^{-20} & 2.67\cdot10^{-27}\\
G_0 & \mu_2 & 7.8474\cdot10^{-5} & 1.94\cdot10^{-3}\\
G_1 & \mu_4 & 3.6239\cdot10^{-11} & 7.23\cdot10^{-14}\\
G_2 & \mu_6 & 1.4613\cdot10^{-17} & 1.83\cdot10^{-23}\\
G_3 & \mu_8 & 4.3038\cdot10^{-24} & 1.01\cdot10^{-32}
\end{array}
\]

This is too thin for independent moment certificates. For example,
\(D_2\) requires a top-rung residue on the order of \(10^{-13}\) after a
remaining correction of size \(10^4\). The certificate must know the
determinant ratio, not merely the top moment.

Therefore the final form of the gate proof should not be:

\[
\text{estimate moments}
\quad\Longrightarrow\quad
\text{estimate determinants}.
\]

It should be:

\[
\boxed{
\text{construct the adjacent determinant ratios directly}
\quad
\frac{D_i}{D_{i-1}},\ \frac{G_i}{G_{i-1}}.
}
\]

In Jacobi language, these ratios are not arbitrary. They are exactly the
positive transfer residues of the moment ladder: squared norm increments,
localizer norm increments, and ultimately the positive off-rung data of the
GNS/Jacobi operator.

This is the next proof target:

\[
\boxed{
\text{replace top-moment threshold certification by}
\quad
\text{direct ratio certification.}
}
\]

### 35.16 T5 bridge: determinant ratios are harmonic-gauge coordinates

T5 supplies the missing interpretation of the previous section. A direct
determinant ratio is not just a numerically convenient margin. It is the
harmonic-dual coordinate of the gate ladder.

The relevant T5 dictionary is:

\[
\begin{array}{c|c}
\text{T5 object} & \text{Pass-3 import}\\
\hline
\text{reciprocal closure} & \text{ratios replace absolute determinant volumes}\\
\text{softmax/softmin mirror} & \text{odd and even gate sensitivities separate}\\
\text{harmonic Helmert reading} & \text{the same ladder is queried in reciprocal units}\\
\text{denominator arithmetic} & \text{thin positive residues are lcm/trace obstructions}
\end{array}
\]

Thus the ratios

\[
R_i^D:=\frac{D_i}{D_{i-1}},
\qquad
R_i^G:=\frac{G_i}{G_{i-1}}
\]

should be treated as primary coordinates. Their logarithms

\[
\lambda_i^D:=\log R_i^D,
\qquad
\lambda_i^G:=\log R_i^G
\]

are the additive ledger of the reciprocal gate.

The probe

\[
\texttt{probe\_pass3\_t5\_dual\_gate\_ledger.py}
\]

gives:

\[
\begin{array}{c|c|c}
\text{gate} & R_i & \log R_i\\
\hline
D_0 & 2.3104993\cdot 10^{-2} & -3.7677065\\
D_1 & 8.4368584\cdot 10^{-8} & -16.2880707\\
D_2 & 1.1146416\cdot 10^{-13} & -29.8250733\\
D_3 & 5.4196245\cdot 10^{-20} & -44.3616753\\
\hline
G_0 & 7.8473532\cdot 10^{-5} & -9.4527492\\
G_1 & 3.6239121\cdot 10^{-11} & -24.0408819\\
G_2 & 1.4613451\cdot 10^{-17} & -38.7645893\\
G_3 & 4.3037530\cdot 10^{-24} & -53.8025548
\end{array}
\]

This is exactly the kind of object T5 was built to see: a positive quantity
whose meaningful measurement is reciprocal, relative, and logarithmic.

The even/odd split also stops looking accidental. Section 35.13 found that
the Hankel gates \(D_i\) are top-sensitive to the odd rungs
\(\mu_{2i+1}\), while the localizer gates \(G_i\) are top-sensitive to the
even rungs \(\mu_{2i+2}\). T5 explains why this split belongs here:

\[
\log(A/H)
\quad\text{carries the even cumulant ledger,}
\]

while

\[
\log(AH/G^2)
\quad\text{carries the odd cumulant ledger.}
\]

So the Pass-3 determinant ladder is not merely a Stieltjes positivity test.
It is a coupled arithmetic-harmonic gauge:

\[
\boxed{
\begin{array}{c}
D\text{-gates certify the odd harmonic skew residues},\\
G\text{-gates certify the even arithmetic-harmonic spread residues}.
\end{array}
}
\]

This changes the proof target one more time. The next object should not be a
raw moment estimate or even a raw determinant estimate. It should be a
reciprocal transfer construction:

\[
\boxed{
\text{construct the log determinant-ratio ledger}
\quad
\{\lambda_i^D,\lambda_i^G\}_{i\ge0}
\quad
\text{as a positive harmonic-gauge carrier.}
}
\]

Equivalently:

\[
\boxed{
\text{direct ratio certification is T5 harmonic gauge on the Jacobi ladder.}
}
\]

### 35.17 Transfer identity: ratios are monic norm squares

The T5 bridge is not only interpretive. It has a finite algebraic theorem
behind it.

Let \(L\) be a moment functional with

\[
L(t^k)=\mu_k,
\]

and define the Hankel determinants

\[
D_i:=\det(\mu_{a+b})_{0\le a,b\le i},
\qquad
D_{-1}:=1.
\]

Let \(P_i(t)\) be the monic orthogonal polynomial of degree \(i\), whenever
it exists, and set

\[
h_i:=L(P_i^2).
\]

Then

\[
\boxed{
h_i=\frac{D_i}{D_{i-1}}.
}
\]

Thus the adjacent determinant ratios are not secondary diagnostics. They
are the monic norm-square ladder itself.

Moreover, if

\[
tP_i=P_{i+1}+\alpha_iP_i+\beta_{i-1}^2P_{i-1}
\]

is the monic Jacobi recurrence, then

\[
\boxed{
\beta_i^2=\frac{h_{i+1}}{h_i}
=
\frac{D_{i+1}D_{i-1}}{D_i^2}.
}
\]

In log coordinates,

\[
\boxed{
2\log\beta_i
=
\log h_{i+1}-\log h_i.
}
\]

So the T5 log-ratio ledger is the additive transfer ledger of the Jacobi
operator.

The upper-radius gates have the same form. Define the boundary-complement
functional

\[
L_R(f):=L((R-t)f(t)),
\qquad
R=\gamma_1^{-2},
\]

so that

\[
L_R(t^k)=R\mu_k-\mu_{k+1}.
\]

Then

\[
G_i
=
\det(R\mu_{a+b}-\mu_{a+b+1})_{0\le a,b\le i}
\]

is simply the \(i\)-th Hankel determinant of \(L_R\). If \(Q_i\) are the
monic orthogonal polynomials for \(L_R\), with

\[
k_i:=L_R(Q_i^2),
\]

then

\[
\boxed{
k_i=\frac{G_i}{G_{i-1}},
\qquad
(\beta_i^{(R)})^2=\frac{k_{i+1}}{k_i}.
}
\]

Therefore Pass-3 has two coupled transfer ledgers:

\[
\boxed{
\begin{array}{c|c|c}
\text{gate} & \text{monic norm ladder} & \text{transfer ladder}\\
\hline
D_i & h_i=D_i/D_{i-1} & \beta_i^2=h_{i+1}/h_i\\
G_i & k_i=G_i/G_{i-1} & (\beta_i^{(R)})^2=k_{i+1}/k_i
\end{array}
}
\]

The probe

\[
\texttt{probe\_pass3\_t5\_transfer\_identities.py}
\]

confirms the identities on the completed ledger:

\[
\begin{array}{c|c|c}
i & h_{i+1}/h_i & \beta_i^2\\
\hline
0 & 3.6515304\cdot10^{-6} & 3.6515304\cdot10^{-6}\\
1 & 1.3211572\cdot10^{-6} & 1.3211572\cdot10^{-6}\\
2 & 4.8622127\cdot10^{-7} & 4.8622127\cdot10^{-7}\\
3 & 3.0745322\cdot10^{-7} & 3.0745322\cdot10^{-7}
\end{array}
\]

and for the boundary-complement functional:

\[
\begin{array}{c|c|c}
i & k_{i+1}/k_i & (\beta_i^{(R)})^2\\
\hline
0 & 4.6180056\cdot10^{-7} & 4.6180056\cdot10^{-7}\\
1 & 4.0325071\cdot10^{-7} & 4.0325071\cdot10^{-7}\\
2 & 2.9450627\cdot10^{-7} & 2.9450627\cdot10^{-7}\\
3 & 2.3328105\cdot10^{-7} & 2.3328105\cdot10^{-7}
\end{array}
\]

This gives the gate-aware proof target in its cleanest form:

\[
\boxed{
\text{construct the two monic norm ladders }(h_i),(k_i)
\text{ natively and prove their positive transfer flow.}
}
\]

The \(D\)-gates and \(G\)-gates are no longer two unrelated determinant
families. They are the primal and boundary-complement harmonic gauges of
one bounded Jacobi carrier.

### 35.18 Pivot form: ratios are rebalanced residuals

There is an even more local form. Determinant ratios can be computed without
forming determinants.

For \(n\ge1\), let

\[
H_{n-1}:=(\mu_{a+b})_{0\le a,b<n},
\qquad
v_n:=(\mu_n,\mu_{n+1},\ldots,\mu_{2n-1})^T.
\]

Then the \(n\)-th monic norm square is the Schur pivot

\[
\boxed{
h_n
=
\mu_{2n}-v_n^T H_{n-1}^{-1}v_n
=
\frac{D_n}{D_{n-1}}.
}
\]

This is the centered-rebalanced form of the gate: project \(t^n\) onto the
lower ladder \(1,t,\ldots,t^{n-1}\), subtract the projection, and measure
the residual square.

For the upper-radius gate, set

\[
\nu_k:=R\mu_k-\mu_{k+1},
\qquad
K_{n-1}:=(\nu_{a+b})_{0\le a,b<n},
\qquad
w_n:=(\nu_n,\ldots,\nu_{2n-1})^T.
\]

Then

\[
\boxed{
k_n
=
\nu_{2n}-w_n^T K_{n-1}^{-1}w_n
=
\frac{G_n}{G_{n-1}}.
}
\]

Thus the determinant gates can be replaced by recursive scalar pivots:

\[
\boxed{
\begin{array}{c}
h_n>0\quad\text{for the interior functional }L,\\
k_n>0\quad\text{for the boundary-complement functional }L_R.
\end{array}
}
\]

The probe

\[
\texttt{probe\_pass3\_t5\_schur\_pivots.py}
\]

checks the completed ledger:

\[
\begin{array}{c|c|c}
n & h_n=D_n/D_{n-1} & k_n=G_n/G_{n-1}\\
\hline
0 & 2.3104993\cdot10^{-2} & 7.8473532\cdot10^{-5}\\
1 & 8.4368584\cdot10^{-8} & 3.6239121\cdot10^{-11}\\
2 & 1.1146416\cdot10^{-13} & 1.4613451\cdot10^{-17}\\
3 & 5.4196245\cdot10^{-20} & 4.3037530\cdot10^{-24}\\
4 & 1.6662810\cdot10^{-26} & 1.0039840\cdot10^{-30}
\end{array}
\]

This is the Pass-3 dish reduced to its smallest local pieces:

\[
\boxed{
\text{prove positive Schur pivots after each centered rebalancing step.}
}
\]

The determinant language is global volume language. The pivot language is
local residual language. T5 tells us why the pivot language is natural:
each pivot is a reciprocal-gauge measurement of what remains after the
previous ladder has been removed.

### 35.19 Pivot component ledger: the half-compensation law

The Schur-pivot form exposes one more layer. The pivot \(h_n\) is nonlinear
as a function of the moment ledger, because the residual polynomial itself
depends on the lower moments. But once the completed ledger has chosen the
monic residual \(P_n\), the pivot is a linear square observable:

\[
h_n=L(P_n^2).
\]

Therefore we can evaluate the same \(P_n^2\) against the three completed
ledger pieces:

\[
L=L_{\mathrm{end}}+L_{\Gamma}+L_{\zeta}.
\]

The probe

\[
\texttt{probe\_pass3\_t5\_pivot\_component\_ledger.py}
\]

does this for both the interior functional \(L\) and the boundary-complement
functional \(L_R\).

For the interior pivots, it finds:

\[
\begin{array}{c|c|c|c|c}
n & h_n & L_{\mathrm{end}}(P_n^2)
& L_{\Gamma}(P_n^2) & L_{\zeta}(P_n^2)\\
\hline
0 & 2.3105\cdot10^{-2} & -4.0000 & 2.1497 & 1.8734\\
1 & 8.4369\cdot10^{-8} & -64.0515 & 32.0279 & 32.0236\\
2 & 1.1146\cdot10^{-13} & -1026.6180 & 513.3090 & 513.3089\\
3 & 5.4196\cdot10^{-20} & -16440.6577 & 8220.3288 & 8220.3288\\
4 & 1.6663\cdot10^{-26} & -263210.6208 & 131605.3104 & 131605.3104
\end{array}
\]

Normalized against the endpoint debt \(-L_{\mathrm{end}}(P_n^2)\), the same
data becomes:

\[
\begin{array}{c|c|c|c|c}
n & h_n/(-E_n) & \Gamma_n/(-E_n) & Z_n/(-E_n)
& (\Gamma_n-Z_n)/(-E_n)\\
\hline
0 & 5.7762\cdot10^{-3} & 0.5374165 & 0.4683597 & 6.9057\cdot10^{-2}\\
1 & 1.3172\cdot10^{-9} & 0.5000338 & 0.4999662 & 6.7563\cdot10^{-5}\\
2 & 1.0857\cdot10^{-16} & 0.5000001 & 0.4999999 & 1.0914\cdot10^{-7}\\
3 & 3.2965\cdot10^{-24} & 0.5000000 & 0.5000000 & 1.7787\cdot10^{-10}\\
4 & 6.3306\cdot10^{-32} & 0.5000000 & 0.5000000 & 2.8866\cdot10^{-13}
\end{array}
\]

The boundary-complement pivots show the same pattern:

\[
\begin{array}{c|c|c|c|c}
n & k_n/(-E_n^R) & \Gamma_n^R/(-E_n^R) & Z_n^R/(-E_n^R)
& (\Gamma_n^R-Z_n^R)/(-E_n^R)\\
\hline
0 & 4.8985\cdot10^{-6} & 0.5009513 & 0.4990536 & 1.8977\cdot10^{-3}\\
1 & 1.4134\cdot10^{-13} & 0.5000013 & 0.4999987 & 2.6816\cdot10^{-6}\\
2 & 3.5597\cdot10^{-21} & 0.5000000 & 0.5000000 & 4.3268\cdot10^{-9}\\
3 & 6.5483\cdot10^{-29} & 0.5000000 & 0.5000000 & 7.0135\cdot10^{-12}\\
4 & 9.5425\cdot10^{-37} & 0.5000000 & 0.5000000 & 1.1363\cdot10^{-14}
\end{array}
\]

This suggests the local proof target:

\[
\boxed{
\text{endpoint creates a large negative pivot debt;}
\quad
\Gamma\text{ and }\zeta\text{ each pay asymptotically one half;}
\quad
\text{the small excess is positive.}
}
\]

Call this the **half-compensation law**. In proof form it should become an
inequality of the shape

\[
L_{\Gamma}(P_n^2)+L_{\zeta}(P_n^2)
>
-L_{\mathrm{end}}(P_n^2),
\]

and similarly for \(L_R\), with a controlled positive surplus. This is much
more precise than broad positivity. It says exactly where the positivity is
hiding: not in one piece, but in the paired Archimedean/zeta compensation
after each centered rebalancing.

### 35.20 Midline defect dominance

The half-compensation law can be written as a one-line dominance test.

For an interior pivot, set

\[
E_n:=L_{\mathrm{end}}(P_n^2)<0,
\qquad
S_n:=-E_n>0,
\]

and define the two midline defects

\[
a_n:=\frac{L_{\Gamma}(P_n^2)}{S_n}-\frac12,
\qquad
b_n:=\frac12-\frac{L_{\zeta}(P_n^2)}{S_n}.
\]

Then

\[
\boxed{
\frac{h_n}{S_n}=a_n-b_n.
}
\]

So the pivot is positive exactly when

\[
\boxed{
a_n>b_n.
}
\]

This is the most local form of the sign problem so far. The endpoint sets
the debt scale \(S_n\). The Archimedean side pays slightly more than half;
the zeta side pays slightly less than half. The Schur pivot is the surviving
difference.

Numerically:

\[
\begin{array}{c|c|c|c}
n & a_n=\Gamma/S-1/2 & b_n=1/2-Z/S & h_n/S\\
\hline
0 & 3.7417\cdot10^{-2} & 3.1640\cdot10^{-2} & 5.7762\cdot10^{-3}\\
1 & 3.3782\cdot10^{-5} & 3.3781\cdot10^{-5} & 1.3172\cdot10^{-9}\\
2 & 5.4572\cdot10^{-8} & 5.4572\cdot10^{-8} & 1.0857\cdot10^{-16}\\
3 & 8.8933\cdot10^{-11} & 8.8933\cdot10^{-11} & 3.2965\cdot10^{-24}\\
4 & 1.4433\cdot10^{-13} & 1.4433\cdot10^{-13} & 6.3306\cdot10^{-32}
\end{array}
\]

For the boundary-complement pivot, define \(E_n^R,S_n^R,a_n^R,b_n^R\) in
the same way using \(Q_n\) and \(L_R\). Then

\[
\boxed{
\frac{k_n}{S_n^R}=a_n^R-b_n^R,
\qquad
k_n>0\Longleftrightarrow a_n^R>b_n^R.
}
\]

The first boundary rows are:

\[
\begin{array}{c|c|c|c}
n & a_n^R & b_n^R & k_n/S_n^R\\
\hline
0 & 9.5128\cdot10^{-4} & 9.4638\cdot10^{-4} & 4.8985\cdot10^{-6}\\
1 & 1.3408\cdot10^{-6} & 1.3408\cdot10^{-6} & 1.4134\cdot10^{-13}\\
2 & 2.1634\cdot10^{-9} & 2.1634\cdot10^{-9} & 3.5597\cdot10^{-21}\\
3 & 3.5067\cdot10^{-12} & 3.5067\cdot10^{-12} & 6.5483\cdot10^{-29}\\
4 & 5.6814\cdot10^{-15} & 5.6814\cdot10^{-15} & 9.5425\cdot10^{-37}
\end{array}
\]

This turns the next theorem into a narrow dominance statement:

\[
\boxed{
\text{prove that the Archimedean midline excess dominates the}
\quad
\zeta\text{-midline shortfall}
}
\]

for both the interior and boundary-complement residual ladders.

### 35.21 T6 bridge: pivots are RMS residual energies

T6 adds the complementary reading to T5.

T5 said:

\[
\text{read }h_n,k_n\text{ as reciprocal/log norm-square coordinates.}
\]

T6 says:

\[
\text{read }\sqrt{h_n},\sqrt{k_n}\text{ as RMS residual amplitudes.}
\]

Indeed, the Schur pivots are not arbitrary scalars. They are quadratic
energies:

\[
h_n=L(P_n^2),
\qquad
k_n=L_R(Q_n^2).
\]

Define the \(L^2\) residual amplitudes

\[
\|P_n\|_L:=\sqrt{L(P_n^2)}=\sqrt{h_n},
\qquad
\|Q_n\|_{L_R}:=\sqrt{L_R(Q_n^2)}=\sqrt{k_n}.
\]

Then the Jacobi transfer coefficients are amplitude ratios:

\[
\boxed{
\beta_n
=
\frac{\|P_{n+1}\|_L}{\|P_n\|_L}
=
\sqrt{\frac{h_{n+1}}{h_n}},
}
\]

and

\[
\boxed{
\beta_n^{(R)}
=
\frac{\|Q_{n+1}\|_{L_R}}{\|Q_n\|_{L_R}}
=
\sqrt{\frac{k_{n+1}}{k_n}}.
}
\]

The probe

\[
\texttt{probe\_pass3\_t6\_rms\_transfer\_amplitudes.py}
\]

prints the RMS amplitude ladder:

\[
\begin{array}{c|c|c|c}
n & h_n & \sqrt{h_n} & \beta_n\\
\hline
0 & 2.3105\cdot10^{-2} & 1.5200\cdot10^{-1} & 1.9109\cdot10^{-3}\\
1 & 8.4369\cdot10^{-8} & 2.9046\cdot10^{-4} & 1.1494\cdot10^{-3}\\
2 & 1.1146\cdot10^{-13} & 3.3386\cdot10^{-7} & 6.9730\cdot10^{-4}\\
3 & 5.4196\cdot10^{-20} & 2.3280\cdot10^{-10} & 5.5448\cdot10^{-4}\\
4 & 1.6663\cdot10^{-26} & 1.2908\cdot10^{-13} & 4.9769\cdot10^{-4}
\end{array}
\]

and for the boundary-complement ladder:

\[
\begin{array}{c|c|c|c}
n & k_n & \sqrt{k_n} & \beta_n^{(R)}\\
\hline
0 & 7.8474\cdot10^{-5} & 8.8585\cdot10^{-3} & 6.7956\cdot10^{-4}\\
1 & 3.6239\cdot10^{-11} & 6.0199\cdot10^{-6} & 6.3502\cdot10^{-4}\\
2 & 1.4613\cdot10^{-17} & 3.8228\cdot10^{-9} & 5.4268\cdot10^{-4}\\
3 & 4.3038\cdot10^{-24} & 2.0745\cdot10^{-12} & 4.8299\cdot10^{-4}\\
4 & 1.0040\cdot10^{-30} & 1.0020\cdot10^{-15} & 3.4140\cdot10^{-4}
\end{array}
\]

Thus T5 and T6 split the same object:

\[
\boxed{
\begin{array}{c|c}
\text{T5 harmonic gauge} & \log h_n,\log k_n\\
\text{T6 RMS gauge} & \sqrt{h_n},\sqrt{k_n}\\
\text{Jacobi transfer} & \beta_n,\beta_n^{(R)}
\end{array}
}
\]

The half-compensation law is therefore an \(L^2\)-energy cancellation law.
The midline dominance \(a_n>b_n\) proves that the residual energy is
positive; T6 then says its square root is the actual amplitude passed to the
next Jacobi rung.

T6 also explains why this is a pair-current problem rather than a scalar
tail problem. The pivot asks for a square:

\[
P_n^2.
\]

In character language, square closure obeys the quadratic selection rule

\[
a+b-c\equiv0\pmod N.
\]

So the next arithmetic audit should not only bound moments. It should
decompose the residual square \(P_n^2\) into quadratic conductor packets and
track which packets carry the Archimedean excess over the zeta shortfall.

The updated proof target is:

\[
\boxed{
\text{prove positive RMS residual amplitudes by quadratic conductor}
\quad
\text{half-compensation.}
}
\]

### 35.22 Pair-current packet target

T6 now lets the pivot be opened packetwise.

Write the monic residual polynomial as

\[
P_n(t)=\sum_{a=0}^n p_{n,a}t^a,
\qquad
p_{n,n}=1.
\]

Then its square has the quadratic pair-current expansion

\[
P_n(t)^2
=
\sum_{m=0}^{2n} C_{n,m}t^m,
\qquad
C_{n,m}:=\sum_{a+b=m}p_{n,a}p_{n,b}.
\]

This is the polynomial analogue of T6's square-closure rule

\[
a+b-c\equiv0.
\]

For each ledger piece

\[
X\in\{\mathrm{end},\Gamma,\zeta\},
\]

define the packet charge

\[
X_{n,m}:=C_{n,m}\,\mu_m^{(X)}.
\]

Let

\[
S_n:=-\sum_{m=0}^{2n}E_{n,m}
\]

be the endpoint debt scale. Then the midline defects split by packets:

\[
A_{n,m}:=\frac{\Gamma_{n,m}+E_{n,m}/2}{S_n},
\qquad
B_{n,m}:=-\frac{Z_{n,m}+E_{n,m}/2}{S_n}.
\]

Thus

\[
\boxed{
\frac{h_n}{S_n}
=
\sum_{m=0}^{2n}(A_{n,m}-B_{n,m}).
}
\]

The boundary-complement ladder has the identical formula with \(Q_n\),
\(k_n\), and the boundary moments

\[
\nu_m^{(X)}:=R\mu_m^{(X)}-\mu_{m+1}^{(X)}.
\]

The probe

\[
\texttt{probe\_pass3\_t6\_pair\_current\_ledger.py}
\]

computes these packet charges. The compact surplus summary is:

\[
\begin{array}{c|c|c|c|c}
\text{ladder} & n & \text{total surplus} & \text{top packet}
& \text{lower correction}\\
\hline
\text{interior} & 1 & 1.3172\cdot10^{-9} & 2.2509\cdot10^{-9} & -9.3371\cdot10^{-10}\\
\text{boundary} & 1 & 1.4134\cdot10^{-13} & 2.2854\cdot10^{-13} & -8.7192\cdot10^{-14}\\
\text{interior} & 2 & 1.0857\cdot10^{-16} & 3.1303\cdot10^{-15} & -3.0218\cdot10^{-15}\\
\text{boundary} & 2 & 3.5597\cdot10^{-21} & 5.0724\cdot10^{-20} & -4.7165\cdot10^{-20}\\
\text{interior} & 3 & 3.2965\cdot10^{-24} & 4.8072\cdot10^{-21} & -4.8039\cdot10^{-21}\\
\text{boundary} & 3 & 6.5483\cdot10^{-29} & 1.4205\cdot10^{-26} & -1.4140\cdot10^{-26}\\
\text{interior} & 4 & 6.3306\cdot10^{-32} & 7.4969\cdot10^{-27} & -7.4968\cdot10^{-27}\\
\text{boundary} & 4 & 9.5425\cdot10^{-37} & 4.2847\cdot10^{-33} & -4.2837\cdot10^{-33}
\end{array}
\]

This shows that the positivity is not packetwise. It is a signed
pair-current dominance:

\[
\Delta_{n,m}:=A_{n,m}-B_{n,m},
\qquad
\frac{h_n}{S_n}=\sum_m\Delta_{n,m}.
\]

The top packet \(m=2n\) carries a positive surplus, while the lower packets
almost cancel it. The finite gate target is therefore:

\[
\boxed{
\Delta_{n,2n}
>
-\sum_{m<2n}\Delta_{n,m}
}
\]

and similarly for the boundary-complement packets.

This is the sharpest local proof target now available:

\[
\boxed{
\text{prove top-pair RMS surplus dominates the lower pair-current}
\quad
\text{correction after Schur rebalancing.}
}
\]

### 35.23 Induction schema for the pair-current gate

The previous section gives an induction target.

For the interior ladder, assume the lower gates have already been proved:

\[
h_0,h_1,\ldots,h_{n-1}>0.
\]

Equivalently, the lower Hankel block \(H_{n-1}\) is positive definite. Then
the Schur residual

\[
P_n(t)=t^n-\Pi_{<n}t^n
\]

is well-defined, where \(\Pi_{<n}\) is projection onto the lower polynomial
ladder with respect to the already-positive lower moment pairing.

Now define packet surplus

\[
\Delta_{n,m}:=A_{n,m}-B_{n,m}.
\]

Then the next gate is equivalent to

\[
\boxed{
h_n>0
\quad\Longleftrightarrow\quad
\sum_{m=0}^{2n}\Delta_{n,m}>0.
}
\]

Since \(C_{n,2n}=1\), this may be written as the top-pair dominance test

\[
\boxed{
\Delta_{n,2n}
>
-\sum_{m<2n}\Delta_{n,m}.
}
\]

The boundary-complement induction is identical. Assume

\[
k_0,k_1,\ldots,k_{n-1}>0.
\]

Then the boundary residual

\[
Q_n(t)=t^n-\Pi_{<n}^{(R)}t^n
\]

is well-defined under \(L_R\), and the next boundary gate is equivalent to

\[
\boxed{
\Delta_{n,2n}^{(R)}
>
-\sum_{m<2n}\Delta_{n,m}^{(R)}.
}
\]

Thus the finite Pass-3 proof reduces to the double induction:

\[
\boxed{
\begin{array}{c}
\text{interior top-pair dominance advances }h_n>0,\\
\text{boundary top-pair dominance advances }k_n>0.
\end{array}
}
\]

The infinite proof would then require uniform control of this induction as
\(n\to\infty\), plus the support bound

\[
0\preceq J\preceq RI.
\]

This is now a precise theorem-shaped target, not a broad positivity wish.

### 35.24 Survival ratio target

The top-pair dominance test has a useful normalized form.

Define

\[
T_n:=\Delta_{n,2n},
\qquad
L_n:=\sum_{m<2n}\Delta_{n,m},
\qquad
\rho_n:=\frac{h_n/S_n}{T_n}.
\]

Then

\[
\boxed{
\rho_n
=
1+\frac{L_n}{T_n}.
}
\]

The gate condition is

\[
h_n>0
\quad\Longleftrightarrow\quad
\rho_n>0.
\]

Since \(L_n<0\) in the observed gates, \(\rho_n\) is the surviving fraction
of the top pair after lower-packet cancellation.

The probe

\[
\texttt{probe\_pass3\_t6\_top\_pair\_dominance\_scan.py}
\]

prints:

\[
\begin{array}{c|c|c|c}
n & T_n & L_n & \rho_n\\
\hline
1 & 2.2509\cdot10^{-9} & -9.3371\cdot10^{-10} & 5.8519\cdot10^{-1}\\
2 & 3.1303\cdot10^{-15} & -3.0218\cdot10^{-15} & 3.4684\cdot10^{-2}\\
3 & 4.8072\cdot10^{-21} & -4.8039\cdot10^{-21} & 6.8574\cdot10^{-4}\\
4 & 7.4969\cdot10^{-27} & -7.4968\cdot10^{-27} & 8.4443\cdot10^{-6}\\
5 & 1.1724\cdot10^{-32} & -1.1724\cdot10^{-32} & 8.3543\cdot10^{-8}\\
6 & 1.8348\cdot10^{-38} & -1.8348\cdot10^{-38} & 4.1510\cdot10^{-10}\\
7 & 2.8719\cdot10^{-44} & -2.8719\cdot10^{-44} & 1.2282\cdot10^{-12}\\
8 & 4.4955\cdot10^{-50} & -4.4955\cdot10^{-50} & 4.0319\cdot10^{-15}\\
9 & 7.0369\cdot10^{-56} & -7.0369\cdot10^{-56} & 1.0516\cdot10^{-17}\\
10 & 1.1016\cdot10^{-61} & -1.1016\cdot10^{-61} & 1.8177\cdot10^{-20}
\end{array}
\]

For the boundary-complement ladder:

\[
\begin{array}{c|c|c|c}
n & T_n^{(R)} & L_n^{(R)} & \rho_n^{(R)}\\
\hline
1 & 2.2854\cdot10^{-13} & -8.7192\cdot10^{-14} & 6.1848\cdot10^{-1}\\
2 & 5.0724\cdot10^{-20} & -4.7165\cdot10^{-20} & 7.0176\cdot10^{-2}\\
3 & 1.4205\cdot10^{-26} & -1.4140\cdot10^{-26} & 4.6098\cdot10^{-3}\\
4 & 4.2847\cdot10^{-33} & -4.2837\cdot10^{-33} & 2.2271\cdot10^{-4}\\
5 & 1.3328\cdot10^{-39} & -1.3328\cdot10^{-39} & 5.2132\cdot10^{-6}\\
6 & 4.2060\cdot10^{-46} & -4.2060\cdot10^{-46} & 7.5674\cdot10^{-8}\\
7 & 1.3365\cdot10^{-52} & -1.3365\cdot10^{-52} & 1.2285\cdot10^{-9}\\
8 & 4.2615\cdot10^{-59} & -4.2615\cdot10^{-59} & 1.5299\cdot10^{-11}\\
9 & 1.3612\cdot10^{-65} & -1.3612\cdot10^{-65} & 1.2815\cdot10^{-13}\\
10 & 4.3515\cdot10^{-72} & -4.3515\cdot10^{-72} & 8.5248\cdot10^{-16}
\end{array}
\]

The cancellation ratio

\[
-L_n/T_n
\]

approaches \(1\) from below. Thus the proof cannot rely on a fixed
separation. It needs an explicit positive survival asymptotic:

\[
\boxed{
\rho_n>0,
\qquad
\rho_n^{(R)}>0,
\qquad
\text{with controlled decay as }n\to\infty.
}
\]

This is now the exact analytic target behind the finite double induction.
The local theorem to prove is no longer merely top-pair dominance; it is
positive top-pair survival.

### 35.25 Survival angle identity

The survival ratio has an exact geometric meaning.

Since the top coefficient of the monic residual is \(1\),

\[
C_{n,2n}=1.
\]

Therefore the top packet is just the top monomial energy:

\[
T_n=\frac{\mu_{2n}}{S_n}.
\]

But the total pivot surplus is

\[
\frac{h_n}{S_n}.
\]

Hence

\[
\boxed{
\rho_n
=
\frac{h_n/S_n}{\mu_{2n}/S_n}
=
\frac{h_n}{\mu_{2n}}.
}
\]

Now recall that

\[
h_n
=
\|t^n-\Pi_{<n}t^n\|_L^2,
\qquad
\mu_{2n}
=
\|t^n\|_L^2.
\]

Thus

\[
\boxed{
\rho_n
=
\frac{\|t^n-\Pi_{<n}t^n\|_L^2}{\|t^n\|_L^2}
=
\sin^2\theta_n,
}
\]

where \(\theta_n\) is the angle between the monomial \(t^n\) and the lower
polynomial ladder

\[
\operatorname{span}\{1,t,\ldots,t^{n-1}\}.
\]

Similarly,

\[
\boxed{
\rho_n^{(R)}
=
\frac{k_n}{\nu_{2n}}
=
\sin^2\theta_n^{(R)}.
}
\]

The probe

\[
\texttt{probe\_pass3\_t6\_survival\_angle\_identity.py}
\]

prints the angles:

\[
\begin{array}{c|c|c}
n & \rho_n & \theta_n\\
\hline
1 & 5.8519\cdot10^{-1} & 8.7100\cdot10^{-1}\\
2 & 3.4684\cdot10^{-2} & 1.8733\cdot10^{-1}\\
3 & 6.8574\cdot10^{-4} & 2.6190\cdot10^{-2}\\
4 & 8.4443\cdot10^{-6} & 2.9059\cdot10^{-3}\\
5 & 8.3543\cdot10^{-8} & 2.8904\cdot10^{-4}\\
6 & 4.1510\cdot10^{-10} & 2.0374\cdot10^{-5}\\
7 & 1.2282\cdot10^{-12} & 1.1083\cdot10^{-6}\\
8 & 4.0319\cdot10^{-15} & 6.3497\cdot10^{-8}\\
9 & 1.0516\cdot10^{-17} & 3.2428\cdot10^{-9}\\
10 & 1.8177\cdot10^{-20} & 1.3482\cdot10^{-10}
\end{array}
\]

and for the boundary-complement ladder:

\[
\begin{array}{c|c|c}
n & \rho_n^{(R)} & \theta_n^{(R)}\\
\hline
1 & 6.1848\cdot10^{-1} & 9.0501\cdot10^{-1}\\
2 & 7.0176\cdot10^{-2} & 2.6811\cdot10^{-1}\\
3 & 4.6098\cdot10^{-3} & 6.7948\cdot10^{-2}\\
4 & 2.2271\cdot10^{-4} & 1.4924\cdot10^{-2}\\
5 & 5.2132\cdot10^{-6} & 2.2832\cdot10^{-3}\\
6 & 7.5674\cdot10^{-8} & 2.7509\cdot10^{-4}\\
7 & 1.2285\cdot10^{-9} & 3.5050\cdot10^{-5}\\
8 & 1.5299\cdot10^{-11} & 3.9114\cdot10^{-6}\\
9 & 1.2815\cdot10^{-13} & 3.5798\cdot10^{-7}\\
10 & 8.5248\cdot10^{-16} & 2.9197\cdot10^{-8}
\end{array}
\]

This reframes the induction one more time:

\[
\boxed{
\text{prove that every new monomial enters with nonzero residual angle}
\quad
\theta_n,\theta_n^{(R)}>0.
}
\]

The quantitative version is:

\[
\boxed{
\theta_n^2\sim\rho_n>0,
\qquad
(\theta_n^{(R)})^2\sim\rho_n^{(R)}>0,
}
\]

with explicit decay. This is the \(L^2\)-geometric face of the top-pair
dominance law.

### 35.26 Residual root locking

In the target trace-gauge spectral representation,

\[
\mu_k=\sum_{j\ge1}\lambda_j^{k+1},
\qquad
\lambda_j=\gamma_j^{-2},
\qquad
\lambda_1>\lambda_2>\cdots>0.
\]

The boundary-complement moments are

\[
\nu_k=R\mu_k-\mu_{k+1}
=
\sum_{j\ge1}(R-\lambda_j)\lambda_j^{k+1}.
\]

Since \(R=\lambda_1\), the first atom is killed:

\[
(R-\lambda_1)\lambda_1=0.
\]

Thus the boundary-complement ladder begins spectrally at \(\lambda_2\).

The probe

\[
\texttt{probe\_pass3\_t6\_residual\_roots.py}
\]

checks the roots of the residual polynomials. It finds the expected locking:

\[
P_n\text{ locks onto }\lambda_1,\ldots,\lambda_n,
\]

while

\[
Q_n\text{ locks onto }\lambda_2,\ldots,\lambda_{n+1}.
\]

For example, at \(n=8\):

\[
\begin{array}{c|c|c|c}
\text{ladder} & j & \text{root} & \text{relative error to target atom}\\
\hline
P_8 & 1 & 0.00500524412359366 & 9.13\cdot10^{-14}\\
P_8 & 2 & 0.00226282055364913 & 4.23\cdot10^{-7}\\
P_8 & 3 & 0.00159836028040746 & 1.57\cdot10^{-4}\\
P_8 & 4 & 0.00105004256659372 & 2.80\cdot10^{-2}\\
\hline
Q_8 & 1 & 0.00226282149845181 & 5.75\cdot10^{-9}\\
Q_8 & 2 & 0.00159859916578008 & 7.49\cdot10^{-6}\\
Q_8 & 3 & 0.00107214041309878 & 7.55\cdot10^{-3}\\
Q_8 & 4 & 0.000862268482014678 & 6.47\cdot10^{-2}
\end{array}
\]

This gives the spectral meaning of the residual angle:

\[
\theta_n
\quad\text{measures the uncancelled angle after }P_n
\text{ has learned the first }n\text{ atoms.}
\]

and

\[
\theta_n^{(R)}
\quad\text{measures the same after }Q_n
\text{ has learned atoms }2,\ldots,n+1.
\]

### 35.27 Spectral payer packets

The root-locking picture suggests a tempting but false simplification:
maybe the residual energy is paid by the next single atom. Numerically this
is too crude.

The probe

\[
\texttt{probe\_pass3\_t6\_spectral\_survival\_asymptotic.py}
\]

tests the one-next-atom product estimate. It has the right sign and scale
logic, but its ratios do not settle near \(1\) in the available range. The
surviving energy is therefore a spectral packet, not a single atom.

The exact target expansion is:

\[
h_n=\sum_{j\ge1}\lambda_j P_n(\lambda_j)^2,
\]

and

\[
k_n=\sum_{j\ge2}(\lambda_1-\lambda_j)\lambda_j Q_n(\lambda_j)^2.
\]

The probe

\[
\texttt{probe\_pass3\_t6\_spectral\_payers.py}
\]

sorts the atom contributions. For example:

\[
\begin{array}{c|c|c|c}
\text{ladder} & n & \text{largest payer zero} & \text{share of pivot}\\
\hline
\text{interior} & 4 & \lambda_3 & 0.4023\\
\text{boundary} & 4 & \lambda_3 & 0.2458\\
\text{interior} & 6 & \lambda_4 & 0.2744\\
\text{boundary} & 6 & \lambda_4 & 0.1890\\
\text{interior} & 8 & \lambda_5 & 0.3344\\
\text{boundary} & 8 & \lambda_6 & 0.2243
\end{array}
\]

So the proof target is not:

\[
\text{next atom pays the residual.}
\]

It is:

\[
\boxed{
\text{a positive spectral tail packet pays the residual angle after root locking.}
}
\]

This is important language discipline. The angle theorem should prove:

1. residual roots lock to the leading atoms;
2. the remaining spectral packet has positive \(L^2\) mass;
3. the boundary-complement version repeats after the top atom is removed.

That is the spectral version of the pair-current induction.

### 35.28 Non-circular form of the target theorem

The spectral language above is diagnostic. It names the desired object, but
it must not be used as an assumption in the RH proof.

The circular version would be:

\[
\text{assume }
\mu_k=\sum_{j\ge1}\lambda_j^{k+1},\quad \lambda_j>0,
\quad
\text{then prove }h_n,k_n>0.
\]

That is only the Stieltjes theorem applied after the answer is already
known.

The non-circular theorem must instead start from the completed ledger:

\[
\mu_k
=
\mu_k^{\mathrm{end}}
+\mu_k^{\Gamma}
+\mu_k^{\zeta},
\]

with the zeta piece represented by the continued explicit-formula
construction, and prove directly that the Schur residuals satisfy

\[
\boxed{
L(P_n^2)>0,
\qquad
L_R(Q_n^2)>0.
}
\]

Using the T5/T6 language, this becomes:

\[
\boxed{
\text{the completed explicit-formula ledger has positive RMS residual}
\quad
\text{amplitudes at every rung.}
}
\]

Equivalently, in the half-compensation variables:

\[
\boxed{
a_n>b_n,
\qquad
a_n^{(R)}>b_n^{(R)}
\quad
\text{for every }n.
}
\]

Equivalently, in the pair-current variables:

\[
\boxed{
\sum_{m=0}^{2n}\Delta_{n,m}>0,
\qquad
\sum_{m=0}^{2n}\Delta_{n,m}^{(R)}>0.
}
\]

Equivalently, in the geometric variables:

\[
\boxed{
\theta_n>0,
\qquad
\theta_n^{(R)}>0.
}
\]

The spectral root-locking and payer-packet probes are therefore not the
proof. They are the target signature. The proof must reproduce that
signature from:

1. endpoint debt;
2. Archimedean midline excess;
3. zeta/prime explicit-formula shortfall;
4. quadratic pair-current cancellation.

That is the current clean Pass-3 theorem:

\[
\boxed{
\textbf{Quadratic Half-Compensation Theorem.}
\quad
\text{For the completed centered xi ledger, every Schur residual has}
\quad
\text{positive interior and boundary-complement RMS energy.}
}
\]

Together with the support bound \(0\preceq J\preceq R I\), this is exactly
the finite gate system needed for the trace-gauge Stieltjes model.

### 35.29 Christoffel angle certificate

The survival angle has a standard moment-theory expression.

Let

\[
H_n=(\mu_{a+b})_{0\le a,b\le n}
\]

be the \(n\)-th Hankel block. Then the Schur pivot satisfies

\[
\boxed{
h_n=\frac{1}{(H_n^{-1})_{n,n}}.
}
\]

Therefore

\[
\boxed{
\rho_n
=
\frac{h_n}{\mu_{2n}}
=
\frac{1}{\mu_{2n}(H_n^{-1})_{n,n}}.
}
\]

Equivalently, if

\[
v_n=(\mu_n,\mu_{n+1},\ldots,\mu_{2n-1})^T
\]

and \(H_{n-1}=(\mu_{a+b})_{0\le a,b<n}\), then

\[
\boxed{
1-\rho_n
=
\frac{v_n^T H_{n-1}^{-1}v_n}{\mu_{2n}}.
}
\]

This is the projection fraction of \(t^n\) onto the lower polynomial ladder.
So the positivity target has three identical forms:

\[
\boxed{
\begin{array}{c}
h_n>0,\\
\rho_n>0,\\
t^n\notin\overline{\operatorname{span}}\{1,t,\ldots,t^{n-1}\}
\text{ at rung }n.
\end{array}
}
\]

For the boundary-complement ladder, with

\[
K_n=(\nu_{a+b})_{0\le a,b\le n},
\qquad
\nu_k=R\mu_k-\mu_{k+1},
\]

the identical formulas hold:

\[
\boxed{
k_n=\frac{1}{(K_n^{-1})_{n,n}},
\qquad
\rho_n^{(R)}
=
\frac{1}{\nu_{2n}(K_n^{-1})_{n,n}}.
}
\]

The probe

\[
\texttt{probe\_pass3\_t6\_christoffel\_angle\_certificate.py}
\]

checks:

\[
\rho_n
=
\frac{1}{\mu_{2n}(H_n^{-1})_{n,n}},
\qquad
\rho_n+
\frac{v_n^T H_{n-1}^{-1}v_n}{\mu_{2n}}
=1,
\]

and the boundary analogue.

This gives a fourth equivalent proof target:

\[
\boxed{
\text{prove positive Christoffel distance from each new monomial}
\quad
\text{to the lower completed ledger.}
}
\]

The value of this form is that it is no longer tied to the packet
decomposition. It can be attacked by inverse Hankel estimates, Christoffel
function bounds, or orthogonal-polynomial extremal principles.

### 35.30 Sum-of-squares cone gate

The pivot induction can also be stated without naming the monomial basis.

For a polynomial

\[
f(t)=\sum_{a=0}^n c_at^a,
\]

the interior quadratic form is

\[
L(f^2)
=
\sum_{a,b=0}^n c_ac_b\mu_{a+b}
=
c^T H_n c.
\]

Therefore

\[
\boxed{
H_n\succ0
\quad\Longleftrightarrow\quad
L(f^2)>0
\ \text{for every nonzero }f,\ \deg f\le n.
}
\]

Likewise, for

\[
L_R(f):=L((R-t)f(t)),
\]

the boundary-complement Gram matrix is

\[
K_n=(\nu_{a+b})_{0\le a,b\le n},
\qquad
\nu_k=R\mu_k-\mu_{k+1},
\]

and

\[
\boxed{
K_n\succ0
\quad\Longleftrightarrow\quad
L((R-t)f^2)>0
\ \text{for every nonzero }f,\ \deg f\le n.
}
\]

Thus the entire finite \([0,R]\) gate system is the three-part
sum-of-squares cone:

\[
\boxed{
L(f^2)>0,
\qquad
L(tf^2)>0,
\qquad
L((R-t)f^2)>0.
}
\]

For every degree \(n\), these are equivalent to all interior pivots

\[
h_0,\ldots,h_n>0
\]

and all boundary pivots

\[
k_0,\ldots,k_n>0.
\]

The lower-support cone

\[
L(tf^2)>0
\]

is the Stieltjes floor at \(t=0\). Its Gram matrix is the shifted Hankel
block

\[
J_n=(\mu_{a+b+1})_{0\le a,b\le n}.
\]

This cone should not be silently omitted. The upper cone \(L((R-t)f^2)>0\)
controls the ceiling \(R\); the lower cone controls the floor \(0\).

The probe

\[
\texttt{probe\_pass3\_t6\_sos\_cone\_eigencheck.py}
\]

prints the finite cone spectrum. The smallest eigenvalues through \(n=10\)
remain positive, while the condition numbers grow rapidly:

\[
\begin{array}{c|c|c|c|c}
n & \lambda_{\min}(H_n) & \kappa(H_n)
& \lambda_{\min}(K_n) & \kappa(K_n)\\
\hline
0 & 2.3105\cdot10^{-2} & 1 & 7.8474\cdot10^{-5} & 1\\
2 & 1.1146\cdot10^{-13} & 2.07\cdot10^{11}
& 1.4613\cdot10^{-17} & 5.37\cdot10^{12}\\
4 & 1.6662\cdot10^{-26} & 1.39\cdot10^{24}
& 1.0040\cdot10^{-30} & 7.82\cdot10^{25}\\
6 & 5.1363\cdot10^{-40} & 4.50\cdot10^{37}
& 8.5787\cdot10^{-45} & 9.15\cdot10^{39}\\
8 & 3.1310\cdot10^{-54} & 7.38\cdot10^{51}
& 4.5010\cdot10^{-59} & 1.74\cdot10^{54}\\
10 & 1.0132\cdot10^{-68} & 2.28\cdot10^{66}
& 2.7030\cdot10^{-67} & 2.90\cdot10^{62}
\end{array}
\]

This explains why broad estimates fail. The SOS cone is positive but
extremely thin. A successful proof must preserve the exact completed
structure:

\[
\boxed{
\text{endpoint debt}
\;+\;
\text{Archimedean excess}
\;+\;
\text{zeta explicit-formula shortfall}
\quad
\text{inside the SOS cone.}
}
\]

This is the cone form of the Quadratic Half-Compensation Theorem:

\[
\boxed{
\text{prove the completed explicit-formula functional is positive on}
\quad
f^2,\quad tf^2,\quad\text{and}\quad (R-t)f^2
\quad
\text{for every polynomial }f.
}
\]

### 35.31 Worst-cone directions

The Schur residuals are not just a convenient coordinate choice. Numerically,
they are the thinnest directions of the SOS cones.

The probe

\[
\texttt{probe\_pass3\_t6\_worst\_cone\_directions.py}
\]

takes the minimum-eigenvalue eigenvector of each finite Gram matrix \(H_n\)
and \(K_n\), then decomposes its square into endpoint, Archimedean, and zeta
pieces.

The output shows:

\[
\begin{array}{c|c|c|c|c}
\text{ladder} & n & \lambda_{\min} & \text{surplus/debt} & \text{top coefficient}\\
\hline
\text{interior} & 1 & 8.4368\cdot10^{-8} & 1.3172\cdot10^{-9} & 0.9999987\\
\text{boundary} & 1 & 3.6239\cdot10^{-11} & 1.4134\cdot10^{-13} & 0.9999999\\
\text{interior} & 3 & 5.4194\cdot10^{-20} & 3.2965\cdot10^{-24} & 0.9999761\\
\text{boundary} & 3 & 4.3037\cdot10^{-24} & 6.5483\cdot10^{-29} & 0.9999949\\
\text{interior} & 6 & 5.1363\cdot10^{-40} & 7.6161\cdot10^{-48} & 0.9999494\\
\text{boundary} & 6 & 8.5787\cdot10^{-45} & 3.1829\cdot10^{-53} & 0.9999839\\
\text{interior} & 9 & 2.0458\cdot10^{-61} & 7.3999\cdot10^{-73} & 0.9999306\\
\text{boundary} & 9 & 1.9271\cdot10^{-66} & 1.7443\cdot10^{-78} & 0.9999738
\end{array}
\]

The top coefficient being nearly \(1\) says the minimum-eigenvalue vector is
essentially monic. Its component decomposition gives the same
half-compensation law as the Schur residual:

\[
\text{endpoint debt}
\quad+\quad
\Gamma\text{ just above half}
\quad+\quad
\zeta\text{ just below half}
\quad=\quad
\text{tiny positive surplus}.
\]

So the Schur pivot induction is not missing a hidden worse direction. It is
tracking the same thin cone directions that the eigenvalue problem sees.

This adds a useful proof heuristic:

\[
\boxed{
\text{control the monic Schur residuals}
\quad\Longrightarrow\quad
\text{control the thinnest SOS directions.}
}
\]

The rigorous version should prove that the Gram minimum directions converge
to the monic residual directions in the completed ledger, or bypass that
comparison by proving positivity of every Schur pivot and using the
LDL/Gram-Schmidt factorization of \(H_n\) and \(K_n\).

### 35.32 Lower-support gate

The previous cone statement reveals a missing gate that should be named
explicitly. A measure on \([0,R]\) is not certified only by the interior cone
and the upper cone. It also needs the lower support cone:

\[
L(tf^2)>0.
\]

In matrix form this is

\[
J_n=(\mu_{a+b+1})_{0\le a,b\le n}\succ0.
\]

The probe

\[
\texttt{probe\_pass3\_t6\_lower\_support\_gate.py}
\]

checks the completed ledger:

\[
\begin{array}{c|c|c|c}
n & \lambda_{\min}(H_n) & \lambda_{\min}(J_n) & \lambda_{\min}(K_n)\\
\hline
0 & 2.3105\cdot10^{-2} & 3.7173\cdot10^{-5} & 7.8474\cdot10^{-5}\\
1 & 8.4368\cdot10^{-8} & 1.0385\cdot10^{-10} & 3.6239\cdot10^{-11}\\
2 & 1.1146\cdot10^{-13} & 8.0815\cdot10^{-17} & 1.4613\cdot10^{-17}\\
3 & 5.4194\cdot10^{-20} & 2.9621\cdot10^{-23} & 4.3037\cdot10^{-24}\\
4 & 1.6662\cdot10^{-26} & 8.5106\cdot10^{-30} & 1.0040\cdot10^{-30}\\
5 & 4.1269\cdot10^{-33} & 1.5728\cdot10^{-36} & 1.1701\cdot10^{-37}\\
6 & 5.1363\cdot10^{-40} & 1.3977\cdot10^{-43} & 8.5787\cdot10^{-45}\\
7 & 3.8072\cdot10^{-47} & 1.0504\cdot10^{-50} & 7.0824\cdot10^{-52}\\
8 & 3.1310\cdot10^{-54} & 8.5021\cdot10^{-58} & 4.5010\cdot10^{-59}\\
9 & 2.0458\cdot10^{-61} & 4.2879\cdot10^{-65} & 1.9271\cdot10^{-66}
\end{array}
\]

Thus the full cone theorem has three gates:

\[
\boxed{
H_n\succ0,
\qquad
J_n\succ0,
\qquad
K_n\succ0.
}
\]

The \(J_n\) gate is not a new mystery; it is the same Stieltjes positivity
shifted by one moment. But it must be carried in the final proof to avoid a
hidden support gap at the origin.

### 35.33 Lower-gate half-compensation

The lower gate also has its own half-compensation signature.  Let

\[
L_0(f):=L(tf)
\]

and let \(U_n\) be the monic residual obtained by orthogonalizing
\(t^n\) against \(1,t,\ldots,t^{n-1}\) under \(L_0\).  Its lower pivot is

\[
r_n=L_0(U_n^2)=L(tU_n^2).
\]

Decompose the completed explicit-formula ledger into endpoint,
Archimedean, and zeta pieces:

\[
r_n
=
E_n^{(0)}+A_n^{(0)}+Z_n^{(0)}.
\]

For the interior and upper gates the endpoint term is the large negative
debt.  For the lower shifted gate the orientation flips:

\[
E_n^{(0)}>0,
\qquad
A_n^{(0)}<0,
\qquad
Z_n^{(0)}<0.
\]

So the lower gate is not "analytic carriers pay endpoint debt." It is:

\[
\boxed{
\text{endpoint credit is almost exactly half-consumed by each analytic
carrier, with a positive remainder.}
}
\]

Put \(C_n=E_n^{(0)}>0\) and define the two midline defects

\[
\alpha_n^{(0)}
:=
\frac{-A_n^{(0)}}{C_n}-\frac12,
\qquad
\beta_n^{(0)}
:=
\frac12-\frac{-Z_n^{(0)}}{C_n}.
\]

Then

\[
\boxed{
\frac{r_n}{C_n}
=
\beta_n^{(0)}-\alpha_n^{(0)}.
}
\]

Thus the lower-gate analytic target is

\[
\boxed{
\beta_n^{(0)}>\alpha_n^{(0)}
\quad\Longrightarrow\quad
r_n>0.
}
\]

The probe

\[
\texttt{probe\_pass3\_t6\_lower\_gate\_half\_compensation.py}
\]

checks this flipped orientation:

\[
\begin{array}{c|c|c|c}
n & r_n/C_n & \alpha_n^{(0)} & \beta_n^{(0)}\\
\hline
0 & 2.3233\cdot10^{-6} & 9.0565\cdot10^{-4} & 9.0797\cdot10^{-4}\\
1 & 4.0489\cdot10^{-13} & 1.3547\cdot10^{-6} & 1.3547\cdot10^{-6}\\
2 & 1.9670\cdot10^{-20} & 2.2058\cdot10^{-9} & 2.2058\cdot10^{-9}\\
3 & 4.5030\cdot10^{-28} & 3.5851\cdot10^{-12} & 3.5851\cdot10^{-12}\\
4 & 8.0818\cdot10^{-36} & 5.8120\cdot10^{-15} & 5.8120\cdot10^{-15}\\
5 & 9.3302\cdot10^{-44} & 9.4104\cdot10^{-18} & 9.4104\cdot10^{-18}\\
6 & 5.1805\cdot10^{-52} & 1.5184\cdot10^{-20} & 1.5184\cdot10^{-20}
\end{array}
\]

The numbers are tiny because the lower gate is measuring a delicate
unconsumed endpoint credit.  Conceptually, this is valuable: the full
support proof has two orientations of the same quadratic gauge law.

\[
\boxed{
\begin{array}{c|c}
\text{interior/upper gates} & \text{analytic carriers overpay endpoint debt}\\
\text{lower gate} & \text{analytic carriers underconsume endpoint credit}
\end{array}
}
\]

### 35.34 LDL spine of the proof

The Schur-pivot induction is exactly the \(LDL^T\) factorization of the
Gram cone.

For the interior Hankel block,

\[
H_n=(\mu_{a+b})_{0\le a,b\le n},
\]

Gram-Schmidt on \(1,t,\ldots,t^n\) produces monic residuals

\[
P_0,P_1,\ldots,P_n
\]

with squared norms

\[
h_j=L(P_j^2).
\]

Let \(M_n\) be the lower triangular change-of-basis matrix from monomials
to monic residuals. Then

\[
\boxed{
M_n H_n M_n^T
=
\operatorname{diag}(h_0,h_1,\ldots,h_n).
}
\]

Equivalently,

\[
\boxed{
H_n
=
M_n^{-1}
\operatorname{diag}(h_0,\ldots,h_n)
(M_n^{-1})^T.
}
\]

Therefore

\[
\boxed{
H_n\succ0
\quad\Longleftrightarrow\quad
h_0,\ldots,h_n>0.
}
\]

The boundary-complement block has the identical factorization:

\[
\boxed{
K_n\succ0
\quad\Longleftrightarrow\quad
k_0,\ldots,k_n>0.
}
\]

The lower-support block

\[
J_n=(\mu_{a+b+1})_{0\le a,b\le n}
\]

also has its own monic residual ladder, say

\[
r_0,r_1,\ldots,r_n,
\]

obtained by applying the same Gram-Schmidt construction to the shifted
functional

\[
L_0(f):=L(tf).
\]

Thus

\[
\boxed{
J_n\succ0
\quad\Longleftrightarrow\quad
r_0,\ldots,r_n>0.
}
\]

Thus the full finite gate induction is:

\[
\boxed{
\begin{array}{rcl}
h_j>0\ (j<n) &\Longrightarrow& P_n\text{ exists},\\
\text{half-compensation for }P_n^2 &\Longrightarrow& h_n>0,\\
r_j>0\ (j<n) &\Longrightarrow& U_n\text{ exists},\\
\text{half-compensation for }tU_n^2 &\Longrightarrow& r_n>0,\\
k_j>0\ (j<n) &\Longrightarrow& Q_n\text{ exists},\\
\text{half-compensation for }(R-t)Q_n^2 &\Longrightarrow& k_n>0.
\end{array}
}
\]

This is the algebraic spine. The only analytic content still missing is the
half-compensation inequality itself:

\[
\boxed{
L(P_n^2)>0,
\qquad
L(tU_n^2)>0,
\qquad
L((R-t)Q_n^2)>0
\quad
\text{from the completed explicit-formula ledger.}
}
\]

Everything else in the finite cone proof is bookkeeping.

### 35.35 Three-gate reduction theorem

The current Pass-3 proof target can now be stated without hiding any gate.

Let the completed centered ledger define a linear functional \(L\) on
polynomials by

\[
L(t^m)=\mu_m.
\]

Fix

\[
R=\gamma_1^{-2}.
\]

For every \(n\), define three monic residuals:

\[
\begin{array}{rcl}
P_n&:&\text{residual under }L,\\
U_n&:&\text{residual under }L_0(f)=L(tf),\\
Q_n&:&\text{residual under }L_R(f)=L((R-t)f).
\end{array}
\]

Their squared residual gates are

\[
h_n=L(P_n^2),
\qquad
r_n=L(tU_n^2),
\qquad
k_n=L((R-t)Q_n^2).
\]

Now split \(L\) into endpoint, Archimedean, and zeta carriers:

\[
L=L_{\mathrm{end}}+L_\Gamma+L_\zeta.
\]

For \(P_n\) and \(Q_n\), the endpoint piece is negative.  Write

\[
S_n=-L_{\mathrm{end}}(P_n^2)>0,
\qquad
S_n^{(R)}=-L_{\mathrm{end}}((R-t)Q_n^2)>0.
\]

For \(U_n\), the shifted endpoint piece is positive:

\[
C_n=L_{\mathrm{end}}(tU_n^2)>0.
\]

The three analytic inequalities are:

\[
\boxed{
\frac{L_\Gamma(P_n^2)}{S_n}-\frac12
>
\frac12-\frac{L_\zeta(P_n^2)}{S_n}
}
\tag{H}
\]

\[
\boxed{
\frac12-\frac{-L_\zeta(tU_n^2)}{C_n}
>
\frac{-L_\Gamma(tU_n^2)}{C_n}-\frac12
}
\tag{J}
\]

\[
\boxed{
\frac{L_\Gamma((R-t)Q_n^2)}{S_n^{(R)}}-\frac12
>
\frac12-\frac{L_\zeta((R-t)Q_n^2)}{S_n^{(R)}}
}
\tag{K}
\]

Call these the **three-gate half-compensation inequalities**.

**Theorem 35.35 (Three-gate reduction).**  If (H), (J), and (K) hold for
every rung \(n\ge0\), then the completed centered ledger has a positive
Hausdorff/Stieltjes representation on \([0,R]\). Equivalently, the
trace-gauge Stieltjes model follows.

**Proof.**  Inequality (H) gives

\[
h_n=L(P_n^2)>0
\]

for every interior Schur residual.  By the \(LDL^T\) factorization,

\[
H_n=(\mu_{a+b})_{0\le a,b\le n}\succ0
\]

for every \(n\).

Inequality (J) gives

\[
r_n=L(tU_n^2)>0,
\]

hence

\[
J_n=(\mu_{a+b+1})_{0\le a,b\le n}\succ0
\]

for every \(n\).

Inequality (K) gives

\[
k_n=L((R-t)Q_n^2)>0,
\]

hence

\[
K_n=(R\mu_{a+b}-\mu_{a+b+1})_{0\le a,b\le n}\succ0
\]

for every \(n\).

Therefore

\[
L(f^2)>0,
\qquad
L(tf^2)>0,
\qquad
L((R-t)f^2)>0
\]

for every nonzero polynomial \(f\).  This is the bounded
Stieltjes/Hausdorff moment criterion on \([0,R]\).  Hence there is a
positive measure \(d\sigma\) supported on \([0,R]\) such that

\[
\mu_m=\int_0^R t^m\,d\sigma(t).
\]

Consequently the curvature derivative has the trace-gauge Stieltjes form

\[
F(x)=\int_0^R \frac{t}{1+xt}\,d\sigma(t)
\]

with positive compact support.  This is precisely the representation needed
by the Padé/trace-gauge convergence layer. \(\square\)

The consolidated audit

\[
\texttt{probe\_pass3\_t6\_three\_gate\_half\_compensation.py}
\]

checks the orientation of all three inequalities in one dashboard.  In each
gate,

\[
\boxed{
\text{winning defect}-\text{challenging defect}
=
\text{normalized pivot}.
}
\]

The first rows are:

\[
\begin{array}{c|c|c|c|c}
\text{gate} & n & \text{normalized pivot} &
\text{winning defect} & \text{challenging defect}\\
\hline
H & 0 & 5.7762\cdot10^{-3} & 3.7417\cdot10^{-2} & 3.1640\cdot10^{-2}\\
J & 0 & 2.3233\cdot10^{-6} & 9.0797\cdot10^{-4} & 9.0565\cdot10^{-4}\\
K & 0 & 4.8985\cdot10^{-6} & 9.5128\cdot10^{-4} & 9.4638\cdot10^{-4}\\
H & 1 & 1.3172\cdot10^{-9} & 3.3782\cdot10^{-5} & 3.3781\cdot10^{-5}\\
J & 1 & 4.0489\cdot10^{-13} & 1.3547\cdot10^{-6} & 1.3547\cdot10^{-6}\\
K & 1 & 1.4134\cdot10^{-13} & 1.3408\cdot10^{-6} & 1.3408\cdot10^{-6}
\end{array}
\]

Thus the remaining summit is no longer "prove positivity" as a vague
global demand.  It is the sharper analytic statement:

\[
\boxed{
\text{prove the three-gate half-compensation inequalities directly from the
completed explicit-formula ledger.}
}
\]

## 36. Side signal from the unit-distance proof: upstairs unit carriers

The supplied note

\[
\texttt{unit-distance-proof.pdf}
\]

does not give an RH lemma, but it gives a useful architecture.

Its geometric part has the following pattern:

1. Build a high-dimensional arithmetic carrier \(K=L(i)\).
2. Use split primes and a class-group pigeonhole to manufacture many
   elements

\[
u=\frac{\alpha}{c(\alpha)}
\]

with relative norm

\[
u\,c(u)=1.
\]

3. Under every complex embedding \(\sigma:K\to\mathbb C\), these elements
   satisfy

\[
|\sigma(u)|=1.
\]

4. Put the carrier in a Minkowski lattice, cut by an Archimedean window,
   count upstairs pairs, and project one complex coordinate. The
   projection observes the norm-one translations as planar unit
   distances.

The abstract lesson is:

\[
\boxed{
\text{manufacture unit objects upstairs;}
\quad
\text{control loss by a bounded carrier/window;}
\quad
\text{project to the observed geometry.}
}
\]

### 32.1 Why this helps Pass-3

Pass-3 has an analogous shape, though not the same theorem.

The old Gram-Bures-Poisson route tried to match an observed spectral
density directly:

\[
\frac{|\Sigma(y,\xi)|^2}{2\pi}
\stackrel{?}{=}
u_B(\xi,y).
\]

That failed because the upstairs positive Gram object and the observed
Bures field are not the same density.

The unit-distance proof warns us not to demand the observed object too
early. Instead:

\[
\boxed{
\text{build the right unit/trace carrier upstairs,}
\quad
\text{then project through the correct observer map.}
}
\]

For Pass-3, the upstairs object is no longer a raw prime Gram square. It
must be the continued centered carrier

\[
C_{12}
\;+\;
\sum_{r\ge3}\frac{P(rs)}{r}
\;+\;
\text{endpoint/Archimedean counter-ledger},
\]

and the observed object is the folded resolvent

\[
F(x)=\frac{B'(x)}{B(x)}
=
\langle\Omega,(I+xJ)^{-1}\Omega\rangle.
\]

The Pass-3 analogue of “norm-one upstairs” is:

\[
\boxed{
0\preceq J\preceq RI
\quad\text{with}\quad
\beta_i>0
\quad\text{and trace-gauge residues.}
}
\]

That is the unit object we need.

### 32.2 New construction heuristic

The native proof should therefore not try to prove positivity of the raw
prime-side field. It should try to construct a bounded positive Jacobi
carrier upstairs:

\[
\boxed{
\text{continued centered prime carrier}
\longrightarrow
\text{bounded Jacobi operator }J
\longrightarrow
\text{folded observed resolvent}.
}
\]

The unit-distance note suggests the right engineering questions:

1. **Abundance:** where do many candidate trace atoms or transfer
   couplings come from upstairs?
2. **Loss control:** what replaces class-number/window loss in the
   Pass-3 setting? Here it is tail control and Archimedean counterterm
   control.
3. **Projection fidelity:** what guarantees that the observed folded
   resolvent still sees the upstairs positivity? Here it is the
   GNS/Jacobi cyclic vector identity.

This is not a proof, but it sharpens the design rule:

\[
\boxed{
\text{do not project raw primes;}
\quad
\text{project a completed unit carrier.}
}
\]

That sentence is compatible with every failure we have seen so far.

## 37. Interlude: what the empirical \(r=3\) is saying

The grep signal is now too coherent to treat as decoration. Across the
program, the number \(3\) keeps appearing at the same kind of boundary:
the first layer where a two-layer bookkeeping problem closes into an
interaction.

This is not numerology. It is a threshold pattern.

First, in the native simplicial chart, the \(N=4\) ledger has a
three-dimensional zero-sum content space:

\[
H_0=\left\{x\in\mathbb R^4:\sum_i x_i=0\right\},
\qquad
\dim H_0=3.
\]

Only in dimension three does the wedge-Hodge package return a binary
cross product whose output is again a vector in the same space. Equivalently,
\(\dim\mathfrak{so}(3)=3\), so a single vector axis can parameterize every
infinitesimal rotation. Below dimension three the package has not yet closed;
above dimension three a rotation is naturally blade-like rather than a single
axis vector. Thus the \(N=4\to 3\) event says:

\[
\boxed{
\text{three is the first dimension where oriented area can be read as an axis.}
}
\]

Second, in the cumulant tower, order \(1\) gives position, order \(2\) gives
the Fisher metric or inertia, and order \(3\) gives the Amari-Chentsov cubic.
The cubic is the first invariant not visible to Riemannian geometry alone:

\[
\boxed{
\text{three is the first order where information geometry exceeds metric geometry.}
}
\]

Third, in the conductor reading, the character basis is diagonal at order
\(2\). Arithmetic first speaks at order \(3\), through the modular selection
rule

\[
a+b+c\equiv 0\pmod N.
\]

That is the first cumulant layer where labels must satisfy a conservation
law. Pairing sees orthogonality; tripling sees ring structure.

Pass-3 adds the prime-occupation version of the same threshold. At the
critical center \(s=\tfrac12\), occupation layer \(r\) carries prime weight

\[
p^{-r/2}.
\]

The convergence threshold is

\[
\frac r2>1.
\]

Therefore \(r=1\) and \(r=2\) are the two raw critical layers that require
continuation, while \(r=3\) is the first ordinary layer that can be carried
directly:

\[
\boxed{
r=1,2:\ \text{continue the critical pair;}
\qquad
r\ge3:\ \text{carry the ordinary tail.}
}
\]

The first carried tail is also the slowest decaying carried tail. This is why
the \(r=3\) prime tail dominates the tail-control problem after the two-layer
continuation has been isolated.

This gives a compact working dictionary:

\[
\begin{array}{c|l}
1 & \text{amount, position, first observation}\\
2 & \text{contrast, metric, pairing, critical raw boundary}\\
3 & \text{interaction, axis, cubic vertex, selection rule, first honest tail}\\
4 & \text{ledger, closure carrier, residual bookkeeping}
\end{array}
\]

The "why three-dimensional space" line in the surrounding program is the
physical reading of the same algebraic threshold: a \(Q=4\) or \(N=4\) ledger
has three observed contrast dimensions, and only in dimension three does the
single-axis inertial projector close under the wedge-Hodge/rotation package.
That should be stated as a selection principle internal to the model:

\[
\boxed{
\text{three is not merely a count;}
\quad
\text{it is the first self-closing contrast dimension.}
}
\]

For the RH pass, the operational message is sharper:

\[
\boxed{
\text{do not fight the whole Euler tower;}
\quad
\text{continue the first two layers and control the third.}
}
\]

## 38. Final Pass-3 slogan

\[
\boxed{
\text{No more broad positivity.}
\quad
\text{No more heat drift.}
\quad
\text{No more arbitrary quadrature.}
}
\]

\[
\boxed{
\text{Trace-gauge Stieltjes}
\quad\Longleftrightarrow\quad
\text{positive determinant}
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\]

That is the clean kitchen.
