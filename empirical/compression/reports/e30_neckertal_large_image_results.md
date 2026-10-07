# E30 Neckertal Large-Image Test

Source image:

- `C:\Users\leomu\Downloads\Neckertal_20150527-6384 (1).jpg`
- dimensions: `4256x2832` RGB
- JPEG file size: `8,410,990` bytes

The full image is large enough that the current Python prototype would be slow for an exact full-frame baseline plus hard-gate pass. The test therefore used center crops at `1024x1024` and `2048x2048`. The `2048x2048` crop contains 4,194,304 pixels, four times the previous 1024 stress tests.

## Results

| crop | WebP lossless | E30 baseline | E30 hard moment | best E30 | best model | best vs WebP | WebP saving |
|---:|---:|---:|---:|---:|---|---:|---:|
| 1024x1024 | 1,210,060 | 1,173,635 | 1,173,956 | 1,173,635 | baseline | -36,425 | 3.010% |
| 2048x2048 | 4,841,382 | 4,572,054 | 4,569,640 | 4,569,640 | hard moment-context | -271,742 | 5.613% |

All E30 rows roundtripped exactly.

## Moment-Gate Behavior

At `1024x1024`, the hard moment gate is slightly worse than baseline:

\[
1{,}173{,}956 - 1{,}173{,}635 = 321 \text{ bytes}.
\]

At `2048x2048`, the hard moment gate becomes better than baseline:

\[
4{,}569{,}640 - 4{,}572{,}054 = -2{,}414 \text{ bytes}.
\]

This matches the E30/E31 diagnosis from the earlier panel. The moment split can be too expensive when contexts are not mature enough, but it becomes useful as the sample size grows. On this image, the larger crop gives the Hankel/moment boundary enough evidence to pay for itself.

The `2048x2048` moment class counts were:

```text
0: 15
1: 4,511,549
2: 8,071,348
```

where class `1` is nonnegative Hankel and class `2` is negative Hankel/barrier.

## Interpretation

This is the strongest large natural-photo test so far. E30 beats WebP lossless by `271,742` bytes on a `2048x2048` crop, a `5.613%` reduction, with exact reconstruction.

The result also reinforces why E31 is the right production direction. At 1024, a governed model would stay near baseline. At 2048, it would follow the hard moment gate after causal regret proves the split. The general compression lesson is not "always split by the Hankel class"; it is "make moment-boundary experts available, then admit them when they pay."

