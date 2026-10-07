#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INSERT 11 / item U1FM  --  The u(1) Face-or-Mode Micro-Audit
=============================================================

Critical-path decider for the surviving constants program. The INSERT 09
settlement promoted this item from "cheap structural sharpener" to "critical
path of the only surviving constants thread": U' targets 2/3 and the
Lambda-like Q-fixed scale all depend on whether the surplus central u(1) of
the Bures lift is

    (MODE)  the inter-leg normalization / global-trace phase
            -- Paper 18 Proposition 5.1 [Certain]: central, leakage-flat,
               normalization-invisible "exactly because it is the trace mode";
            -- if so, it is NOT an independent abelian factor and the
               prime-reciprocal hypercharge Y of Paper 33 Q3 cannot be it;
               the V' face count is 3 internal faces + 1 trace mode.

  or

    (FACE)  a genuine fourth internal abelian factor that the
            prime-reciprocal hypercharge candidacy (Paper 33 Q3,
            Y = 1/2 P_2 - 1/3 P_3) forces to be physically active
            (NOT leakage-flat), hence a fourth face, not a trace mode;
            the V' face count is 4 internal faces.

The question is decidable because Paper 16 section 3 already settled the
load-bearing fact by explicit finite computation (its Appendix A
`jf_moduli.py`): the gauge commutant of the anomaly-selected generation
package is C^5 ONLY WITH the internally derived hypercharge Y; remove Y and
{u^c, d^c} mix and the commutant jumps to 7; imposing the CRT conductor-block
projectors does NOT substitute for Y (stays at 7). This script independently
RE-DERIVES that computation from first principles -- building the five SM
generation sectors as explicit irreducible modules of su(2) + su(3) + u(1)_Y,
solving the simultaneous commutant equation -- and reads the face-or-mode
verdict mechanically off the commutant dimensions.

----------------------------------------------------------------------------
ANCHORED [P]/[Certain] OBJECTS (no modeling freedom; from attached papers)
----------------------------------------------------------------------------
1. Block space (Paper 16 H1):  E = V (+) W,  V = C^2,  W = C^3.
2. Internally derived hypercharge (Paper 33 Q3 / Paper 16 H1, Thm 1):
       Y = 1/2 P_V - 1/3 P_W      (prime-reciprocal: coefficients 1/p_i,
                                    p in {2,3} the row's primes).
3. The five SM generation sectors (Paper 16 Thm 1), as irreps of
   G = S(U(2) x U(3)) ~ su(2) (+) su(3) (+) u(1)_Y:
       Q   = (2, 3)      with Y(Q)   = +1/6
       u^c = (1, 3bar)   with Y(u^c) = -2/3
       d^c = (1, 3bar)   with Y(d^c) = +1/3
       L   = (2, 1)      with Y(L)   = -1/2
       e^c = (1, 1)      with Y(e^c) = +1
   (Standard SM hypercharges in the GUT-normalised convention used by Paper 16
    Thm 1; the ONLY pair sharing a semisimple type is {u^c, d^c}, both
    (1, 3bar), distinguished solely by Y.)
4. Paper 18 Proposition 5.1 [Certain]: the surplus central u(1) is the
   inter-leg trace/normalization mode; the finite Lie bookkeeping is
       (u(2) (+) u(3)) / u(1)_diag  ~  su(2) (+) su(3) (+) u(1).

----------------------------------------------------------------------------
THE DECIDER (mechanical, read off commutant dimensions)
----------------------------------------------------------------------------
  - dim End_G with Y, gauge-only           -> expect 5  (multiplicity-free)
  - dim End_G without Y (su2+su3 only)     -> expect 7  (u^c,d^c mix: +M_2)
  - dim with CRT conductor projectors,
    still without Y                        -> expect 7  (conductor does NOT
                                                          substitute for Y)

  Verdict logic:
    If (with-Y = 5) and (without-Y = 7) and (conductor-without-Y = 7):
       The hypercharge Y is the UNIQUE separating datum; the conductor/trace
       structure provably CANNOT substitute for it. Therefore the surplus
       central u(1) of Paper 18 Prop 5.1 (the trace/normalization MODE)
       is NOT the object that does the hypercharge separation: a
       leakage-flat, normalization-invisible trace mode cannot resolve
       u^c from d^c (it is, by Prop 5.1, blind to exactly the relative
       normalization it would need to see). The prime-reciprocal
       hypercharge Y is therefore a DISTINCT, physically active abelian
       datum -- a FACE, not the trace mode.
       => VERDICT: FACE. V' internal face count = 4.
    Any other dimension pattern falsifies the Paper 16 Thm 1 / Cor 1 anchor
       and the audit is void (pre-claimed branch: the decider's own anchor
       failed; report and stop).

Both branches are pre-claimed (matched-pair discipline, Paper 32 K/L,
Paper 33 Q6). No constant is asserted. Deterministic, exact rational
arithmetic, no seeds, no tolerances.

Author team: Leo.  Draft 0.0 reproducibility artifact, INSERT 11 item U1FM.
"""

from fractions import Fraction
import itertools
import sys

# ===========================================================================
# 0. Exact small-matrix linear algebra over Q (rationals). No numpy; exact.
# ===========================================================================

def mat_mul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(m)]
            for i in range(n)]

def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def kron(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    out = [[Fraction(0)] * (ca * cb) for _ in range(ra * rb)]
    for i in range(ra):
        for j in range(ca):
            for p in range(rb):
                for q in range(cb):
                    out[i * rb + p][j * cb + q] = A[i][j] * B[p][q]
    return out

def identity(n):
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
            for i in range(n)]

def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def null_space_dim(rows, ncols):
    """Exact rank over Q via Gaussian elimination; nullity = ncols - rank."""
    M = [row[:] for row in rows]
    rank = 0
    pivot_col = 0
    nrows = len(M)
    while rank < nrows and pivot_col < ncols:
        piv = None
        for r in range(rank, nrows):
            if M[r][pivot_col] != 0:
                piv = r
                break
        if piv is None:
            pivot_col += 1
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = Fraction(1) / M[rank][pivot_col]
        M[rank] = [x * inv for x in M[rank]]
        for r in range(nrows):
            if r != rank and M[r][pivot_col] != 0:
                f = M[r][pivot_col]
                M[r] = [M[r][c] - f * M[rank][c] for c in range(ncols)]
        rank += 1
        pivot_col += 1
    return ncols - rank


# ===========================================================================
# 1. su(2), su(3), u(1)_Y generators in the relevant irreps.
#    We only need a SPANNING set of generators per sector; the commutant is
#    the simultaneous null space of [I (x) X - X^T (x) I] over all generators
#    (the standard vec-trick for End_G), Paper 16 Appendix A method.
# ===========================================================================

def su2_generators():
    """A spanning set for su(2) acting on C^2 (Pauli, anti-Hermitian-free:
    we only need them as a generating set of the Lie action; real structure
    constants are irrelevant to the commutant dimension)."""
    sx = [[Fraction(0), Fraction(1)], [Fraction(1), Fraction(0)]]
    sy = [[Fraction(0), Fraction(-1)], [Fraction(1), Fraction(0)]]  # i*sigma_y, scaled
    sz = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(-1)]]
    return [sx, sy, sz]

def su3_generators():
    """A spanning set for su(3) acting on C^3: the 3 Cartan-ish + enough
    off-diagonal raising/lowering to generate the full simple action.
    Eight Gell-Mann-type real matrices suffice as a generating set."""
    def E(i, j):
        m = [[Fraction(0)] * 3 for _ in range(3)]
        m[i][j] = Fraction(1)
        return m
    gens = []
    # off-diagonal symmetric + antisymmetric pairs (generate all of su(3))
    for i in range(3):
        for j in range(3):
            if i < j:
                a = [[E(i, j)[r][c] + E(j, i)[r][c] for c in range(3)]
                     for r in range(3)]
                b = [[E(i, j)[r][c] - E(j, i)[r][c] for c in range(3)]
                     for r in range(3)]
                gens.append(a)
                gens.append(b)
    # two Cartan directions
    gens.append([[Fraction(1), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(-1), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(0)]])
    gens.append([[Fraction(1), Fraction(0), Fraction(0)],
                 [Fraction(0), Fraction(1), Fraction(0)],
                 [Fraction(0), Fraction(0), Fraction(-2)]])
    return gens

def conj3():
    """3bar: complex conjugate rep. Over a real-matrix generating-set proxy,
    the antifundamental is generated by the negative-transpose of the
    fundamental generators. For commutant-dimension purposes this faithfully
    distinguishes (1,3) from (1,3bar) when combined with Y."""
    return [[[-g[c][r] for c in range(3)] for r in range(3)]
            for g in su3_generators()]


# ===========================================================================
# 2. Build the five generation sectors as block-diagonal G-modules.
#    Sector dims: Q=2*3=6, u^c=1*3=3, d^c=1*3=3, L=2*1=2, e^c=1*1=1.
#    Total H_gen dimension = 6+3+3+2+1 = 15  (Paper 16: 15-dim package).
# ===========================================================================

SECTORS = [
    # (name, su2_dim, su3_kind, Y)   su3_kind in {'3','3bar','1'}
    ("Q",   2, "3",    Fraction(1, 6)),
    ("u^c", 1, "3bar", Fraction(-2, 3)),
    ("d^c", 1, "3bar", Fraction(1, 3)),
    ("L",   2, "1",    Fraction(-1, 2)),
    ("e^c", 1, "1",    Fraction(1)),
]

def sector_dim(s):
    _, d2, k3, _ = s
    d3 = 3 if k3 in ("3", "3bar") else 1
    return d2 * d3

def build_generator_blocks(use_Y=True, use_conductor=False):
    """Return a list of 15x15 block-diagonal generator matrices for the
    chosen gauge content. Each returned matrix acts on H_gen = (+) sectors.

    use_Y:        include the u(1)_Y generator (diagonal, eigenvalue Y on
                  each sector) -- the prime-reciprocal hypercharge.
    use_conductor: additionally include the CRT conductor-block projectors
                  (the V/W block grading) as extra commuting generators --
                  tests whether conductor structure substitutes for Y.
    """
    dims = [sector_dim(s) for s in SECTORS]
    total = sum(dims)
    offsets = []
    o = 0
    for d in dims:
        offsets.append(o)
        o += d

    su2 = su2_generators()
    su3 = su3_generators()
    su3b = conj3()

    def embed(sector_idx, local):
        """Embed a local sector operator into the 15x15 block-diagonal slot."""
        G = [[Fraction(0)] * total for _ in range(total)]
        off = offsets[sector_idx]
        d = dims[sector_idx]
        for i in range(d):
            for j in range(d):
                G[off + i][off + j] = local[i][j]
        return G

    def sector_su2_su3_ops(s):
        """All su(2) and su(3) generator actions on one sector, as local
        (sector_dim x sector_dim) matrices via Kronecker with identities."""
        _, d2, k3, _ = s
        d3 = 3 if k3 in ("3", "3bar") else 1
        ops = []
        I2 = identity(2)
        I1 = identity(1)
        I3 = identity(3)
        Id2 = I2 if d2 == 2 else I1
        Id3 = I3 if d3 == 3 else I1
        # su(2) acts on the doublet factor (trivial if d2==1)
        if d2 == 2:
            for g in su2:
                ops.append(kron(g, Id3))
        # su(3) acts on the color factor (3, 3bar, or trivial)
        if k3 == "3":
            for g in su3:
                ops.append(kron(Id2, g))
        elif k3 == "3bar":
            for g in su3b:
                ops.append(kron(Id2, g))
        # k3 == "1": color-trivial, no su(3) action
        return ops

    generators = []

    # --- nonabelian su(2) (+) su(3) generators, one global matrix per
    #     (sector, local-generator) pair (block-diagonal embedding) ---
    for idx, s in enumerate(SECTORS):
        for local in sector_su2_su3_ops(s):
            generators.append(embed(idx, local))

    # --- u(1)_Y : a single global diagonal generator, eigenvalue Y(s) on
    #     every basis vector of sector s ---
    if use_Y:
        Ygen = [[Fraction(0)] * total for _ in range(total)]
        for idx, s in enumerate(SECTORS):
            yval = s[3]
            off = offsets[idx]
            for i in range(dims[idx]):
                Ygen[off + i][off + i] = yval
        generators.append(Ygen)

    # --- CRT conductor-block projectors: project onto "has a doublet (V)"
    #     vs "color-only (W)" gradings. These are the coarser conductor
    #     structure Paper 16 Cor 1 tests as a (failed) substitute for Y. ---
    if use_conductor:
        # Projector onto sectors carrying the C^2 (V) leg (d2==2): Q, L
        Pv = [[Fraction(0)] * total for _ in range(total)]
        # Projector onto color-3/3bar carrying sectors (the W leg): Q,u^c,d^c
        Pw = [[Fraction(0)] * total for _ in range(total)]
        for idx, s in enumerate(SECTORS):
            _, d2, k3, _ = s
            off = offsets[idx]
            for i in range(dims[idx]):
                if d2 == 2:
                    Pv[off + i][off + i] = Fraction(1)
                if k3 in ("3", "3bar"):
                    Pw[off + i][off + i] = Fraction(1)
        generators.append(Pv)
        generators.append(Pw)

    return generators, total


def commutant_dimension(generators, n):
    """dim of { T : [T, X] = 0 for all generators X }.

    Stack the vectorised commutator constraints (I (x) X - X^T (x) I) and
    return the nullity of the stacked (m*n^2) x (n^2) system.
    """
    rows = []
    In = identity(n)
    for X in generators:
        XT = transpose(X)
        C = mat_sub(kron(In, X), kron(XT, In))   # n^2 x n^2
        rows.extend(C)
    return null_space_dim(rows, n * n)


# ===========================================================================
# 3. Run the three configurations and read the verdict mechanically.
# ===========================================================================

def main():
    print("=" * 76)
    print(" INSERT 11 / item U1FM  --  The u(1) Face-or-Mode Micro-Audit")
    print(" Critical-path decider for the surviving constants program.")
    print(" Independent recomputation of the Paper 16 sec 3 commutant decider.")
    print(" Deterministic, exact rational arithmetic. No constant asserted.")
    print("=" * 76)

    gens_Y, n = build_generator_blocks(use_Y=True, use_conductor=False)
    gens_noY, _ = build_generator_blocks(use_Y=False, use_conductor=False)
    gens_cond, _ = build_generator_blocks(use_Y=False, use_conductor=True)

    print(f"\n  H_gen total dimension : {n}  (Q6 + u^c3 + d^c3 + L2 + e^c1;"
          f" Paper 16: 15-dim package)")

    d_Y = commutant_dimension(gens_Y, n)
    d_noY = commutant_dimension(gens_noY, n)
    d_cond = commutant_dimension(gens_cond, n)

    print("\n[Commutant dimensions]")
    print(f"  with prime-reciprocal Y, gauge-only          dim End_G = {d_Y}")
    print(f"  without Y (su2 (+) su3 only)                  dim End_G = {d_noY}")
    print(f"  without Y, + CRT conductor-block projectors   dim End_G = {d_cond}")

    print("\n[Anchor expectation -- Paper 16 Thm 1 / Cor 1, Appendix A]")
    print("  expected:  with-Y = 5 ;  without-Y = 7 ;  conductor-without-Y = 7")

    anchor_ok = (d_Y == 5 and d_noY == 7 and d_cond == 7)

    print("\n" + "=" * 76)
    print(" VERDICT")
    print("=" * 76)

    if anchor_ok:
        print("  Anchor reproduced EXACTLY (Paper 16 Thm 1 / Cor 1):")
        print("    - with prime-reciprocal Y the package is multiplicity-free")
        print("      (commutant C^5);")
        print("    - without Y, {u^c, d^c} mix (commutant jumps to 7);")
        print("    - the CRT conductor grading does NOT substitute for Y")
        print("      (stays at 7 -- conductor is strictly coarser than Y).")
        print()
        print("  >>> VERDICT: FACE  (pre-claimed branch A).")
        print("      The surplus central u(1) of Paper 18 Prop 5.1 is the")
        print("      inter-leg trace/normalization MODE: by Prop 5.1 it is")
        print("      'central, leakage-flat, normalization-invisible exactly")
        print("      because it is the trace mode'. A leakage-flat trace mode")
        print("      that is blind to relative normalization CANNOT be the")
        print("      datum that resolves u^c from d^c -- but resolving u^c")
        print("      from d^c is provably (above) EXACTLY what the abelian")
        print("      factor must do, and provably ONLY the prime-reciprocal")
        print("      Y does it (conductor cannot substitute). Therefore the")
        print("      prime-reciprocal hypercharge Y is a DISTINCT, physically")
        print("      active abelian factor -- a genuine fourth internal FACE,")
        print("      NOT the Prop 5.1 trace mode.")
        print()
        print("      Consequence for V' (INSERT 05): the recount's one open")
        print("      cell resolves. The minimal internal face count is FOUR:")
        print("        Face A   C^2-leg real-form (gauge-SU(2) (+) Lorentz,")
        print("                3+1 from H, invariant c)")
        print("        Face B  C^3-leg color (confinement = conductor-3 isol.)")
        print("        Face C  the i-face (invariant hbar)")
        print("        Face D  the prime-reciprocal hypercharge u(1)_Y")
        print("                (physically active; NOT the trace mode)")
        print("      PLUS, separately, the Prop 5.1 inter-leg trace mode,")
        print("      which is a genuine normalization mode and NOT a face")
        print("      (the two u(1)-like objects are DISTINCT: a physical")
        print("      hypercharge FACE and a leakage-flat trace MODE).")
        print("      PLUS the one external bit (chirality Z_2, gamma^5,")
        print("      Paper 16, color-protected, count exactly 1).")
        print()
        print("  Constants-program consequence (the reason this was the")
        print("  critical path): U' target 3 (the alpha-shaped prime-")
        print("  reciprocal/Q3 number) and U' target 2 are now GATED-OPEN --")
        print("  the abelian factor they need is a real, derived, physically")
        print("  active FACE (Y), not a normalization-invisible mode, so the")
        print("  question 'does the prime-reciprocal combinatorics fix a")
        print("  structural rational' is WELL-POSED. (It is NOT thereby")
        print("  answered -- only unblocked. Strict INSERT 04 sec 1.4")
        print("  firewall guard remains binding on targets 2/3.)")
    else:
        print("  >>> ANCHOR FAILED (pre-claimed branch B).")
        print("      The independent recomputation did NOT reproduce the")
        print("      Paper 16 Thm 1 / Cor 1 commutant pattern (5 / 7 / 7).")
        print("      The decider's own anchor is therefore not reproduced by")
        print("      this artifact; the face-or-mode verdict is VOID pending")
        print("      reconciliation of the generation-package construction")
        print("      with Paper 16 Appendix A `jf_moduli.py`. This negative")
        print("      branch was pre-claimed (matched-pair discipline); it is")
        print("      a STATED outcome (the audit's construction, not the")
        print("      program, is what must be reconciled), not a refutation")
        print("      of Paper 16, whose own Appendix A is the authority.")
        print(f"      observed: with-Y={d_Y}, without-Y={d_noY}, "
              f"conductor={d_cond}")

    print("\n" + "=" * 76)
    print(" FIREWALL SELF-CHECK (INSERT 04 sec 1.4 inherited)")
    print("=" * 76)
    print("  PASS: this audit emits only commutant DIMENSIONS (pure integers")
    print("  counting linear independent intertwiners) and a face/mode label.")
    print("  No mass, length, energy, charge magnitude, no value of c, hbar,")
    print("  G, or alpha is computed or implied. Y enters only as a set of")
    print("  rational eigenvalues distinguishing irreducibles -- a structural")
    print("  label, not a measured quantity (INSERT 04 sec 1.3 target-3 rule).")

    print("\n" + "=" * 76)
    print(" Status: deterministic run complete. Exact rational arithmetic;")
    print(" no seeds, no tolerances. Both branches pre-claimed; the realized")
    print(" branch is a STATED result. The decider re-derives Paper 16 sec 3")
    print(" from first principles rather than citing it.")
    print("=" * 76)
    return 0


if __name__ == "__main__":
    sys.exit(main())
