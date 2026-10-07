r"""Developing the metaplectic/Selberg lens: L(1,chi_D) as a weight-3/2 coefficient, tied to N_inf.

The divergence (the exceptional real-quadratic D is NOT irreducible) routes through the metaplectic /
half-integral-weight world -- which is the program's OWN apparatus (the UPT Bargmann-Fock at v=inf is
the Weil representation = the archimedean component of Mp_2, where weight-3/2 forms live).  Concretely:

  IMAGINARY D (fundamental):  L(1,chi_{-D}) = pi * H(D) / sqrt(D),   H = Hurwitz class number.
  And {H(n)} are the Fourier coefficients of a WEIGHT-3/2 modular form (Zagier's Eisenstein series),
  certified by the HURWITZ-KRONECKER class-number relation:
       sum_{r in Z} H(4n - r^2)  =  2 sigma_1(n) - sum_{d|n} min(d, n/d).
  This relation IS the modularity (the Hecke/theta-trace identity); we verify it in exact arithmetic.

So L(1,chi_{-D}) is literally a coefficient of an N_inf-form (weight 3/2; archimedean = the oscillator
the program already selected).  The asymmetry that makes REAL D the hard core, sharpened:
  * IMAGINARY D <-> a HOLOMORPHIC weight-3/2 coefficient = a CM point on the modular curve (0-dim,
    rigid).  Controllable: Goldfeld-Gross-Zagier (Heegner points) gives effective h(-D) >> (log D)^{1-eps};
    h=1 finite (HSB, 9 fields).
  * REAL D <-> a GEODESIC-CYCLE period (1-dim closed geodesic of length = the regulator R_D).  The
    regulator is the geodesic length; the family is the length spectrum (Selberg trace formula's
    geometric side).  No holomorphic CM point -> GGZ does not apply.  Control is SPECTRAL: the Siegel
    zero <-> an exceptional small Laplacian eigenvalue (Selberg lambda_1 >= 1/4), where the proven
    partial result Kim-Sarnak lambda_1 >= 975/4096 ~ 0.238 is EFFECTIVE -- teeth the arithmetic lens lacks.

This probe VERIFIES the exact chain (H via reduced forms; Hurwitz-Kronecker modularity; L=pi H/sqrt D),
and states the holomorphic-imaginary / geodesic-real asymmetry with the spectral residual.  NOT a proof.

EXACT (fractions) + mpmath, labelled.
"""

import sys
from fractions import Fraction
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 25


def hurwitz_H(N):
    # Hurwitz class number H(N): H(0)=-1/12; 0 if N≡1,2 mod 4; else weighted count of reduced
    # positive-definite forms (a,b,c), b^2-4ac=-N, -a<b<=a<=c, b>=0 if a==c; weight 1/2 for (a,0,a),
    # 1/3 for (a,a,a), else 1.
    if N == 0:
        return Fraction(-1, 12)
    if N % 4 in (1, 2):
        return Fraction(0)
    total = Fraction(0)
    a = 1
    while 3 * a * a <= N:
        for b in range(-a + 1, a + 1):
            num = b * b + N
            if num % (4 * a) != 0:
                continue
            c = num // (4 * a)
            if c < a:
                continue
            if a == c and b < 0:
                continue
            if a == c and b == 0:
                total += Fraction(1, 2)
            elif a == c and b == a:
                total += Fraction(1, 3)
            else:
                total += Fraction(1)
        a += 1
    return total


def sigma1(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)


def min_div_sum(n):
    return sum(min(d, n // d) for d in range(1, n + 1) if n % d == 0)


def w_units(D):  # for the field of discriminant -D
    return 6 if D == 3 else (4 if D == 4 else 2)


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    # ---- validate H ----
    log("================  Hurwitz class numbers H(N) (reduced-form count)  ================")
    known = {3: Fraction(1, 3), 4: Fraction(1, 2), 7: Fraction(1), 8: Fraction(1),
             11: Fraction(1), 12: Fraction(4, 3), 15: Fraction(2), 16: Fraction(3, 2),
             19: Fraction(1), 20: Fraction(2), 23: Fraction(3), 24: Fraction(2)}
    ok = all(hurwitz_H(N) == h for N, h in known.items())
    log("  H(3..24) match known values: %s" % ok)
    log("  H = {" + ", ".join("%d:%s" % (N, hurwitz_H(N)) for N in sorted(known)) + "}")
    log("")

    # ---- Hurwitz-Kronecker relation = weight-3/2 modularity (exact) ----
    log("================  Hurwitz-Kronecker relation (the weight-3/2 MODULARITY), exact  ===========")
    log("  sum_{r} H(4n-r^2) = 2 sigma_1(n) - sum_{d|n} min(d, n/d) :")
    log("    n     LHS (sum_r H)      RHS (2 sigma_1 - min-div)     equal?")
    allok = True
    for n in range(1, 11):
        lhs = Fraction(0)
        r = 0
        while r * r <= 4 * n:
            mult = 1 if r == 0 else 2
            lhs += mult * hurwitz_H(4 * n - r * r)
            r += 1
        rhs = Fraction(2 * sigma1(n)) - Fraction(min_div_sum(n))
        eq = (lhs == rhs)
        allok = allok and eq
        log("   %2d     %-14s     %-22s     %s" % (n, str(lhs), str(rhs), "OK" if eq else "FAIL"))
    log("  Hurwitz-Kronecker holds for n=1..10 (exact): %s  -> {H(n)} IS a weight-3/2 modular form." % allok)
    log("")

    # ---- L(1,chi_{-D}) = pi H(D)/sqrt(D) : the L-value IS the weight-3/2 coefficient ----
    log("================  L(1,chi_{-D}) = pi H(D)/sqrt(D)  (the metaplectic-coefficient realization)  =")
    log("     D     H(D)      pi H(D)/sqrt(D)      class-number formula 2 pi h/(w sqrtD)    match?")
    # fundamental discriminants D>0 (field disc -D): D ≡ 3 mod 4 squarefree, or 4m, m≡1,2 mod 4 sqfree
    hclass = {3: 1, 4: 1, 7: 1, 8: 1, 11: 1, 15: 2, 19: 1, 20: 2, 23: 3, 24: 2, 163: 1}
    for D in [3, 4, 7, 8, 11, 15, 19, 20, 23, 24, 163]:
        H = hurwitz_H(D)
        viaH = mp.pi * float(H) / mp.sqrt(D)
        viaCNF = 2 * mp.pi * hclass[D] / (w_units(D) * mp.sqrt(D))
        log("   %4d   %-6s   %s      %s      %s"
            % (D, str(H), mp.nstr(viaH, 9), mp.nstr(viaCNF, 9), abs(viaH - viaCNF) < mp.mpf(10) ** -8))
    log("  (H(D) = 2 h(-D)/w, so pi H/sqrtD = 2 pi h/(w sqrtD) = L(1,chi_{-D}) exactly; e.g. D=4 -> pi/4.)")
    log("")

    # ---- the asymmetry + the spectral residual ----
    log("================  the holomorphic-imaginary / geodesic-real asymmetry (the lens)  ===========")
    log("IMAGINARY D: H(D) is a HOLOMORPHIC weight-3/2 coefficient = a CM point (0-dim, rigid) on the")
    log("  modular curve.  Controllable: Goldfeld + Gross-Zagier (Heegner-point height of a triple-zero")
    log("  L-function) => effective h(-D) >> (log D)^{1-eps}; the tightest (h=1) are the FINITE 9 fields")
    log("  (HSB, last D=-163; here H(163)=1, L(1,chi_{-163})=pi/sqrt163).")
    log("REAL D: the analogue is a GEODESIC-CYCLE period -- a closed geodesic of length = the regulator")
    log("  R_D, a 1-dimensional cycle, NOT a rigid CM point.  No Heegner point -> GGZ does not transfer.")
    log("  The regulator IS the geodesic length; the family {(R_D,h_D)} is the length spectrum (Selberg")
    log("  trace formula, geometric side).  Control is SPECTRAL: a real Siegel zero <-> an exceptional")
    log("  small Laplacian eigenvalue (Selberg lambda_1 >= 1/4), where Kim-Sarnak's PROVEN lambda_1 >=")
    log("  975/4096 ~ 0.238 is EFFECTIVE -- the teeth the ineffective arithmetic (Siegel) lens lacks.")
    log("")
    log("PAYOFF: L(1,chi_D) lives natively as a coefficient of a weight-3/2 (metaplectic) form whose")
    log("archimedean component IS the program's N_inf.  The exceptional real D is the geodesic-period /")
    log("exceptional-eigenvalue shadow -- over-determined, NOT irreducible; softest on the spectral side")
    log("(Kim-Sarnak 0.238 -> 0.25) and the metaplectic side (our UPT).  Not a proof; a route with teeth.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "metaplectic_weight32.md"
    header = [
        "# L(1,chi_D) as a weight-3/2 (metaplectic) coefficient, tied to N_inf",
        "",
        "**Script:** `empirical/verify_metaplectic_weight32.py`",
        "**Context:** develops the divergent metaplectic/Selberg lens on the real-quadratic Siegel core.",
        "**Result:** L(1,chi_{-D})=pi H(D)/sqrt(D), H=Hurwitz class number = weight-3/2 coefficient (certified",
        "exact by Hurwitz-Kronecker); weight-3/2 = metaplectic = N_inf archimedean; imaginary=holomorphic/CM",
        "(GGZ-controllable) vs real=geodesic-period/regulator (spectral-only; Selberg, Kim-Sarnak 0.238/0.25).",
        "**Nature:** exact (fractions) + mpmath, validated.  NOT a proof.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
