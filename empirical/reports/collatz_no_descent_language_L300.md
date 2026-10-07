# Collatz No-Descent Carry Language

## Meaning

Assume the margin theorem candidate is true: every contracting carry block decreases the first positive integer in its exact cylinder, and all larger representatives too.  Then an orbit can avoid descent below its current value for `m` accelerated odd steps only if every prefix is noncontracting:

```text
S_j <= floor(j log2(3))  for every j <= m.
```

This report studies that avoidance language.  It is the second half of the program in finite form.

## What We Can Know

The avoiding language is symbolically large but arithmetically small.  Its word count grows exponentially, while its exact cylinder mass decays exponentially.  Therefore the margin theorem would imply a density-one total stopping statement: the set of odd integers with no descent by step `m` has density at most the mass below.

- max length: `300`
- final word count: `2014549997906717303130740523187366891297492730903728386056476619937300274279334560644235669631296308845677687692464786213166699155258`
- final log2 word count / step: `1.465016553788`
- final cylinder mass: `1.28156024932e-10`
- final log2 mass / step: `-0.109537932147`
- tail mean log2 mass / step: `-0.117929552033`

## Avoidance Counts And Mass

| m | words | log2 words/m | mass | log2 mass | log2 mass/m | states |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0.000000 | 0.5 | -1.000000 | -1.000000 | 1 |
| 2 | 2 | 0.500000 | 0.375 | -1.415037 | -0.707519 | 2 |
| 3 | 3 | 0.528321 | 0.25 | -2.000000 | -0.666667 | 2 |
| 4 | 7 | 0.701839 | 0.203125 | -2.299560 | -0.574890 | 3 |
| 5 | 12 | 0.716993 | 0.1484375 | -2.752072 | -0.550414 | 3 |
| 8 | 173 | 0.929329 | 0.089599609375 | -3.480364 | -0.435045 | 5 |
| 10 | 961 | 0.990839 | 0.0645141601563 | -3.954240 | -0.395424 | 6 |
| 12 | 8045 | 1.081156 | 0.0521240234375 | -4.261908 | -0.355159 | 8 |
| 16 | 312455 | 1.140831 | 0.0309161543846 | -5.015495 | -0.313468 | 10 |
| 20 | 13472296 | 1.184175 | 0.0192539221607 | -5.698704 | -0.284935 | 12 |
| 24 | 820236724 | 1.233811 | 0.013138690927 | -6.250035 | -0.260418 | 15 |
| 30 | 248369601964 | 1.261790 | 0.00707457120691 | -7.143142 | -0.238105 | 18 |
| 40 | 6113392816333320 | 1.311022 | 0.00298613076691 | -8.387507 | -0.209688 | 24 |
| 60 | 4327322846731848749589802 | 1.363996 | 0.000615234565339 | -10.666576 | -0.177776 | 36 |
| 80 | 2743802136233200494910736532266785 | 1.388498 | 0.000139555997566 | -12.806868 | -0.160086 | 47 |
| 100 | 2309006583627815515505755316801664143732646 | 1.407283 | 3.45154871652e-05 | -14.822397 | -0.148224 | 59 |
| 120 | 2450373701953557431607378691550657268769334632341673 | 1.422594 | 9.3061361718e-06 | -16.713386 | -0.139278 | 71 |
| 160 | 1938149484343764719905423876895343603751625390241910067211236056365513 | 1.438548 | 6.88680796139e-07 | -20.469661 | -0.127935 | 94 |
| 200 | 1529521697313791255149057175236694954324379833018091836162568610052464825042974622948613 | 1.448104 | 5.45670421483e-08 | -24.127395 | -0.120637 | 117 |
| 240 | 1926783595515421208290691860966934375920174004059675726695909095115675733961306794111780739084642156052550 | 1.457286 | 4.81831383212e-09 | -27.628824 | -0.115120 | 141 |
| 300 | 2014549997906717303130740523187366891297492730903728386056476619937300274279334560644235669631296308845677687692464786213166699155258 | 1.465017 | 1.28156024932e-10 | -32.861380 | -0.109538 | 176 |

## Extremal Corridors

`all-ones` is the maximally expanding symbolic corridor; its infinite 2-adic limit is `-1`.  `balanced-boundary` is the maximal prefix that stays just under the height boundary.

| label | m | S | H | log2 n0 | log2 image | log2 gain | word |
|---|---:|---:|---:|---:|---:|---:|---|
| all-ones | 1 | 1 | -0.584963 | 1.584963 | 2.321928 | 0.736966 | `(1)` |
| balanced-boundary | 1 | 1 | -0.584963 | 1.584963 | 2.321928 | 0.736966 | `(1)` |
| all-ones | 2 | 2 | -1.169925 | 2.807355 | 4.087463 | 1.280108 | `(1^2)` |
| balanced-boundary | 2 | 3 | -0.169925 | 3.459432 | 3.700440 | 0.241008 | `(1 2)` |
| all-ones | 3 | 3 | -1.754888 | 3.906891 | 5.727920 | 1.821030 | `(1^3)` |
| balanced-boundary | 3 | 4 | -0.754888 | 4.754888 | 5.554589 | 0.799701 | `(1 2 1)` |
| all-ones | 4 | 4 | -2.339850 | 4.954196 | 7.330917 | 2.376721 | `(1^4)` |
| balanced-boundary | 4 | 6 | -0.339850 | 6.942515 | 7.294621 | 0.352106 | `(1 2 1 2)` |
| all-ones | 5 | 5 | -2.924813 | 5.977280 | 8.921841 | 2.944561 | `(1^5)` |
| balanced-boundary | 5 | 7 | -0.924813 | 7.971544 | 8.903882 | 0.932338 | `(1 2 1 2 1)` |
| all-ones | 8 | 8 | -4.679700 | 8.997179 | 13.679590 | 4.682411 | `(1^8)` |
| balanced-boundary | 8 | 12 | -0.679700 | 12.806348 | 13.486458 | 0.680110 | `(1 2 1 2 1 2^2 1)` |
| all-ones | 10 | 10 | -5.849625 | 10.999295 | 16.849613 | 5.850317 | `(1^10)` |
| balanced-boundary | 10 | 15 | -0.849625 | 14.523256 | 15.373035 | 0.849779 | `(1 2 1 2 1 2^2 1 2 1)` |
| all-ones | 12 | 12 | -7.019550 | 12.999824 | 20.019549 | 7.019725 | `(1^12)` |
| balanced-boundary | 12 | 19 | -0.019550 | 19.843913 | 19.863468 | 0.019555 | `(1 2 1 2 1 2^2 1 2 1 2^2)` |
| all-ones | 16 | 16 | -9.359400 | 16.999989 | 26.359400 | 9.359411 | `(1^16)` |
| balanced-boundary | 16 | 25 | -0.359400 | 24.802062 | 25.161462 | 0.359400 | `(1 2 1 2 1 2^2 1 2 1 2^2 1 2 1 2)` |
| all-ones | 20 | 20 | -11.699250 | 20.999999 | 32.699250 | 11.699251 | `(1^20)` |
| balanced-boundary | 20 | 31 | -0.699250 | 31.656379 | 32.355629 | 0.699250 | `(1 2 1 2 1 2^2 1 ... 1 2 1 2 1 2^2 1)` |
| all-ones | 24 | 24 | -14.039100 | 25.000000 | 39.039100 | 14.039100 | `(1^24)` |
| balanced-boundary | 24 | 38 | -0.039100 | 37.452466 | 37.491566 | 0.039100 | `(1 2 1 2 1 2^2 1 ... 2 1 2^2 1 2 1 2^2)` |
| all-ones | 30 | 30 | -17.548875 | 31.000000 | 48.548875 | 17.548875 | `(1^30)` |
| balanced-boundary | 30 | 47 | -0.548875 | 46.015048 | 46.563923 | 0.548875 | `(1 2 1 2 1 2^2 1 ... 2^2 1 2 1 2 1 2)` |
| all-ones | 40 | 40 | -23.398500 | 41.000000 | 64.398500 | 23.398500 | `(1^40)` |
| balanced-boundary | 40 | 63 | -0.398500 | 63.434669 | 63.833169 | 0.398500 | `(1 2 1 2 1 2^2 1 ... 2 1 2^2 1 2 1 2)` |
| all-ones | 60 | 60 | -35.097750 | 61.000000 | 96.097750 | 35.097750 | `(1^60)` |
| balanced-boundary | 60 | 95 | -0.097750 | 92.056454 | 92.154204 | 0.097750 | `(1 2 1 2 1 2^2 1 ... 2^2 1 2 1 2 1 2^2)` |
| all-ones | 80 | 80 | -46.797000 | 81.000000 | 127.797000 | 46.797000 | `(1^80)` |
| balanced-boundary | 80 | 126 | -0.797000 | 126.941891 | 127.738891 | 0.797000 | `(1 2 1 2 1 2^2 1 ... 1 2 1 2^2 1 2 1)` |
| all-ones | 100 | 100 | -58.496250 | 101.000000 | 159.496250 | 58.496250 | `(1^100)` |
| balanced-boundary | 100 | 158 | -0.496250 | 158.853938 | 159.350188 | 0.496250 | `(1 2 1 2 1 2^2 1 ... 2 1 2^2 1 2 1 2)` |
| all-ones | 120 | 120 | -70.195500 | 121.000000 | 191.195500 | 70.195500 | `(1^120)` |
| balanced-boundary | 120 | 190 | -0.195500 | 190.396425 | 190.591925 | 0.195500 | `(1 2 1 2 1 2^2 1 ... 2^2 1 2 1 2^2 1 2)` |

## Interpretation

The second half is exactly the infinite-intersection problem.  The finite bad sets shrink in density, but the infinite symbolic language is nonempty in the 2-adics.  The all-ones corridor already shows why measure is not enough: it is a perfectly valid infinite 2-adic carry sequence, but it corresponds to `-1`, not a positive escaping integer.

So the remaining pointwise theorem is:

```text
No positive odd integer has an infinite carry sequence with
S_j <= floor(j log2(3)) for every prefix j.
```

Equivalently: every positive odd integer other than the trivial fixed point eventually has a positive-height prefix block, hence a descent block if the margin theorem holds.

## Reproduction

```powershell
python empirical/collatz_no_descent_language.py --max-length 300
```
