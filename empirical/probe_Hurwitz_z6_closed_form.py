"""Verify closed-form formulas for Hurwitz zeta values at r/6.

The identities are exact by residue-class decomposition and analytic
continuation.  This probe checks them near the critical line and at the first
zeta zeros, then verifies the simplified B_G formula for the canonical
G_balanced diagonal used in nueve/probe_A2.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 60


def zeta(s: mp.mpc) -> mp.mpc:
    return mp.zeta(s)


def L3(s: mp.mpc) -> mp.mpc:
    """Primitive quadratic character mod 3: chi3(1)=1, chi3(2)=-1."""
    return mp.power(3, -s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))


def L6_unit(s: mp.mpc) -> mp.mpc:
    """Unit-class mod-6 difference A_1-A_5."""
    return mp.power(6, -s) * (mp.zeta(s, mp.mpf(1) / 6) - mp.zeta(s, mp.mpf(5) / 6))


def hurwitz_direct(s: mp.mpc, r: int) -> mp.mpc:
    return mp.zeta(s, mp.mpf(r) / 6)


def hurwitz_closed(s: mp.mpc, r: int) -> mp.mpc:
    a = mp.power(2, -s)
    b = mp.power(3, -s)
    Z = zeta(s)
    L = L3(s)
    if r == 1:
        return mp.power(6, s) * (mp.mpf("0.5") * (1 - a) * (1 - b) * Z + mp.mpf("0.5") * (1 + a) * L)
    if r == 2:
        return mp.power(3, s) * mp.mpf("0.5") * ((1 - b) * Z + L)
    if r == 3:
        return (mp.power(2, s) - 1) * Z
    if r == 4:
        return mp.power(3, s) * mp.mpf("0.5") * ((1 - b) * Z - L)
    if r == 5:
        return mp.power(6, s) * (mp.mpf("0.5") * (1 - a) * (1 - b) * Z - mp.mpf("0.5") * (1 + a) * L)
    raise ValueError("r must be 1..5")


def F_closed(s: mp.mpc, r: int) -> mp.mpc:
    """Residue partial zeta F_r=6^-s zeta(s,r/6), with r=0 as multiples of 6."""
    a = mp.power(2, -s)
    b = mp.power(3, -s)
    Z = zeta(s)
    L = L3(s)
    if r == 0:
        return a * b * Z
    if r == 1:
        return mp.mpf("0.5") * (1 - a) * (1 - b) * Z + mp.mpf("0.5") * (1 + a) * L
    if r == 2:
        return mp.mpf("0.5") * a * ((1 - b) * Z + L)
    if r == 3:
        return b * (1 - a) * Z
    if r == 4:
        return mp.mpf("0.5") * a * ((1 - b) * Z - L)
    if r == 5:
        return mp.mpf("0.5") * (1 - a) * (1 - b) * Z - mp.mpf("0.5") * (1 + a) * L
    raise ValueError("r must be 0..5")


def B_G_direct(s: mp.mpc) -> mp.mpc:
    # Canonical diagonal from empirical/probe_A2_cumulant_tower.py:
    # g=[1,-1,1/2,-1/2,0,0], but B_G uses r=1..5.
    g = {1: -1, 2: mp.mpf("0.5"), 3: -mp.mpf("0.5"), 4: 0, 5: 0}
    return sum(mp.power(6, -s) * mp.zeta(s, mp.mpf(r) / 6) * g[r] for r in range(1, 6))


def B_G_closed(s: mp.mpc) -> mp.mpc:
    a = mp.power(2, -s)
    b = mp.power(3, -s)
    return zeta(s) * (-mp.mpf("0.5") + a * (3 - b) / 4) - (mp.mpf("0.5") + a / 4) * L3(s)


def fmt(z: mp.mpc) -> str:
    return f"{float(mp.re(z)):+.6e}{float(mp.im(z)):+.6e}j"


def check_point(s: mp.mpc) -> None:
    print(f"\ns = {fmt(s)}")
    max_abs = mp.mpf("0")
    for r in range(1, 6):
        direct = hurwitz_direct(s, r)
        closed = hurwitz_closed(s, r)
        err = abs(direct - closed)
        max_abs = max(max_abs, err)
        print(f"  r={r}: err={float(err):.3e}")
    l6_relation = abs(L6_unit(s) - (1 + mp.power(2, -s)) * L3(s))
    bg_err = abs(B_G_direct(s) - B_G_closed(s))
    print(f"  max Hurwitz err: {float(max_abs):.3e}")
    print(f"  L6_unit - (1+2^-s)L3 err: {float(l6_relation):.3e}")
    print(f"  B_G closed err: {float(bg_err):.3e}")


def check_zero_structure(t: float) -> None:
    s = mp.mpc(mp.mpf("0.5"), t)
    Z = zeta(s)
    L = L3(s)
    a = mp.power(2, -s)
    print(f"\nzero-height test t={t:.8f}, |zeta|={float(abs(Z)):.3e}, |L3|={float(abs(L)):.3e}")
    print(f"  F3={fmt(F_closed(s, 3))}")
    print(f"  F1+F5={fmt(F_closed(s, 1) + F_closed(s, 5))}")
    print(f"  F2+F4={fmt(F_closed(s, 2) + F_closed(s, 4))}")
    print(f"  F1-F5 predicted={(fmt((1+a)*L))}")
    print(f"  F2-F4 predicted={(fmt(a*L))}")
    print(f"  B_G direct={fmt(B_G_direct(s))}")
    print(f"  B_G at zero approx=-(1/2+2^-s/4)L3 = {fmt(-(mp.mpf('0.5') + a/4) * L)}")


if __name__ == "__main__":
    points = [
        mp.mpc("0.5", "14.13472514173469379046"),
        mp.mpc("0.5", "18.0"),
        mp.mpc("0.42", "21.02203963877155499263"),
        mp.mpc("0.63", "25.01085758014568876321"),
        mp.mpc("0.5", "32.93506158773918969066"),
    ]
    print("=" * 100)
    print("Closed-form Hurwitz zeta formulas at r/6")
    print("=" * 100)
    for point in points:
        check_point(point)

    print("\n" + "=" * 100)
    print("K-even/K-odd structure at zeta-zero heights")
    print("=" * 100)
    for t in [14.13472514173469379046, 21.02203963877155499263, 25.01085758014568876321]:
        check_zero_structure(t)
