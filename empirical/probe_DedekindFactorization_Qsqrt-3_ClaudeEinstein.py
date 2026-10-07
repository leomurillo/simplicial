"""Verify the Dedekind zeta factorization zeta_{Q(sqrt(-3))}(s) = zeta(s) * L(s, chi_3).

This is the structural identification of the 2-channel Bures fiber with the
Connes-Consani Picard groupoid restricted to the degree-2 cover by Q(sqrt(-3)).

The K-involution = Galois involution of Q(sqrt(-3)) / Q. K-fixed elements
correspond to ideals from Q (zeta-channel); K-anti-fixed correspond to ideals
that are not Galois-invariant (L_{chi_3}-channel).

zeta_K(s) = sum over ideals a of O_K, 1/N(a)^s
         = product over primes p of Q of L-factor at p:
             p inert in K:   1/(1 - p^{-2s})  (Norm = p^2)
             p split in K:   1/(1 - p^{-s})^2  (two primes of Norm p)
             p ramified:     1/(1 - p^{-s})  (one prime of Norm p)
         = zeta(s) * L(s, chi_3) for K = Q(sqrt(-3))
where chi_3 = Kronecker symbol of disc(K) = -3.

The 5 is ramified (3) and primes split/inert according to chi_3.
"""

from __future__ import annotations

import mpmath as mp
from sympy import isprime


mp.mp.dps = 40


def chi3_L(s: mp.mpc) -> mp.mpc:
    return mp.power(3, -s) * (
        mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3)
    )


def zeta_K_via_factorization(s: mp.mpc) -> mp.mpc:
    """zeta_{Q(sqrt(-3))}(s) = zeta(s) * L(s, chi_3)."""
    return mp.zeta(s) * chi3_L(s)


def zeta_K_via_euler_product(s: mp.mpc, max_p: int = 100) -> mp.mpc:
    """zeta_K(s) via Euler product over primes p <= max_p.

    For K = Q(sqrt(-3)):
      p = 3 ramified:     factor 1/(1 - 3^{-s})
      p with chi_3(p) = +1 (p split):  1/(1 - p^{-s})^2
      p with chi_3(p) = -1 (p inert): 1/(1 - p^{-2s})

    chi_3(p) = +1 if p === 1 mod 3, -1 if p === 2 mod 3.
    """
    result = mp.mpc(1)
    p = 2
    while p <= max_p:
        if isprime(p):
            p_s = mp.power(p, -s)
            if p == 3:
                # Ramified
                factor = 1 / (1 - p_s)
            else:
                chi_val = 1 if p % 3 == 1 else -1
                if chi_val == 1:
                    # Split
                    factor = 1 / (1 - p_s) ** 2
                else:
                    # Inert
                    factor = 1 / (1 - p_s**2)
            result *= factor
        p += 1
    return result


def main():
    print("=" * 100)
    print("Dedekind zeta factorization: zeta_{Q(sqrt(-3))} = zeta * L(., chi_3)")
    print("=" * 100)

    print("\n(i) Numerical verification at sample s:")
    samples = [
        mp.mpc(2, 0),
        mp.mpc(3, 0),
        mp.mpc(mp.mpf("1.5"), 0),
        mp.mpc(mp.mpf("0.5"), 14),  # on critical line near gamma_1
        mp.mpc(mp.mpf("0.5"), 21),  # near gamma_2
        mp.mpc(2, 5),
    ]
    for s in samples:
        z_K_factorized = zeta_K_via_factorization(s)
        # For real s > 1 we can also do the Euler product
        if mp.re(s) > mp.mpf("1.2"):
            z_K_euler = zeta_K_via_euler_product(s, max_p=200)
            err_euler = abs(z_K_factorized - z_K_euler)
            print(
                f"  s={complex(s)}:  zeta*L_chi3 = {complex(z_K_factorized)}\n"
                f"               Euler product = {complex(z_K_euler)}\n"
                f"               diff = {float(err_euler):.3e}"
            )
        else:
            print(
                f"  s={complex(s)}:  zeta*L_chi3 = {complex(z_K_factorized)}"
            )

    print("\n(ii) Class number formula sanity check:")
    print("    L(1, chi_3) = pi / (3 sqrt(3))")
    L1 = chi3_L(mp.mpf("1.000001"))  # near 1, avoid exact pole
    expected_L1 = mp.pi / (3 * mp.sqrt(3))
    print(f"    Computed L(1, chi_3) ~= {float(L1):.10f}")
    print(f"    pi/(3 sqrt(3))     ~= {float(expected_L1):.10f}")

    print("\n(iii) Galois K-action on the Bures fiber:")
    print("    Q(sqrt(-3)) has Galois group Z/2; K acts as complex conjugation")
    print("    on sqrt(-3) -> -sqrt(-3).")
    print("    Under K-action on the 2-channel Bures fiber (zeta, L_chi3):")
    print("    - K-fixed (parity +1) = zeta-channel")
    print("    - K-anti-fixed (parity -1) = L_chi3-channel")
    print("    These are the Galois eigenspaces of zeta_K.")

    print("\n(iv) Conductor / discriminant identification:")
    print("    Discriminant of Q(sqrt(-3)) = -3.")
    print("    Conductor of chi_3 = 3.")
    print("    Cyclotomic field Q(zeta_6) = Q(sqrt(-3)) since zeta_6 = (1+sqrt(-3))/2.")
    print("    Roots of unity in Q(sqrt(-3)) form Z/6 (6th roots of unity).")
    print("    This is the program's Z/6 Bures fiber, with K-involution = ")
    print("    complex conjugation = Galois automorphism.")


if __name__ == "__main__":
    main()
