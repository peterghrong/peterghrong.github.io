"""
Median age of US operating companies at IPO, by decade.
Source: Jay Ritter, University of Florida, IPO Statistics dataset.
"""
import os
import matplotlib.pyplot as plt
from _style import setup, BLACK, MUTED, ACCENT

setup()

decades = ["1980s", "1990s", "2000s", "2010s", "2020-24"]
median_age = [6, 7, 9, 10, 12]

fig, ax = plt.subplots(figsize=(7.5, 4.0))

ax.plot(decades, median_age, color=BLACK, linewidth=2.0, marker="o",
        markersize=8, markerfacecolor=ACCENT, markeredgecolor=BLACK,
        markeredgewidth=1.0)

for x, y in zip(decades, median_age):
    ax.annotate(
        f"{y} yrs",
        xy=(x, y), xytext=(0, 12), textcoords="offset points",
        ha="center", color=BLACK, fontsize=10, fontweight="bold",
    )

ax.set_title("Companies are going public twice as old as in the 1980s")
ax.set_ylabel("Median age at IPO (years)")
ax.set_ylim(0, 16)
ax.spines["left"].set_visible(False)
ax.tick_params(left=False, labelleft=False)

fig.text(
    0.01, -0.02,
    "Source: Jay Ritter, U. Florida, IPO Statistics. Approximate decade medians.",
    color=MUTED, fontsize=9,
)

out = os.path.join(
    os.path.dirname(__file__),
    "../../img/posts/data-centers/age_at_ipo.png",
)
fig.savefig(os.path.abspath(out))
print("wrote", os.path.abspath(out))
