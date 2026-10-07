"""E5 physical discriminator for the Paper 28 Z6 canonical bridge.

Pre-registered protocol
-----------------------

Candidate physical model:

    a_candidate = a_Newton + lambda_E5 * a_T
    a_T         = a_EL(eta_copula) - a_EL(eta_base)

Reduced coordinates use sigma=(rho,u,w).  Cartesian ephemeris propagation
lifts a_T by the mass-metric minimum-norm inverse of D sigma, so the added
body acceleration is translation/rotation neutral and changes only the
declared reduced shape acceleration to first order.

Fixed bridge parameters:

    kappa      = 0.8
    phi_coeffs = (1, 0)
    eta        = Z6 e-pure dyadic product base plus scale-free Heron copula gate
    Pi         = Pi_EL, the Euler-Lagrange projection of the pulled-back cubic
                 Fisher action

Parameter fixing:

    lambda_E5 is fixed once from the declared weak-field cap.  The default
    source is the known weak-field ephemeris calibrator set; the legacy reduced
    weak-field source is still available by command-line switch.  Lambda is then
    held fixed for the dyadic boundary, controlled-regime, Cartesian ephemeris,
    and near-equilateral sign tests. No per-sample or sign-based retuning is
    allowed.

Discriminator metrics:

1. Weak-field/Solar-System consistency.
   On the declared solar-like weak-field samples, require

       ||lambda_E5 a_T||_G / ||a_Newton||_G <= weak_field_tol.

2. Two-body Newtonian recovery on dyadic boundary.
   On near-collinear, pair-dominated boundary samples, require

       ||lambda_E5 a_T||_G / ||a_Newton||_G <= boundary_tol.

3. Controlled sign-definite deviation.
   On near-equilateral samples with the declared shape velocity, require the
   signed metric projection

       <lambda_E5 a_T, a_Newton>_G

   to have one nonzero sign across the sample set and to exceed the declared
   signal floor in relative magnitude.

4. Ephemeris residual.
   On known weak-field/perturbed three-body reference arcs and synthetic
   near-equilateral arcs, propagate

       x_Newton, x_candidate

   from identical initial states for N orbits and require final RMS position
   and velocity deviations, normalized by the initial RMS system scales, to
   stay below the declared ephemeris tolerances.  Also require sampled
   weak-field anomalous acceleration ratios to respect the 1e-10 cap.

5. Cartesian near-equilateral sign consistency.
   Lift the declared near-equilateral shape velocity into Cartesian velocities
   and require the mass-metric projection of lambda_E5 a_T against a_Newton to
   be sign-definite and above the declared signal floor.

Kill conditions:

   - lambda_E5 is non-finite or below lambda_floor.
   - any weak-field ratio exceeds weak_field_tol.
   - any dyadic-boundary ratio exceeds boundary_tol.
   - controlled-regime signs are mixed or all numerically zero.
   - max controlled relative signal is below controlled_signal_floor.
   - ephemeris weak-field sampled ratios exceed weak_field_tol.
   - final ephemeris position/velocity residuals exceed tolerance.
   - Cartesian near-equilateral signs are mixed/zero or below floor.

This audit is intentionally hostile. A KILL means the finite-row bridge remains
mathematically canonical but is not yet a parameter-fixed physical candidate.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import numpy as np

from z6_copula_variational_consistency_audit import el_acceleration
from z6_jacobi_fisher_execution_audit import (
    shape_metric,
    sides_from_sigma,
    triangle_positions_from_sides,
)


SOLAR_G_AU_YEAR = 4.0 * math.pi * math.pi
AU_KM = 149_597_870.7
DAY_PER_YEAR = 365.256363004


@dataclass(frozen=True)
class EphemerisCase:
    name: str
    family: str
    masses: np.ndarray
    positions: np.ndarray
    velocities: np.ndarray
    g_const: float
    period: float
    orbits: int
    weak_field_calibrator: bool
    near_equilateral_sign: bool


def sigma_from_sides(sides: np.ndarray) -> np.ndarray:
    s12, s23, s31 = sides
    rho = math.log(float(np.sum(sides)))
    logs = np.log(sides)
    u = (logs[0] - logs[1]) / math.sqrt(2.0)
    w = (logs[0] + logs[1] - 2.0 * logs[2]) / math.sqrt(6.0)
    return np.array([rho, u, w], dtype=float)


def newtonian_potential(sigma: np.ndarray, masses: np.ndarray, g_const: float) -> float:
    s12, s23, s31 = sides_from_sigma(sigma)
    return float(
        -g_const
        * (
            masses[0] * masses[1] / s12
            + masses[1] * masses[2] / s23
            + masses[2] * masses[0] / s31
        )
    )


def newtonian_lagrangian(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    masses: np.ndarray,
    g_const: float,
    fd_step: float,
) -> float:
    metric = shape_metric(sigma, masses, fd_step)
    kinetic = 0.5 * float(sigmadot @ metric @ sigmadot)
    return kinetic - newtonian_potential(sigma, masses, g_const)


def numerical_gradient(fn, x: np.ndarray, step: float) -> np.ndarray:
    out = np.zeros_like(x, dtype=float)
    for i in range(x.size):
        xp = x.copy()
        xm = x.copy()
        xp[i] += step
        xm[i] -= step
        out[i] = (fn(xp) - fn(xm)) / (2.0 * step)
    return out


def numerical_jacobian(fn, x: np.ndarray, step: float) -> np.ndarray:
    y0 = fn(x)
    out = np.zeros((y0.size, x.size), dtype=float)
    for i in range(x.size):
        xp = x.copy()
        xm = x.copy()
        xp[i] += step
        xm[i] -= step
        out[:, i] = (fn(xp) - fn(xm)) / (2.0 * step)
    return out


def grad_velocity_newtonian(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    masses: np.ndarray,
    fd_step: float,
) -> np.ndarray:
    return shape_metric(sigma, masses, fd_step) @ sigmadot


def newtonian_acceleration(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    masses: np.ndarray,
    g_const: float,
    fd_step: float,
    variation_step: float,
    rcond: float,
) -> np.ndarray:
    metric = shape_metric(sigma, masses, fd_step)
    grad_sigma = numerical_gradient(
        lambda q: newtonian_lagrangian(q, sigmadot, masses, g_const, fd_step),
        sigma,
        variation_step,
    )
    jac_grad_vel = numerical_jacobian(
        lambda q: grad_velocity_newtonian(q, sigmadot, masses, fd_step),
        sigma,
        variation_step,
    )
    rhs = grad_sigma - jac_grad_vel @ sigmadot
    accel, *_ = np.linalg.lstsq(metric, rhs, rcond=rcond)
    return accel


def ternary_acceleration(sigma: np.ndarray, sigmadot: np.ndarray, args: argparse.Namespace) -> np.ndarray:
    copula_args = SimpleNamespace(
        kappa=args.kappa,
        phi_coeffs=args.phi_coeffs,
        fd_step=args.fd_step,
        variation_step=args.variation_step,
        lstsq_rcond=args.lstsq_rcond,
    )
    return el_acceleration(sigma, sigmadot, copula_args) - el_acceleration(
        sigma, sigmadot, copula_args, fixed_theta=0.0
    )


def metric_norm(metric: np.ndarray, vector: np.ndarray) -> float:
    return math.sqrt(max(float(vector @ metric @ vector), 0.0))


def evaluate_state(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    masses: np.ndarray,
    lambda_e5: float,
    args: argparse.Namespace,
) -> dict[str, Any]:
    metric = shape_metric(sigma, masses, args.fd_step)
    a_newton = newtonian_acceleration(
        sigma,
        sigmadot,
        masses,
        args.g_const,
        args.fd_step,
        args.variation_step,
        args.lstsq_rcond,
    )
    a_t = ternary_acceleration(sigma, sigmadot, args)
    participation = e5_participation_factor_from_sigma(sigma, masses, args)
    dynamic = e5_dynamic_suppression_factor(sigmadot, args)
    a_t = participation * dynamic * a_t
    scaled_t = lambda_e5 * a_t
    norm_newton = metric_norm(metric, a_newton)
    norm_t = metric_norm(metric, scaled_t)
    ratio = norm_t / max(norm_newton, 1.0e-300)
    signed_projection = float(scaled_t @ metric @ a_newton)
    relative_signed_projection = signed_projection / max(norm_newton * norm_newton, 1.0e-300)
    return {
        "sigma": sigma.tolist(),
        "sides": sides_from_sigma(sigma).tolist(),
        "sigmadot": sigmadot.tolist(),
        "newtonian_acceleration": a_newton.tolist(),
        "ternary_acceleration_unscaled": a_t.tolist(),
        "ternary_acceleration_scaled": scaled_t.tolist(),
        "participation_factor": participation,
        "dynamic_suppression_factor": dynamic,
        "newtonian_metric_norm": norm_newton,
        "scaled_ternary_metric_norm": norm_t,
        "relative_correction_norm": ratio,
        "signed_metric_projection": signed_projection,
        "relative_signed_projection": relative_signed_projection,
    }


def sample_from_sides(sides: list[float], sigmadot: list[float]) -> tuple[np.ndarray, np.ndarray]:
    return sigma_from_sides(np.array(sides, dtype=float)), np.array(sigmadot, dtype=float)


def build_samples(args: argparse.Namespace) -> dict[str, list[tuple[np.ndarray, np.ndarray]]]:
    weak_v = [1.0e-4, -2.0e-4, 1.0e-4]
    boundary_v = [2.0e-4, -1.0e-4, 0.5e-4]
    controlled_v = list(args.controlled_shape_velocity)
    return {
        "weak_field": [
            sample_from_sides([1.0, 4.25, 5.2], weak_v),
            sample_from_sides([1.0, 8.65, 9.55], weak_v),
            sample_from_sides([1.0, 14.2, 15.1], weak_v),
        ],
        "dyadic_boundary": [
            sample_from_sides([1.0, args.boundary_radius, args.boundary_radius], boundary_v),
            sample_from_sides([1.0, 2.0 * args.boundary_radius, 2.0 * args.boundary_radius], boundary_v),
        ],
        "controlled": [
            sample_from_sides([1.0, 1.0, 1.0], controlled_v),
            sample_from_sides([1.0, 1.04, 0.97], controlled_v),
            sample_from_sides([1.0, 0.96, 1.03], controlled_v),
            sample_from_sides([1.02, 0.99, 1.0], controlled_v),
        ],
    }


def center_cartesian_state(
    positions: np.ndarray, velocities: np.ndarray, masses: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    total_mass = float(np.sum(masses))
    center = np.sum(masses[:, None] * positions, axis=0) / total_mass
    center_velocity = np.sum(masses[:, None] * velocities, axis=0) / total_mass
    return positions - center, velocities - center_velocity


def pairwise_distances(positions: np.ndarray) -> np.ndarray:
    return np.array(
        [
            np.linalg.norm(positions[0] - positions[1]),
            np.linalg.norm(positions[1] - positions[2]),
            np.linalg.norm(positions[2] - positions[0]),
        ],
        dtype=float,
    )


def sigma_from_positions(positions: np.ndarray) -> np.ndarray:
    sides = np.maximum(pairwise_distances(positions), 1.0e-300)
    return sigma_from_sides(sides)


def cartesian_fd_step(positions: np.ndarray, args: argparse.Namespace) -> float:
    scale = max(float(np.max(pairwise_distances(positions))), 1.0)
    return max(args.cartesian_fd_abs, args.cartesian_fd_rel * scale)


def sigma_position_jacobian(positions: np.ndarray, args: argparse.Namespace) -> np.ndarray:
    flat = positions.reshape(-1)
    step = cartesian_fd_step(positions, args)

    def fn(x: np.ndarray) -> np.ndarray:
        return sigma_from_positions(x.reshape(3, 3))

    return numerical_jacobian(fn, flat, step)


def cartesian_newtonian_acceleration(
    positions: np.ndarray, masses: np.ndarray, g_const: float
) -> np.ndarray:
    acceleration = np.zeros_like(positions, dtype=float)
    for i in range(3):
        for j in range(i + 1, 3):
            delta = positions[j] - positions[i]
            r2 = float(delta @ delta)
            inv_r3 = 1.0 / max(r2, 1.0e-300) ** 1.5
            acceleration[i] += g_const * masses[j] * delta * inv_r3
            acceleration[j] -= g_const * masses[i] * delta * inv_r3
    return acceleration


def mass_metric_inner(masses: np.ndarray, x: np.ndarray, y: np.ndarray) -> float:
    return float(np.sum(masses[:, None] * x * y))


def mass_metric_norm(masses: np.ndarray, x: np.ndarray) -> float:
    return math.sqrt(max(mass_metric_inner(masses, x, x), 0.0))


def rms_state_norm(x: np.ndarray) -> float:
    return math.sqrt(max(float(np.mean(np.sum(x * x, axis=1))), 0.0))


def normalized_mass_participation(masses: np.ndarray) -> float:
    total = float(np.sum(masses))
    if total <= 0.0:
        return 0.0
    return float(27.0 * np.prod(masses) / total**3)


def normalized_heron_participation_from_sides(sides: np.ndarray) -> float:
    a, b, c = sides
    area16 = 2 * a * a * b * b + 2 * b * b * c * c + 2 * c * c * a * a - a**4 - b**4 - c**4
    return float(27.0 * max(area16, 0.0) / max((a + b + c) ** 4, 1.0e-300))


def e5_participation_factor_from_sides(
    sides: np.ndarray, masses: np.ndarray, args: argparse.Namespace
) -> float:
    mode = args.participation_lift
    mass_factor = normalized_mass_participation(masses)
    shape_factor = normalized_heron_participation_from_sides(sides) ** args.shape_participation_power
    if mode == "none":
        return 1.0
    if mode == "mass":
        return mass_factor
    if mode == "shape":
        return shape_factor
    if mode == "mass_shape":
        return mass_factor * shape_factor
    raise ValueError(f"unknown participation lift: {mode}")


def e5_participation_factor_from_sigma(
    sigma: np.ndarray, masses: np.ndarray, args: argparse.Namespace
) -> float:
    return e5_participation_factor_from_sides(sides_from_sigma(sigma), masses, args)


def e5_participation_factor_from_positions(
    positions: np.ndarray, masses: np.ndarray, args: argparse.Namespace
) -> float:
    return e5_participation_factor_from_sides(pairwise_distances(positions), masses, args)


def dynamic_shape_rate_center(args: argparse.Namespace) -> float:
    center = args.dynamic_shape_rate_center
    if center > 0.0:
        return center
    return max(float(np.linalg.norm(np.array(args.controlled_shape_velocity, dtype=float))), 1.0e-300)


def e5_dynamic_suppression_factor(sigmadot: np.ndarray, args: argparse.Namespace) -> float:
    mode = args.dynamic_suppression
    if mode == "none":
        return 1.0
    rate = float(np.linalg.norm(sigmadot))
    center = dynamic_shape_rate_center(args)
    x = rate / center
    if mode == "shape_bandpass":
        # Symmetric finite-row response window: adiabatic shape drift and
        # rapidly averaged Keplerian shape phase both decouple.
        return float(4.0 * x * x / max((1.0 + x * x) ** 2, 1.0e-300))
    if mode == "shape_lowpass":
        return float(1.0 / (1.0 + x * x))
    raise ValueError(f"unknown dynamic suppression mode: {mode}")


def lift_shape_acceleration(
    positions: np.ndarray,
    masses: np.ndarray,
    sigma_acceleration: np.ndarray,
    args: argparse.Namespace,
) -> np.ndarray:
    jac = sigma_position_jacobian(positions, args)
    mass_inv = np.repeat(1.0 / masses, 3)
    weighted_jac_t = mass_inv[:, None] * jac.T
    normal = jac @ weighted_jac_t
    coeffs, *_ = np.linalg.lstsq(normal, sigma_acceleration, rcond=args.lstsq_rcond)
    return (weighted_jac_t @ coeffs).reshape(3, 3)


def e5_cartesian_acceleration_unscaled(
    positions: np.ndarray,
    velocities: np.ndarray,
    masses: np.ndarray,
    args: argparse.Namespace,
) -> np.ndarray:
    sigma = sigma_from_positions(positions)
    jac = sigma_position_jacobian(positions, args)
    sigmadot = jac @ velocities.reshape(-1)
    sigma_acceleration = ternary_acceleration(sigma, sigmadot, args)
    participation = e5_participation_factor_from_positions(positions, masses, args)
    dynamic = e5_dynamic_suppression_factor(sigmadot, args)
    return participation * dynamic * lift_shape_acceleration(positions, masses, sigma_acceleration, args)


def cartesian_correction_ratio(
    positions: np.ndarray,
    velocities: np.ndarray,
    masses: np.ndarray,
    g_const: float,
    args: argparse.Namespace,
    lambda_e5: float = 1.0,
) -> dict[str, Any]:
    newton = cartesian_newtonian_acceleration(positions, masses, g_const)
    e5 = lambda_e5 * e5_cartesian_acceleration_unscaled(positions, velocities, masses, args)
    norm_newton = mass_metric_norm(masses, newton)
    norm_e5 = mass_metric_norm(masses, e5)
    signed_projection = mass_metric_inner(masses, e5, newton)
    return {
        "newtonian_mass_metric_norm": norm_newton,
        "e5_mass_metric_norm": norm_e5,
        "relative_correction_norm": norm_e5 / max(norm_newton, 1.0e-300),
        "relative_signed_projection": signed_projection / max(norm_newton * norm_newton, 1.0e-300),
    }


def cartesian_rhs(
    state: np.ndarray,
    masses: np.ndarray,
    g_const: float,
    lambda_e5: float,
    args: argparse.Namespace,
    include_e5: bool,
) -> np.ndarray:
    positions = state[:9].reshape(3, 3)
    velocities = state[9:].reshape(3, 3)
    acceleration = cartesian_newtonian_acceleration(positions, masses, g_const)
    if include_e5:
        acceleration = acceleration + lambda_e5 * e5_cartesian_acceleration_unscaled(
            positions, velocities, masses, args
        )
    return np.concatenate([velocities.reshape(-1), acceleration.reshape(-1)])


def rk4_cartesian_step(
    state: np.ndarray,
    dt: float,
    masses: np.ndarray,
    g_const: float,
    lambda_e5: float,
    args: argparse.Namespace,
    include_e5: bool,
) -> np.ndarray:
    k1 = cartesian_rhs(state, masses, g_const, lambda_e5, args, include_e5)
    k2 = cartesian_rhs(state + 0.5 * dt * k1, masses, g_const, lambda_e5, args, include_e5)
    k3 = cartesian_rhs(state + 0.5 * dt * k2, masses, g_const, lambda_e5, args, include_e5)
    k4 = cartesian_rhs(state + dt * k3, masses, g_const, lambda_e5, args, include_e5)
    return state + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)


def state_scales(positions: np.ndarray, velocities: np.ndarray) -> tuple[float, float]:
    pos_scale = max(rms_state_norm(positions), float(np.max(pairwise_distances(positions))), 1.0e-300)
    vel_scale = max(rms_state_norm(velocities), 1.0e-300)
    return pos_scale, vel_scale


def run_ephemeris_case(
    case: EphemerisCase, lambda_e5: float, args: argparse.Namespace
) -> dict[str, Any]:
    steps = max(1, int(case.orbits * args.ephemeris_steps_per_orbit))
    duration = case.orbits * case.period
    dt = duration / steps
    initial = np.concatenate([case.positions.reshape(-1), case.velocities.reshape(-1)])
    reference = initial.copy()
    candidate = initial.copy()
    pos_scale, vel_scale = state_scales(case.positions, case.velocities)
    max_pos_rel = 0.0
    max_vel_rel = 0.0
    sampled_ratios = []

    for step in range(steps + 1):
        if step % args.ephemeris_ratio_stride == 0 or step == steps:
            pos = candidate[:9].reshape(3, 3)
            vel = candidate[9:].reshape(3, 3)
            sampled_ratios.append(
                cartesian_correction_ratio(pos, vel, case.masses, case.g_const, args, lambda_e5)
            )
        ref_pos = reference[:9].reshape(3, 3)
        ref_vel = reference[9:].reshape(3, 3)
        cand_pos = candidate[:9].reshape(3, 3)
        cand_vel = candidate[9:].reshape(3, 3)
        max_pos_rel = max(max_pos_rel, rms_state_norm(cand_pos - ref_pos) / pos_scale)
        max_vel_rel = max(max_vel_rel, rms_state_norm(cand_vel - ref_vel) / vel_scale)
        if step == steps:
            break
        reference = rk4_cartesian_step(reference, dt, case.masses, case.g_const, 0.0, args, False)
        candidate = rk4_cartesian_step(
            candidate, dt, case.masses, case.g_const, lambda_e5, args, True
        )

    ref_pos = reference[:9].reshape(3, 3)
    ref_vel = reference[9:].reshape(3, 3)
    cand_pos = candidate[:9].reshape(3, 3)
    cand_vel = candidate[9:].reshape(3, 3)
    final_pos_rel = rms_state_norm(cand_pos - ref_pos) / pos_scale
    final_vel_rel = rms_state_norm(cand_vel - ref_vel) / vel_scale
    max_ratio = max(s["relative_correction_norm"] for s in sampled_ratios)
    signed = [s["relative_signed_projection"] for s in sampled_ratios]
    return {
        "name": case.name,
        "family": case.family,
        "period": case.period,
        "orbits": case.orbits,
        "duration": duration,
        "steps": steps,
        "dt": dt,
        "weak_field_calibrator": case.weak_field_calibrator,
        "near_equilateral_sign": case.near_equilateral_sign,
        "initial_sides": pairwise_distances(case.positions).tolist(),
        "position_scale": pos_scale,
        "velocity_scale": vel_scale,
        "final_relative_position_deviation": final_pos_rel,
        "final_relative_velocity_deviation": final_vel_rel,
        "max_relative_position_deviation": max_pos_rel,
        "max_relative_velocity_deviation": max_vel_rel,
        "sampled_relative_correction_norms": [
            s["relative_correction_norm"] for s in sampled_ratios
        ],
        "max_sampled_relative_correction_norm": max_ratio,
        "sampled_relative_signed_projections": signed,
    }


def circular_velocity(g_const: float, central_mass: float, radius: float) -> float:
    return math.sqrt(g_const * central_mass / radius)


def earth_moon_sun_case(args: argparse.Namespace) -> EphemerisCase:
    masses = np.array([1.0, 3.003489614915e-6, 3.694303349e-8], dtype=float)
    moon_distance = 384_400.0 / AU_KM
    moon_angle = math.radians(args.moon_phase_degrees)
    positions = np.array(
        [
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [
                1.0 + moon_distance * math.cos(moon_angle),
                moon_distance * math.sin(moon_angle),
                0.0,
            ],
        ],
        dtype=float,
    )
    earth_speed = 2.0 * math.pi
    moon_period = 27.321661 / DAY_PER_YEAR
    moon_speed = 2.0 * math.pi * moon_distance / moon_period
    moon_tangent = np.array([-math.sin(moon_angle), math.cos(moon_angle), 0.0])
    velocities = np.array(
        [
            [0.0, 0.0, 0.0],
            [0.0, earth_speed, 0.0],
            np.array([0.0, earth_speed, 0.0]) + moon_speed * moon_tangent,
        ],
        dtype=float,
    )
    positions, velocities = center_cartesian_state(positions, velocities, masses)
    return EphemerisCase(
        name="earth_moon_sun_quadrature",
        family="known_perturbed_three_body",
        masses=masses,
        positions=positions,
        velocities=velocities,
        g_const=SOLAR_G_AU_YEAR,
        period=moon_period,
        orbits=args.ephemeris_orbits,
        weak_field_calibrator=True,
        near_equilateral_sign=False,
    )


def jupiter_io_europa_case(args: argparse.Namespace) -> EphemerisCase:
    masses = np.array([9.547919384243266e-4, 4.491552e-8, 2.413468e-8], dtype=float)
    io_radius = 421_700.0 / AU_KM
    europa_radius = 671_034.0 / AU_KM
    europa_angle = math.radians(110.0)
    positions = np.array(
        [
            [0.0, 0.0, 0.0],
            [io_radius, 0.0, 0.0],
            [europa_radius * math.cos(europa_angle), europa_radius * math.sin(europa_angle), 0.0],
        ],
        dtype=float,
    )
    io_speed = circular_velocity(SOLAR_G_AU_YEAR, masses[0], io_radius)
    europa_speed = circular_velocity(SOLAR_G_AU_YEAR, masses[0], europa_radius)
    velocities = np.array(
        [
            [0.0, 0.0, 0.0],
            [0.0, io_speed, 0.0],
            [-europa_speed * math.sin(europa_angle), europa_speed * math.cos(europa_angle), 0.0],
        ],
        dtype=float,
    )
    positions, velocities = center_cartesian_state(positions, velocities, masses)
    return EphemerisCase(
        name="jupiter_io_europa",
        family="known_perturbed_three_body",
        masses=masses,
        positions=positions,
        velocities=velocities,
        g_const=SOLAR_G_AU_YEAR,
        period=1.769137786 / DAY_PER_YEAR,
        orbits=args.ephemeris_orbits,
        weak_field_calibrator=True,
        near_equilateral_sign=False,
    )


def equilateral_state_from_sides(
    sides: list[float], args: argparse.Namespace
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, float]:
    masses = np.ones(3, dtype=float)
    sides_array = np.array(sides, dtype=float)
    positions = triangle_positions_from_sides(sides_array, masses)
    side_scale = float(np.mean(sides_array))
    omega = math.sqrt(3.0 * args.g_const / max(side_scale**3, 1.0e-300))
    velocities = omega * np.stack([-positions[:, 1], positions[:, 0], positions[:, 2]], axis=1)
    positions, velocities = center_cartesian_state(positions, velocities, masses)
    period = 2.0 * math.pi / omega
    return masses, positions, velocities, args.g_const, period


def synthetic_equilateral_case(args: argparse.Namespace) -> EphemerisCase:
    masses, positions, velocities, g_const, period = equilateral_state_from_sides(
        [1.0, 1.0, 1.0], args
    )
    return EphemerisCase(
        name="synthetic_lagrange_equilateral",
        family="synthetic_near_equilateral",
        masses=masses,
        positions=positions,
        velocities=velocities,
        g_const=g_const,
        period=period,
        orbits=args.ephemeris_orbits,
        weak_field_calibrator=False,
        near_equilateral_sign=True,
    )


def build_ephemeris_cases(args: argparse.Namespace) -> list[EphemerisCase]:
    cases = [earth_moon_sun_case(args), jupiter_io_europa_case(args)]
    if args.include_synthetic_equilateral:
        cases.append(synthetic_equilateral_case(args))
    return cases


def near_equilateral_sign_scan(lambda_e5: float, args: argparse.Namespace) -> list[dict[str, Any]]:
    side_sets = [
        [1.0, 1.0, 1.0],
        [1.0, 1.04, 0.97],
        [1.0, 0.96, 1.03],
        [1.02, 0.99, 1.0],
    ]
    declared_shape_velocity = np.array(args.controlled_shape_velocity, dtype=float)
    out = []
    for sides in side_sets:
        masses, positions, _, g_const, _ = equilateral_state_from_sides(sides, args)
        velocities = lift_shape_acceleration(positions, masses, declared_shape_velocity, args)
        ratio = cartesian_correction_ratio(positions, velocities, masses, g_const, args, lambda_e5)
        out.append(
            {
                "sides": sides,
                "declared_shape_velocity": declared_shape_velocity.tolist(),
                "relative_correction_norm": ratio["relative_correction_norm"],
                "relative_signed_projection": ratio["relative_signed_projection"],
            }
        )
    return out


def unscaled_ratio(
    sigma: np.ndarray,
    sigmadot: np.ndarray,
    masses: np.ndarray,
    args: argparse.Namespace,
) -> float:
    metric = shape_metric(sigma, masses, args.fd_step)
    a_newton = newtonian_acceleration(
        sigma,
        sigmadot,
        masses,
        args.g_const,
        args.fd_step,
        args.variation_step,
        args.lstsq_rcond,
    )
    a_t = ternary_acceleration(sigma, sigmadot, args)
    a_t = (
        e5_participation_factor_from_sigma(sigma, masses, args)
        * e5_dynamic_suppression_factor(sigmadot, args)
        * a_t
    )
    return metric_norm(metric, a_t) / max(metric_norm(metric, a_newton), 1.0e-300)


def audit(args: argparse.Namespace) -> dict[str, Any]:
    samples = build_samples(args)
    ephemeris_cases = build_ephemeris_cases(args)
    solar_masses = np.array(args.solar_masses, dtype=float)
    controlled_masses = np.array(args.controlled_masses, dtype=float)

    weak_unscaled = [
        unscaled_ratio(sigma, sigmadot, solar_masses, args)
        for sigma, sigmadot in samples["weak_field"]
    ]
    max_weak_unscaled = max(weak_unscaled)
    ephemeris_weak_unscaled = [
        {
            "case": case.name,
            **cartesian_correction_ratio(
                case.positions, case.velocities, case.masses, case.g_const, args, 1.0
            ),
        }
        for case in ephemeris_cases
        if case.weak_field_calibrator
    ]
    max_ephemeris_weak_unscaled = (
        max(s["relative_correction_norm"] for s in ephemeris_weak_unscaled)
        if ephemeris_weak_unscaled
        else 0.0
    )
    if args.lambda_source == "ephemeris":
        lambda_e5 = args.weak_field_tol / max(max_ephemeris_weak_unscaled, 1.0e-300)
    else:
        lambda_e5 = args.weak_field_tol / max(max_weak_unscaled, 1.0e-300)

    weak_results = [
        evaluate_state(sigma, sigmadot, solar_masses, lambda_e5, args)
        for sigma, sigmadot in samples["weak_field"]
    ]
    boundary_results = [
        evaluate_state(sigma, sigmadot, controlled_masses, lambda_e5, args)
        for sigma, sigmadot in samples["dyadic_boundary"]
    ]
    controlled_results = [
        evaluate_state(sigma, sigmadot, controlled_masses, lambda_e5, args)
        for sigma, sigmadot in samples["controlled"]
    ]

    weak_max = max(s["relative_correction_norm"] for s in weak_results)
    boundary_max = max(s["relative_correction_norm"] for s in boundary_results)
    controlled_signed = [s["relative_signed_projection"] for s in controlled_results]
    controlled_abs = [abs(x) for x in controlled_signed]
    signs = [1 if x > args.sign_zero_tol else -1 if x < -args.sign_zero_tol else 0 for x in controlled_signed]
    nonzero_signs = [s for s in signs if s != 0]
    sign_definite = bool(nonzero_signs) and all(s == nonzero_signs[0] for s in nonzero_signs) and len(nonzero_signs) == len(signs)
    controlled_max_signal = max(controlled_abs)
    controlled_min_signal = min(controlled_abs)
    ephemeris_results = [
        run_ephemeris_case(case, lambda_e5, args)
        for case in ephemeris_cases
        if not args.skip_ephemeris
    ]
    ephemeris_weak_results = [s for s in ephemeris_results if s["weak_field_calibrator"]]
    ephemeris_position_max = (
        max(s["final_relative_position_deviation"] for s in ephemeris_results)
        if ephemeris_results
        else 0.0
    )
    ephemeris_velocity_max = (
        max(s["final_relative_velocity_deviation"] for s in ephemeris_results)
        if ephemeris_results
        else 0.0
    )
    ephemeris_weak_max = (
        max(s["max_sampled_relative_correction_norm"] for s in ephemeris_weak_results)
        if ephemeris_weak_results
        else 0.0
    )
    ephemeris_sign_samples = near_equilateral_sign_scan(lambda_e5, args)
    ephemeris_sign_values = [s["relative_signed_projection"] for s in ephemeris_sign_samples]
    ephemeris_signs = [
        1 if x > args.sign_zero_tol else -1 if x < -args.sign_zero_tol else 0
        for x in ephemeris_sign_values
    ]
    ephemeris_nonzero_signs = [s for s in ephemeris_signs if s != 0]
    ephemeris_sign_definite = (
        bool(ephemeris_nonzero_signs)
        and all(s == ephemeris_nonzero_signs[0] for s in ephemeris_nonzero_signs)
        and len(ephemeris_nonzero_signs) == len(ephemeris_signs)
    )
    ephemeris_min_abs_sign_signal = min(abs(x) for x in ephemeris_sign_values)
    ephemeris_max_abs_sign_signal = max(abs(x) for x in ephemeris_sign_values)

    kills = []
    if not np.isfinite(lambda_e5) or lambda_e5 < args.lambda_floor:
        kills.append("weak-field cap forces lambda_E5 below floor or non-finite")
    if weak_max > args.weak_field_tol * (1.0 + args.numeric_slack):
        kills.append("weak-field correction exceeds tolerance after lambda fixation")
    if boundary_max > args.boundary_tol:
        kills.append("dyadic-boundary correction does not recover Newtonian shadow within tolerance")
    if not sign_definite:
        kills.append("controlled-regime signed deviations are not sign-definite")
    if controlled_max_signal < args.controlled_signal_floor:
        kills.append("controlled-regime signal is below floor")
    if not args.skip_ephemeris and not ephemeris_results:
        kills.append("no ephemeris cases were evaluated")
    if ephemeris_weak_max > args.weak_field_tol * (1.0 + args.numeric_slack):
        kills.append("ephemeris weak-field acceleration correction exceeds 1e-10 cap")
    if ephemeris_position_max > args.ephemeris_position_tol:
        kills.append(
            "finite-row rigidity prevents ephemeris recovery: final position residual exceeds tolerance"
        )
    if ephemeris_velocity_max > args.ephemeris_velocity_tol:
        kills.append(
            "finite-row rigidity prevents ephemeris recovery: final velocity residual exceeds tolerance"
        )
    if not ephemeris_sign_definite:
        kills.append("near-equilateral Cartesian E5 signs are not sign-definite")
    if ephemeris_max_abs_sign_signal < args.ephemeris_sign_signal_floor:
        kills.append("near-equilateral Cartesian E5 signal is below floor")

    return {
        "claim_tested": "E5 parameter-fixed physical discriminator for the Z6 canonical bridge",
        "pre_registration": {
            "model": "a_candidate = a_Newton + lambda_E5 * (a_EL(eta_copula)-a_EL(eta_base))",
            "cartesian_lift": "mass-metric minimum-norm inverse of D sigma",
            "participation_lift": args.participation_lift,
            "shape_participation_power": args.shape_participation_power,
            "dynamic_suppression": args.dynamic_suppression,
            "dynamic_shape_rate_center": dynamic_shape_rate_center(args),
            "kappa": args.kappa,
            "phi_coeffs": args.phi_coeffs,
            "lambda_fixing": "lambda_E5 fixed once by weak-field tolerance, then held fixed",
            "lambda_source": args.lambda_source,
            "weak_field_tol": args.weak_field_tol,
            "boundary_tol": args.boundary_tol,
            "controlled_signal_floor": args.controlled_signal_floor,
            "sign_zero_tol": args.sign_zero_tol,
            "ephemeris_metric": "final RMS position/velocity deviation relative to initial RMS scale after N orbits",
            "ephemeris_position_tol": args.ephemeris_position_tol,
            "ephemeris_velocity_tol": args.ephemeris_velocity_tol,
            "ephemeris_orbits": args.ephemeris_orbits,
            "ephemeris_steps_per_orbit": args.ephemeris_steps_per_orbit,
        },
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "lambda_fixing": {
            "source": args.lambda_source,
            "weak_unscaled_ratios": weak_unscaled,
            "max_weak_unscaled_ratio": max_weak_unscaled,
            "ephemeris_weak_unscaled_ratios": ephemeris_weak_unscaled,
            "max_ephemeris_weak_unscaled_ratio": max_ephemeris_weak_unscaled,
            "lambda_E5": lambda_e5,
        },
        "weak_field": weak_results,
        "dyadic_boundary": boundary_results,
        "controlled": controlled_results,
        "ephemeris": ephemeris_results,
        "near_equilateral_cartesian_sign_scan": ephemeris_sign_samples,
        "summary": {
            "status": "PASS_EPHEMERIS_DISCRIMINATOR" if not kills else "KILL",
            "lambda_E5": lambda_e5,
            "lambda_source": args.lambda_source,
            "weak_field_max_relative_correction": weak_max,
            "dyadic_boundary_max_relative_correction": boundary_max,
            "controlled_relative_signed_projections": controlled_signed,
            "controlled_signs": signs,
            "controlled_sign_definite": sign_definite,
            "controlled_min_abs_signal": controlled_min_signal,
            "controlled_max_abs_signal": controlled_max_signal,
            "ephemeris_final_position_max": ephemeris_position_max,
            "ephemeris_final_velocity_max": ephemeris_velocity_max,
            "ephemeris_weak_field_max_sampled_correction": ephemeris_weak_max,
            "near_equilateral_cartesian_signed_projections": ephemeris_sign_values,
            "near_equilateral_cartesian_signs": ephemeris_signs,
            "near_equilateral_cartesian_sign_definite": ephemeris_sign_definite,
            "near_equilateral_cartesian_min_abs_signal": ephemeris_min_abs_sign_signal,
            "near_equilateral_cartesian_max_abs_signal": ephemeris_max_abs_sign_signal,
            "kills": kills,
        },
    }


def write_report(result: dict[str, Any], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    p = result["pre_registration"]
    lines = [
        "# Z6 E5 Physical Discriminator",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        "",
        "## Pre-Registration",
        "",
        f"- Model: {p['model']}",
        f"- Cartesian lift: {p['cartesian_lift']}",
        f"- participation lift: {p['participation_lift']}",
        f"- shape participation power: {p['shape_participation_power']}",
        f"- dynamic suppression: {p['dynamic_suppression']}",
        f"- dynamic shape-rate center: {p['dynamic_shape_rate_center']:.6e}",
        f"- kappa: {p['kappa']}",
        f"- phi coefficients: {p['phi_coeffs']}",
        f"- lambda fixing: {p['lambda_fixing']}",
        f"- lambda source: {p['lambda_source']}",
        f"- weak-field tolerance: {p['weak_field_tol']:.6e}",
        f"- dyadic-boundary tolerance: {p['boundary_tol']:.6e}",
        f"- controlled signal floor: {p['controlled_signal_floor']:.6e}",
        f"- ephemeris metric: {p['ephemeris_metric']}",
        f"- ephemeris position tolerance: {p['ephemeris_position_tol']:.6e}",
        f"- ephemeris velocity tolerance: {p['ephemeris_velocity_tol']:.6e}",
        f"- ephemeris N orbits: {p['ephemeris_orbits']}",
        f"- ephemeris steps per orbit: {p['ephemeris_steps_per_orbit']}",
        "",
        "## Summary",
        "",
        f"- lambda_E5: {s['lambda_E5']:.12e}",
        f"- lambda source: {s['lambda_source']}",
        f"- weak-field max relative correction: {s['weak_field_max_relative_correction']:.6e}",
        f"- dyadic-boundary max relative correction: {s['dyadic_boundary_max_relative_correction']:.6e}",
        f"- controlled relative signed projections: {[f'{x:.6e}' for x in s['controlled_relative_signed_projections']]}",
        f"- controlled signs: {s['controlled_signs']}",
        f"- controlled sign-definite: {s['controlled_sign_definite']}",
        f"- controlled min abs signal: {s['controlled_min_abs_signal']:.6e}",
        f"- controlled max abs signal: {s['controlled_max_abs_signal']:.6e}",
        f"- ephemeris final position max: {s['ephemeris_final_position_max']:.6e}",
        f"- ephemeris final velocity max: {s['ephemeris_final_velocity_max']:.6e}",
        f"- ephemeris weak-field max sampled correction: {s['ephemeris_weak_field_max_sampled_correction']:.6e}",
        f"- near-equilateral Cartesian signed projections: {[f'{x:.6e}' for x in s['near_equilateral_cartesian_signed_projections']]}",
        f"- near-equilateral Cartesian signs: {s['near_equilateral_cartesian_signs']}",
        f"- near-equilateral Cartesian sign-definite: {s['near_equilateral_cartesian_sign_definite']}",
        f"- near-equilateral Cartesian min abs signal: {s['near_equilateral_cartesian_min_abs_signal']:.6e}",
        f"- near-equilateral Cartesian max abs signal: {s['near_equilateral_cartesian_max_abs_signal']:.6e}",
        f"- kills: {s['kills']}",
        "",
        "## Samples",
        "",
        "### Weak Field",
        "",
        "| idx | sides | relative correction | signed projection |",
        "|---:|---|---:|---:|",
    ]
    for idx, sample in enumerate(result["weak_field"]):
        lines.append(
            f"| {idx} | {sample['sides']} | {sample['relative_correction_norm']:.6e} | "
            f"{sample['relative_signed_projection']:.6e} |"
        )
    lines.extend(["", "### Dyadic Boundary", "", "| idx | sides | relative correction | signed projection |", "|---:|---|---:|---:|"])
    for idx, sample in enumerate(result["dyadic_boundary"]):
        lines.append(
            f"| {idx} | {sample['sides']} | {sample['relative_correction_norm']:.6e} | "
            f"{sample['relative_signed_projection']:.6e} |"
        )
    lines.extend(["", "### Controlled Near-Equilateral", "", "| idx | sides | relative correction | signed projection |", "|---:|---|---:|---:|"])
    for idx, sample in enumerate(result["controlled"]):
        lines.append(
            f"| {idx} | {sample['sides']} | {sample['relative_correction_norm']:.6e} | "
            f"{sample['relative_signed_projection']:.6e} |"
        )
    lines.extend(
        [
            "",
            "### Ephemeris Propagation",
            "",
            "| case | family | orbits | steps | final pos rel | final vel rel | max weak correction |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for sample in result["ephemeris"]:
        lines.append(
            "| {name} | {family} | {orbits} | {steps} | {final_relative_position_deviation:.6e} | "
            "{final_relative_velocity_deviation:.6e} | {max_sampled_relative_correction_norm:.6e} |".format(
                **sample
            )
        )
    lines.extend(
        [
            "",
            "### Near-Equilateral Cartesian Sign Scan",
            "",
            "| idx | sides | relative correction | signed projection |",
            "|---:|---|---:|---:|",
        ]
    )
    for idx, sample in enumerate(result["near_equilateral_cartesian_sign_scan"]):
        lines.append(
            f"| {idx} | {sample['sides']} | {sample['relative_correction_norm']:.6e} | "
            f"{sample['relative_signed_projection']:.6e} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "A PASS means this finite bridge survives the fixed-parameter",
            "reduced-shape and Cartesian ephemeris discriminator. A KILL means",
            "the bridge remains a mathematical projection-closure prototype,",
            "not a parameter-fixed physical candidate.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kappa", type=float, default=0.8)
    parser.add_argument("--phi-coeffs", nargs=2, type=float, default=[1.0, 0.0])
    parser.add_argument("--solar-masses", nargs=3, type=float, default=[1.0, 3.0e-6, 9.5e-4])
    parser.add_argument("--controlled-masses", nargs=3, type=float, default=[1.0, 1.0, 1.0])
    parser.add_argument("--g-const", type=float, default=1.0)
    parser.add_argument("--weak-field-tol", type=float, default=1.0e-10)
    parser.add_argument("--boundary-tol", type=float, default=1.0e-8)
    parser.add_argument("--controlled-signal-floor", type=float, default=1.0e-12)
    parser.add_argument("--ephemeris-position-tol", type=float, default=1.0e-10)
    parser.add_argument("--ephemeris-velocity-tol", type=float, default=1.0e-10)
    parser.add_argument("--ephemeris-sign-signal-floor", type=float, default=1.0e-12)
    parser.add_argument("--ephemeris-orbits", type=int, default=2)
    parser.add_argument("--ephemeris-steps-per-orbit", type=int, default=10)
    parser.add_argument("--ephemeris-ratio-stride", type=int, default=5)
    parser.add_argument("--lambda-source", choices=["reduced", "ephemeris"], default="ephemeris")
    parser.add_argument(
        "--participation-lift",
        choices=["none", "mass", "shape", "mass_shape"],
        default="none",
    )
    parser.add_argument("--shape-participation-power", type=float, default=1.0)
    parser.add_argument(
        "--dynamic-suppression",
        choices=["none", "shape_bandpass", "shape_lowpass"],
        default="none",
    )
    parser.add_argument("--dynamic-shape-rate-center", type=float, default=0.0)
    parser.add_argument("--controlled-shape-velocity", nargs=3, type=float, default=[0.04, -0.02, 0.015])
    parser.add_argument("--cartesian-fd-rel", type=float, default=1.0e-6)
    parser.add_argument("--cartesian-fd-abs", type=float, default=1.0e-9)
    parser.add_argument("--moon-phase-degrees", type=float, default=90.0)
    parser.add_argument("--skip-ephemeris", action="store_true")
    parser.add_argument("--include-synthetic-equilateral", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--lambda-floor", type=float, default=1.0e-14)
    parser.add_argument("--sign-zero-tol", type=float, default=1.0e-14)
    parser.add_argument("--numeric-slack", type=float, default=1.0e-6)
    parser.add_argument("--boundary-radius", type=float, default=100.0)
    parser.add_argument("--fd-step", type=float, default=1.0e-6)
    parser.add_argument("--variation-step", type=float, default=2.0e-5)
    parser.add_argument("--lstsq-rcond", type=float, default=1.0e-10)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_e5_physical_discriminator.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_e5_physical_discriminator.json"),
    )
    args = parser.parse_args()
    result = audit(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
