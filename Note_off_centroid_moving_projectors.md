# Note: Off-Centroid Moving Projectors for \(K^{CH}\)

**Status:** theory bridge; complements the empirical weekday/month centroid
pipeline.

The uniform tetrahedral theorem writes \(K^{CH}_{p_*}\) using the fixed
projector squares \(I+K(\tau_i)^2\).  The off-centroid version is not a
single fixed-projector correction.  The right object is the moving score
frame.

For \(p\in\Delta_N^\circ\), define

$$
\sigma_i(p):=e_i-p\in T_p\Delta_N^\circ.
$$

For tangent vectors \(u,v\), the Fisher metric gives

$$
g_p(\sigma_i(p),u)=\frac{u_i}{p_i},
\qquad
\|\sigma_i(p)\|_{g_p}^2=\frac{1-p_i}{p_i}.
$$

Therefore the raised Amari-Chentsov cubic admits the exact moving-frame
presentation

$$
K^{CH}_p(u)v
=
\sum_i p_i\,g_p(\sigma_i(p),u)\,g_p(\sigma_i(p),v)\,\sigma_i(p).
$$

If \(\Pi_i^p\) denotes the \(g_p\)-orthogonal projector onto
\(\mathbb R\sigma_i(p)\), then

$$
\Pi_i^p v
=
\frac{g_p(\sigma_i(p),v)}{\|\sigma_i(p)\|_{g_p}^2}\sigma_i(p)
=
\frac{v_i}{1-p_i}\sigma_i(p),
$$

and equivalently

$$
K^{CH}_p(u)v
=
\sum_i (1-p_i)\,g_p(\sigma_i(p),u)\,\Pi_i^p v.
$$

For \(N=4\), the tangent space is an oriented three-dimensional
inner-product space under \(g_p\).  Let \(K_p(a)\) be the cross-product
operator defined by the Fisher-Hodge star at \(p\), and set
\(\widehat\sigma_i(p)=\sigma_i(p)/\|\sigma_i(p)\|_{g_p}\).  Then

$$
\Pi_i^p=I+K_p(\widehat\sigma_i(p))^2,
$$

so

$$
K^{CH}_p(u)v
=
\sum_i(1-p_i)\,g_p(\sigma_i(p),u)
\left(I+K_p(\widehat\sigma_i(p))^2\right)v.
$$

The matrix \(K_p(u)\) can be written explicitly.  Let

$$
r_i:=\sqrt{p_i},\qquad D_p:=\operatorname{diag}(1/p_i).
$$

The map \(L_p:H\to r^\perp\subset\mathbb R^4\), \(L_p(x)_i=x_i/r_i\),
is an isometry from \((H,g_p)\) to the Euclidean hyperplane orthogonal to
\(r=(r_1,r_2,r_3,r_4)\).  With the orientation chosen to match the uniform
matrix of the simplicial vector-calculus draft, define

$$
K_p(u)v
=
L_p^{-1}\left(-*_{\mathbb R^4}
\bigl(r\wedge L_pu\wedge L_pv\bigr)\right).
$$

Equivalently, with \(\varepsilon_{1234}=+1\),

$$
\bigl(K_p(u)v\bigr)_i
=
-\sum_{j,k,\ell=1}^4
\varepsilon_{ijk\ell}\,
\frac{r_i r_j}{r_k r_\ell}\,u_kv_\ell,
$$

or, as matrix entries,

$$
\bigl(K_p(u)\bigr)_{i\ell}
=
-\sum_{j,k=1}^4
\varepsilon_{ijk\ell}\,
\frac{r_i r_j}{r_k r_\ell}\,u_k.
$$

Expanded out, this is

$$
K_p(u)=
\begin{pmatrix}
0&
\frac{r_1}{r_2}\left(\frac{r_4}{r_3}u_3-\frac{r_3}{r_4}u_4\right)&
\frac{r_1}{r_3}\left(\frac{r_2}{r_4}u_4-\frac{r_4}{r_2}u_2\right)&
\frac{r_1}{r_4}\left(\frac{r_3}{r_2}u_2-\frac{r_2}{r_3}u_3\right)
\\[0.6em]
\frac{r_2}{r_1}\left(\frac{r_3}{r_4}u_4-\frac{r_4}{r_3}u_3\right)&
0&
\frac{r_2}{r_3}\left(\frac{r_4}{r_1}u_1-\frac{r_1}{r_4}u_4\right)&
\frac{r_2}{r_4}\left(\frac{r_1}{r_3}u_3-\frac{r_3}{r_1}u_1\right)
\\[0.6em]
\frac{r_3}{r_1}\left(\frac{r_4}{r_2}u_2-\frac{r_2}{r_4}u_4\right)&
\frac{r_3}{r_2}\left(\frac{r_1}{r_4}u_4-\frac{r_4}{r_1}u_1\right)&
0&
\frac{r_3}{r_4}\left(\frac{r_2}{r_1}u_1-\frac{r_1}{r_2}u_2\right)
\\[0.6em]
\frac{r_4}{r_1}\left(\frac{r_2}{r_3}u_3-\frac{r_3}{r_2}u_2\right)&
\frac{r_4}{r_2}\left(\frac{r_3}{r_1}u_1-\frac{r_1}{r_3}u_3\right)&
\frac{r_4}{r_3}\left(\frac{r_1}{r_2}u_2-\frac{r_2}{r_1}u_1\right)&
0
\end{pmatrix}.
$$

This extension satisfies

$$
\mathbf 1^\top K_p(u)=0,\qquad K_p(u)p=0,\qquad
D_pK_p(u)+K_p(u)^\top D_p=0.
$$

On \(H\),

$$
K_p(u)^3=-\|u\|_{g_p}^2K_p(u).
$$

Thus, for a \(g_p\)-unit axis \(u\), the local Fisher-Rodrigues tangent
rotation is

$$
R_p(u,\theta)
=
I_H+\sin\theta\,K_p(u)+(1-\cos\theta)K_p(u)^2.
$$

At \(p_*=\frac14\mathbf1\), all \(r_i\) are equal and the expanded matrix
reduces to the raw cyclic-difference matrix \(\widetilde K(u)\), i.e. the
\(M\)-normalized version of the uniform simplicial cross product.

This is the exact off-centroid deformation of the \(N=4\) uniform formula.
Along \(p(t)=p_*+th\), with \(\tau_i=e_i-p_*\), the displacement \(h\)
moves:

1. the score axes, \(\sigma_i(t)=\tau_i-th\);
2. the Fisher metric, \(g_{p(t)}(a,b)=\sum_i a_i b_i/p_i(t)\);
3. the weights, \(1-p_i(t)\);
4. the Fisher-Hodge cross product \(K_{p(t)}\).

The character-convolution formulas in Papers 10-12 are the Fourier-side
Taylor expansion of this moving-projector identity.
