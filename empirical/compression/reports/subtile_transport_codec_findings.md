# Sub-Tile Transport Codec Findings

This pass deployed the first T13-T15 refinement-boundary codec benchmark:

```text
g-bg-ravg gauge
  -> local tile predictor
  -> direct block-refined Apex posterior
  -> optional sub-tile DC/copy boundary commands
```

The implementation is `../benchmark_subtile_transport_vs_webp.py`.

## What Shipped

The script now supports two paths:

- **direct block Apex:** keep exact predictor residuals, but route the Apex
  posterior through block-scale decoder-visible context such as gradient;
- **refined sub-tile commands:** optionally replace a residual block by either
  a DC boundary correction or a transported prior residual string, storing
  sparse command flags and reference metadata.

The deployed value is the smaller of those two paths. This makes refinement
safe: if a boundary command does not pay, the codec falls back to direct
posterior coding.

## Costa Rica 512x512 Deployment

Best deployed run:

```powershell
python empirical\compression\benchmark_subtile_transport_vs_webp.py `
  --direct-only --crop-size 512 --block-size 32 `
  --json empirical\compression\reports\subtile_transport_vs_webp_costa_rica_512_b32_direct.json `
  --report empirical\compression\reports\subtile_transport_vs_webp_costa_rica_512_b32_direct.md `
  C:\Users\leomu\Downloads\que-ver-en-costa-rica-correos-portada.jpg `
  C:\Users\leomu\Downloads\central-valley-san-jose-costa-rica.jpg
```

| file | WebP | deployed native | best state | ideal | result |
|---|---:|---:|---|---:|---:|
| `que-ver-en-costa-rica-correos-portada.jpg` | 231,732 | 250,486 | `ch-ctx-energy` | 245,833 | +18,754 (+8.09%) |
| `central-valley-san-jose-costa-rica.jpg` | 307,430 | 303,155 | `ch-ctx-grad` | 297,378 | -4,275 (-1.39%) |

Totals:

- WebP lossless: `539,162` bytes
- deployed native estimate: `553,641` bytes
- result vs WebP: `+14,479` bytes (`+2.69%`)
- ideal no-codebook ceiling: `543,211` bytes
- ideal vs WebP: `+4,049` bytes (`+0.75%`)

This result counts the residual-energy side metadata: 3 stored bits per
predictor tile when an energy-context scheme is selected.

## What Improved

Compared with the first Apex-ANS estimate on these same 512 crops:

- old Apex-ANS: `560,505` bytes (`+3.96%` vs WebP)
- deployed block-refined Apex: `553,641` bytes (`+2.69%` vs WebP)
- improvement: `6,864` bytes

The gain is the T14 move: residual energy is projected curvature, so it should
route the posterior. The central crop still prefers gradient routing; the
Correos crop needs stored residual-energy routing.

## What Did Not Work Yet

The sub-tile DC/copy command path is implemented, but it is not profitable on
the tested 512 deployment. On 256 smoke tests, command refinement saved too few
local residual-score bytes to repay command flags and reference metadata.

That means the next copy layer must be more selective than "try every block":

- use row/path strings instead of rectangular blocks;
- mine candidate references from repeated context signatures;
- use cheaper command coding for common near references;
- accept copy commands only after a global entropy estimate, not only local
  Rice-score savings.

## Current Native Reading

The retained sector is now:

```text
g-bg-ravg + tile predictor + channel/context/gradient/energy posterior state
```

The exact boundary is still mostly a direct residual stream. The deployed
prototype proves the posterior-routing part is useful; the transported-string
boundary still needs a better candidate miner.

