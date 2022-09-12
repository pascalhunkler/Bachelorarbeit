import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd

import sys


if __name__ == "__main__":
    df_ssph = pd.read_csv("PlotFiles/stiffness_timestep_ssph.txt", sep="\t")

    x_ssph = df_ssph.columns[0]
    y_ssph = df_ssph.columns[1]

    plt.axhline(y=0.075, label="IISPH", color="tab:blue")
    plt.plot(df_ssph[x_ssph], df_ssph[y_ssph], label="SSPH", color="tab:orange")
    plt.scatter(df_ssph[x_ssph], df_ssph[y_ssph], color="tab:orange")
    plt.xscale("log")
    plt.legend()
    plt.xlabel(x_ssph)
    plt.ylabel(y_ssph)
    plt.savefig("Abbildungen/stiffness_timestep.png")