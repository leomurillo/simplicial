"""Smoke tests for cross_mode_critical_leaf_summary.py."""

from __future__ import annotations

from cross_mode_critical_leaf_summary import build_summary


def main() -> int:
    neural = {
        "runs": [
            {
                "preset": "months",
                "model_tag": "toy",
                "best_proper_nonflat_by_rho_frac": "conductor_3",
                "best_nonflat_by_rho_frac": "conductor_3",
                "best_regular_by_rho_frac": "conductor_2",
                "leaves": [
                    {
                        "leaf": "conductor_3",
                        "mean_balanced_leakage": 0.0,
                        "mean_kch_closure_leakage_fraction": 0.0,
                    }
                ],
            }
        ]
    }
    local = {
        "rows": [
            {
                "ring": "F_4[u]/(u^2)",
                "best_proper_regular_leaf": "u^2",
                "best_regular_leaf": "u^2",
                "leaves": [
                    {
                        "leaf": "u^2",
                        "balanced_leakage": 0.0,
                        "support_leakage_fraction": 0.0,
                    }
                ],
            }
        ]
    }
    per_leaf = {
        "rows": [
            {
                "ring": "F_4[u]/(u^2)",
                "leaf": "u^2",
                "skipped": False,
                "raw_is_coboundary": False,
                "residual_deficit": 1.0,
                "packet_mass_normalized_residual": 1.0,
                "orbit_count_normalized_residual": 82.2857142857,
                "nu_lambda_E_residual_mass": 0.015625,
                "nu_lambda_E_deficit": 1.0,
            }
        ]
    }
    rows = build_summary(neural, local, per_leaf)
    assert rows[0]["selected_leaf"] == "conductor_3"
    assert rows[1]["full_block_status"] == "residual"
    assert rows[1]["full_block_packet_mass_normalized_residual"] == 1.0
    assert rows[1]["nu_lambda_E_deficit"] == 1.0
    print("All cross_mode_critical_leaf_summary smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
