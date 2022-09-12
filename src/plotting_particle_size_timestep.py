import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd

import sys


if __name__ == "__main__":
    df_iisph = pd.read_csv("PlotFiles/particle_size_timestep_iisph.txt", sep="\t")
    df_ssph = pd.read_csv("PlotFiles/particle_size_timestep_ssph.txt", sep="\t")

    x_iisph = df_iisph.columns[0]
    y_iisph = df_iisph.columns[1]

    x_ssph = df_ssph.columns[0]
    y_ssph = df_ssph.columns[1]

    plt.plot(df_iisph[x_iisph], df_iisph[y_iisph], label="IISPH")
    plt.scatter(df_iisph[x_iisph], df_iisph[y_iisph])
    plt.plot(df_ssph[x_ssph], df_ssph[y_ssph], label="SSPH")
    plt.scatter(df_ssph[x_ssph], df_ssph[y_ssph])
    plt.legend()
    plt.xlabel(x_iisph)
    plt.ylabel(y_iisph)
    plt.savefig("Abbildungen/particle_size_timestep.png")