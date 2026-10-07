# FC1-A Centroid Invariant Classification Theorem

Created: 2026-05-15

This note closes the first proof obligation in FC1.  It proves the centroid
classification of natural quadratic macrovariable jets.  The result is
finite-dimensional representation theory, not empirical evidence.

## Setup

Let \(A\) be a finite abelian outcome group.  For quotient-ring applications,
take \(A=(R,+)\).  Put \(Q=|A|\).  Let

```text
H_A = {h in C^A : sum_a h_a = 0}.
```

At the categorical centroid \(p_*=|A|^{-1}{\bf 1}\), the additive translation
representation of \(A\) on \(H_A\) decomposes as

```text
H_A = direct sum_{chi in hat A, chi != 1} C e_chi,
```

where \(e_\chi=|A|^{-1/2}\chi\) is the normalized character vector.  The
centroid Fisher form is a scalar multiple of the standard Hermitian form in
this basis.

Let \(\Gamma\le \operatorname{Aut}(\widehat A)\) be a finite normalizer group
acting by permutation of nontrivial character lines.  In the quotient-ring
case, \(\Gamma\) is the CRT/Hayes/Galois normalizer used in Paper 11.  Let

```text
P = {O}
```

be the packet partition of \(\widehat A\setminus\{1\}\) into \(\Gamma\)-orbits,
or into coarser primitive conductor packets when the Hayes/Galois normalizer is
known to act transitively on each primitive conductor packet.  Write
\(\Pi_O\) for the centroid Fisher-orthogonal projector onto the span of packet
\(O\), and define

```text
E_O(h) = 1/2 ||Pi_O h||^2_{F,*}.
```

A **quadratic centroid macrovariable jet** is a real quadratic function

```text
Q_B(h) = 1/2 <h, B h>_{F,*}
```

for a Fisher-self-adjoint operator \(B:H_A\to H_A\).

This is the Hermitian complexified convention used by the Fisher character
atlas.  On the real tangent space, complex-conjugate character lines are tied
by \(z_{\chi^{-1}}=\overline{z_\chi}\); the corresponding real invariant
quadratic term is still the packet energy \(|z_\chi|^2\), and
\(\chi\) and \(\chi^{-1}\) have the same conductor.  Thus the real-form
statement has the same packet-energy conclusion.

## Theorem

**FC1-A. Centroid invariant classification.**  Let \(Q_B\) be a quadratic
centroid macrovariable jet.

1. If \(Q_B\) is invariant under additive translations of \(A\), then
   \(B\) is diagonal in the additive-character basis.  Equivalently,
   \(Q_B\) has no cross-character terms.
2. If \(Q_B\) is also invariant under \(\Gamma\), then the diagonal weights
   are constant on \(\Gamma\)-orbits.  Hence
   \[
   Q_B(h)=\sum_{O\in P}\lambda_O E_O(h)
   \]
   for real constants \(\lambda_O\).  In the quotient-ring packet convention,
   this is a function of primitive conductor packet energies.
3. If \(Q_B\) is required to be relative finite-sufficient for a quotient
   layer \(\pi_{\mathfrak d}:R\to R/\mathfrak d\), then only packets with
   conductor dividing \(\mathfrak d\) may appear.  Primitive packet energies
   are the new quadratic jets added when passing from proper quotient layers
   to layer \(\mathfrak d\).

Consequently, at the centroid, every additive-translation invariant,
normalizer-equivariant, relative finite-sufficient quadratic macrovariable is
a linear combination of packet energies, with only packetwise orthogonal flag
freedom remaining inside packets.  A genuine cross-packet quadratic term cannot
be natural under these hypotheses.

## Proof

Let the additive translation action be denoted \(\tau_a\).  In the normalized
character basis,

```text
tau_a e_chi = chi(a) e_chi.
```

Write the matrix entries of \(B\) in this basis as

```text
B_{psi,chi} = <e_psi, B e_chi>_{F,*}.
```

Additive translation invariance of \(Q_B\) is equivalent to
\(\tau_a^*B\tau_a=B\) for every \(a\in A\).  Therefore

```text
B_{psi,chi}
  = <tau_a e_psi, B tau_a e_chi>
  = conj(psi(a)) chi(a) B_{psi,chi}
```

for all \(a\).  If \(\psi\ne\chi\), then \(\chi\psi^{-1}\) is a nontrivial
character, so there is some \(a\in A\) with
\(\chi(a)\psi(a)^{-1}\ne1\).  The displayed identity forces
\(B_{\psi,\chi}=0\).  Thus \(B\) is diagonal:

```text
B e_chi = b_chi e_chi.
```

Because \(B\) is Fisher-self-adjoint and \(Q_B\) is real, the weights
\(b_\chi\) are real.

Now impose \(\Gamma\)-invariance.  For \(\gamma\in\Gamma\), the action
permutes character lines:

```text
gamma e_chi = u_{gamma,chi} e_{gamma chi}
```

for unit phases \(u_{\gamma,\chi}\).  Since \(B\) is diagonal, the phases
cancel in \(\gamma^*B\gamma=B\), giving

```text
b_{gamma chi} = b_chi.
```

Thus the weight is constant on every \(\Gamma\)-orbit.  Grouping by packets,

```text
Q_B(h) = 1/2 sum_O b_O ||Pi_O h||^2_{F,*}
       = sum_O b_O E_O(h).
```

This proves the first two claims.

For the finite-sufficiency clause, recall Paper 10 Proposition 3.4: functions
factoring through \(\pi_{\mathfrak d}:R\to R/\mathfrak d\) are exactly the
span of characters whose conductor divides \(\mathfrak d\).  Therefore the
tangent space of the corresponding quotient categorical subfamily is

```text
L_{<= d} = direct sum_{e | d, e != 1} H_R^[e].
```

A quadratic jet that is relative sufficient for this quotient layer must
factor through \(L_{\le\mathfrak d}\); equivalently, its operator \(B\) must
vanish on packet projectors outside that cumulative subspace.  By the first
two parts, the surviving invariant terms are exactly the energies of packets
inside \(L_{\le\mathfrak d}\).  Passing from all proper quotient layers below
\(\mathfrak d\) to the layer \(\mathfrak d\) adds precisely the primitive
packet \(H_R^{[\mathfrak d]}\), hence the primitive energy
\(E_{\mathfrak d}\) is the new quadratic macrovariable jet.  This proves the
finite-sufficiency claim.  \(\square\)

## Consequences For FC1

1. **No arbitrary cross-packet Hamiltonians at first jet.**  Any quadratic
   cross-packet term is killed before mechanics enters: translation invariance
   already forbids it.
2. **Conductor energies are forced by symmetry.**  Hayes/Galois/CRT
   equivariance collapses character-line energies to packet energies.  The
   conductor packet convention is not a modeling preference once this
   normalizer is chosen.
3. **Finite sufficiency fixes which packets are allowed.**  Quotient
   sufficient-statistic layers are cumulative conductor spaces.  Primitive
   packet energies are the increments in that filtration.
4. **Within-packet freedom is real but bounded.**  A choice of Fisher
   orthogonal flag inside a packet is not a new cross-packet macrovariable; it
   is the NZSBTL internal freedom already allowed by Paper 10.
5. **The next proof frontier moves off the centroid.**  FC1-B and FC1-C no
   longer need to justify packet energies at quadratic order.  They need to
   show that exact decomposable currents generated from these jets remain
   natural under Noether equivariance, and that their first off-centroid
   failure is exactly Paper 11 adjacency carry.

## First-Current Corollary

The theorem also gives the first nonzero current jet for simplectic Hamiltonian
tuples.

Let

```text
C_i(h) = Q_{B_i}(h) + O(||h||^3)
```

be \(Q-2\) macro-Hamiltonians whose first nonconstant jets satisfy FC1-A.
Then

```text
B_i = sum_O lambda_{i,O} Pi_O
```

and

```text
dC_i(h)[v] = <B_i h, v>_{F,*} + O(||h||^2).
```

Therefore the first nonzero decomposable Nambu current jet is

```text
P_C^{lead}(h)
  = wedge_i <B_i h, d(-)>_{F,*}
```

and belongs to the exterior algebra generated by packet-energy covectors.  In
particular, no leading current term can contain a cross-packet quadratic
Hamiltonian component.

If a normalizer element \(\gamma\in\Gamma\) sends the Hamiltonian tuple to

```text
gamma^* C_i = sum_j A_{ij}(gamma) C_j + O(||h||^3)
```

then

```text
gamma^* P_C^{lead} = det(A(gamma)) P_C^{lead}.
```

Thus Paper 13's adjacency-Noether determinant character is already forced at
the first nonzero jet by the packet-energy classification.

**Proof.**  Differentiating the classified quadratic jet gives
\(dQ_{B_i}(h)[v]=\langle B_i h,v\rangle_{F,*}\), and the expression for
\(B_i\) follows from FC1-A.  Wedge the \(Q-2\) leading covectors.  A linear
change of the Hamiltonian tuple multiplies the wedge by the determinant of
the change-of-basis matrix.  \(\square\)

## Sharp Scope

This theorem classifies quadratic centroid jets.  It does not classify:

1. higher-degree invariant polynomials inside a packet;
2. arbitrary smooth functions of the packet energies;
3. all closed Fisher-current residuals;
4. nonuniform Fisher-orthogonal moving frames;
5. nonabelian or non-quotient output spaces without a specified packet action.

Those are later FC1/FC6 problems.  The closed result here is the first
nontrivial jet, which is the layer where "did we choose these Hamiltonians?"
was most exposed.
