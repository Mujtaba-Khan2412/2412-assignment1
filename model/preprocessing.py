import pandas as pd


def load_and_clean_data(path="data/unique_dataset.csv"):
    df = pd.read_csv(path)
    # Minimal preprocessing: drop NaN
    df = df.dropna()
    return df
