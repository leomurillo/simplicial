"""Verify the distinct-value correction budget with exact rational arithmetic."""
from fractions import Fraction
from pathlib import Path
import json
import math


def admissible_lower_points(n, m):
    points = [n]
    z = n + 2
    while len(points) < m:
        if z % 3:
            points.append(z)
        z += 2
    return points


def main():
    checks = certificates = 0
    example = None
    descent_without_packing_certificate = []
    for n in range(3, 10001, 2):
        z, S, actual_product, seen, points_product, b = n, 0, Fraction(1), set(), Fraction(1), n
        for m in range(1, 10001):
            assert z >= n and z not in seen
            seen.add(z)
            actual_product *= Fraction(3*z+1, 3*z)
            if m == 1:
                b = n
            else:
                b += 2
                while b % 3 == 0:
                    b += 2
            points_product *= Fraction(3*b+1, 3*b)
            v = 3*z+1
            s = (v & -v).bit_length()-1
            z = v >> s
            S += s
            assert Fraction(z, n) == Fraction(3**m, 2**S)*actual_product
            assert actual_product <= points_product
            assert Fraction(2**S, 3**m) <= points_product or z < n
            if Fraction(2**S, 3**m) > points_product:
                certificates += 1
            checks += 1
            if z < n:
                if Fraction(2**S,3**m) <= points_product:
                    descent_without_packing_certificate.append(dict(n=n, odd_steps=m, halvings=S, endpoint=z))
                if n == 27:
                    example = dict(n=n, odd_steps=m, halvings=S, endpoint=z,
                                   log_surplus=S*math.log(2)-m*math.log(3),
                                   actual_log_correction=math.log(actual_product),
                                   packing_log_budget=math.log(points_product),
                                   old_linear_log_budget=m/(3*n),
                                   packing_certificate=Fraction(2**S,3**m)>points_product)
                break
        else:
            raise AssertionError(('Cap reached', n))
    for r in range(2, 101):
        n=2**r-1
        z=n
        for j in range(r-1):
            v=3*z+1
            assert v%4==2
            z=v//2
            assert z==3**(j+1)*2**(r-j-1)-1
        assert 3*z+1==2*3**r-2
    result=dict(status='passed', starts=4999, exact_prefix_checks=checks,
                sufficient_packing_certificates=certificates, example_27=example,
                descent_without_packing_certificate=descent_without_packing_certificate,
                mersenne_family_r_range=[2,100])
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
