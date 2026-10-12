"""Illustrate CES substitution with equal-output curves in three limiting cases."""

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/lse-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "images"
OUTPUT.mkdir(exist_ok=True)

# With omega=1/2, every curve below has output q=1 and passes through (1,1).
# The theta=0 aggregator is interpreted as its Cobb-Douglas limit.
assert np.isclose(np.sqrt(0.5 * 2), 1)
assert np.isclose((0.5 + 1.5) / 2, 1)
assert min(0.5, 2) < 1  # Extra infrastructure cannot compensate in fixed proportions.

BLUE, TEAL, GREY, RED = "#3333B3", "#087F8C", "#64748B", "#B64B38"
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titleweight": "bold",
    "svg.fonttype": "path",
})

fig, axes = plt.subplots(1, 3, figsize=(12, 3.3))
fig.subplots_adjust(left=0.062, right=0.99, top=0.73, bottom=0.24, wspace=0.31)
titles = ["Fixed proportions", "Some substitution", "Perfect substitutes"]
parameters = [
    r"$\theta\to-\infty\quad\varsigma\to0$",
    r"$\theta\to0\quad\varsigma\to1$",
    r"$\theta\to1^{-}\quad\varsigma\to\infty$",
]
captions = [
    "Halving tokens: impossible",
    "Halving tokens: infrastructure = 2",
    "Halving tokens: infrastructure = 1.5",
]

for index, axis in enumerate(axes):
    axis.set(xlim=(0, 2.3), ylim=(0, 2.3), xticks=[0, 0.5, 1, 2], yticks=[0, 1, 2])
    axis.set_xlabel("AI tokens", labelpad=3, fontsize=12)
    axis.set_title(titles[index], pad=31, fontsize=15)
    axis.text(0.5, 1.055, parameters[index], transform=axis.transAxes,
              ha="center", va="bottom", fontsize=13, color=BLUE)
    axis.text(0.5, -0.29, captions[index], transform=axis.transAxes,
              ha="center", va="top", fontsize=12, color=RED if index == 0 else TEAL)
    axis.axvline(0.5, color=GREY, lw=1, ls=(0, (3, 4)), alpha=0.45)
    axis.scatter([1], [1], color=GREY, s=30, zorder=5)
    axis.spines["left"].set_color("#A6AFBC")
    axis.spines["bottom"].set_color("#A6AFBC")
    axis.tick_params(length=0, labelsize=10, pad=3)
    axis.set_axisbelow(True)
    axis.grid(alpha=0.1)

axes[0].set_ylabel("Infrastructure", labelpad=6, fontsize=12)
axes[0].plot([1, 1, 2.3], [2.3, 1, 1], color=BLUE, lw=3, solid_capstyle="round")
axes[0].scatter([0.5], [1], color=RED, marker="x", s=55, linewidths=2, zorder=6)
axes[0].annotate("", xy=(0.56, 1), xytext=(0.92, 1),
                 arrowprops={"arrowstyle": "->", "color": RED, "lw": 1.5})

tokens = np.linspace(1 / 2.3, 2.3, 400)
axes[1].plot(tokens, 1 / tokens, color=BLUE, lw=3, solid_capstyle="round")
axes[1].scatter([0.5], [2], color=TEAL, s=45, zorder=6)
axes[1].hlines(2, 0, 0.5, color=TEAL, lw=1, ls=(0, (3, 4)), alpha=0.7)
axes[1].annotate("", xy=(0.62, 1 / 0.62), xytext=(0.79, 1 / 0.79),
                 arrowprops={"arrowstyle": "->", "color": TEAL, "lw": 2})

tokens = np.linspace(0, 2, 200)
axes[2].plot(tokens, 2 - tokens, color=BLUE, lw=3, solid_capstyle="round")
axes[2].scatter([0.5], [1.5], color=TEAL, s=45, zorder=6)
axes[2].hlines(1.5, 0, 0.5, color=TEAL, lw=1, ls=(0, (3, 4)), alpha=0.7)
axes[2].annotate("1.5", (0, 1.5), xytext=(-7, 0), textcoords="offset points",
                 ha="right", va="center", fontsize=10, color=TEAL)
axes[2].annotate("", xy=(0.62, 1.38), xytext=(0.83, 1.17),
                 arrowprops={"arrowstyle": "->", "color": TEAL, "lw": 2})

fig.savefig(OUTPUT / "ces-substitution.svg", transparent=True)
fig.savefig(OUTPUT / "ces-substitution.pdf", transparent=True)
fig.savefig("/tmp/lse-ces-substitution-preview.png", dpi=180, facecolor="white")
plt.close(fig)
print("Generated equal-output CES curves, normalized to omega=1/2 and q=1.")
