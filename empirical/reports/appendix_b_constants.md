# Empirical Validation Report: Appendix B Constants and $K^3 = -K$

**Claim under test:** Trace computations, eigenvalues, and characteristic polynomial of the unscaled simplicial cross-product matrix $\tilde{K}(u)$ and its scaled version $K(u)$ for $N=4$ as stated in §3.1 and Appendix B.

**Methodology:** 
We built a symbolic verification script using `sympy` (`empirical/verify_appendix_b_constants.py`). We defined symbolic variables $u_1, u_2, u_3, u_4$ subject to the zero-sum constraint $u_4 = -u_1 - u_2 - u_3$, constructed the matrix $\tilde{K}$ exactly as defined in Definition 3.1, and rigorously evaluated the sum of squares, trace, characteristic polynomial, and corresponding constants. A numerical spot-check was also performed using $u = [0.75, -0.25, -0.25, -0.25]$.

## 1. Findings on Specific Claims

Reviewer X is correct. The manuscript contains multiple arithmetic errors in its derivation of the normalisation factor, although the final stated theorem ($K^3 = -K$) is miraculously robust due to a series of compensating errors.

- **(i) Sum of squares of entries of $\tilde{K}(u)$ (line 618):**
  - **Manuscript:** Claims $6 \sum_i u_i^2$.
  - **Correction:** The correct symbolic sum is **$8 \sum_i u_i^2$**.

- **(ii) $\operatorname{tr}(K^2)$ intermediate formula (line 622):**
  - **Manuscript:** Claims $\operatorname{tr}(K^2) = \frac{1}{3}(-1)(6 \sum u_i^2) = -2 \sum u_i^2$.
  - **Correction:** Using $K = \frac{1}{\sqrt{3}} \tilde{K}$, we have $\operatorname{tr}(K^2) = \frac{1}{3} \operatorname{tr}(\tilde{K}^2)$. The trace of $\tilde{K}^2$ is the negative of the sum of squared entries, so $\operatorname{tr}(\tilde{K}^2) = -8 \sum u_i^2$. Therefore, $\operatorname{tr}(K^2) = -\frac{8}{3} \sum u_i^2$.

- **(iii) $\operatorname{tr}(K^2)$ final value (line 628):**
  - **Manuscript:** Incomplete/garbled arithmetic: $\operatorname{tr}(K^2) = -2 \cdot \frac{3}{4} \cdot \frac{2}{3} = \ldots$ (The author seems to have realised $-2(3/4) \neq -2$ and appended arbitrary factors to reach the target).
  - **Correction:** Applying the unit-axis condition $\sum u_i^2 = 3/4$ to the correct formula $-\frac{8}{3} \sum u_i^2$, we obtain exactly $-\frac{8}{3} \cdot \frac{3}{4} = -2$. The derivation cleanly works out without arbitrary factors.

- **(iv) $\tilde{K}^3$ equation in §3.1 (line 205):**
  - **Manuscript:** Claims $\tilde{K}^3 = -c^2 \tilde{K}$ with $c^2 = 3/4$.
  - **Correction:** The characteristic polynomial of $\tilde{K}$ under the zero-sum constraint is $\lambda^4 + 4(\sum u_i^2)\lambda^2 = 0$. Using $\sum u_i^2 = 3/4$, the minimal polynomial is $\lambda^3 + 3\lambda = 0$. Thus, $\tilde{K}^3 = -3\tilde{K}$. The correct constant is **$c^2_{\text{unscaled}} = 3$**.

- **(v) Unscaled spectrum (Remark B.1, line 638):**
  - **Manuscript:** Claims spectrum is $\{0, 0, \pm\sqrt{3/4} i\}$ and $\tilde{K}^3 = -\frac{3}{4}\tilde{K}$.
  - **Correction:** As derived above, the spectrum is **$\{0, 0, \pm i\sqrt{3}\}$** and $\tilde{K}^3 = -3\tilde{K}$.

## 2. Status of Theorem 3.3

**The core theorem ($K^3 = -K$) is computationally PRESERVED.** 
Because $\tilde{K}^3 = -3\tilde{K}$, if we scale by $1/\sqrt{3}$ to obtain $K = \tilde{K}/\sqrt{3}$, we get:
$$ K^3 = \left(\frac{1}{\sqrt{3}}\tilde{K}\right)^3 = \frac{1}{3\sqrt{3}} \tilde{K}^3 = \frac{1}{3\sqrt{3}} (-3\tilde{K}) = -\frac{1}{\sqrt{3}} \tilde{K} = -K $$
The factor $1/\sqrt{3}$ defined in Definition 3.1 is absolutely correct; only the underlying arithmetic justification in the text is flawed.

## 3. Required Revisions

The Author must revise the following locations to replace the erroneous constants:
- **Line 205:** Update $c^2 = 3/4$ to $c^2 = 3$ and $-\frac{3}{4}\tilde{K}(u)$ to $-3\tilde{K}(u)$.
- **Lines 207-209:** The notation $\frac{1}{\sqrt{3/4}}\cdot \frac{1}{2}$ may need rethinking, since the $1/\sqrt{3}$ is sufficient by itself.
- **Line 618:** Correct $6\sum_i u_i^2$ to $8\sum_i u_i^2$, and update the parenthetical explanation (a row contains $u_i - u_j$, sum of squares per row expands differently under zero sum).
- **Line 622:** Correct the intermediate trace formula to $\operatorname{tr}(K(u)^2) = -\frac{8}{3} \sum u_i^2$.
- **Lines 627-628:** Clean up the final substitution: $-\frac{8}{3} \cdot \frac{3}{4} = -2$.
- **Line 638:** Correct the unscaled spectrum to $\{0, 0, \pm i\sqrt{3}\}$ and the minimal polynomial to $\tilde{K}^3 = -3\tilde{K}$.

STATUS: AMBER
