"""Reproduce the two-round baseline illustration used in slides.md."""

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/lse-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(__file__).resolve().parents[1] / "images"
OUTPUT.mkdir(exist_ok=True)

# Illustrative parameters, not empirical estimates. Both rounds use positive AI.
gamma = tau_v = tau_u = learning = 1.0
ai_price = 0.1
depreciation = 0.5
capital_1 = 8.0

precision = gamma**2 / (2 * tau_u) * (
    np.sqrt(1 + 4 * tau_u / gamma**2 * (1 / (2 * gamma * ai_price) - tau_v)) - 1
)
rho = 1 - depreciation + learning * ai_price * (1 + learning * ai_price / 2)
capital_2 = rho * capital_1
human = np.array([capital_1 * ai_price * (1 + learning * ai_price / 2), ai_price * capital_2])
ai = precision - human
price_precision = tau_u * precision**2 / gamma**2
assert ai.min() > 0 and capital_2 < capital_1

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titleweight": "bold",
    "svg.fonttype": "none",
})
fig, axes = plt.subplots(1, 2, figsize=(10, 3.3), gridspec_kw={"width_ratios": [1.2, 1]})
positions = np.arange(2)
human_color, ai_color = "#3333B3", "#BDBDEE"

axes[0].bar(positions, human / precision * 100, width=0.52, color=human_color, label="Cognitive effort")
axes[0].bar(positions, ai / precision * 100, bottom=human / precision * 100, width=0.52,
            color=ai_color, label="AI")
for index, share in enumerate(human / precision * 100):
    axes[0].text(index, share / 2, f"{share:.0f}%", ha="center", va="center", color="white", weight="bold")
    axes[0].text(index, share + (100 - share) / 2, f"{100 - share:.0f}%", ha="center", va="center",
                 color="#252567", weight="bold")
axes[0].set(xticks=positions, xticklabels=["Round 1", "Round 2"], ylim=(0, 108), yticks=[0, 50, 100],
            ylabel="Share of private precision (%)", title="Who produces the information?")
axes[0].legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=False, fontsize=11)

axes[1].bar(positions, [100, 100 * rho], width=0.52, color=human_color)
for index, value in enumerate([100, 100 * rho]):
    axes[1].text(index, value + 3, f"{value:.1f}".rstrip("0").rstrip("."), ha="center", weight="bold")
axes[1].set(xticks=positions, xticklabels=["Round 1", "Round 2"], ylim=(0, 115), yticks=[0, 50, 100],
            ylabel="Cognitive capital (initial = 100)", title="The human capacity underneath")

for axis in axes:
    axis.set_axisbelow(True)
    axis.grid(axis="y", alpha=0.15)
    axis.spines["left"].set_color("#cccccc")
    axis.spines["bottom"].set_color("#cccccc")
    axis.tick_params(axis="both", length=0)

fig.tight_layout(w_pad=3)
fig.savefig(OUTPUT / "cognitive-capital-baseline.svg", bbox_inches="tight", transparent=True)
fig.savefig(OUTPUT / "cognitive-capital-baseline.pdf", bbox_inches="tight", transparent=True)
plt.close(fig)
print(f"Private precision = {precision:.6f}; price precision = {price_precision:.6f} in both rounds.")
print(f"Human precision: {human}; AI precision: {ai}; capital: {capital_1} -> {capital_2}.")
