import pandas as pd


def load_data(file_path):
    """
    Load the bank customer churn dataset.
    """
    return pd.read_csv(file_path)