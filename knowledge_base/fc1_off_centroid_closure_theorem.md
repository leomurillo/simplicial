# FC1-C Off-Centroid Finite-Jet Closure Theorem

Created: 2026-05-15

This note closes the off-centroid proof obligation in FC1 at the finite-jet
level.  It proves that the first failure of the natural macrovariable algebra
is exactly a quotient-character adjacency carry term, with the filtered source
given by the FC2 section class \([\kappa]\).  It does not enumerate every
Hamiltonian tuple orbit; that is the finite Noether atlas census built from
the seed table.

## Setup

Let \(R\) be a finite quotient ring, or a finite abelian output algebra with a
chosen normalizer packet action.  Let

```text
M = Delta_R^o,       p_* = |R|^{-1} 1,
H_R = {h in C^R : sum h = 0}.
```

Fix a packet set \(S\) in the nontrivial additive-character tangent space and
write

```text
H_S = direct sum_{d in S} H_R^[d],
Pi_S = sum_{d in S} Pi_d.
```

Along an \(m\)-flat ray

```text
p(t)=p_*+t h
```

Paper 10 gives the normalized Fisher coefficient

```text
g_{p_*+th}(e_chi,e_psi)
  = sum_{n >= 0} (-t)^n hhat^{*n}(psi chi^{-1}).
```

Paper 11 packages its \((\mathfrak f,\mathfrak e)\)-block as

```text
C_n^[f,e](h)
  = sum_eta hhat^{*n}(eta) A_eta^[f,e],
```

where

```text
A_eta^[f,e] = Pi_f M_eta Pi_e.
```

For simplectic Hamiltonian data

```text
C = (C_1,...,C_{Q-2})
```

whose differentials are finite-sufficient through the observation atlas
\(\Phi_{R,k}\), write the Nambu-Fisher current and vector field as

```text
P_C = dC_1 wedge ... wedge dC_{Q-2},
i_{X_C} Omega_R^F = P_C.
```

Let

```text
X_C(p_*+th) = sum_b t^b X_C^(b)(h).
```

Define the order-\(m\) closure-defect operator

```text
D_m^S(h,C)
  = Pi_{S^c} sum_{a+b=m} (-1)^a C_a(h) X_C^(b)(h),
```

where \(C_a(h)\) is the full block operator with corners
\(C_a^{[\mathfrak f,\mathfrak e]}(h)\).

## Theorem

**FC1-C. Off-centroid finite-jet closure and first carry obstruction.**

At a fixed finite adjacency/Fisher-jet order \(k\):

1. The finite-sufficient natural current remains in the declared packet
   algebra through order \(k\) if and only if
   \[
   D_m^S(h,\mathbf C)=0
   \qquad(0\le m\le k).
   \]
2. Assume the centroid current is already in the declared packet algebra,
   \(D_0^S=0\).  If off-centroid closure first fails at a positive order
   \(m_0\), then \(D_{m_0}^S\) is a nonzero finite polynomial in
   quotient-character adjacency generators \(A_\eta^{\mathfrak f,\mathfrak e}\),
   and at least one surviving term contains a quotient shift crossing the
   declared packet boundary.  Thus the first off-centroid obstruction is
   quotient-character adjacency carry, not a new smooth Hamiltonian term.
3. For a conductor-respecting NZSBTL with PSL data, the only cross-packet
   failures are the PSL boundary terms
   \[
   \sum_\eta \widehat{h^n}(\eta)A_\eta^{\mathfrak d',\mathfrak d},
   \]
   i.e. the translation-stretching carry operators of Paper 10/Paper 11.
   Within-packet terms may refine flags or rescale internal coordinates, but
   they do not create a cross-packet macrovariable.
4. In local filtered rows, the section-dependent representative of the carry
   changes by a coboundary, and the section-independent filtered source is the
   FC2 class \([\kappa]\).  The \(K^{CH}\) row, H4 support, contraction
   shadows, and higher Fisher jets are visible Fisher-shadow projections of
   \([\kappa]\) modulo the relevant Fisher-jet kernels.
5. If a finite normalizer group \(G\le N(\mathcal A_R)\) preserves the packet
   set \(S\), then
   \[
   D_m^S(g\cdot h,g\cdot\mathbf C)
   =
   \lambda_g\,g\cdot D_m^S(h,\mathbf C),
   \]
   so the first failure order and the filtered residual label are constant on
   \(G\)-orbits of displacement/Hamiltonian tuple data.

## Proof

For claim 1, the Fisher-dual response of the Nambu vector field is obtained by
applying the Fisher metric expansion to the vector-field jet:

```text
Theta_C(p_*+th)
  = sum_m t^m sum_{a+b=m} (-1)^a C_a(h) X_C^(b)(h).
```

Projecting to \(S^c\) gives exactly \(D_m^S(h,\mathbf C)\).  Therefore the
response has no component outside \(H_S^*\) through order \(k\) exactly when
all displayed projections vanish for \(m\le k\).  This is Paper 13 Theorem
10.4 rewritten in the FC1 notation.

For claim 2, the hypothesis \(D_0^S=0\) removes the degenerate case where the
Hamiltonian tuple was outside the declared packet algebra already at the
centroid.  For \(a>0\), each \(C_a(h)\) is, by Paper 11, a finite sum of
\(\widehat h^{*a}(\eta)A_\eta^{\mathfrak f,\mathfrak e}\).  Hence every
coefficient of \(D_m^S\) is a finite polynomial in the quotient-shift
generators and the finite-sufficient Hamiltonian jet coefficients.  If
\(m_0>0\) is the first order with \(D_{m_0}^S\ne0\), its projection by
\(\Pi_{S^c}\) has a surviving term whose target lies outside \(S\).  Such a
term must contain a quotient-shift path that crosses from a declared source
packet to an undeclared target packet.  This is precisely quotient-character
adjacency carry.  If all such projected shift paths cancel, \(D_m^S=0\) and
closure has not failed at that order; the first failure is the first
noncancelled carry polynomial.

Claim 3 is Paper 10 Theorem 12.8 in this notation.  A conductor-respecting
NZSBTL keeps within-packet steps inside one packet.  The off-centroid
coefficient inside a packet is still one of the \(A_\eta^{\mathfrak d,\mathfrak d}\)
terms, so it is internal to the packet algebra.  The only way to leave the
packet algebra is to cross a conductor/PSL boundary
\(\mathfrak d\to\mathfrak d'\), and the coefficient at order \(n\) is exactly
the displayed quotient-character carry sum.

For claim 4, use FC2.  In a local filtered row, choose a section

```text
s : gr A_R -> A_R.
```

The filtered multiplication defect is

```text
kappa_s(x,y)=s(x)s(y)-s(xy).
```

Associativity makes \(\kappa_s\) a 2-cocycle, and changing \(s\) changes it by
a coboundary.  Thus the section-independent obstruction is \([\kappa]\).  The
Fisher-jet functor sends quotient-shift products to \(K^{CH}\), H4, and
higher Fisher-shadow supports; any invisible part is exactly kernel data of
that projection.  Therefore a support-erased or \(K^{CH}\)-invisible residual
is not zero filtered carry.  It is only invisible to that chosen projection.

For claim 5, if \(G\) normalizes \(\mathcal A_R\), then

```text
g C_a(h) g^{-1} = C_a(g h).
```

If \(G\) preserves \(S\), then \(g\Pi_Sg^{-1}=\Pi_S\) and likewise for
\(\Pi_{S^c}\).  The Nambu current transforms by the determinant character of
the Hamiltonian tuple, while the Fisher volume transforms by the volume
character; their ratio is the nonzero scalar \(\lambda_g\).  Substituting into
the formula for \(D_m^S\) proves the equivariance identity.  Nonzero
closure-defect, first failure order, and the residual filtered class are
therefore orbit invariants.  \(\square\)

## Finite Noether Atlas Consequence

Fix:

1. the finite observation map \(\Phi_{R,k}\);
2. a polynomial jet order \(r\);
3. a finite support skeleton or finite coefficient alphabet for Hamiltonian
   tuples in \((J^r\mathcal N_{R,k})^{Q-2}\).

Then the candidate tuple set is finite, the normalizer \(G\) is finite, and
the Noether data are finite linear algebra:

1. tuple orbits;
2. stabilizers;
3. determinant characters;
4. closure defects \(D_m^S\) through order \(k\);
5. filtered residual labels from \([\kappa]\) and its visible Fisher shadows.

The current seed table is generated by:

- `empirical/fc1_noether_atlas_seed.py`
- `empirical/reports/fc1_noether_atlas_seed.md`
- `empirical/reports/fc1_noether_atlas_seed.json`

The seed table proves the finite coordinate skeleton for the current rows.  It
does not claim to have enumerated all Hamiltonian tuple orbits.  The theorem
above proves that once a tuple orbit is chosen, every off-centroid failure
recorded by the census is a quotient-character carry term, and every local
filtered source is an FC2 \([\kappa]\)-label.

## FC1 Status After This Note

FC1 is theorem-facing at the stated finite-jet scope:

1. FC1-A proves the centroid quadratic macrovariable classification.
2. FC1-B1 proves exact finite-sufficient decomposable currents live in the
   finite differential module.
3. FC1-C proves off-centroid finite-jet closure fails first by
   quotient-character adjacency carry, with filtered source \([\kappa]\).

What remains is not a new naturality axiom.  It is the finite atlas census:
choose the row/order/skeleton, enumerate tuple orbits and stabilizers, compute
determinant characters, and attach the \(D_m^S\) and \([\kappa]\) labels.
