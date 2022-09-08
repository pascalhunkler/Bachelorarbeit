import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd

import sys


if __name__ == "__main__":
    in_files = sys.argv[1:-1]
    out_file = sys.argv[-1]

    for in_file in in_files:
        df = pd.read_csv(in_file, sep="\t")
        plt.plot(df["Iteration"], df["Durchschnittsdichte"])
    plt.xlabel("Iteration")
    plt.ylabel("Durchschnittsdichte")
    plt.savefig(out_file)