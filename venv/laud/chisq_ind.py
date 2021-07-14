import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import sys

def chisq_ind():
    data = pd.read_csv("laud/df.csv")
    data["present"] = np.array(["yes" for i in range(len(data))])
    data.loc[data["taxa_count"] == 0, ["present"]] = "no"
    contingency = pd.crosstab(data["cure_status"], data["present"])
    c, p, dof, expected = chi2_contingency(contingency)
    string = "Test statistic: " + str(c) + "\n" + "P-value: " + str(p) + "\n" + "Degrees Freedom: " + str(dof)
    f = open("laud/result.txt", "w+")
    f.write(str(contingency))
    f.write("\n"+ string)
    f.close()

chisq_ind()
