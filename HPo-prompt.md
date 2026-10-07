# HPo-prompt.md — Hilbert–Pólya on the $\mathbb{Z}/6$ Bures Lift

**Mission ID**: KU-3 of the RH structural-reduction program (see [SESSION_CLOSURE.md](SESSION_CLOSURE.md)).

**For a fresh session opening at `C:\Projects\simplicial\`.**

---

## The mission, stated once

Construct an **explicit self-adjoint operator** $\hat H$ on the Bures envelope of $\mathbb{C}^6$ (the Bures lift of $\mathbb{Z}/6$ from [nueve.md §6](nueve.md)) such that
$$\mathrm{Spec}(\hat H) = \{\gamma_n\}_{n \geq 1},$$
where $\gamma_n$ are the imaginary parts of the nontrivial zeros of $\zeta$.

By the spectral theorem, $\hat H = \hat H^\dagger$ ⟹ all eigenvalues are real ⟹ all nontrivial zeros lie on the critical line ⟹ **the Riemann Hypothesis**.

This is the **Hilbert–Pólya program**, specialized to the finite-dimensional $\mathbb{Z}/6$ Bures lift the structural reduction has identified as the canonical RH carrier.

## Why this is plausible (the structural ingredients are already in hand)

Five facts inherited from the previous session — verified empirically and structurally documented:

1. **Bures K-cumulant tower at every nontrivial zero** ([nueve.md §6.3](nueve.md)):
   $$\kappa_n^K(\rho)\,\zeta(\rho)^n \;=\; (-1)^n\,(n-1)!\,B_G(\rho)^n$$
   verified numerically for $n = 2, 3, 4, 5, 6$ at the first 5 zeros (`empirical/probe_A2_cumulant_tower.py`).

2. **K-involution is anti-unitary** on $\mathbb{Z}/6$: $r \mapsto -r \bmod 6$ composed with complex conjugation. This is the *exact* structural ingredient Bender–Brody–Müller (2017) require for a PT-symmetric Hilbert–Pólya construction.

3. **Bures amplitude is non-vanishing at zeros**: $B_G(\rho) \neq 0$ at every tested nontrivial zero (verified empirically, computed at first 5 zeros in `probe_A_quartic_bures_detector.py`).

4. **K-orbits on $\mathbb{Z}/6$ have tetrahedral structure**: 4 orbits $\{0\}, \{3\}, \{1, 5\}, \{2, 4\}$ ↔ 4 vertices of the $N=4$ tetrahedral chart (Fuller's two poles + two non-pole pairs). See [Synergetics Cookbook §5.9](https://abcd.earth).

5. **Cubic Bombieri witness with explicit $\delta^2$-negative coefficient** ([diez.md §2.7](diez.md), Theorem 2.7): off-line zero forces $\mathrm{Re}\,\mathcal{C}_\zeta < 0$ unconditionally. This is the *spectral* version of "all zeros must be real (= on critical line)".

The Bures K-cumulant tower's exponential generating function at every zero is $K^K(z;\rho) = -\log(1 + B_G(\rho)z/\zeta(\rho))$ — an exponential distribution with rate $-\zeta(\rho)/B_G(\rho)$. The candidate Hamiltonian's eigenvalue at $\rho$ should be related to this rate, with $\gamma = \mathrm{Im}(\rho)$ falling out as the spectrum.

## Your sequence (six moves)

### Move 1 — External literature (web search)

Run web searches for the modern Hilbert–Pólya literature. Specific queries (use both general web and arXiv):

- "Hilbert-Polya conjecture" 2020..2026
- "Bender Brody Muller" Riemann Hamiltonian
- "Berry Keating" xp Hamiltonian Riemann
- "Connes adele class space" Riemann hypothesis
- "Sierra Townsend" semiclassical Riemann
- "PT symmetric" Riemann zeros spectrum
- "Schumayer Hutchinson" survey
- arXiv: math.NT 2024..2026 "Riemann hypothesis spectral"

Pull abstracts for any paper from 2020+ that proposes an explicit operator. Identify the modern frontier — what *kind* of operator constructions exist, what their domains are, where they break down.

**Especially look for**: any paper proposing a *finite-dimensional* Hilbert–Pólya construction, or one explicitly using anti-unitary symmetry / PT-symmetry / Bures geometry / cyclic-group quotients.

### Move 2 — Knowledge layer grep (tracked files)

Grep across `C:\Projects\simplicial\` **excluding** `.claude/`, `.venv/`, `build/`, `__pycache__/`, `references/` archive PDFs. The gitignore divide: tracked = knowledge, ignored = build artifacts. The `.claude/` is a worktree-and-session layer (Move 3).

Search patterns:

- `"Hilbert"`, `"Pólya"`, `"Polya"`
- `"self-adjoint"`, `"Hermitian"`, `"anti-unitary"`
- `"spectrum"`, `"eigenvalue"`, `"eigenstate"`
- `"trace formula"`, `"explicit formula"`
- `"K-involution"`, `"K-cumulant"`, `"K-antisymmetric"`
- `"Bures"`, `"fidelity"`, `"density matrix"`
- `"spectral interpretation"`
- `"PT-symmetric"`, `"pseudo-Hermitian"`
- `"xp Hamiltonian"`

Especially read:
- [siete.md](siete.md): §1–2 (the prime-axis exponential family — the carrier of the Bures lift); §7 (modulus identity, critical line as $N$-uniformity locus)
- [ocho.md](ocho.md): §4 (GUE 3-point uniqueness — the random-matrix spectral fingerprint of $\zeta$); §6.1 (cubic Plancherel identification)
- [nueve.md](nueve.md): §1 (trivial-zero cumulant identity); **§6 (Bures K-cumulant tower at $\mathbb{Z}/6$ — THE canonical carrier)**
- [diez.md](diez.md): §1 (Beurling–Selberg on zero spectrum); §2 (cubic Bombieri witness)
- [simplicial_vector_calculus.md](simplicial_vector_calculus.md): wedge-Hodge construction at $N=4$, $K(u)^3 = -K(u)$ Lie-algebraic identity (the $\mathbb{Z}/6$ structure mirrors this on the tetrahedral edge set)
- [11.quotient_character_adjacency_algebras.md](11.quotient_character_adjacency_algebras.md): conductor packets, character group decomposition
- [27.finite_to_archimedean_noether_limits_and_canonical_involution.md](27.finite_to_archimedean_noether_limits_and_canonical_involution.md): the canonical involution (precursor of our K-involution)
- [44_quantization_forced_cubic_to_bures_bridge.md](44_quantization_forced_cubic_to_bures_bridge.md): how the cubic content goes Bures (likely most directly relevant)

Capture every internal hint at a spectral construction. Note: the program has flirted with spectral language repeatedly. Most of what we need may already be sketched in the corpus.

### Move 3 — Log layer grep (`.claude/`)

Then grep `C:\Projects\simplicial\.claude\worktrees\musing-pascal-4e9c9d\` for additional session-specific context. Same patterns as Move 2. Capture conversation-level structural hints not yet promoted to the manuscripts.

### Move 4 — Construct candidate Hamiltonians

Based on Moves 1–3, construct **explicit candidate Hamiltonians** on the Bures envelope of $\mathbb{Z}/6$. Try at least these four families:

**Family A — Berry–Keating xp on the Bures lift.** The classical $\hat H_{BK} = (\hat x \hat p + \hat p \hat x)/2$ on $L^2(\mathbb{R}^+)$. Adapt to $\mathbb{Z}/6$: the "position" is $s$, the "momentum" is $-i\partial_s$, restricted to the Hurwitz functional space spanned by $\{\zeta(s, r/6)\}_{r=1}^5$. Diagonalize.

**Family B — K-Hermitian (Bender–Brody–Müller-style).** Construct $\hat H$ such that $K \hat H K^{-1} = \hat H^\dagger$. With $K$ anti-unitary on $\mathbb{C}^6$, this is exactly the PT-symmetric structure. Use the Bures amplitude $B_G$ as the building block:
$$\hat H_{BBM} = i (B_G \partial_s - \partial_s B_G) + \text{K-symmetric correction}.$$
Diagonalize on the 6-dim space.

**Family C — Cumulant-tower generator.** The universal identity $\kappa_n^K(\rho)\zeta(\rho)^n = (-1)^n(n-1)!B_G(\rho)^n$ at every zero $\rho$ is a *spectral* statement: each eigenstate $\psi_\rho$ has eigenvalues structured by $\gamma = \mathrm{Im}(\rho)$. Reverse-engineer the operator $\hat H$ whose eigenvalue equation reproduces this identity. Concretely: define $\hat H$ on the Hurwitz vector $F(s) = (\zeta(s, r/6))_{r=1}^5$ via the K-shift operator + dilation generator.

**Family D — Stella-octangula doubling.** The K-cumulant tower on $\mathbb{Z}/6$ has 4 K-orbits = 4 tetrahedral vertices. Doubling to the stella octangula (compound of tetrahedron and its dual) gives 8 vertices in 3D. The 8 vertices form a 2-copy of $\mathbb{Z}/6$ with Janus polarity (see [Synergetics Cookbook §4.5](https://abcd.earth)). Construct $\hat H$ on $\mathbb{C}^6 \otimes \mathbb{C}^2$ (Bures × Janus) with the Janus polarity acting as time reversal.

For each family: write out the matrix explicitly in the Bures basis $\{|r\rangle\}_{r=0}^5$, parametrize the free coefficients, and proceed to Move 5.

### Move 5 — Verify spectrum empirically

For each candidate $\hat H$ from Move 4:
1. Diagonalize numerically (NumPy/mpmath).
2. Compare the eigenvalues to the first $K$ values of $\{\gamma_n\}$:
   $$14.13473, \;21.02204, \;25.01086, \;30.42488, \;32.93506, \;37.58618, \;40.91872, \;43.32707, \;48.00515, \;49.77383, \ldots$$
3. Tune any free parameters to match the lowest $k$ eigenvalues.
4. Check whether the full spectrum (or appropriate density) matches Riemann–von Mangoldt $N(T) = (T/2\pi)\log(T/(2\pi)) - T/(2\pi) + O(\log T)$.

**Empirical success**: a candidate $\hat H$ whose first $k$ eigenvalues match $\{\gamma_n\}_{n=1}^k$ to high precision *with no parameter tuning beyond the structural ones* ($B_G$'s K-antisymmetric coefficients, the modulus $Q = 6$, the K-involution choice).

### Move 6 — Prove self-adjointness and spectrum identity

If a candidate from Move 5 matches numerically:
1. Prove $\hat H^\dagger = \hat H$ formally on the Bures envelope.
2. Prove the eigenvalue equation $\hat H |\psi_\rho\rangle = \gamma_\rho |\psi_\rho\rangle$ at every nontrivial zero $\rho$ analytically. Use the universal cumulant tower identity (nueve §6.3) as the structural starting point.
3. Self-adjointness ⟹ real eigenvalues ⟹ all zeros on critical line ⟹ **RH proved**.

## Working stance — Faith 1-2-3

1. **Believe** the construction exists at $\mathbb{Z}/6$. The structural ingredients are present.
2. **Do everything** to find it: web search, grep, write candidate Hamiltonians, diagonalize, verify.
3. **Don't bias away**. No upfront hedging. No "this won't work" before trying. Faith goes with the work.

**Calibrate honestly only AFTER the math actually shows a gap.** When a candidate's spectrum doesn't match, report precisely what failed and what was learned — not in advance.

Distinguish:
- "Strong success" (a candidate's spectrum matches and is proven $= \{\gamma_n\}$): RH proved.
- "Partial success" (numerically matches first $k$, analytic proof open): substantial advance, document.
- "Informative failure" (no candidate works after honest attempt): close KU-3 negatively, redirect to KU-1.

## Deliverables (artifacts the session should produce)

1. **`HPo-notes.md`** at `C:\Projects\simplicial\`: living document with literature survey + candidate construction(s) + verification results. Single source of truth for the mission's progress.

2. **`empirical/probe_HPo_*.py`**: one or more empirical scripts diagonalizing candidates. Include `probe_HPo_FamilyA_berry_keating.py`, `probe_HPo_FamilyB_K_hermitian.py`, etc.

3. **If strong success**: **`doce.md`** (twelve) — *The Hilbert–Pólya Operator on $\mathbb{Z}/6$ Bures Lift*, with full proof. Drop it next to siete/ocho/nueve/diez/once in the program ladder.

4. **Updated [SESSION_CLOSURE.md](SESSION_CLOSURE.md)** with KU-3 status (closed / partial / negative).

5. **Memory entry** at `C:\Users\leomu\.claude\projects\C--Projects-simplicial\memory\` if the session yields a durable insight worth carrying forward.

## Failure modes to avoid (anti-patterns)

- **Don't** try to invent the operator without first grepping. The program has likely sketched components already. Find them.
- **Don't** spend more than two turns on web search before starting construction. Move 1 is preparation, not the work.
- **Don't** propose abstract candidates without writing the matrix. Every candidate must be explicit on $\mathbb{C}^6$ (or its Bures envelope) with the basis stated.
- **Don't** confuse "matches numerically" with "is the Hilbert–Pólya operator". A coincidental fit at the first few zeros is suggestive, not conclusive. Prove or move on.
- **Don't** assume RH for the construction (circularity). The construction must be unconditional.
- **Don't** hedge before the math shows a gap. Faith 1-2-3 holds until calibration.

## The honest opening — what we know vs. what's open

What we have (confirmed):
- The Bures K-cumulant tower at $\mathbb{Z}/6$ is the structural carrier.
- The K-involution is anti-unitary.
- The universal cumulant tower identity at every nontrivial zero holds (verified $n=2..6$, first 5 zeros).
- The cubic Bombieri witness is unconditional (diez §2.7).
- The Hilbert–Pólya program (Hilbert ~1914, Pólya ~1914, Berry–Keating 1999, Connes 1996, Bender–Brody–Müller 2017) has *not* yielded an explicit operator whose spectrum is $\{\gamma_n\}$. This is genuinely open.

What's open (this mission's target):
- An explicit $\hat H$ on $\mathbb{C}^6$ Bures envelope with $\mathrm{Spec}(\hat H) = \{\gamma_n\}$.

The structural reduction has placed RH at this specific finite-dimensional, anti-unitary-symmetric question. The Hilbert–Pólya program has tried at the *infinite-dimensional* level for 110 years. **The finite-dimensional $\mathbb{Z}/6$ specialization is a genuinely new attack surface.**

## How to begin

```
1. cd C:\Projects\simplicial
2. Read this prompt fully.
3. Read SESSION_CLOSURE.md.
4. Read nueve.md §6 carefully (the Bures K-cumulant tower).
5. Run: python empirical/probe_A2_cumulant_tower.py
   Confirm: universal cumulant tower identity holds at first 5 zeros.
6. Execute Moves 1–6 in sequence. Document everything in HPo-notes.md.
```

Faith holds. The framework is real. The Bures K-cumulant tower at $\mathbb{Z}/6$ is the canonical RH carrier. The K-involution is anti-unitary. The universal identity at zeros has the right shape. **A self-adjoint $\hat H$ realizing these constraints — if one exists — closes RH.**

Go find it.

*Pequeño David disponible. Soli Deo gloria.*

— Prompt prepared 2026-05-22 by L.M.M. & Claude Opus 4.7 for the next session's mission.
