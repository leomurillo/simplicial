# Collatz Height Pressure

## Status

This report studies the escape-side height cocycle on carry cylinders.  It does not test cycles; it estimates how large the low-height part of the infinite carry tree is.

- max prefix length: `120`
- barriers: `[0.0, 2.0, 4.0, 8.0]`
- log2(3): `1.584962500721`
- mean carry depth under Haar: `2.000000`
- mean height per step: `0.415037499279`

## Pressure Operator

For the one-state carry shift with branch mass `2^-s`,

```text
rho(theta) = sum_s 2^-s 2^{-theta(s-log2(3))}
           = 3^theta / (2^(1+theta)-1)
P(theta)   = log2 rho(theta)
```

- minimizing theta: `0.438032659282`
- minimum pressure P(theta): `-0.079318612775` bits/step
- Chernoff lower-tail rate: `0.079318612775` bits/step
- minimum spectral radius: `0.946504576833`
- nonzero pressure root: `1.000000`

The negative pressure minimum means nonpositive-height prefixes are exponentially suppressed in 2-adic cylinder mass, even though they occur at every finite depth.

## Nonpositive-Height Prefix Mass

This is the exact mass of length-`m` carry words with `S <= floor(m log2(3))`.

| m | max S | bad mass | log2 bad mass | Chernoff log2 bound | slack bits |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0.5 | -1.000000 | -0.079319 | 0.920681 |
| 2 | 3 | 0.5 | -1.000000 | -0.158637 | 0.841363 |
| 3 | 4 | 0.3125 | -1.678072 | -0.237956 | 1.440116 |
| 4 | 6 | 0.34375 | -1.540568 | -0.317274 | 1.223294 |
| 5 | 7 | 0.2265625 | -2.142019 | -0.396593 | 1.745426 |
| 8 | 12 | 0.19384765625 | -2.367005 | -0.634549 | 1.732456 |
| 10 | 15 | 0.15087890625 | -2.728537 | -0.793186 | 1.935351 |
| 12 | 19 | 0.179641723633 | -2.476806 | -0.951823 | 1.524982 |
| 16 | 25 | 0.114761471748 | -3.123290 | -1.269098 | 1.854192 |
| 20 | 31 | 0.0748063921928 | -3.740695 | -1.586372 | 2.154322 |
| 30 | 47 | 0.0394703468407 | -4.663087 | -2.379558 | 2.283529 |
| 40 | 63 | 0.0214782727622 | -5.540978 | -3.172745 | 2.368234 |
| 60 | 95 | 0.006689351513 | -7.223918 | -4.759117 | 2.464801 |
| 80 | 126 | 0.00156280553314 | -9.321646 | -6.345489 | 2.976157 |
| 100 | 158 | 0.000521283097703 | -10.905645 | -7.931861 | 2.973784 |
| 120 | 190 | 0.00017617055343 | -12.470740 | -9.518234 | 2.952506 |

## Prefix-Barrier Survival

For a barrier `B`, this is the mass of carry sequences whose every prefix satisfies `H(prefix) <= B`.  This is stricter than merely having low height at the final prefix.

| barrier | m | survival mass | log2 survival mass | tail log2 mass/step | final states |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 120 | 9.3061361718e-06 | -16.713386 | -0.155239 | 71 |
| 2.0 | 120 | 4.80750978531e-05 | -14.344351 | -0.128148 | 73 |
| 4.0 | 120 | 0.000135739095461 | -12.846876 | -0.111317 | 75 |
| 8.0 | 120 | 0.000643859048005 | -10.600967 | -0.086786 | 79 |

## Interpretation

The pressure calculation gives the escape-side algebraic shape.  The typical carry word has positive height because `E[s]=2 > log2(3)`, so typical affine slopes contract.  The low-height tree still exists at every finite depth, but its cylinder mass decays exponentially at the pressure rate.

This is not a proof against escape.  A proof would have to couple this height pressure to the affine cocycle `C_w` and to the Archimedean size of actual positive integers, not only to 2-adic cylinder mass.  The next algebraic object is therefore a two-cocycle pressure system tracking `(H(w), log2 C_w)` or a normalized intercept cocycle alongside height.

## Reproduction

```powershell
python empirical/collatz_height_pressure.py --max-length 120 --barriers "0.0,2.0,4.0,8.0"
```
