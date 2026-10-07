"""probe_finite_frobenius_lattice.py — anchoring certificate for Pinf-B.

The finite compression of the arithmetic-site Frobenius correspondences Psi_lambda (Connes-Consani)
at level m | P_n is the lattice of multiplication correspondences Gamma_a = {(x, ax)} on (Z/m)^2,
a in (Z/m)^x.  This probe certifies the ORDER-2 / ORDER-3 DICHOTOMY:

  THM B.1 (order-2 blindness; all certified exactly):
   (i)  the overlap Gram of the graphs is the gcd-circulant G(a,b) = gcd(a-b, m); its eigenvalues are
        lambda_k = prod_{p|m} ((p-1) + p*[p|k])  — POSITIVE (PD, no index), EVEN in k, functions of
        gcd(k,m) only: order-2 set data = divisor lattice, nothing else.
   (ii) the composition/Weil pairing T(a,b) = gcd(a b^{-1} - 1, m) on units has eigenvalues
        mu_chi = prod_{p|m} (p-1)(1 + [chi_p principal])  — REAL, POSITIVE, equal for chi and bar chi,
        depending ONLY on the ramification SUPPORT of chi: no phases, no L-values, chirality-blind.
   (iii) the finite Weil sigma-form sigma(Z o Z^t), sigma(Gamma_c) = d1 + d2 - Gamma_c.Delta
        = 2 - gcd(c-1, m), has spectrum sigma_hat(chi) = 2 phi(m)[chi=chi_0] - mu_chi <= 0:
        the POSITIVE (timelike) sector is EMPTY; the light cone is touched only at m = prime,
        chi = chi_0.  The hyperbolic pole plane (Weil's f1, f2; W1's e^{+-x/2}) cannot be generated
        at finite level: the finite correspondences are degree-1 (unitary).  Even the true Frobenius
        x -> x^q on F_{q^2} is a BIJECTION on points (scheme degree q lives in dz^q = 0, invisible
        set-theoretically): expansion/degree is not point data — over Q its carrier is the
        archimedean modulus of the scaling flow.

  THM B.2 (order-3 first visibility):
   (iv) Jacobi sums J(chi,psi) (the order-3 additive-multiplicative contraction of the same lattice)
        have |J| = sqrt(p) (elementary) and NON-REAL phases with J(bar chi, bar psi) = conj J(chi,psi):
        the first chirality-bearing invariant is order 3 — these ARE the Frobenius eigenvalues of the
        abelian (Fermat) quotients.
   (v)  the order-3 selection-rule mass of the unit lattice (unordered nonzero triples a+b+c == 0
        mod p) equals ocho sec.5.1's S(p) (0, 2, (p^2-1)/6), and pure_V(P_n) = sum S(p_i): the
        discrete cubic witness IS the order-3 mass of the Frobenius lattice.

No torch.  Deterministic.  Exit GREEN iff all checks pass.
"""
import math, cmath, sys
from itertools import product

PASS = True
def check(label, ok, detail=""):
    global PASS
    print(("  PASS " if ok else "  FAIL ") + label + (("  " + detail) if detail else ""))
    if not ok: PASS = False

def primes_of(m):
    ps, d, mm = [], 2, m
    while d*d <= mm:
        if mm % d == 0:
            ps.append(d)
            while mm % d == 0: mm //= d
        d += 1
    if mm > 1: ps.append(mm)
    return ps

def primitive_root(p):
    if p == 2: return 1
    for g in range(2, p):
        seen, x = set(), 1
        for _ in range(p-1):
            x = x*g % p; seen.add(x)
        if len(seen) == p-1: return g
    raise RuntimeError

# ---------------------------------------------------------------- (i) gcd-circulant
print("== (i) additive gcd-circulant G(a,b)=gcd(a-b,m): PD, even, divisor-lattice-only ==")
for m in (30, 210):
    ps = primes_of(m)
    lam_direct = []
    for k in range(m):
        s = sum(math.gcd(c, m)*cmath.exp(-2j*math.pi*k*c/m) for c in range(m))
        lam_direct.append(s)
    imag_max = max(abs(s.imag) for s in lam_direct)
    formula = [math.prod((p-1) + p*(1 if k % p == 0 else 0) for p in ps) for k in range(m)]
    diff = max(abs(lam_direct[k].real - formula[k]) for k in range(m))
    check(f"m={m}: eigenvalues real (max imag {imag_max:.1e})", imag_max < 1e-8)
    check(f"m={m}: lambda_k = prod_p((p-1)+p[p|k])  (max dev {diff:.1e})", diff < 1e-7)
    check(f"m={m}: all positive (PD, no index possible)", min(formula) > 0,
          f"min={min(formula)}")
    check(f"m={m}: even, gcd(k,m)-only", all(formula[k] == formula[(m-k) % m] for k in range(m)))

# ------------------------------------------------- units, characters via CRT
def unit_data(m):
    ps = primes_of(m)
    units = [a for a in range(1, m) if math.gcd(a, m) == 1]
    gens = {p: primitive_root(p) for p in ps}
    ind = {}
    for p in ps:
        ind[p] = {}
        x = 1
        for e in range(p-1):
            ind[p][x] = e; x = x*gens[p] % p
    # characters = exponent tuples j = (j_p), chi_j(a) = prod_p e(j_p ind_p(a)/(p-1))
    Js = list(product(*[range(p-1) for p in ps]))
    def chi(j, a):
        v = 0.0
        for (p, jp) in zip(ps, j):
            if p == 2: continue                      # (Z/2)^x trivial
            v += jp*ind[p][a % p]/(p-1)
        return cmath.exp(2j*math.pi*v)
    return ps, units, Js, chi

# ---------------------------------------------------------------- (ii) composition form
print("== (ii) multiplicative composition form T(a,b)=gcd(ab^-1-1,m): support-only, chiral-blind ==")
for m in (30, 210):
    ps, units, Js, chi = unit_data(m)
    phi = len(units)
    mu = {}
    for j in Js:
        s = sum(math.gcd((c-1) % m if (c-1) % m else 0, m) if (c-1) % m else m for c in units) \
            if False else sum((math.gcd(c-1, m) if c != 1 else m)*chi(j, c).conjugate() for c in units)
        mu[j] = s
    imax = max(abs(mu[j].imag) for j in Js)
    form = {j: math.prod((p-1)*(1 + (1 if jp == 0 else 0)) for (p, jp) in zip(ps, j)) for j in Js}
    dev = max(abs(mu[j].real - form[j]) for j in Js)
    conj_ok = all(abs(mu[j] - mu[tuple((-jp) % (p-1) for (p, jp) in zip(ps, j))]) < 1e-7 for j in Js)
    check(f"m={m}: mu_chi real (max imag {imax:.1e})", imax < 1e-7)
    check(f"m={m}: mu_chi = prod_p (p-1)(1+[chi_p princ])  (max dev {dev:.1e})", dev < 1e-6)
    check(f"m={m}: mu_chi = mu_(bar chi)  (chirality-blind)", conj_ok)
    check(f"m={m}: depends only on ramification support",
          len({(tuple(jp == 0 for jp in j), form[j]) for j in Js}) == len({tuple(jp == 0 for jp in j) for j in Js}))

# ---------------------------------------------------------------- (iii) finite Weil sigma-form
print("== (iii) finite Weil form sigma_hat(chi) = 2 phi(m)[chi0] - mu_chi: positive sector EMPTY ==")
for m in (7, 30, 210):
    ps, units, Js, chi = unit_data(m)
    phi = len(units)
    vals = []
    for j in Js:
        muj = math.prod((p-1)*(1 + (1 if jp == 0 else 0)) for (p, jp) in zip(ps, j))
        sig = (2*phi if all(jp == 0 for jp in j) else 0) - muj
        vals.append((j, sig))
    mx = max(v for _, v in vals)
    nullv = [j for j, v in vals if v == 0]
    check(f"m={m}: max sigma_hat = {mx} <= 0 (no timelike sector)", mx <= 0)
    if len(ps) == 1:
        check(f"m={m} (prime): principal direction exactly LIGHTLIKE (sigma_hat=0)",
              nullv == [tuple([0]*len(ps))])
    else:
        check(f"m={m} (composite): strictly inside the negative cone", mx < 0, f"max={mx}")

# degree-1 fact: Frobenius x->x^5 on F_25 is a bijection on points (scheme degree 5 invisible)
F = [(a, b) for a in range(5) for b in range(5)]          # a + b*alpha, alpha^2 = 3
def fmul(z, w):
    (a, b), (c, d) = z, w
    return ((a*c + 3*b*d) % 5, (a*d + b*c) % 5)
def fpow(z, n):
    r = (1, 0)
    for _ in range(n): r = fmul(r, z)
    return r
img = {fpow(z, 5) for z in F}
fixed = [z for z in F if fpow(z, 5) == z]
check("Frobenius x->x^5 on F_25: bijection on points (set-degree 1; scheme degree 5 in dz^5=0)",
      len(img) == 25 and len(fixed) == 5, f"|image|={len(img)}, #fixed={len(fixed)} (=q)")

# ---------------------------------------------------------------- (iv) Jacobi sums: order-3 phases
print("== (iv) order-3 contraction: Jacobi sums |J|=sqrt(p), non-real chiral phases ==")
for p in (7, 13):
    g = primitive_root(p)
    ind = {}
    x = 1
    for e in range(p-1):
        ind[x] = e; x = x*g % p
    def chip(j, a): return cmath.exp(2j*math.pi*j*ind[a]/(p-1)) if a % p else 0
    bad, phases, conj_ok = 0.0, [], True
    for j1 in range(1, p-1):
        for j2 in range(1, p-1):
            if (j1 + j2) % (p-1) == 0: continue       # chi*psi principal -> excluded
            J = sum(chip(j1, x)*chip(j2, (1-x) % p) for x in range(2, p))
            bad = max(bad, abs(abs(J) - math.sqrt(p)))
            phases.append(cmath.phase(J))
            Jc = sum(chip(p-1-j1, x)*chip(p-1-j2, (1-x) % p) for x in range(2, p))
            if abs(Jc - J.conjugate()) > 1e-8: conj_ok = False
    nonreal = sum(1 for th in phases if min(abs(th), abs(abs(th)-math.pi)) > 1e-6)
    check(f"p={p}: | |J| - sqrt(p) | < 1e-9 on all admissible pairs", bad < 1e-9, f"max dev {bad:.1e}")
    check(f"p={p}: non-real phases present ({nonreal}/{len(phases)}) — chirality lives at order 3", nonreal > 0)
    check(f"p={p}: J(bar chi, bar psi) = conj J(chi, psi)  (conjugation = chirality flip)", conj_ok)

# ---------------------------------------------------------------- (v) pure_V = order-3 unit-lattice mass
print("== (v) cubic witness: S(p) = # unordered nonzero triples a+b+c=0 mod p; pure_V = sum S ==")
def S_count(p):
    seen = set()
    for a in range(1, p):
        for b in range(1, p):
            c = (-a - b) % p
            if c: seen.add(tuple(sorted((a, b, c))))
    return len(seen)
S_formula = lambda p: 0 if p == 2 else (2 if p == 3 else (p*p-1)//6)
PR = [2, 3, 5, 7, 11, 13]
ok = all(S_count(p) == S_formula(p) for p in PR)
check("S(p) brute-force == ocho closed form for p<=13", ok,
      " ".join(f"S({p})={S_count(p)}" for p in PR))
pure = 0
table = {2: 2, 3: 6, 4: 14, 5: 34, 6: 62}
ok2 = True
for i, p in enumerate(PR, start=1):
    pure += S_formula(p)
    if i in table and pure != table[i]: ok2 = False
check("pure_V(P_n) = sum S(p_i) reproduces ocho sec.5.2 table (n=2..6)", ok2,
      f"pure_V(P_6)={pure}")

print()
print("ORDER-2 invariants of the finite Frobenius lattice: gcd / ramification-support only —")
print("positive-definite or negative-semidefinite, REAL, chi<->bar-chi-blind: no index, no arithmetic.")
print("ORDER-3 invariants: Jacobi phases (= abelian Frobenius eigenvalues) + pure_V selection mass.")
print()
print("RESULT: " + ("GREEN — all certified" if PASS else "RED — failures above"))
sys.exit(0 if PASS else 1)
