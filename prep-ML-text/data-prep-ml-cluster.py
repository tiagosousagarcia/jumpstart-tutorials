import pandas as pd

DIR_NAME = "prep-ML-text/obs_subset/"

df_full = pd.read_csv("prep-ML-text/subset_obv_words_v2_28-01-2017.tsv", sep="\t")

ids = df_full['obo_trial'].unique().tolist()

for id in ids:
    df_single_trial = df_full[df_full['obo_trial'] == id]

    text = df_single_trial['words'].values.tolist()

    file_name = id + ".txt"

    with open(DIR_NAME + file_name, "w") as file:
        for line in text:
            file.write(line + "\n")
