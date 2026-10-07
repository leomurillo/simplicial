# \heb{ל}2 — Identifying 3: The Cumulant Tower as Effective Action

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*leonardo.murillo@gmail.com*

*Preprint, version 1.0 — May 21, 2026*

## Abstract

**Situation.** [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) gave the chart: probability simplex, zero-sum hyperplane $H_0$, sphere pullback, Fisher–Rao metric, rotation group at the uniform. But the chart supplies only one geometric object — a metric. A working theory needs more: a notion of position, a notion of curvature, a notion of force, and a notion of how truncations of the theory fail. Where do these come from, and is there a unifying source for all of them?

**Task.** Identify a single scalar functional on [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s chart whose successive derivatives generate the geometric objects we need, with no ad-hoc additions.

**Action.** Use the **log-partition function** $\Phi(\eta) = \log Z(\eta)$ of the categorical exponential family. The natural parameters $\eta$ live on $H_0$ (dual to [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s centered chart); the mean parameters $\mu = \nabla \Phi$ are exactly the probabilities $p$. Take successive cumulants of $\Phi$.

**Result.** The derivatives of $\Phi$ form a tower:

1. $\nabla\Phi = \mu = p$ — the mean parameter; the position.
2. $\nabla^2 \Phi = \mathrm{Cov}(X)$ — the covariance of the sufficient statistic, equal to the **Fisher information** at $p$; the metric, and simultaneously the inertia.
3. $\nabla^3 \Phi = T$ — the **Amari–Chentsov 3-tensor**; the cubic structure that defines information geometry as its own subject beyond Riemannian geometry.
4. $\nabla^4 \Phi$ and higher — higher cumulants, which we read *programmatically* as **closure defects** of the cubic theory (§3): the residual that any third-order truncation of the cumulant tower must carry.

One functional $\Phi$, four successive geometric objects. The leap from order 2 (Fisher metric / Riemannian) to order 3 (Amari–Chentsov / dually flat) is the load-bearing distinction — the third cumulant is the first invariant Riemannian geometry cannot see. This is the "3" of the trilogy title, made concrete: the cumulant order at which information geometry separates from ordinary differential geometry.

This is \heb{ל}2 of the trilogy *Identifying 3*. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) supplied the chart; \heb{ל}2 develops its successor structure; \heb{ל}3 reads the resulting tensors through Pontryagin character orthogonality on the conductor lattice.

**Keywords:** information geometry, exponential families, log-partition function, cumulant generating functional, Fisher information, Amari–Chentsov tensor, dually flat structure, categorical distribution, effective action.

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=0.5em]
Take the probabilities of \(N\) outcomes and write one number (the log of their normalization) as a function of the parameters driving them. Successive derivatives of this single scalar generate every geometric object information geometry needs: the first recovers the probabilities themselves; the second gives the Fisher information metric (how distinguishable nearby distributions are); the third gives the Amari--Chentsov 3-tensor (the cubic ``force law'' that distinguishes information geometry from ordinary Riemannian geometry); the fourth records where any third-order truncation stops closing. Four named geometric objects from one functional, no extras. A Gaussian's third derivative vanishes, so Riemannian geometry sees its whole geometry; the categorical distribution does not stop at order 2, and its third cumulant is the first invariant Riemannian geometry cannot see: the ``3'' that the trilogy title names.
\end{mdframed}

---

## Notation (extending [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872))

| Symbol | Meaning |
|---|---|
| $\eta = (\eta_1, \dots, \eta_N) \in H_0$ | Natural parameters of the categorical exponential family (§1). |
| $Z(\eta) = \sum_i \exp(\eta_i)$ | Partition function. |
| $\Phi(\eta) = \log Z(\eta)$ | Log-partition; cumulant generating functional. |
| $\mu = \nabla \Phi \in \Delta^{N-1}$ | Mean parameter; equals the probability vector $p$. |
| $\Sigma_{ij} = \partial_i \partial_j \Phi$ | Covariance of the sufficient statistic; equals the Fisher information. |
| $T_{ijk} = \partial_i \partial_j \partial_k \Phi$ | Amari–Chentsov 3-tensor; third cumulant. |
| $Q_{ijk\ell} = \partial_i \partial_j \partial_k \partial_\ell \Phi$ | Fourth cumulant; programmatically read as the *closure defect* of the cubic theory (§3). |
| $X$ | The categorical sufficient statistic — a random vector taking values in $\{e_1, \dots, e_N\}$. |

Notation from [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) (in particular $\Delta^{N-1}$, $H_0$, $u$, $\psi$, $\langle\cdot,\cdot\rangle$) is in force throughout.

---

## 1. The categorical exponential family and the $\eta \leftrightarrow p$ duality

The categorical distribution over $N$ outcomes has a natural exponential family form. Parameterize by $\eta = (\eta_1, \dots, \eta_N) \in \mathbb{R}^N$ and set

$$p_i(\eta) = \frac{\exp(\eta_i)}{Z(\eta)}, \qquad Z(\eta) = \sum_{j=1}^N \exp(\eta_j).$$

The probabilities $p_i$ are invariant under the gauge $\eta \to \eta + c \cdot (1,1,\dots,1)$ for any scalar $c$: shifting all natural parameters by the same constant rescales $Z$ but leaves $p$ unchanged. The natural gauge slice is

$$\eta \in H_0 = \{ x \in \mathbb{R}^N : \textstyle\sum_i x_i = 0 \}.$$

This is the same $H_0$ that [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) identified as the simplex's tangent space at the uniform. The natural parameters live on it.

**Sufficient statistic.** A sample $X$ from the categorical distribution takes one of the values $e_1, \dots, e_N$ with probabilities $p_1, \dots, p_N$. Identifying $X$ with its coordinate vector in $\mathbb{R}^N$, the sufficient statistic is $X$ itself, with

$$\mathbb{E}_\eta[X_i] = p_i.$$

**Legendre duality.** The map $\eta \mapsto p$ is the Legendre transform of $\Phi$:

$$p_i = \frac{\partial \Phi}{\partial \eta_i}, \qquad \eta_i = \frac{\partial \Phi^*}{\partial p_i},$$

where $\Phi^*$ is the convex conjugate of $\Phi$ (it equals the negative Shannon entropy $\sum_i p_i \log p_i$ up to the gauge). The natural parameters and the mean parameters form a dually flat pair in the sense of Amari [Amari, 1985; Amari & Nagaoka, 2000]: $\eta$ parameterizes the **e-flat** ("exponential-flat") chart, $p$ the **m-flat** ("mixture-flat") chart, and the Legendre transform between them is $\Phi$.

The picture so far:

$$\eta \in H_0 \quad\xleftrightarrow{\;\;\Phi\;\;}\quad p \in \Delta^{N-1}.$$

The left side $\eta \in H_0$ is the natural ("force") chart, $e$-flat; the right side $p \in \Delta^{N-1}$ is the mean ("position") chart, $m$-flat. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s chart sits on the right side; \heb{ל}2 develops the structure on the left.

## 2. $\Phi(\eta) = \log Z$ as cumulant generating functional

The standard fact about exponential families: the log-partition $\Phi$ is the **cumulant generating function** of the sufficient statistic. In symbols:

$$\Phi(\eta) = \log \mathbb{E}_0\!\left[ \exp\!\big(\textstyle\sum_i \eta_i X_i\big) \right],$$

where $\mathbb{E}_0$ is expectation with respect to a reference measure on $\{e_1, \dots, e_N\}$. The Taylor expansion of $\Phi$ around any point $\eta_*$ has coefficients equal to the **cumulants** of $X$ at $\eta_*$:

$$\Phi(\eta_* + \delta) = \Phi(\eta_*) + \sum_i \mu_i\, \delta_i + \tfrac{1}{2} \sum_{i,j} \Sigma_{ij}\, \delta_i \delta_j + \tfrac{1}{6} \sum_{i,j,k} T_{ijk}\, \delta_i \delta_j \delta_k + \cdots$$

with coefficients

$$\mu_i = \partial_i \Phi, \quad \Sigma_{ij} = \partial_i \partial_j \Phi, \quad T_{ijk} = \partial_i \partial_j \partial_k \Phi, \quad Q_{ijk\ell} = \partial_i \partial_j \partial_k \partial_\ell \Phi, \quad \ldots$$

Each tensor is symmetric in all its indices (mixed partials commute) and is the corresponding **cumulant** of $X$ at $\eta_*$. This is standard [Brillinger, 1975].

For the categorical family, these can be computed in closed form. Differentiating once:

$$\partial_i \Phi = \frac{\partial}{\partial \eta_i} \log Z = \frac{\exp(\eta_i)}{Z} = p_i. \tag{1}$$

So **the first derivative of $\Phi$ is the mean parameter**: $\nabla \Phi = \mu = p$. This is the simplest possible way to see the Legendre duality of §1.

Differentiating again:

$$\partial_j p_i = \frac{\partial}{\partial \eta_j} \frac{\exp(\eta_i)}{Z} = \frac{\delta_{ij} \exp(\eta_i) Z - \exp(\eta_i) \exp(\eta_j)}{Z^2} = p_i(\delta_{ij} - p_j),$$

which gives the second-derivative (covariance) formula

$$\Sigma_{ij} = \partial_i \partial_j \Phi = p_i \delta_{ij} - p_i p_j. \tag{2}$$

This is simultaneously the covariance of $X$ at $p$ and the **Fisher information matrix** in $\eta$-coordinates. (The two coincide for any exponential family — another standard fact.)

Differentiating once more gives the third cumulant:

$$T_{ijk} = \partial_i \partial_j \partial_k \Phi = p_i\, \delta_{ij}\, \delta_{ik} - p_i p_k \delta_{ij} - p_i p_j \delta_{ik} - p_i p_j \delta_{jk} + 2 p_i p_j p_k. \tag{3}$$

*Symmetry check.* The first term $p_i \delta_{ij} \delta_{ik}$ is non-zero only when $i = j = k$, which is totally symmetric. The last term $2 p_i p_j p_k$ is symmetric under any permutation of $(i, j, k)$. The middle three terms — $-p_i p_k \delta_{ij}$, $-p_i p_j \delta_{ik}$, $-p_i p_j \delta_{jk}$ — are the three index pairings $(ij)$, $(ik)$, $(jk)$, summed; any transposition of $(i, j, k)$ permutes them among themselves. So $T_{ijk}$ is symmetric in all three indices, as required of a cumulant.

The fourth cumulant $Q_{ijk\ell} = \partial_i \partial_j \partial_k \partial_\ell \Phi$ is computed by one more differentiation; we record the formula schematically as $Q = O(p)$ in mixed second-, third-, and fourth-order products of $p_i$ and Kronecker deltas. The exact form is not needed for what follows.

\begin{figure}[H]
\centering
\begin{tikzpicture}[scale=1.0]

  % --- Panel 1: position (the point u) ---
  \begin{scope}[xshift=0cm]
    \draw[gray!40, very thin] (-1.1,-1.1) rectangle (1.1,1.1);
    \filldraw (0,0) circle (0.07);
    \node[above right] at (0,0) {$u$};
    \node[below] at (0,-1.4) {(i) $\nabla\Phi = \mu$};
    \node[below] at (0,-1.95) {\footnotesize position};
  \end{scope}

  % --- Panel 2: metric (round ellipsoid = Sigma) ---
  \begin{scope}[xshift=3.6cm]
    \draw[gray!40, very thin] (-1.1,-1.1) rectangle (1.1,1.1);
    \draw[thick] (0,0) ellipse (0.85 and 0.55);
    \filldraw (0,0) circle (0.06);
    \node[below right] at (0,0) {$u$};
    \node[above] at (0, 0.55) {$\Sigma$};
    \node[below] at (0,-1.4) {(ii) $\nabla^{2}\Phi = \Sigma$};
    \node[below] at (0,-1.95) {\footnotesize metric / inertia};
  \end{scope}

  % --- Panel 3: cubic (ellipsoid + skewness arrow = T) ---
  % Arrow ends on the ellipse at parametric angle 35 deg:
  %   (0.85 cos 35, 0.55 sin 35) = (0.696, 0.315)
  \begin{scope}[xshift=7.2cm]
    \draw[gray!40, very thin] (-1.1,-1.1) rectangle (1.1,1.1);
    \draw[thick] (0,0) ellipse (0.85 and 0.55);
    \filldraw (0,0) circle (0.06);
    \node[below left] at (0,0) {$u$};
    \draw[->, thick] (0,0) -- (0.696, 0.315);
    \node at (0.75, 0.85) {$T$};
    \node[below] at (0,-1.4) {(iii) $\nabla^{3}\Phi = T$};
    \node[below] at (0,-1.95) {\footnotesize Amari--Chentsov};
  \end{scope}

  % --- Panel 4: quartic (ellipsoid + outer shell = Q) ---
  \begin{scope}[xshift=10.8cm]
    \draw[gray!40, very thin] (-1.1,-1.1) rectangle (1.1,1.1);
    \draw[thick] (0,0) ellipse (0.85 and 0.55);
    \draw[dashed, thick] (0,0) ellipse (1.00 and 0.72);
    \filldraw (0,0) circle (0.06);
    \node[below right] at (0,0) {$u$};
    \node at (0.75, 0.85) {$Q$};
    \node[below] at (0,-1.4) {(iv) $\nabla^{4}\Phi = Q$};
    \node[below] at (0,-1.95) {\footnotesize closure defect};
  \end{scope}

\end{tikzpicture}
\caption{The cumulant tower at the uniform $u \in \Delta^{N-1}$, generated by successive derivatives of one functional~$\Phi = \log Z$. Each panel adds one order: (i)~the point~$u$ itself, the mean parameter; (ii)~a round ellipsoid representing the covariance / Fisher information $\Sigma|_u$, which is the metric and the inertia; (iii)~the same ellipsoid with a small directional bias representing the Amari--Chentsov skewness $T|_u$, the first object beyond Riemannian geometry (it vanishes for $N=2$ at the centroid); (iv)~an outer contour shell representing the fourth cumulant $Q|_u$, the closure defect of the cubic truncation. The figure visualizes the tower as a sequence of refinements, each adding structure that the previous order cannot see.}
\label{fig:cumulant-tower}
\end{figure}

## 3. Identifying each cumulant with a geometric object

Each derivative of $\Phi$ plays a distinct, named role.

**Order 1: position.** $\mu = \nabla \Phi$ is the **mean parameter** of the family, which by (1) equals the probability vector $p$. Geometrically: the Legendre dual of $\eta$. Physically: where the system sits in $\Delta^{N-1}$.

**Order 2: metric / inertia.** $\Sigma_{ij}$ has three simultaneous interpretations:

- the **covariance** of the sufficient statistic $X$ at $\eta$;
- the **Fisher information** $I_{ij}(\eta)$, which controls how distinguishable nearby distributions are;
- the **inertia tensor** of the exponential family — the "mass matrix" coupling rates of change of $\eta$ to rates of change of $\mu$.

In coordinates: $\Sigma = \partial \mu / \partial \eta$, so $\Sigma$ is the Jacobian of the Legendre map $\eta \mapsto \mu$. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s identification of Fisher–Rao with a pulled-back sphere metric corresponds, in this language, to evaluating $\Sigma$ at the uniform and recognizing it as the round-sphere metric on $H_0$ (up to [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s factor-of-4 convention).

**Order 3: force / Amari–Chentsov tensor.** $T_{ijk}$ is the **Amari–Chentsov 3-tensor** [Chentsov, 1982; Amari & Nagaoka, 2000]. It is the first object of the tower that is not Riemannian — symmetric 3-tensors do not appear in ordinary Riemannian geometry; they enter only when the family is non-Gaussian.

Three readings:

- $T_{ijk}$ is the **third cumulant** of $X$ — its skewness structure.
- $T_{ijk}$ is the **cubic difference tensor** of Amari's dual flat structure. The $\alpha$-connection family of §4 reads $\Gamma^{(\alpha)}_{ijk} = \Gamma^{LC}_{ijk} - \tfrac{\alpha}{2}\, T_{ijk}$, so the Levi-Civita connection of $\Sigma$ sits at the $\alpha = 0$ midpoint and the e-connection ($\alpha = +1$) and m-connection ($\alpha = -1$) differ from each other by $T_{ijk}$ after lowering an index with the Fisher metric. $T$ is itself a **symmetric** 3-tensor (the standard Amari–Chentsov object); calling it the "cubic difference tensor" names its role as the splitting that distinguishes the dual pair from the Riemannian average.
- $T_{ijk}$ acts as a **force law** in cubic dynamics on the simplex. The Taylor expansion of §2 makes the analogy precise: $T_{ijk}$ is the cubic vertex in the expansion of $\Phi$, exactly as the cubic coupling in a field-theory action $S[\phi]$ is the cubic vertex of its perturbative expansion. In a flow generated by gradients of a function $h$ with respect to $\Sigma$, the leading correction beyond linear response is the contraction $\Sigma^{-1} T \nabla h$ — the analogue of a Newtonian force scaled by inverse mass.

**Order 4 and higher: closure defects (programmatic reading).** $Q_{ijk\ell}$ is, on borrowed grounds, just the **fourth cumulant** of the sufficient statistic — the fourth derivative of $\Phi$ at $\eta_*$, a standard exponential-family object. We additionally adopt the label **closure defect** for $Q$, in the following programmatic sense: were the cubic tensor $T_{ijk}$ to satisfy a Jacobi-like identity at the categorical family, third-order dynamics generated by $T$ would be closed under composition and the perturbative tower would terminate at order 3, with $Q$ vanishing. It does not. The fourth cumulant is therefore read as the residual that any third-order projection of the full cumulant theory must carry, and the higher cumulants as the extended obstruction tower.

This reading is a working interpretation, not a theorem: \heb{ל}2 introduces *closure defect* as a label for $Q$ on the cumulant tower at $u$, without proving a residual or closure theorem to back the reading. Downstream, $Q$ is used as the next cumulant tensor; the closure-defect framing is exposition, not deductive content.

The cumulant tower is therefore the canonical successor structure on [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s chart: each derivative of one functional $\Phi$ supplies a named, load-bearing geometric object, and the tower extends naturally to all orders.

## 4. The leap from order 2 to order 3

Among the cumulants, the transition from order 2 to order 3 is structurally distinguished. Three observations.

**Gaussians stop at order 2.** A multivariate Gaussian has $\Phi$ quadratic in $\eta$, so all cumulants of order $\geq 3$ vanish identically. Riemannian geometry — and the entire toolkit of Gaussian statistics — sees only $\mu$ and $\Sigma$. The 3-tensor is invisible.

**The categorical family does not stop.** The exponential of a non-quadratic $\Phi$ has non-vanishing higher cumulants. For the categorical family, $T_{ijk}$ in (3) is non-zero generically; an information-geometric theory needs it.

**Order 3 is where the dually flat structure first appears.** Two classical results combine:

- **Chentsov's uniqueness theorem** [Chentsov, 1982]: on the categorical simplex (and more generally on any statistical manifold of positive measures), the Fisher–Rao metric is the unique Riemannian metric (up to scale) invariant under sufficient statistics. This pins down the order-2 content.

- **Amari's $\alpha$-connections** [Amari, 1985]: a one-parameter family of affine connections $\nabla^{(\alpha)}$ on the simplex, all compatible with Fisher–Rao, related to the Levi-Civita connection $\nabla^{LC}$ of $\Sigma$ by

$$\Gamma^{(\alpha)}_{ijk} = \Gamma^{LC}_{ijk} - \tfrac{\alpha}{2}\, T_{ijk}.$$

The $\alpha$-connections coincide with $\nabla^{LC}$ exactly when $T_{ijk} = 0$. Two of them — the **e-connection** ($\alpha = +1$) and the **m-connection** ($\alpha = -1$) — are flat (zero curvature), and they are dual under $\Sigma$. The dual flat structure that defines information geometry as a subject distinct from Riemannian geometry therefore exists **only because** $T_{ijk} \neq 0$.

The first cumulant order at which information geometry has content beyond Riemannian geometry is therefore **three**. This is the operational meaning of the trilogy title *Identifying 3*: the third cumulant is where information geometry separates from its Gaussian shadow.

**A parallel "leap to 3" inside the cumulant story.** For $N = 2$ (Bernoulli), $T_{ijk}$ evaluated at the uniform $u = (1/2, 1/2)$ vanishes — the binary family is "too symmetric" to exhibit the third cumulant at the centroid (verification: substitute $p_i = 1/2$ into (3) and every term cancels; equivalently, the sigmoid third derivative $p(1-p)(1-2p)$ has a zero at $p = 1/2$). For $N \geq 3$, $T_{ijk}|_u \neq 0$ generically (see §5.2 for the $N = 3$ computation, which gives $T_{111}|_u = 2/27$).

The trilogy title's "Identifying 3" therefore appears twice in this paper, in parallel:

- **Cumulant-order leap:** order 2 (Riemannian / Gaussian) $\to$ order 3 (information-geometric / Amari–Chentsov). The third cumulant is the first invariant Riemannian geometry cannot see.
- **Outcome-count leap:** $N = 2 \to N = 3$. The simplex with two outcomes has no Amari–Chentsov tensor at the centroid; the simplex with three outcomes does.

Both leaps cross the same threshold for the same reason: the third symmetric tensor is the first object on the categorical exponential family that does not vanish by symmetry, and it does so only when both the cumulant order and the simplex dimension are large enough to support it.

## 5. Worked examples

### 5.1. $N = 2$ (Bernoulli)

For Bernoulli, the cleanest natural parameter is the **logit** $\eta = \log(p_1 / p_2) \in \mathbb{R}$ (a single scalar, since $H_0 \subset \mathbb{R}^2$ is one-dimensional after the gauge fixing). In this parameterization

$$\Phi(\eta) = \log(1 + e^\eta), \qquad p_1 = \frac{e^\eta}{1 + e^\eta} = \sigma(\eta), \qquad p_2 = 1 - p_1,$$

where $\sigma$ is the **sigmoid**. Writing $p = p_1$, the cumulant tower is the classic table of sigmoid derivatives:

$$\Phi'(\eta) = p, \qquad \Phi''(\eta) = p(1-p), \qquad \Phi'''(\eta) = p(1-p)(1 - 2p), \qquad \Phi^{(4)}(\eta) = p(1-p)(1 - 6p(1-p)).$$

At the uniform $p = 1/2$: $\Phi' = 1/2$, $\Phi'' = 1/4$, $\Phi''' = \mathbf{0}$, $\Phi^{(4)} = -1/8$.

**Bernoulli at the centroid has no Amari–Chentsov tensor**: the third cumulant vanishes by the $p \leftrightarrow 1-p$ symmetry of the binary outcome. Information geometry on $\Delta^1$ at $u$ is entirely Riemannian. To see the third cumulant non-trivially at the centroid, we need $N \geq 3$.

### 5.2. $N = 3$ (trinomial)

Gauge-fix $\sum \eta_i = 0$; then $\eta \in H_0$ is 2-dimensional. The probability vector is $p_i = \exp(\eta_i)/\sum_j \exp(\eta_j)$.

At the uniform $u = (1/3, 1/3, 1/3)$, the second cumulant is

$$\Sigma_{ij}|_u = p_i \delta_{ij} - p_i p_j = \tfrac{1}{3} \delta_{ij} - \tfrac{1}{9}.$$

Restricted to $H_0$ (i.e., acting on tangent vectors $v, w$ with $\sum v_i = \sum w_i = 0$), the constant second term drops out and

$$\Sigma|_{u, H_0} = \tfrac{1}{3}\, I_{H_0}.$$

This is the **covariance** of $X$ at $u$, which equals the Fisher information **in $\eta$-coordinates**. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) §5 worked in **$p$-coordinates** (mean coordinates), where Fisher information is the inverse Jacobian of the Legendre map and evaluates to $N \langle\cdot,\cdot\rangle$ on $H_0$. The two are consistent precisely as inverses:

$$\bigl(\Sigma|_{u, H_0}\bigr)^{-1} = 3\, I_{H_0} = N \langle\cdot,\cdot\rangle\big|_{H_0} = g_{FR}|_u \text{ in p-coordinates.}$$

The same metric viewed from the two dual charts: $\Sigma$ in $\eta$, $g_{FR}$ in $p$, related by Legendre inversion.

The third cumulant at the uniform: from (3) with $p_i = 1/3$:

$$T_{ijk}|_u = \tfrac{1}{3} \delta_{ij} \delta_{ik} - \tfrac{1}{9}(\delta_{ij} + \delta_{ik} + \delta_{jk}) + \tfrac{2}{27}.$$

For $i = j = k = 1$: $T_{111}|_u = \tfrac{1}{3} - \tfrac{3}{9} + \tfrac{2}{27} = \tfrac{2}{27} \neq 0$.

For distinct $i, j, k$: $T_{ijk}|_u = 0 - 0 + \tfrac{2}{27} = \tfrac{2}{27}$.

So $T|_u$ on $\Delta^2$ is a non-trivial symmetric 3-tensor — the first Amari–Chentsov structure of the trilogy that actually exists at the centroid. From $N = 3$ onward, information geometry has genuine cubic content the metric cannot supply.

## 6. The effective-action framing

*Forward pointer.* That $\Phi$ earns this name is derived, not posited, in Paper 54 (*The One Functional, Derived*, Theorem 1): $\Phi=\log Z$ is the generating function of the completely passive (Gibbs) states, and the identity $\nabla^2\Phi=$ covariance $=$ response $=$ Fisher is the static fluctuation–dissipation theorem (Theorem 2).

In statistical physics, $-\log Z$ is the dimensionless free energy of a Gibbs ensemble with sources $\eta$. Its derivatives generate connected correlation functions. In quantum field theory, the analogous functional is the Legendre transform $\Gamma[\phi]$ of $W[J] = \log Z[J]$, called the **effective action**; its stationary points give the equations of motion, and its successive derivatives are the 1PI vertices.

Here $\Phi(\eta) = \log Z(\eta)$ plays the same role for the categorical exponential family: it is the cumulant generating functional, its first derivative gives the mean, its second the covariance, its third the cubic vertex, and so on. Calling $\Phi$ the **categorical effective action** is therefore appropriate in the precise sense that it generates the family's connected $n$-point functions through differentiation.

We do not develop a dynamical theory built on $\Phi$ in \heb{ל}2. The point of the effective-action framing is only to name the functional and to license the standard physics intuition: *one scalar object generates the tower*. [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872)'s chart said where probability lives; \heb{ל}2's $\Phi$ says how probability is governed.

**A forward note (the cubic vertex as a dynamical coefficient).** Although \heb{ל}2 does not build a dynamical theory, one exact consequence pins $T_{ijk}$ to a measurable coefficient and bridges to the Curvature-and-Current track [CBS]. On a 2-dimensional (marginal / Hopf) sector of $H_0$ with complex coordinate $z = x_1 + i x_2$, let the cubic vertex $T_{abc}$ ($a,b,c \in \{1,2\}$) supply the leading nonlinearity of the slow cyclic flow.

> **Proposition 6.1 (cubic vertex $=$ Stuart–Landau symmetry-breaking coefficient).** The leading rotation-symmetry-breaking coefficient of the cubic flow — the $\bar z^2$ coefficient of the Stuart–Landau normal form — is exactly the spin-3 (traceless) part of the Amari–Chentsov vertex,
> $$\gamma = -\tfrac18\big[(T_{111}-3T_{122}) + i(3T_{112}-T_{222})\big] = -\overline{w_3},$$
> where $w_3$ is the $z^3$ component of $T$ on the sector and the gauge-covariant resonant term ($|z|^2 z$) is the spin-1 (trace) part. Hence the orbit's non-circularity, the slow-chart curvature defect, and the spectral/functional dimensionality gap of [CBS] are three readings of the one vertex $T = \nabla^3\Phi$.

*Proof.* The cubic gradient flow is $\dot z = -2\,\partial_{\bar z} V_3$ with $V_3 = \tfrac16 T_{abc}x^a x^b x^c$; substitute $x_1 = (z+\bar z)/2$, $x_2 = (z-\bar z)/(2i)$ and collect the $\bar z^2$ coefficient. The spin decomposition of a symmetric 3-tensor on a 2-plane into its $z^3$ (spin-3) and $|z|^2 z$ (spin-1) parts identifies $\gamma = -\overline{w_3}$. Certified `empirical/probe_gamma_kch_identity.py`. $\square$

This is the exact form of the $\kappa_3$ scaling law observed in [CBS] (the "tri-linkage"): there the same $T = \nabla^3\Phi$ appears as the third cumulant of a learned representation and controls the deformation of a maintained limit cycle; \heb{ל}2 supplies the explicit constant $\tfrac18$ and the spin-projection. The cumulant tower thus generates not only the static objects of §3 but, through the spin decomposition of its cubic vertex, the leading coefficients of the cubic dynamics.

**A second forward note (the tower in closed form; the arithmetic transfer).** A single closed form pins the *entire* tower on the uniform categorical and supplies the spectral side of an arithmetic identity used downstream [N5].

> **Proposition 6.2 (the all-distinct cumulant tower; the apex side of the explicit-formula transfer).** For the uniform categorical on $m$ points the joint cumulant of $n$ *distinct* one-hot coordinates is
> $$\kappa_n = (-1)^{n-1}(n-1)!\,m^{-n},\qquad\text{equivalently the cumulant generating function is}\quad \log\!\big(1+t/m\big).$$
> On the conductor block $(\mathbb Z/p)^\times$ ($m=\varphi(p)=p-1$) this tower is the spectral side of the explicit-formula transfer of [N5, Thm 6.2]: it equals $(-1)^n$ times the Hardy–Littlewood connected $n$-tuple weight $-(n-1)!/(p-1)^n$, the sign being the $\alpha\!\to\!-\alpha$ dual involution $t\mapsto -t$ on $\Phi$ — the Fisher metric ($n=2$) self-dual, the Amari–Chentsov cubic ($n=3$) flipped.

*Proof.* In the cumulant–partition identity $\kappa_n = \sum_\pi (-1)^{|\pi|-1}(|\pi|-1)!\prod_{B\in\pi}(\partial_B Z/Z)$ with $Z(t)=\sum_j e^{t_j}$, every $\partial_B Z$ with $|B|\ge 2$ vanishes on distinct indices (each $e^{t_j}$ depends on one variable), so only the all-singletons partition survives, giving $(-1)^{n-1}(n-1)!\prod_k(\partial_{i_k}Z/Z)\big|_0 = (-1)^{n-1}(n-1)!\,m^{-n}$. Summing $\sum_{n\ge1}(-1)^{n-1}(n-1)!\,m^{-n}t^n/n! = \sum_{n\ge1}(-1)^{n-1}(t/m)^n/n = \log(1+t/m)$. The transfer comparison and the dual involution are [N5, Thm 6.2]. Certified `empirical/probe_n5_transfer_signn.py`. $\square$

The same $T=\nabla^3\Phi$ that §6's first note sends into the Stuart–Landau coefficient is, here at $n=3$, the cubic rung $\kappa_3 = +2/(p-1)^3$ whose sign-flip against the arithmetic $-2/(p-1)^3$ is the $e\!\leftrightarrow\!m$ duality of §4 — the cubic, not the metric, carries the connection.

## 7. The toolkit, as a working list

*All derivatives are taken in $\eta$-coordinates at any reference $\eta_* \in H_0$. Translation to $p$-coordinates is by Legendre inversion: $\Sigma_p = \Sigma_\eta^{-1}$, with corresponding transformations of the higher tensors (§5.2).*

| Order | Tensor | Standard name | Geometric role |
|---|---|---|---|
| 0 | $\Phi(\eta)$ | log-partition | scalar generating functional (free energy) |
| 1 | $\mu_i = \partial_i \Phi$ | mean parameter | position; equals probability vector $p$ |
| 2 | $\Sigma_{ij} = \partial_i \partial_j \Phi$ | covariance / Fisher information | metric and inertia (the Riemannian content) |
| 3 | $T_{ijk} = \partial_i \partial_j \partial_k \Phi$ | Amari–Chentsov 3-tensor | force law; the first invariant beyond Riemannian geometry |
| 4 | $Q_{ijk\ell} = \partial_i \partial_j \partial_k \partial_\ell \Phi$ | fourth cumulant | *closure defect* of the cubic theory — programmatic reading (§3); borrowed content is "fourth cumulant" |
| $\geq 5$ | higher cumulants | — | extended closure tower |

Four objects are generated by one functional. The chart of [\heb{ל}1](https://doi.org/10.5281/zenodo.20336872) hosts the tower; the leap from order 2 to order 3 is the moment information geometry separates from Riemannian geometry.

\heb{ל}3 will pick a finite ring structure $\mathbb{Z}/N$ on the outcome index set and read the multilinear forms $\Sigma_{ij}$, $T_{ijk}$, $Q_{ijk\ell}$, $\ldots$ through the Pontryagin character basis $\widehat{\mathbb{Z}/N}$. The cubic vertex $T_{ijk}$ then carries a **selection rule** of the form $k + \ell + m \equiv 0 \pmod{N}$ — a finite arithmetic constraint that picks out which character-mode combinations can be non-zero. The cumulant tower of \heb{ל}2 supplies the tensors; \heb{ל}3 supplies their arithmetic decomposition. \heb{ל}2's role is complete at the tower itself.

## 8. Acknowledgments

I collaborated extensively with agentic AI (Anthropic's Claude Opus 4.7, Google's Gemini 3.1 Pro, OpenAI's ChatGPT 5.5, and xAI's Grok 4.3) during the development of the derivations presented in this paper. These collaborations were productive for real-time derivation checking, literature contextualization, and iterative exposition. I acknowledge this use transparently; the mathematical content and its correctness are my responsibility.

## 9. References

Amari, S. (1985). *Differential-Geometrical Methods in Statistics.* Lecture Notes in Statistics 28. Springer.

Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry.* Translations of Mathematical Monographs 191. American Mathematical Society.

Brillinger, D. R. (1975). *Time Series: Data Analysis and Theory.* Holt, Rinehart and Winston. (For the standard exponential-family / cumulant-generating identification.)

Chentsov, N. N. (1982). *Statistical Decision Rules and Optimal Inference.* Translations of Mathematical Monographs 53. American Mathematical Society. (Russian original 1972.)

Murillo Montero, L. (2026). *\heb{ל}1 — Identifying 3: The Native Simplicial Chart.* Zenodo preprint (concept DOI, resolves to latest version), DOI [10.5281/zenodo.20336872](https://doi.org/10.5281/zenodo.20336872).

Murillo Montero, L. (2026). *[CBS] Curvature and Current: The Two Blind Spots of Self-Supervised Representation Learning.* Zenodo, DOI [10.5281/zenodo.20519464](https://doi.org/10.5281/zenodo.20519464).

Murillo Montero, L. (2026). *[N5] The Apex Edge Operator and the Archimedean Weil Form.* First draft, June 5, 2026. (Thm 6.2: the explicit-formula transfer $\kappa_n^{\mathrm{HL}} = (-1)^n\,\kappa_n^{\mathrm{apex}}$ on the conductor block.)
