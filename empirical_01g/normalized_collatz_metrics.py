"""Standard-map normalized metrics; exact record comparisons and finite scope."""
import json
from pathlib import Path


def main():
    N = 1_000_000
    total = [0] * (N + 1)
    peak = [0] * (N + 1)
    peak[1] = 1
    records = {k: [] for k in ('peak_over_n', 'total_over_n', 'descent_over_n')}
    best = {k: (0, 1) for k in records}
    samples = []
    selected = {}
    for n in range(2, N + 1):
        z, count, high = n, 0, n
        while z >= n:
            z = 3*z+1 if z & 1 else z//2
            count += 1
            high = max(high, z)
            if count >= 100_000:
                raise RuntimeError(('No descent within cap', n))
        total[n] = count + total[z]
        peak[n] = max(high, peak[z])
        values = dict(peak_over_n=peak[n], total_over_n=total[n], descent_over_n=count)
        for name, value in values.items():
            bn, bd = best[name]
            if value*bd > bn*n:
                best[name] = value, n
                records[name].append(dict(n=n, numerator=value, ratio=value/n))
        if n in (3, 7, 27, 1819, 8191, 9663, 704511):
            selected[n] = dict(n=n, peak=peak[n], total_steps=total[n], first_descent_steps=count,
                               **{k:v/n for k,v in values.items()})
        if n <= 2000 or (n <= 100000 and n % 17 == 0) or n % 251 == 0:
            samples.append((n, peak[n]/n, total[n]/n, count/n))
    result = dict(map='standard: odd 3n+1; even n/2', limit=N,
                  convention='Transitions counted; stop at first 1; peak includes start; first descent is strictly below start.',
                  status='All seeds descended and reached 1 by induction on n.',
                  records=records, selected=selected)
    out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(dict(limit=N, selected=selected, records=records), indent=2))
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(3, 1, figsize=(10, 10), sharex=True, layout='constrained')
        labels = [('peak_over_n', 'Maximum value / start'), ('total_over_n', 'Total steps / start'),
                  ('descent_over_n', 'First-descent steps / start')]
        for i, (key, label) in enumerate(labels):
            ax = axes[i]
            ax.scatter([s[0] for s in samples], [s[i+1] for s in samples], s=3, alpha=.25, color='#527ea6')
            rec = records[key]
            ax.plot([r['n'] for r in rec]+[N], [r['ratio'] for r in rec]+[rec[-1]['ratio']],
                    drawstyle='steps-post', color='#c05030', lw=1.5, label='Running record (all seeds scanned)')
            v=selected[27][key]
            ax.scatter([27], [v], color='black', s=25, zorder=5)
            ax.annotate('27', (27,v), xytext=(7,7), textcoords='offset points')
            ax.set_ylabel(label); ax.set_yscale('log'); ax.grid(alpha=.15)
        axes[0].legend(fontsize=8)
        axes[0].set_title('Collatz ratios: early time peaks, but rising height records\nExact scan 2 ≤ n ≤ 1,000,000; points subsampled')
        axes[-1].set_xscale('log'); axes[-1].set_xlabel('Starting integer n (log scale)')
        fig.savefig(out.with_suffix('.png'), dpi=160)
        print('Plot:', out.with_suffix('.png'))
    except ImportError as exc:
        print('Plot unavailable:', str(exc))


if __name__ == '__main__':
    main()
