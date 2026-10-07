"""Sweep 1: degrees 2-4, integer coefficients, find max N* and survivors."""
from search import scan, full_psd_failure, poly_from_coeffs, valid_on_primes
import itertools

Nmax = 8
cands = []

# degree 2: p^2 + a p + b
for a in range(-3, 12):
    for b in range(-3, 30):
        cands.append((f"p^2+{a}p+{b}", [1, a, b]))

# degree 3: p^3 + a p^2 + b p + c  (smaller range)
for a in range(-2, 6):
    for b in range(-2, 8):
        for c in range(-2, 8):
            cands.append((f"p^3+{a}p^2+{b}p+{c}", [1, a, b, c]))

print(f"Total candidates (pre-filter): {len(cands)}")
res = scan(cands, Nmax=Nmax)

survivors = [r for r in res if r[2] is None]
print(f"Leading-minor survivors through N={Nmax}: {len(survivors)}")
for s in survivors[:50]:
    print("  SURVIVOR:", s[0], s[1])

# distribution of N*
from collections import Counter
dist = Counter(r[2] for r in res if r[2] is not None)
print("N* distribution:", dict(sorted(dist.items())))

# largest N* (closest to survivor)
nonsurv = [r for r in res if r[2] is not None]
nonsurv.sort(key=lambda r: -r[2])
print("Largest N* examples:")
for r in nonsurv[:15]:
    print(f"  N*={r[2]}  {r[0]}")
