"""Smoke tests for tower_quotient_saturation.py."""

from __future__ import annotations

from tower_quotient_saturation import assess_saturation, exponent_label, suffix_leaf


def main() -> int:
    assert exponent_label(1) == "u"
    assert exponent_label(5) == "u^5"
    assert suffix_leaf(2) == "u+u^2"
    assert suffix_leaf(5) == "u^4+u^5"

    assessment = assess_saturation(
        [
            {
                "exponent": 2,
                "residual_is_exact": True,
                "nu_lambda_E_residual_mass": 0.25,
                "orbit_quotient_residual_mass": 0.5,
                "residual_deficit": 1.0,
                "h4_to_h3_orbit_cokernel_dimension": 0,
            },
            {
                "exponent": 3,
                "residual_is_exact": True,
                "nu_lambda_E_residual_mass": 0.125,
                "orbit_quotient_residual_mass": 0.25,
                "residual_deficit": 1.0,
                "h4_to_h3_orbit_cokernel_dimension": 0,
            },
        ]
    )
    assert assessment["c2_volume_residual_halves_on_exact_rows"]
    assert assessment["orbit_residual_mass_strictly_decreases_on_exact_rows"]
    assert assessment["relative_full_block_deficit_flat_one"]
    assert assessment["support_h4_to_h3_cokernel_zero_on_available_rows"]
    print("All tower_quotient_saturation smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
