#!/usr/bin/env python3
"""Exact symbolic certificate for the first primorial triple-mixing row.

This script certifies the support-level claim used in Paper 22:

    R = Z/30Z is the first row where the three prime axes 2, 3, and 5
    can mix into the full conductor 30.

It uses only integer arithmetic.  The key check is that pairwise sums of
primitive prime-axis character packets land on the pairwise faces 6, 10, and
15, while sums of one primitive character from each of the three prime axes
hit every primitive full-conductor character exactly once.  Equivalently, if
h is the indicator of the three prime-axis packets, the full-conductor
projection of h*h is zero and the full-conductor projection of h*h*h is
nonzero with coefficient 6 on every primitive full-conductor character.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from math import gcd
from pathlib import Path
from typing import Iterable


N = 30
PRIMES = (2, 3, 5)


def conductor(k: int, n: int = N) -> int:
    """Conductor of additive character chi_k on Z/nZ."""
    k %= n
    if k == 0:
        return 1
    return n // gcd(k, n)


def packet(cond: int, n: int = N) -> list[int]:
    return [k for k in range(n) if conductor(k, n) == cond]


def packet_table(n: int = N) -> dict[int, list[int]]:
    out: dict[int, list[int]] = defaultdict(list)
    for k in range(n):
        out[conductor(k, n)].append(k)
    return dict(sorted(out.items()))


def cyclic_convolution_support(labels: Iterable[int], order: int, n: int = N) -> Counter[int]:
    """Ordered convolution coefficients of an indicator supported on labels."""
    labels = list(labels)
    coeff = Counter({0: 1})
    for _ in range(order):
        nxt: Counter[int] = Counter()
        for a, ca in coeff.items():
            for b in labels:
                nxt[(a + b) % n] += ca
        coeff = nxt
    return coeff


@dataclass(frozen=True)
class FaceCertificate:
    face: str
    input_conductors: tuple[int, ...]
    output_conductors: tuple[int, ...]
    output_labels: tuple[int, ...]
    multiplicities: dict[int, int]


def pairwise_face_certificate(a: int, b: int) -> FaceCertificate:
    sums = Counter((x + y) % N for x in packet(a) for y in packet(b))
    return FaceCertificate(
        face=f"{a}x{b}",
        input_conductors=(a, b),
        output_conductors=tuple(sorted({conductor(k) for k in sums})),
        output_labels=tuple(sorted(sums)),
        multiplicities=dict(sorted(sums.items())),
    )


def triple_face_certificate() -> FaceCertificate:
    sums = Counter(
        (x + y + z) % N
        for x in packet(2)
        for y in packet(3)
        for z in packet(5)
    )
    return FaceCertificate(
        face="2x3x5",
        input_conductors=(2, 3, 5),
        output_conductors=tuple(sorted({conductor(k) for k in sums})),
        output_labels=tuple(sorted(sums)),
        multiplicities=dict(sorted(sums.items())),
    )


def build_certificate() -> dict:
    packets = packet_table()
    prime_axis_labels = sorted(k for p in PRIMES for k in packets[p])
    c2 = cyclic_convolution_support(prime_axis_labels, 2)
    c3 = cyclic_convolution_support(prime_axis_labels, 3)

    full_packet = packets[30]
    c2_full = {k: c2[k] for k in full_packet if c2[k]}
    c3_full = {k: c3[k] for k in full_packet if c3[k]}

    pairwise = [
        pairwise_face_certificate(2, 3),
        pairwise_face_certificate(2, 5),
        pairwise_face_certificate(3, 5),
    ]
    triple = triple_face_certificate()

    checks = {
        "pairwise_faces_have_no_full_conductor": all(
            cert.output_conductors != (30,) and 30 not in cert.output_conductors
            for cert in pairwise
        ),
        "triple_face_is_exactly_full_conductor": triple.output_conductors == (30,),
        "triple_face_hits_full_packet_once_unordered": sorted(triple.output_labels) == full_packet
        and all(v == 1 for v in triple.multiplicities.values()),
        "indicator_square_has_no_full_conductor": c2_full == {},
        "indicator_cube_hits_full_packet_with_ordered_multiplicity_6": sorted(c3_full) == full_packet
        and set(c3_full.values()) == {6},
    }

    return {
        "ring": "Z/30Z",
        "modulus": N,
        "primes": PRIMES,
        "conductor_packets": {str(k): v for k, v in packets.items()},
        "prime_axis_labels": prime_axis_labels,
        "pairwise_faces": [asdict(cert) for cert in pairwise],
        "triple_face": asdict(triple),
        "indicator_convolution": {
            "support": prime_axis_labels,
            "order_2_full_conductor_coefficients": c2_full,
            "order_3_full_conductor_coefficients": c3_full,
        },
        "checks": checks,
        "pass": all(checks.values()),
    }


def markdown_report(cert: dict) -> str:
    packet_rows = "\n".join(
        f"| {cond} | {len(labels)} | `{labels}` |"
        for cond, labels in cert["conductor_packets"].items()
    )
    pair_rows = "\n".join(
        f"| `{p['face']}` | `{p['input_conductors']}` | `{p['output_conductors']}` | `{p['output_labels']}` | `{p['multiplicities']}` |"
        for p in cert["pairwise_faces"]
    )
    checks = "\n".join(
        f"- {'PASS' if ok else 'FAIL'} `{name}`"
        for name, ok in cert["checks"].items()
    )
    c3_full = cert["indicator_convolution"]["order_3_full_conductor_coefficients"]
    c2_full = cert["indicator_convolution"]["order_2_full_conductor_coefficients"]
    triple = cert["triple_face"]

    return f"""# Z/30 Primorial Symbolic Certificate

This certificate is generated by `empirical/z30_primorial_symbolic_certificate.py`.
It uses exact integer arithmetic on `R = Z/30Z`.

## Claim

`R=30=2*3*5` is the first primorial row where one primitive character from each
prime-axis conductor packet can mix into the full conductor `30`.

Equivalently, if `h` is the indicator of the primitive prime-axis packets
`cond=2`, `cond=3`, and `cond=5`, then:

- the full-conductor projection of `h*h` is zero;
- the full-conductor projection of `h*h*h` is nonzero;
- every primitive full-conductor label is hit with ordered multiplicity `6`.

This is the exact support-level certificate for the Paper 22 quartic/triple-prime
mixing statement. It is not a numerical RH verification.

## Conductor Packets

| conductor | size | labels |
|---:|---:|---|
{packet_rows}

## Pairwise Faces

Pairwise prime-axis sums stay on pairwise conductors and do not reach `30`.

| face | input conductors | output conductors | output labels | multiplicities |
|---|---|---|---|---|
{pair_rows}

## Triple Face

One label from each prime-axis packet hits the full conductor.

- face: `{triple['face']}`
- input conductors: `{triple['input_conductors']}`
- output conductors: `{triple['output_conductors']}`
- output labels: `{triple['output_labels']}`
- multiplicities: `{triple['multiplicities']}`

## Indicator Convolution

Prime-axis support:

`{cert['prime_axis_labels']}`

Full-conductor coefficients in `h*h`:

`{c2_full}`

Full-conductor coefficients in `h*h*h`:

`{c3_full}`

## Checks

{checks}

## Verdict

`{'PASS' if cert['pass'] else 'FAIL'}`

The first non-pairwise conductor support appears exactly at the triple product
of the three prime axes, landing on conductor `30`. This supports the claim that
the quartic/jerk row `R=30` is the first symbolic stage at which genuine
three-prime mixing can occur.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json",
        default="empirical/reports/z30_primorial_symbolic_certificate.json",
        help="JSON output path",
    )
    parser.add_argument(
        "--md",
        default="empirical/reports/z30_primorial_symbolic_certificate.md",
        help="Markdown output path",
    )
    args = parser.parse_args()

    cert = build_certificate()
    json_path = Path(args.json)
    md_path = Path(args.md)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(markdown_report(cert), encoding="utf-8")
    print(f"wrote {json_path}")
    print(f"wrote {md_path}")
    print(f"verdict: {'PASS' if cert['pass'] else 'FAIL'}")


if __name__ == "__main__":
    main()
