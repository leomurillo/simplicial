r"""The IRREVERSIBLE blind spot, transported to RH: the off-line displacement is an ARROW, and every
SYMMETRIC instrument has it in its kernel by parity.  (Third reading of front (a).)

The Irreversible Blind Spot (sibling paper) proves: the single-encoder/SYMMETRIC objective is a
functional of the symmetric part S=(T+T*)/2 ALONE; the antisymmetric part A=(T-T*)/2 -- the probability
CURRENT, the arrow of time -- is in the KERNEL of every real quadratic form (Lemma 1: <h,Ah>=0). The
PREDICTOR (asymmetric, two-encoder) probes <f,Tg> with f!=g, recovers the SVD, and reads A. The
irreversibility gap Delta = sum sigma_i(T) - sum lambda_i(S) >= 0 measures it; =0 iff detailed balance.

RH READING (the unification this script makes concrete):
  * The de Branges clock: E_B = Xi + i Xi', phase phi = -arg E_B, phi(T)/pi = N(T), and
        phi'(t) = (Xi'^2 - Xi Xi'') / (Xi^2 + Xi'^2),     RH <=> phi'(t) >= 0 for all t.
  * The NUMERATOR  Xi'^2 - Xi Xi''  is the ADDITIVE/Kubo-Mori "arrow" object: its SIGN is the arrow
    (phi increasing = forward). A zero leaving the critical line is exactly phi' changing sign
    (de Bruijn-Newman / Lehmer): the arrow REVERSES.
  * The DENOMINATOR  Xi^2 + Xi'^2 = |E_B|^2  is the BURES (quadratic, symmetric) magnitude. It is
    ALWAYS > 0 -- so it is SIGN-BLIND: it cannot see whether phi' > 0 or < 0. The Bures magnitude is
    the arrow-blind symmetric instrument; the phase phi' is the predictor that carries the arrow. This
    IS the program's Kubo-Mori-vs-Bures fork (T24), now NAMED by the irreversibility axis.
  * So front (a)'s "symmetric/averaged statistics (2nd moment, pair correlation, Bures) are blind to
    the off-line zero" is not "averages miss rare events" -- it is the EXACT parity fact: the off-line
    displacement is the ANTISYMMETRIC (arrow) content, in the kernel of every symmetric form. Lifting
    it needs an ASYMMETRIC instrument: the phase clock phi' / m_B = -Xi'/Xi / the predictor.
  * RH  <=>  phi' >= 0 (no arrow reversal)  <=>  Delta = 0 (detailed balance)  <=>  every zero is fixed
    by the reflection about the critical line (on the line), no antisymmetric displacement.

This probe: (A) operator-level -- a toy reversible vs irreversible operator: S has REAL spectrum (a
"line of zeros"), adding A pushes it OFF (complex), the symmetric form <h,Th>=<h,Sh> is blind, the
predictor/SVD sees A, and Delta>0 iff off-line; (B) the RH instance -- compute Xi, Xi', Xi'' and the
arrow-numerator vs Bures-denominator near the first zeros, show phi' carries the sign (arrow) the Bures
magnitude discards; (C) synthesis + honest residual.  NUMERICAL; NO claim RH is proved.
"""

import sys
import numpy as np
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 30
np.set_printoptions(precision=5, suppress=True)


# ----------------------------------------------------------------------------------------
def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    # ============================================================================
    #  PART A -- operator level: reversible (real spectrum/on-line) vs irreversible (off-line arrow)
    # ============================================================================
    log("================  PART A: on-line = reversible (real spectrum); off-line = the arrow (A!=0)  ===")
    n = 12

    def ring(q, b):  # doubly-stochastic drift ring (Irreversible paper E9); eigenvalues in unit disc
        r = 1 - q - b
        T = np.zeros((n, n))
        for k in range(n):
            T[k, k] = r
            T[k, (k + 1) % n] = q
            T[k, (k - 1) % n] = b
        return T

    d = 3  # top-d slow subspace (the gap subspace; the paper's Delta is defined on the top modes)
    rng = np.random.default_rng(0)
    for (q, b, label) in [(0.2, 0.2, "detailed balance q=b"), (0.5, 0.1, "drift q>b (arrow)")]:
        T = ring(q, b)
        S = 0.5 * (T + T.T)
        A = 0.5 * (T - T.T)
        max_im = np.max(np.abs(np.linalg.eigvals(T).imag))
        blind = max(abs((h := rng.standard_normal(n)) @ T @ h - h @ S @ h) for _ in range(200))
        sig = np.sort(np.linalg.svd(T, compute_uv=False))[::-1][:d]
        lamS = np.sort(np.linalg.eigvalsh(S))[::-1][:d]
        Delta = float(sig.sum() - lamS.sum())
        log("  %-22s: max|Im eig(T)|=%.4f %s ; <h,Th>-<h,Sh> max=%.1e (BLIND) ; Delta(top-%d)=%.4f ; |A|=%.4f"
            % (label, max_im, "(ON line)" if max_im < 1e-12 else "(OFF line: arrow!)", blind, d, Delta, np.linalg.norm(A)))
    log("  => detailed balance (q=b): spectrum REAL = 'zeros on the line', A=0, Delta=0 -- no arrow.")
    log("     drift (q!=b): spectrum COMPLEX = 'zeros off the line', the symmetric form is BLIND to it")
    log("     (<h,Th>=<h,Sh> to 1e-15); only the predictor/SVD (Delta>0) sees the arrow. Delta=0 switches")
    log("     the blind spot OFF exactly at detailed balance -- the operator-level RH<=>no-arrow picture.")
    log("")

    # ============================================================================
    #  PART B -- the RH instance: de Branges arrow-numerator vs Bures denominator
    # ============================================================================
    log("================  PART B: RH -- phi' numerator (arrow) vs Bures denominator (sign-blind)  =====")

    def xi(s):
        return mp.mpf(1) / 2 * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)

    def Xi(t):
        return mp.re(xi(mp.mpf(1) / 2 + 1j * t))

    log("  Xi(t)=xi(1/2+it) is real; E_B=Xi+iXi'; phi'(t)=(Xi'^2 - Xi Xi'')/(Xi^2+Xi'^2).")
    log("  arrow numerator N(t)=Xi'^2 - Xi Xi''  (additive/Kubo-Mori; its SIGN = the arrow);")
    log("  Bures denominator D(t)=Xi^2 + Xi'^2 = |E_B|^2  (quadratic/symmetric; ALWAYS > 0 = sign-blind).")
    log("")
    log("     t        Xi(t)         N(t)=Xi'^2-XiXi''   D(t)=|E_B|^2     phi'=N/D     arrow")
    gammas = [mp.mpf("14.134725"), mp.mpf("21.022040"), mp.mpf("25.010858")]
    test_t = [mp.mpf("8"), mp.mpf("14.134725"), mp.mpf("17"), mp.mpf("21.022040"),
              mp.mpf("23"), mp.mpf("25.010858"), mp.mpf("30")]
    minphi = mp.inf
    for t in test_t:
        X = Xi(t)
        Xp = mp.diff(Xi, t, 1)
        Xpp = mp.diff(Xi, t, 2)
        N = Xp ** 2 - X * Xpp
        D = X ** 2 + Xp ** 2
        php = N / D
        minphi = min(minphi, php)
        tag = "fwd (phi'>0)" if php > 0 else "REVERSED (phi'<0!)"
        atzero = " <- zero" if any(abs(t - g) < mp.mpf("1e-4") for g in gammas) else ""
        log("   %7s  %12s  %14s  %12s  %10s  %s%s"
            % (mp.nstr(t, 6), mp.nstr(X, 5), mp.nstr(N, 6), mp.nstr(D, 6), mp.nstr(php, 6), tag, atzero))
    log("")
    log("  min phi' over tested t = %s  (>=0: RH-consistent, arrow always forward).  At each zero Xi=0 so" % mp.nstr(minphi, 6))
    log("  N=Xi'^2 and phi'=1 exactly -- the clock ticks one unit per zero (phi(T)/pi = N(T)).")
    log("  KEY: D=|E_B|^2 is POSITIVE at every t -- the Bures magnitude cannot see the SIGN of phi'.  An")
    log("  off-line zero is exactly N(t)<0 (phi' reverses); D stays >0 and is BLIND to it.  The arrow lives")
    log("  in the numerator N (additive/Kubo-Mori), in the KERNEL of the Bures quadratic -- Irreversible")
    log("  Blind Spot Lemma 1, on zeta: the symmetric/quadratic instrument cannot carry the antisymmetric arrow.")
    log("")

    # ============================================================================
    #  PART C -- synthesis + residual
    # ============================================================================
    log("================  PART C: synthesis -- front (a) is blind on TWO axes  ================")
    log("Front (a)'s statistical->individual gap is now explained at the structural level, and it is blind")
    log("on BOTH of the program's blind-spot axes at once:")
    log("  * CUMULANT axis (CBS / parent): the averaged instrument is 2nd-ORDER -- it misses the higher")
    log("    moments (the two-tower thermometer; 2nd moment Levinson-Conrey ~42%, needs the 4th).")
    log("  * REVERSIBILITY axis (this sibling): the averaged instrument is SYMMETRIC -- the off-line")
    log("    displacement is the ANTISYMMETRIC arrow, in the KERNEL by parity (Lemma 1), NOT merely a")
    log("    rare event. The Bures magnitude |E_B|^2 is sign-blind; the phase phi' (Kubo-Mori/m_B) carries it.")
    log("These two axes are ORTHOGONAL (Irreversible paper E14: zero cross-talk). So the 'individual")
    log("guarantee' RH needs is doubly out of reach of symmetric 2nd-moment statistics: it requires an")
    log("instrument that is BOTH higher-order AND asymmetric -- which is exactly the additive/phase object")
    log("the program kept arriving at (phi', m_B=-Xi'/Xi, the integer count N(T), the predictor).")
    log("")
    log("THE UNIFIED STATEMENT (tiered):")
    log("  [P] computed: symmetric forms are blind to the antisymmetric part (A in kernel), exact to 1e-15;")
    log("      the de Branges arrow-numerator N=Xi'^2-XiXi'' carries the sign phi'; the Bures denominator")
    log("      |E_B|^2>0 is sign-blind; phi'>=0 at all tested t (RH-consistent); phi'=1 at each zero.")
    log("  [A] structural: off-line zero = antisymmetric arrow = phi'<0 = irreversibility gap Delta>0;")
    log("      RH <=> phi'>=0 <=> Delta=0 <=> detailed balance <=> no zero off the reflection axis. The")
    log("      Kubo-Mori-vs-Bures fork (T24) IS the symmetric-vs-predictor split of the irreversibility axis.")
    log("  [open == RH] forcing phi'>=0 (Delta=0) from the arithmetic = building the asymmetric (predictor)")
    log("      object whose self-adjointness is detailed balance -- the Hilbert-Polya H = N_inf + V_arith,")
    log("      whose self-adjointness IS RH. Difficulty conserved; the unification names WHY every symmetric")
    log("      instrument fails and WHICH object (asymmetric/additive/phase) is forced.")
    log("")
    log("NET: the Irreversible Blind Spot upgrades front (a) from 'averages are blind' to the exact parity")
    log("reason -- the arrow is antisymmetric, the symmetric instruments' kernel -- and identifies the lift")
    log("as the predictor/phase object, unifying the statistical->individual gap, the Kubo-Mori/Bures fork,")
    log("and the 'one obstruction, three names' into ONE: the off-line displacement is the arrow of time of")
    log("the zero-dynamics, and RH is its detailed balance.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "irreversible_arrow_rh.md"
    header = [
        "# The irreversible blind spot, transported to RH: the off-line zero is an ARROW",
        "",
        "**Script:** `empirical/verify_irreversible_arrow_rh.py`  (uses IrreversibleBlindSpot.md insights).",
        "**Finding:** front (a)'s statistical->individual gap is blind on TWO orthogonal axes -- cumulant",
        "(2nd-order, the moment thermometer) AND reversibility (symmetric, the arrow). The off-line",
        "displacement is the ANTISYMMETRIC arrow, in the kernel of every symmetric/quadratic form by parity",
        "(Lemma 1) -- NOT a rare event. The de Branges arrow-numerator Xi'^2-XiXi'' carries the sign (phi');",
        "the Bures magnitude |E_B|^2>0 is sign-blind (= the Kubo-Mori/Bures fork, T24, named). RH <=> phi'>=0",
        "<=> irreversibility gap Delta=0 <=> detailed balance. The lift is the asymmetric predictor/phase object.",
        "**Nature:** numerical (numpy operator toy + mpmath de Branges) + structural transport. NO claim RH proved.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
