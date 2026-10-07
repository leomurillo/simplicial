"""
Run the full apex zero-variety gate (C1-C8). Deterministic; numpy/mpmath only.
Exit 0 iff every certificate passes.
"""
import subprocess
import sys
import os

SCRIPTS = [
    ("C1", "c1_strip_and_zeros.py"),
    ("C2", "c2_counting_law.py"),
    ("C3", "c3_exact_line_locus.py"),
    ("C4", "c4_character_phase.py"),
    ("C5", "c5_mean_line_nogo.py"),
    ("C6", "c6_newton_polygon.py"),
    ("C7", "c7_functional_equation.py"),
    ("C8", "c8_arithmetic_bridge.py"),
    ("C9", "c9_function_field_weil.py"),
    ("C10", "c10_higher_genus.py"),
    ("C11", "c11_padic_newton.py"),
    ("C12", "c12_function_field_innovation.py"),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    results = []
    for tag, script in SCRIPTS:
        r = subprocess.run([sys.executable, "-u", os.path.join(here, script)],
                           cwd=here)
        results.append((tag, r.returncode == 0))
    print("\n" + "=" * 50)
    print("APEX ZERO-VARIETY GATE")
    for tag, ok in results:
        print(f"  {tag}: {'PASS' if ok else 'FAIL'}")
    allok = all(ok for _, ok in results)
    print("GATE:", "ALL PASS" if allok else "FAIL")
    print("=" * 50)
    return allok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
