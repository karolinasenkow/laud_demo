import pandas as pd
import numpy as np

df = pd.read_csv("laud/df.csv") #df has only sample id, species, and count columns

first_sample = df.iloc[0][0]
species_cols = df[df["sample_id"] == first_sample]["taxa_name"].tolist()
new_columns = ["sample_id"] + species_cols 
unique_samples = np.unique(df["sample_id"]).tolist()

heat_df = pd.DataFrame(columns = new_columns)
for sample in unique_samples:
    new_row1 = pd.DataFrame()
    new_row1["sample_id"] = [sample]
    tab = df[df["sample_id"] == sample]
    tab = tab.drop(["sample_id"], axis = 1)
    new_row2 = tab.transpose()
    new_header = new_row2.iloc[0]
    new_row2 = new_row2[1:]
    new_row2.columns = new_header.values
    new_row2 = new_row2.reset_index(drop = True)
    new_row = pd.concat([new_row1, new_row2], axis = 1)
    heat_df = heat_df.append(new_row)
heat_df = heat_df.reset_index(drop = True)


heat_df.to_csv("laud/heat_df.csv", index = False)
