"""
Determine sign of (Cstar - Cmin) on each envelope piece's B-interval.
sign(Cstar-Cmin) = sign(numerator) since (B^2+15B+68)>0.
If <=0 on the whole piece => Cmin>=Cstar => D2 closes (detW2<0 on all valid C there).
If >0 => there's a sub-band Cmin < C <= Cstar needing D3.
"""
from sympy import symbols, factor, Interval, solveset, S, Rational, oo
import sympy as sp

B = symbols('B', real=True)

pieces = [
    (2,  sp.Rational(-5), oo,         3*(B+5)*(B+7)*(B+12)),
    (3,  sp.Rational(-8), sp.Rational(-5),  4*(B+5)*(B+8)*(B+10)),
    (5,  sp.Rational(-12),sp.Rational(-8),  6*(B+7)*(B+8)**2),
    (7,  sp.Rational(-18),sp.Rational(-12), 8*(B+10)*(B**2+14*B+54)),
    (11, sp.Rational(-24),sp.Rational(-18), 12*(B**3+27*B**2+242*B+768)),
    (13, sp.Rational(-30),sp.Rational(-24), 2*(7*B**3+201*B**2+1880*B+6240)),
    (17, sp.Rational(-36),sp.Rational(-30), 6*(3*B**3+97*B**2+972*B+3440)),
    (19, sp.Rational(-42),sp.Rational(-36), 4*(5*B**3+171*B**2+1762*B+6384)),
]

for pk, lo, hi, num in pieces:
    # sample interior points to get sign; also report real roots in (lo,hi)
    aa = float(lo); bb = float(hi) if hi != oo else aa+10
    mids = [aa + (bb-aa)*t for t in (0.1,0.3,0.5,0.7,0.9)]
    if hi == oo:
        mids = [aa+1, aa+5, aa+50, aa+500]
    signs = []
    for m in mids:
        v = float(num.subs(B, m))
        signs.append('+' if v>0 else ('-' if v<0 else '0'))
    # real roots of num
    roots = sp.solve(sp.Eq(num,0), B)
    realroots = [r for r in roots if r.is_real]
    inrange = [r for r in realroots if (lo < r) and (hi == oo or r < hi)]
    print(f"p_k={pk}, B in ({lo},{hi}): signs at samples {list(zip([round(m,2) for m in mids],signs))}")
    print(f"     real roots of numerator: {[sp.nsimplify(r) for r in realroots]}")
    print(f"     roots INSIDE interval: {inrange}")
    allneg = all(s=='-' for s in signs)
    allpos = all(s=='+' for s in signs)
    verdict = ("Cmin>=Cstar on whole piece => D2 CLOSES" if allneg else
               ("Cstar>Cmin (band needs D3)" if allpos else "MIXED - need sub-split"))
    print(f"     => {verdict}\n")
