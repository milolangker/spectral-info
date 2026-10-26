""" jatis style figures.
5.25 inch width.
"""

import os

import matplotlib.pyplot as plt

FIG_WIDTH = 5.25 # from measured pdf widths
FONT_SIZE = 8 # jatis minimum 
LINEWIDTH = 0.5 # nice width

PREAMBLE = r"""
\usepackage[T1]{fontenc}
\usepackage{newtxtext,newtxmath}
"""

RC = {
    "text.usetex": True,
    "font.family": "serif",
    "text.latex.preamble": PREAMBLE,

    "font.size": FONT_SIZE,
    "axes.labelsize": FONT_SIZE,
    "axes.titlesize": FONT_SIZE,
    "xtick.labelsize": FONT_SIZE,
    "ytick.labelsize": FONT_SIZE,
    "legend.fontsize": FONT_SIZE,
    "legend.title_fontsize": FONT_SIZE,
    "figure.titlesize": FONT_SIZE,

    "axes.linewidth": LINEWIDTH,
    "xtick.major.width": LINEWIDTH,
    "ytick.major.width": LINEWIDTH,
    "xtick.minor.width": 0.4,
    "ytick.minor.width": 0.4,
    "xtick.major.size": 3.0,
    "ytick.major.size": 3.0,
    "xtick.minor.size": 1.75,
    "ytick.minor.size": 1.75,

    "figure.dpi": 300,
    "savefig.bbox": None,

    # pdf export that doesn't break minus signs
    "pgf.texsystem": "pdflatex",
    "pgf.rcfonts": False,
    "pgf.preamble": PREAMBLE,
}

# white box behind a panel label so dashed lines etc. don't cut through it
LABEL_BBOX = dict(boxstyle="square,pad=0.1", facecolor="white", edgecolor="none")


def apply():
    """Put LaTeX on the PATH and update matplotlib's rcParams."""
    texbin = "/Library/TeX/texbin"
    if texbin not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] = texbin + os.pathsep + os.environ["PATH"]
    plt.rcParams.update(RC)


def panel_label(ax, letter, x=0.008, y=0.96, ha="left", va="top", **kwargs):
    """Write a JATIS panel label, e.g. "(a)", at (x, y) in axes coordinates."""
    kwargs.setdefault("transform", ax.transAxes)
    return ax.text(x, y, f"({letter})", ha=ha, va=va, **kwargs)
