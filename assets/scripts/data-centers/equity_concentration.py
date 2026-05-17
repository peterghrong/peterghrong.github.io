"""
Share of US corporate equities and mutual fund shares by wealth percentile.
Source: Federal Reserve Distributional Financial Accounts, Q1 2025.
"""
import os
import matplotlib.pyplot as plt
from _style import setup, BLACK, MUTED, ACCENT, HAIRLINE

setup()

groups = ["Bottom 50%", "50th–90th", "90th–99th", "Top 1%"]
shares = [1.0, 11.0, 38.0, 50.0]

fig, ax = plt.subplots(figsize=(7.5, 3.8))

bars = ax.barh(groups, shares, color=[HAIRLINE, HAIRLINE, MUTED, ACCENT],
               edgecolor=BLACK, linewidth=0.6, height=0.62)

for bar, share in zip(bars, shares):
    ax.text(
        share + 1.2, bar.get_y() + bar.get_height() / 2,
        f"{share:.0f}%",
        va="center", ha="left",
        color=BLACK, fontsize=11, fontweight="bold",
    )

ax.set_title("Half of US equities are owned by the top 1%")
ax.set_xlim(0, 60)
ax.set_xlabel("Share of US corporate equities and mutual fund shares")
ax.invert_yaxis()
ax.spines["bottom"].set_visible(False)
ax.tick_params(bottom=False, labelbottom=False)

fig.text(
    0.01, -0.02,
    "Source: Federal Reserve Distributional Financial Accounts, Q1 2025.",
    color=MUTED, fontsize=9,
)

out = os.path.join(
    os.path.dirname(__file__),
    "../../img/posts/data-centers/equity_concentration.png",
)
fig.savefig(os.path.abspath(out))
print("wrote", os.path.abspath(out))
