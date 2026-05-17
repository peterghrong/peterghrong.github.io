"""
Latest private-market valuations of companies still not public.
Public investors hold zero direct equity in any of these.
Source: company funding rounds and secondary marks, 2024-2025.
"""
import os
import matplotlib.pyplot as plt
from _style import setup, BLACK, MUTED, ACCENT, HAIRLINE

setup()

companies = ["Databricks", "Stripe", "SpaceX", "OpenAI"]
valuations = [134, 106, 400, 500]  # $B

fig, ax = plt.subplots(figsize=(7.5, 3.8))

bars = ax.barh(companies, valuations, color=ACCENT, edgecolor=BLACK,
               linewidth=0.6, height=0.6)

for bar, v in zip(bars, valuations):
    ax.text(
        v + 8, bar.get_y() + bar.get_height() / 2,
        f"${v}B",
        va="center", ha="left",
        color=BLACK, fontsize=11, fontweight="bold",
    )

ax.set_title("$1.1 trillion of value, locked in the private market")
ax.set_xlim(0, 600)
ax.set_xlabel("Latest private valuation (USD billions)")
ax.invert_yaxis()
ax.spines["bottom"].set_visible(False)
ax.tick_params(bottom=False, labelbottom=False)

fig.text(
    0.01, -0.02,
    "Source: company funding rounds and secondary-market valuations, 2024-25.",
    color=MUTED, fontsize=9,
)

out = os.path.join(
    os.path.dirname(__file__),
    "../../img/posts/data-centers/private_valuations.png",
)
fig.savefig(os.path.abspath(out))
print("wrote", os.path.abspath(out))
