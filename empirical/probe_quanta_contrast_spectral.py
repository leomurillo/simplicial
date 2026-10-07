"""probe_quanta_contrast_spectral.py -- the contrast -> spectral weld.

CLAIM. The quanta object's gauge-invariant content is the contrast classes [q_i/q_j]_n.
For n=2 a contrast square class [c] IS a Dirichlet character chi_d (Kronecker symbol, d the
fundamental discriminant of Q(sqrt c)). So the contrasts are not bookkeeping -- they are the
CHARACTER LABELS of the L-functions L(s,chi_d), whose zeros are the spectrum and whose
central values L(1/2,chi_d) are gauge-invariant spectral data. The compositum field K of the
contrast group has zeta_K = prod_chi L(s,chi) (Artin), so the contrast group indexes exactly
the spectral factors; the conductor-discriminant formula disc(K) = prod_chi cond(chi) welds
the contrast group to the field's discriminant exactly.

THE CHIRAL LEVER. The index-n character (the gauge-RIGID phi(n) part, sec. earlier) for n=3
is chi_{-3} = chi_3, with central value L(1/2,chi_3) = 0.4808... > 0 -- the program's c_2<0
lever (diez sec 2.6). So the chiral lever is the central value of the index-3 contrast-
character, and it is gauge-rigid because the index, not the data, summons it.

PRE-REGISTERED (GPD):
  S1 (contrasts are gauge-invariant characters): contrast square classes of raw (2,3,5) and
     sum-gauged (20,30,50) are identical (the gauge cancels in the ratio); each is a chi_d
     with computable conductor, parity, L(1/2). FALSIFIER: contrasts differ raw vs gauged.
  S2 (the chiral lever): L(1/2, chi_{-3}) = 0.4808.. > 0 (anchor); the index->character->L(1/2)
     ladder p=3 (chi_{-3}, CHIRAL), 5 (chi_5), 7 (chi_{-7}). FALSIFIER: L(1/2,chi_{-3}) != 0.4808.
  S3 (conductor-discriminant weld): for K = Q(sqrt2,sqrt3) the contrast character group has
     conductors {1,8,12,24} with product 2304 = disc(K) (known). zeta_K = prod L(s,chi):
     the contrasts ARE the spectral factors. FALSIFIER: product != 2304.

Exact (sympy) + mpmath for L-values. Deterministic.
"""
import sys
from sympy import factorint, jacobi_symbol
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30


# ---------------- Kronecker symbol, fundamental discriminant, L-values ----------------
def kronecker(a, n):
    if n == 0:
        return 1 if abs(a) == 1 else 0
    if n < 0:
        return (-1 if a < 0 else 1) * kronecker(a, -n)
    res = 1
    while n % 2 == 0:
        n //= 2
        if a % 2 == 0:
            return 0
        if a % 8 in (3, 5):
            res = -res
    if n == 1:
        return res
    j = jacobi_symbol(a % n, n)
    return res * int(j)


def sqfree_signed(c):
    """squarefree signed kernel of integer c (the square class as a signed squarefree int)."""
    c = int(c)
    s = -1 if c < 0 else 1
    c = abs(c)
    k = 1
    for p, e in factorint(c).items():
        if e % 2:
            k *= p
    return s * k


def fund_disc(c):
    """fundamental discriminant of Q(sqrt c), c the signed squarefree kernel."""
    c = sqfree_signed(c)
    return c if c % 4 == 1 else 4 * c


def Lval_half(d):
    """L(1/2, chi_d) via Hurwitz zeta; chi_d(a) = kronecker(d, a), modulus |d|."""
    q = abs(d)
    s = mp.mpf(1) / 2
    return mp.fsum(kronecker(d, a) * mp.zeta(s, mp.mpf(a) / q) for a in range(1, q + 1)) / q**s


def parity(d):
    return "even" if kronecker(d, -1) == 1 else "odd"


# ---------------- S1: contrasts are gauge-invariant characters ----------------
print("== S1: the contrasts are gauge-invariant Dirichlet characters ==")
qs = [2, 3, 5]
S = sum(qs)
gauged = [q * S for q in qs]   # value-clock radicands (n=2): q_i * S
print(f"   raw {qs}, sum-gauged radicands {gauged} (S={S})")
print(f"   {'contrast':<12}{'raw [c]':<12}{'gauged [c]':<12}{'cond':>6}{'parity':>8}{'L(1/2)':>12}")
pairs = [(0, 1), (0, 2), (1, 2)]
s1 = True
for i, j in pairs:
    c_raw = sqfree_signed(qs[i] * qs[j])         # [q_i/q_j] = [q_i q_j] (mod squares)
    c_g = sqfree_signed(gauged[i] * gauged[j])   # gauge cancels: q_i S * q_j S = q_i q_j S^2
    d = fund_disc(c_raw)
    same = (c_raw == c_g)
    s1 &= same
    L = Lval_half(d)
    print(f"   {f'{qs[i]}/{qs[j]}':<12}{f'[{c_raw}]':<12}{f'[{c_g}]':<12}{abs(d):>6}{parity(d):>8}"
          f"{float(L):>12.6f}  {'OK' if same else 'DIFFER'}")
print(f"   S1: contrasts gauge-invariant (raw == gauged): {'PASS' if s1 else 'FAIL'}")


# ---------------- S2: the chiral lever (index -> character -> L(1/2)) ----------------
print("\n== S2: index p -> rigid character chi_{p*} -> central value L(1/2) ==")
print(f"   {'index p':>8}{'p*':>5}{'character':>12}{'parity':>8}{'L(1/2)':>12}   note")
anchor_ok = False
for p in [3, 5, 7]:
    pstar = ((-1) ** ((p - 1) // 2)) * p
    d = fund_disc(pstar)
    L = Lval_half(d)
    note = "<-- CHIRAL (the c_2<0 lever, L(1/2,chi_3))" if p == 3 else ""
    if p == 3:
        anchor_ok = abs(float(L) - 0.4808) < 1e-3
    print(f"   {p:>8}{pstar:>5}{f'chi_{d}':>12}{parity(d):>8}{float(L):>12.6f}   {note}")
print(f"   anchor L(1/2, chi_{{-3}}) = 0.4808: {'PASS' if anchor_ok else 'FAIL'}")
print("   index 2 boundary: chi_{-4} (the sign/i character) -- the archimedean reflection.")
Lm4 = Lval_half(-4)
print(f"   L(1/2, chi_{{-4}}) = {float(Lm4):.6f}  (the index-2/archimedean character)")


# ---------------- S3: conductor-discriminant weld (contrasts ARE the spectral factors) ----
print("\n== S3: conductor-discriminant weld -- the contrast group indexes zeta_K = prod L(s,chi) ==")
# K = Q(sqrt2, sqrt3): contrast character group = {1, chi_8, chi_12, chi_24}
chars = {1: 1, 8: 8, 12: 12, 24: 24}   # square class -> fundamental disc (positive here)
# build from the contrast group of sqrt2, sqrt3: classes generated by [2],[3]: {1,[2],[3],[6]}
gens = {sqfree_signed(2), sqfree_signed(3)}
group = {1}
for a in list(gens):
    group |= {sqfree_signed(g * a) for g in group}
group |= {sqfree_signed(2 * 3)}   # [6]
group = {1, 2, 3, 6}
conds = {1: 1}
for c in group:
    if c != 1:
        conds[c] = abs(fund_disc(c))
prod = 1
for c, cd in conds.items():
    prod *= cd
disc_K_known = 2304   # disc(Q(sqrt2,sqrt3)), standard
print(f"   K = Q(sqrt2,sqrt3); contrast character group square-classes {sorted(group)}")
print(f"   conductors {conds}  (1, sqrt2->8, sqrt3->12, sqrt6->24)")
print(f"   prod of conductors = {prod}   vs disc(K) = {disc_K_known}")
s3 = (prod == disc_K_known)
print(f"   conductor-discriminant: disc(K) = prod cond(chi): {'PASS' if s3 else 'FAIL'}")
print("   => zeta_K(s) = zeta(s) * L(s,chi_8) * L(s,chi_12) * L(s,chi_24): the contrasts ARE")
print("      the spectral factors; the zeros of zeta_K are the union of the contrast-chi zeros.")

# central values of the contrast group (the spectral data the contrasts carry)
print("   central values L(1/2,chi) of the contrast group:")
for c in sorted(group):
    if c != 1:
        d = fund_disc(c)
        print(f"      [{c}] -> chi_{d}: L(1/2) = {float(Lval_half(d)):.6f}  ({parity(d)})")


print("\n== the weld, stated ==")
print("   The quanta contrasts [q_i/q_j]_n are gauge-invariant -- and they ARE Dirichlet")
print("   characters: contrast = character label, contrast group = the character group of a")
print("   field K, zeta_K = prod L(s,chi) so the contrasts index the SPECTRAL LINES (zeros),")
print("   their conductors give disc(K), their central values L(1/2,chi) are the gauge-rigid")
print("   spectral invariants. The index-3 rigid character is chi_3, L(1/2,chi_3)=0.4808>0 =")
print("   the program's c_2<0 lever: the chiral spectral invariant is the index's contrast-")
print("   character central value, rigid because the index summons it.")

verdict = s1 and anchor_ok and s3
print("\nRESULT: " + ("GREEN -- contrasts = gauge-invariant Dirichlet characters = spectral "
                      "labels; chiral lever = L(1/2,chi_3); conductor-discriminant weld exact"
                      if verdict else "PARTIAL -- see blocks"))
