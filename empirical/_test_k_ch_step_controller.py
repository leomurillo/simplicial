"""Smoke tests for k_ch_step_controller.py."""

from __future__ import annotations

import math

import numpy as np

from k_ch_step_controller import (
    StepControllerConfig,
    control_step,
    cyclic_packet_energy,
    fisher_inner,
    fisher_norm,
    k_ch_raise,
)


def assert_close(a: float, b: float, tol: float = 1e-9) -> None:
    if abs(a - b) > tol:
        raise AssertionError(f"{a} != {b} within {tol}")


def main() -> int:
    p = np.full(7, 1.0 / 7.0)
    step = np.array([0.24, -0.08, -0.04, -0.03, -0.03, -0.03, -0.03])
    step = step - np.mean(step)

    kss = k_ch_raise(p, step, step)
    assert_close(float(np.sum(kss)), 0.0)
    assert fisher_norm(p, kss) > 0.0

    # Raising identity: g(K(u)v,w) = T(u,v,w), checked directly on one witness.
    witness = np.array([0.05, -0.02, 0.01, 0.03, -0.04, -0.01, -0.02])
    witness = witness - np.mean(witness)
    lhs = fisher_inner(p, kss, witness)
    rhs = float(np.sum(step * step * witness / (p * p)))
    assert_close(lhs, rhs, 1e-10)

    cfg = StepControllerConfig(max_cubic_fraction=0.05, min_probability=1e-9)
    diag = control_step(p, step, config=cfg, name="synthetic", cyclic_packets=True)
    assert diag.controlled_cubic_fraction <= cfg.max_cubic_fraction + 1e-10
    assert diag.accepted_scale < 1.0
    assert diag.min_probability_after_step > 0.0
    assert "cubic_fraction" in diag.active_limits

    # The scale law should be linear for cubic_fraction under step scaling.
    diag_half = control_step(p, 0.5 * step, config=cfg, name="synthetic_half")
    assert_close(
        diag_half.original_cubic_fraction,
        0.5 * diag.original_cubic_fraction,
        1e-10,
    )

    # Positivity guard should activate before crossing the simplex boundary.
    boundary_step = np.array([-0.20, 0.20, 0, 0, 0, 0, 0], dtype=float)
    boundary_step = boundary_step - np.mean(boundary_step)
    boundary_diag = control_step(
        p,
        boundary_step,
        config=StepControllerConfig(max_cubic_fraction=10.0, min_probability=1e-4),
        name="boundary",
    )
    assert boundary_diag.accepted_scale < 1.0
    assert boundary_diag.min_probability_after_step >= 1e-4 - 1e-12
    assert "positivity" in boundary_diag.active_limits

    packets = cyclic_packet_energy(step)
    nontrivial_sum = sum(v for k, v in packets.items() if k != "trivial")
    assert_close(nontrivial_sum, 1.0)
    assert packets["trivial"] < 1e-20

    print("All k_ch_step_controller smoke tests passed.")
    print(f"synthetic raw cubic fraction: {diag.original_cubic_fraction:.6f}")
    print(f"synthetic accepted scale: {diag.accepted_scale:.6f}")
    print(f"boundary accepted scale: {boundary_diag.accepted_scale:.6f}")
    print(f"packet sum: {nontrivial_sum:.6f}")
    if not math.isfinite(diag.original_directional_rho):
        raise AssertionError("directional rho should be finite")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
