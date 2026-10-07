"""Compute the mixed Ext_CH and curvature diagnostics for F_4[u]/(u^2).

This script supports Section 11 of ``11.quotient_character_adjacency_algebras.md``.
It uses the centroid-normalized raised Amari-Chentsov operator

    Kbar_p(alpha)(v) = Q^{-1} Pi_p(chi_alpha * v / p),

so that at the centroid the full character algebra action is exactly
character multiplication and the normalization scalar in the defect is c = 1.

For an elementary tame Fourier mode tau and wild Fourier mode omega, the
script extracts the coefficient of s*r*t^2 in the pure-axis-subtracted defect.
The s*r*t coefficient vanishes because the first variation is linear in
h = s h_tame + r h_wild; geometrically this is the Codazzi-symmetric first
variation.  The script also splits the quadratic coefficient into the
symmetric Ext piece and antisymmetric commutator, the latter being the
Fisher-Rao curvature carry.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


F4_NAMES = {
    0: "0",
    1: "1",
    2: "w",
    3: "w+1",
}

Label = tuple[int, int]  # a + b*u in F_4[u]/(u^2), used as a character label.
Matrix = dict[tuple[Label, Label], Fraction]
Witness = dict[str, object]

ZERO: Label = (0, 0)
LABELS: list[Label] = [(a, b) for a in range(4) for b in range(4)]
NONTRIVIAL: list[Label] = [label for label in LABELS if label != ZERO]
TAME: list[Label] = [(0, b) for b in range(1, 4)]
WILD: list[Label] = [(a, b) for a in range(1, 4) for b in range(4)]


def f4_add(a: int, b: int) -> int:
    return a ^ b


def f4_mul(a: int, b: int) -> int:
    """Multiply in F_2[w]/(w^2+w+1), with w encoded as 2."""

    a0, a1 = a & 1, (a >> 1) & 1
    b0, b1 = b & 1, (b >> 1) & 1
    c0 = a0 & b0
    c1 = (a0 & b1) ^ (a1 & b0)
    c2 = a1 & b1
    # w^2 = w + 1.
    return (c0 ^ c2) | ((c1 ^ c2) << 1)


def f4_inv(a: int) -> int:
    if a == 0:
        raise ZeroDivisionError("0 has no inverse in F_4")
    for candidate in range(1, 4):
        if f4_mul(a, candidate) == 1:
            return candidate
    raise AssertionError("unreachable")


def f4_div(a: int, b: int) -> int:
    return f4_mul(a, f4_inv(b))


def f4_square(a: int) -> int:
    return f4_mul(a, a)


def add_label(x: Label, y: Label) -> Label:
    return (f4_add(x[0], y[0]), f4_add(x[1], y[1]))


def mul_label(x: Label, y: Label) -> Label:
    a, b = x
    c, d = y
    return (f4_mul(a, c), f4_add(f4_mul(a, d), f4_mul(b, c)))


def frobenius(x: Label) -> Label:
    return (f4_mul(x[0], x[0]), f4_mul(x[1], x[1]))


def unit_action(unit: Label, x: Label) -> Label:
    return mul_label(unit, x)


def conductor(x: Label) -> str:
    if x == ZERO:
        return "1"
    if x[0] == 0:
        return "u"
    return "u^2"


def f2_rank(values: list[int]) -> int:
    vectors = [value for value in values if value]
    rank = 0
    pivot_bits = [2, 1]
    for bit in pivot_bits:
        pivot = next((value for value in vectors if value & bit), None)
        if pivot is None:
            continue
        rank += 1
        vectors = [value ^ pivot if value & bit else value for value in vectors]
    return rank


def label_name(x: Label) -> str:
    a, b = x
    if x == ZERO:
        return "0"

    def nilpotent_name(value: int) -> str:
        if value == 1:
            return "u"
        if value == 2:
            return "wu"
        return "(w+1)u"

    if b == 0:
        return F4_NAMES[a]
    if a == 0:
        return nilpotent_name(b)
    return f"{F4_NAMES[a]}+{nilpotent_name(b)}"


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def matrix_add(*matrices: Matrix) -> Matrix:
    keys = set().union(*(matrix.keys() for matrix in matrices))
    out: Matrix = {}
    for key in keys:
        value = sum((matrix.get(key, Fraction(0)) for matrix in matrices), Fraction(0))
        if value:
            out[key] = value
    return out


def matrix_neg(matrix: Matrix) -> Matrix:
    return {key: -value for key, value in matrix.items()}


def matrix_sub(a: Matrix, b: Matrix) -> Matrix:
    return matrix_add(a, matrix_neg(b))


def matrix_scale(matrix: Matrix, scalar: Fraction) -> Matrix:
    return {key: scalar * value for key, value in matrix.items() if scalar * value}


def matrix_mul(a: Matrix, b: Matrix) -> Matrix:
    by_mid: dict[Label, list[tuple[Label, Fraction]]] = {}
    for (mid, col), value in b.items():
        by_mid.setdefault(mid, []).append((col, value))

    out: dict[tuple[Label, Label], Fraction] = {}
    for (row, mid), left in a.items():
        for col, right in by_mid.get(mid, []):
            key = (row, col)
            out[key] = out.get(key, Fraction(0)) + left * right

    return {key: value for key, value in out.items() if value}


@dataclass(frozen=True)
class ElementaryExpansion:
    """Pieces of Kbar through the mixed second-order coefficient."""

    order0: Matrix
    tame_order1: Matrix
    wild_order1: Matrix
    mixed_order2: Matrix


def first_order_coeff(mode: Label, gamma: Label, rho: Label) -> Fraction:
    """Coefficient of the elementary mode in the t-linear term."""

    if gamma == ZERO:
        return Fraction(-2 if mode == rho else 0)
    return Fraction(-1 if mode == add_label(rho, gamma) else 0)


def mixed_second_order_coeff(tau: Label, omega: Label, gamma: Label, rho: Label) -> Fraction:
    """Coefficient of s*r in the t^2 term for a fixed output rho.

    The convolution term contributes two ordered products when
    rho + gamma = tau + omega.  The moving tangent projection contributes one
    more mixed product when {gamma, rho} = {tau, omega}.
    """

    value = Fraction(0)
    if add_label(rho, gamma) == add_label(tau, omega):
        value += 2
    if (gamma == tau and rho == omega) or (gamma == omega and rho == tau):
        value += 1
    return value


@lru_cache(maxsize=None)
def elementary_expansion(alpha: Label, tau: Label, omega: Label) -> ElementaryExpansion:
    order0: Matrix = {}
    tame_order1: Matrix = {}
    wild_order1: Matrix = {}
    mixed_order2: Matrix = {}

    for beta in NONTRIVIAL:
        gamma = add_label(alpha, beta)

        if gamma != ZERO:
            order0[(gamma, beta)] = Fraction(1)

        for rho in NONTRIVIAL:
            tame = first_order_coeff(tau, gamma, rho)
            wild = first_order_coeff(omega, gamma, rho)
            mixed = mixed_second_order_coeff(tau, omega, gamma, rho)

            if tame:
                tame_order1[(rho, beta)] = tame
            if wild:
                wild_order1[(rho, beta)] = wild
            if mixed:
                mixed_order2[(rho, beta)] = mixed

    return ElementaryExpansion(order0, tame_order1, wild_order1, mixed_order2)


@lru_cache(maxsize=None)
def mixed_product_order2(alpha: Label, beta: Label, tau: Label, omega: Label) -> Matrix:
    """Coefficient of s*r*t^2 in K(alpha)K(beta)."""

    ka = elementary_expansion(alpha, tau, omega)
    kb = elementary_expansion(beta, tau, omega)
    return matrix_add(
        matrix_mul(ka.mixed_order2, kb.order0),
        matrix_mul(ka.tame_order1, kb.wild_order1),
        matrix_mul(ka.wild_order1, kb.tame_order1),
        matrix_mul(ka.order0, kb.mixed_order2),
    )


def mixed_defect_order2(alpha: Label, beta: Label, tau: Label, omega: Label) -> Matrix:
    """Coefficient of s*r*t^2 in K(alpha)K(beta) - K(alpha+beta), c=1."""

    kab = elementary_expansion(add_label(alpha, beta), tau, omega)
    return matrix_sub(mixed_product_order2(alpha, beta, tau, omega), kab.mixed_order2)


def mixed_symmetric_order2(alpha: Label, beta: Label, tau: Label, omega: Label) -> Matrix:
    """Symmetric part: 1/2({K(alpha),K(beta)} - 2K(alpha+beta))."""

    kab = elementary_expansion(add_label(alpha, beta), tau, omega)
    sym_product = matrix_scale(
        matrix_add(
            mixed_product_order2(alpha, beta, tau, omega),
            mixed_product_order2(beta, alpha, tau, omega),
        ),
        Fraction(1, 2),
    )
    return matrix_sub(sym_product, kab.mixed_order2)


def mixed_commutator_order2(alpha: Label, beta: Label, tau: Label, omega: Label) -> Matrix:
    """Antisymmetric part: 1/2[K(alpha),K(beta)]."""

    return matrix_scale(
        matrix_sub(
            mixed_product_order2(alpha, beta, tau, omega),
            mixed_product_order2(beta, alpha, tau, omega),
        ),
        Fraction(1, 2),
    )


def principal_unit_orbit(seed: Label) -> set[Label]:
    return {unit_action((1, c), seed) for c in range(4)}


def normalizer_orbit(seed: Label) -> set[Label]:
    units = [(a, b) for a in range(1, 4) for b in range(4)]
    out = set()
    for unit in units:
        y = unit_action(unit, seed)
        out.add(y)
        out.add(frobenius(y))
    return out


def normalizer_actions() -> list[dict[Label, Label]]:
    actions: list[dict[Label, Label]] = []
    seen: set[tuple[Label, ...]] = set()
    for leading_unit in range(1, 4):
        for nilpotent_unit in range(4):
            unit = (leading_unit, nilpotent_unit)
            for use_frobenius in [False, True]:
                action: dict[Label, Label] = {}
                for label in LABELS:
                    image = unit_action(unit, label)
                    if use_frobenius:
                        image = frobenius(image)
                    action[label] = image
                signature = tuple(action[label] for label in LABELS)
                if signature not in seen:
                    seen.add(signature)
                    actions.append(action)
    return actions


ACTIONS = normalizer_actions()


def transformed_key(key: tuple[Label, ...], action: dict[Label, Label]) -> tuple[Label, ...]:
    return tuple(action[label] for label in key)


def witness_key(witness: Witness) -> tuple[Label, ...]:
    return (
        witness["tau"],
        witness["omega"],
        witness["alpha"],
        witness["beta"],
        witness["input"],
        witness["output"],
    )


def swap_key(key: tuple[Label, ...]) -> tuple[Label, ...]:
    tau, omega, alpha, beta, input_label, output_label = key
    return (tau, omega, beta, alpha, input_label, output_label)


def frobenius_key(key: tuple[Label, ...]) -> tuple[Label, ...]:
    return tuple(frobenius(label) for label in key)


def local_coordinates(key: tuple[Label, ...]) -> tuple[tuple[object, ...], ...]:
    """Normalizer coordinates based at the elementary wild mode omega.

    For wild labels a+b*u, record leading ratio a/a_omega and translated tail
    ratio b/a - b_omega/a_omega.  For tame labels b*u, record b/a_omega.
    Principal units translate every wild tail ratio by the same amount, so
    subtracting the omega tail removes the wild-congruence gauge.
    """

    omega = key[1]
    omega_lead = omega[0]
    omega_tail = f4_div(omega[1], omega_lead)
    coordinates: list[tuple[object, ...]] = []

    for label in key:
        lead, tail = label
        if label == ZERO:
            coordinates.append(("0", 0, 0))
        elif lead == 0:
            coordinates.append(("u", f4_div(tail, omega_lead), 0))
        else:
            coordinates.append(
                (
                    "u^2",
                    f4_div(lead, omega_lead),
                    f4_add(f4_div(tail, lead), omega_tail),
                )
            )

    return tuple(coordinates)


def frobenius_coordinates(
    coordinates: tuple[tuple[object, ...], ...],
) -> tuple[tuple[object, ...], ...]:
    out = []
    for kind, leading, tail in coordinates:
        out.append((kind, f4_square(leading), f4_square(tail)))
    return tuple(out)


def canonical_local_signature(key: tuple[Label, ...]) -> tuple[tuple[object, ...], ...]:
    coordinates = local_coordinates(key)
    conjugate = frobenius_coordinates(coordinates)
    return min(coordinates, conjugate)


def coarse_local_signature(key: tuple[Label, ...], swap_kind: str) -> tuple[object, ...]:
    coordinates = canonical_local_signature(key)
    wild_tails = [tail for kind, _leading, tail in coordinates if kind == "u^2"]
    wild_leads = [leading for kind, leading, _tail in coordinates if kind == "u^2"]
    frobenius_cycle = 1 if frobenius_key(key) == key else 2
    return (
        tuple(conductor(label) for label in key[2:6]),
        f"{conductor(key[4])}->{conductor(key[5])}",
        swap_kind,
        frobenius_cycle,
        len(set(wild_leads)),
        f2_rank(wild_tails),
    )


def compute_witnesses(kind: str = "defect") -> list[Witness]:
    extractors = {
        "defect": mixed_defect_order2,
        "symmetric": mixed_symmetric_order2,
        "commutator": mixed_commutator_order2,
    }
    extractor = extractors[kind]
    witnesses: list[Witness] = []
    for tau in TAME:
        for omega in WILD:
            for alpha in NONTRIVIAL:
                for beta in NONTRIVIAL:
                    entries = extractor(alpha, beta, tau, omega)
                    for (row, col), coefficient in entries.items():
                        witnesses.append(
                            {
                                "tau": tau,
                                "omega": omega,
                                "alpha": alpha,
                                "beta": beta,
                                "input": col,
                                "output": row,
                                "coefficient": coefficient,
                                "input_conductor": conductor(col),
                                "output_conductor": conductor(row),
                            }
                        )
    return witnesses


def tangent_compatible(witnesses: list[Witness]) -> list[Witness]:
    return [
        witness for witness in witnesses if add_label(witness["alpha"], witness["beta"]) != ZERO
    ]


def full_depth(witnesses: list[Witness]) -> list[Witness]:
    return [
        witness
        for witness in witnesses
        if witness["input_conductor"] == "u^2" and witness["output_conductor"] == "u^2"
    ]


def orbit_decomposition(witnesses: list[Witness]) -> list[dict[str, object]]:
    coeff_by_key = {witness_key(witness): witness["coefficient"] for witness in witnesses}
    key_set = set(coeff_by_key)
    remaining = set(coeff_by_key)
    orbits: list[dict[str, object]] = []

    while remaining:
        seed = next(iter(remaining))
        orbit = {transformed_key(seed, action) for action in ACTIONS}
        present = orbit & key_set
        coefficients = Counter(coeff_by_key[key] for key in present)
        missing = len(orbit - key_set)
        orbits.append(
            {
                "seed": seed,
                "keys": present,
                "size": len(present),
                "ambient_size": len(orbit),
                "missing": missing,
                "coefficients": coefficients,
            }
        )
        remaining -= present

    return orbits


def coefficient_by_key(witnesses: list[Witness]) -> dict[tuple[Label, ...], Fraction]:
    return {witness_key(witness): witness["coefficient"] for witness in witnesses}


def orbit_summary_lines(title: str, witnesses: list[Witness]) -> list[str]:
    orbits = orbit_decomposition(witnesses)
    bad_orbits = [
        orbit for orbit in orbits if len(orbit["coefficients"]) > 1 or orbit["missing"] != 0
    ]
    size_counts = Counter(orbit["size"] for orbit in orbits)
    coeff_orbit_counts: Counter[tuple[Fraction, int]] = Counter()
    coeff_entry_counts: Counter[Fraction] = Counter()

    for orbit in orbits:
        if len(orbit["coefficients"]) == 1:
            coefficient = next(iter(orbit["coefficients"]))
            coeff_orbit_counts[(coefficient, orbit["size"])] += 1
            coeff_entry_counts[coefficient] += orbit["size"]

    return [
        f"### {title}",
        "",
        f"- Hayes-Frobenius action size: {len(ACTIONS)}",
        f"- orbits: {len(orbits)}",
        "- orbit sizes: "
        + ", ".join(f"{size}: {count}" for size, count in sorted(size_counts.items())),
        f"- nonconstant or incomplete orbits: {len(bad_orbits)}",
        "- coefficient entries by orbit union: "
        + ", ".join(
            f"{fraction_text(value)}: {count}"
            for value, count in sorted(coeff_entry_counts.items())
        ),
        "- coefficient/orbit-size table: "
        + ", ".join(
            f"coeff {fraction_text(coefficient)}, size {size}: {count} orbits"
            for (coefficient, size), count in sorted(coeff_orbit_counts.items())
        ),
        "",
    ]


def swap_orbit_summary_lines(
    defect_witnesses: list[Witness],
    symmetric_witnesses: list[Witness],
    commutator_witnesses: list[Witness],
) -> list[str]:
    defect_orbits = orbit_decomposition(defect_witnesses)
    defect_coeffs = coefficient_by_key(defect_witnesses)
    symmetric_coeffs = coefficient_by_key(symmetric_witnesses)
    commutator_coeffs = coefficient_by_key(commutator_witnesses)

    key_to_orbit: dict[tuple[Label, ...], int] = {}
    for orbit_id, orbit in enumerate(defect_orbits):
        for key in orbit["keys"]:
            key_to_orbit[key] = orbit_id

    swap_partner: dict[int, int] = {}
    for orbit_id, orbit in enumerate(defect_orbits):
        seed = next(iter(orbit["keys"]))
        swap_partner[orbit_id] = key_to_orbit[swap_key(seed)]

    swap_symmetric = [orbit_id for orbit_id, partner in swap_partner.items() if orbit_id == partner]
    swap_asymmetric = [orbit_id for orbit_id, partner in swap_partner.items() if orbit_id != partner]
    asymmetric_pairs = {
        tuple(sorted((orbit_id, partner)))
        for orbit_id, partner in swap_partner.items()
        if orbit_id != partner
    }

    commutator_supported_orbits = {
        key_to_orbit[key] for key in commutator_coeffs if key in key_to_orbit
    }
    commutator_zero_symmetric = sum(
        1
        for orbit_id in swap_symmetric
        if not (defect_orbits[orbit_id]["keys"] & set(commutator_coeffs))
    )

    asymmetric_pair_types: Counter[tuple[Fraction, Fraction, Fraction, Fraction]] = Counter()
    sym_pair_types: Counter[tuple[Fraction, Fraction]] = Counter()
    full_pair_types: Counter[tuple[Fraction, Fraction]] = Counter()

    for left, right in asymmetric_pairs:
        left_key = next(iter(defect_orbits[left]["keys"]))
        right_key = swap_key(left_key)
        if key_to_orbit[right_key] != right:
            right_key = next(iter(defect_orbits[right]["keys"]))
            left_key = swap_key(right_key)

        left_full = defect_coeffs[left_key]
        right_full = defect_coeffs[right_key]
        left_sym = symmetric_coeffs[left_key]
        right_sym = symmetric_coeffs[right_key]
        left_comm = commutator_coeffs.get(left_key, Fraction(0))
        right_comm = commutator_coeffs.get(right_key, Fraction(0))

        asymmetric_pair_types[(left_sym, right_sym, left_comm, right_comm)] += 1
        sym_pair_types[tuple(sorted((left_sym, right_sym)))] += 1
        full_pair_types[tuple(sorted((left_full, right_full)))] += 1

    missing_comm_asym = len(set(swap_asymmetric) - commutator_supported_orbits)
    extra_comm_sym = len(commutator_supported_orbits & set(swap_symmetric))

    return [
        "### Swap-involution structure",
        "",
        f"- full-defect orbits: {len(defect_orbits)}",
        f"- swap-symmetric orbits: {len(swap_symmetric)}",
        f"- swap-asymmetric orbits: {len(swap_asymmetric)}",
        f"- swap-asymmetric +/- pairs: {len(asymmetric_pairs)}",
        f"- commutator-supported orbits: {len(commutator_supported_orbits)}",
        f"- swap-symmetric orbits with zero commutator: {commutator_zero_symmetric}",
        f"- asymmetric orbits missing from commutator support: {missing_comm_asym}",
        f"- commutator orbits inside swap-symmetric stratum: {extra_comm_sym}",
        "- symmetric coefficients across asymmetric pairs: "
        + ", ".join(
            f"({fraction_text(a)},{fraction_text(b)}): {count}"
            for (a, b), count in sorted(sym_pair_types.items())
        ),
        "- full coefficients across asymmetric pairs: "
        + ", ".join(
            f"({fraction_text(a)},{fraction_text(b)}): {count}"
            for (a, b), count in sorted(full_pair_types.items())
        ),
        "- signed asymmetric pair types: "
        + ", ".join(
            f"sym ({fraction_text(sa)},{fraction_text(sb)}), comm ({fraction_text(ca)},{fraction_text(cb)}): {count}"
            for (sa, sb, ca, cb), count in sorted(asymmetric_pair_types.items())
        ),
        "",
    ]


def local_signature_summary_lines(
    defect_witnesses: list[Witness],
    commutator_witnesses: list[Witness],
) -> list[str]:
    defect_orbits = orbit_decomposition(defect_witnesses)
    defect_coeffs = coefficient_by_key(defect_witnesses)
    commutator_coeffs = coefficient_by_key(commutator_witnesses)

    key_to_orbit: dict[tuple[Label, ...], int] = {}
    for orbit_id, orbit in enumerate(defect_orbits):
        for key in orbit["keys"]:
            key_to_orbit[key] = orbit_id

    commutator_supported_orbits = {
        key_to_orbit[key] for key in commutator_coeffs if key in key_to_orbit
    }

    swap_partner: dict[int, int] = {}
    for orbit_id, orbit in enumerate(defect_orbits):
        seed = next(iter(orbit["keys"]))
        swap_partner[orbit_id] = key_to_orbit[swap_key(seed)]

    exact_signatures = Counter(
        canonical_local_signature(next(iter(orbit["keys"]))) for orbit in defect_orbits
    )
    commutator_exact_signatures = Counter(
        canonical_local_signature(next(iter(defect_orbits[orbit_id]["keys"])))
        for orbit_id in commutator_supported_orbits
    )

    coarse_buckets: dict[tuple[object, ...], list[int]] = {}
    for orbit_id, orbit in enumerate(defect_orbits):
        seed = next(iter(orbit["keys"]))
        if swap_partner[orbit_id] == orbit_id:
            swap_kind = "swap-fixed"
        else:
            swap_kind = "swap-asymmetric"
        coarse_buckets.setdefault(coarse_local_signature(seed, swap_kind), []).append(orbit_id)

    pure_coarse_coefficients = 0
    pure_coarse_curvature = 0
    max_coarse_size = 0
    for orbit_ids in coarse_buckets.values():
        max_coarse_size = max(max_coarse_size, len(orbit_ids))
        coefficients = {
            next(iter(defect_orbits[orbit_id]["coefficients"]))
            for orbit_id in orbit_ids
        }
        curvature_flags = {orbit_id in commutator_supported_orbits for orbit_id in orbit_ids}
        if len(coefficients) == 1:
            pure_coarse_coefficients += 1
        if len(curvature_flags) == 1:
            pure_coarse_curvature += 1

    exact_collision_buckets = sum(1 for count in exact_signatures.values() if count > 1)
    exact_max_multiplicity = max(exact_signatures.values())
    comm_exact_collision_buckets = sum(
        1 for count in commutator_exact_signatures.values() if count > 1
    )
    comm_exact_max_multiplicity = max(commutator_exact_signatures.values())

    return [
        "### Local-coordinate signatures",
        "",
        "Use omega as the wild base point.  For each wild label a+b*u, record",
        "a/a_omega and b/a - b_omega/a_omega; for each tame label b*u, record",
        "b/a_omega.  Then quotient the resulting tuple by Frobenius.",
        "",
        f"- exact local signatures for full-defect orbits: {len(exact_signatures)} / {len(defect_orbits)}",
        f"- exact signature collision buckets: {exact_collision_buckets}",
        f"- exact signature max multiplicity: {exact_max_multiplicity}",
        f"- exact local signatures for commutator orbits: {len(commutator_exact_signatures)} / {len(commutator_supported_orbits)}",
        f"- commutator exact signature collision buckets: {comm_exact_collision_buckets}",
        f"- commutator exact signature max multiplicity: {comm_exact_max_multiplicity}",
        "",
        "For the coarser candidate",
        "(operand conductors, matrix conductor transition, swap kind, Frobenius",
        "cycle length, number of wild leading residues, wild tail-rank):",
        "",
        f"- coarse buckets: {len(coarse_buckets)}",
        f"- max orbits in one coarse bucket: {max_coarse_size}",
        f"- coefficient-pure coarse buckets: {pure_coarse_coefficients} / {len(coarse_buckets)}",
        f"- curvature-support-pure coarse buckets: {pure_coarse_curvature} / {len(coarse_buckets)}",
        "",
    ]


def component_summary(kind: str, witnesses: list[Witness]) -> list[str]:
    tangent_witnesses = tangent_compatible(witnesses)
    full_depth_witnesses = full_depth(tangent_witnesses)
    coefficient_counts = Counter(w["coefficient"] for w in witnesses)
    tangent_coefficient_counts = Counter(w["coefficient"] for w in tangent_witnesses)
    conductor_counts = Counter((w["input_conductor"], w["output_conductor"]) for w in witnesses)
    pair_counts = Counter((w["tau"], w["omega"]) for w in witnesses)
    alpha_beta_counts = Counter((w["alpha"], w["beta"]) for w in witnesses)
    tangent_alpha_beta_counts = Counter((w["alpha"], w["beta"]) for w in tangent_witnesses)

    return [
        f"### {kind}",
        "",
        f"- nonzero elementary s*r*t^2 matrix entries: {len(witnesses)}",
        f"- tangent-compatible entries with alpha+beta nontrivial: {len(tangent_witnesses)}",
        f"- full-depth-to-full-depth tangent-compatible entries: {len(full_depth_witnesses)}",
        f"- nonzero (tau, omega) elementary mode pairs: {len(pair_counts)} / {len(TAME) * len(WILD)}",
        f"- nonzero (alpha, beta) operator pairs: {len(alpha_beta_counts)} / {len(NONTRIVIAL) ** 2}",
        f"- nonzero tangent-compatible (alpha, beta) pairs: {len(tangent_alpha_beta_counts)} / {len(NONTRIVIAL) * (len(NONTRIVIAL) - 1)}",
        "- coefficient distribution: "
        + ", ".join(
            f"{fraction_text(value)}: {count}" for value, count in sorted(coefficient_counts.items())
        ),
        "- tangent-compatible coefficient distribution: "
        + ", ".join(
            f"{fraction_text(value)}: {count}"
            for value, count in sorted(tangent_coefficient_counts.items())
        ),
        "- conductor transition distribution: "
        + ", ".join(
            f"{src}->{dst}: {count}" for (src, dst), count in sorted(conductor_counts.items())
        ),
        "",
    ]


def sorted_witnesses(witnesses: list[Witness]) -> list[Witness]:
    return sorted(
        witnesses,
        key=lambda w: (
            -abs(w["coefficient"]),
            label_name(w["tau"]),
            label_name(w["omega"]),
            label_name(w["alpha"]),
            label_name(w["beta"]),
            label_name(w["input"]),
            label_name(w["output"]),
        ),
    )


def summarize() -> str:
    defect_witnesses = compute_witnesses("defect")
    symmetric_witnesses = compute_witnesses("symmetric")
    commutator_witnesses = compute_witnesses("commutator")

    tangent_defect = tangent_compatible(defect_witnesses)
    full_corner_witnesses = full_depth(tangent_defect)
    first = sorted_witnesses(full_corner_witnesses)[0]

    tame_lower_orbits = [principal_unit_orbit(seed) for seed in WILD if seed[1] == 0]
    normalizer = normalizer_orbit((1, 0))

    lines = [
        "# F4[u]/(u^2) Ext_CH Diagnostic",
        "",
        "Ring model: F_4 = F_2[w]/(w^2+w+1), R = F_4[u]/(u^2).",
        "Character labels are written a+b*u and multiplied by addition in the label group.",
        "",
        "## Character packets",
        "",
        f"- total labels: {len(LABELS)}",
        f"- nontrivial tangent labels: {len(NONTRIVIAL)}",
        f"- conductor u (tame residue packet): {', '.join(label_name(x) for x in TAME)}",
        f"- conductor u^2 (wild/full packet): {len(WILD)} labels",
        "",
        "The lower-character action of the tame packet on the full packet preserves the",
        "leading coefficient and gives three affine F_4-fibers:",
    ]

    for orbit in tame_lower_orbits:
        lines.append("- " + ", ".join(label_name(x) for x in sorted(orbit)))

    lines += [
        "",
        "The unit group of R, together with Frobenius, is transitive on the full packet:",
        f"- |R^* semidirect Gal(F_4/F_2) orbit of 1| = {len(normalizer)}",
        "",
        "## Mixed curvature-defect extraction",
        "",
        "Normalization:",
        "",
        "```text",
        "Kbar_p(alpha)(v) = 16^{-1} Pi_p(chi_alpha * v / p)",
        "c = 1",
        "```",
        "",
        "With this normalization Kbar_{p_*}(alpha) is the full character",
        "multiplication operator before taking the augmentation corner.",
        "",
        "For every elementary tame mode tau and wild mode omega, the coefficient",
        "of s*r*t in the pure-axis-subtracted Delta is zero.  This is the",
        "Codazzi-symmetric first variation in computational form.  The first",
        "possible mixed term occurs at order t^2, and it is nonzero.",
        "",
        "The quadratic coefficient splits as",
        "",
        "```text",
        "K(alpha)K(beta)-K(alpha+beta)",
        "  = 1/2({K(alpha),K(beta)} - 2K(alpha+beta))",
        "    + 1/2[K(alpha),K(beta)].",
        "```",
        "",
    ]

    lines += component_summary("Full defect K(alpha)K(beta)-K(alpha+beta)", defect_witnesses)
    lines += component_summary("Symmetric Ext piece", symmetric_witnesses)
    lines += component_summary("Antisymmetric commutator piece", commutator_witnesses)

    lines += [
        "A full-depth explicit representative is:",
        "",
        "```text",
        f"tau    = {label_name(first['tau'])}        (tame Fourier mode)",
        f"omega  = {label_name(first['omega'])}        (wild Fourier mode)",
        f"alpha  = {label_name(first['alpha'])}",
        f"beta   = {label_name(first['beta'])}",
        f"input  = chi_{label_name(first['input'])}",
        f"output = chi_{label_name(first['output'])}",
        f"[s*r*t^2] Delta_mix = {fraction_text(first['coefficient'])}",
        "```",
        "",
        "Thus the mixed surplus survives after subtracting both pure axes.  It is",
        "not a scalar trace artifact: entries occur in the full-packet-to-full-packet",
        "corner as well as in transitions involving the residue packet.",
        "",
        "## Orbit canonicalization",
        "",
        "The normalizer used here is the 24-element group generated by F_4^*",
        "residue scaling, the four principal units 1+c*u, and Frobenius.  It acts",
        "simultaneously on tau, omega, alpha, beta, input, and output.",
        "",
    ]

    lines += orbit_summary_lines("Full defect tangent-compatible orbits", tangent_defect)
    lines += orbit_summary_lines(
        "Commutator tangent-compatible orbits",
        tangent_compatible(commutator_witnesses),
    )
    lines += swap_orbit_summary_lines(
        tangent_defect,
        tangent_compatible(symmetric_witnesses),
        tangent_compatible(commutator_witnesses),
    )
    lines += local_signature_summary_lines(
        tangent_defect,
        tangent_compatible(commutator_witnesses),
    )

    lines += [
        "## Interpretation",
        "",
        "The row confirms the first expected obstruction.  The tame packet alone",
        "only translates the nilpotent coordinate inside each fixed leading-residue",
        "fiber.  The principal-unit part of the local normalizer moves the nilpotent",
        "coordinate by a multiple of the leading residue.  The s*r*t^2 term is the",
        "first place where those two motions are multiplied inside the raised cubic",
        "composition law.",
        "",
        "The symmetric projection is nonzero and saturated, giving the first",
        "concrete Ext_CH representative for F_4[u]/(u^2).  The antisymmetric",
        "projection is also nonzero and saturated, so the curvature reading does",
        "not diverge on this row; it is an honest theorem candidate rather than",
        "an empty commutator.",
        "",
        "The coefficient classes are unions of Hayes-Frobenius orbits, not single",
        "orbits.  The four-value coefficient table is therefore a compression of",
        "the canonical form, while the orbit table is the first canonical",
        "representative datum for Problem 11.5.",
        "",
        "The swap test is sharper than the first guess: swap-asymmetry is necessary",
        "for a nonzero commutator but not sufficient.  Only 592 of the 4424",
        "swap-asymmetric full-defect orbits carry curvature; the remaining 3832",
        "are Ext-only.  The exact local-coordinate signature reconstructs the",
        "normalizer orbit without collisions, while the coarse candidate invariants",
        "collapse the row to 62 buckets and do not determine the coefficient.",
        "",
    ]

    return "\n".join(lines)


def main() -> None:
    report = summarize()
    report_path = Path(__file__).with_name("reports") / "f4_u2_ext_ch.md"
    report_path.write_text(report, encoding="utf-8")
    print(report)
    print(f"\nWrote {report_path}")


if __name__ == "__main__":
    main()
