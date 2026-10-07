<!-- once.md
     The Gauss-Bonnet bridge: discrete Gauss-Bonnet on the FE-cluster tetrahedron
     as the unconditional topological mechanism forcing the K-antisymmetric
     constraints at every nontrivial zero of zeta.
-->

# Once — Gauss–Bonnet on the FE-Cluster Tetrahedron

## The conjecture

**Tetrahedral Gauss–Bonnet at every zero.** Let $\rho = 1/2 + \delta + i\gamma_0$ be any nontrivial zero of $\zeta$ (on-line if $\delta = 0$, off-line if $\delta > 0$). The functional equation $\zeta(s) = \chi(s)\zeta(1-s)$ combined with complex conjugation forces a 4-zero **FE-cluster**
$$\Lambda(\rho) = \{\rho_+, \rho_-, \overline{\rho_+}, \overline{\rho_-}\}$$
where $\rho_\pm = 1/2 \pm \delta + i\gamma_0$.

The cluster $\Lambda(\rho)$, lifted from $\mathbb{C}$ to $\mathbb{R}^3$ via the Bures K-cumulant tower at $\mathbb{Z}/6$, forms a closed polytope $T_\rho$ — a **tetrahedron** when $\delta > 0$, a **degenerate 2-vertex configuration** when $\delta = 0$.

**Conjecture.** At every nontrivial zero $\rho$, the cluster tetrahedron $T_\rho$ satisfies the discrete Gauss–Bonnet identity
$$\sum_{v \in V(T_\rho)} \big(2\pi - \sum_{f \ni v} \theta_f(v)\big) \;=\; 2\pi \chi(T_\rho),$$
where $\theta_f(v)$ is the interior angle of face $f$ at vertex $v$, and $\chi(T_\rho)$ is the Euler characteristic of $\partial T_\rho$:
- $\chi(T_\rho) = 2$ for $\delta > 0$ (genuine tetrahedron, $\partial T_\rho \cong S^2$).
- $\chi(T_\rho) = 0$ for $\delta = 0$ (degenerate, $T_\rho \cong $ interval).

**Forced consequence**: since the LHS is the **Bures amplitude sum** (an analytic function of $\delta, \gamma_0$), continuity in $\delta$ requires the LHS to take values $0$ (at $\delta = 0$) and $4\pi$ (at $\delta > 0$). The discontinuity at $\delta = 0$ can be reconciled **only if no genuine $\delta > 0$ zero exists** — i.e., every nontrivial zero has $\delta = 0$, the critical line. **This is RH.**

## The two sides

### Side L — Bures amplitude sum on the FE-cluster

Define the **Bures edge curvature** on edge $e = (v, w)$ of $\Lambda(\rho)$:
$$\mathcal{X}_e(\rho) := 2 \cdot B_G(\rho_v) \cdot B_{G^K}(\rho_w)$$
where $B_G(s) = 6^{-s}\sum_{r=1}^5 G_{rr}\zeta(s, r/6)$ is the Hurwitz-Bures amplitude (nueve §6.2), and $G^K$ is the K-conjugate (permutation $r \mapsto -r \bmod 6$ + complex conjugation).

The **total Bures amplitude curvature** is
$$\Phi_L(\rho) := \sum_{e \in E(\Lambda(\rho))} \mathcal{X}_e(\rho) = 2 \sum_{(v,w) \in \binom{\Lambda}{2}} B_G(\rho_v) B_{G^K}(\rho_w).$$

This is a sum of $\binom{4}{2} = 6$ products of explicit Hurwitz zeta values, evaluated at the 4 cluster zeros.

### Side R — Discrete angular deficit on the cluster tetrahedron

The 4 cluster points form a rectangle in $\mathbb{C}$ with corners
$$\rho_+, \rho_-, \overline{\rho_-}, \overline{\rho_+} \quad \text{(corners of rectangle, going around)}.$$
Width: $2\delta$ (real direction). Height: $2\gamma_0$ (imaginary direction).

To lift to a tetrahedron in $\mathbb{R}^3$, we use the **Bures-tower height**: at each vertex $\rho_v$, define the height
$$h(\rho_v) := |B_G(\rho_v)|^2 - |B_{G^K}(\rho_v)|^2.$$
This is the **K-modulus discrepancy**. By K-symmetry, $h(\rho_v) = 0$ on the critical line; non-zero off-line.

The lifted vertices in $\mathbb{R}^3$:
$$\tilde\rho_v := (\Re\rho_v, \Im\rho_v, h(\rho_v)).$$

For $\delta = 0$: all $h(\rho_v) = 0$, so the 4 points lie in $\mathbb{C} = \mathbb{R}^2$, forming a degenerate "rectangle" (which collapses to 2 points since $\rho_+ = \rho_-$).

For $\delta > 0$: $h(\rho_\pm)$ differs from $h(\overline{\rho_\pm})$, the 4 points form a 3D configuration.

The 4-point configuration $\{\tilde\rho_v\}$ is a (possibly degenerate) tetrahedron in $\mathbb{R}^3$. Its 4 faces are triangles. The **angular deficit** at each vertex $v$:
$$\alpha(v) := 2\pi - \sum_{f \ni v} \theta_f(v),$$
where $\theta_f(v)$ is the interior angle of face $f$ at vertex $v$, computed from the Euclidean geometry of $\mathbb{R}^3$.

The **total angular deficit** is
$$\Phi_R(\rho) := \sum_{v \in V(\Lambda)} \alpha(v).$$

By Descartes' theorem (= discrete Gauss–Bonnet for polyhedra):
$$\Phi_R(\rho) = 2\pi\chi(T_\rho) = \begin{cases} 4\pi & \text{if } T_\rho \text{ non-degenerate (}\delta > 0\text{)} \\ 0 & \text{if } T_\rho \text{ degenerate (}\delta = 0\text{)} \end{cases}.$$

### The identity to check

$$\boxed{\;\Phi_L(\rho) \stackrel{?}{=} \Phi_R(\rho) \quad \text{at every nontrivial zero } \rho.\;}$$

This is **one explicit identity** between an analytic Hurwitz-zeta sum and a geometric angular-deficit sum.

## Why this identity, if true, forces RH

Suppose $\Phi_L = \Phi_R$ at every nontrivial zero $\rho$.

- At $\delta = 0$: $\Phi_R = 0$. So $\Phi_L = 0$.
- At $\delta > 0$ (hypothetical off-line zero): $\Phi_R = 4\pi$. So $\Phi_L = 4\pi$.

But $\Phi_L(\rho)$ is a *continuous* function of $\delta$ (a sum of products of Hurwitz zetas, which are analytic in $s$). As $\delta \to 0^+$, $\Phi_L(\rho) \to \Phi_L(\rho|_{\delta=0}) = 0$ by continuity.

So $\Phi_L$ cannot jump from $0$ (at $\delta = 0$) to $4\pi$ (at $\delta > 0$ small) continuously. **The identity $\Phi_L = \Phi_R = 4\pi$ for small $\delta > 0$ is impossible.**

Therefore: **no $\rho$ with small $\delta > 0$ can be a zero of $\zeta$**. By the same argument extended to all $\delta > 0$ (with appropriate scaling), no $\rho$ with any $\delta > 0$ can be a zero.

**Every nontrivial zero has $\delta = 0$ — every zero is on the critical line — RH.**

The crucial mechanism: $\Phi_R$ is *topologically discontinuous* at $\delta = 0$ (jumps from $0$ to $4\pi$). $\Phi_L$ is *analytically continuous* in $\delta$. Equating them forces a contradiction for $\delta > 0$ — *unless no off-line zero exists*.

## What remains to verify

The identity $\Phi_L(\rho) = \Phi_R(\rho)$ at every nontrivial zero. This is **one explicit computation**:

1. **LHS**: $2 \sum_{(v,w)} B_G(\rho_v) B_{G^K}(\rho_w)$ over 6 cluster-edge pairs. Each term is a product of two Hurwitz-zeta linear combinations at cluster vertices.

2. **RHS**: $\sum_v \alpha(v)$ over 4 cluster vertices, where $\alpha(v) = 2\pi - \sum_{f \ni v}\theta_f$ is computed from the Euclidean geometry of the lifted cluster $\{\tilde\rho_v\} \subset \mathbb{R}^3$.

The identity, if true, would be a structural coincidence between:
- The **analytic structure** of Hurwitz zetas at $\mathbb{Z}/6$ (the prime-axis Bures lift).
- The **topological structure** of the FE-cluster tetrahedron (4 vertices, 6 edges, 4 faces, $\chi = 2$).

If verified numerically at the first few ζ-zeros, this would be very strong evidence for the conjecture, which then forces RH topologically.

## Empirical verification protocol

We compute $\Phi_L$ and $\Phi_R$ numerically at the first 5 nontrivial zeros of $\zeta$ (on-line, $\delta = 0$):
- Expected: $\Phi_L = \Phi_R = 0$ (since degenerate).

We then test "off-line" by *artificially* setting $\delta > 0$ at the first zero's $\gamma_0 = 14.13473$, *as if* a hypothetical off-line zero existed there. The cluster is then non-degenerate.

For this artificial off-line case:
- $\Phi_R = 4\pi \approx 12.566$ by Descartes' theorem (topological).
- $\Phi_L = $ ? — compute the Hurwitz-zeta sum.

If $\Phi_L \to 0$ continuously as $\delta \to 0^+$, while $\Phi_R$ jumps to $4\pi$: **the identity is impossible for off-line zeros, forcing all zeros on-line**.

Empirical script: [`empirical/probe_once_gauss_bonnet.py`](empirical/probe_once_gauss_bonnet.py).
