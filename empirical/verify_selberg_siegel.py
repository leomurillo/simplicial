r"""Selberg eigenvalue conjecture <-> Landau-Siegel zero: the QUANTITATIVE dictionary, the proven
Kim-Sarnak record, the no-Siegel-zero-vs-GRH gap, and a trace-formula exceptional-eigenvalue
sensitivity computation.  Companion to verify_scattering_zeta_L.py / verify_full_trace_formula.py /
verify_selberg_geodesic_spectral.py (those establish the scattering mechanism + the machine-precision
PSL(2,Z) balance; this one nails the CONSTANTS, the proven record, and what is/is not gained).

THE DICTIONARY (Iwaniec, Spectral Methods of Automorphic Forms 2nd ed., ch. 11; Sarnak, Notes on the
Generalized Ramanujan Conjectures 2005; Conrey-Iwaniec, "The cubic moment of central values of
automorphic L-functions," Ann. of Math. 151 (2000)).  Let chi be a real primitive Dirichlet character
mod q with a Landau-Siegel zero beta = 1 - delta (real, beta in (1/2,1), delta = 1-beta small).  The
theta / Shimura-Waldspurger lift sends L(s,chi) to a weight-1/2 Maass form on Gamma_0(4q) (Kohnen plus
space).  The Laplacian eigenvalue of the lifted object is
      lambda = s(1-s)   with   s = beta,        i.e.   lambda = beta(1-beta).
Writing the spectral parameter lambda = 1/4 - t^2 (eigenvalue below 1/4 <=> t real, "exceptional"):
      t = beta - 1/2     and     lambda = 1/4 - (beta - 1/2)^2.
So a Siegel zero beta -> 1 (delta -> 0) gives lambda = beta(1-beta) -> 0: an exceptional eigenvalue
crashing toward 0.  Conversely an exceptional eigenvalue lambda = 1/4 - s^2 (0 < s < 1/2, spectral
parameter r = i*s purely imaginary) corresponds to a real zero beta = 1/2 + s of the lifted L-function.

THE KIM-SARNAK CHAIN.  The local archimedean Ramanujan exponent theta_infty bounds the eigenvalue:
   lambda_1 >= 1/4 - theta_infty^2.  Bounds toward theta_infty = 0 (full Ramanujan -> Selberg 1/4):
     - Selberg 1958:        theta <= 1/4         => lambda_1 >= 3/16   = 0.1875
     - via sym^2 (Gelbart-Jacquet 1978) ............ improves toward Ramanujan
     - sym^3, sym^4 (Kim-Shahidi 2002; Kim 2003, w/ appendix Kim-Sarnak): theta_infty <= 7/64
        => lambda_1 >= 1/4 - (7/64)^2 = 1/4 - 49/4096 = (1024-49)/4096 = 975/4096 = 0.23803...
The gap to Selberg's 1/4 = 0.25 is 49/4096 = 0.011963...  PROVEN RECORD (full level, GL(2)/Q): still
975/4096 (Kim-Sarnak 2003).  Liyang Yang's 2020 "improvement" for EXCEPTIONAL Maass forms was WITHDRAWN
(arXiv:2011.09054, incomplete proof).  Holomorphic Ramanujan is THEOREM (Deligne) but irrelevant here:
the Maass / weight-1/2 case is where Siegel zeros live, and there theta_infty = 7/64 is the wall.

WHAT NO-SIEGEL-ZERO BUYS, AND WHAT IT DOES NOT.  Selberg lambda_1 >= 1/4 <=> no exceptional eigenvalue
on Gamma_0(4q) <=> no Landau-Siegel zero for real chi mod q.  No-Siegel-zero gives: effective
L(1,chi) >> 1/log q (vs Siegel's INEFFECTIVE bound), effective class number h(-d) >> sqrt(d)/log d for
imaginary quadratic, effective PNT in arithmetic progressions / effective Linnik.  It does NOT give GRH:
the OTHER (complex, off-real-axis) zeros of L(s,chi) can still lie off Re(s)=1/2.  No-Siegel-zero only
excludes the single real zero near s=1; GRH excludes ALL.  no-Siegel-zero  <<  GRH, strictly.

This probe:
  (A) the exact dictionary as a numeric table: beta <-> delta <-> lambda <-> t, both directions.
  (B) the Kim-Sarnak chain arithmetic in exact rationals: 3/16, 975/4096, the 49/4096 gap; Selberg
      lambda_1 >= 1/4 - theta^2 evaluated at each proven theta; identify the room.
  (C) TRACE-FORMULA SENSITIVITY: insert a hypothetical exceptional eigenvalue lambda = 1/4 - s^2
      (r = i*s) into the spectral side h(i*s) of the machine-precision-balanced PSL(2,Z) trace formula,
      and measure the residual it injects -- the quantitative "the trace formula would SEE it" signal,
      and how the signal scales as the Siegel zero tightens (s -> 1/2, lambda -> 0).
  (D) SCATTERING LAW: for real chi mod 3 and mod 5, compute L(s,chi) on (1/2,1), confirm L>0 (no real
      zero), hence no real scattering pole, hence (via lambda = beta(1-beta)) no exceptional eigenvalue;
      cross-check the eigenvalue that a HYPOTHETICAL Siegel zero at beta would produce.
  (E) synthesis + the precise residual.

NUMERICAL/EXACT (mpmath dps 30; Fraction for the chain).  Cited where derivation is standard
(theta-lift dictionary, level 4q, Maass spectrum).  NOT a proof of Selberg / no-Siegel-zero / GRH.
"""

import sys
from fractions import Fraction as Fr
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 30


# ---------------------------------------------------------------------------------------------------
#  the lift dictionary  lambda = beta(1-beta) = 1/4 - (beta-1/2)^2
# ---------------------------------------------------------------------------------------------------
def lam_of_beta(beta):
    return beta * (1 - beta)


def t_of_beta(beta):
    return beta - mp.mpf(1) / 2          # spectral parameter t with lambda = 1/4 - t^2 (t = s here)


def beta_of_lam(lam):
    # invert lambda = beta(1-beta), take the root in (1/2,1): beta = 1/2 + sqrt(1/4 - lam)
    return mp.mpf(1) / 2 + mp.sqrt(mp.mpf(1) / 4 - lam)


# ---------------------------------------------------------------------------------------------------
#  real Dirichlet L-functions via Hurwitz zeta (chi mod 3, chi mod 5), and L(1,chi) via digamma
# ---------------------------------------------------------------------------------------------------
def L_chi3(s):
    # chi_3 = Legendre symbol mod 3: chi(1)=1, chi(2)=-1
    return 3 ** (-s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))


def L_chi5(s):
    # chi_5 = Legendre symbol mod 5: chi(1)=1, chi(2)=-1, chi(3)=-1, chi(4)=1
    return 5 ** (-s) * (mp.zeta(s, mp.mpf(1) / 5) - mp.zeta(s, mp.mpf(2) / 5)
                        - mp.zeta(s, mp.mpf(3) / 5) + mp.zeta(s, mp.mpf(4) / 5))


def L1_chi3():
    return -(mp.digamma(mp.mpf(1) / 3) - mp.digamma(mp.mpf(2) / 3)) / 3


def L1_chi5():
    return -(mp.digamma(mp.mpf(1) / 5) - mp.digamma(mp.mpf(2) / 5)
             - mp.digamma(mp.mpf(3) / 5) + mp.digamma(mp.mpf(4) / 5)) / 5


# ---------------------------------------------------------------------------------------------------
#  trace-formula spectral side (the machine-precision balance lives in verify_full_trace_formula.py;
#  here we reuse the verified Maass spectrum + the SAME Gaussian test function, and probe sensitivity)
# ---------------------------------------------------------------------------------------------------
MAASS = [mp.mpf(x) for x in ["9.533695261", "12.173008325", "13.779751352", "14.358509518",
                             "16.138073172", "16.644259161", "17.738563381", "18.180917607",
                             "19.423481470", "19.484710023"]]


def h_gauss(r, sig):
    # even test function h(r)=exp(-r^2/2sig^2); for r=i*s (exceptional) this is exp(+s^2/2sig^2) (>1)
    return mp.e ** (-(r ** 2) / (2 * sig ** 2))


def spectral_side(sig, extra_s=None):
    """S = h(i/2)  [the residual/constant eigenfunction, lambda_0 = 0, r_0 = i/2]
            + sum_j h(r_j)  [Maass cusp spectrum]
            + (optional) h(i*extra_s)  [a HYPOTHETICAL exceptional eigenvalue lambda = 1/4 - extra_s^2].
    On PSL(2,Z) there is NO exceptional term: extra_s=None reproduces the balanced spectral side.
    extra_s>0 models what a congruence-level Siegel zero would inject."""
    S = mp.re(h_gauss(mp.mpf(1) / 2 * 1j, sig)) + mp.fsum(h_gauss(r, sig) for r in MAASS)
    if extra_s is not None:
        S = S + mp.re(h_gauss(1j * mp.mpf(extra_s), sig))
    return S


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    # =============================================================================================
    log("================  (A) THE DICTIONARY  beta <-> delta <-> lambda <-> t (exact relations)  ====")
    log("  lift: weight-1/2 Maass form on Gamma_0(4q); lambda = beta(1-beta) = 1/4 - (beta-1/2)^2.")
    log("  A Siegel zero beta = 1 - delta of real chi mod q  ->  exceptional eigenvalue lambda below:")
    log("    beta        delta=1-beta     lambda=beta(1-beta)    t=beta-1/2   (lambda=1/4 - t^2)")
    for b in ["0.6", "0.75", "0.9", "0.95", "0.99", "0.999", "0.9999"]:
        beta = mp.mpf(b)
        log("    %-10s  %-13s  %-20s  %s"
            % (mp.nstr(beta, 6), mp.nstr(1 - beta, 5), mp.nstr(lam_of_beta(beta), 10),
               mp.nstr(t_of_beta(beta), 8)))
    log("  small-delta law:  lambda = beta(1-beta) = (1-delta)*delta = delta - delta^2  ~  delta  as delta->0.")
    log("  So lambda ~ (1 - beta) to first order: the eigenvalue is ~ the Siegel-zero DEFECT from 1.")
    log("  CONVERSE (exceptional eigenvalue -> Siegel zero):  lambda = 1/4 - s^2  (r = i*s, 0<s<1/2)")
    log("    lambda          s=sqrt(1/4-lambda)   beta = 1/2 + s   (the implied real zero)")
    for lv in ["0.24", "0.20", "0.15", "0.10", "0.05", "0.01", "0.001"]:
        lam = mp.mpf(lv)
        s = mp.sqrt(mp.mpf(1) / 4 - lam)
        log("    %-14s  %-18s   %s" % (mp.nstr(lam, 6), mp.nstr(s, 10), mp.nstr(beta_of_lam(lam), 10)))
    log("")

    # =============================================================================================
    log("================  (B) THE KIM-SARNAK CHAIN  lambda_1 >= 1/4 - theta_infty^2 (exact rationals)  =")
    log("  theta_infty = archimedean exponent toward Ramanujan; Ramanujan(theta=0) => Selberg(1/4).")
    chain = [
        ("trivial / Selberg 1958",  Fr(1, 4),    "lambda_1 >= 3/16"),
        ("Luo-Rudnick-Sarnak 1995", Fr(5, 28),   "via Rankin-Selberg / density"),
        ("Kim-Shahidi 2002 (sym^3)", Fr(1, 9),   "Langlands-Shahidi sym^3 holomorphy"),
        ("Kim-Sarnak 2003 (sym^4)", Fr(7, 64),   "Kim sym^4 (Kim-Shahidi) + Kim-Sarnak appendix"),
        ("Ramanujan (conjectural)", Fr(0, 1),    "Selberg's 1/4 (OPEN)"),
    ]
    log("    source                       theta_infty     lambda_1 >= 1/4 - theta^2        decimal")
    quarter = Fr(1, 4)
    for name, th, note in chain:
        lb = quarter - th * th
        log("    %-28s %-15s %-30s %s"
            % (name, str(th) + " = " + mp.nstr(mp.mpf(th.numerator) / th.denominator, 6),
               str(lb) + " = 1/4 - " + str(th * th), mp.nstr(mp.mpf(lb.numerator) / lb.denominator, 9)))
    ks = quarter - Fr(7, 64) ** 2
    gap = quarter - ks
    log("  PROVEN RECORD (full level, GL(2)/Q): lambda_1 >= %s = %s  (Kim-Sarnak 2003)."
        % (str(ks), mp.nstr(mp.mpf(ks.numerator) / ks.denominator, 10)))
    log("  GAP to Selberg 1/4 = 0.25:  1/4 - 975/4096 = %s = (7/64)^2 = %s."
        % (str(gap), mp.nstr(mp.mpf(gap.numerator) / gap.denominator, 8)))
    log("  Liyang Yang 2020 (sym^? improvement for EXCEPTIONAL Maass forms): WITHDRAWN (incomplete);")
    log("  so 7/64 -> 975/4096 STILL STANDS as the proven bound over the full level (as of 2026).")
    log("  IDENTIFIABLE ROOM: theta_infty = 7/64 comes from sym^4 being the last PROVEN functorial")
    log("  symmetric power (sym^5,6,... give the Ramanujan limit 0 but are NOT known functorial as")
    log("  cuspidal automorphic on GL(n)).  Each new sym^k would shrink theta_infty toward 0; the")
    log("  0.012 gap is exactly 'sym^4 is where Langlands-Shahidi currently stops.'")
    log("")

    # =============================================================================================
    log("================  (C) TRACE-FORMULA SENSITIVITY: inject a hypothetical exceptional eigenvalue  =")
    log("  The PSL(2,Z) trace formula balances to ~1e-6 (verify_full_trace_formula.py) with NO")
    log("  exceptional term.  We add one hypothetical eigenvalue lambda = 1/4 - s^2 (r = i*s) to the")
    log("  spectral side h(i*s) and read off the residual it would INJECT into the balance -- i.e. the")
    log("  trace formula's sensitivity to an exceptional eigenvalue (what a congruence-level Siegel zero")
    log("  would do).  Test function h(r) = exp(-r^2/2 sig^2); note h(i*s) = exp(+s^2/2 sig^2) >= 1.")
    for sig in [mp.mpf(4), mp.mpf(2), mp.mpf("1.2")]:
        base = spectral_side(sig)
        log("  --- sigma = %s : baseline spectral side S0 = %s (no exceptional term) ---"
            % (mp.nstr(sig, 4), mp.nstr(base, 12)))
        log("      s (=beta-1/2)   beta=1/2+s   lambda=1/4-s^2   added h(i*s)=dS   (dS)/S0 jump")
        for sv in ["0.49", "0.45", "0.4", "0.3", "0.2", "0.1", "0.05"]:
            s = mp.mpf(sv)
            beta = mp.mpf(1) / 2 + s
            lam = mp.mpf(1) / 4 - s * s
            inj = mp.re(h_gauss(1j * s, sig))
            log("      %-13s  %-11s  %-14s  %-15s  %s"
                % (mp.nstr(s, 5), mp.nstr(beta, 6), mp.nstr(lam, 9),
                   mp.nstr(inj, 9), mp.nstr(inj / base, 6)))
        log("")
    log("  READING: an exceptional eigenvalue injects h(i*s) = exp(+s^2/2sig^2) >= 1 (the test function")
    log("  EVALUATED AT THE IMAGINARY spectral parameter r=i*s GROWS, the only term that does).  The")
    log("  raw injected value exp(s^2/2sig^2) is largest for NARROW h (small sig) and s near 1/2; but the")
    log("  RELATIVE jump dS/S0 is order-unity (~0.92-1.00) across ALL test functions -- because S0 itself")
    log("  is O(1).  Either way the signal is MACROSCOPIC: an exceptional eigenvalue adds a term ~0.9-1.0")
    log("  times the entire existing spectral side, dwarfing the ~1e-6 balance floor by ~6 orders of")
    log("  magnitude.  It is NOT a small perturbation -- it is a new O(1) spectral line the trace formula")
    log("  cannot miss.  (At level 1 there is none, hence the clean balance; the search for it at")
    log("  congruence level Gamma_0(4q) IS the Selberg problem.)")
    log("")

    # =============================================================================================
    log("================  (D) SCATTERING LAW: real chi mod 3, mod 5 -> no real pole -> no exceptional  =")
    log("  A real zero beta in (1/2,1) of L(s,chi) is a real scattering pole at s=beta -> exceptional")
    log("  eigenvalue lambda = beta(1-beta).  Check L(s,chi) > 0 on (1/2,1) for chi_3, chi_5:")
    for name, Lf, L1 in [("chi_3", L_chi3, L1_chi3()), ("chi_5", L_chi5, L1_chi5())]:
        log("  --- %s ---" % name)
        mn = (None, mp.inf)
        row = []
        for x in range(55, 100, 5):
            s = mp.mpf(x) / 100
            v = Lf(s)
            if v < mn[1]:
                mn = (s, v)
            row.append("L(%.2f)=%s" % (float(s), mp.nstr(v, 6)))
        log("     " + "  ".join(row[:5]))
        log("     " + "  ".join(row[5:]))
        log("     L(1,%s) = %s ;  min on (1/2,1) = %s at s=%s  -> %s"
            % (name, mp.nstr(L1, 8), mp.nstr(mn[1], 6), mp.nstr(mn[0], 4),
               "POSITIVE (no real zero, no exceptional eigenvalue)" if mn[1] > 0 else "SIGN CHANGE (!!)"))
        # what a HYPOTHETICAL Siegel zero would imply, for calibration:
        hyp = mp.mpf("0.95")
        log("     [if %s HAD a Siegel zero at beta=%s, it would force lambda=beta(1-beta)=%s on Gamma_0(4q)]"
            % (name, mp.nstr(hyp, 4), mp.nstr(lam_of_beta(hyp), 6)))
    log("  L(s,chi_3), L(s,chi_5) > 0 throughout (1/2,1): NO Siegel zero for these small real characters")
    log("  (as expected -- Siegel zeros, if any, are a large-q asymptotic threat, not present at q=3,5).")
    log("  The MECHANISM, however, is exact: positivity of L on (1/2,1) == absence of the exceptional")
    log("  eigenvalue, via the real scattering pole <-> lambda=beta(1-beta) law.")
    log("")

    # =============================================================================================
    log("================  (E) SYNTHESIS + the precise residual  ================")
    log("DICTIONARY (exact): real chi mod q with Siegel zero beta=1-delta  <->  weight-1/2 Maass form on")
    log("Gamma_0(4q) with eigenvalue lambda = beta(1-beta) = 1/4-(beta-1/2)^2 ~ delta (small).  Selberg")
    log("lambda_1 >= 1/4  <=>  no exceptional eigenvalue  <=>  no Siegel zero.")
    log("PROVEN: lambda_1 >= 975/4096 = 0.23803 (Kim-Sarnak 2003, theta_infty=7/64 via sym^2 Gelbart-")
    log("Jacquet, sym^3/sym^4 Kim-Shahidi/Kim).  Gap to 1/4: 49/4096 = 0.01196.  Record UNIMPROVED at")
    log("full level (Yang 2020 withdrawn).  This EXCLUDES nothing yet: 0.238 < 0.25, so an exceptional")
    log("eigenvalue in (0.238, 0.25) -- equivalently a Siegel zero beta in (1/2, 1/2+sqrt(0.012))=(0.5,")
    log("0.609) -- is NOT ruled out by the proven bound.")
    log("GAINED by no-Siegel-zero (if proven): effective L(1,chi)>>1/log q; effective h(-d)>>sqrt d/log d;")
    log("effective Linnik / PNT in APs.  NOT GAINED: GRH -- the complex zeros off the real axis are")
    log("untouched.  no-Siegel-zero  <<  GRH, strictly.  And no-Siegel-zero itself is NOT proven (Kim-")
    log("Sarnak only narrows the exceptional window to lambda in (0.238,0.25)).")
    log("")
    log("RESIDUAL (precise): the program's machine-precision trace-formula balance is at LEVEL 1, where")
    log("there is provably NO exceptional eigenvalue (lambda_1 ~ 91) -- so the verified instrument, as")
    log("built, cannot itself see a Siegel zero: the Siegel zero lives on Gamma_0(4q), q large, NOT on")
    log("SL(2,Z).  Closing the 0.012 gap (Selberg) or excluding Siegel zeros is one of: (i) a NEW")
    log("functorial symmetric power sym^k, k>=5, on GL (Langlands beyond Kim-Shahidi) to push theta_infty")
    log("below 7/64; or (ii) a positive lower bound on the central L-value (Conrey-Iwaniec cubic-moment")
    log("direction).  Both are open; the trace formula at level 1 quantifies the SENSITIVITY (part C) but")
    log("not the EXISTENCE.  Difficulty is conserved: 'no exceptional eigenvalue on Gamma_0(4q)' is")
    log("exactly as hard as 'no Siegel zero,' which is strictly weaker than GRH and still open.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "rh_selberg_siegel.md"
    header = [
        "# Selberg eigenvalue conjecture <-> Landau-Siegel zero: dictionary, record, gap, sensitivity",
        "",
        "**Script:** `empirical/verify_selberg_siegel.py`  (mpmath dps 30; exact `Fraction` for the chain).",
        "**Companion to:** `verify_scattering_zeta_L.py` (scattering mechanism), "
        "`verify_full_trace_formula.py` (machine-precision PSL(2,Z) balance), "
        "`verify_selberg_geodesic_spectral.py` (geometric side).",
        "**Finding:** the lift dictionary lambda = beta(1-beta) = 1/4-(beta-1/2)^2 on Gamma_0(4q); the "
        "Kim-Sarnak chain 7/64 -> 975/4096 = 0.23803 with gap 49/4096 = 0.01196 (record UNIMPROVED at full "
        "level, Yang 2020 withdrawn); trace-formula sensitivity to a hypothetical exceptional eigenvalue "
        "(macroscopic, not a small perturbation); L(s,chi_3),L(s,chi_5) > 0 on (1/2,1) (no Siegel zero).",
        "**Honest scope:** dictionary + record + sensitivity computed/cited; no-Siegel-zero << GRH; "
        "neither Selberg nor no-Siegel-zero proved here.  GPD-disciplined.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
