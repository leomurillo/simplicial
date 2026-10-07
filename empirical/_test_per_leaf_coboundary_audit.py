"""Smoke tests for per_leaf_coboundary_audit.py."""

from __future__ import annotations

from per_leaf_coboundary_audit import (
    c2_volume_normalized_masses,
    normalized_residual_metrics,
    path_in_leaf,
    split_leaf,
)


def main() -> int:
    assert split_leaf("u^4+u^5") == ("u^4", "u^5")
    key = ("a", "b", "u^4", "u^5", "u^5", "out", "in")
    assert path_in_leaf(key, {"u^4", "u^5"})
    assert not path_in_leaf(key, {"u^5"})
    metrics = normalized_residual_metrics(
        {"raw_support": 10, "residual_support": 5},
        {"active_atom_mass": 20, "active_orbits": 2},
    )
    assert metrics["packet_mass_normalized_residual"] == 0.25
    assert metrics["orbit_count_normalized_residual"] == 2.5
    masses = c2_volume_normalized_masses(4, 2, 16)
    assert masses["nu_lambda_E_raw_mass"] == 0.25
    assert masses["nu_lambda_E_residual_mass"] == 0.125
    assert masses["nu_lambda_E_deficit"] == 0.5
    print("All per_leaf_coboundary_audit smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
