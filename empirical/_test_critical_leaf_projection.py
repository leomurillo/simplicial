"""Smoke tests for critical_leaf_projection.py."""

from __future__ import annotations

import numpy as np

from critical_leaf_projection import (
    closure_leakage_fraction,
    conductor_subsets,
    project_to_conductors,
)
from k_ch_step_controller import fisher_norm, k_ch_raise, project_tangent


def assert_close(a: float, b: float, tol: float = 1e-10) -> None:
    if abs(a - b) > tol:
        raise AssertionError(f"{a} != {b} within {tol}")


def main() -> int:
    assert conductor_subsets(7) == [(7,)]

    p7 = np.full(7, 1.0 / 7.0)
    v7 = project_tangent(np.array([0.30, -0.10, 0.04, -0.08, 0.02, -0.11, -0.07]))
    full7 = project_to_conductors(v7, (7,))
    assert_close(fisher_norm(p7, full7 - v7), 0.0)
    assert_close(closure_leakage_fraction(p7, k_ch_raise(p7, full7, full7), (7,)), 0.0)

    p12 = np.full(12, 1.0 / 12.0)
    v12 = project_tangent(np.array([0.21, -0.03, 0.05, -0.07, 0.02, -0.11, 0.09, -0.04, 0.08, -0.12, 0.01, -0.09]))
    c2 = project_to_conductors(v12, (2,))
    assert fisher_norm(p12, c2) > 0.0
    assert_close(fisher_norm(p12, k_ch_raise(p12, c2, c2)), 0.0)

    c3 = project_to_conductors(v12, (3,))
    assert fisher_norm(p12, k_ch_raise(p12, c3, c3)) > 0.0

    print("All critical_leaf_projection smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
