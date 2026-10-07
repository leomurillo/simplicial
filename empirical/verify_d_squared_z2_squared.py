"""Tiny explicit check on R = (Z/2)^2 of whether d^2 = 0 holds for the
Paper 11 Cor 9.5.11 chain complex with the literal sign convention.

R = (Z/2)^2 has 4 elements, 3 nonzero. dim H^(2) = 3, dim H^(3) = 6, dim H^(4) = 21.

We compute d_3 d_4(c) by hand for c = (1,2,1,2) and report all term cancellations.
"""

ORDER = 4
def add(x, y):
    return x ^ y


def differential_term(cell):
    """Return list of (sign, output_cell) pairs."""
    n = len(cell)
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            merged = add(cell[i], cell[j])
            if merged == 0:
                continue
            rest = tuple(cell[k] for k in range(n) if k != i and k != j)
            out_cell = rest + (merged,)
            sign = -1 if (i + j) % 2 else 1
            out.append((sign, out_cell, (i, j)))
    return out


def apply_d(coefs):
    """Apply d to a formal Z-linear combination given as dict cell -> coef."""
    result: dict = {}
    for cell, coef in coefs.items():
        for sign, out_cell, _ in differential_term(cell):
            result[out_cell] = result.get(out_cell, 0) + sign * coef
    # Drop zeros
    return {c: v for c, v in result.items() if v != 0}


def main():
    print("R = (Z/2)^2, cell c = (1,2,1,2) (sum 1+2+1+2 = 0 mod 2 in each bit)")
    print()

    c = (1, 2, 1, 2)
    print(f"d_4(c):")
    d4c: dict = {}
    for sign, out_cell, pair in differential_term(c):
        s = "+" if sign > 0 else "-"
        print(f"  d_{pair} = {s}{out_cell}")
        d4c[out_cell] = d4c.get(out_cell, 0) + sign
    d4c_clean = {k: v for k, v in d4c.items() if v != 0}
    print(f"  Total d_4(c) = {d4c_clean}")
    print()

    print(f"d_3 d_4(c):")
    dd = apply_d(d4c_clean)
    print(f"  d_3 d_4(c) = {dd}")
    print()

    if not dd:
        print("d^2 = 0 on this cell. (Test passes)")
    else:
        print("d^2 != 0 on this cell.")
        print(f"Concrete witness for failure of Paper 11 Cor 9.5.11 sign convention.")
        print()
        print("Over F_2 (mod 2):")
        dd_f2 = {k: v % 2 for k, v in dd.items() if v % 2 != 0}
        print(f"  d_3 d_4(c) mod 2 = {dd_f2}")
        if not dd_f2:
            print("  Vanishes mod 2.")
        else:
            print("  Does NOT vanish mod 2 either.")


if __name__ == "__main__":
    main()
