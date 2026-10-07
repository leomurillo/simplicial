"""
Does the CRT conductor grading pin the SM finite charge-conjugation J_F,
or leave mixing freedom?  Compute the moduli space dimension under
Branch B (block C^2 + C^3) and Branch T (tensor C^2 x C^3) gradings.

Method (let the data speak, no narrative):
  - Build the 5 one-generation modules of Lambda^2 E + E*, E = C^2 + C^3,
    as explicit gauge representations of su(2) + su(3) + u(1)_Y.
  - The linear part of an admissible antilinear J_F is an operator T on the
    total matter space H = (+) H_i that (a) intertwines the gauge action
    (gauge-equivariant), (b) maps each module to a charge-conjugate slot,
    (c) commutes with the conductor-block projectors of the chosen branch.
  - dim(solution space) = (# independent free parameters in such T).
    Pure phases per irreducible = trivial/expected gauge-trivial freedom.
    Any EXTRA dimension = genuine J_F ambiguity the grading fails to break.
"""

import numpy as np
import itertools

np.set_printoptions(linewidth=140, suppress=True)

# ---------------------------------------------------------------------------
# Gauge generators on the fundamentals
# su(2): Pauli/2 ; su(3): Gell-Mann/2 ; u(1): scalar Y
# ---------------------------------------------------------------------------
def su2_gens():
    sx = np.array([[0,1],[1,0]], complex)
    sy = np.array([[0,-1j],[1j,0]], complex)
    sz = np.array([[1,0],[0,-1]], complex)
    return [sx/2, sy/2, sz/2]

def su3_gens():
    g = []
    l1 = np.zeros((3,3),complex); l1[0,1]=l1[1,0]=1
    l2 = np.zeros((3,3),complex); l2[0,1]=-1j; l2[1,0]=1j
    l3 = np.diag([1,-1,0]).astype(complex)
    l4 = np.zeros((3,3),complex); l4[0,2]=l4[2,0]=1
    l5 = np.zeros((3,3),complex); l5[0,2]=-1j; l5[2,0]=1j
    l6 = np.zeros((3,3),complex); l6[1,2]=l6[2,1]=1
    l7 = np.zeros((3,3),complex); l7[1,2]=-1j; l7[2,1]=1j
    l8 = np.diag([1,1,-2]).astype(complex)/np.sqrt(3)
    for L in [l1,l2,l3,l4,l5,l6,l7,l8]:
        g.append(L/2)
    return g

S2 = su2_gens()      # 3 generators, 2-dim
S3 = su3_gens()      # 8 generators, 3-dim
I2 = np.eye(2,dtype=complex)
I3 = np.eye(3,dtype=complex)
I1 = np.eye(1,dtype=complex)

def kron(*mats):
    out = np.array([[1.0+0j]])
    for m in mats:
        out = np.kron(out, m)
    return out

# ---------------------------------------------------------------------------
# The five modules.  For each: dimension, list of gauge generators (as full
# matrices on that module), and its (block-branch, tensor-branch) conductor tag.
#
# SM one-generation (left-handed Weyl), internal package Lambda^2 E + E*:
#   Q_L   = (2,3)_{1/6}    from V (x) W        dim 6
#   uRc   = (1,3bar)_{-2/3} from Lambda^2 W     dim 3
#   eRc   = (1,1)_{1}       from Lambda^2 V     dim 1
#   L_L   = (2,1)_{-1/2}    from V*             dim 2
#   dRc   = (1,3bar)_{1/3}  from W*             dim 3
# ---------------------------------------------------------------------------
def module_gens(su2_rep, su3_rep, Y, dim):
    """Return list of gauge generators acting on a module of given dim.
       su2_rep in {'2','1'}, su3_rep in {'3','3bar','1'}.  u(1): Y * I."""
    gens = []
    # su(2) part
    if su2_rep == '2':
        s2_loc = [s for s in S2]; d2 = 2
    else:
        s2_loc = [np.zeros((1,1),complex) for _ in S2]; d2 = 1
    # su(3) part
    if su3_rep == '3':
        s3_loc = [t for t in S3]; d3 = 3
    elif su3_rep == '3bar':
        s3_loc = [-t.conj() for t in S3]; d3 = 3   # conjugate rep
    else:
        s3_loc = [np.zeros((1,1),complex) for _ in S3]; d3 = 1
    assert d2*d3 == dim, (su2_rep,su3_rep,dim)
    Id2 = np.eye(d2,dtype=complex); Id3 = np.eye(d3,dtype=complex)
    for s in s2_loc:
        gens.append(np.kron(s, Id3))
    for t in s3_loc:
        gens.append(np.kron(Id2, t))
    gens.append(Y*np.eye(dim,dtype=complex))   # u(1)_Y
    return gens

modules = {
 # name : (su2, su3, Y, dim, blockcond, tensorcond)
 'Q_L' : ('2','3',   1/6,  6, 6, 6),
 'uRc' : ('1','3bar',-2/3, 3, 3, 3),
 'eRc' : ('1','1',   1.0,  1, 1, 1),
 'L_L' : ('2','1',  -1/2,  2, 2, 2),
 'dRc' : ('1','3bar', 1/3, 3, 3, 3),
}

names = list(modules.keys())
dims  = {n:modules[n][3] for n in names}
offsets = {}
o=0
for n in names:
    offsets[n]=o; o+=dims[n]
N = o   # total matter dimension (one chirality copy)
print("module dims:", dims, " total N =", N)

# Full gauge generators on the direct sum H = (+) H_i  (block diagonal)
def full_gauge_generators():
    # We need the SAME abstract generator acting across all modules
    # simultaneously (it is the global gauge symmetry).  Build per generator.
    G = []
    # su(2): 3 gens
    for k in range(3):
        M = np.zeros((N,N),complex)
        for n in names:
            su2,su3,Y,d,_,_ = modules[n]
            gg = module_gens(su2,su3,Y,d)
            M[offsets[n]:offsets[n]+d, offsets[n]:offsets[n]+d] = gg[k]
        G.append(('su2_%d'%k, M))
    # su(3): 8 gens (indices 3..10 in module_gens)
    for k in range(8):
        M = np.zeros((N,N),complex)
        for n in names:
            su2,su3,Y,d,_,_ = modules[n]
            gg = module_gens(su2,su3,Y,d)
            M[offsets[n]:offsets[n]+d, offsets[n]:offsets[n]+d] = gg[3+k]
        G.append(('su3_%d'%k, M))
    # u(1)_Y
    M = np.zeros((N,N),complex)
    for n in names:
        su2,su3,Y,d,_,_ = modules[n]
        M[offsets[n]:offsets[n]+d, offsets[n]:offsets[n]+d] = Y*np.eye(d,dtype=complex)
    G.append(('u1_Y', M))
    return G

GG = full_gauge_generators()
print("num gauge generators:", len(GG))

# ---------------------------------------------------------------------------
# Charge conjugation maps H -> Hbar*.  Its linear representative T must:
#   (1) intertwine gauge: for every gen X,  X is rep on H, conj rep is -X^T
#       gauge-equivariance of an ANTILINEAR map C with C = T o (complex conj):
#       C X = (Xbar) C  on the conjugate module; in matrix terms the linear
#       T satisfies   T Xbar = (-X^T) T   ... we instead use the standard
#       reduction: the space of antilinear gauge-equivariant maps H->H is the
#       space of linear maps T with  T conj(X) = X T  is NOT it; the clean,
#       basis-free count is the dimension of gauge intertwiners Hom_G(H, Hbar).
#   We compute dim Hom_G(H, conj(H)) directly: linear T with
#       T (Xbar) = (Xbar) T   are intertwiners of conj(H) with itself;
#   charge conj identifies module i with the slot whose gauge rep is conj of i.
#
# Operationally the moduli of admissible J_F (up to overall gauge-trivial
# phases) = dim of the commutant of the gauge action on the matter space,
# RESTRICTED to maps that also commute with the conductor-block projector.
# A larger commutant = more J_F freedom = grading fails to pin J_F.
# ---------------------------------------------------------------------------
def commutant_dim(generator_mats, extra_constraints=()):
    """dim of {T : [T, X]=0 for all X in generator_mats and all extra}."""
    mats = [X for _,X in generator_mats] + list(extra_constraints)
    # Solve vec(T): for each X, (I (x) X - X^T (x) I) vec(T) = 0
    rows = []
    n = mats[0].shape[0]
    Ifull = np.eye(n,dtype=complex)
    for X in mats:
        rows.append(np.kron(Ifull, X) - np.kron(X.T, Ifull))
    A = np.vstack(rows)
    # nullspace dim
    u,s,vh = np.linalg.svd(A)
    tol = 1e-9 * max(A.shape) * (s[0] if s.size else 1.0)
    rank = int((s > tol).sum())
    return n*n - rank

# Baseline: commutant of gauge action alone (no conductor constraint)
base = commutant_dim(GG)
print("\n[gauge only] dim commutant of gauge action on matter space =", base)

# Conductor-block projectors
def conductor_projectors(which):
    """which in {'block','tensor'} -> dict tag->projector matrix on H."""
    tags = {}
    for n in names:
        bc = modules[n][4] if which=='block' else modules[n][5]
        tags.setdefault(bc, [])
        tags[bc].append(n)
    projs = []
    for tag, ns in sorted(tags.items()):
        P = np.zeros((N,N),complex)
        for n in ns:
            P[offsets[n]:offsets[n]+dims[n], offsets[n]:offsets[n]+dims[n]] = \
                np.eye(dims[n],dtype=complex)
        projs.append((tag, ns, P))
    return projs

for branch in ['block','tensor']:
    projs = conductor_projectors(branch)
    print("\n=== Branch %s : conductor classes ===" % branch.upper())
    for tag,ns,_ in projs:
        print("  conductor %s : %s" % (tag, ns))
    Pmats = [P for _,_,P in projs]
    d = commutant_dim(GG, extra_constraints=Pmats)
    print("  dim commutant (gauge AND conductor-grading-preserving) =", d)
    # Decompose: how much is gauge-trivial per-module phase vs genuine mixing?
    # per-irreducible Schur phase count = number of irreducible modules = 5
    print("  -> per-module gauge-trivial phases expected = 5")
    print("  -> EXTRA J_F freedom not killed by this branch =", d - 5)

print("\n" + "="*70)
print("DECISIVE TEST: remove U(1)_Y. Can CRT conductor grading substitute?")
print("="*70)

# Gauge generators WITHOUT u(1)_Y  (su(2) + su(3) only)
GG_noY = [(nm,M) for nm,M in GG if not nm.startswith('u1')]
base_noY = commutant_dim(GG_noY)
print("[su(2)+su(3) only] dim commutant =", base_noY,
      " (rigid would be 5; excess = mixing freedom Y normally kills)")

for branch in ['block','tensor']:
    Pmats=[P for _,_,P in conductor_projectors(branch)]
    d = commutant_dim(GG_noY, extra_constraints=Pmats)
    print("  + %-6s conductor grading: commutant = %d  -> excess over 5 = %d"
          % (branch, d, d-5))

print("\nROBUSTNESS: force Y(uRc)=Y(dRc) (collapse hypercharge) WITH full gauge")
mods2 = dict(modules); mods2['dRc']=('1','3bar',-2/3,3,3,3)  # same Y as uRc
# rebuild generators with collapsed Y
def gauge_with(modmap):
    G=[]
    for k in range(3):
        M=np.zeros((N,N),complex)
        for n in names:
            su2,su3,Y,dd,_,_=modmap[n]; gg=module_gens(su2,su3,Y,dd)
            M[offsets[n]:offsets[n]+dd,offsets[n]:offsets[n]+dd]=gg[k]
        G.append(('su2_%d'%k,M))
    for k in range(8):
        M=np.zeros((N,N),complex)
        for n in names:
            su2,su3,Y,dd,_,_=modmap[n]; gg=module_gens(su2,su3,Y,dd)
            M[offsets[n]:offsets[n]+dd,offsets[n]:offsets[n]+dd]=gg[3+k]
        G.append(('su3_%d'%k,M))
    M=np.zeros((N,N),complex)
    for n in names:
        su2,su3,Y,dd,_,_=modmap[n]
        M[offsets[n]:offsets[n]+dd,offsets[n]:offsets[n]+dd]=Y*np.eye(dd,dtype=complex)
    G.append(('u1_Y',M))
    return G
d_collapsed = commutant_dim(gauge_with(mods2))
print("  commutant with Y(uRc)=Y(dRc) =", d_collapsed,
      " (jump above 5 = the freedom Y was killing)")
for branch in ['block','tensor']:
    Pmats=[P for _,_,P in conductor_projectors(branch)]
    dd=commutant_dim(gauge_with(mods2),extra_constraints=Pmats)
    print("    + %-6s grading then re-pins to: %d" % (branch, dd))
