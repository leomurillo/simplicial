"""Smoke tests for local_row_balanced_leakage.py."""

from __future__ import annotations

from local_row_balanced_leakage import summarize_leaf


def assert_close(a: float, b: float, tol: float = 1e-12) -> None:
    if abs(a - b) > tol:
        raise AssertionError(f"{a} != {b} within {tol}")


def main() -> int:
    rows = [
        {
            "representative": {"source": "u", "middle": "u", "target": "u"},
            "atom_count": 3,
            "path": "u->u->u",
        },
        {
            "representative": {"source": "u", "middle": "u", "target": "u^2"},
            "atom_count": 1,
            "path": "u->u->u^2",
        },
        {
            "representative": {"source": "u^2", "middle": "u", "target": "u^2"},
            "atom_count": 4,
            "path": "u^2->u->u^2",
        },
    ]

    thin = summarize_leaf(rows, 8, ("u",), residual_weight=0.5, min_active_mass_fraction=0.01)
    assert_close(thin["support_leakage_fraction"], 0.25)
    assert_close(thin["balanced_leakage"], 0.125)
    assert thin["active_orbits"] == 2
    assert thin["leaking_orbits"] == 1

    full = summarize_leaf(rows, 8, ("u", "u^2"), residual_weight=0.5, min_active_mass_fraction=0.01)
    assert_close(full["support_leakage_fraction"], 0.0)
    assert_close(full["balanced_leakage"], 0.0)
    assert full["active_atom_mass"] == 8

    print("All local_row_balanced_leakage smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
