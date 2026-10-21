"""Finite Gaussian observer models from the October 2026 research conversation.

Reference ensemble: q(0) ~ N(0, T K^-1); hidden target
u=sqrt(3/T)*(e(0)+4*b(0)/3). All work is reference-averaged.
No code here modifies a manuscript or silently assumes a stationary active bath.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.optimize import brentq


GAP = 0.1
MAX_D = 8.0 - GAP - 16.0 / (3.0 - GAP)


def stiffness(d: float, h: float) -> np.ndarray:
    return np.array([[3.0, 4.0, 0.0], [4.0, 8.0-d, h], [0.0, h, d]])


def budget_stiffness(d: float, r: float) -> np.ndarray:
    """r in [0,1] parameterizes exactly the positive h stability region."""
    if not GAP <= d <= MAX_D or not 0 <= r <= 1:
        raise ValueError("Outside the declared component budget")
    return stiffness(d, r*np.sqrt(max(0.0, (d-GAP)*(MAX_D-d))))


def circulation(omega: float) -> np.ndarray:
    return np.array([[0.0, 0.0, 0.0], [0.0, 0.0, omega], [0.0, -omega, 0.0]])


def port_visibility(t: float) -> float:
    """c=3, |B|=4, independent unit-temperature hidden/blanket baths."""
    th = np.tanh(5.0*t)
    info = 8.0*th/(5.0+3.0*th)  # T=1; S=1/3 cancels temperature.
    return float(info/(3.0+info))


def covariance_step(A, diffusion, P0, t):
    """Exact stable OU covariance via its stationary Lyapunov solution."""
    E = expm(-A*t)
    Ps = solve_continuous_lyapunov(A, 2.0*diffusion)
    P = Ps + E@(P0-Ps)@E.T
    return E, (P+P.T)/2


def observer(K, t, omega=0.0, mobility=1.0, gate_deadline=None,
             gate_mobility=0.01, temperature=1.0):
    """Acquire for t; optionally remove the drive and gate until deadline.

    Actual force is -Nq and mobility M. Work includes M in the drift and
    the Stratonovich correction -T tr(MN), zero for the diagonal M here.
    Work excludes switch/actuator hardware and any signal preparation.
    """
    if t < 0 or mobility <= 0 or temperature <= 0:
        raise ValueError("Nonphysical duration, mobility or temperature")
    M = np.diag([1.0, 1.0, mobility])
    N = circulation(omega)
    A = M@(K+N)
    P0 = temperature*np.linalg.inv(K)
    Ps = solve_continuous_lyapunov(A, 2.0*temperature*M)
    E = expm(-A*t)
    delta = P0-Ps
    P = Ps+E@delta@E.T
    integrated = solve_continuous_lyapunov(A, delta-E@delta@E.T)
    G = N.T@A
    work = float(t*np.trace(G@Ps)+np.trace(G@integrated)
                 -temperature*t*np.trace(M@N))
    drive_end_P = P.copy()
    if gate_deadline is not None:
        if gate_deadline < t:
            raise ValueError("Readout cannot precede the gate")
        Mh = np.diag([1.0, 1.0, gate_mobility])
        H = expm(-Mh@K*(gate_deadline-t))
        P = P0+H@(P-P0)@H.T
        E = H@E
    P = (P+P.T)/2
    visibility = float((temperature/3.0)*E[2, 0]**2/P[2, 2])
    F = gaussian_free_energy(drive_end_P, K, temperature)
    precision = np.linalg.inv(P)
    return dict(visibility=visibility, work_over_T=work/temperature,
                variance_over_T=float(P[2, 2]/temperature), covariance=P,
                propagator=E, drive_end_covariance=drive_end_P,
                drive_end_free_energy_over_T=F,
                drive_entropy_production=work/temperature-F,
                precision_ei=float(precision[0, 2]),
                partial_correlation_ei_given_b=float(
                    -precision[0, 2]/np.sqrt(precision[0, 0]*precision[2, 2])))


def gaussian_free_energy(P, K, temperature=1.0):
    X = K@P/temperature
    sign, ld = np.linalg.slogdet(X)
    if sign <= 0:
        raise ValueError("Nonpositive covariance determinant")
    return float((np.trace(X)-len(K)-ld)/2.0)


def frontier(E: float, R: float = 4.0):
    """Exact global deterministic rotation optimum, including a rate cap.

    Normalized duration tau=alpha*t and rate r=omega/alpha. This is a
    transfer stage, not the three-coordinate observer's full frontier.
    """
    if E < 0 or R <= 0:
        raise ValueError("E>=0 and R>0 required")
    if E == 0:
        return dict(visibility=0.0, angle=0.0, rate=0.0, duration=0.0,
                    work_over_T=0.0, regime="zero")
    angle0, angle1 = np.arctan(R/2.0), np.arctan(R)
    E0, E1 = 2.0*R*angle0, 2.0*R*angle1
    if E < E0:
        theta = brentq(lambda x: 4*x*np.tan(x)-E, 0.0, angle0, xtol=1e-14)
        rate = 2.0*np.tan(theta)
        regime = "work_limited"
    elif E < E1:
        theta, rate, regime = E/(2*R), R, "work_and_rate_limited"
    else:
        theta, rate, regime = angle1, R, "rate_limited"
    duration = theta/rate
    return dict(visibility=float(np.exp(-2*duration)*np.sin(theta)**2),
                angle=float(theta), rate=float(rate), duration=float(duration),
                work_over_T=float(2*rate*rate*duration), regime=regime)


def frontier_objective(theta, E, R):
    if E == 0:
        return 0.0
    tau = max(2*theta*theta/E, theta/R)
    return float(np.exp(-2*tau)*np.sin(theta)**2)


# Full-precision candidates transcribed from the conversation, not recomputed
# optimizer outputs. Reproduction verifies their values, not global optimality.
CANDIDATES = {
    "baseline_peak": dict(d=1.0, h=1.0, t=1.9567041514331798,
                          expected=0.0077872529305161),
    "passive_peak": dict(d=1.513752857740705, h=0.9966577914723513,
                         t=1.7224937087339054, expected=0.009250087738064537),
    "constant_deadline": dict(d=1.6616164828894258, h=1.0612009465191348,
                              t=10.0, mobility=10**(-0.3292660108182104),
                              expected=0.0019779065221337674),
    "passive_gated": dict(d=1.4866527250823187, h=1.0197783303313308,
                          t=1.7553826517927784, gate_deadline=10.0,
                          expected=0.00861339958486881),
    "active_peak_E1": dict(d=1.4206816623178493, h=0.6912585213956283,
                           omega=-0.858076000871971, t=1.1281969373382619,
                           budget=1.0, expected=0.018428126261418525),
    "active_peak_E10": dict(d=0.8742097892087175, h=0.22573806156759046,
                            omega=-3.944579305428668, t=0.5793468395097395,
                            budget=10.0, expected=0.048225449816711376),
    "active_gated_E1": dict(d=1.3691618907306502, h=0.7569035493375817,
                            omega=-0.8296361052501221, t=1.1765367760907959,
                            gate_deadline=10.0, budget=1.0,
                            expected=0.016568708654564158),
    "active_gated_E10": dict(d=0.8431250914109382, h=0.328238533858396,
                             omega=-3.811124709125496, t=0.6087800734056767,
                             gate_deadline=10.0, budget=10.0,
                             expected=0.04090894782239556),
}


def evaluate_candidate(spec, temperature=1.0):
    kwargs = {k:v for k,v in spec.items() if k not in ("d", "h", "expected", "budget")}
    return observer(stiffness(spec["d"], spec["h"]), temperature=temperature, **kwargs)
