import pandas as pd
from scipy.stats import chi2_contingency
import sys

def chisq_ind(species, var):
    #data = pd.read_csv("df.csv")
    #contingency = pd.crosstab(data[var1], data[var2])
    #c, p, dof, expected = chi2_contingency(contingency)
    #print(contingency)
    #print("\n")
    #print("Test statistic: " + str(c) + "\n" + "P-value: " + str(p) + "\n" + "Degrees Freedom: " + str(dof))
    f = open("result.txt", "w+")
    f.write(species + "\n" + var)
    f.close()

chisq_ind(str(sys.argv[1]), str(sys.argv[2]))
