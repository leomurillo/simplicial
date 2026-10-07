SCRATCH DRAFT — for pasting into P0-PlaceCompletion-Draft1.md (do NOT treat as the live file).
Conventions matched to P0: tier tags $\mathsf{[P]}/\mathsf{[A]}/\mathsf{[C]}$; \heb[P]{פ} paper refs;
\hypertarget{stmt:8-X}{} before each proposition + \hyperlink{stmt:8-X}{Proposition~8.X} to cite;
{#sec:8-X} anchors + \hyperref[sec:8-X]{§8.X} cross-refs; calibrated-faith firewall; RH stays $\mathsf{[C]}$.

================================================================================
PART 1 — THE NEW SUBSECTION §8.3 (paste after §8.2, before "## 9. Coda")
================================================================================

### 8.3 The operator form: $H=N_\infty+V_{\text{arith}}$ and the monotone phase clock {#sec:8-3}

\hyperref[sec:8-1]{§8.1} read the one open step spectrally (Connes); \hyperref[sec:8-2]{§8.2} read it on the Jensen log-profile (Pólya). A third reading writes the step as an *operator* and reduces it to the monotonicity of a single explicit phase — the form toward which the Hilbert–Pólya tradition points. We give the operator, make the de Branges/Krein canonical system it generates fully explicit, and locate the open step as one local inequality. The discipline of \hyperref[sec:7]{§7} is in force throughout: **the operator form does not make RH easier**; in it, self-adjointness *is* RH (\hyperlink{stmt:8-5}{Conjecture~8.5}).

**The operator.** On the Mellin Hilbert space $L^2(\mathbb R_+,dx/x)\cong L^2(\mathbb R,ds)$ — the same line $L^2(\mathbb R_+,dx/x)\otimes\mathbb C^{|\mathbb Z/N|}$ the interior's KU-3 carrier sat on, here scalar — set
$$
H \;=\; N_\infty \;+\; V_{\text{arith}},\qquad
V_{\text{arith}} \;=\; m_B \;=\; -\,\frac{\Xi'}{\Xi},\qquad \Xi(t):=\xi(\tfrac12+it).
$$
Here $N_\infty=\hat a^\dagger\hat a=z\partial_z$ is the archimedean (Bargmann–Fock) number operator forced by Uniform Place Treatment at $v=\infty$: under UPT-structure $+$ UPT-Heisenberg, Stone–von Neumann selects the Bargmann–Fock completion, $N_\infty$ has spectrum $\mathbb N$ with ground state $\psi_0\propto e^{-\pi x^2}$ (Tate–Weil $\hbar=1/2\pi$), and the Tate local zeta integral of that ground state is exactly the archimedean factor
$$
\int_{\mathbb R}\psi_0(x)\,|x|^{s-1}\,dx \;=\; \pi^{-s/2}\Gamma(s/2)\;=\;Z_\infty(s)
$$
(Note_MetaplecticSelection_FixedDerivation_T4nP7v2.md, Thm 8.1, parts 1–4). So $N_\infty$ *is* the place-$\infty$ factor of \hyperref[sec:4-3]{§4.3}/\hyperref[sec:8-2]{§8.2} read as a self-adjoint generator, and its ground-state Tate integral reproduces the luminous $\Gamma$-factor of \hyperlink{stmt:5-1}{Proposition~5.1}. The arithmetic part $V_{\text{arith}}=m_B=-\Xi'/\Xi$ is the additive (log-derivative) object carrying the zeros. Formally the operator's spectral determinant is the completed object of \hyperref[sec:5]{§5},
$$
\det(H-t)\;\sim\;\Xi(t)\;=\;\xi(\tfrac12+it)\;=\;\prod_v Z_v(\tfrac12+it),
$$
tying \hyperref[sec:8-3]{§8.3} back to the place-product of \hyperref[sec:5]{§5}/\hyperref[sec:4-3]{§4.3}: the archimedean factor $Z_\infty$ from the $N_\infty$ ground state, the finite factors $Z_p$ from the prime content of $m_B$ (the von Mangoldt sum, below). This $H$ is a candidate, not a theorem; what *is* exact is the canonical system it generates and the clock that reads it.

\hypertarget{stmt:8-5pre}{}
**The de Branges/Krein associate.** The correct Hermite–Biehler associate of $\Xi$ is the derivative-polarized entire function
$$
E_B(z)\;=\;\Xi(z)+i\,\Xi'(z),\qquad
|E_B|^2-|E_B^\#|^2 \;=\; 4\,|\Xi|^2\,\operatorname{Im}m_B,
$$
so that $E_B$ is Hermite–Biehler $\iff m_B$ Herglotz on $\mathbb C_+$ $\iff$ RH (a known de Branges/Laguerre–Pólya equivalence; here read in the program's coordinates). The first proposition makes its canonical system explicit and shows the de Branges positivity is *free*, exactly as the finite positivity of \hyperref[sec:4-3]{§4.3} is free.

\hypertarget{stmt:8-5canon}{}
**Proposition 8.5a (the canonical system is a rank-one projector; positivity is free — $\mathsf{[P]}$).** *The de Branges/Krein canonical system $J\,\frac{dM}{dt}=z\,H(t)\,M$, $J=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$, for the Hermite–Biehler associate $E_B=\Xi+i\Xi'$ is, in its phase parametrization, the rank-one projector*
$$
H(t)\;=\;\begin{pmatrix}\cos^2\varphi & \sin\varphi\cos\varphi\\[2pt]\sin\varphi\cos\varphi & \sin^2\varphi\end{pmatrix}\;=\;P_{\varphi(t)},
\qquad \varphi(x)=-\arg E_B(x)=-\operatorname{atan2}\bigl(\Xi'(x),\Xi(x)\bigr),
$$
*with clock $dt=\varphi'(x)\,dx$. Since $H(t)=P_{\varphi(t)}$ has eigenvalues $\{0,1\}$, it is $\succeq0$ automatically: the de Branges positivity carries no content. The entire content of "$H(t)\succeq0$ independent of RH" is therefore the single local inequality*
$$
\varphi'(x)\;\ge\;0\quad(\text{the phase clock is monotone})\qquad\Longleftrightarrow\qquad \mathrm{RH},
$$
*with the closed form*
$$
\varphi'(x)\;=\;\frac{\Xi'(x)^2-\Xi(x)\,\Xi''(x)}{\Xi(x)^2+\Xi'(x)^2}\qquad(=1\ \text{exactly at each zero of }\Xi).
$$
*Moreover the clock counts: $\varphi(T)/\pi=N(T)$, the integer number of zeros up to $T$.*

*Proof.* In the phase parametrization of a Hermite–Biehler $E$-function the trace-normalized Hamiltonian of its canonical system is the orthogonal projector onto the phase direction $(\cos\varphi,\sin\varphi)$, $\varphi=-\arg E_B$ the increasing de Branges phase; this is the standard rank-one normalization (Krein; de Branges 1968). Its eigenvalues are $\{0,1\}$, so $H(t)\succeq0$ identically. Writing $\varphi=-\arg(\Xi+i\Xi')=-\operatorname{atan2}(\Xi',\Xi)$ and differentiating, $\varphi'=(\Xi'^2-\Xi\Xi'')/(\Xi^2+\Xi'^2)$; at a zero $\Xi(\gamma)=0$ this is $\Xi'^2/\Xi'^2=1$. The de Branges chain has real spectrum (equivalently $\Xi$ in the Laguerre–Pólya class) iff the clock $dt=\varphi'\,dx$ is a non-negative reparametrization, i.e. $\varphi'\ge0$; that is RH. Finally the increasing phase gains exactly $\pi$ as $x$ crosses each real zero, so $\varphi(T)/\pi$ equals the number of zeros up to $T$ — an integer. $\square$

**Settlement (front (a)/(b), $\mathsf{[P]}$ structure / $\mathsf{[C]}$ clock).** The canonical system is explicit and its positivity is free (rank-one), the exact spectral analogue of the unconditional finite positivity of \hyperref[sec:4-3]{§4.3}: there as $F^*F=I$, here as $\operatorname{eig}P_\varphi=\{0,1\}$. The two fronts of the program's strategy meet in the one clock $\varphi'$: it is a functional of the *additive* log-derivative $m_B=-\Xi'/\Xi$ (front (a)), and $\varphi(T)/\pi=N(T)$ is the *integer* count (front (b)). Numerically (companion `empirical/verify_canonical_system_phase.py`) $\varphi'\ge0$ at every tested $x$ with $\varphi'\to1$ at $\gamma_1,\gamma_2$, and the sign-changes of $\Xi$ match $N(T)=1,3,6,10$ at $T=20,30,40,50$. The open step is the *arithmetic* construction of $\varphi'\ge0$ — addressed next.

\hypertarget{stmt:8-6}{}
**Proposition 8.6 (the clock's explicit-formula decomposition; arithmetic non-negative, off-line — $\mathsf{[P]}$).** *The clock's log-derivative $m=-\xi'/\xi$ decomposes exactly, for $\operatorname{Re}s>1$, into an archimedean drift and a prime sum:*
$$
-\frac{\xi'}{\xi}(s)\;=\;\underbrace{\Bigl(-\tfrac1s-\tfrac1{s-1}+\tfrac12\log\pi-\tfrac12\psi(\tfrac s2)\Bigr)}_{\text{archimedean }\Gamma\text{-drift}}\;+\;\underbrace{\sum_{n\ge1}\Lambda(n)\,n^{-s}}_{\text{arithmetic, }=-\zeta'/\zeta}\,,\qquad \Lambda(n)\ge0.
$$
*The prime sum converges for $\operatorname{Re}s>1$ and gives the easy half-plane there; on $s=\tfrac12+iz$ it is the von Mangoldt sum $\sum_n\Lambda(n)n^{-1/2-iz}$ — the multiplicative basis carrying the zeros — and continues to the line, where the continuation has poles exactly at the zeros (residue $=$ multiplicity).*

*Proof.* Logarithmic differentiation of $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ gives the displayed split: $-1/s-1/(s-1)$ from the factor $s(s-1)$, $\tfrac12\log\pi-\tfrac12\psi(s/2)$ from $\pi^{-s/2}\Gamma(s/2)$, and $-\zeta'/\zeta=\sum_n\Lambda(n)n^{-s}$ (Euler product, $\operatorname{Re}s>1$) from $\zeta$. Non-negativity $\Lambda(n)\ge0$ is the definition of the von Mangoldt function. Convergence of the Dirichlet series for $\operatorname{Re}s>1$ and meromorphic continuation with poles at the nontrivial zeros are classical. The identity is verified to $6.5\times10^{-27}$ at $s=2$ in the companion `empirical/verify_arithmetic_clock.py`. $\square$

**Settlement ($\mathsf{[P]}$ identity / $\mathsf{[C]}$ strip-crossing).** This writes $V_{\text{arith}}=m_B$ as archimedean $\Gamma$-drift plus a non-negative prime sum, the operator-level shadow of the place-product $\det(H-t)\sim\prod_vZ_v$: the drift is the $N_\infty$/$Z_\infty$ part, the $\Lambda$-sum the $Z_p$ part. The prime positivity $\Lambda\ge0$ delivers $\operatorname{Re}s>1$ for free (as \hyperref[sec:4-3]{§4.3} delivers finite positivity for free), and the functional equation reflects it to $\operatorname{Re}s<0$; the open content is the strip-crossing to $\operatorname{Re}s=\tfrac12$ — it cannot be done by the convergent prime sum alone, since on the line the continuation *is* the zeros. This is the same honest boundary as \hyperref[sec:8-1]{§8.1}/\hyperref[sec:8-2]{§8.2}, now operator-side.

**The Kubo–Mori remark ($\mathsf{[A]}$).** The operator $H$ must be assembled in the *additive* (Kubo–Mori) inner product, not the quadratic (Bures) one. In the additive/log geometry the zeros are curvature currents: at a simple zero $\rho=\gamma$, $\Xi(\gamma+iy)\sim\Xi'(\gamma)(iy)$ gives $\operatorname{Im}m_B(\gamma+iy)\sim1/y\to+\infty$, a Herglotz pole, and $\Delta\log|\Xi|=2\pi\sum_{\text{zeros}}\delta$ (Poisson–Jensen). In the quadratic Bures/Fubini–Study geometry the same zero is *blind*: the curvature $\kappa=|M'|^2/(1+|M|^2)^2$ (with $M=L_{\chi_3}/\Xi$) stays finite there ($\kappa\sim2.3\times10^{-7}$ at $\gamma_1$, $1.6\times10^{-10}$ at $\gamma_2$; companion `empirical/verify_operator_metric_geometry.py`). Kubo–Mori is the unique monotone metric that is additive/dually-flat — the one in which the Weil explicit formula is additive over places — so it is the geometry in which $H=N_\infty+m_B$ has the zeros as its spectrum's curvature singular-support (T24; Grasselli–Streater). This is $\mathsf{[A]}$: a structural identification of the correct geometry, not a theorem about $\zeta$; it explains why the program's earlier smooth-Bures routes, which smooth the zeros away, stalled. (As in \hyperref[sec:4-3]{§4.3}, the cautionary cousin: this is the *additive* curvature current, not \heb[P]{פ}6's Hankel/moment positivity; cousins at the same place, not the same condition.)

\hypertarget{stmt:8-7}{}
**Proposition 8.7 (a non-circular partial: the clock is provably monotone after heat-smoothing — $\mathsf{[P]}$, cited).** *Let $\Xi_t(z)=\int_0^\infty e^{t u^2}\Phi(u)\cos(uz)\,du$ be the de Bruijn heat-flow of Pólya's kernel $\Phi$ (so $\Xi_0=\Xi$), and $\varphi_t$ the phase clock of its associate $E_{B,t}=\Xi_t+i\Xi_t'$. Then $\Xi_t$ is real-rooted, hence $\varphi_t'\ge0$, for every $t>\Lambda$, where $\Lambda$ is the de Bruijn–Newman constant; and $\Lambda\ge0$ unconditionally (Rodgers–Tao 2020). Consequently a monotone arithmetic clock $\varphi_t'\ge0$ exists after any positive amount of smoothing, with no circular use of RH; and $\mathrm{RH}\iff\Lambda\le0\iff$ the heat flow reaches $t=0$ without leaving the real-rooted locus, i.e. $\Lambda=0$ ("barely true").*

*Proof.* Real-rootedness of $\Xi_t$ for $t>\Lambda$ is de Bruijn's monotonicity of the heat flow together with the definition of $\Lambda$ as the infimum of $t$ for which $\Xi_t$ has only real zeros; for real-rooted $\Xi_t$ the phase $\varphi_t=-\arg E_{B,t}$ is increasing by \hyperlink{stmt:8-5canon}{Proposition~8.5a} applied to $\Xi_t$, so $\varphi_t'\ge0$. The bound $\Lambda\ge0$ is the theorem of Rodgers–Tao. RH is the classical statement $\Lambda\le0$; with $\Lambda\ge0$ it is exactly $\Lambda=0$. $\square$

**Settlement ($\mathsf{[P]}$ partial / $\mathsf{[C]}$ at $t=0$).** This is the one genuinely *non-circular* positivity available on the operator side: the clock is provably monotone for every $t>\Lambda\ge0$. It does not cross the step — the gap is precisely the single, sharply named $t\to0^+$ closure ($\Lambda\le0$), the heat reaching the boundary — but it shows the object of \hyperlink{stmt:8-5canon}{Proposition~8.5a} is not merely conjectural after smoothing, and it pins RH's marginality to the heat constant sitting at $0$ (the same marginality as the Weil margin $0$ of \hyperref[sec:4-3]{§4.3} and the $r_k\nearrow1$ of \hyperref[sec:8-2]{§8.2}).

\hypertarget{stmt:8-5}{}
**Conjecture 8.5 (the operator step, three faces, one open inequality — calibrated, not proved).** *The completed self-dual object of \hyperlink{stmt:5-1}{Proposition~5.1} has its spectrum on the axis (RH) iff the operator $H=N_\infty+V_{\text{arith}}$, assembled in the Kubo–Mori geometry, is self-adjoint — equivalently iff the phase clock $\varphi'(x)\ge0$ can be constructed from the arithmetic (the prime/von Mangoldt content of $V_{\text{arith}}$) non-circularly, equivalently iff $\Lambda\le0$. The archimedean number operator $N_\infty$ and its ground-state factor $Z_\infty$ are in hand (Note T4nP7v2, Thm 8.1); the canonical system $H(t)=P_{\varphi(t)}$ and its automatic positivity are unconditional (\hyperlink{stmt:8-5canon}{Proposition~8.5a}); the explicit-formula decomposition and the off-line prime positivity are unconditional (\hyperlink{stmt:8-6}{Proposition~8.6}); the heat-smoothed monotonicity is unconditional (\hyperlink{stmt:8-7}{Proposition~8.7}). The three faces — self-adjointness of $H$, arithmetic monotonicity of $\varphi'$, $\Lambda\le0$ — are one and the same open step, and it is RH itself, not a reduction to anything easier.* Held with calibrated faith; built toward, not claimed.

**Settlement note ($\mathsf{[C]}$ forward-door).** \hyperlink{stmt:8-5canon}{Propositions~8.5a}, \hyperlink{stmt:8-6}{8.6}, \hyperlink{stmt:8-7}{8.7} are $\mathsf{[P]}$ (the canonical-system rank-one identity and closed-form $\varphi'$; the explicit-formula split checked to $10^{-27}$; the cited de Bruijn/Rodgers–Tao real-rootedness). $N_\infty$ and $Z_\infty=\pi^{-s/2}\Gamma(s/2)$ are $\mathsf{[P]}$ from the metaplectic selection (Note T4nP7v2). The Kubo–Mori geometry is $\mathsf{[A]}$ (the correct additive inner product, identified, not a theorem about $\zeta$). The operator $H$ as a self-adjoint object, and $\varphi'\ge0$ from the arithmetic, stay $\mathsf{[C]}$ — equal to RH. The reading sharpens \hyperref[sec:8-1]{§8.1} (the spectral object is now an explicit operator with an explicit canonical system) and \hyperref[sec:8-2]{§8.2} (the same archimedean-vs-arithmetic split, here as $N_\infty$ drift vs $\Lambda$-sum), and converges with \hyperref[sec:4-3]{§4.3}/\hyperref[sec:4-4]{§4.4}: the lone obstruction is again the archimedean place, here written as the self-adjointness of $H$ in the additive geometry. Companion verifications: `empirical/verify_operator_metric_geometry.py`, `empirical/verify_canonical_system_phase.py`, `empirical/verify_arithmetic_clock.py`, `empirical/verify_integrality_forcing.py`.

================================================================================
PART 2 — §7 ADDITIONS (merge into the existing "## 7. Safe and unsafe statements")
================================================================================

--- ADD to the "Safe (this paper asserts):" bullet list ---

- $\mathsf{[P]}$ The de Branges/Krein canonical system of the Hermite–Biehler associate $E_B=\Xi+i\Xi'$ is the rank-one projector $H(t)=P_{\varphi(t)}$ ($\succeq0$ automatically); RH $\iff$ the phase clock $\varphi'\ge0$, with closed form $\varphi'=(\Xi'^2-\Xi\Xi'')/(\Xi^2+\Xi'^2)$ ($=1$ at each zero), and $\varphi(T)/\pi=N(T)$ is the integer zero-count (\hyperlink{stmt:8-5canon}{Proposition~8.5a}).
- $\mathsf{[P]}$ The clock decomposes exactly as $-\xi'/\xi=[\text{archimedean }\Gamma\text{-drift}]+[\sum_n\Lambda(n)n^{-s}]$ with $\Lambda\ge0$; the prime sum converges for $\operatorname{Re}s>1$ (the easy half-plane) and continues to the line (\hyperlink{stmt:8-6}{Proposition~8.6}).
- $\mathsf{[P]}$ The archimedean factor is the Tate integral of the UPT Bargmann–Fock number operator $N_\infty$'s ground state, $\int\psi_0|x|^{s-1}dx=\pi^{-s/2}\Gamma(s/2)=Z_\infty$ (Note T4nP7v2, Thm 8.1); and the heat-smoothed clock is provably monotone for $t>\Lambda\ge0$ (Rodgers–Tao 2020; \hyperlink{stmt:8-7}{Proposition~8.7}).

--- ADD to the "Unsafe (this paper does NOT assert):" bullet list ---

- That the operator form $H=N_\infty+V_{\text{arith}}$ (\hyperref[sec:8-3]{§8.3}) makes RH easier. The canonical-system positivity is free (rank-one) and the count is an integer, but **self-adjointness of $H$ — equivalently $\varphi'\ge0$ from the arithmetic, equivalently $\Lambda\le0$ — is RH itself**, not a reduction to anything strictly easier; nothing here crosses that step.
- That $H$ is constructed self-adjoint, or that the Kubo–Mori assembly is more than the identification of the correct additive geometry. The geometry is $\mathsf{[A]}$; the self-adjoint operator and the arithmetic clock stay $\mathsf{[C]}$ (\hyperlink{stmt:8-5}{Conjecture~8.5}).

================================================================================
PART 3 — NEW REFERENCES (merge into "## References", alphabetical/contextual order)
================================================================================

Krein, M. G. (1947–1955). *On the theory of entire functions of exponential type; and the continual analogue of the moment problem and the spectral theory of canonical (string) systems.* Izv. Akad. Nauk SSSR Ser. Mat. (The canonical/Hamiltonian system and its inverse spectral theory; \hyperref[sec:8-3]{§8.3}.)

de Branges, L. (1968). *Hilbert Spaces of Entire Functions.* Prentice-Hall, Englewood Cliffs, N.J. (Hermite–Biehler associates, de Branges spaces, and the canonical-system positivity used in \hyperref[sec:8-3]{§8.3}.)

Rodgers, B., Tao, T. (2020). *The de Bruijn–Newman constant is non-negative.* Forum of Mathematics, Pi **8**, e6. DOI 10.1017/fmp.2020.6. (The non-circular partial: $\Lambda\ge0$, hence the heat-smoothed clock is provably monotone for $t>\Lambda$; \hyperref[sec:8-3]{§8.3}, \hyperlink{stmt:8-7}{Proposition~8.7}.)

--- OPTIONAL companion-note reference (only if the paper cites in-house Notes; T24 + the metaplectic Note are already program-internal) ---

Murillo Montero, L. (2026). *The Monotone-Metric Apex: the Petz Fork and the Kubo–Mori Selection* (T24). Companion manuscript. (The additive/dually-flat monotone metric in which $H$ of \hyperref[sec:8-3]{§8.3} is assembled and the zeros are curvature currents; cited at $\mathsf{[A]}$.)
