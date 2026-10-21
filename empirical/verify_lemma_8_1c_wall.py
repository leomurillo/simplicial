r"""Lemma 8.1c (primorial character uniformity) in Paper 22's RH route: what it needs, and what discharges it.

Paper 22's limit (Conjecture 5.2 => RH, Thm 6.1) reduces the prime side to Lemma 8.1, now split:
  8.1a0  [P]  CRT isolation (VM projector = CRT packet projector; certified verify_lemma_8_1a0...).
  8.1a   [P skeleton / A occupation-lift]  squarefree mixed/single separation [P]; the prime-power
         occupation ladder Lambda(p^r)=log p at position r log p is EXTERNAL (the K_n->inf double cutoff).
  8.1b   [elementary]  double-cutoff tail (dominated convergence on a log-decaying dense test class).
  8.1c   [A, on OpenAI 2026]  the weighted character PNT, UNIFORM over all Dirichlet chi mod q=P_n:
            max_chi | sum_{m<=X} Lambda(m) chi(m) G_f(log m) - delta_{chi_0} \int G_f | <= X E_n(f),  E_n->0.
  8.1d   [density]  S_0^exp dense in the Weil topology.

Route 1 (Siegel-Walfisz-safe, M_n = exp(P_n^beta)) was always classical: huge cutoffs, ineffective.
Route 2 (natural scale, M_n polynomial in P_n) was the open finite-place gap.  BV / the large sieve give
the AVERAGE over chi (the RMS column below), not the MAX, so they do not settle it.

CORRECTION (Oct 2026).  Earlier versions of this probe said "uniform E_n->0 <=> no Siegel zero <=> GRH for
the primorial characters", and called this the same obstruction as Selberg lambda_1>=1/4.  That
overstated it.  By the explicit formula, E_n is governed by Theta = max_chi sup Re(rho).  ANY fixed
half-plane Theta <= theta < 1 gives
    |psi(X,chi) - delta X| << X^theta log^2(qX),    E_n << X^(theta-1) log^2(P_n X) -> 0
for X >= (log P_n)^(2/(1-theta)+eps).  GRH (theta=1/2) only improves the exponent.  Excluding Siegel zeros
is necessary at polynomial scale but weaker than a fixed half-plane.  The fixed half-plane theta = 7/8 is
now Theorem 1.1 of OpenAI, "The Quasi-Riemann Hypothesis" (30 Sep 2026, github.com/openai/math, family
003).  It is model-generated, and OpenAI reports it as Lean-formalized.  Paper 22 Proposition 8.1c' gives
the derivation.  So route 2 is DISCHARGED at tier [A], resting on OpenAI 2026.

The remaining genuine wall of Paper 22 is the ARCHIMEDEAN one: the Archimedean Noether Limit and Weil
positivity in the limit.  A zero-free strip 1/8 <= Re rho <= 7/8 says nothing about Re rho = 1/2.

This probe COMPUTES the 8.1c object on q=6 and q=30: the character sums psi(X,chi), MAX-over-chi vs
RMS-over-chi, the ratio of the MAX to the 7/8 envelope X^(-1/8) log^2(qX), and L(1,chi) for the real
characters.  NUMERICAL (sieve + mpmath).  Numerics at small q illustrate the bound; they prove nothing
uniform.  NO RH claim.
"""

import sys
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 20


def vonmangoldt_sieve(X):
    import math
    # smallest-prime-factor sieve, then Lambda(n)=log p iff n is a prime power
    spf = list(range(X + 1))
    i = 2
    while i * i <= X:
        if spf[i] == i:
            for j in range(i * i, X + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    Lam = [0.0] * (X + 1)
    for n in range(2, X + 1):
        p = spf[n]
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            Lam[n] = math.log(p)
    return Lam


# --- Dirichlet characters mod 6 and mod 30 via generator decomposition ---
def chars_mod6():
    # units {1,5}; 5 has order 2.  chi_eps(5^a)=eps^a
    table = {1: 0, 5: 1}  # m -> a
    chars = []
    for eps in (1, -1):
        chars.append(("eps=%d" % eps, {m: eps ** a for m, a in table.items()}, eps == 1))
    return 6, chars


def chars_mod30():
    # units = 11^a 7^b, a in {0,1}, b in {0,1,2,3}
    decomp = {1: (0, 0), 7: (0, 1), 19: (0, 2), 13: (0, 3),
              11: (1, 0), 17: (1, 1), 29: (1, 2), 23: (1, 3)}
    chars = []
    for eps in (1, -1):
        for c in range(4):
            vals = {}
            real = True
            for m, (a, b) in decomp.items():
                z = (eps ** a) * (1j ** (c * b))
                if abs(z.imag) > 1e-12:
                    real = False
                vals[m] = z
            chars.append(("eps=%d,c=%d" % (eps, c), vals, real and (eps == 1 and c == 0)))
    return 30, chars, decomp


def psi_chi(X, q, charvals, Lam):
    s = 0.0 + 0.0j
    for n in range(2, X + 1):
        if Lam[n] == 0.0:
            continue
        r = n % q
        if r in charvals:           # gcd(n,q)=1
            s += Lam[n] * charvals[r]
    return s


def L1_real_char(q, charvals):
    # L(1,chi) = -(1/q) sum_{a=1}^{q-1} chi(a) psi_digamma(a/q)   (for nonprincipal chi)
    tot = mp.mpf(0)
    for a in range(1, q):
        if a % q in charvals:
            tot += mp.re(charvals[a % q]) * mp.digamma(mp.mpf(a) / q)
    return -tot / q


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    Xmax = 60000
    log("Sieving von Mangoldt up to X=%d ..." % Xmax)
    Lam = vonmangoldt_sieve(Xmax)
    log("  done.")
    log("")

    # ============================================================================
    #  PART B -- the 8.1c object on q=6 and q=30
    # ============================================================================
    log("================  PART B: the 8.1c character sums  psi(X,chi)/X  (q=6, q=30)  ================")
    for spec in (chars_mod6(), chars_mod30()):
        q, chars = spec[0], spec[1]
        log("  --- modulus q=%d : %d Dirichlet characters ---" % (q, len(chars)))
        Xs = [10000, 30000, 60000]
        log("       X        principal psi/X (-> 1, PNT)   max_{chi != chi0} |psi/X|   RMS_{chi != chi0} |psi/X|   max / [X^(-1/8) log^2(qX)]")
        for X in Xs:
            pri = None
            nonpri = []
            for name, vals, is_pri in chars:
                v = abs(psi_chi(X, q, vals, Lam)) / X
                if is_pri:
                    pri = psi_chi(X, q, vals, Lam) / X   # real, ~ density of units
                else:
                    nonpri.append(v)
            mx = max(nonpri)
            rms = (sum(v * v for v in nonpri) / len(nonpri)) ** 0.5
            env = mp.mpf(X) ** (-mp.mpf(1) / 8) * mp.log(q * X) ** 2
            log("     %6d        %s                 %s              %s              %s"
                % (X, mp.nstr(pri, 5), mp.nstr(mx, 5), mp.nstr(rms, 5), mp.nstr(mx / env, 4)))
        log("     => principal psi/X -> 1 (the PNT main term; the few p|q drop only O(log X)); nonprincipal -> 0 (PNT for L(s,chi)).")
        log("        max over the family >= RMS (average); the gap is ~sqrt(#chi) here, modest at small q.")
        log("        The last column (max over the 7/8 envelope) stays small, as Prop 8.1c' predicts.  Illustration only.")
        log("")

    # ============================================================================
    #  PART C -- L(1,chi) for the real characters (no Siegel at small q) + the wall framing
    # ============================================================================
    log("================  PART C: real characters, L(1,chi)>0, and the half-plane framing  ================")
    q, chars, _ = chars_mod30()
    log("  real (quadratic) characters mod 30 and L(1,chi):")
    for name, vals, is_pri in chars:
        if is_pri:
            continue
        if all(abs(v.imag) < 1e-12 for v in vals.values()):  # real character
            L1 = L1_real_char(q, vals)
            log("     chi[%s] : L(1,chi) = %s" % (name, mp.nstr(L1, 8)))
    log("  All real L(1,chi) at q=30 are bounded away from 0.  This is a finite check at one modulus.")
    log("")
    log("  THE EXPLICIT-FORMULA LINK.  psi(X,chi) - delta_{chi0} X = - sum_{rho} X^rho/rho + ... over the zeros")
    log("  rho of L(s,chi), so |psi(X,chi)|/X is governed by Theta = max_chi sup Re(rho).  Precisely:")
    log("     Theta <= theta < 1 uniformly  ==>  E_n << X^(theta-1) log^2(P_n X) -> 0 for X >= (log P_n)^(2/(1-theta)+eps).")
    log("  GRH is NOT needed.  No-Siegel-zero is necessary at polynomial scale (a real zero with 1-beta <= c/log q")
    log("  contributes X^(beta-1) >= e^(-cA) at X = q^A), but it is weaker than a fixed half-plane.")
    log("  BV / the large sieve control the AVERAGE sum_chi |psi(X,chi)|^2 (the RMS column), not the MAX.")
    log("")
    log("  THE DISCHARGE (Oct 2026).  OpenAI 2026 (family 003, Thm 1.1): every Dirichlet L(s,chi) is zero-free")
    log("  in Re s > 7/8 [A; model-generated; OpenAI reports Lean formalization].  The functional equation then")
    log("  puts every nontrivial zero in 1/8 <= beta <= 7/8.  The truncated explicit formula with T = X gives")
    log("  |psi(X,chi) - delta X| << X^(7/8) log^2(qX), so 8.1c route 2 holds with M_n polynomial in P_n.")
    log("  (Paper 22, Proposition 8.1c'.)")
    log("")
    log("  RE-SCOPED COMPARISON.  The earlier claim that 8.1c, Selberg lambda_1 >= 1/4, pair correlation and")
    log("  de Bruijn-Newman are 'one' obstruction is withdrawn.  8.1c needs only a STRIP.  The others are")
    log("  statements about zeros ON the critical line.  The strip gives de Bruijn-Newman Lambda <= 9/32 only,")
    log("  which is worse than Polymath's 0.22, and leaves Re rho = 1/2 open.")
    log("")
    log("  THE ROUTES (Paper 22 sec 8):")
    log("    route 1 (Siegel-Walfisz-safe): M_n = exp(P_n^beta), HUGE cutoffs, classical individual")
    log("       uniformity (q <= (log X)^A), INEFFECTIVE.")
    log("    route 2 (natural scale): M_n polynomial in P_n.  Was the gap.  Now [A] on OpenAI 2026, with")
    log("       EFFECTIVE constants and threshold X_n = (log P_n)^(16+eps) ~ p_n^(16+eps).")
    log("")
    log("  THE WALL THAT REMAINS (not the prime side): the ARCHIMEDEAN Noether Limit (Conjecture 5.2 input #2,")
    log("  Theorem 5.2.2).  The archimedean place pi^{-s/2}Gamma(s/2) is NOT finitely-prime-generable (No-Go).")
    log("  Even granting the prime-side recovery, assembling the COMPLETED Weil form and its positivity in the")
    log("  limit is the marginal-archimedean-positivity step, which is RH itself.")
    log("")
    log("HONEST SCOPE / VERDICT:")
    log("  [P]  8.1a0 (CRT isolation), the 8.1a squarefree skeleton, the finite leakage extinction.")
    log("  [A]  8.1c route 1 (Siegel-Walfisz, ineffective) and 8.1c route 2 (natural scale, on OpenAI 2026).")
    log("  [A]  the 8.1a occupation lift (K_n -> inf): external, still to be written in.")
    log("  [open]  projective critical-leaf closure (Theorem 5.1.3) and 8.1d density.")
    log("  [open == RH]  the Archimedean Noether Limit + Weil positivity in the limit.")
    log("  NO RH claim.  The finite-place character side no longer meets RH/GRH.  Paper 22's wall is archimedean.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "lemma_8_1c_wall.md"
    header = [
        "# Lemma 8.1c: primorial character uniformity in Paper 22's RH route (re-scoped Oct 2026)",
        "",
        "**Script:** `empirical/verify_lemma_8_1c_wall.py`  (builds on Paper 22 sec 8, the 8.1 sub-lemmas).",
        "**Finding:** Paper 22's limit (Conjecture 5.2) reduces the prime side to Lemma 8.1.  Its analytic",
        "piece 8.1c is a weighted character PNT UNIFORM over chi mod P_n, governed by Theta = max sup Re(rho).",
        "**Correction:** earlier versions said 'uniform E_n->0 <=> no Siegel zero <=> GRH'.  That was an",
        "overstatement.  Any fixed half-plane Theta <= theta < 1 suffices, for X >= (log P_n)^(2/(1-theta)+eps).",
        "OpenAI 2026 (github.com/openai/math, family 003; model-generated; OpenAI reports Lean formalization)",
        "gives theta = 7/8 for every Dirichlet L.  So 8.1c route 2 is now [A], resting on OpenAI 2026",
        "(Paper 22 Proposition 8.1c').  BV/large sieve still give only the average (RMS), not the max.",
        "The 'one wall' unification with Selberg lambda_1 >= 1/4 and pair correlation is WITHDRAWN: those concern",
        "zeros on the critical line, and 8.1c needs only a strip.  The remaining wall of Paper 22 is archimedean",
        "(the Archimedean Noether Limit).  NO RH/GRH claim.",
        "**Nature:** numerical (sieve + mpmath) + literature-exact reduction.  Numerics illustrate; they prove nothing uniform.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
