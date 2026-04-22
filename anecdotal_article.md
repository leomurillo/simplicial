# Vibe-Solving: How a Team of AI Agents Helped Me Close a Math Gap I'd Chased for Years

*Draft — for LinkedIn and cross-posting.*

---

## The short version

A few days ago, with the help of a small team of AI agents working inside my IDE, I finished a math problem I'd been stuck on, on and off, since 2023. The output is a short pre-print paper on a slightly unusual corner of geometry. You can read it here: **[link to pre-print — placeholder]**.

This post is not really about the math. It's about *how* I did it. I'm calling this way of working **vibe-solving**: a hobbyist (or specialist) using a disciplined, multi-agent AI workflow, with themselves firmly in the loop as the accountable owner, to push through a real problem faster and deeper than they could alone.

I think what happened on my laptop over the last few weeks is a small, concrete example of something much bigger that's coming for education, research, and knowledge work in general.

---

## A little context about me (so the rest makes sense)

I won two international math olympiad medals back in 2000 (OIM and APMO) as a Costa Rican student, and afterwards spent several years as a coach, deputy, and judge training younger olympians. Geometry has been my favourite room in the math house since I was a kid.

I later trained as an Electronics Engineer, which pulled me through more math, physics (including quantum basics and electromagnetics), and chemistry. I'm a polymath-wannabe: I've taken roughly 50 university courses across social promotion, economic planning, law, and an MBA, plus dozens more on Coursera, edX, and The Great Courses. I was an autodidact before I knew the word — a scholarship to a great high school lit that fire early.

None of that is a résumé flex; it's the context for why AI-as-thought-partner lands so hard for me. I've watched these models go from "neat chatbot" to *actually useful collaborator*, and my own habits of cognitive resilience — ask probing questions, get a second model to challenge the first, never frame a prompt in a way that rewards sycophancy ("I found this but I'm skeptical…" beats "what do you think of this I wrote?") — transfer over directly.

My current paid work is as an **AI Augmentation Architect / Consultant** for a company in a *safety-critical* domain: avionics. Over there, "just use a tool" is not a move — tools have to be formally qualified, or the engineer has to stay in the loop as the accountable owner of the output. That constraint ("humans on the hook, always") has pushed my dive into agent design *deeper*, not shallower. It's also part-time, which means my free hours have been spilling back into my hobbies with a new set of toys.

One of those hobbies is math. Specifically, this one.

---

## The problem I couldn't let go of

Back in 2023, I got curious about whether you could build a *coordinate system without negative numbers* — something at least as symmetric as Cartesian, maybe more so. I called it the "Optimist Plane" (as in "optimal" and "positive"), later generalizing to higher dimensions.

The idea was simple: instead of two perpendicular axes meeting at a right angle, use three rays from a centre out to the corners of an equilateral triangle for the plane, four rays out to the corners of a regular tetrahedron for 3D, and so on. Any point in the plane becomes a combination of the three rays; any point in space, a combination of the four. You trade one redundant coordinate (you have one more number than dimensions) for a gorgeous symmetry: no axis is privileged, and the basis is permutation-symmetric.

Playing with this, I found you could rotate a point in the plane with **four multiplications** — on par with the Cartesian 2D cost. There was genuine beauty here: simplification fell out, the "distance to origin" formula had a clean symmetric shape, conversions to and from Cartesian were balanced, and the basis vectors themselves summed to zero. It was like discovering a new room in my mental math house, full of toys.

Months later, I learned others had been here before me. This system has names: **barycentric coordinates** in finite element analysis, **Quadray** coordinates (Kirby Urner), **4t** coordinates (Tom Ace), **Fuller's synergetics** in spirit. The probability simplex in information geometry lives here too. So I was not the discoverer — I was a visitor in a lightly-travelled room.

But there was one thing I couldn't find done *and* tried but couldn't do myself: **a general 3D rotation, natively in the 4-ray system, around an arbitrary axis, without falling back to Cartesian or quaternions.**

I'd pick this up, stare at it for a weekend, drop it, play with Collatz for a while, come back. Months went by. The block was real.

---

## The unblocking moment

A few days ago, after yet another round of Collatz burnout, I decided to take one more run at it. This time I paired up with **Gemini 3.1 Pro** and **Claude Opus 4.6 / 4.7** (Claude upgraded to 4.7 in the middle of the work, which was nice).

Gemini noticed something my 2023-self never did: the right arena for the rotation wasn't the full coordinate space — it was the **zero-sum slice** of it, the set of 4-tuples whose entries add to zero. The basis rays themselves sum to zero; the "redundancy" direction I'd spent months trying to interpret was exactly the direction to *quotient out*. Working on the zero-sum slice, the rotation matrix suddenly had the right shape. Gemini sketched a solution.

Claude went through the draft, found the errors Gemini had introduced, and repaired them.

The lesson about my own bias was almost funny. I'd called the whole system "Optimist" — betting on positive-only. I'd been so attached to "no negatives" that it had literally never occurred to me to look at the *zero-sum* form, despite the fact that the basis vectors themselves sum to zero and were shouting it at me from day one. The name had become the blinder.

Two different models, with different biases than mine, got me past my own.

At that point I had a plausible result and a back-of-napkin derivation. What I *didn't* have yet was confidence that this was right, well-situated in the literature, rigorously argued, and written well enough for a pre-print. So I changed gears.

---

## From chat window to an agentic workflow

Here's where the story becomes less about a flash of insight and more about the discipline that followed it.

For 20+ years I've worked in software engineering, so I'm comfortable in an IDE. I set up **Cursor** — the AI-native code editor — with a small team of specialized agents, two workflow skills, and a set of global rules. Think of it as building a research group on my laptop, except each "person" is a purpose-led AI model, and I'm the head of the group and the only name on the paper.

Here's the team, in plain English:

**1. The Author.** The lead writer. Drafts and revises the manuscript. Takes critique from the reviewers and integrates it. Cannot rewrite the paper in one giant pass — must work section by section, in cycles.

**2. Reviewer X — the formalism red team.** A pedantic, hostile-to-claims logician. Reads the manuscript as an adversary. Its only job is to find unstated assumptions, hidden preconditions, and "it is easy to see that…" hand-waves. Read-only: it critiques, it does not edit.

**3. Reviewer Y — the narrative red team.** Plays the role of an experienced arXiv moderator / senior editor. Worries about motivation, section flow, notation conventions, whether a graduate student could follow the argument, and whether citations are placed correctly. Also read-only.

**4. The Empirical Skeptical.** An experimental-mathematician-slash-software-engineer. Its job is to *not trust* the paper. It takes each non-trivial claim, writes Python code that tests it numerically, runs the code, captures the output, and actively hunts for counter-examples. It writes under a strictly separate folder and is forbidden from touching the manuscript.

**5. The Empirical Reviewer.** A senior numerical-analysis QA engineer. Reviews the Skeptical's code *and* its captured output. Checks for floating-point hazards, off-by-one errors, wrong norms, mismatched tolerances, silent NaNs. Gatekeeps: the Author does not get to use an empirical result until this reviewer certifies the code and the numbers.

Two **skills** (workflow recipes) orchestrate them:

- **Authorship orchestration** runs the Author ↔ Reviewers X & Y loop, scope by scope (introduction, then each theorem, then each appendix).
- **Empirical validation** runs the Skeptical ↔ Empirical Reviewer loop, claim by claim.

And a set of **global rules** imposed on everyone: arXiv-quality tone, rigorous notation, no hyperbole, no mathematical leaps of faith, and — most importantly — a termination protocol.

### The termination protocol is the whole game

Every reviewer finding gets a severity tag: **Critical, High, Medium, Low.** Only Critical and High are loop-blocking.

Each loop closes with one of three statuses:

- **STATUS GREEN** — no Critical or High findings remain. Halt. Present to the human (me) for sign-off.
- **STATUS AMBER** — after three revision cycles, Critical or High findings still open. Halt. Surface the disputes to me with explicit citations, append them to a persistent `open-issues.md` log, and let *me* adjudicate.
- **STATUS RED** — the empirical team has found a numerical counter-example to a claim. Halt writing on that claim. Revise or downgrade the theorem.

That little state machine is what turns a clever chat into a disciplined research workflow. The three-loop cap is essential: it refuses to let the agents spiral, and it forces every genuinely hard disagreement out into the open where I have to make the call.

Borrowed straight from my day job: **the human is the accountable owner.** The agents accelerate and challenge. They don't sign off.

---

## What the paper actually says (in plain-ish English)

If you learned geometry in school, you learned **Cartesian coordinates**: two perpendicular axes in the plane (x, y), three in space (x, y, z). It works, but it has a subtle ugliness — the axes are *privileged directions*. Rotate the picture and the axes themselves feel off.

There's a beautiful alternative. For the plane, pick three rays from a centre point, spaced 120° apart (like a Mercedes logo). For 3D space, pick four rays from a centre point, pointing to the four corners of a regular tetrahedron. Any point is now a combination of those three (or four) rays. You have **one coordinate more than you have dimensions** — a built-in redundancy — but in exchange you get *perfect symmetry* of the basis. No direction is special.

Engineers, graphics programmers, and chemists have wandered into various corners of this idea for decades (barycentric coordinates, Quadray coordinates, 4t coordinates, Fuller's synergetics, the probability simplex). What had *not* been cleanly written down, as far as I could find, is this:

> **Can you rotate 3D objects natively in this 4-ray system, around any axis you like, without translating back to Cartesian? And can you do it efficiently?**

The paper's answer is **yes**. Specifically:

- There is a clean algebraic object — a "twist operator" parameterized by any axis — that behaves like the familiar cross product from vector math, but lives natively in the 4-ray world.
- That operator satisfies a small, elegant identity (algebraists: $K^3 = -K$) that lets you write the rotation in *closed form*, directly analogous to Rodrigues' rotation formula that engineers use every day.
- The resulting rotation plays nicely with the built-in redundancy (it "fixes the gauge direction," in the paper's language) and preserves the zero-sum slice where the real geometry lives.
- Applied to a point, the rotation costs **9 multiplications** — exactly matching the standard quaternion-to-matrix pathway that computer graphics has relied on since the 1980s, but with a different, permutation-symmetric flavour.
- As a bonus, the paper pins down *why* this particularly clean behaviour only happens at 4 rays (3D). It's the simplicial coordinate reflection of a well-known exceptional fact about 3D rotations.

Is this going to change computer graphics tomorrow? No. Is it a small, well-defined gap in the literature, now closed, with a clean proof and empirical verification? Yes. That's exactly the scale at which an amateur should contribute, and as an amateur, I am licensed to publish it. Professional mathematicians often get steered away from topics like this for career reasons. Hobbyists don't have that problem.

---

## Why this feels like a genuine shift

Working math with this agentic workflow feels like having a faster, broader-read, and less-tired research team sitting next to me. I fire intuitions as prompts; I get structured feedback in seconds or minutes; I argue back; we converge. A single idea that would have cost me a weekend of manual exploration — and would have been capped by my own blind spots, by my energy, by whether I happened to know the right keyword to Google — now costs me a coffee.

The cognitive-resilience discipline matters. I challenge results, cross-check one model with another, explicitly ask reviewers to *try to break the claims*, require empirical verification before I accept a numerical statement into the paper, and keep an open-issues log for anything that stays contested. That's the only way the workflow adds signal rather than a more articulate flavour of noise.

I used Cursor because it's an IDE, and IDEs are my native UI after two decades of software engineering. But the UIs are evolving fast. **OpenEvidence** for clinicians, **GPT-Rosalind** from OpenAI for life-science researchers — these are specialized research cockpits for specific disciplines, and they are arriving quickly. I suspect within a couple of years, most serious knowledge workers will live inside a workspace like this, agents-and-all, regardless of their background in coding.

For me personally, having closed a hobby-math problem I'd stared at for three years — *with AI, but under my own accountability* — is a visceral data point. AI Augmentation is not a slogan. It is, at this moment, concretely accelerating STEM for someone like me, working alone, on a hobby, in my spare time.

---

## Education, accountability, and the Public Sphere

I'll close with a slightly wider frame.

In 2015, I took the admission test for Universidad de Costa Rica because I wanted to study law — not to become a lawyer, but to be able to *think like one* well enough to be useful in policy debates. I took the spot, studied eight courses and bought a stack of books, and then dropped out once I felt I could reason legally well enough for my purposes. I still feel a little guilty for having taken the seat of someone who would have stayed.

I cannot imagine doing that today. The skills that got me through self-study — reading books, Googling well, synthesizing — transfer almost directly to working with AI agents, and the ceiling is dramatically higher. Agents are not chatbots anymore; they are tireless study partners, specialized tutors, ruthless proof-checkers, and co-authors, depending on how you frame them.

If that is true for me — a hobbyist working on amateur geometry on weekends — it is *emphatically* true for the student who cannot afford a UCR seat in the first place. Access to polymath-grade thought partners is now within reach of anyone with a laptop and discipline.

That's why I'm in the optimistic camp about this shift, but *conditionally* so. The industrial-revolution analogy gets thrown around a lot, usually with the phrase "on steroids." I think it's apt. It means, as Habermas would remind us, that the **Public Sphere** has a lot of deliberative work to do: about labour and compensation, about authorship and accountability, about access and equity, about the epistemic hygiene of a civilization whose reasoning has been partially outsourced. Many clauses of our social contract are due for a serious revisit.

My bet — and it is a bet, not a prediction — is that we can get there through *reform* rather than revolution or barbarie, and that what's on the other side is not a crisis but a new social homeostasis in an exponentially accelerated Era of Abundance.

In the meantime, I'll keep vibe-solving on the weekends and keeping humans firmly in the loop on the weekdays.

---

**Pre-print:** [link — placeholder]

**Workflow artefacts (agents, skills, rules):** I've kept the Cursor configuration that ran this project. If there's interest I'll write a follow-up walking through the agent prompts and the termination protocol in detail. Happy to share.

*Comments and criticism welcome — especially the skeptical kind. That's how the workflow got here in the first place.*
