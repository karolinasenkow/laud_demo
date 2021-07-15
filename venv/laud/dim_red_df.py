import pandas as pd
import numpy as np

df = pd.read_csv("laud/df.csv")
first_column = df.pop("cure_status")
df.insert(0, "cure_status", first_column)
first_sample = df.iloc[0][1]
species_cols = df[df["sample_id"] == first_sample]["taxa_name"].tolist()
new_columns = ["cure_status", "sample_id"] + species_cols
unique_samples = np.unique(df["sample_id"]).tolist()

dim_df = pd.DataFrame(columns = new_columns)
for sample in unique_samples:
    new_row = pd.DataFrame()
    result = df.isin([sample])
    row_index = list(result["sample_id"][result["sample_id"] == True].index)[0]
    new_row["cure_status"] = [df.iloc[row_index][0]]
    new_row["sample_id"] = [sample]
    tab = df[df["sample_id"] == sample]
    for i in range(len(tab)):
        row = tab.iloc[i]
        species = [row[2]]
        count = [row[3]]
        new_row[species] = [count]
    dim_df = dim_df.append(new_row)
dim_df = dim_df.reset_index(drop = True)

dim_df.to_csv("laud/dim_df.csv", index = False)

