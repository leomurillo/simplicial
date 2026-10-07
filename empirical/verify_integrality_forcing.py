r"""Front (b): the integrality that would force the marginal R(0) <= 1 to be STRICT (R(0) < 1).

Diagnosis (from the proof-strategy synthesis): soft/analytic methods are symmetric under RH-true/false
near the line, hence MARGINAL (R(0) ~ 0.9999, never strict).  A proof needs a THIRD input that breaks
the symmetry.  Over function fields that input is INTEGRALITY: integer point counts -> integer
Frobenius trace a -> the Hasse bound a^2 <= 4q is an INTEGER inequality, so its violation would be a
NEGATIVE INTEGER (<= -1) -- strictness is automatic, the margin can never be a tiny positive number.

PART A -- the function-field integer protection (the template, [P] in-house, P4/פWeil):
  Fermat cubic C: x^3+y^3+z^3=0 over F_q.  a = q+1 - #C(F_q) (integer, exact point count).
  RH-for-the-curve = |alpha|=sqrt(q) <=> 4q - a^2 >= 0 (Hasse).  The margin 4q-a^2 is an INTEGER >= 1
  for ordinary q -- it CANNOT be marginal.  And q = N(J) = a'^2 - a'b' + b'^2 (Eisenstein-integer
  norm of the Jacobi sum): sqrt(q) is an ALGEBRAIC identity, not an analytic limit.

PART B -- the number-field count integrality (the candidate third input; Turing / Lefschetz analogue):
  N(T) = #{zeros up to T} is an INTEGER.  Riemann-von Mangoldt: N(T) = theta(T)/pi + 1 + S(T), with
  theta the Riemann-Siegel theta (the archimedean/Gamma phase, NON-integer/continuous) and
  S(T) = (1/pi) arg zeta(1/2+iT) the fluctuation.  The integer count is the rigidity: at each zero N
  jumps by +1.  RH <=> (on-line count) = (total count) for all T.  Since both are INTEGERS, an
  analytic near-miss |on-line - total| < 1 would force EXACT equality (this is Turing's method, which
  proves RH in finite ranges).  The obstruction to all T is a uniform S(T) bound -- which is RH.

PART C -- contrast + unification with front (a):
  function field: margin 4q-a^2 is an INTEGER >= 1 (strict, protected).
  number field:   1 - R(0) ~ 0.0003 (cumulant corner) -- CONTINUOUS, -> 0, NO integer floor; and the
  primorial Hankel minor D_3 = -787680 is an integer but NEGATIVE (the smooth primorial is the wrong
  object, P6).  The third input = an integer-valued spectral count: front (a)'s operator H, if
  self-adjoint, makes N(T) = #eigenvalues an integer automatically -- the integrality IS the operator.
  Fronts (a) and (b) are the same: the operator supplies the integer count; the count rigidity forces
  the marginal R(0) < 1 strict; both = RH.

NUMERICAL/EXACT (mpmath + exact integer point counts), labelled.  NOT a proof.
"""

import sys
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
mp.mp.dps = 25


def fermat_cubic_proj_count(q):
    """Exact count of projective points of x^3+y^3+z^3=0 over F_q (q prime, q != 3)."""
    cubes = [pow(t, 3, q) for t in range(q)]
    cnt = 0
    for x in range(q):
        cx = cubes[x]
        for y in range(q):
            cxy = cx + cubes[y]
            for z in range(q):
                if (x or y or z) and (cxy + cubes[z]) % q == 0:
                    cnt += 1
    return cnt // (q - 1)


def eisenstein_norm_rep(q):
    """Find integers (a,b) with a^2 - a b + b^2 = q (norm form of Z[omega]); None if q inert."""
    r = int(q ** 0.5) + 2
    for a in range(-r, r + 1):
        for b in range(-r, r + 1):
            if a * a - a * b + b * b == q:
                return (a, b)
    return None


def main():
    out = []

    def log(s=""):
        print(s); out.append(s)

    log(__doc__)

    # ---------- PART A : function-field integer protection ----------
    log("================  PART A : function field -- the Hasse margin is an INTEGER >= 1  ==========")
    log("   q   type        #C(F_q)   a=q+1-#C   4q-a^2 (margin, INTEGER)   q=a'^2-a'b'+b'^2 (Eisenstein)")
    for q in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43]:
        N = fermat_cubic_proj_count(q)
        a = q + 1 - N
        margin = 4 * q - a * a
        typ = "split(ord)" if q % 3 == 1 else "inert(ss) "
        eis = eisenstein_norm_rep(q)
        eis_s = ("%d^2-%d*%d+%d^2=%d" % (eis[0], eis[0], eis[1], eis[1], q)) if eis else "(inert: q=N(q))"
        log("  %2d   %s   %4d      %+3d        %4d  (>=1, strict)        %s"
            % (q, typ, N, a, margin, eis_s))
    log("  -> the positivity margin 4q-a^2 is a NON-NEGATIVE INTEGER; for ordinary q it is >= 1.")
    log("     It cannot be a tiny positive number: integrality makes RH-for-the-curve STRICT.")
    log("     (Supersingular q==2 mod 3: a=0 exactly, margin=4q.)  And q is an Eisenstein-integer")
    log("     norm -> sqrt(q) is an algebraic identity, not an analytic limit.")
    log("")

    # ---------- PART B : number-field count integrality (Turing / Lefschetz analogue) ----------
    log("================  PART B : number field -- the zero count N(T) is an INTEGER  ==============")
    log("  N(T) = theta(T)/pi + 1 + S(T):  smooth archimedean phase (continuous) + integer count.")
    log("    T      N(T)=#zeros(int)   theta(T)/pi + 1 (smooth, NON-int)    S(T)=N - smooth")
    for T in [30, 50, 100, 200, 500]:
        NT = mp.nzeros(T)                       # exact integer count of zeros up to T
        smooth = mp.siegeltheta(T) / mp.pi + 1  # archimedean (Gamma-phase) smooth term
        S = NT - smooth
        log("   %4d     %5d            %s            %s"
            % (T, NT, mp.nstr(smooth, 10), mp.nstr(S, 6)))
    log("  -> N(T) is an INTEGER; the smooth archimedean term is not; S(T) is the fluctuation that")
    log("     snaps the total to an integer.  The integer count is the rigidity (Turing's method:")
    log("     |on-line count - N(T)| < 1  =>  EXACT equality  =>  RH in that range).  The uniform-in-T")
    log("     version (a global S(T) bound) is RH -- the integer floor exists, the analytic bound is open.")
    log("")

    # ---------- PART C : contrast + unification with front (a) ----------
    log("================  PART C : the contrast, and why fronts (a)+(b) are one  ================")
    log("  function field:  margin = 4q - a^2  is an INTEGER >= 1   (strict, integer-protected).")
    log("  number field:    1 - R(0) ~ 0.0003  (cumulant corner)    CONTINUOUS, -> 0, NO integer floor;")
    log("                   primorial Hankel D_3 = -787680 is an integer but NEGATIVE (wrong object, P6).")
    log("")
    log("  The third input that breaks the RH-true/false symmetry = an INTEGER-VALUED count.  Over F_q")
    log("  it is the Lefschetz/point count (Frobenius an endomorphism).  Over Q it is the spectral count")
    log("  N(T) = #eigenvalues of the Hilbert-Polya operator H (front a): if H is self-adjoint, N(T) is")
    log("  automatically an integer, and (on-line count)=(total count) is an INTEGER equality that a")
    log("  near-miss upgrades to exact.  So:")
    log("    FRONT (a) supplies the operator;  FRONT (b) = its integer spectral count is the integrality;")
    log("    the count rigidity forces the marginal R(0) < 1 to be STRICT.  Both fronts = the SAME RH.")
    log("  The archimedean integrality is the integer zero-count -- the number-field shadow of the")
    log("  function-field Lefschetz integer point count.  NOT a proof: the uniform analytic bound that")
    log("  would let integrality close it (global S(T), or self-adjointness of H) is RH itself.")

    from pathlib import Path
    rep = Path(__file__).resolve().parent / "reports" / "integrality_forcing.md"
    header = [
        "# Front (b): the integrality that would force R(0) < 1 strict",
        "",
        "**Script:** `empirical/verify_integrality_forcing.py`",
        "**Context:** front (b); the third input = an integer-valued count (Hasse gap / spectral count).",
        "**Finding:** function-field margin 4q-a^2 is an integer >= 1 (strict); number-field 1-R(0) has no",
        "integer floor; the candidate third input is the integer zero-count N(T) = #eigenvalues of front (a)'s H.",
        "**Nature:** exact integer point counts + mpmath; labelled.  NOT a proof.",
        "",
        "```text",
    ]
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text("\n".join(header + out + ["```", ""]), encoding="utf-8")
    print("\n[report -> %s]" % rep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
