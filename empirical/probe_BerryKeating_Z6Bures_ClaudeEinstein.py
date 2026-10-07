"""Berry-Keating on the 2-channel Bures fiber.

Hilbert space:
  H_BK = L^2(R, dt) tensor C^2_K
  with C^2_K = K-parity fiber from the Z/6 Bures decomposition.

Hamiltonian (proposed):
  H = t * I_2 + B_G(1/2 + i t) * sigma_K
  where sigma_K = [[0, 1], [1, 0]] anti-commutes with K-parity.

This is a 2x2 matrix-valued multiplication operator on L^2(R, dt).
Its spectrum is the union of eigenvalues at each t:

  E_+- (t) = t +/- |B_G(1/2 + i t)|.

For the spectrum to match {gamma_n}, we'd want the eigenvalues to vanish at
zeta-zero ordinates.  But t = gamma_n with E = gamma_n requires
|B_G(1/2 + i gamma_n)| = 0, which contradicts the program's empirical fact
that B_G(rho) != 0 at zeta zeros.

So the multiplication-operator construction alone is too simple.

This probe verifies:
  (i) the FE/K-symmetry of H;
  (ii) the magnitude |B_G(1/2 + i t)| at and near zeta zeros;
  (iii) what the naive spectrum t +/- |B_G(t)| does.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 40


def chi3_L(s: mp.mpc) -> mp.mpc:
    return mp.power(3, -s) * (
        mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3)
    )


def B_G_at_critical(t: mp.mpf) -> mp.mpc:
    """Bures amplitude B_G(1/2 + i t) using the closed form from Addendum A4.

    B_G(s) = -(1/2 + 2^{-s} / 4) * L(s, chi_3)
    at s = 1/2 + i t.
    """
    s = mp.mpc(mp.mpf("0.5"), t)
    coeff = -(mp.mpf("0.5") + mp.power(2, -s) / 4)
    L_val = chi3_L(s)
    return coeff * L_val


def H_eigenvalues(t: mp.mpf) -> tuple[mp.mpc, mp.mpc]:
    """Eigenvalues of H = t*I + B_G(t)*sigma_x on C^2.

    For sigma_x = [[0, 1], [1, 0]], the 2x2 matrix
       [[t, B_G(t)], [B_G(t), t]]
    has eigenvalues t +/- B_G(t).
    """
    b = B_G_at_critical(t)
    return mp.mpc(t) + b, mp.mpc(t) - b


def main() -> None:
    gammas = [
        mp.mpf("14.134725141734693790457251983562"),
        mp.mpf("21.022039638771554992628479593897"),
        mp.mpf("25.010857580145688763213790992562"),
        mp.mpf("30.424876125859513210311897530585"),
        mp.mpf("32.935061587739189690662368964075"),
    ]

    print("=" * 100)
    print("Berry-Keating on 2-channel Bures fiber: H = t I + B_G(1/2+it) sigma_K")
    print("=" * 100)

    # (i) K-symmetry check: B_G(1/2 - i t) should be conjugate of B_G(1/2 + i t)
    print("\n(i) FE / K-symmetry: B_G(1/2 - i t) vs conj B_G(1/2 + i t)")
    for t in [mp.mpf("5"), mp.mpf("14.13"), mp.mpf("20"), mp.mpf("50")]:
        b_plus = B_G_at_critical(t)
        b_minus = B_G_at_critical(-t)
        b_plus_conj = mp.conj(b_plus)
        err = abs(b_minus - b_plus_conj)
        print(
            f"  t={float(t):>8.2f}  B_G(1/2+it)={complex(b_plus)}  "
            f"err(K-symm)={float(err):.3e}"
        )

    # (ii) |B_G| at zeta zeros
    print("\n(ii) |B_G(1/2 + i gamma_n)| at first 5 zeta zeros:")
    for n, g in enumerate(gammas, 1):
        b = B_G_at_critical(g)
        print(
            f"  gamma_{n}={float(g):.6f}  |B_G|={float(abs(b)):.6e}  "
            f"arg B_G={float(mp.arg(b)):+.4f}"
        )

    # (iii) Naive spectrum t +/- |B_G(t)| near gamma_1
    print("\n(iii) Naive eigenvalues E_+- = t +/- |B_G(t)| near gamma_1:")
    g1 = gammas[0]
    for dt in [
        mp.mpf("-0.5"),
        mp.mpf("-0.1"),
        mp.mpf("-0.01"),
        mp.mpf("0"),
        mp.mpf("0.01"),
        mp.mpf("0.1"),
        mp.mpf("0.5"),
    ]:
        t = g1 + dt
        e_plus, e_minus = H_eigenvalues(t)
        print(
            f"  t = gamma_1 + {float(dt):+.3g} = {float(t):.6f}  "
            f"E_+={complex(e_plus)}  E_-={complex(e_minus)}"
        )

    # Where would the eigenvalues vanish?
    print("\n(iv) Where does E_-(t) = t - B_G(t) vanish in real part?")
    print("    (i.e. t = Re B_G(t))")
    for t_try in [mp.mpf("5"), mp.mpf("14.135"), mp.mpf("20"), mp.mpf("50")]:
        b = B_G_at_critical(t_try)
        re_b = mp.re(b)
        print(
            f"  t={float(t_try):>8.3f}  Re B_G={float(re_b):+.6e}  "
            f"t - Re B_G = {float(t_try - re_b):+.6e}"
        )

    print("\nConclusion:")
    print("  The naive multiplication-form H = t I + B_G(t) sigma_K does NOT")
    print("  have spectrum at zeta-zero ordinates -- |B_G(gamma_n)| > 0 from")
    print("  the program's joint-non-vanishing fact.  The construction needs")
    print("  an additional differential / derivative coupling to access the")
    print("  zero structure (this is what de Branges m_B = -Xi'/Xi accomplishes).")
    print()
    print("  The Berry-Keating direction therefore requires the operator")
    print("  to include a derivative term -- not just multiplication on the")
    print("  Bures fiber.  This brings us back to the Krein canonical system")
    print("  (Addendum F6), now with the 2-channel structure as boundary data.")


if __name__ == "__main__":
    main()
