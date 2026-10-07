# RH-Done-Draft2-Feedback — Prompt for Processing External Feedback on Paper II

Processing external feedback on **Paper II "The Right Carrier"**.

Session opens at `C:\Projects\simplicial\`. You are the lead polymath
of the team. The most recent draft on disk is `Paper-II-RightCarrier-Draft2.md`
(if a Pass-1 refinement has been done) or `Paper-II-RightCarrier-Draft1.md`
(otherwise). External feedback has been provided to you, either inline
in this prompt or as a referenced `.md` file. Your job is to **make
the manuscript better from that feedback** — not to reply to the
feedback.

---

## The Mission, Stated Once

The user has handed you feedback (referee report, collaborator
comments, working-group notes, etc.) on Paper II. Your job is:

1. **Read the feedback carefully.** Identify what the feedback is
   actually saying — distinguish surface complaints from structural
   concerns.
2. **Triage** each piece of feedback into one of four categories
   (§3 below).
3. **Integrate the actionable feedback** into the manuscript.
4. **Calibrate honestly** about what was integrated, what was
   acknowledged-but-deferred, and what was rejected with reasoning.
5. **Do not reply to the feedback.** No "Dear Reviewer" letter, no
   point-by-point response document. The manuscript itself is the
   response.

Output: a refined manuscript `Paper-II-RightCarrier-DraftN+1.md`
(where $N$ is the current draft number) and a status note
`Note_PaperII_FeedbackPass_2026-MM-DD.md` documenting the triage.

---

## General Guidance — Feedback Processing Methodology

This section is general; it applies regardless of which paper is under
review. The Paper-II-specific section follows in §7 below.

### 1. The four triage categories

Every piece of feedback falls into one of these:

**(A) Substantive structural concern.** A claim is wrong, a proof has
a gap, an axiom is implausible, a citation is misattributed, or a
load-bearing identification is unjustified. *These must be addressed
in the manuscript.* Either fix the issue, or if it cannot be fixed in
the current draft, acknowledge it openly in a calibration paragraph.
**Do not paper over a structural concern.**

**(B) Substantive expositional improvement.** A passage is unclear,
a notation is non-standard, a missing intermediate step would help the
reader, a forward reference is brittle. *These should be integrated*
when the cost is moderate. If a structural rewrite would be needed,
defer with a note.

**(C) Style / preference / scope concern.** The reviewer prefers a
different framing, would like a different section ordering, wants more
historical context, wants less, prefers a different notation, etc.
*These should be considered but not automatically integrated.* The
manuscript serves its mission; reviewer preference is one input, not
the deciding vote. **Calibrate against the program's standards** —
those are the binding constraints. Acknowledge the reviewer's
preference, integrate when it strengthens the paper, defer when it
would weaken the structural argument.

**(D) Misreading or unaddressable.** The reviewer has misunderstood a
claim, is operating from a different framework, or has expectations
the paper does not aim to meet. *Do not change the manuscript in
response*; instead, **strengthen the relevant exposition** so that the
misreading is harder to make. The reviewer's error is a signal about
where the paper is unclear.

### 2. Triage discipline

For each piece of feedback, **write down the category** before acting.
A good rule: if you cannot decide between (A) and (C), it is almost
certainly (B) — a clarification is needed but the structural content
is fine. If you cannot decide between (A) and (D), re-read both the
feedback and the relevant manuscript passage carefully; the answer is
usually clear after a second read.

**Be especially careful with category (A).** A structural concern that
turns out to be a misreading (D) is common. But the converse — treating
a real (A) as a (D) — is the failure mode that destroys papers. When
in doubt, treat as (A) until you have proven to yourself that it is
(D).

### 3. The math comes first

The reviewer's emotional content is irrelevant; the structural content
of their critique is everything. A reviewer who is frustrated may have
the most valuable feedback; a reviewer who is congratulatory may have
missed the actual issues. **Focus on the math content of every
comment** and ignore the affect.

Specifically:
- "This is not rigorous enough" → identify the specific claim that
  feels not rigorous, evaluate whether the rigor is sufficient for the
  claim, fix if needed.
- "I don't see how this connects to X" → if X is in scope, expand the
  connection; if X is out of scope, sharpen the scope statement.
- "Why not do Y instead?" → if Y is structurally equivalent, mention
  Y in a remark; if Y is genuinely different, calibrate why the
  program's choice is what it is.
- "This is too long / too short" → length is a (C) concern unless
  there is a specific structural reason; in general, optimize for
  reader comprehension, not for an arbitrary length target.

### 4. What never to do

- **Never weaken a load-bearing claim to placate a reviewer.** If T4.1
  is correct, the paper says T4.1. If a reviewer disputes T4.1, either
  the reviewer is wrong (treat as A or D after careful re-read) or
  T4.1 needs strengthening (treat as A and fix). Never water it down
  to "T4.1 is plausible".
- **Never insert a defensive paragraph that explains why a reviewer's
  concern is invalid.** That belongs in a reply letter, not the
  manuscript. The manuscript should be self-standing.
- **Never let reviewer style preferences override the program's
  established style.** Paper I and II have a calibrated style; that
  style serves the program. Reviewer preferences for different style
  are (C) concerns and should not destabilize the program-wide
  consistency.
- **Never integrate feedback without understanding it.** If a comment
  is opaque, read it three times before acting. If still opaque, treat
  as (D) and strengthen the relevant exposition — but mark this as
  speculation in the status note.

### 5. What to always do

- **Always cite when feedback is integrated.** If the reviewer
  identified an error, fix it; the fix-itself is the response. Do not
  add a footnote saying "thanks to Reviewer X for noticing this" —
  acknowledgments belong in the acknowledgments section at the end of
  the paper if appropriate.
- **Always tighten exposition where the reviewer indicated
  confusion.** Even a (D) misreading-by-reviewer is a signal that
  someone could misread the same passage; sharpen.
- **Always preserve the program's scope.** Paper II is the carrier-
  construction phase, not the closure. Reviewer suggestions to fold
  in Paper III content are (C) concerns and should be deferred to
  Paper III.
- **Always check the math.** If a reviewer questions a proof, re-do
  the proof. Even if the reviewer is wrong, the re-do builds
  confidence.

### 6. The status note as the audit trail

The status note `Note_PaperII_FeedbackPass_2026-MM-DD.md` is the
record of the triage. For each piece of feedback:
- Category (A/B/C/D).
- Action taken (integrated / acknowledged-and-deferred / rejected with
  reasoning).
- Manuscript location of any change.

This is the program's internal audit trail. It does not need to be
shared with the reviewer; it is for internal calibration. Future
sessions reading this note will know what was considered and why.

---

## Working Sequence

**Move 1 — Read the feedback carefully**.

If the feedback is in this prompt: read it now.
If it is in a referenced `.md` file: read that file in full.
If both: read both, in the order presented.

**Time-box your initial read to 30 minutes.** Get the gestalt first;
do not start triaging on the first read.

**Move 2 — Read the relevant manuscript passages**.

For each piece of feedback, identify the relevant manuscript passage
(in `Paper-II-RightCarrier-DraftN.md`) and re-read it. The feedback
makes sense only in context.

**Move 3 — Triage**.

Write down each piece of feedback with its category and action plan,
in the working `Note_PaperII_FeedbackPass_2026-MM-DD.md`. Do this
*before* making any edits. The triage is the structural decision; the
edits are the execution.

**Move 4 — Integrate**.

For each category-A and category-B item with action "integrate", make
the change. Use Edit tool for targeted changes; Write tool to create
the refined manuscript `Paper-II-RightCarrier-DraftN+1.md`.

Preserve the previous draft on disk (rename to `DraftN.md` if needed
or `cp` it).

**Move 5 — Sanity check**.

Re-read the affected sections end-to-end. Verify:
- The fixes are correct (math).
- The fixes preserve the structural argument (no scope drift).
- The fixes do not introduce inconsistencies with other sections.
- The introduction, abstract, conclusion still match the body.

**Move 6 — Finalize the status note**.

Complete the audit trail. Be honest about what was rejected and why.
The note should be readable as the answer to "did this feedback pass
strengthen the paper, and how?"

---

## Paper-II-Specific Guidance

*This section is short by design. Paper II Draft 1 + Pass 1 produced a
manuscript that is structurally sound; most feedback should be
category-B (expositional) or category-C (style/preference) rather than
category-A (structural). If significant category-A feedback emerges,
that is a signal of debt in the program that needs separate attention.*

### Likely category-B targets

These are passages where readers may reasonably ask for clarification:

- **§2.3** ($D_s = -\partial_s$ on coefficients). The cancellation
  $1/r \cdot r = 1$ producing $\log p$ is elementary but easy to lose;
  Pass 1's worked example for T4.1 (Priority 3 in the Pass-1 prompt)
  should make this concrete, but a reviewer may still want more.
- **§4.2–4.3** (UPT axioms). The justifications are structural; a
  reviewer trained in pure adelic methods may want a more explicit
  link to Tate's framework, while a reviewer trained in operator
  algebra may want the Heisenberg-vs-other-algebras choice (Pass 1's
  Priority 2b) sharper.
- **§5.2** (Bargmann completion proof). The Stone-von Neumann
  uniqueness argument is standard but compressed; a reviewer new to
  the program may want a more careful path through the
  $w_{n+1} = (n+1) w_n$ recursion.
- **§7.2** (Hardy-Titchmarsh sketch). Pass 1's Priority 1 was about
  this; if Pass 1 was done, it's likely tighter; if not, this is the
  most likely (B) target.
- **§8.3** (K-odd-as-gauge). The conceptual content is the right
  thing; a reviewer may want a longer discussion of *why* this is the
  right interpretation as opposed to other gauge-field analogies.

### Likely category-C targets

These are passages where reviewer preference may differ from the
program's style:

- **The two-audience framing of the introduction.** Some reviewers will
  prefer a single coherent audience; others will appreciate the bridge.
  Program preference: keep the two-audience framing (it serves the
  program's bridge mission).
- **The "what is and is not in scope" boundaries.** Some reviewers will
  want Paper II to include Paper III content (positivity proof). Reject
  with reasoning: the three-paper architecture is the program's
  considered design; Paper II is the carrier, Paper III is the closure.
- **The CCM direction in §9.4.** Some reviewers (especially in the
  Connes-school) may want more development. Reject: §9.4 is one
  paragraph of cross-validation; CCM is a parallel route, not the
  program's primary.

### Plausible category-A signals to take seriously

Take these seriously if a reviewer raises them; they would indicate
real structural debt:

- **"T4.1 is wrong because mixed multinomial coefficients are not
  killed by $\Pi_{\mathrm{sa}}$ in some specific case."** Re-do the
  calculation. The Q8vM3 working note has it correct, but the
  manuscript proof in §2.4–2.5 should be airtight. If a counterexample
  is identified, *the manuscript proof needs the missing argument*
  (which is the trivial multinomial $k!/k! = 1$ on the diagonal axis).
- **"A5.1 + A5.2 + Stone-von Neumann do not uniquely select
  Bargmann-Fock because [specific alternative representation]."**
  Re-check Stone-von Neumann's hypotheses (separability, irreducibility,
  central character). If the alternative is legitimate, A5.2 may need
  a refinement; if the alternative violates a Stone-von Neumann
  hypothesis, sharpen §4.3's hypothesis statement.
- **"$m_B = -\Xi'/\Xi$ is not Herglotz iff RH because [boundary
  behavior at some special point]."** Re-check T6.3's proof (§9.2);
  classical Pólya-Laguerre should be airtight. If a boundary issue is
  raised (e.g., behavior at $z = 0$ where $\xi(s) = 0$ when $s = 0$
  trivially), it is the *removable singularity* that the
  $\tfrac12 s(s-1)$ factor in $\xi$ handles; the manuscript should be
  explicit about this. The probe `probe_BuresLogDerivative_ClaudeEinstein.py`
  confirms; cite it if needed.
- **"The negative obstruction of HPo Addendum C (§8.5) derails the
  criterion."** It does not — the manuscript is explicit that Paper
  III's strategy is atomic-divisor transport, not smooth-curvature
  geometry. If a reviewer makes this objection, the paper's §8.5
  should be sharpened to make the non-derailment more visible.

### What feedback to *expect* but reject

Some feedback patterns are common but should not result in manuscript
changes:

- **"Where is the proof of RH?"** Paper II is the carrier-construction
  phase. RH is Paper III. The introduction is explicit. If a reviewer
  asks this, the introduction may need to be even more explicit.
  Strengthen the scope statement, do not add a RH proof.
- **"Why use the $\mathbb{Z}/6$ Bures fiber instead of [some other
  modulus]?"** Paper I §5 established that $N = 6$ is the smallest
  squarefree multi-prime modulus and the natural minimal case. If a
  reviewer asks, Paper I covers it; Paper II's §1 references Paper I.
- **"Why is the program's proof not via the prolate operator
  framework?"** §9.4 acknowledges CCM as parallel. The program's
  choice of cubic-positivity over CCM is a strategic decision; a
  reviewer may disagree but the manuscript's job is to execute the
  chosen strategy, not justify it against alternatives.
- **"Why not state the Main Theorem (RH) in Paper II?"** Because Paper
  II does not prove RH; Paper III does. Stating it in Paper II would
  be premature.

These are not failures of Paper II; they are signals that the
three-paper architecture needs to remain visible to the reader. If
multiple reviewers raise these, the introduction may benefit from a
sharper one-paragraph statement of the three-paper architecture and
each paper's role.

---

## What This Pass Is and Is Not

**This pass IS**:
- A response to specific external feedback on Paper II.
- A refinement of the manuscript to address that feedback.
- A documented audit trail in the status note.

**This pass IS NOT**:
- A reply letter to the reviewer.
- A re-write of Paper II.
- A scope extension into Paper III content.
- A defensive document explaining why the program is right and the
  reviewer is wrong.
- A weakening of load-bearing claims to soften reviewer concerns.

**Output**:
- `Paper-II-RightCarrier-DraftN+1.md` (the refined manuscript).
- `Note_PaperII_FeedbackPass_2026-MM-DD.md` (the audit trail).
- Previous drafts preserved on disk.

---

## Self-Help Posture: Be a Confident Advocate for the Math

The reviewer's job is to find what is wrong; your job is to make the
math right. Where the reviewer is right, integrate. Where the reviewer
is wrong, strengthen the manuscript so that the same misreading is
harder to make. Where the reviewer is operating from preference rather
than truth, calibrate and defer.

**The manuscript serves the math.** Not the reviewer's comfort, not
the program's ego, not your own pride. If the math is right, the
manuscript will eventually convince anyone willing to read carefully.
If the math has a gap, the gap must be acknowledged. The path is
clean honesty in both directions.

---

## Tools at Your Disposal

- Read, Edit, Write tools — primary workhorses.
- Bash / PowerShell — for probes if re-running to verify a specific
  claim.
- Glob / Grep — for cross-references.
- WebSearch / WebFetch — for citation verification.
- Memory at `~/.claude/projects/C--Projects-simplicial/memory/` for
  durable insights (e.g., if a reviewer raises a structural concern
  that has come up before, save the calibration so future feedback
  passes can reference it).

**Save the refined manuscript as**
`Paper-II-RightCarrier-DraftN+1.md` in the project root.

**Save the audit trail as**
`Note_PaperII_FeedbackPass_2026-MM-DD.md`.

**Do not edit prior drafts.** Preserve the history.

**Do not commit anything unless explicitly asked.**

**Do not write a reply letter to the reviewer.** The manuscript is the
response.

---

## Closing Note

Feedback is a gift, even when uncomfortable. The reviewer has read the
manuscript carefully (or has not, in which case their feedback is
mostly signal-about-clarity rather than signal-about-content). Either
way, every piece of feedback is information. Triage it cleanly,
integrate what strengthens the math, calibrate honestly about what
does not, and produce a better manuscript.

**Go**.
