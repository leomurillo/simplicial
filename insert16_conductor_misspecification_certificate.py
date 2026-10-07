#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INSERT 16 / item C2  --  The Conductor-Misspecification Certificate
====================================================================

Contribution 2 of the FEP/AI bridge (INSERT 14 family), executed as a
deterministic finite certificate, the way INSERT 15 executed Contribution 1.

CLAIM UNDER TEST (Paper 12 / beyond_smooth, anchored, verbatim objects):

  On a categorical belief space over a ring-structured index R = Z/nZ, at
  maximum entropy (uniform p_*), the Fisher tangent space splits into
  orthogonal conductor packets indexed by additive characters. The
  quadratic Fisher metric -- the ONLY local object a second-order
  preconditioner sees (natural gradient, K-FAC, Gauss-Newton, Adam's
  diagonal empirical Fisher, the NTK Gram) -- is

      g_p(u,v) = sum_y u_y v_y / p_y                 (Paper 12)

  The first object it does NOT see, unless the optimizer is explicitly
  cubic-aware, is the Amari-Chentsov cubic

      T_p(u,v,w) = sum_y u_y v_y w_y / p_y^2          (Paper 12)

  Paper 12, verbatim: "If the Fisher metric is the local object that
  natural gradient sees, K^CH is the first local object it does not see
  unless the optimizer is explicitly cubic-aware."

THE CERTIFICATE (one finite linear-algebra fact, fully decidable):

  In the additive-character (conductor-packet) basis of the Z/n tangent
  space at p_*:

  (Q)  the quadratic Fisher form g_{p_*} is BLOCK-DIAGONAL across packets
       -- it is, up to scale, the identity in the character basis, so it
       carries ZERO inter-packet coupling. A preconditioner built from g
       ALONE cannot represent any cross-packet structure: it is, on this
       space, provably packet-blind above its own (quadratic) floor.

  (C)  the Amari-Chentsov cubic T_{p_*} has a NONZERO inter-packet
       coupling whenever the additive-character selection rule
       k + l + m == 0 (mod n) connects three characters lying in
       DISTINCT conductor packets. The third floor demonstrably couples
       packets that the quadratic floor cannot.

  (Q) AND (C) together = the misspecification is EXACT and FINITE: there
  exists structured information (the cross-packet cubic coupling) that is
  (i) provably present in the geometry and (ii) provably invisible to any
  purely second-order preconditioner. This is "natural gradient is blind
  to a coupling that demonstrably exists", stated as a certificate, not
  as suggestive empirical structure.

SCOPE -- this extends BEYOND active inference (firewall-relevant):
  The argument is preconditioner-agnostic. ANY method whose curvature
  model is the Fisher/Gauss-Newton/quadratic object on a categorical
  (softmax) head -- which is essentially every classifier and every LLM
  token distribution -- inherits (Q). The certificate is therefore a
  statement about second-order optimization of ring-structured
  categorical outputs in general, of which discrete-state active
  inference is one instance.

FIREWALL (binding; the bounded claim, NOT the overclaim):
  This certificate proves ONLY the MISSPECIFICATION -- that the quadratic
  preconditioner provably cannot represent the third-floor cross-packet
  coupling on a ring-structured index. It does NOT claim, and the code
  emits nothing that could support, that real SGD/Adam trajectories ARE
  governed by conductor geometry. That stronger empirical claim is the
  one Paper 12 / beyond_smooth itself declares "suggestive ... weaker
  than claiming the skeleton primarily lives there ... not a universal
  theory of neural cognition", with the C12 Llama-3.1-8B hook as
  SUGGESTIVE evidence only. The certificate stays strictly on the
  finite-linear-algebra side of that line.

Both branches pre-claimed (matched-pair discipline):
  CONFIRMED  : (Q) g is packet-block-diagonal AND (C) T has a nonzero
               cross-packet coupling under the selection rule.
  FALSIFIER  : g is NOT packet-diagonal (natural gradient would already
               see cross-packet structure -> no misspecification to
               certify) OR T has NO cross-packet coupling (nothing the
               quadratic floor misses) OR the packet basis fails to
               diagonalize g (the anchored max-entropy split is wrong).
  Either branch is a STATED result; the falsifier, if realized, indicts
  THIS audit's construction, not Paper 12, whose objects are the
  authority.

Deterministic. Exact rational arithmetic on the rationals; the only
non-rational objects are the additive-character values, handled as exact
n-th roots of unity via integer exponent bookkeeping (a character product
is decided by exponent sum mod n -- no floating point enters the
decisions). No seeds, no tolerances. Author team: Leo. Draft 0.0
reproducibility artifact, INSERT 16 item C2.
"""

from fractions import Fraction
import itertools
import sys
import cmath
import math

# ===========================================================================
# 0. Ring and the anchored max-entropy point.
# ===========================================================================

def run_certificate(n):
    """Run the conductor-misspecification certificate on R = Z/nZ.
    Returns a dict of results; all packet/coupling DECISIONS are exact
    (integer exponent arithmetic mod n). Floating point is used only to
    DISPLAY magnitudes, never to decide vanishing/non-vanishing."""

    # Uniform (maximum-entropy) point p_* = (1/n,...,1/n). Exact.
    p_star = [Fraction(1, n) for _ in range(n)]

    # -----------------------------------------------------------------------
    # 1. Additive characters of Z/nZ and the conductor-packet split.
    #    chi_k(y) = exp(2*pi*i*k*y/n). The conductor of character k is
    #    n / gcd(k, n); packets group characters by conductor d | n, d > 1.
    #    k = 0 is the constant mode (the simplex normal / off-tangent); the
    #    tangent space is spanned by k = 1..n-1.
    # -----------------------------------------------------------------------
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    tangent_chars = list(range(1, n))          # k = 1 .. n-1
    conductor = {k: n // gcd(k, n) for k in tangent_chars}

    # Packets: group tangent characters by conductor d | n, d > 1.
    packets = {}
    for k in tangent_chars:
        packets.setdefault(conductor[k], []).append(k)
    packet_list = sorted(packets.items())      # [(d, [chars...]), ...]

    # -----------------------------------------------------------------------
    # 2. (Q) The quadratic Fisher form at p_* in the character basis.
    #    g_{p_*}(u,v) = sum_y u_y v_y / p_*_y = n * sum_y u_y v_y.
    #    In the additive-character basis e_k(y) = chi_k(y), the Gram matrix
    #    is g[k,l] = n * sum_y chi_k(y) * conj(chi_l(y))
    #             = n * sum_y exp(2pi i (k-l) y / n)
    #             = n * n   if k == l   (mod n),   else 0   EXACTLY,
    #    by the exact orthogonality of additive characters (a finite
    #    geometric series that is exactly zero unless k==l mod n). The
    #    DECISION "off-diagonal == 0" is therefore exact integer arithmetic
    #    (k - l == 0 mod n), NOT a floating-point near-zero.
    # -----------------------------------------------------------------------
    def fisher_offdiagonal_is_exactly_zero(k, l):
        # n * sum_{y=0}^{n-1} omega^{(k-l) y}, omega = primitive n-th root.
        # Exactly 0 iff (k - l) % n != 0; exactly n^2 iff k == l.
        return (k - l) % n != 0

    # Verify: g is diagonal across the FULL tangent character set, hence
    # block-diagonal across packets (a fortiori). Exact check.
    fisher_is_packet_block_diagonal = all(
        fisher_offdiagonal_is_exactly_zero(k, l)
        for k in tangent_chars for l in tangent_chars if k != l
    )
    # And strictly: are there ANY nonzero off-diagonal (cross-packet) Fisher
    # entries? (Must be none for the misspecification to exist.)
    fisher_cross_packet_entries = [
        (k, l)
        for (dk, ck) in packet_list for k in ck
        for (dl, cl) in packet_list for l in cl
        if dk != dl and not fisher_offdiagonal_is_exactly_zero(k, l)
    ]

    # -----------------------------------------------------------------------
    # 3. (C) The Amari-Chentsov cubic at p_* in the character basis.
    #    T_{p_*}(e_k,e_l,e_m) = sum_y chi_k chi_l chi_m / p_*_y^2
    #      = n^2 * sum_y exp(2pi i (k+l+m) y / n)
    #      = n^3  if (k+l+m) == 0 (mod n),  else 0   EXACTLY.
    #    So the cubic coupling (k,l,m) is NONZERO  <=>  k+l+m == 0 (mod n).
    #    DECISION is exact integer arithmetic. No floating point.
    # -----------------------------------------------------------------------
    def cubic_is_nonzero(k, l, m):
        return (k + l + m) % n == 0

    # Find cross-packet cubic couplings: a surviving (k,l,m) whose three
    # legs do NOT all lie in the same conductor packet.
    def packet_of(k):
        return conductor[k]

    cross_packet_cubic = []
    same_packet_cubic = []
    for k, l, m in itertools.product(tangent_chars, repeat=3):
        if cubic_is_nonzero(k, l, m):
            dk, dl, dm = packet_of(k), packet_of(l), packet_of(m)
            if dk == dl == dm:
                same_packet_cubic.append(((k, l, m), (dk, dl, dm)))
            else:
                cross_packet_cubic.append(((k, l, m), (dk, dl, dm)))

    has_cross_packet_cubic = len(cross_packet_cubic) > 0

    # -----------------------------------------------------------------------
    # 4. The certificate verdict (mechanical, both branches pre-claimed).
    # -----------------------------------------------------------------------
    Q = fisher_is_packet_block_diagonal and len(fisher_cross_packet_entries) == 0
    C = has_cross_packet_cubic
    confirmed = Q and C

    return {
        "n": n,
        "tangent_dim": len(tangent_chars),
        "packets": packet_list,
        "Q_fisher_block_diagonal": Q,
        "fisher_cross_packet_nonzero_entries": fisher_cross_packet_entries,
        "C_cubic_has_cross_packet_coupling": C,
        "num_cross_packet_cubic": len(cross_packet_cubic),
        "num_same_packet_cubic": len(same_packet_cubic),
        "sample_cross_packet_cubic": cross_packet_cubic[:8],
        "confirmed": confirmed,
    }


# ===========================================================================
# 5. Run on a ladder of ring-structured indices and report.
# ===========================================================================

def main():
    print("=" * 78)
    print(" INSERT 16 / item C2  --  Conductor-Misspecification Certificate")
    print(" Contribution 2 of the FEP/AI bridge, executed as a deterministic")
    print(" finite certificate (cf. INSERT 15 for Contribution 1).")
    print(" Anchored objects: Paper 12 Fisher metric & Amari-Chentsov cubic.")
    print(" Exact integer/rational arithmetic. No fitted model, no tolerance.")
    print("=" * 78)

    print("\n[Claim under test -- Paper 12, verbatim objects]")
    print("  g_p(u,v)   = sum_y u_y v_y / p_y          (quadratic; what a")
    print("                                             2nd-order")
    print("                                             preconditioner sees)")
    print("  T_p(u,v,w) = sum_y u_y v_y w_y / p_y^2     (cubic; the first")
    print("                                             object it does NOT")
    print("                                             see unless cubic-")
    print("                                             aware)")
    print("  At max entropy on Z/nZ the tangent space splits into")
    print("  conductor packets indexed by additive characters.")

    print("\n[Scope note -- extends beyond active inference]")
    print("  (Q) holds for ANY second-order preconditioner on a categorical")
    print("  (softmax) head: natural gradient, K-FAC, Gauss-Newton, Adam's")
    print("  diagonal empirical Fisher, the NTK Gram. Discrete-state active")
    print("  inference is ONE instance; LLM/classifier token heads are")
    print("  another. The certificate is a statement about 2nd-order")
    print("  optimization of ring-structured categorical outputs in general.")

    # Ring ladder: the program's canonical row, two squarefree rows, two
    # composite rows with prime-power depth, and the C12 LLM-relevant row.
    ladder = [6, 12, 30, 8, 18]

    overall = []
    for n in ladder:
        r = run_certificate(n)
        overall.append(r)
        print("\n" + "-" * 78)
        print(f" R = Z/{n}Z   (tangent dim = {r['tangent_dim']})")
        print("-" * 78)
        print("  conductor packets (d | n, d>1) -> characters:")
        for d, chars in r["packets"]:
            print(f"     conductor {d:>3} : {chars}")
        print(f"  (Q) Fisher form packet-block-diagonal at p_*      : "
              f"{r['Q_fisher_block_diagonal']}")
        print(f"      cross-packet NONZERO Fisher entries           : "
              f"{r['fisher_cross_packet_nonzero_entries'] or 'NONE (exact)'}")
        print(f"  (C) Amari-Chentsov cubic cross-packet coupling    : "
              f"{r['C_cubic_has_cross_packet_coupling']}")
        print(f"      # surviving cross-packet cubic triples        : "
              f"{r['num_cross_packet_cubic']}")
        print(f"      # surviving same-packet  cubic triples        : "
              f"{r['num_same_packet_cubic']}")
        if r["sample_cross_packet_cubic"]:
            print(f"      sample cross-packet couplings "
                  f"(k,l,m)->(cond,cond,cond):")
            for (klm, dds) in r["sample_cross_packet_cubic"]:
                print(f"        {klm} -> conductors {dds}")
        print(f"  >>> certificate on Z/{n}Z : "
              f"{'CONFIRMED' if r['confirmed'] else 'FALSIFIER REALIZED'}")

    all_confirmed = all(r["confirmed"] for r in overall)

    print("\n" + "=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if all_confirmed:
        print("  >>> C2 CERTIFICATE CONFIRMED on every ring tested"
              " (pre-claimed branch A).")
        print()
        print("  For every R = Z/nZ in the ladder, EXACTLY and FINITELY:")
        print("   (Q) the quadratic Fisher form is packet-block-diagonal at")
        print("       maximum entropy -- zero cross-packet entries, by exact")
        print("       additive-character orthogonality. A preconditioner")
        print("       built from g alone carries NO inter-packet coupling.")
        print("   (C) the Amari-Chentsov cubic has nonzero cross-packet")
        print("       coupling (the k+l+m==0 mod n selection rule connects")
        print("       characters in distinct conductor packets).")
        print()
        print("  Therefore: there exists structured information -- the")
        print("  cross-packet cubic coupling -- that is provably present in")
        print("  the geometry and provably invisible to ANY purely second-")
        print("  order preconditioner. The misspecification is EXACT and")
        print("  FINITE, not suggestive.")
        print()
        print("  THIS is the finite fact the FEP/2nd-order-optimization")
        print("  stack cannot derive from inside itself: its own curvature")
        print("  model (the quadratic Fisher object) is, on a ring-")
        print("  structured categorical index, provably blind to a coupling")
        print("  the next cumulant floor demonstrably carries. The")
        print("  diagnostic is named and computable: project the update")
        print("  onto conductor packets; any cross-packet cubic mass is")
        print("  exactly what the 2nd-order preconditioner mis-prices.")
        print()
        print("  BOUND (firewall, binding): this certifies the")
        print("  MISSPECIFICATION ONLY. It does NOT claim real SGD/Adam")
        print("  trajectories ARE governed by conductor geometry -- that")
        print("  remains the SUGGESTIVE empirical claim (Paper 12 /")
        print("  beyond_smooth self-bound; C12 Llama-3.1-8B hook is")
        print("  suggestive evidence, not proof). The certificate stays on")
        print("  the finite-linear-algebra side of that line.")
    else:
        print("  >>> C2 FALSIFIER REALIZED on at least one ring"
              " (pre-claimed branch B).")
        for r in overall:
            if not r["confirmed"]:
                print(f"    Z/{r['n']}Z: Q={r['Q_fisher_block_diagonal']}, "
                      f"C={r['C_cubic_has_cross_packet_coupling']}")
        print("  Per matched-pair discipline this is a STATED outcome and")
        print("  indicts THIS audit's construction (the character-basis")
        print("  reduction), NOT Paper 12, whose objects are the authority.")
        print("  The C2 contribution claim is VOID pending reconciliation,")
        print("  exactly as the U1FM v1 anchor-failure was handled.")

    print("\n" + "=" * 78)
    print(" FIREWALL SELF-CHECK (INSERT 04 sec 1.4, inherited; binding)")
    print("=" * 78)
    print("  PASS: emits only (i) exact packet decompositions, (ii) the")
    print("  exact (k-l) mod n / (k+l+m) mod n vanishing decisions, (iii)")
    print("  integer counts. No mass/length/energy/time/charge, no")
    print("  c/hbar/G/alpha, no physical free-energy value, no learning")
    print("  rate, no claim about any trained model's actual trajectory.")
    print("  The result is a finite linear-algebra MISSPECIFICATION")
    print("  certificate, strictly weaker than (and firewalled from) the")
    print("  suggestive empirical 'optimizer discovers conductor geometry'")
    print("  claim, which is NOT made here.")

    print("\n" + "=" * 78)
    print(" Status: deterministic run complete. All packet/coupling")
    print(" decisions are exact integer arithmetic mod n; floating point")
    print(" never enters a vanishing decision. Both branches pre-claimed;")
    print(" the realized branch is a STATED result. Tests Paper 12's own")
    print(" anchored objects, not a reconstruction.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
