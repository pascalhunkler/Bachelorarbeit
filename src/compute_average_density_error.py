import sys

import numpy as np
import pandas as pd

if __name__ == "__main__":
    in_file = sys.argv[1]
    df = pd.read_csv(in_file, sep="\t")
    average_density = df["Durchschnittsdichte"]
    mean = average_density.mean()
    mad = average_density.mad()
    print("Mittelwert: " + str(mean))
    print("Durchschnittliche Abweichung: " + str(mad))
    #average_density = np.array(df["Durchschnittsdichte"])
    #average_density.