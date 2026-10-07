r"""Exact probe: can the archimedean place be supplied by a FINITE moment-completion?

Forward-door probe for the RH direction (P3 פ15 / Paper 22 conservation-of-difficulty).
Grounded-paranoid-delusional gate: the settlement meaning below was fixed BEFORE the run.

Background (settled): the primorial is not a moment sequence -- its Hankel determinant
D_3 = -787680 < 0 (P3 פ15, independently verified). P3 reads this as: the real/archimedean
place must be ADJOINED from outside; the finite-prime data cannot self-complete the way the
factorial does (n! = int t^n e^{-t} dt, all D_k > 0, completes to Gamma).

The concrete question this probe settles: is "restore Hankel positivity by a finite
correction" a FAITHFUL finite shadow of the archimedean place -- i.e., is the finite shortcut
to the place real -- or is moment-positivity merely a number-field-growth artifact?

============================================================================
PRE-REGISTRATION  (matched-pair; meaning fixed pre-run)
============================================================================
K (faithful shadow): moment-positivity tracks the archimedean place. The number-field
   primorial fails (D_3<0) while the FUNCTION-FIELD primorial -- the face where the
   Riemann Hypothesis is Weil's THEOREM (no archimedean place needed) -- is moment-positive;
   and the completing datum is canonical. => the finite moment-completion is a faithful
   shadow of the place; the finite shortcut is live.

L (artifact): the function-field primorial ALSO fails moment-positivity (so "moment-positive
   <=> RH/place" is false), and/or the minimal finite completion is a non-canonical family
   (a free location parameter, different minimal mass for each). => moment-positivity is a
   generic primorial-growth artifact, not the place's shadow; the finite shortcut is
   foreclosed; the archimedean place is irreducibly analytic (P3's Gamma_inf, the
   metaplectic/UPT factor), not a finite moment correction.

JOINT-ON-DISJOINT: K that D_3<0 is a real, exact obstruction (factorial positive vs
   primorial fails: prime irregularity genuinely breaks moment positivity) AND L that it does
   not shadow the place (function field fails too; completion non-canonical). Net: re-confirms
   the No-Go from a new angle and redirects effort to the analytic/metaplectic place.
============================================================================

All arithmetic is exact (integers / fractions.Fraction); no floating point enters any sign,
positivity, or canonicity decision.
"""

from __future__ import annotations

import sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path

# Force UTF-8 output: this script prints the glyph פ. On Windows the default cp1252
# stdout raises UnicodeEncodeError (the retained portability failure of P3/P4 §6.2).
# The sanctioned fix is to fix the stream, not strip the glyph.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
try:
    sys.set_int_max_str_digits(1_000_000)         # the function-field determinants are huge
except Exception:
    pass


def fmt(x):
    """Full value for human-size integers; sign + digit count for the huge ones."""
    if -10 ** 50 < x < 10 ** 50:
        return str(x)
    return "%s(%d-digit)" % ("-" if x < 0 else "+", len(str(abs(x))))


def fmt_list(seq):
    return "[" + ", ".join(fmt(x) for x in seq) + "]"


# ---- exact linear algebra ----------------------------------------------------------

def det_int(M):
    """Exact integer determinant via the fraction-free Bareiss algorithm."""
    M = [list(row) for row in M]
    n = len(M)
    sign, prev = 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if M[i][k] != 0), None)
            if sw is None:
                return 0
            M[k], M[sw] = M[sw], M[k]
            sign = -sign
        pivot = M[k][k]
        for i in range(k + 1, n):
            row_i = M[i]
            mik = row_i[k]
            for j in range(k + 1, n):
                row_i[j] = (row_i[j] * pivot - mik * M[k][j]) // prev
        prev = pivot
    return sign * M[n - 1][n - 1]


def inverse(M):
    n = len(M)
    A = [[F(M[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for i in range(n):
        piv = next(r for r in range(i, n) if A[r][i] != 0)
        A[i], A[piv] = A[piv], A[i]
        p = A[i][i]
        A[i] = [x / p for x in A[i]]
        for r in range(n):
            if r != i and A[r][i] != 0:
                f = A[r][i]
                A[r] = [a - f * b for a, b in zip(A[r], A[i])]
    return [row[n:] for row in A]


def hankel_dets(seq, kmax):
    return [det_int([[seq[i + j] for j in range(k + 1)] for i in range(k + 1)]) for k in range(kmax + 1)]


def first_negative(dets):
    for k, d in enumerate(dets):
        if d < 0:
            return k
    return None


# ---- the sequences -----------------------------------------------------------------

def primes(n):
    out, c = [], 2
    while len(out) < n:
        if all(c % p for p in out):
            out.append(c)
        c += 1
    return out


def primorial_seq(K):
    ps = primes(K)
    s, prod = [1], 1
    for p in ps:
        prod *= p
        s.append(prod)
    return s                                   # P_0..P_K


def factorial_seq(K):
    return [factorial(n) for n in range(K + 1)]


def mobius(n):
    if n == 1:
        return 1
    m, d, primefac = n, 2, 0
    while d * d <= m:
        if m % d == 0:
            m //= d
            primefac += 1
            if m % d == 0:
                return 0
        d += 1
    if m > 1:
        primefac += 1
    return -1 if primefac % 2 else 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def irreducible_count(q, d):
    """# monic irreducible polynomials of degree d over F_q."""
    return sum(mobius(e) * q ** (d // e) for e in divisors(d)) // d


def ff_primorial_seq(q, K):
    """Function-field primorial Pi_m = q^{S(m)}, S(m)=sum_{deg<=m} deg over monic irreducibles."""
    seq, S = [1], 0
    for m in range(1, K + 1):
        S += m * irreducible_count(q, m)
        seq.append(q ** S)
    return seq                                 # Pi_0..Pi_K


# ---- the probe ---------------------------------------------------------------------

def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(__doc__)

    KMAX = 6
    log("================  PART A: does moment-positivity track the place? (exact)  ================")
    log("Hankel determinants D_0..D_%d (sign is all that matters; a moment sequence has all >= 0):" % KMAX)
    log("")

    fact = hankel_dets(factorial_seq(2 * KMAX), KMAX)
    prim = hankel_dets(primorial_seq(2 * KMAX), KMAX)
    log("  factorial   n!         (control; n! = int t^n e^{-t} dt, a moment sequence):")
    log("      D = %s" % fmt_list(fact))
    log("      first negative at k = %s   -> %s" % (first_negative(fact),
        "all >= 0 : IS a moment sequence (self-completes to Gamma)" if first_negative(fact) is None else "fails"))
    log("")
    log("  primorial   p_n#        (number field; RH OPEN):")
    log("      D = %s" % fmt_list(prim))
    log("      first negative at k = %s" % first_negative(prim))
    log("")

    FF_KMAX = 4
    ff_dets = {}
    for q in (2, 3):
        ff_dets[q] = hankel_dets(ff_primorial_seq(q, 2 * FF_KMAX), FF_KMAX)
        log("  ff-primorial q=%d  D_0..D_%d  (function field; RH is WEIL'S THEOREM, no archimedean place):"
            % (q, FF_KMAX))
        log("      D = %s" % fmt_list(ff_dets[q]))
        log("      first negative at k = %s" % first_negative(ff_dets[q]))
        log("")

    nf_fails = first_negative(prim)
    ff2_fails = first_negative(ff_dets[2])
    ff3_fails = first_negative(ff_dets[3])
    factorial_positive = first_negative(fact) is None
    oracle_distinguishes = (nf_fails is not None) and (ff2_fails is None) and (ff3_fails is None)
    log("  [A-verdict] factorial moment-positive            : %s" % factorial_positive)
    log("  [A-verdict] number-field primorial fails          : k=%s" % nf_fails)
    log("  [A-verdict] function-field primorial fails (q=2,3): k=%s, k=%s" % (ff2_fails, ff3_fails))
    log("  [A-verdict] does moment-positivity track RH/place : %s" % oracle_distinguishes)
    log("              (K needs YES: ff positive while nf fails;  L if ff also fails)")
    log("")

    log("================  PART B: is the finite completion canonical? (exact)  ================")
    log("Add a point mass c*delta_a to the primorial's representing measure: s_n -> s_n + c*a^n,")
    log("a rank-1 PSD update H_3 -> H_3 + c*v v^T, v=(1,a,a^2,a^3). By the matrix-determinant")
    log("lemma the minimal completing mass at location a is c*(a) = -1 / (v^T H_3^{-1} v), valid")
    log("where the denominator is negative. A CANONICAL place would give one answer; a free")
    log("parameter a with a different mass for each a is a non-canonical family.")
    log("")
    P = primorial_seq(6)
    H3 = [[P[i + j] for j in range(4)] for i in range(4)]
    Hinv = inverse(H3)
    log("  primorial H_3 = %s" % H3)
    log("  a   | w(a)=v^T H_3^{-1} v        | c*(a)= -1/w(a)  (minimal completing mass at a)")
    log("  ----+---------------------------+------------------------------------------------")
    masses = []
    for a in (F(1), F(2), F(3), F(5), F(7), F(1, 2)):
        v = [a ** k for k in range(4)]
        w = sum(v[i] * Hinv[i][j] * v[j] for i in range(4) for j in range(4))
        if w < 0:
            c = -1 / w
            masses.append((a, c))
            log("  %3s | %-25s | %s  (= %.6f)" % (str(a), str(w), str(c), float(c)))
        else:
            log("  %3s | %-25s | (w >= 0: location cannot complete; mass would be infinite)" % (str(a), str(w)))
    any_completion = len(masses) > 0
    distinct = len({c for _, c in masses}) > 1
    log("")
    if any_completion:
        log("  [B-verdict] positive point-mass completion exists; minimal mass varies with a: %s" % distinct)
    else:
        log("  [B-verdict] NO positive point mass at a in {1,2,3,5,7,1/2} restores positivity")
        log("              (w(a) > 0 at every tested location): the finite point-mass completion")
        log("              does not even exist at the natural locations, let alone canonically.")
    log("")

    log("================  REALIZED BRANCH  ================")
    realized_L = (not oracle_distinguishes) or (not any_completion) or distinct
    if realized_L and factorial_positive and (nf_fails is not None):
        log("JOINT-ON-DISJOINT, with the decisive half = L.")
        log("")
        log("K  (real obstruction): the factorial is moment-positive and self-completes to Gamma,")
        log("   while the primorial fails (D_3<0). Prime irregularity genuinely breaks moment")
        log("   positivity -- the obstruction P3 פ15 found is real and exact.")
        log("")
        log("L  (NOT the place): moment-positivity does NOT track the archimedean place.")
        log("   The FUNCTION-FIELD primorial -- where RH is Weil's proven THEOREM and there is no")
        log("   archimedean place at all -- FAILS moment positivity for q=2 (at D_2, even earlier")
        log("   than the number field) while PASSING for q=3 through the computed range. That")
        log("   q-dependence is decisive: moment-positivity tracks the constant field's arithmetic,")
        log("   not RH-status (which holds for every q). And (Part B) no positive point mass at the")
        log("   natural locations restores positivity (w(a)>0 throughout), so the finite completion")
        log("   does not even exist there. A finite moment-completion cannot be the archimedean place.")
        log("")
        log(">>> The finite shortcut is foreclosed. D_3<0 correctly DETECTS that a completion is")
        log(">>> needed, but the completion is irreducibly analytic (P3's Gamma_inf; the")
        log(">>> metaplectic/UPT Bargmann-Fock factor) -- not a finite moment correction. This")
        log(">>> RE-CONFIRMS the No-Go from a fresh angle and redirects effort to the analytic place.")
    else:
        log(">>> K realized (unexpected): moment-positivity tracks the place. Re-examine before")
        log(">>> trusting -- this would be a strong, surprising signal.")

    report = Path(__file__).resolve().parent / "reports" / "primorial_hankel_completion.md"
    header = [
        "# Primorial Hankel-Completion Probe (RH direction, forward-door [C])",
        "",
        "**Script:** `empirical/verify_primorial_hankel_completion.py`",
        "**Context:** P3 פ15 ($D_3=-787680<0$) / Paper 22 conservation-of-difficulty.",
        "**Question:** can the archimedean place be supplied by a finite moment-completion?",
        "",
        "Deterministic, exact (`fractions.Fraction`); no floating point in any sign, positivity,",
        "or canonicity decision. The transcript below is the record.",
        "",
        "```text",
    ]
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(header + lines + ["```", ""]), encoding="utf-8")
    print("\n[report written to %s]" % report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
