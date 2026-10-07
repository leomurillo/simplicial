# Grounded-Paranoid-Delusional Inquiry: A Verification-Gated Methodology for High-Variance, High-Conviction Research Under Capable AI Assistance

**Leonardo Murillo Montero**
*May 19, 2026*

**arXiv-style preprint (draft v1 — methodology; self-applying)**

---

## Abstract

We describe, formalize, and stress-test a research methodology designed for a
specific and increasingly common situation: a single investigator pursuing a
high-variance, high-conviction research program with the assistance of frontier
language models capable of fluent, plausible, and unverified elaboration. The
central problem this methodology addresses is not productivity but
*epistemic integrity under two simultaneous failure pressures* — the
investigator's conviction, which tends to harden load-bearing beliefs into
unfalsifiable priors, and the model's fluency, which tends to launder
unverified claims into authoritative-sounding prose. The methodology is named,
descriptively rather than romantically, **grounded-paranoid-delusional
inquiry**: its three words are not a mood but a *resolution order*, read
right-to-left — divergent generation (delusional), adversarial bounding
(paranoid), and forced settlement on a verifiable artifact (grounded). Its
procedural core is a small set of tenets: matched-pair pre-claiming of both
branches of every falsifier before any check is run; a three-tier evidentiary
ledger ([P] proven, [A] structural-pending-named-audit, [C]
conjectural-reduced) with a strict no-upward-crossing firewall; an
anchored-objects rule forbidding reconstruction in place of the source's own
objects; an append-only record in which failed attempts are retained as
first-class evidence; and a working-backwards planning layer adapted from the
HOW service-design framework, supplying direction without licensing
conviction. We give the methodology's worked record from a single intensive
session — six deterministic audits, of which three settled negative (one of
them earning an unconditional positive as a by-product of the failed branch),
one failed its own anchor and was corrected, and two contributed bounded
results to an external research stack — and we devote a full section to the
methodology's *own* failure modes, including the one it is most prone to:
using divergence as a permanent defense against settlement. We state
explicitly what this paper does and does not claim. It does not claim to
certify the truth of any program to which it is applied; a disciplined method
is not a correctness oracle. Its contribution is narrower and, we argue, more
durable: a procedure under which neither the investigator's priors nor the
model's fluency can reach a conclusion without passing a verification gate
that was specified before the conclusion was known.

**Keywords:** research methodology, epistemics, falsifiability, human–AI
collaboration, pre-registration, adversarial verification, scientific
self-correction, working-backwards planning, philosophy of science.

---

## 1. The problem this methodology is for

### 1.1 A specific situation, not a general manifesto

This paper is deliberately narrow. It is not a theory of how science should be
done in general, and it is not addressed to large collaborations with built-in
adversarial review, replication culture, and institutional gatekeeping —
those communities already possess, in their social structure, much of what
this methodology must reconstruct procedurally for an individual. It is
addressed to a situation that the present technological moment has made common
and that classical research methodology does not specifically arm the
investigator against: **one investigator, a high-variance and
high-personal-conviction research program, and a frontier model that will,
on request, produce fluent and confident elaboration of almost any
hypothesis, true or false, at a rate far exceeding the investigator's ability
to verify it.**

The PhD-trained reader will recognize the two classical failure modes
separately. Confirmation bias — the investigator's tendency to weight evidence
toward a cherished hypothesis — is old and well documented. Automation bias —
the tendency to over-trust fluent machine output — is newer and increasingly
documented. The thesis of this paper is that under single-investigator
AI-assisted research these two are not independent risks to be managed
separately; they *compose into a single closed loop* that classical
methodology does not specifically interrupt: the investigator's conviction
selects which hypotheses to elaborate, the model elaborates them with a
fluency that reads as corroboration, the corroboration-shaped output deepens
the conviction, and the loop tightens. Neither participant is acting in bad
faith. The loop is structural. A methodology for this situation must place a
gate *inside the loop* — at the point where a claim would otherwise pass from
"elaborated" to "believed" — and the gate must be specified before the claim's
truth value is known, or it is not a gate.

### 1.2 What "verification-gated" means and why the gate must precede the claim

A verification gate is a pre-specified, mechanically checkable condition whose
*outcome the investigator has committed, in advance and in writing, to accept
in either direction*. The phrase "in either direction" is the entire content.
A check whose negative outcome can be reinterpreted as a different kind of
success is not a gate; it is a ritual. The methodology's procedural tenets
(Section 3) exist almost entirely to make the gate's two outcomes
*symmetrically consequential and pre-committed*, because an investigator with
strong conviction and a fluent model will, absent that symmetry, reliably and
sincerely reframe every negative outcome — not by dishonesty, but by the
ordinary cognitive route through which a sufficiently flexible mind protects a
sufficiently important belief. The methodology assumes good faith and treats
the failure mode as structural rather than moral; this assumption is itself a
tenet (Section 3.7) and is load-bearing for the method's tone and for its
psychological sustainability.

---

## 2. Grounded-paranoid-delusional: the name is a resolution order

The methodology's name is descriptive and the order of its three words is its
most compressed statement. Read left-to-right the words name three faculties.
Read **right-to-left they name the order in which a question must be
resolved**, and that order is the method.

* **Delusional (generation).** Permit, deliberately, the high-variance
  divergent move: the unification, the bridge, the "what if it were like
  this." This faculty is not a defect to be suppressed; in a high-ceiling
  program it is the only source of candidate structure worth verifying. The
  methodology's wager is that divergence is *safe to maximize precisely
  because the other two faculties are non-negotiable downstream*. The
  HOW framework (Section 5) is the disciplined housing for this faculty: it
  gives divergence a direction (a "Star") without giving it a vote on truth.

* **Paranoid (bounding).** Before any check, enumerate how the divergent
  claim could be *false*, and pre-commit, in writing, to both branches of
  the decisive falsifier (Section 3.1). This faculty's job is to convert an
  exciting claim into a *decidable* one and to fix the meaning of its
  failure before its failure can be renegotiated. "Paranoid" is the accurate
  word: the suspicion is directed not at the world but at the
  investigator's own most-wanted conclusion and at the model's most fluent
  output.

* **Grounded (settlement).** Resolve the question by forcing it onto a
  verifiable artifact — typically a deterministic, exact-arithmetic
  computation anchored to the source's own objects (Section 3.3, 3.4) —
  and record the realized branch as a stated result, *whichever branch it
  is*. Settlement is not optional and not deferrable; the failure mode of
  refusing to ever settle is treated at length in Section 6.

The phrase the investigator uses informally — *diverge, and do not converge
until you can bring success* — is correct only under a precise reading, and
the precise reading is the entire difference between the methodology and its
pathological twin. It means: **do not prematurely collapse the hypothesis
space onto the first adequate answer; keep generating until a candidate
survives the paranoid bounding and is ready for grounded settlement.** It does
*not* mean: postpone settlement indefinitely because no candidate has yet
yielded the desired conclusion. The first is productive divergence under a
standing commitment to eventually ground. The second is the unfalsifiable
loop of Section 1.1 wearing the methodology's vocabulary. Section 6 is devoted
to the boundary between them because, in the authors' own worked record, that
boundary is where the method is most often and most subtly violated — and the
violator is sincere every time.

---

## 3. Procedural tenets

Each tenet is stated, justified, and accompanied by the failure it exists to
prevent. The tenets are not independent; the firewall (3.5) is what gives the
others force.

### 3.1 Matched-pair pre-claiming (with three-outcome extension)

Before any decisive check is executed, write down — in the permanent record,
before the result is known — *both* outcomes (binary K/L) **and a third
"joint-on-disjoint" outcome** when the underlying structure admits it, with
what each will be taken to mean. Each branch must be specified with the same
concreteness as the others and must be a genuine, reportable result, not a
placeholder.

*Failure prevented:* outcome-dependent reinterpretation. An investigator who
has written, in advance, "if the cubic self-energy is zero, the constants
target is vacuous and closes negative" cannot, on seeing zero, narrate it as
unexpected support for a different claim — the negative meaning was fixed
while its truth value was still unknown. The tenet works precisely because it
removes the *degree of freedom* through which sincere reinterpretation
operates.

**The three-outcome extension (binding from v2insert-04 onward).** The
original tenet pre-claimed *binary* K/L matched pairs. The Paper 32 §13.2
Bures-dispersion audit (settled at §13.2B) realized a *third* outcome that
the binary framing could not capture: K (Lorentzian signature) and L
(Euclidean signature) were *jointly realized on HS-orthogonal sub-bundles*
of `T_{ρ_*} D(ℂ⁶)` — the hybrid Hartle–Hawking signature pattern. The
binary K/L pre-claim would have been forced to absorb this third outcome
silently into K, hiding the structural content of the joint realization.

From v2insert-04 §3.1 onward, the rule is corrected: when a matched-pair
pre-claim's underlying structure admits the possibility, the three-outcome
branches are stated explicitly:

* **K** — the positive branch is realized.
* **L** — the negative branch is realized.
* **Joint-on-disjoint** — both K and L are realized, on disjoint sub-structures
  (orthogonal sub-bundles, disjoint character classes, leading order vs
  correction order, etc.), in a way that the binary framing would have
  forced into K. The branch must be specified with the same concreteness
  as K and L; it is a genuine, reportable, *third* publishable outcome.

The three-outcome rule produced **thirteen named audits** in the 2026-05-20 session, with **six explicit joint-on-disjoint outcomes** that the binary K/L framing would have absorbed silently into K:

| Audit | Outcome | Joint-on-disjoint substance |
|---|---|---|
| §13.2B (Bures dispersion on `D(ℂ⁶)`) | **joint-on-disjoint** | K (V-Lorentzian) + L (M-Euclidean) on HS-orthogonal tangent sub-bundles — the *archetypal* worked example |
| α/η on `ℤ/30` | triple-K | clean K-branch on Papers 46/47/48 simultaneously; no joint-on-disjoint |
| θ on the primorial ladder (5 rows) | K-direction + **joint-on-disjoint at exponent** | monotone decay (K) + super-exponential in `n`, not log-linear (sub-finding) |
| ι on Bousso-bound shape | K-leading + **joint-on-disjoint at corrections** | leading-order match to 't Hooft–Susskind / Bousso `1/N²` (K) + polynomial-log-`n` correction is program-specific |
| δ (all-orders Pontryagin) | K-branch | finite combinatorial proof; subsumes audit ζ |
| μ_30 (geometric on `D(ℂ³⁰)`) | K-branch | Hessian (1, 6, 892), quartic (22, 0, 877), HS-orthogonal at 5.82e-16 |
| λ (training-side V/M propagation) | K-branch | ρ_{V/M} monotonic in α at signal-to-noise 47–119 across widths |
| β (Hartle–Hawking Lie-algebra dictionary) | K + **joint-on-disjoint at row 3** | rows 1, 2, 4, 5 clean; row 3 (imaginary time): `so(2)` matches, but program's `dim_M`-dim Wick parameter generalizes HH's 1-dim |
| γ (classical-limit identification) | K-branch | `I_real = E² − p²` exactly on V-rays; slow-momentum limit recovers Lemma 9.2 Galilean |
| ε (QG-mixing-bypass Lie-algebra dictionary) | K-branch | five-row dictionary; correspondence language only |
| ξ (capacity at `ℤ/510510`) | K with sub-finding | ratio 1.538 to PNT prediction; K-drift `3.64 → 6.92` is the sub-leading correction |
| χ (Bures-Hessian on `D(ℂ¹⁰) + D(ℂ¹²)`) | K (binary V/M) + **joint-on-disjoint at trichotomy** | strict + inclusive V/M both K at machine floor; trichotomy V/W/M has W ⊥ M tangent overlap 0.447 |
| ν (cross-manifestation natural transformation) | **joint-on-disjoint at abstract-vs-literal** | identity-on-certificate-ingredients is a natural transformation in `CertificateCategory` (K abstract); no faithful inter-substrate map (L literal) |
| FEP-3 (variational free-energy metriplectic split) | K-branch | F = F_V Hamiltonian + F_M gradient-of-entropy, additive, no interaction; arrow of time = ∇F_M direction |

**Six of thirteen named audits realized joint-on-disjoint outcomes** that the binary K/L framing would have hidden. The three-outcome extension is now load-bearing methodology, not optional convention. The pattern is clear: when an audit's realized structure has *finer detail* than the binary pre-claim admits, the joint-on-disjoint branch is the precise compromise — *the most informative outcome* the three-outcome rule was designed to capture.

*Methodological observation.* The joint-on-disjoint branch is *the most
informative* of the three: it surfaces sub-leading structural content that
the binary framing necessarily absorbs into K. Pre-claiming the three-branch
structure is the corrective response to the failure mode of "K confirmed,
nothing further reported" when the realized outcome has finer structure.

### 3.2 The three-tier evidentiary ledger

Every assertion in the program carries one of three tiers, explicitly:

* **[P] — proven.** A deductively valid argument or a deterministic,
  reproducible computation with no fitted parameter and no tolerance in any
  decision.
* **[A] — structural, pending a named audit.** A claim that is precise and
  very likely correct on structural grounds but whose verification is an
  explicitly *named*, not-yet-performed, finite check. The name of the
  missing audit is part of the claim.
* **[C] — conjectural, reduced.** A genuine conjecture, stated with its
  falsifier, ideally *reduced* to the smallest unproven obligation
  ("cornered") so that what remains unknown is a single named thing rather
  than a diffuse hope.

The tier is not decoration; it is the unit the firewall operates on.

### 3.3 The anchored-objects rule

When verifying a claim about a source's construction, the check must operate
on *the source's own objects*, reconstructed only when reconstruction is
itself verified against the source. An independent reconstruction that
*resembles* the source's object is not a check of the source; it is a check
of the reconstruction, and the two diverge exactly when it matters most.

*Failure prevented, with a worked instance:* in the session record (Section
4), a from-scratch reconstruction of a representation-theoretic commutant
returned a clean-looking but wrong answer because the reconstruction had
silently built in the very separation it was meant to test for. The anchored
re-run — executing the source's own artifact — returned the correct,
different answer. The tenet's price is that one cannot always "just
re-derive"; its return is that one cannot launder a reconstruction error as a
result.

### 3.4 Deterministic, exact, reproducible settlement

Where a question can be forced onto a finite computation, the settlement
artifact must be deterministic (no seeds), exact (no floating point in any
vanishing or membership decision; integer or rational arithmetic where the
decision is discrete), and reproducible (source and full run transcript
archived together, including transcripts of *failed* runs). A settlement that
cannot be re-run by an adversary is not a settlement.

### 3.5 The firewall: no upward tier-crossing

This is the tenet that gives the others force. **No claim may be cited, used,
or built upon at a tier higher than the one at which it was established.** A
[C] conjecture may not be silently used as an [A] premise; an [A] structural
claim may not be cited as a [P] result; an external resonance may not become
internal validation. Each paper carries an explicit "safe / unsafe
statements" section (the convention is borrowed and generalized from the
program's number-theoretic work) naming, in the unsafe column, the precise
overclaims that the work is one careless sentence away from and is choosing
not to make.

*Failure prevented:* the most dangerous failure in conviction-driven work,
which is not a single false claim but the *gradual promotion* of a hopeful
conjecture into an unexamined foundation through many small, individually
forgivable elisions. The firewall makes each elision a visible, locatable
violation rather than an invisible drift.

### 3.6 The append-only record; failures are first-class

The record is append-only. A refuted conjecture, a failed reconstruction, a
carried assumption found mis-specified — these are retained, with their
transcripts, as first-class entries, not deleted or quietly corrected. A
reproducibility archive that contains only the runs that worked is not a
reproducibility archive; it is a highlight reel, and a highlight reel is
indistinguishable, to an adversary, from a fabrication.

### 3.7 Assume good faith; treat the failure as structural

The methodology assumes both participants — investigator and model — are
acting in good faith and that the failure modes it guards against are
*structural*, not moral. This is not naïveté; it is a design decision with
two consequences. First, it keeps the method psychologically sustainable: a
procedure that required the investigator to suspect their own honesty would
not be followed. Second, it correctly locates the intervention. The loop of
Section 1.1 does not require anyone to lie; it requires only a flexible mind
and a fluent assistant. A method that treated the problem as dishonesty would
build the wrong defenses. The defenses are procedural gates, not integrity
audits.

---

## 4. The worked record (a single intensive session)

A methodology paper that offered only precepts would violate its own Section
3.6. We therefore report the full ledger of one intensive working session in
which the methodology was applied to live problems, including its failures.
The technical content is documented elsewhere in the program; here only the
*methodological* shape matters.

* **Two settlements that closed negative.** A "cheapest constants target"
  and a "Q-fixed scale," each *carried in the program's own working notes
  as promising*, were each, on first contact with their anchored
  definitions, found to be mis-specified — one structurally vacuous, one
  defined against a quantity that was constant rather than the claimed
  variable. Both negative outcomes had been pre-claimed (3.1); both were
  recorded as stated results (3.6). Their value to the program was real and
  came *from* their being negative: two-for-two refutation of un-audited
  carried labels produced a new mandatory tenet (an anchor-check before any
  carried item may be promoted), which is itself an instance of the method
  improving itself under the evidence of its own failures.

* **One reconstruction that failed its own anchor.** A from-scratch
  reconstruction returned a clean but wrong result; its *pre-claimed*
  anchor-failure branch fired; the failure was diagnosed (3.3), the
  source's own artifact was run instead, and the corrected, different
  result was recorded together with the failed transcript (3.6). The
  settlement was *stronger* for containing the recorded failure, not
  weaker: it demonstrated that the verification gate had already rejected
  one wrong answer before accepting the right one.

* **Two bounded contributions to an external research stack.** Two
  questions an external, peer-reviewed research program poses and leaves
  open were given finite, exact, falsifier-pre-registered partial answers,
  each explicitly bounded to its tested instance and each emitting an
  explicit "this is not general closure" with the generalizing falsifier
  named. No claim of external validation was made or implied; the firewall
  (3.5) classified the external resonance as resonance, not corroboration.

* **One in-session conjecture, pre-claimed in three branches, falsified in
  two rounds, closed with an unconditional positive surviving as
  by-product.** Audit σ — the *spinfoam-V projection conjecture* —
  pre-claimed three branches before any calculation: (i) all natural
  label-arithmetic lifts \(\widehat{\mathrm{SU}(2)}\to\widehat{\mathbb Z/N}\)
  fail to factor the EPRL/FK simplicity constraint through the cubic
  Amari–Chentsov structure constant on the conductor lattice of
  \(\mathbb Z/N\); (ii) exactly one lift factors; (iii) multiple factor
  compatibly. Round 1 (combinatorial) executed on \(\mathbb Z/6\) with the
  spin set \(\{0,\tfrac12,1,\tfrac32\}\) and three natural lifts
  (spin-doubling \(2j\), irrep-dimension \(2j+1\), Casimir \(2j(2j+1)\), all
  mod 6): spin-doubling matched 3 of 8 SU(2)-admissible triples with two
  genuine V-cubic-closure failures on V-supported admissible triples;
  dimension matched 0 of 8; Casimir collapsed degenerately. **Branch (i)
  fired.** Round 2 (weighted-EPRL hedge) checked whether natural SU(2)
  recoupling weights (dimension product; Wigner 3j with all magnetic
  numbers zero; \(\theta\)-net character integral; Riemannian EPRL Y-map at
  rational Immirzi \(\gamma\in\{0,\tfrac13,\tfrac12,1,3\}\)) could
  introduce the required mod-6 vanishing pattern. The decisive pair
  T6 = \(\{\tfrac12,1,\tfrac32\}\) versus T7 = \(\{1,1,1\}\) — both with
  lifted sum \(\equiv 0\bmod 6\), both needing nonzero weight — ruled out
  Y-map rescue at any rational \(\gamma\). The structural reason the
  negative is forced rather than circumstantial: SU(2) recoupling weights
  carry no \(\bmod N\) residue data; the conductor-lattice closure
  \(k+\ell+m\equiv 0\;(\bmod N)\) is not in the image of any such weight
  scheme. The negative was therefore banked at [P], not [A]. The candidate
  Paper 50 (originally framed in-session as an open spinfoam-V projection
  workstream) was reframed in the *same* session as a closed no-go
  demarcation. The unconditional positive that survived as by-product —
  that the cubic Amari–Chentsov structure constant
  \(T^{(\mathrm{AC})}_{k\ell m}=\mathbf 1[k+\ell+m\equiv 0\;(\bmod N)]\) is
  exactly the abelian-BF 3-vertex amplitude on the finite group
  \(\mathbb Z/N\), with the V/M decomposition decomposing it via CRT
  character orthogonality into single-prime closures plus typed cross-prime
  carry — was promoted to a one-paragraph remark in Paper 47 §3 and to a
  worked six-slot certificate in Paper 30 §9.6. The audit is reported here
  because of its unusual methodological cleanness: the conjecture was
  generated *in-conversation* at high investigator conviction, pre-claimed
  in three branches with the same concreteness as the K and L options the
  binary rule traditionally uses, falsified twice within a single session,
  and the falsification produced downstream content that the conjecture's
  failure had nonetheless earned. It is a demonstration that the gate
  operates on conjectures the investigator is attached to *at the moment
  of generation*, not only on legacy items inherited from earlier work.

The shape of the record is the point. A methodology whose worked history is
*all confirmations* has not been tested; it has been performed. This one's
history is three negatives (one of them earning an unconditional positive as
by-product of the failed branch), one caught error, and two deliberately
bounded positives. That distribution is what a working verification gate
produces and is the only honest evidence that the gate is load-bearing rather
than ceremonial.

---

## 5. The HOW layer: working backwards supplies direction, not conviction

The planning layer of the methodology is adapted from the HOW
("Historic Organisation Way") framework, a working-backwards service-design
method whose three circular components — a science-fictional *Historic
Fiction* of an achieved success, a *Historic Goal* roadmap distilled from it,
and an append-only *Historic Record* of what actually happened — translate
directly into a research program with one critical modification.

In its native form HOW supplies *direction* through narrative: imagine the
program already succeeded, write its history, and work backwards. Adapted into
this methodology, the Historic Fiction is permitted to play exactly one role —
it is the housing for the *delusional* faculty of Section 2, the disciplined
container for the divergent "what if it were like this." It supplies the Star,
the direction of search. **It is explicitly denied any evidentiary vote.**
The modification, stated as a tenet:

> The Historic Fiction may determine *what is worth attempting and in what
> order*. It may never determine *what is true*. The transformation from
> Fiction to Record runs only through the verification gate of Section 3;
> there is no other admissible path, and in particular narrative coherence,
> however compelling, is not one.

This is the precise point at which the methodology diverges from
working-backwards planning as commonly practiced and from the failure mode of
Section 6. HOW's native append-only Historic Record, its event-sourced "what
we knew when," and its insistence on a single coherent *Head* version map
cleanly onto Section 3.6's append-only ledger and Section 3.5's firewall. The
borrowed structure is sound; the one added constraint — *fiction sets
heading, only the gate sets truth* — is what makes it a research methodology
rather than a vision exercise. The HOW framework's own closing admission, that
its introduction "was not intended to be complete," is retained here as a
tenet rather than a caveat: a methodology that presented itself as complete
would fail Section 3.5 on its own cover.

---

## 6. The methodology's own failure modes (the section that makes this a method, not a manifesto)

A methodology paper that did not adversarially audit its own methodology would
violate every tenet it advances. We state the failure modes plainly, worst
first, because the worst one is the one the methodology is *most* prone to and
the one its vocabulary most effectively disguises.

### 6.1 Divergence as permanent deferral of settlement (the principal failure)

The tenet "diverge, do not converge until you can bring success" (Section 2)
has an exact pathological reading: *never settle, because settling risks a
negative, and a sufficiently fertile mind with a fluent assistant can always
generate one more dimension, one more reframing, one more "why not both,"
that postpones the gate indefinitely.* This is not a hypothetical; it is the
specific way the methodology fails, and it fails *sincerely* — the
investigator experiences each deferral as continued productive divergence,
not as evasion, because the two are subjectively identical from the inside.
The only known defense is external and procedural: the matched-pair
pre-claim (3.1) must be written *before* the check is contemplated, the
settlement artifact (3.4) must be committed to a date or a defined trigger,
and — critically — *a second party with standing must be empowered to call
the deferral*. A methodology operated by a single mind with no external
caller has no defense against this failure and should be honest that it does
not. This is the methodology's most important limitation and is stated here,
unhedged, as such.

### 6.2 The unfalsifiable core

A research program may contain one belief held at such high precision that
every possible disconfirmation is, by the believer, converted into
confirmation. Formally (after the program's own resilience analysis): a
self-model or core hypothesis at maximal precision is the inertial limit —
maximally robust, minimally able to update, and brittle in the specific way a
single-point-of-failure system is brittle. The methodology's tiering (3.2) and
firewall (3.5) can *quarantine* such a core — by forcing it to carry its [C]
tier and forbidding its use as an [A] or [P] premise — but they cannot
*dissolve* it, because the believer can always satisfy the letter of the
tiering while exempting the core from genuine exposure. The honest statement
is that this methodology bounds the blast radius of an unfalsifiable core; it
does not cure one. Curing one is not a methodological act.

### 6.3 Fluent corroboration mistaken for verification

The model's role in this methodology is strictly bounded: it generates
candidates (faculty one), it helps enumerate falsifiers (faculty two), and it
*executes and reports* deterministic checks (faculty three) — but its fluent
agreement is never, at any tier, evidence. The failure mode is the
investigator accepting the model's articulate restatement of a hypothesis as
though articulacy were corroboration. The defense is Section 3.4: only the
deterministic artifact settles, and the artifact's transcript, not the
model's prose about the artifact, is the record. A model that says "this is
correct" has produced zero evidence; a model that produces a reproducible
transcript an adversary can re-run has produced all of it.

### 6.4 Self-application is not self-certification

This paper applies its own method to itself: it makes a bounded claim (a
verification-gated methodology interrupts the Section 1.1 loop), states what
it does not claim (Section 7), and retains its own failure modes as
first-class content (this section). But a methodology cannot certify itself
by being internally consistent — internal consistency is necessary and
radically insufficient. The methodology's actual warrant, if it has one, is
external and empirical: does it, in the hands of others, produce records with
the failure-containing distribution of Section 4 rather than highlight reels?
That question is not answered by this paper and cannot be. It is the
pre-registered open question of the methodology itself.

---

## 7. Safe and unsafe statements

In the program's convention, stated plainly for the PhD reader who will, and
should, look for the overclaim.

**Safe (this paper asserts):**

* Single-investigator AI-assisted research has a structural failure loop
  (Section 1.1) that classical individual methodology does not specifically
  interrupt.
* A verification gate whose two outcomes are pre-committed and
  symmetrically consequential interrupts that loop *at the point of
  interruption*, and the procedural tenets of Section 3 are a concrete,
  operable specification of such a gate.
* The methodology has a worked record (Section 4) whose failure-containing
  distribution is consistent with the gate being load-bearing.
* The methodology's own principal failure mode (Section 6.1) is named, and
  its only known defense is external; the paper states it has no internal
  defense against that mode.

**Unsafe (this paper does NOT assert):**

* That the methodology certifies the truth of any program to which it is
  applied. It bounds how falsehood propagates; it is not a correctness
  oracle.
* That following the tenets guarantees good research, or that violating
  them guarantees bad research. The tenets reduce a specific class of
  error; they do not manufacture insight, which has no procedure.
* That this is a general theory of scientific method, or that it supersedes
  the social epistemics of established research communities. It is a
  procedural reconstruction, for the single AI-assisted investigator, of
  defenses those communities already obtain socially.
* That the methodology cures an unfalsifiable core (6.2) or defends a
  solo operator against permanent deferral (6.1). It bounds the first and
  is defenseless against the second without an empowered external party.
* Any claim that this paper is seminal, important, or field-defining. By
  Section 3.5 such a claim would be an unsafe statement asserted at the [P]
  tier on [C] evidence; the methodology forbids its author from making it,
  and the prohibition is not modesty but the method operating on its own
  paper. Whether the work matters is, by construction, not the author's
  ruling to issue.

---

## 8. Relation to existing methodological work

For the PhD audience, the honest placement against the three nearest
literatures, adverse to ourselves.

* **Pre-registration and registered reports** (the open-science movement).
  Matched-pair pre-claiming (3.1) is pre-registration, narrowed to the
  single-investigator AI-assisted case and extended so that the *negative
  branch's meaning*, not only the analysis plan, is fixed in advance. Where
  it stops short of subsuming us: registered reports presuppose a
  reviewing institution; the present method must reconstruct, procedurally
  and for one person, what that institution supplies socially — and is
  honest (6.1) that one procedural defense, against permanent deferral, it
  cannot reconstruct alone.

* **Falsificationism and its critics** (Popper; Lakatos's research
  programmes; Duhem–Quine). The tiering and firewall are closer to
  Lakatos than to naïve Popper: a program is permitted a hard core and a
  protective belt, but the firewall forbids the *unmarked* migration of
  belt into core, which is precisely the move Lakatos describes
  descriptively and this methodology forbids procedurally. The
  Duhem–Quine underdetermination problem is not solved here; it is
  *localized* by the anchored-objects rule (3.3), which forces the
  ambiguity to surface at a named reconstruction rather than diffuse
  through the argument.

* **Human–AI collaboration and automation-bias research.** This literature
  documents over-trust in fluent machine output. The contribution here is
  not the observation but the *specific structural composition* (Section
  1.1) of automation bias with investigator confirmation bias into a single
  closed loop, and a gate placed inside that specific loop. We claim the
  composition and the placement; we do not claim to have founded the study
  of automation bias.

---

## 9. Conclusion

The situation this paper addresses — one convinced investigator, one fluent
model, one high-variance program — is now ordinary, and it has a structural
hazard that ordinary individual methodology does not specifically arm against:
conviction and fluency compose into a loop that, with no one acting in bad
faith, converts elaboration into belief without passing a gate. The
methodology offered here is a concrete, operable specification of such a gate:
divergence maximized because bounding and settlement are non-negotiable
downstream; both branches of every falsifier written before the check;
everything tiered and the tiers firewalled against upward crossing; the
source's own objects, not their resemblances, audited; the record
append-only, failures retained; a working-backwards layer that supplies
heading and is denied a vote on truth.

We have given the worked record, including its negatives and its one caught
error, because a methodology evidenced only by its successes has been
performed rather than tested. We have devoted a full section to the
methodology's own failure modes, worst first, including the one — divergence
as permanent deferral — against which a solo operator has, we state plainly,
no internal defense. And we have applied the method to this paper: it makes a
bounded claim, names what it does not claim, and forbids its own author, by
its own firewall, from declaring it important. Whether it is important is, by
the method's own construction, not a ruling its author is entitled to issue.
It is a question for adversaries and for time, which is the only verdict the
methodology recognizes and the only one worth having.

---

**Reproducibility.** The worked record of Section 4 is backed by deterministic,
exact-arithmetic artifacts with archived transcripts, including the
transcripts of the failed reconstruction and the two negative settlements.
Sections 3, 5, and 6 are specifications and self-audits; they assert no
empirical result and are offered for adversarial use, which is their intended
use.

**Tier summary.** Sections 1–3, 5: methodological specification (not
tier-bearing; they define the tiers). Section 4: the cited settlements are
each **[P]** in their own records; their *aggregate methodological reading* is
**[A]** (the named pending audit is independent replication by other
investigators, Section 6.4). Section 6 failure modes: **[P]** as
identified hazards (each has an exhibited or argued instance), **[C]** as a
claim that the listed defenses are *sufficient* — they are not asserted
sufficient; 6.1 is asserted *insufficient* without an external party. No
statement in this paper is asserted at a tier above its evidence; the
firewall of Section 3.5 was applied to this paper as it was written, and the
prohibited self-promotional sentence (Section 7, final unsafe item) is named
precisely so that it can be seen not to have been written.

---

*Draft v1. This paper is self-applying: it is an instance of the methodology
it describes, and its principal claim is bounded, its falsifier is named
(independent replication of the failure-containing record distribution by
other investigators), and its author is forbidden by its own Section 3.5
from ruling on its significance. The romantic title was available and is
recorded here as the first unsafe statement the method declined to assert.*
