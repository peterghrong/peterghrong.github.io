"""
Cumulative US CPI-U since 2000, indexed to 100.
Source: BLS CPI-U annual averages (bls.gov/cpi).
"""
import os
import matplotlib.pyplot as plt
from _style import setup, BLACK, MUTED, ACCENT

setup()

YEARS = list(range(2000, 2026))
CPI = [
    172.2, 177.1, 179.9, 184.0, 188.9,
    195.3, 201.6, 207.3, 215.3, 214.5,
    218.1, 224.9, 229.6, 233.0, 236.7,
    237.0, 240.0, 245.1, 251.1, 255.7,
    258.8, 271.0, 292.7, 304.7, 313.7,
    322.5,
]
base = CPI[0]
index = [v / base * 100 for v in CPI]

fig, ax = plt.subplots(figsize=(7.5, 4.2))
ax.plot(YEARS, index, color=BLACK, linewidth=2.2)
ax.fill_between(YEARS, 100, index, color=ACCENT, alpha=0.08)

ax.axhline(100, color=MUTED, linewidth=0.8, linestyle="--")

ax.set_title("$1 in 2000 buys $0.53 of goods today")
ax.set_ylabel("CPI-U, 2000 = 100")
ax.set_xlim(2000, 2025)
ax.set_ylim(95, 200)

end_val = index[-1]
ax.annotate(
    f"{end_val:.0f}",
    xy=(YEARS[-1], end_val),
    xytext=(6, 0),
    textcoords="offset points",
    color=BLACK,
    fontsize=11,
    fontweight="bold",
    va="center",
)

fig.text(
    0.01, -0.02,
    "Source: BLS CPI-U, annual average. 2025 is YTD estimate.",
    color=MUTED, fontsize=9,
)

out = os.path.join(
    os.path.dirname(__file__),
    "../../img/posts/data-centers/cumulative_inflation.png",
)
fig.savefig(os.path.abspath(out))
print("wrote", os.path.abspath(out))
