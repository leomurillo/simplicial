r"""Selberg trace formula: the geometric (geodesic) side sum_D h_D (kernel of R_D) vs the spectral side,
and the 'Siegel zero = exceptional eigenvalue' correspondence -- made concrete, honestly scoped.

On the modular surface X = SL(2,Z)\H, the Selberg trace formula reads (schematically)
   sum_j h(r_j)  +  (continuous/Eisenstein, involves zeta)   [SPECTRAL: eigenvalues lambda_j = 1/4 + r_j^2]
   =  (Area/4pi) int h(r) r tanh(pi r) dr                    [identity / Weyl]
      + (elliptic, orders 2,3)
      + SUM OVER CLOSED GEODESICS:  sum_{prim gamma} sum_{k>=1} ( ell_gamma / (2 sinh(k ell_gamma/2)) ) g(k ell_gamma)
The geodesic sum is EXACTLY the user's sum_D h_D (kernel of R_D): primitive closed geodesics <-> primitive
indefinite binary quadratic forms <-> real quadratic discriminants D, with
   length ell_D = 2 log eps_D^+   (eps_D^+ = the norm-+1 fundamental unit; (t+u sqrt D)/2, t^2 - D u^2 = 4),
and multiplicity h_D (the form class number).  So the ARITHMETIC of real quadratic fields (regulators,
class numbers) IS the geometric side; the Laplacian eigenvalues are the spectral side; the trace formula
is the bridge.

THE CORRESPONDENCE (Siegel zero <-> exceptional eigenvalue): an eigenvalue lambda < 1/4 (r = i t imaginary,
'exceptional') is the spectral shadow of a Landau-Siegel zero of the relevant L-function -- AT CONGRUENCE
LEVEL Gamma_0(q) (the theta/metaplectic level where the weight-1/2 forms live).  Selberg's conjecture
lambda_1 >= 1/4 <=> no exceptional eigenvalue; the PROVEN partial bound Kim-Sarnak lambda_1 >= 975/4096
~ 0.238 is EFFECTIVE.  For SL(2,Z) ITSELF (level 1) the smallest eigenvalue is lambda_1 ~ 91.14 (r_1 ~
9.534) >> 1/4 -- NO exceptional eigenvalue, so no Siegel-analogue at level 1; the action is at the level.

This probe: (1) computes the geodesic length spectrum {(ell_D, h_D)} (geometric data; validates ell_min);
(2) evaluates the geodesic sum sum_D h_D (kernel) for a test function (short-geodesic dominated);
(3) lists the spectral side (cited Maass eigenvalues; lambda_1 >> 1/4); (4) states the correspondence.
NOT a full numerical trace-formula balance (the continuous/zeta term is not implemented) and NOT a search
for exceptional eigenvalues -- it makes the geometric side and the dictionary concrete.  Labelled.
"""

import sys
from math import isqrt
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 25


def squarefree(n):
    n = abs(n); i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return False
        i += 1
    return n > 0


def is_fund_disc(D):
    if D in (0, 1):
        return False
    if D % 4 == 1:
        return squarefree(D)
    if D % 4 == 0:
        m = D // 4
        return (m % 4 in (2, 3)) and squarefree(m)
    return False


def geodesic_length(D, umax=20000):
    # fundamental automorph: smallest u>=1 with D u^2 + 4 a perfect square t^2, t>2.  ell = 2 acosh(t/2).
    for u in range(1, umax + 1):
        val = D * u * u + 4
        t = isqrt(val)
        if t * t == val and t > 2:
            return 2 * mp.acosh(mp.mpf(t) / 2), t, u
    return None


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    # small known form/narrow class numbers for the short discriminants (multiplicity h_D)
    hD = {5: 1, 8: 1, 12: 1, 13: 1, 17: 1, 21: 1, 24: 1, 28: 1, 29: 1, 33: 1, 37: 1,
          40: 2, 41: 1, 44: 1, 53: 1, 56: 1, 57: 1, 60: 2, 61: 1, 65: 2}

    # ---- (1) geodesic length spectrum ----
    log("================  (1) geodesic length spectrum {(ell_D, h_D)} -- the GEOMETRIC side data  ====")
    spec = []
    for D in range(5, 70):
        if not is_fund_disc(D):
            continue
        g = geodesic_length(D)
        if g is None:
            continue
        ell, t, u = g
        spec.append((ell, D, hD.get(D, None), t, u))
    spec.sort()
    log("   length ell_D    D    h_D    automorph (t,u): t^2-Du^2=4    eps_D^+=(t+u sqrt D)/2")
    for ell, D, h, t, u in spec[:12]:
        eps = (t + u * mp.sqrt(D)) / 2
        log("   %s     %3d   %s     (%d,%d)                  %s"
            % (mp.nstr(ell, 8), D, str(h) if h is not None else "?", t, u, mp.nstr(eps, 7)))
    ellmin = spec[0][0]
    log("  shortest geodesic: ell_min = %s at D=5  (known value 2*acosh(3/2) = %s)  match: %s"
        % (mp.nstr(ellmin, 8), mp.nstr(2 * mp.acosh(mp.mpf(3) / 2), 8),
           abs(ellmin - 2 * mp.acosh(mp.mpf(3) / 2)) < mp.mpf(10) ** -10))
    log("  (ell_D = 2 log eps_D^+; for D=5, eps_5^+ = phi^2, so ell_5 = 4 log phi = 4 R_5.)")
    log("")

    # ---- (2) the geodesic sum  sum_D h_D (kernel of R_D)  for a test function ----
    log("================  (2) the geodesic sum  G = sum_D h_D sum_k ell_D/(2 sinh(k ell_D/2)) g(k ell_D)  =")
    sigma = mp.mpf(2)
    g = lambda u: mp.e ** (-(u ** 2) / (2 * sigma ** 2))   # Gaussian test function on lengths
    log("  test function g(u) = exp(-u^2/(2*%s^2)); contributions by discriminant (k=1 primitive):" % sigma)
    G = mp.mpf(0)
    contribs = []
    for ell, D, h, t, u in spec:
        if h is None:
            continue
        term = mp.mpf(0)
        k = 1
        while True:
            kl = k * ell
            t_k = (ell / (2 * mp.sinh(kl / 2))) * g(kl)
            term += h * t_k
            if t_k < mp.mpf(10) ** -12:
                break
            k += 1
        G += term
        contribs.append((term, D))
    contribs.sort(reverse=True)
    for term, D in contribs[:6]:
        log("     D=%3d : %s   (%.1f%% of G)" % (D, mp.nstr(term, 6), float(100 * term / G)))
    log("  geodesic-side total G = %s   -- a convergent sum DOMINATED by the shortest geodesic (D=5)."
        % mp.nstr(G, 8))
    log("  This is literally sum_D h_D (kernel of R_D): the real-quadratic arithmetic, as the geometric side.")
    log("")

    # ---- (3) the spectral side (cited) ----
    log("================  (3) the SPECTRAL side: Laplacian eigenvalues lambda_j = 1/4 + r_j^2  ========")
    maass_r = [mp.mpf(x) for x in ["9.533695", "12.173008", "13.779751", "14.358509",
                                   "16.138073", "16.644259", "17.738563", "18.180918"]]
    log("  first SL(2,Z) Maass cusp-form spectral parameters r_j (cited; Hejhal/LMFDB):")
    log("    " + ", ".join(mp.nstr(r, 7) for r in maass_r[:6]))
    log("  lambda_1 = 1/4 + r_1^2 = %s  >>  1/4 = 0.25." % mp.nstr(mp.mpf(1) / 4 + maass_r[0] ** 2, 8))
    log("  => SL(2,Z) (level 1) has NO exceptional eigenvalue (lambda < 1/4): Selberg holds trivially")
    log("     here; there is no Siegel-zero analogue at level 1.")
    # Weyl term: N(lambda) ~ (Area/4pi) lambda, Area(SL2Z\H) = pi/3, so N(lambda) ~ lambda/12
    log("  Weyl law: N(lambda) ~ (Area/4pi) lambda = lambda/12  (Area = pi/3); the smooth eigenvalue count.")
    log("")

    # ---- (4) the correspondence, concrete ----
    log("================  (4) 'Siegel zero = exceptional eigenvalue', made concrete  ================")
    log("The trace formula equates the GEOMETRIC side -- (Weyl) + (elliptic) + the geodesic sum sum_D h_D")
    log("(kernel of R_D), i.e. the REAL-QUADRATIC ARITHMETIC of step (2) -- to the SPECTRAL side, the")
    log("Laplacian eigenvalues of step (3) (plus the zeta-laden continuous term).  An EXCEPTIONAL")
    log("eigenvalue lambda = 1/4 - s^2 (0<s<1/2; r = i s) is the spectral shadow of a Landau-Siegel zero")
    log("beta = 1/2 + s of the associated real L-function -- at CONGRUENCE LEVEL Gamma_0(q) (the theta /")
    log("metaplectic level, weight 1/2, Kohnen plus space; Shimura-Waldspurger).  As beta -> 1 (s -> 1/2)")
    log("the eigenvalue lambda -> 0.  Selberg's lambda_1 >= 1/4 <=> no exceptional eigenvalue <=> (via the")
    log("theta lift) control of the Siegel zero; the PROVEN Kim-Sarnak lambda_1 >= 975/4096 ~ 0.238 is the")
    log("effective partial result -- 0.238 of the 0.250 wall, the teeth the ineffective Siegel bound lacks.")
    log("")
    log("HONEST SCOPE: computed -- the geodesic length spectrum (geometric data, validated) and the")
    log("geodesic sum sum_D h_D (kernel); cited -- the SL(2,Z) Maass eigenvalues and Kim-Sarnak; NOT done")
    log("-- a full geometric=spectral balance (needs the zeta-scattering continuous term) and a search for")
    log("exceptional eigenvalues (none at level 1; at congruence level it is the open Selberg problem).")
    log("The payoff: the real-quadratic arithmetic (regulators R_D, class numbers h_D) IS the geometric")
    log("side of a Laplace spectrum; the Siegel zero is an exceptional eigenvalue; and the spectral side")
    log("carries proven effective traction (Kim-Sarnak) the arithmetic side does not.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "selberg_geodesic_spectral.md"
    header = [
        "# Selberg trace formula: sum_D h_D (kernel of R_D) geometric side vs the spectral side",
        "",
        "**Script:** `empirical/verify_selberg_geodesic_spectral.py`",
        "**Context:** makes the geodesic (geometric) side and the 'Siegel zero = exceptional eigenvalue'",
        "correspondence concrete for the real-quadratic Siegel core.",
        "**Finding:** geodesic length spectrum ell_D=2 log eps_D^+ (ell_min=2acosh(3/2)=1.9248 at D=5),",
        "weighted by h_D, IS the trace-formula geometric side; spectral side has lambda_1~91>>1/4 at level 1",
        "(no exceptional eigenvalue); Siegel zero <-> exceptional eigenvalue at congruence level, Kim-Sarnak 0.238/0.25.",
        "**Nature:** numerical (geometric side computed/validated) + cited (eigenvalues, Kim-Sarnak).  NOT a full balance.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
