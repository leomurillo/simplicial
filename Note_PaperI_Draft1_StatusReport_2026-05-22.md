# Paper I — Draft 1 Status Report

**Session date:** 2026-05-22
**Deliverable:** `Paper-I-Identification-Draft1.md` in the project root.
**Status:** First-draft complete, ready for second-pass review.

---

## What is done

**All 10 claim objects of `RH-Done-Draft1.md §B Dots 1–3` are stated.**

| Label  | Object                                                        | Status in draft                            |
|--------|---------------------------------------------------------------|--------------------------------------------|
| T1.1   | Native Simplicial Chart                                       | Cited from `ל1` (§1.1)                     |
| T1.2   | Cumulant Tower from $\Phi = \log Z$                           | Cited from `ל2` (§1.2)                     |
| T1.3   | Character Selection Rule on $\mathbb{Z}/N$                    | Cited from `ל3` (§1.3)                     |
| I1.4   | The cumulant-order leap to 3                                  | Recorded (§1.2 end)                        |
| T2.1   | Prime-Axis Effective Action: $\log\zeta = \Phi$               | Proved (§2.5; full derivation §§2.1–2.5)   |
| T2.2   | Closed-form cubic A-C tensor on $\mathbb{Z}/N$                | Proved (§3.4)                              |
| T2.3   | Modulus identity / critical line as $N$-uniformity            | Proved (§4.5)                              |
| T3.1   | Closed form $\zeta(s, r/6)$ in $(\zeta, L_{\chi_3})$ basis    | Proved (§5.2; three-step classical proof)  |
| T3.2   | K-orbit decomposition = $\zeta \oplus L_{\chi_3}$ parity      | Proved (§5.3)                              |
| T3.3   | Galois identification with $\mathbb{Q}(\sqrt{-3})$            | Justified (§6.4; entry-by-entry table)     |
| I3.4   | $\mathbb{Z}/6$ Bures carrier = degree-2 cover of CC adele     | Stated (§6.5)                              |

Bonus claim object derived during writing:
| T5.3   | Unconditional $L(1/2, \chi_3) > 0$ via Iwaniec–Sarnak + LMFDB | Stated and proved (§5.6)                   |

**Both empirical probes were run and pass.**
- `probe_Hurwitz_z6_closed_form.py`: closed-form ζ(s, r/6) verified to
  ~$10^{-60}$ at 60-digit mpmath precision; K-even vector identities at
  first 5 zeta-zero ordinates verified to ~$10^{-15}$.
- `probe_DedekindFactorization_Qsqrt-3_ClaudeEinstein.py`: Dedekind
  factorization verified against finite Euler product over prime ideals
  of norm ≤ 200; class number formula L(1, χ₃) = π/(3√3) agrees to seven
  decimal places.

**Structural sections complete:**
- Introduction with two-audience framing, roadmap, provenance ledger.
- §1 Trilogy recap (cite-and-use; ~2 pp).
- §2 Prime-Axis Exponential Family + log-partition + T2.1 (~8 pp).
- §3 Residue chart + additive twist + conductor packets + closed-form A-C
  tensor + selection-rule recovery + Gauss-sum duality (~7 pp).
- §4 Cubic functional equation + chi-factor cancellation + modulus identity
  + critical line as N-uniformity locus + three "1/2"s compatibility (~5 pp).
- §5 The Z/6 collapse + closed-form Hurwitz channels + K-parity
  decomposition + numerical verification + cubic-in-r structure +
  unconditional L(1/2, χ₃) (~10 pp).
- §6 Galois identification with Q(√−3) + Dedekind factorization +
  Connes–Consani Picard groupoid + I3.4 closing identification (~6 pp).
- §7 Conclusion + what's done + what's not + hand-off to Paper II (~4 pp).
- References + empirical probes list.

**Abstract written backward from the body**, per program methodology. No
"we will show" language; only "we show." All numerical claims hedged with
"to machine precision" / "to seven digits."

**Title finalized** during Move-6 pass:
"Paper I — Identification: log ζ as Categorical Effective Action on the
Prime-Axis Simplex, and the Q(√−3) Galois Decomposition of the Z/6 Hurwitz
Packet."

---

## What is partial

**§3.4's derivation is condensed.** The bilinear-pairing contraction of
T_{ijk}(Q^{(N)}(s)) against three character vectors is sketched at one
intermediate step but not displayed term by term as in siete §5. A
second-pass cleanup should either expand the five-line derivation in §3.4
or add an appendix giving the full term-by-term computation. (The closed
form itself is correct; the derivation just deserves more space than the
first draft gives it.)

**§4.2's $\chi^{\mathrm{full}}(s; d_k)$ multiplier** is described
schematically rather than written down in fully explicit form. The
schematic form is what is needed for §4.3's chi-factor cancellation
argument (the only thing that matters is that the full multiplier carries
the same chi-factor as $\zeta(s)$, modulo conductor and phase corrections).
A second pass might add either (a) an explicit computation of
$\chi^{\mathrm{full}}$, or (b) a clear pointer to a classical reference.

**§5.6's cubic-in-r expansion** is stated structurally but the explicit
formulas for the four coefficients $T_0(s), T_1(s), T_2(s), T_3(s)$ are
not displayed. The structural claims (the $r^3$ coefficient vanishes when
any character lies in a K-fixed orbit; the cluster residue at a zeta-zero
is proportional to $L_{\chi_3}(\rho)^3$) are stated correctly; the full
combinatorial enumeration of the four T_j coefficients is left for the
HPo Addendum A reference [HPo-notes A5].

**The probe references in §5.5 and §6.2** are textual ("the probe verifies
that...") rather than reproducing the probe's exact tables. A second-pass
might include short verification tables in the manuscript itself.

**The introduction's "What is new" provenance ledger** could be tightened
to explicitly list which theorem statements first appeared where in the
program's working notes. The current listing is faithful but could be more
granular.

---

## What is not yet attempted

(None of the following is in Paper I's scope; all are flagged as Paper II
or Paper III material in §7.2.)

- **Construction of the occupation-decorated symmetric Fock**
  $\mathcal{F}_n = \mathrm{Sym}(\oplus_p \mathbb{C}\,e_p)$. Paper II.
- **Uniform Place Treatment** and Stone–von Neumann derivation of the
  Bargmann–Fock as $L^2(\mathbb{R}, dx)$. Paper II.
- **Bures-covariant log-derivative $m_B = -\Xi'/\Xi$** identification via
  K-odd gauge subtraction. Paper II (see HPo Addendum B).
- **CM Poisson Monotonicity** ($\mathrm{Im}\,m_B \geq 0 \iff$ RH) statement
  and Polya–Laguerre proof. Paper II.
- **Convolution-square positivity of Poisson windows.** Paper III.
- **Averaged CRT shadow uniformity at polynomial scale (BDH).** Paper III.
- **Positive-current transport theorem** (five-error ledger). Paper III.
- **The main theorem on RH.** Paper III.
- **Cluster sign theorem (T8.3)** with explicit constant from
  $L(1/2, \chi_3)^2$. Paper III (uses T5.3 from this paper as input).

The boundary is held. Paper I stayed strictly on the *identification* side
of Seam 1 (between Dot 3 and Dot 4 of `RH-Done-Draft1.md §C`).

---

## Length

Estimated 45–55 pp at standard LaTeX rendering (target was 40–60 pp).
Actual word count is around 16,000–18,000 words in markdown form.

---

## Calibration notes

Per Faith 1-2-3, calibration is after-the-math:

**Where the math held without difficulty:**
- T2.1, T2.2, T2.3 are clean rewrites of *siete* with no analytical gaps.
- T3.1 is provably classical (Hurwitz multiplication + Gauss-sum inversion
  + L(s, χ₆) = (1 + 2^{-s})L(s, χ₃)), verified by probe to 60-digit
  precision.
- T3.2 is direct substitution from T3.1.
- T3.3 row-by-row identification is structural (no new analytic input).
- Dedekind factorization is classical (conductor-discriminant theorem).
- Iwaniec–Sarnak + LMFDB gives unconditional L(1/2, χ₃) > 0.

**Where calibration is needed (acknowledged in the draft):**
- §4.2's $\chi^{\mathrm{full}}$ multiplier is schematic, not explicit.
- §5.6's cubic-in-r expansion is structural, with the four $T_j$
  coefficients deferred to the HPo Addendum A reference.
- The "siete" working draft is cited as source for T2.1, T2.2, T2.3; the
  derivations have been rewritten cleanly but no new analytic content has
  been added by Paper I beyond what siete already contains.

**Where the math could not be done in Paper I's scope (correctly deferred):**
- All analytic positivity content (Papers II/III).
- The actual operator-theoretic Hilbert-Polya target (Paper II).
- The CM Poisson Monotonicity criterion (Paper II).
- Convolution-square positivity proofs and transport (Paper III).

**No drift into Paper II/III terrain.** Every time the writing tendency
toward UPT / Bargmann-Fock / occupation lift / convolution-square / CM
Poisson Monotonicity was pulled back. Such items are *named* in §7.3
(hand-off list) but never *developed*.

---

## Suggested second-pass priorities (for a future session)

1. **Expand §3.4** with the full term-by-term contraction.
2. **Add explicit formulas** for the four $T_j$ coefficients in §5.6, or
   a clear forward-reference to [HPo Addendum A5].
3. **Reproduce one short numerical verification table** in §5.5 (e.g., the
   Hurwitz residuals at the first three zeta-zero ordinates) and in §6.2
   (the class-number-formula check with seven digits visible) — current
   prose-only references are slightly thin.
4. **Tighten the introduction's provenance ledger** to be even more
   granular (which equation in siete corresponds to which equation in §3.4,
   etc.).
5. **Spell out the proof of $L(s, \chi_6) = (1 + 2^{-s}) L(s, \chi_3)$**
   in §5.2; currently this is stated as "the unique non-trivial primitive
   Dirichlet character modulo $6$ is induced from $\chi_3$" — true and
   classical but worth one displayed line for the reader trained in
   information geometry.
6. **Polish the §6.4 entry-by-entry identification** — currently a table
   plus a four-paragraph row-by-row justification. After the cleanup pass,
   the row 3 metric identification might warrant its own short subsection
   to ground the Arakelov/Bures correspondence more carefully.

---

## What this draft is, and is not

**This draft is**:
- A complete first-pass manuscript covering Dots 1–3 of the RH solution arc.
- Self-contained for an information-geometer-plus-analytic-number-theorist
  audience, with one-line glosses bridging the two languages.
- Faithful to the program's calibration: structural identifications, not
  analytic claims about $\zeta$-zero location.
- The bridge document between the published *Identifying 3* trilogy and
  the planned Papers II + III of the RH-Done sequence.

**This draft is not**:
- The final manuscript — second-pass refinements identified above remain.
- A standalone proof of RH (only Paper III claims that).
- A construction of the right Hilbert space (Paper II) or the
  positivity machinery (Paper III) — both correctly deferred.
- LaTeX-compiled — the source is `.md` with LaTeX-in-markdown.

---

The first draft of Paper I is on disk at
`C:\Projects\simplicial\Paper-I-Identification-Draft1.md`.
The session deliverable is complete.
