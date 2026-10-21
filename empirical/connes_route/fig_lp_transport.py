r"""
fig_lp_transport.py -- figure for N7 section 5 (Laguerre-Polya transport and the matched pair).

Reads the two certificate logs (probe_lp_transport_zeta_run.log and the DH log) and plots
(a) the order parameter sigma(lambda) = S(lambda)/(L^2/24) for zeta (bulk mode, sigma -> 0) and
Davenport-Heilbronn (bulk -> edge transition, sigma -> 3 = the cos(zL/2) value), and (b) the
Krein-Langer index of the DH form, annotated with the off-line quadruple each step resolves.
Run with the Python that has matplotlib:
    C:/Users/leomu/AppData/Local/Programs/Python/Python313/python.exe fig_lp_transport.py
"""
import os
import re
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullFormatter, FixedFormatter

HERE = r"C:/Projects/simplicial/empirical/connes_route/"


def parse_zeta(path):
    lam, sig = [], []
    for line in open(path, encoding="utf-8"):
        m = re.match(r"\s+(\d\.\d)\s+[\d.]+\s+\d+\s+\d+\s+\S+\s+\S+\s+\S+\s+[YN]\s+\S+.*sigma=(\S+)", line)
        if m:
            lam.append(float(m.group(1)))
            sig.append(float(m.group(2)))
    return lam, sig


def parse_dh(path):
    lam, sig, idx = [], [], []
    for line in open(path, encoding="utf-8"):
        m = re.match(r"\s+(\d+\.\d\d)\s+[\d.]+\s+\d+\s+\S+\s+\S+\s+\S+\s+\((\d+),(\d+)\)\s+[YN]\s+\S+\s+(\S+)", line)
        if m:
            lam.append(float(m.group(1)))
            idx.append(int(m.group(2)))
            sig.append(float(m.group(4)))
    return lam, sig, idx


def main():
    dh_log = HERE + "probe_lp_transport_dh_run.log"
    lz, sz = parse_zeta(HERE + "probe_lp_transport_zeta_run.log")
    ld, sd, idx = parse_dh(dh_log)
    if not lz or not ld:
        print("logs not parsed", len(lz), len(ld))
        return 1
    ticks = [1.5, 2, 3, 5, 7, 10, 20, 30]
    fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.0))
    a = ax[0]
    a.semilogy(lz, sz, "o-", color="#1f4e79", label=r"$\zeta$ (Euler product)")
    a.semilogy(ld, sd, "s-", color="#b03a2e", label="Davenport–Heilbronn")
    a.axhline(3.0, ls="--", lw=0.8, color="gray")
    a.text(1.35, 3.6, r"edge mode $\cos(zL/2)$: $\sigma=3$", fontsize=8, color="gray")
    a.set_xscale("log")
    a.xaxis.set_major_locator(FixedLocator(ticks))
    a.xaxis.set_major_formatter(FixedFormatter([str(t) for t in ticks]))
    a.xaxis.set_minor_formatter(NullFormatter())
    a.set_xlabel(r"$\lambda$  (window $[\lambda^{-1},\lambda]$)")
    a.set_ylabel(r"$\sigma(\lambda)=S(\lambda)\,/\,(L^2/24)$")
    a.set_title("(a) order parameter of the Weil ground state", fontsize=10)
    a.legend(fontsize=8, loc="lower right")
    b = ax[1]
    b.step(ld, idx, where="post", color="#b03a2e")
    b.plot(ld, idx, "s", color="#b03a2e", ms=4)
    b.set_xscale("log")
    b.xaxis.set_major_locator(FixedLocator(ticks[1:]))
    b.xaxis.set_major_formatter(FixedFormatter([str(t) for t in ticks[1:]]))
    b.xaxis.set_minor_formatter(NullFormatter())
    b.set_yticks([0, 1, 2, 3, 4])
    b.set_xlabel(r"$\lambda$")
    b.set_ylabel("negative directions (even sector)")
    b.set_title("(b) Davenport–Heilbronn: Krein–Langer index", fontsize=10)
    notes = [(5.75, 1, r"$T=85.70,\ \delta=0.31$"), (8.0, 2, r"$T=114.16,\ \delta=0.15$"),
             (10.0, 3, r"$T=176.70,\ \delta=0.22$"), (12.0, 4, r"$T=166.48,\ \delta=0.07$")]
    for x, y, t in notes:
        b.annotate(t, xy=(x, y), xytext=(x * 0.62 if x > 9 else x * 0.55, y + 0.25), fontsize=7.5,
                   arrowprops=dict(arrowstyle="-", lw=0.5, color="gray"))
    b.set_ylim(-0.2, 4.7)
    fig.tight_layout()
    out = HERE + "fig_lp_transport.png"
    fig.savefig(out, dpi=200)
    print("wrote", out, "from", os.path.basename(dh_log))
    return 0


if __name__ == "__main__":
    sys.exit(main())
