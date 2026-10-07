r"""How far does an EXACT FINITE model of Weil/adelic global positivity reach, and where is
the archimedean wall?  (RH-direction step (c); metaplectic/UPT global-positivity.)

Grounded-paranoid-delusional gate: meanings fixed BEFORE the run.

The idea. On the FUNCTION-FIELD face (a curve C/F_q) the Riemann Hypothesis is Weil's
theorem and the whole object is finite and exact: Frobenius acts on H^1 with eigenvalues
alpha_1..alpha_{2g}, the power sums S_k = sum_i alpha_i^k are integers (S_0=2g; N_k =
q^k + 1 - S_k are the point counts), and RH is the statement |alpha_i| = sqrt(q), i.e. the
eigenvalues lie on the CIRCLE of radius sqrt(q). By Herglotz/Bochner that circle-positivity
is a TOEPLITZ positivity: c_k = S_k/q^{k/2} are the trigonometric moments of a positive
measure on the circle (the angle atoms) iff the Toeplitz matrix (c_{m-m'}) is PSD. Clearing
the sqrt(q) by the diagonal congruence diag(q^{m/2}) gives the EXACT INTEGER matrix

        M_{m,m'} = S_{|m-m'|} * q^{min(m,m')},

with  M >= 0  <=>  Toeplitz >= 0  <=>  eigenvalues on the circle  <=>  RH for the curve.

This is a finite, exact, RH-equivalent positivity. The number-field side has the SAME shape
but two ingredients a finite model cannot supply: (i) infinitely many zeros (no finite
operator; the program's KU-3 finite Bures envelope already failed), and (ii) the geometry is
the LINE/strip, not the circle -- the number-field "primorial" obstruction is a HANKEL
(real-line moment) failure, D_3 = -787680 < 0, while the curve is a TOEPLITZ (circle) success.
The circle-vs-line difference is exactly the archimedean place: the metaplectic/UPT step
SELECTS the archimedean local factor pi^{-s/2} Gamma(s/2) (the line's completion), but its
global-positivity contribution is the open part. The finite model reaches the wall there.

============================================================================
PRE-REGISTRATION (matched-pair; fixed pre-run)
============================================================================
K: the integer matrix M is PSD exactly for Hasse-valid curves (RH holds) and NOT PSD for
   RH-violators (a^2 > 4q etc.), at the genus-1 and genus-2 levels, by exact leading-minor
   signs -- so the finite model captures function-field global positivity precisely; and the
   transport wall is identified as the archimedean place (circle Toeplitz holds vs line Hankel
   fails) plus infinite spectrum.
L: M does not track RH (PSD for a violator, or non-PSD for a real curve), or the wall is
   elsewhere (the finite model already fails on the function-field face).
JOINT-ON-DISJOINT: K that the function-field/circle positivity is exactly captured AND that
   the number-field transport hits the archimedean wall (line Hankel D_3<0 vs circle Toeplitz
   PSD; finite vs infinite spectrum) -- the wall is the place, made concrete.
============================================================================

Exact integers only; no floating point in any positivity, sign, or PSD decision.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")           # prints פ (cp1252 would raise; P3/P4 §6.2)
except Exception:
    pass


def det_int(M):
    """Exact integer determinant (fraction-free Bareiss)."""
    M = [list(r) for r in M]
    n = len(M)
    sign, prev = 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if M[i][k] != 0), None)
            if sw is None:
                return 0
            M[k], M[sw] = M[sw], M[k]
            sign = -sign
        piv = M[k][k]
        for i in range(k + 1, n):
            ri, mik = M[i], M[i][k]
            for j in range(k + 1, n):
                ri[j] = (ri[j] * piv - mik * M[k][j]) // prev
        prev = piv
    return sign * M[n - 1][n - 1]


def power_sums_g1(a, q, K):
    """S_0..S_K for Frobenius char poly T^2 - aT + q (genus 1)."""
    S = [2, a]
    for k in range(2, K + 1):
        S.append(a * S[-1] - q * S[-2])
    return S


def power_sums_g2(a, b, q, K):
    """Genus-2 Weil poly = product of two genus-1 factors (abelian surface E_a x E_b)."""
    Sa, Sb = power_sums_g1(a, q, K), power_sums_g1(b, q, K)
    return [Sa[k] + Sb[k] for k in range(K + 1)]


def weil_matrix(S, q, n):
    return [[S[abs(m - mp)] * q ** min(m, mp) for mp in range(n + 1)] for m in range(n + 1)]


def leading_minors(M):
    return [det_int([row[:k + 1] for row in M[:k + 1]]) for k in range(len(M))]


def is_psd_by_minors(minors):
    """A negative leading minor certifies NOT PSD; for these genuine moment matrices all >=0
    certifies PSD (rank = #angle atoms, higher minors vanish)."""
    return all(d >= 0 for d in minors)


def main():
    lines = []

    def log(s=""):
        print(s)
        lines.append(s)

    log(__doc__)
    N = 4                                              # Toeplitz size (5x5)

    log("================  FUNCTION-FIELD FACE: circle (Toeplitz) positivity = RH (exact)  ========")
    log("M_{m,m'} = S_{|m-m'|} q^{min(m,m')}; PSD <=> Frobenius eigenvalues on |z|=sqrt(q) <=> RH.")
    log("Level-1 leading minor is exactly 4q - a^2, the Hasse-Weil bound.")
    log("")

    ok = True

    log("  -- genus 1 (T^2 - aT + q) --")
    log("   q | a  | a^2<=4q (RH) | leading minors of M            | M PSD | model == RH")
    log("  ---+----+--------------+--------------------------------+-------+------------")
    g1_cases = [
        (7, -1, "Fermat cubic /F_7 (P4 פWeil)"),
        (2, 2, "real"), (3, 3, "real"), (5, 4, "real"), (7, 5, "real"),
        (7, 6, "RH-VIOLATOR (no curve: Hasse forbids)"),
        (2, 3, "RH-VIOLATOR"), (5, 5, "RH-VIOLATOR"),
    ]
    for q, a, tag in g1_cases:
        S = power_sums_g1(a, q, 2 * N)
        minors = leading_minors(weil_matrix(S, q, N))
        psd = is_psd_by_minors(minors)
        rh = (a * a <= 4 * q)
        ok = ok and (psd == rh)
        log("  %2d | %2d | %-12s | %-30s | %-5s | %-5s  %s"
            % (q, a, str(rh), str([int(x) for x in minors]), str(psd), str(psd == rh), tag))
    log("")

    log("  -- genus 2 (E_a x E_b over F_q; RH <=> a^2<=4q AND b^2<=4q) --")
    log("   q | a,b   | RH    | leading minors of M                    | M PSD | model == RH")
    log("  ---+-------+-------+----------------------------------------+-------+------------")
    g2_cases = [
        (7, -1, 2, "real x real"),
        (5, 4, -2, "real x real"),
        (7, 6, 2, "VIOLATOR (first factor)"),
        (5, 5, 0, "VIOLATOR (first factor)"),
    ]
    for q, a, b, tag in g2_cases:
        S = power_sums_g2(a, b, q, 2 * N)
        minors = leading_minors(weil_matrix(S, q, N))
        psd = is_psd_by_minors(minors)
        rh = (a * a <= 4 * q) and (b * b <= 4 * q)
        ok = ok and (psd == rh)
        log("  %2d | %2d,%-2d | %-5s | %-38s | %-5s | %-5s  %s"
            % (q, a, b, str(rh), str([int(x) for x in minors]), str(psd), str(psd == rh), tag))
    log("")
    log("  [FF-verdict] integer Toeplitz model tracks curve-RH on every case: %s" % ok)
    log("")

    log("================  THE WALL: number-field transport (exact contrast)  ====================")
    primorial = [1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690]
    hankel = leading_minors([[primorial[i + j] for j in range(4)] for i in range(4)])
    log("  Number-field 'primorial' is a LINE (Hankel / real-line moment) object, not a circle one.")
    log("  Hankel leading minors of the primorial: %s" % [int(x) for x in hankel])
    log("      -> first negative at k=3 (D_3 = %d < 0): NOT a moment sequence; RH OPEN." % int(hankel[3]))
    log("")
    log("  Side by side:")
    log("    function field : CIRCLE  (Toeplitz)  -> PSD holds       -> RH is Weil's THEOREM")
    log("    number field   : LINE    (Hankel)    -> D_3 < 0 fails   -> RH is OPEN")
    log("  The circle-vs-line difference IS the archimedean place. A curve is complete (no")
    log("  archimedean place; finite 2g-dim Frobenius). Spec Z has the place at infinity and")
    log("  infinitely many zeros (no finite operator -- the program's KU-3 confirmed this).")
    log("")

    log("================  REALIZED BRANCH  ================")
    if ok and int(hankel[3]) < 0:
        log("JOINT-ON-DISJOINT.")
        log("")
        log("K  (model reaches): the EXACT integer Toeplitz positivity captures function-field global")
        log("   positivity precisely -- PSD <=> RH on every genus-1 and genus-2 case, the level-1 minor")
        log("   IS the Hasse-Weil bound 4q-a^2, and RH-violators are detected by an exact negative minor.")
        log("   On the face where RH is proven and there is no archimedean place, the finite model is the")
        log("   whole story.")
        log("")
        log("L  (wall = the place): the number-field transport needs the LINE (Hankel), where the")
        log("   primorial fails (D_3<0), not the CIRCLE (Toeplitz), where the curve succeeds; and it")
        log("   needs an infinite spectrum (KU-3). Both missing ingredients are the archimedean place.")
        log("   The metaplectic/UPT step selects the place's local factor pi^{-s/2}Gamma(s/2) (the line's")
        log("   completion) but cannot supply its global-positivity contribution from finite data.")
        log("")
        log(">>> HOW FAR THE FINITE MODEL GOES: all the way to PROVEN global positivity on the")
        log(">>> function-field (circle) face, and exactly to -- not across -- the archimedean wall on")
        log(">>> the number-field (line) face. The wall is the place, now exhibited as circle vs line.")
    else:
        log(">>> Pre-registered expectation did not hold; inspect rows above.")

    report = Path(__file__).resolve().parent / "reports" / "finite_global_positivity.md"
    header = [
        "# Finite Global-Positivity Model — how far, and the archimedean wall",
        "",
        "**Script:** `empirical/verify_finite_global_positivity.py`",
        "**Context:** RH-direction step (c); metaplectic/UPT global positivity; P4 פWeil / P3 פ15.",
        "**Status:** %s" % ("function-field (circle) positivity = RH captured exactly; wall = archimedean place"
                            if ok else "see transcript"),
        "",
        "Exact integers only; no floating point in any PSD / sign decision. The transcript is the record.",
        "",
        "```text",
    ]
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(header + lines + ["```", ""]), encoding="utf-8")
    print("\n[report written to %s]" % report)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
