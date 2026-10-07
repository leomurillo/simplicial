# 51. The Residual Conductor Pullback Theorem

**Jacobian Transport of Packet Geometry Through Transformer Residual Streams**

**Leonardo Murillo Montero**  
*May 22, 2026*

**arXiv-style preprint (draft v0.0 - analysis core: residual/parameter quotient, exact pullback theorem, approximate transformer stability theorem; empirical protocol deferred)**

---

## Abstract

The conductor trilogy and its AI-facing descendants establish a sharp output-side fact. For a cyclic categorical label algebra `C_N`, the centered tangent space decomposes orthogonally into conductor packets
`H_R = direct_sum_{d | N, d > 1} H_d`. At the maximum-entropy point, the Fisher quadratic form is scalar on this character basis, while the Amari-Chentsov cubic tensor has the modular selection rule `a + b + c = 0 mod N`, and therefore contains cross-packet content invisible to purely quadratic curvature objects. Paper 26 proves the quotient-readout consequence: a readout factoring through `C_N -> C_k` retains exactly the packets `H_d` with `d | k` and annihilates exactly the packets with `d not| k`. Paper 36 measures where those packets appear in transformer residual streams. Paper 45 uses a qualifying layer to certify sparse-autoencoder decoder spans against packet supports.

The missing bridge is functorial: when does the output-side packet decomposition pull back through a residual or parameter Jacobian to become an honest packet decomposition upstairs? This paper supplies the analysis. Let `J_l : V_l -> H_R` be the local task readout Jacobian from a residual or parameter tangent space into the centered cyclic output tangent. The invisible directions `ker J_l` are gauge. The observable object is the quotient `V_l / ker J_l`, equivalently the visible output subspace `W_l = im J_l`.

The main exact theorem is finite linear algebra. The residual quotient admits an honest conductor-packet lift if and only if `W_l` is invariant under the output packet projectors `P_d`, equivalently if the Fisher-orthogonal projector `Pi_l` onto `W_l` commutes with every `P_d`. In that case the quotient decomposes as `direct_sum_d V_{l,d}`, the pulled-back Fisher form is conductor-block diagonal, quotient readouts obey the same divisor survival rule as Paper 26, and the pulled-back cubic tensor obeys the same character-level modular selection rule as Paper 34.

Real transformers need not satisfy exact invariance. The approximate theorem defines the layer leakage
`epsilon_l = max_d ||[Pi_l, P_d]||_op`. The soft pulled-back packet operators
`Q_{l,d} = Pi_l P_d Pi_l |_{W_l}` always form a positive partition of unity on the visible subspace. When `epsilon_l` is small, each `Q_{l,d}` is close to an orthogonal projector and different packets are almost orthogonal:
`||Q_{l,d}^2 - Q_{l,d}|| <= epsilon_l`,
`||Q_{l,d} Q_{l,e}|| <= epsilon_l` for `d != e`.
Transporting the result from the visible output subspace back to raw residual coordinates costs the nonzero singular-value condition number of `J_l`. Thus Paper 36's packet spectrum becomes the diagonal of a soft conductor measurement, and Paper 45's certification target becomes the approximate eigenspaces of these soft packet operators.

The paper does not claim that arbitrary natural-language behavior is conductor-packet decomposable, nor that real transformer layers satisfy the exact theorem. It gives the precise condition under which the slogan "conductor packets pull back through residual subspaces" is true, and the quantitative defect to measure when it is only approximately true.

**Keywords:** conductor packets, residual stream, transformer interpretability, Jacobian pullback, parameter Fisher, quotient readout, logit lens, Amari-Chentsov tensor, sparse autoencoders, mechanistic interpretability.

---

## 1. Introduction

### 1.1 The gap

The program has three output-side facts that are already sharp.

First, the trilogy gives the native categorical geometry. The centered tangent space `H_R` of a cyclic categorical algebra `R = C_N` is the zero-sum hyperplane, the Fisher metric at the uniform is scalar in the character basis, and the conductor packets `H_d` give the canonical finite arithmetic decomposition.

Second, Paper 34 proves the conductor blind spot. At `p_*`, quadratic curvature objects are conductor-block diagonal, while the Amari-Chentsov cubic tensor sees cross-packet interactions through the exact character selection rule

```text
a + b + c = 0 mod N.
```

Third, Paper 26 proves the quotient-readout theorem. A readout whose codomain is a quotient `C_k` cannot recover packets whose conductors do not divide `k`. After lifting back to `C_N`, the forbidden packets are annihilated exactly.

What has not been stated as a theorem is the residual/parameter-side lift:

```text
When do these output packets pull back through a network Jacobian
to become meaningful packet subspaces inside the residual stream,
inside a probe feature space, or inside parameter space?
```

This is not automatic. A linear map can send a residual subspace into the output tangent in a way that cuts across the conductor packets. In that case packet fractions are still measurable after the readout, but there is no honest packet decomposition upstairs. The missing theorem is the condition that separates those two cases.

### 1.2 The answer

Let `J_l : V_l -> H_R` be the local readout Jacobian at layer `l`. Here `V_l` may be:

- the residual stream at a fixed token position;
- a probe feature space;
- an SAE decoder span;
- a parameter tangent space;
- any other finite-dimensional tangent space whose local task effect is measured by a map into the cyclic output tangent.

The kernel

```text
K_l = ker J_l
```

is gauge. Directions in `K_l` are invisible to the chosen cyclic task. They may matter for other behavior, but they do not have a conductor label for this task.

The observable quotient is

```text
Vbar_l = V_l / K_l.
```

Equivalently, one may work with the visible output subspace

```text
W_l = im J_l subset H_R.
```

The theorem says:

> Conductors pull back as honest residual packets exactly when `W_l` is closed under the output conductor projectors.

Everything else is a stability version of that sentence.

### 1.3 What this paper does not claim

This paper does not claim that the exact pullback condition holds in trained transformers. It defines the condition.

It does not claim that natural-language representation space has a universal conductor basis. The conductor basis is attached to a named finite cyclic task algebra, such as months, weekdays, digits, modular arithmetic, or another explicitly indexed categorical subtask.

It does not claim that Paper 36's packet fractions alone prove residual packet subspaces exist. Paper 36 measures packet energy after a readout. The present theorem says what additional commutator/invariance diagnostic is needed to promote that measurement to a residual-subspace statement.

It does not revise Paper 34's firewall. Paper 34's exact theorem remains output-side and maximum-entropy-local. The present theorem is a conditional transport theorem: if a Jacobian has the required invariance, the output-side result pulls back; if not, the failure is measured by an explicit leakage operator.

---

## 2. Output-side conductor geometry

### 2.1 Cyclic tangent space

Fix `N >= 2` and let

```text
R = C_N = Z/NZ.
```

Let `H_R` be the centered real tangent space of functions on `R`:

```text
H_R = {f : R -> R_real : sum_x f(x) = 0}.
```

We use the normalized inner product

```text
<f,g> = N^{-1} sum_x f(x) g(x)
```

or its complexification when using characters. At the maximum-entropy distribution `p_*`, this is the Fisher metric up to the fixed scalar convention used in the earlier papers. Scalars do not affect packet orthogonality.

### 2.2 Character packets

The additive characters are

```text
chi_a(x) = exp(2 pi i a x / N),     a = 0, ..., N-1.
```

The trivial character `chi_0` spans the constant subspace and is excluded from `H_R`. For `a != 0`, define the conductor

```text
cond(chi_a) = N / gcd(a,N).
```

For every divisor `d | N`, `d > 1`, the conductor packet is

```text
H_d = span{chi_a : cond(chi_a) = d}.
```

Thus

```text
H_R = direct_sum_{d | N, d > 1} H_d.
```

Let

```text
P_d : H_R -> H_d
```

be the orthogonal projector. The projectors satisfy

```text
P_d^2 = P_d,
P_d P_e = 0 for d != e,
sum_d P_d = I_H.
```

### 2.3 Output-side tensors

At `p_*`, the Fisher quadratic form is scalar:

```text
g_*(u,v) = c_N <u,v>.
```

Therefore it is block-diagonal across every orthogonal packet decomposition.

The Amari-Chentsov cubic tensor has the character-level selection rule:

```text
T_*(chi_a, chi_b, chi_c) != 0
iff
a + b + c = 0 mod N,
```

with all three characters nontrivial. This rule is the origin of the conductor blind spot: the quadratic form carries no cross-packet coupling, but the cubic tensor often does.

---

## 3. Ingredient 1: the upstairs object

### 3.1 The local readout Jacobian

Fix a layer, probe, SAE span, or parameter point. Let `V` be the finite-dimensional real vector space of local perturbations. Let

```text
J : V -> H_R
```

be the local task readout Jacobian.

Examples:

- **Frozen unembedding lens.** `V` is the residual stream at layer `l`; `J` is the restriction of the model unembedding to the cyclic sub-vocabulary, followed by centering.
- **Tuned or trained probe.** `V` is the hidden activation space; `J` is the fitted affine readout's linear part, followed by centering and possibly quotient lift.
- **Parameter tangent.** `V` is the parameter tangent space at `w`; `J = D_w ell_w` is the centered logit Jacobian.
- **Behavior map.** `V` is a learned activation manifold; `J = D F` for a local activation-to-behavior map `F`.

The analysis below does not care which source produced `J`.

### 3.2 Gauge and visible quotient

The invisible subspace is

```text
K = ker J.
```

For this task, directions in `K` have no output-side tangent effect. They cannot be assigned conductor packet labels by this readout. They are gauge.

The observable residual/parameter space is the quotient

```text
Vbar = V / K.
```

The map `J` descends to an injective map

```text
Jbar : Vbar -> H_R.
```

Its image is the visible output subspace

```text
W = im J subset H_R.
```

The quotient `Vbar` and the subspace `W` are equivalent descriptions of the same observable object. The cleanest theorem lives on `W`; the residual-coordinate version is obtained by transporting back through `Jbar`.

### 3.3 Pulled-back Fisher form

The output Fisher form pulls back to `V` by

```text
B(v,w) = g_*(Jv, Jw).
```

This is positive semidefinite on `V` and positive definite on `Vbar`.

Packetwise pieces are always defined:

```text
B_d(v,w) = g_*(P_d Jv, P_d Jw).
```

Because the `P_d` are orthogonal and sum to the identity,

```text
B = sum_d B_d.
```

This identity always holds. It is not yet a residual packet decomposition. It is only a decomposition of the readout energy after applying `J`.

### 3.4 Soft pulled-back packet operators

Let

```text
Pi_W : H_R -> W
```

be the Fisher-orthogonal projector onto the visible subspace.

Define the soft packet operator on `W` by

```text
Q_d = Pi_W P_d Pi_W | W.
```

Since the input is already in `W`, this is equivalently `Q_d = Pi_W P_d | W`.

The operators `Q_d` satisfy:

```text
Q_d = Q_d^*,
Q_d >= 0,
sum_d Q_d = I_W.
```

Thus `d -> Q_d` is always a positive operator-valued conductor measurement on the visible subspace.

This is the first key distinction:

```text
Soft packet measurement: always exists.
Honest packet subspaces: exist only under an invariance condition.
```

---

## 4. Ingredient 2: the exact pullback theorem

### 4.1 Conductor-closed visible subspaces

**Definition 4.1 (Conductor-closed visible subspace).**  
A visible subspace `W subset H_R` is conductor-closed if

```text
P_d W subset W
```

for every nontrivial conductor `d | N`.

Equivalently, every vector in `W` can be decomposed into output conductor packets without leaving `W`.

### 4.2 Exact theorem

**Theorem 4.2 (Residual Conductor Pullback Theorem, exact form).**  
Let `H_R = direct_sum_d H_d` be the conductor packet decomposition with orthogonal projectors `P_d`. Let `J : V -> H_R` be a finite-dimensional linear map, let `K = ker J`, let `Vbar = V/K`, let `W = im J`, and let `Pi_W` be the orthogonal projector onto `W`. The following are equivalent:

1. `W` is conductor-closed: `P_d W subset W` for every `d`.
2. `Pi_W` commutes with every packet projector:

   ```text
   [Pi_W, P_d] = 0 for every d.
   ```

3. The soft packet operators are honest orthogonal projectors:

   ```text
   Q_d^2 = Q_d,
   Q_d Q_e = 0 for d != e,
   sum_d Q_d = I_W.
   ```

4. The visible subspace decomposes orthogonally as

   ```text
   W = direct_sum_d W_d,
   W_d = W cap H_d.
   ```

5. The observable quotient decomposes as

   ```text
   Vbar = direct_sum_d Vbar_d,
   Vbar_d = Jbar^{-1}(W cap H_d).
   ```

When these equivalent conditions hold, the pulled-back Fisher form is conductor-block diagonal on `Vbar`, quotient readouts obey the same divisor survival law as Paper 26, and the pulled-back Amari-Chentsov cubic tensor obeys the same character-level modular selection rule as the output tensor.

### 4.3 Metric consequence

Assume Theorem 4.2 holds. For `v_d in Vbar_d` and `v_e in Vbar_e`, with `d != e`,

```text
B(v_d, v_e) = g_*(Jbar v_d, Jbar v_e) = 0.
```

Therefore

```text
B = direct_sum_d B_d
```

as a genuine block decomposition of the observable residual/parameter quotient, not merely as a post-readout energy accounting.

This is the exact meaning of:

```text
the Fisher quadratic form pulls back packetwise.
```

### 4.4 Quotient-readout consequence

Let `q_k : C_N -> C_k` be the canonical quotient, with `k | N`. Let `P_{q_k}` be the output-side quotient projector. Paper 26 gives

```text
P_{q_k} = sum_{d | k} P_d.
```

Under exact conductor closure,

```text
Q_{q_k} = Pi_W P_{q_k} Pi_W | W
        = sum_{d | k} Q_d.
```

Since the `Q_d` are honest orthogonal projectors in the exact case, the quotient readout keeps precisely the pulled-back packets with `d | k` and annihilates precisely those with `d not| k`.

Thus Paper 26 pulls back through `J` without modification once the visible subspace is conductor-closed.

### 4.5 Cubic consequence

Define the pulled-back cubic tensor

```text
T_J(v_1, v_2, v_3) = T_*(Jbar v_1, Jbar v_2, Jbar v_3).
```

Under exact conductor closure, choose character-level vectors upstairs by pulling back output characters inside `W cap H_d`. If

```text
Jbar v_i = chi_{a_i}
```

or a linear combination supported in the corresponding packet, then the character-level selection rule is inherited:

```text
T_J(v_1, v_2, v_3) != 0
only if
a_1 + a_2 + a_3 = 0 mod N
```

on the character components that appear in the three vectors.

Consequently the same packet triples that are allowed output-side are the only packet triples allowed upstairs. In particular, when `N` is composite, there may be cross-packet cubic content in the residual quotient even though the pulled-back Fisher quadratic form is block diagonal.

This is the conductor blind spot transported through the Jacobian.

### 4.6 Proof of Theorem 4.2

The proof is standard finite-dimensional projection algebra.

`(1) <=> (2)`. If `W` is invariant under `P_d`, then because `P_d` is self-adjoint, `W^\perp` is also invariant under `P_d`. Hence `P_d` reduces the orthogonal decomposition `H_R = W direct_sum W^\perp`, so `P_d` commutes with `Pi_W`. Conversely, if `[Pi_W, P_d] = 0`, then for `w in W`,

```text
Pi_W P_d w = P_d Pi_W w = P_d w,
```

so `P_d w in W`.

`(2) => (3)`. If `Pi_W` commutes with `P_d`, then on `W`,

```text
Q_d^2 = Pi_W P_d Pi_W P_d Pi_W
      = Pi_W P_d^2 Pi_W
      = Q_d.
```

For `d != e`,

```text
Q_d Q_e = Pi_W P_d P_e Pi_W = 0.
```

The sum is `I_W` because `sum_d P_d = I_H`.

`(3) => (4)`. The ranges of the orthogonal projectors `Q_d` give an orthogonal direct-sum decomposition of `W`. Since `Q_d w = Pi_W P_d w` and the exact-projector condition forces `P_d w in W`, each range is exactly `W cap H_d`.

`(4) => (1)` is immediate.

`(4) <=> (5)` follows because `Jbar : Vbar -> W` is an isomorphism onto its image.

The metric, quotient, and cubic consequences follow by substituting this decomposition into the output-side Fisher, quotient-projector, and Amari-Chentsov formulas.

---

## 5. Ingredient 3: approximate transformer pullback

### 5.1 Why approximate structure is necessary

A real transformer residual stream is not expected to produce a visible subspace `W_l` that is exactly conductor-closed. Even when the final logits over a cyclic sub-vocabulary show strong packet energy, the intermediate residual subspace can be tilted relative to the output packet decomposition.

Therefore the operational question is not:

```text
Does [Pi_l, P_d] vanish exactly?
```

but:

```text
How small is [Pi_l, P_d], and how expensive is the pullback through J_l?
```

### 5.2 Leakage

**Definition 5.1 (Layer conductor leakage).**  
For `W_l = im J_l`, define

```text
epsilon_l = max_d ||[Pi_l, P_d]||_op,
```

where `Pi_l` is the orthogonal projector onto `W_l`.

Equivalent one-sided forms are

```text
delta_{l,d} = ||(I - Pi_l) P_d Pi_l||_op,
delta'_{l,d} = ||Pi_l P_d (I - Pi_l)||_op.
```

For orthogonal projections, these are controlled by the commutator norm, and the commutator norm is controlled by the largest off-diagonal block. Thus all three definitions measure the same geometric defect: how much a visible vector leaves the visible subspace when packet-projected.

### 5.3 Soft packet stability

**Theorem 5.2 (Approximate residual conductor pullback).**  
Let `Q_{l,d} = Pi_l P_d Pi_l | W_l`. Then for every layer/readout:

1. The operators `Q_{l,d}` form a positive partition of unity:

   ```text
   Q_{l,d} >= 0,
   sum_d Q_{l,d} = I_{W_l}.
   ```

2. If `epsilon_l = max_d ||[Pi_l, P_d]||_op`, then

   ```text
   ||Q_{l,d}^2 - Q_{l,d}||_op <= epsilon_l,
   ```

   and for `d != e`,

   ```text
   ||Q_{l,d} Q_{l,e}||_op <= epsilon_l.
   ```

3. If `epsilon_l < 1/4`, the spectrum of each `Q_{l,d}` lies near `{0,1}` up to a gap controlled by `epsilon_l`. Hence the approximate packet subspace may be defined by thresholding the spectrum of `Q_{l,d}` near `1`, with ambiguity only inside the transition band.

In words: small commutator leakage makes the soft conductor measurement close to a family of honest packet projectors.

### 5.4 Proof

For `w in W_l`, `Pi_l w = w`. Hence

```text
Q_d^2 - Q_d
= Pi P_d Pi P_d Pi - Pi P_d Pi
= Pi P_d (Pi - I) P_d Pi
= - Pi P_d (I - Pi) P_d Pi.
```

Therefore

```text
||Q_d^2 - Q_d||
<= ||(I - Pi) P_d Pi||
<= ||[Pi, P_d]||.
```

For `d != e`,

```text
Q_d Q_e
= Pi P_d Pi P_e Pi
= Pi P_d (Pi - I) P_e Pi
```

because `P_d P_e = 0`. Hence

```text
||Q_d Q_e||
<= ||Pi P_d (I - Pi)|| ||P_e Pi||
<= ||[Pi, P_d]||.
```

The spectral statement follows from the elementary fact that a self-adjoint positive contraction with small idempotence defect has spectrum near the roots of `lambda^2 - lambda = 0`, namely `0` and `1`.

### 5.5 Pulling back to residual coordinates

The clean bounds above live on `W_l`, where the metric is inherited from `H_R`. To express them in raw residual coordinates, one must transport through

```text
Jbar_l : Vbar_l -> W_l.
```

Let the nonzero singular values of `Jbar_l` be

```text
s_min(l) <= ... <= s_max(l)
```

and define

```text
kappa_l = s_max(l) / s_min(l).
```

If `A` is an operator on `W_l`, its transported residual-quotient operator is

```text
A^V = Jbar_l^{-1} A Jbar_l.
```

Then, for operator norms induced by the chosen quotient norm,

```text
||A^V|| <= kappa_l ||A||.
```

Quadratic-form and energy comparisons may cost `kappa_l^2`, because both input and output vectors must be compared through `Jbar_l`.

Therefore the residual-coordinate version of Theorem 5.2 is:

```text
operator form:
|| (Q_{l,d}^V)^2 - Q_{l,d}^V || <= kappa_l epsilon_l
|| Q_{l,d}^V Q_{l,e}^V ||       <= kappa_l epsilon_l

quadratic/energy form:
defect <= kappa_l^2 epsilon_l.
```

The exact exponent of `kappa_l` depends on whether one measures operators, forms, or energies. The invariant statement is simpler: use the quotient Fisher norm `||v||_B = ||Jbar_l v||_{g_*}` and the constants are the output-side constants above. Use the raw residual Euclidean norm and conditioning appears.

### 5.6 Cubic stability

Let

```text
T_l(v_1,v_2,v_3) = T_*(J_l v_1, J_l v_2, J_l v_3).
```

Let `Q_{l,d}` be the soft packet operators and let `E_{l,d}` be spectral packet projectors obtained by thresholding `Q_{l,d}` when `epsilon_l` is below the chosen gap tolerance.

The approximate cubic leakage outside the output selection rule is controlled by two defects:

1. **Subspace leakage:** the failure of `W_l` to be conductor-closed, measured by `epsilon_l`;
2. **Conditioning:** the cost of moving from `W_l` back to `Vbar_l`, measured by `kappa_l`.

A working bound has the form

```text
|T_l(v_f, v_e, v_m) - T_*(P_f Jv_f, P_e Jv_e, P_m Jv_m)|
<= C_N ||T_*|| epsilon_l prod_i ||v_i||_B,
```

for vectors whose soft packet labels are `f,e,m`. If the packet triple has no character components satisfying the modular selection rule, the leading term vanishes and the cubic value is `O(epsilon_l)` in the quotient Fisher norm, or `O(kappa_l^3 epsilon_l)` in raw residual coordinates.

This is the approximate version of the conductor blind spot upstairs: cross-packet cubic content that is allowed by the modular rule persists under a good pullback; content forbidden by the rule appears only at the leakage scale.

---

## 6. Reading existing papers through Paper 51

### 6.1 Paper 12

Paper 12 already contains the parameter Fisher and NTK pullback machinery:

```text
F(w) = E_z[J_w(z)^* g_{p_w(z)} J_w(z)].
```

Paper 51 supplies the missing subspace criterion. Paper 12 says that the parameter-side object is a Jacobian pullback. Paper 51 says when that pullback carries an honest conductor packet decomposition rather than only output-side packet energy.

### 6.2 Paper 26

Paper 26 proves exact quotient survival output-side:

```text
P_{q_k} = sum_{d | k} P_d.
```

Paper 51 says this survival law pulls back to residual/parameter space exactly when `im J_l` is conductor-closed, and approximately when the commutator leakage is small.

### 6.3 Paper 34

Paper 34 proves the blind spot at `p_*`: the Fisher quadratic is packet-diagonal while the cubic tensor sees cross-packet modular content.

Paper 51 transports that statement through `J_l`. It does not expand Paper 34's exact theorem off the centroid. It says: at a point where the output-side statement is valid, any Jacobian satisfying the exact or approximate pullback condition inherits the corresponding packet structure upstairs.

### 6.4 Paper 36

Paper 36 measures `f_{d,l}`, the packet energy visible at layer `l`.

Paper 51 adds the missing diagnostic:

```text
epsilon_l = max_d ||[Pi_l, P_d]||.
```

The pair `(f_{d,l}, epsilon_l)` separates two cases:

- high packet energy but large leakage: the readout sees conductor structure, but there is no stable residual packet subspace;
- high packet energy and small leakage: the residual layer approximately realizes the conductor pullback theorem.

Thus Paper 36's "which layer lifts which packet" becomes theorem-facing only after measuring `epsilon_l`.

### 6.5 Paper 38

Paper 38 defines a residual-stream frame cost using a model-dependent pullback `Pi`.

Paper 51 supplies the linear-algebra criterion for when that pullback is packet-aligned. The frame-cost term "packet-mismatch leakage" becomes a measurable commutator defect between the visible residual subspace and the output packet projectors.

### 6.6 Paper 45

Paper 45 certifies SAE decoder spans by projection onto packet supports.

Paper 51 refines the certification target. A CCSAE trained at layer `l` should certify against:

```text
exact case:      W_l cap H_d,
approximate case: spectral packet subspaces of Q_{l,d}.
```

This prevents a false upgrade from "the output projection is packet-clean" to "the residual feature itself is packet-clean." The latter requires small commutator leakage.

---

## 7. Empirical protocol deferred

The present draft contains the analysis core only. The empirical section should be added after the layerwise artifacts are available.

The minimal diagnostic suite is:

1. Choose a cyclic task algebra `C_N` and task sub-vocabulary.
2. For each layer `l`, construct the local readout `J_l`:
   - frozen unembedding lens;
   - trained full-label probe;
   - trained quotient probes;
   - optional SAE decoder map.
3. Compute `W_l = im J_l` numerically using an SVD threshold.
4. Compute output packet projectors `P_d`.
5. Compute:

   ```text
   f_{d,l}       = packet energy fraction,
   epsilon_l     = max_d ||[Pi_l, P_d]||,
   kappa_l       = condition number of Jbar_l,
   eta_l         = kappa_l^2 epsilon_l.
   ```

6. Report layers in four regimes:

   | regime | packet energy | leakage | interpretation |
   |---|---:|---:|---|
   | null | low | any | no visible cyclic packet |
   | readout-only | high | high | packet seen after readout, no stable residual packet subspace |
   | pulled-back | high | low | approximate residual conductor lift |
   | degenerate | high | low but high `kappa` | lift exists but is numerically unstable in raw residual coordinates |

7. For layers in the pulled-back regime, run causal packet patching:
   - patch only spectral packet subspace `E_{l,d}`;
   - compare to random same-rank subspaces;
   - compare to shuffled packet labels;
   - compare to quotient-forbidden packets.

The empirical claim is not part of this draft. The theorem merely states what these diagnostics would certify.

---

## 8. Falsifiers

The theorem itself is finite linear algebra. The transformer-facing interpretation can fail in several informative ways.

**F1. High packet energy with high leakage.**  
Paper 36's layerwise packet spectrum may show strong `H_d` energy, while `epsilon_l` remains large. Then the model has output-visible conductor structure but no stable residual packet subspace at that layer.

**F2. Low leakage only at the final unembedding.**  
If `epsilon_l` becomes small only at the final layer, the conductor structure is a late decoding phenomenon rather than a distributed residual-stream structure.

**F3. Good leakage, bad conditioning.**  
If `epsilon_l` is small but `kappa_l` is large, the quotient geometry is packet-aligned but unstable in raw residual coordinates. This would explain why probes see clean packet structure while interventions are brittle.

**F4. SAE mismatch.**  
If CCSAE features certified against output packet supports fail when recertified against the spectral subspaces of `Q_{l,d}`, then the earlier certification was output-clean but not residual-clean.

**F5. Causal patch failure.**  
If packet patching inside the low-leakage spectral subspaces does not affect the corresponding cyclic behavior more than same-rank controls, then the pullback is geometrically present but not causally load-bearing for that behavior.

---

## 9. Conclusion

The phrase "conductor packets pull back through residual subspaces" is true only under a precise condition.

The exact condition is:

```text
[Pi_l, P_d] = 0 for every conductor d.
```

Equivalently, the visible output subspace of the residual readout must be closed under the conductor projectors.

When this holds, the residual or parameter quotient decomposes into pulled-back packets, quotient readouts obey the same divisor law as Paper 26, and the Amari-Chentsov cubic selection rule of Paper 34 survives upstairs.

When it does not hold, there is still structure: the operators

```text
Q_{l,d} = Pi_l P_d Pi_l | W_l
```

form a soft conductor measurement. The commutator norm

```text
epsilon_l = max_d ||[Pi_l, P_d]||
```

is the obstruction to turning that soft measurement into honest residual packet subspaces.

Thus the residual conductor lift is neither a slogan nor a free assumption. It is a finite-dimensional transport theorem with a measurable defect.

---

## References and dependency map

- T1, *Native Simplicial Chart*: zero-sum hyperplane, Fisher-Rao pullback, gauge-compatible tangent chart.
- T2, *Cumulant Tower as Effective Action*: log-partition tower, Fisher quadratic, Amari-Chentsov cubic, closure defects.
- T3, *Character Orthogonality and the Conductor Lattice*: character basis, conductor packets, cubic modular selection rule.
- Paper 11, *Quotient-Character Adjacency Algebras*: finite packet algebra and projector calculus.
- Paper 12, *Discrete Fisher Skeletons for AI Optimization*: activation/parameter pullback, NTK and forcing-spectrum machinery.
- Paper 26, *The Conductor Probe-Obstruction Theorem*: quotient survival rule and pullback through `q_k^*`.
- Paper 34, *The Conductor Blind Spot*: output-side quadratic/cubic separation and second-order optimizer blind spot.
- Paper 36, *Layerwise Packet Spectroscopy*: layerwise packet fractions and residual-stream measurement program.
- Paper 38, *Multi-Head Attention as Frame-Cost Minimization*: residual-stream frame cost and packet-mismatch leakage.
- Paper 45, *Conductor-Certified Sparse Autoencoders*: decoder-span certification and packet-purity theorem.
