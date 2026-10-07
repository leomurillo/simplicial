# ERRAND PROMPT — Ship the CCM verification note (v2): repo + DOI + contact draft

Open a fresh Claude Code session **in `C:\Projects\Connes`** and paste everything
below. (If the session opens elsewhere, cd context is `C:\Projects\Connes`.)

---

This is a SHIPPING errand. The science is FROZEN. You are packaging and preparing a
finished, adversarially-hardened verification note for (1) a public GitHub repo,
(2) a Zenodo DOI, and (3) a contact email to the authors of arXiv:2511.22755
(Connes–Consani–Moscovici, "Zeta spectral triples"). Nothing is sent or made public
without Leo's explicit confirmation at the end.

## The artifact (already finished — 2026-06-12 hardening pass)

- `ExactVerification-SemilocalWeilForm-Note-v2.md` — the note. v2 is the hardened
  version: corrected CCM reference numbers (Lem 2.3/3.1/3.2, Lem 7.2/7.3, Fig 4 —
  CCM has NO appendix), verbatim §8 quotes, N-labeled tables with drift disclosures,
  five certificates, §8 trailer sentence on the step-(ii) mechanism.
- `AUDIT.md` — per-claim novelty verdicts + number freeze table.
- `README.md` — repo skeleton; five fired falsifiers retained by design (GPD method).
- `ExactVerification-SemilocalWeilForm-Note-v1.md` — kept for record.
- Probe certificates + `attack_v2_hardening.py` + logs (the "6 scripts + logs") —
  these MUST be mirrored into the repo before anything is sent.
- Target paper TeX (read-only reference): `C:\Users\leomu\Downloads\arXiv-2511.22755v1\mc2arXiv.tex`.

Novelty positioning is already settled in AUDIT.md — do not re-litigate it. Key
context: Groskin arXiv:2605.20224 and Śliwiński arXiv:2601.12133 are PRIOR ART for
"independent implementation" claims; the note's surviving claims are the sharpened
ones (O(N) per-frequency reduction; simple-even VERIFIED (not basis-imposed) at small
λ = 1.3/1.5/2.0; first quantitative Rayleigh r/ε; ladder-ratio measurement; small-λ
primes-{2,3} regime). The note and email must match AUDIT.md's framing exactly.

## HARD RULES

1. **Content freeze.** No edits to v2 beyond: the affiliation line, links (repo URL,
   DOI), date, and typo-level fixes. Any other change — even "improvements" — needs
   Leo's explicit approval first.
2. **Nothing outbound without confirmation.** GitHub repo may be created PRIVATE and
   flipped public only at the final confirmation step. Zenodo deposition saved as
   DRAFT (not published). Email is a draft file, never sent by you.
3. **PDF discipline** (known build gotchas): the title block needs the affiliation
   line; pandoc parses title/author/date from the H1 block and the first `---`
   closes it; ALWAYS visually inspect the rendered PDF page by page — a clean log
   does not mean a clean render.
4. Do not ask the recipients for an arXiv endorsement in this first contact.

## LEO'S FOUR CALLS (ask via a single question round at session start if not filled in here)

- A. Affiliation line for the note/Zenodo: ______
- B. GitHub repo name + owner + start private? (suggest: short, e.g. `ccm-exact-verification`): ______
- C. Recipients: Connes, Consani, Moscovici — include van Suijlekom too? ______
- D. Attach/link the v1→v2 diff? ______

## EXECUTION

**Phase 1 — Repo.** Create the GitHub repo (private until final confirmation) via
`gh`. Contents: v2 note (md + built PDF), AUDIT.md, README.md, v1 (for record), the
probe scripts + `attack_v2_hardening.py` + run logs, a LICENSE (CC-BY-4.0 for text,
MIT for code — confirm with Leo in the same question round if unsure), and a short
top-level README pointing to the note and the certificate re-run instructions.
Re-run the certificates once from a clean checkout to confirm they are
self-contained (they are sympy/mpmath-grade local probes — no torch; if any need an
absent dependency, record it in the repo README rather than restructuring).

**Phase 2 — PDF.** Insert the affiliation line, build the PDF with the established
pandoc/xelatex pipeline (a `build.ps1`/`build.sh` may exist; otherwise plain pandoc),
and visually inspect every page (math rendering, tables, the §8 verbatim quotes).

**Phase 3 — Zenodo draft.** Check for a Zenodo API token (`$env:ZENODO_TOKEN`; the
simplicial repo has a `zenodo-metrics/` precedent). If present: create a DRAFT
deposition (do NOT publish) with metadata — title = the note's title; author
Leonardo Murillo Montero (affiliation from call A); description = the note's
abstract; related identifiers: arXiv:2511.22755 (cites), the GitHub repo URL
(isSupplementTo); license per Phase 1. If no token: write
`zenodo_metadata.json` + an upload checklist instead, and say so.

**Phase 4 — Contact email draft.** Write `EMAIL_DRAFT_ccm.md`: recipients per call C
(find academic addresses from their institutional pages — IHES/Vanderbilt/JHU/Ohio
State as applicable; cite where each address was found, flag any uncertainty).
Body ≤ 250 words, professional, concrete: (i) what was verified independently in
exact arithmetic against 2511.22755 (the five certificates, one sentence); (ii) the
two or three sharpest findings as stated in AUDIT.md (e.g. parity verified rather
than imposed at small λ; the quantitative r/ε = 0.135; the reference-numbering
errata they may want for their records); (iii) honest placement next to Groskin and
Śliwiński in one clause; (iv) one closing line: a short follow-up note on a
candidate mechanism for their §8 step (ii) exists and can be shared on interest —
no overclaim, no attachment of that second note; (v) link to repo + DOI
(placeholders until flipped live). No flattery padding, no endorsement request.

**Phase 5 — Final checklist for Leo.** Present: repo URL (private), built PDF path,
Zenodo draft link (or manual checklist), email draft, the v1-diff (per call D), and
the exact go-sequence: flip repo public → publish Zenodo → fill DOI into note/email
→ Leo sends email. STOP there; the sends and the public flips are Leo's clicks.
