# Helmert Frame-Price Frontier

This sweep estimates the arithmetic frame price needed to prefer
conductor-respecting gauge cascades over Haar-random mixed flags.
Each row/packet is evaluated at several off-centroid amplitudes.

The main number is `lambda_full_crit`: the maximum sampled
packet-commutator impurity weight needed for the conductor prefix to
beat every sampled mixed flag under the full subspace J ledger.

## Config

- `rows`: `['f2-u2', 'f2-u3', 'f4-u2']`
- `amplitudes`: `[0.05, 0.1, 0.2, 0.35, 0.5]`
- `samples`: `1000`
- `seed`: `20260515`
- `ledger_weights`: `{'block': 1.0, 'mix': 1.0, 'fisher_projection': 1.0, 'reciprocal_projection': 1.0, 'closure': 1.0, 'resource': 0.1, 'depth': 0.1}`
- `skip_lowest`: `True`
- `keep_details`: `False`

## Frontier Summary

| row | packet | depth | active dim | lambda_full max | lambda_full median | lambda_raw max | max better full J | max better raw |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| F_2[u]/(u^2) | u^2 | 2 | 3 | 63540.8 | 24710.7 | 63540.8 | 270/1000 | 1000/1000 |
| F_4[u]/(u^2) | u^2 | 2 | 15 | 3.51202 | 1.21474 | 3.51202 | 97/1000 | 866/1000 |
| F_2[u]/(u^3) | u^3 | 3 | 7 | 1.78538 | 0.367223 | 1.78538 | 22/1000 | 1000/1000 |
| F_2[u]/(u^3) | u^2 | 2 | 3 | 0 | 0 | 0.57787 | 0/1000 | 84/1000 |

## Amplitude Traces

### F_2[u]/(u^2) target `u^2`

| amplitude | lambda_full | better full J | lambda_raw | better raw | conductor J | random J median | conductor coupling | random coupling median |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.05 | 68.08 | 15/1000 | 68.08 | 1000/1000 | 0.202266 | 0.550052 | 0.00226647 | 0.000777419 |
| 0.1 | 3630.46 | 48/1000 | 3630.46 | 1000/1000 | 0.20919 | 0.59542 | 0.00919013 | 0.00303009 |
| 0.2 | 24710.7 | 69/1000 | 24710.7 | 999/1000 | 0.238855 | 0.577522 | 0.0388547 | 0.0146932 |
| 0.35 | 48422.7 | 162/1000 | 48422.7 | 987/1000 | 0.339748 | 0.615715 | 0.139748 | 0.0602841 |
| 0.5 | 63540.8 | 270/1000 | 63540.8 | 989/1000 | 0.576257 | 0.753877 | 0.376257 | 0.166227 |

### F_4[u]/(u^2) target `u^2`

| amplitude | lambda_full | better full J | lambda_raw | better raw | conductor J | random J median | conductor coupling | random coupling median |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.05 | 0.102413 | 0/1000 | 0.102413 | 866/1000 | 0.208573 | 0.398256 | 0.00857348 | 0.00574133 |
| 0.1 | 0.300136 | 0/1000 | 0.300136 | 851/1000 | 0.23003 | 0.415439 | 0.0300301 | 0.0218982 |
| 0.2 | 1.21474 | 3/1000 | 1.21474 | 848/1000 | 0.30045 | 0.465195 | 0.10045 | 0.0736344 |
| 0.35 | 1.93941 | 14/1000 | 1.93941 | 684/1000 | 0.479846 | 0.641741 | 0.279846 | 0.24912 |
| 0.5 | 3.51202 | 97/1000 | 3.51202 | 442/1000 | 0.826408 | 1.04582 | 0.626408 | 0.654536 |

### F_2[u]/(u^3) target `u^3`

| amplitude | lambda_full | better full J | lambda_raw | better raw | conductor J | random J median | conductor coupling | random coupling median |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.05 | 0.00939342 | 0/1000 | 0.00939342 | 1000/1000 | 0.203401 | 0.806107 | 0.00340098 | 0.0017647 |
| 0.1 | 0.0437513 | 0/1000 | 0.0437513 | 1000/1000 | 0.213806 | 0.806255 | 0.0138059 | 0.0071809 |
| 0.2 | 0.367223 | 0/1000 | 0.367223 | 1000/1000 | 0.258633 | 0.829047 | 0.0586327 | 0.0315288 |
| 0.35 | 0.55139 | 0/1000 | 0.55139 | 1000/1000 | 0.413485 | 0.920966 | 0.213485 | 0.121329 |
| 0.5 | 1.78538 | 22/1000 | 1.78538 | 1000/1000 | 0.785609 | 1.15234 | 0.585609 | 0.359188 |

### F_2[u]/(u^3) target `u^2`

| amplitude | lambda_full | better full J | lambda_raw | better raw | conductor J | random J median | conductor coupling | random coupling median |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.05 | 0 | 0/1000 | 0.00250239 | 84/1000 | 0.11179 | 2.23072 | 0.00226647 | 0.00354569 |
| 0.1 | 0 | 0/1000 | 0.0104438 | 77/1000 | 0.118714 | 2.23487 | 0.00919013 | 0.0146085 |
| 0.2 | 0 | 0/1000 | 0.57787 | 82/1000 | 0.148378 | 2.29194 | 0.0388547 | 0.0616686 |
| 0.35 | 0 | 0/1000 | 0.145972 | 54/1000 | 0.249272 | 2.48443 | 0.139748 | 0.229288 |
| 0.5 | 0 | 0/1000 | 0.258474 | 47/1000 | 0.485781 | 2.89879 | 0.376257 | 0.660497 |

## Reading

A high raw critical price says that random mixed frames can diagonalize
the single tested Fisher matrix better than the conductor frame.  A
low full critical price says that this advantage disappears once packet
respect, projection, closure, resource, and depth are priced.  The
interesting pressure points are therefore not the rows where raw mixed
flags win, but the rows where `lambda_full_crit` remains high across
amplitudes.
