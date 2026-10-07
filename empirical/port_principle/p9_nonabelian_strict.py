"""
P9 -- Strict non-Abelian symmetry: which states are completely passive under cycles that commute with EVERY
total charge?  Certificate for PortPrinciple.md Section 7 (Theorem 7.4, Proposition 7.5, Open Problem 7.6).

numpy / sympy / fractions only.  Usage: python p9_nonabelian_strict.py

CONTEXT (literature check, 2026-10-02).  Remark 7.3 of v3.2 credited the non-Abelian converse to Guryanova et al.
2016, Yunger Halpern et al. 2016 and Lostaglio-Jennings-Rudolph 2017.  Those works prove a DIFFERENT statement:
with a reference frame and charge batteries, and work valued by H - sum mu_j Q_j, complete passivity singles out
the NATS (Pusz-Woronowicz applied to H - mu.Q), and LJR show that the maximum-entropy state is not passive for the
individual charges.  The strict statement used here (energy is the only work; cycles commute with every total
charge; copies of the state only) is not proven there.  This file settles what can be settled finitely.

SETTING.  G = SU(2) acts on H_S = (+)_j V_j (x) M_j; H = (+)_j I (x) H_j.  On n copies the strictly symmetric
unitaries are the unitaries of the commutant (+)_Lambda I_{V_Lambda} (x) End(M_Lambda^(n)).  So rho^{(x)n} is
strictly passive iff, for every total spin Lambda, the multiplicity marginal
  sigma_Lambda = tr_{V_Lambda}(P_Lambda rho^{(x)n} P_Lambda)
is passive for H_n on M_Lambda^(n) (Lemma 7.4a).

PRE-REGISTERED FALSIFIERS (written 2026-10-02 before the first run)
Part A [BLIND] -- invariant states (Theorem 7.4).  For a G-invariant faithful rho = (+)_j (I/d_j) (x) rho_j with
  [rho_j, H_j] = 0, Lemma 7.4a reduces passivity of rho^{(x)n} to: no two configurations nu, nu' of n copies (occupation
  numbers over the levels (j, a)) whose spin multisets share a common total spin satisfy E_nu < E_nu' and
  f_nu > f_nu', where f_(j,a) = -ln(P_(j,a)/d_j).  Theorem 7.4: rho is completely passive iff rho = e^{-beta H}/Z.
  A1  For 12 random rational invariant instances on V_(1/2) (x) C^2 (+) V_0 (x) C^2 (and 4 on V_1 (x) C^2 (+) V_0 (x) C^1;
      weights anti-ordered with energy inside each sector, so that only cross-sector exchanges can activate them),
      the brute-force verdict (build rho^{(x)n}, H_n, collective S_z, S_+; restrict to each highest-weight space;
      test the ordering) equals the configuration-lattice verdict for every n <= 4.        L_A1: any disagreement.
  A2  Gibbs controls (rho_j proportional to e^{-beta H_j} with one beta): passive by brute force for every n <= 4.
                                                                                          L_A2: any activation.
  A3  "Sector chemical potentials" (rho_j proportional to e^{-beta H_j - kappa_j}, kappa_(1/2) != kappa_0): Theorem 7.4
      predicts activation; the lattice criterion finds a violating pair at some n <= 8 for every instance (12 random).
                                                                                          L_A3: an instance passive to n = 8.
Part B [NOT BLIND: exploratory runs preceded this file] -- non-invariant states (Proposition 7.5).
  B1  Spin-temperature correlated qubit, rho = 1/2 |up><up| (x) g1 + 1/2 |dn><dn| (x) g2 with g1 = (20/21, 1/21),
      g2 = (11/20, 9/20) (not a NATS: a NATS is a product r (x) Gibbs): an exact rational witness of strict
      activation at n = 4, total spin 1: two Yamanouchi basis vectors |t,e>, |t',e'> with E(e') > E(e) and
      <t',e'|sigma|t',e'> > <t,e|sigma|t,e> (rational arithmetic).
  B2  NATS controls (r (x) Gibbs, r = diag(4/5, 1/5) and r = diag(2/3, 1/3)): every multiplicity marginal
      Omega_J(e) is exactly proportional to the identity for n <= 5 (sympy, exact).
  B3  Spin-1, r = diag(1/2, 1/10, 2/5) (not of the form c e^{a S_z}) with an energy qubit at e^{-beta eps} = 1/2: an
      exact rational witness of strict activation at some n <= 6; and the NATS control c diag(e^a, 1, e^{-a}) with
      e^a = 2 has flat multiplicity marginals (exact) for n <= 4.
"""
import itertools, math, random
from fractions import Fraction as Fr
from functools import lru_cache
import numpy as np
import sympy as sp
from sympy.physics.quantum.cg import CG

res = []
def check(name, ok, detail=""):
    res.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

# ------------------------------------------------------------------ exact spin coupling helpers
def jset(spins):
    """set of total spins (as Fractions) in the coupling of a multiset of spins."""
    cur = {Fr(0)}
    for j in spins:
        nxt = set()
        for J in cur:
            x = abs(J - j)
            while x <= J + j:
                nxt.add(x); x += 1
        cur = nxt
    return cur

@lru_cache(maxsize=None)
def cgc(j1, m1, j2, m2, J, M):
    """exact Clebsch-Gordan coefficient (Condon-Shortley; a signed square root of a rational)."""
    return sp.simplify(CG(sp.Rational(j1), sp.Rational(m1), sp.Rational(j2), sp.Rational(m2),
                          sp.Rational(J), sp.Rational(M)).doit())

def yam_paths(n, j, J):
    out = []
    def rec(k, jj, path):
        if k == n:
            if jj == J:
                out.append(tuple(path))
            return
        x = abs(jj - j)
        while x <= jj + j:
            rec(k + 1, x, path + [x]); x += 1
    rec(1, j, [j])
    return out

def coeff_exact(n, j, J, s, path):
    """exact Yamanouchi coefficient <J, M, path | s> for the product state s (tuple of m values)."""
    val = sp.Integer(1)
    M = s[0]
    for k in range(1, n):
        Mn = M + s[k]
        if abs(Mn) > path[k]:
            return sp.Integer(0)
        c = cgc(path[k - 1], M, j, s[k], path[k], Mn)
        if c == 0:
            return sp.Integer(0)
        val *= c
        M = Mn
    return val

# ================================================================== PART A (blind): invariant states
print("== Part A [blind]: invariant states (Theorem 7.4) ==", flush=True)
rng = random.Random(970001)

def spin_ops(j):
    d = int(2 * j + 1)
    ms = [j - k for k in range(d)]
    Sz = np.diag([float(m) for m in ms])
    Sp = np.zeros((d, d))
    for a in range(1, d):
        m = ms[a]
        Sp[a - 1, a] = math.sqrt(float(j * (j + 1) - m * (m + 1)))
    return Sz, Sp

def single_copy(sectors):
    """sectors: list of (j, [(E_a, P_a)]) with P_a the eigenvalue weights of rho_j (sum over all = 1).
    Returns Sz, Sp, H, rho on H_S = (+)_j V_j (x) M_j, plus level list [(j, E, f, P/d)]."""
    blocks = []
    for (j, lev) in sectors:
        d = int(2 * j + 1)
        Sz, Sp = spin_ops(j)
        mdim = len(lev)
        Hm = np.diag([float(E) for (E, P) in lev]); Rm = np.diag([float(P) for (E, P) in lev])
        blocks.append((np.kron(Sz, np.eye(mdim)), np.kron(Sp, np.eye(mdim)), np.kron(np.eye(d), Hm),
                       np.kron(np.eye(d) / d, Rm)))
    D = sum(b[0].shape[0] for b in blocks)
    out = [np.zeros((D, D)) for _ in range(4)]
    o = 0
    for b in blocks:
        s = b[0].shape[0]
        for t in range(4):
            out[t][o:o + s, o:o + s] = b[t]
        o += s
    levels = []
    for (j, lev) in sectors:
        d = int(2 * j + 1)
        for (E, P) in lev:
            levels.append((Fr(j), Fr(E), Fr(P) / d))
    return out, levels

def nfold(op_list, n):
    Sz, Sp, H, rho = op_list
    D = Sz.shape[0]
    I = np.eye(D)
    def tot(A):
        T = np.zeros((D ** n, D ** n))
        for i in range(n):
            M = np.array([[1.0]])
            for k in range(n):
                M = np.kron(M, A if k == i else I)
            T += M
        return T
    R = np.array([[1.0]])
    for _ in range(n):
        R = np.kron(R, rho)
    return tot(Sz), tot(Sp), tot(H), R

def brute_passive(op_list, n, tol=1e-11):
    Szn, Spn, Hn, Rn = nfold(op_list, n)
    sz = np.diag(Szn)
    Js = sorted(set(np.round(sz * 2).astype(int)))
    for twoJ in Js:
        if twoJ < 0:
            continue
        idx = np.where(np.round(sz * 2).astype(int) == twoJ)[0]
        idx_up = np.where(np.round(sz * 2).astype(int) == twoJ + 2)[0]
        if len(idx_up):
            A = Spn[np.ix_(idx_up, idx)]
            u, s_, vt = np.linalg.svd(A)
            rank = int((s_ > 1e-9).sum())
            W = vt[rank:].T
        else:
            W = np.eye(len(idx))
        if W.shape[1] == 0:
            continue
        Wf = np.zeros((Szn.shape[0], W.shape[1])); Wf[idx, :] = W
        Hw = Wf.T @ Hn @ Wf; Rw = Wf.T @ Rn @ Wf
        he, hv = np.linalg.eigh(Hw)
        Es = []
        for E in np.unique(np.round(he, 9)):
            sel = np.where(np.abs(he - E) < 1e-7)[0]
            sub = hv[:, sel].T @ Rw @ hv[:, sel]
            ev = np.linalg.eigvalsh((sub + sub.T) / 2)
            Es.append((E, ev.min(), ev.max()))
        Es.sort()
        for a in range(len(Es)):
            for b in range(a + 1, len(Es)):
                if Es[b][2] > Es[a][1] * (1 + tol) + tol * 1e-3:
                    return False
    return True

def lattice_active_at(levels, n):
    """True iff some pair of n-copy configurations with a common total spin is inverted."""
    L = len(levels)
    confs = []
    for comb in itertools.combinations_with_replacement(range(L), n):
        spins = [levels[i][0] for i in comb]
        E = sum(levels[i][1] for i in comb)
        logw = sum(math.log(levels[i][2]) for i in comb)
        w = Fr(1)
        for i in comb:
            w *= levels[i][2]
        confs.append((E, w, frozenset(jset(spins))))
    for a in range(len(confs)):
        for b in range(len(confs)):
            Ea, wa, Ja = confs[a]; Eb, wb, Jb = confs[b]
            if Ea < Eb and wa < wb and (Ja & Jb):
                return True
    return False

def rand_frac(lo, hi, den=12):
    return Fr(rng.randint(int(lo * den), int(hi * den)), den)

def make_instance(kind, beta=None, kappa=None):
    if kind == "half0":
        Eh = sorted([rand_frac(0, 2), rand_frac(0, 2)]); E0 = sorted([rand_frac(0, 2), rand_frac(0, 2)])
        if Eh[0] == Eh[1]: Eh[1] += Fr(1, 3)
        if E0[0] == E0[1]: E0[1] += Fr(1, 4)
        spec = [(Fr(1, 2), Eh), (Fr(0), E0)]
    else:
        E1 = sorted([rand_frac(0, 2), rand_frac(0, 2)]); E0 = [rand_frac(0, 2)]
        if E1[0] == E1[1]: E1[1] += Fr(1, 3)
        spec = [(Fr(1), E1), (Fr(0), E0)]
    raw = []
    for (j, Es) in spec:
        d = int(2 * j + 1)
        if beta is None:
            # arbitrary (generically non-Gibbs) weights, anti-ordered with energy inside each sector, so that the
            # state is passive at n = 1 and only cross-sector exchanges (n >= 2) can activate it
            ws = sorted([Fr(rng.randint(1, 30)) for _ in Es], reverse=True)
            for E, w in zip(Es, ws):
                raw.append((j, E, Fr(d) * w))
            continue
        for E in Es:
            w = Fr(d) * Fr(2) ** (-(int(E * 12) * beta)) * (Fr(3) ** (-kappa) if (kappa and j != 0) else 1)
            raw.append((j, E, w))
    Z = sum(w for (_, _, w) in raw)
    sectors = []
    for (j, Es) in spec:
        sectors.append((j, [(E, w / Z) for (jj, E, w) in raw if jj == j]))
    # [rho_j, H_j] = 0 automatically (diagonal); passivity at n = 1 is NOT imposed: the brute force decides
    return sectors

agree = True; detail = []
insts = [make_instance("half0") for _ in range(12)] + [make_instance("one0") for _ in range(4)]
for t, sectors in enumerate(insts):
    ops, levels = single_copy(sectors)
    for n in range(1, 5):
        b = brute_passive(ops, n)
        l = not lattice_active_at(levels, n)
        if b != l:
            agree = False; detail.append(f"inst {t} n={n}: brute={b} lattice={l}")
check("A1 [blind] brute-force strict passivity = configuration-lattice verdict (16 invariant instances, n<=4)",
      agree, "; ".join(detail) if detail else "all 64 verdicts agree")

gibbs_ok = True; gdet = []
for t in range(6):
    sectors = make_instance("half0" if t < 4 else "one0", beta=1, kappa=0)
    ops, levels = single_copy(sectors)
    for n in range(1, 5):
        if not brute_passive(ops, n):
            gibbs_ok = False; gdet.append(f"inst {t} n={n}")
check("A2 [blind] Gibbs controls passive under strict symmetry for n <= 4 (6 instances)", gibbs_ok,
      "; ".join(gdet) if gdet else "all passive")

act = True; adet = []
for t in range(12):
    kap = rng.choice([-2, -1, 1, 2])
    sectors = make_instance("half0", beta=1, kappa=kap)
    ops, levels = single_copy(sectors)
    nstar = None
    for n in range(1, 9):
        if lattice_active_at(levels, n):
            nstar = n; break
    adet.append(f"kappa={kap}: n*={nstar}")
    if nstar is None:
        act = False
check("A3 [blind] sector chemical potentials are activated (Theorem 7.4): n* <= 8 for 12 instances", act,
      "; ".join(adet))

# ================================================================== PART B (not blind): non-invariant states
print("== Part B [NOT BLIND]: non-invariant states (Proposition 7.5) ==", flush=True)
half = sp.Rational(1, 2)

def omega_diag_exact(n, j, J, weight):
    """exact diagonal of Omega_J(e) for every energy configuration class e = 1^m 0^(n-m) (qubit energy register),
    for a state diagonal in (S_z) x (energy): weight(s_i, e_i) rational."""
    paths = yam_paths(n, sp.Rational(j), sp.Rational(J))
    ms = [sp.Rational(j) - k for k in range(int(2 * j + 1))]
    configs = list(itertools.product(ms, repeat=n))
    coeffs = {s: [coeff_exact(n, sp.Rational(j), sp.Rational(J), s, p) for p in paths] for s in configs}
    out = {}
    for m in range(n + 1):
        e = (1,) * m + (0,) * (n - m)
        diag = []
        for a in range(len(paths)):
            tot = sp.Integer(0)
            for s in configs:
                c = coeffs[s][a]
                if c != 0:
                    w = sp.Integer(1)
                    for i in range(n):
                        w *= weight(s[i], e[i])
                    tot += w * c ** 2
            tot = sp.Rational(tot)       # c^2 is rational, so tot is an exact rational (no nsimplify: P4.R10 lesson)
            diag.append(tot)
        out[m] = diag
    return paths, out, coeffs, configs

def find_witness(n, j, weight, Jlist):
    for J in Jlist:
        paths, diag, _, _ = omega_diag_exact(n, j, J, weight)
        for m in range(n):
            for m2 in range(m + 1, n + 1):
                lo = min(diag[m]); hi = max(diag[m2])
                if hi > lo:
                    return J, m, m2, lo, hi
    return None

g1 = (sp.Rational(20, 21), sp.Rational(1, 21)); g2 = (sp.Rational(11, 20), sp.Rational(9, 20))
def w_T1(s, e):
    return half * (g1[e] if s > 0 else g2[e])
wit = find_witness(4, half, w_T1, [1])
ok = wit is not None and all(isinstance(x, sp.Rational) or x.is_rational for x in wit[3:])
check("B1 [not blind] correlated spin-temperature qubit: exact rational strict-activation witness at n=4, J=1", ok,
      f"J={wit[0]}, energy m={wit[1]} -> m'={wit[2]}: <sigma>_low = {wit[3]} < <sigma>_high = {wit[4]} "
      f"(ratio {float(wit[4] / wit[3]):.4f})" if wit else "none found")

def flat_exact(n, j, J, weight):
    paths = yam_paths(n, sp.Rational(j), sp.Rational(J))
    ms = [sp.Rational(j) - k for k in range(int(2 * j + 1))]
    configs = list(itertools.product(ms, repeat=n))
    coeffs = {s: [coeff_exact(n, sp.Rational(j), sp.Rational(J), s, p) for p in paths] for s in configs}
    Om = sp.zeros(len(paths), len(paths))
    for s in configs:
        w = sp.Integer(1)
        for i in range(n):
            w *= weight(s[i])
        v = sp.Matrix(coeffs[s])
        Om += w * (v * v.T)
    Om = sp.simplify(Om)
    d0 = Om[0, 0]
    return all(sp.simplify(Om[a, b] - (d0 if a == b else 0)) == 0 for a in range(len(paths)) for b in range(len(paths)))

flat2 = True; fdet = []
for rr in [(sp.Rational(4, 5), sp.Rational(1, 5)), (sp.Rational(2, 3), sp.Rational(1, 3))]:
    for n in range(2, 6):
        for twoJ in range(n % 2, n + 1, 2):
            J = sp.Rational(twoJ, 2)
            f = flat_exact(n, half, J, lambda s, rr=rr: rr[0] if s > 0 else rr[1])
            if not f:
                flat2 = False; fdet.append(f"r={rr} n={n} J={J}")
check("B2 [not blind] NATS controls (spin-1/2): every multiplicity marginal exactly proportional to I, n<=5", flat2,
      "; ".join(fdet) if fdet else "all flat (exact)")

r1 = {sp.Integer(1): sp.Rational(1, 2), sp.Integer(0): sp.Rational(1, 10), sp.Integer(-1): sp.Rational(2, 5)}
ge = (sp.Rational(2, 3), sp.Rational(1, 3))          # energy qubit with e^{-beta eps} = 1/2
def w_spin1(s, e):
    return r1[s] * ge[e]
wit3 = None
for n in range(3, 7):
    Jl = list(range(0, n + 1))
    wit3 = find_witness(n, 1, w_spin1, Jl)
    if wit3:
        wit3 = (n,) + wit3
        break
check("B3a [not blind] non-group spin-1 state with energy qubit (x = 1/2): exact strict-activation witness, n<=6",
      wit3 is not None, f"n={wit3[0]}, J={wit3[1]}, m={wit3[2]} -> m'={wit3[3]}: {wit3[4]} < {wit3[5]} "
      f"(ratio {float(wit3[5] / wit3[4]):.4f})" if wit3 else "none found")
nats1 = {sp.Integer(1): sp.Rational(4, 7), sp.Integer(0): sp.Rational(2, 7), sp.Integer(-1): sp.Rational(1, 7)}
flat3 = all(flat_exact(n, 1, J, lambda s: nats1[s]) for n in range(2, 5) for J in range(0, n + 1)
            if yam_paths(n, sp.Integer(1), sp.Integer(J)))
check("B3b [not blind] NATS control (spin-1, ratios 4:2:1): multiplicity marginals exactly flat, n<=4", flat3)

print(f"\nTOTAL: {sum(res)}/{len(res)} PASS")
