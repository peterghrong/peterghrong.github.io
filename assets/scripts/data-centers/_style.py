"""Shared matplotlib styling for data-center post charts."""
import matplotlib.pyplot as plt

BLACK = "#0a0a0a"
MUTED = "#6b6b66"
HAIRLINE = "#cfccc1"
CREAM = "#fdfdfb"
ACCENT = "#b8442b"


def setup():
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Iowan Old Style", "Charter", "Palatino", "Georgia", "serif"],
        "font.size": 11,
        "axes.edgecolor": BLACK,
        "axes.labelcolor": BLACK,
        "axes.titlesize": 13,
        "axes.titleweight": "semibold",
        "axes.titlepad": 16,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "figure.facecolor": CREAM,
        "axes.facecolor": CREAM,
        "savefig.facecolor": CREAM,
        "savefig.dpi": 180,
        "savefig.bbox": "tight",
        "text.parse_math": False,
    })
