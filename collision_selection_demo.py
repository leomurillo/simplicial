"""
Collision / scattering on the categorical simplex Z/6 — the conductor selection
rule as a momentum-transfer GATE.

Model (autonomous, energy-conserving):
    state eta(t) in H_6 = { x in R^6 : sum_a x_a = 0 }   (simplex tangent at centroid)
    Lagrangian  L = 1/2 m |eta_dot|^2  - 1/2 m w^2 |eta|^2  + (g3/3) sum_a eta_a^3
        - m   = Fisher inertia g = Q*I = 6*I at the centroid (Paper 32 Thm 3.1)
        - w   = uniform harmonic 'mass term' (so packets are massive oscillators)
        - the cubic term is the Amari-Chentsov tensor:  T(u,v,w) = 36 sum_a u_a v_a w_a
          so V3 = -(g3/3) sum_a eta_a^3 has force  F_a = g3 eta_a^2, projected to H_6.

Why this is the faithful gate.  In the character basis (chi_k(a)=w^{ka}), the cubic
vertex is  T_{klm} = 216 * 1[k+l+m = 0 mod 6]  (Paper 32 Lemma 5.1a).  Writing the
point-basis cubic force  P_H(g3 * eta o eta)  and Fourier-transforming reproduces
EXACTLY that selection rule by the convolution theorem — the mean-subtraction P_H is
the "(3,3,0) gauge-killed" mechanism.  So momentum/energy moves from packet P to
packet P' only through a vertex with one leg in each, i.e. only when allowed by
k+l+m=0.  Packets on Z/6:
        A2 = {k=3}   (p=2 axis, 1 real dim)
        A3 = {k=2,4} (p=3 axis, 2 real dims)
        M  = {k=1,5} (conductor-6 carry, 2 real dims)

Predicted, exactly (Cor. 5.1d):
  (A) pure A2:  eta o eta = chi_3^2 = chi_0 -> killed -> force == 0.  A2 is INERT,
      leaks nothing, ever.
  (B) pure A3:  products stay in {2+2=4, 4+4=2, 2+4=0(killed)} = A3.  A3 self-closes,
      no leak to A2 or M.
  (C) A2 + A3:  cross product 3+2=5 in M  -> M is SOURCED.  And A2 receives force only
      from pairs summing to 3, every one of which (1+2, 4+5) carries an M leg.  So
      A2<->A3 exchange is impossible unless M is populated: M is the obligatory carry.
      Control run kill_M=True forbids M (projects out k=1,5 each step) -> A2 freezes.
"""

import numpy as np

np.set_printoptions(precision=6, suppress=True)

Q = 6
PACKETS = {"A2": [3], "A3": [2, 4], "M": [1, 5]}

m = 6.0       # Fisher inertia g = Q I
w = 1.0       # harmonic frequency
g3 = 0.5      # cubic Amari-Chentsov coupling
dt = 0.004
T_END = 240.0
NSTEPS = int(T_END / dt)
REC = 50      # record every REC steps

chi3 = np.array([(-1.0) ** a for a in range(Q)])              # mode k=3  (A2)
uA3 = np.cos(2 * np.pi * 2 * np.arange(Q) / Q)                # modes k=2,4 (A3)


def proj_H(x):
    return x - x.mean()


def kill_modes(x, ks):
    X = np.fft.fft(x)
    X[ks] = 0.0
    return np.fft.ifft(X).real


def cubic_force(eta):
    # F_a = g3 eta_a^2, projected onto H (gauge mode k=0 removed)
    return proj_H(g3 * eta * eta)


def accel(eta):
    return (-m * w * w * eta + cubic_force(eta)) / m


def packet_energy(eta, v):
    Ee, Ev = np.fft.fft(eta), np.fft.fft(v)
    out = {}
    for name, ks in PACKETS.items():
        e = 0.0
        for k in ks:
            e += 0.5 * m * abs(Ev[k]) ** 2 + 0.5 * m * w * w * abs(Ee[k]) ** 2
        out[name] = e / Q          # Parseval normalization
    return out


def total_energy(eta, v):
    K = 0.5 * m * np.sum(v * v)
    U2 = 0.5 * m * w * w * np.sum(eta * eta)
    U3 = -(g3 / 3.0) * np.sum(eta ** 3)
    return K + U2 + U3


def run(eta0, v0, kill_M=False):
    eta, v = proj_H(eta0.copy()), proj_H(v0.copy())
    if kill_M:
        eta, v = kill_modes(eta, [1, 5]), kill_modes(v, [1, 5])
    ac = accel(eta)
    ts, E, packs = [], [], {n: [] for n in PACKETS}
    Emax = abs(total_energy(eta, v))
    e0 = total_energy(eta, v)
    drift = 0.0
    for n in range(NSTEPS):
        v = v + 0.5 * dt * ac
        eta = eta + dt * v
        if kill_M:
            eta = kill_modes(eta, [1, 5])
        ac = accel(eta)
        v = v + 0.5 * dt * ac
        if kill_M:
            v = kill_modes(v, [1, 5])
        if n % REC == 0:
            ts.append(n * dt)
            E.append(total_energy(eta, v))
            pe = packet_energy(eta, v)
            for nm in PACKETS:
                packs[nm].append(pe[nm])
        drift = max(drift, abs(total_energy(eta, v) - e0))
    return dict(t=np.array(ts), E=np.array(E),
                packs={k: np.array(v) for k, v in packs.items()},
                drift=drift, e0=e0, maxabs=np.max(np.abs(eta)))


def summarize(tag, r):
    p = r["packs"]
    print(f"\n=== {tag} ===")
    print(f"  total energy E0 = {r['e0']:.6f},  max |dE| over run = {r['drift']:.2e}"
          f"   (symplectic conservation)")
    print(f"  max|eta| over run = {r['maxabs']:.3f}  (bounded -> recurrent, Paper 19)")
    for nm in PACKETS:
        arr = p[nm]
        print(f"  E_{nm:<2}:  init={arr[0]:.6e}   min={arr.min():.6e}   "
              f"max={arr.max():.6e}   span={arr.max()-arr.min():.3e}")


# ---------------------------------------------------------------- experiments
print("Z/6 cubic mechanics — selection rule as momentum-transfer gate")
print(f"  m(Fisher)={m}  w={w}  g3={g3}  dt={dt}  T={T_END}  steps={NSTEPS}")

A = run(0.30 * chi3, np.zeros(Q))                       # (A) pure A2
B = run(0.30 * uA3, np.zeros(Q))                        # (B) pure A3
C = run(0.30 * chi3 + 0.30 * uA3, np.zeros(Q))          # (C) A2 + A3, M starts empty
Cn = run(0.30 * chi3 + 0.30 * uA3, np.zeros(Q), kill_M=True)  # (C-control) M forbidden

summarize("(A) pure A2  ->  expect NO leak to A3 or M (A2 cubically isolated)", A)
summarize("(B) pure A3  ->  expect NO leak to A2 or M (A3 self-closes)", B)
summarize("(C) A2 + A3  ->  expect M SOURCED, then A2<->A3 exchange", C)
summarize("(C-control) A2 + A3 with M FORBIDDEN -> expect A2 FROZEN (no exchange)", Cn)

# ---------------------------------------------------------------- certificates
eps = 1e-10
print("\n----------------- CERTIFICATES -----------------")
okA = A["packs"]["A3"].max() < eps and A["packs"]["M"].max() < eps
print(f"[A] A2 isolated: max E_A3={A['packs']['A3'].max():.2e}, "
      f"max E_M={A['packs']['M'].max():.2e}  -> {'PASS' if okA else 'FAIL'} (both ~0)")

okB = B["packs"]["A2"].max() < eps and B["packs"]["M"].max() < eps
print(f"[B] A3 self-closes: max E_A2={B['packs']['A2'].max():.2e}, "
      f"max E_M={B['packs']['M'].max():.2e}  -> {'PASS' if okB else 'FAIL'} (both ~0)")

M_sourced = C["packs"]["M"].max() > 1e-4
print(f"[C] M sourced by A2xA3: E_M init={C['packs']['M'][0]:.2e} -> "
      f"max={C['packs']['M'].max():.2e}  -> {'PASS' if M_sourced else 'FAIL'} (grows from 0)")

# A2<->A3 exchange: how much does A2 energy swing, free vs M-forbidden?
swing_free = C["packs"]["A2"].max() - C["packs"]["A2"].min()
swing_noM = Cn["packs"]["A2"].max() - Cn["packs"]["A2"].min()
gated = swing_noM < 0.02 * swing_free
print(f"[C] A2<->A3 exchange gated by M:")
print(f"     A2 energy swing  (M allowed) = {swing_free:.4e}")
print(f"     A2 energy swing  (M forbidden) = {swing_noM:.4e}")
print(f"     ratio forbidden/allowed = {swing_noM/swing_free:.2e}  -> "
      f"{'PASS' if gated else 'FAIL'} (transfer vanishes without M)")

# ---------------------------------------------------------------- optional plot
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(2, 2, figsize=(12, 7.5), sharex=True)
    runs = [("(A) pure A2: isolated -> nothing leaks", A),
            ("(B) pure A3: self-closes -> nothing leaks", B),
            ("(C) A2+A3: M fills, A2<->A3 exchange opens", C),
            ("(C-ctrl) M forbidden: A2 frozen, no exchange", Cn)]
    col = {"A2": "#d33", "A3": "#27a", "M": "#2a2"}
    for axx, (title, r) in zip(ax.ravel(), runs):
        for nm in PACKETS:
            dev = r["packs"][nm] - r["packs"][nm][0]   # deviation from initial
            axx.plot(r["t"], dev, color=col[nm], lw=1.6, label=f"ΔE_{nm}")
        axx.axhline(0, color="k", lw=0.6, alpha=0.4)
        axx.set_title(title, fontsize=11)
        axx.set_ylabel("packet energy change  ΔE")
        axx.grid(alpha=0.25)
        axx.legend(fontsize=9, loc="upper right")
    for axx in ax[1]:
        axx.set_xlabel("time")
    fig.suptitle("Z/6 cubic scattering — A2<->A3 momentum transfer is gated through M "
                 "(deviation from t=0)", fontsize=13)
    fig.tight_layout()
    fig.savefig("collision_selection_demo.png", dpi=130)
    print("\nplot saved -> collision_selection_demo.png")
except Exception as e:
    print(f"\n(plot skipped: {e})")
