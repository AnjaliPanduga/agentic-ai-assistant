import pandas as pd

def analyze_data(file):

    df = pd.read_csv(file)

    summary = {
        "Shape": df.shape,
        "Columns": list(df.columns),
        "Missing Values": df.isnull().sum().to_dict()
    }

    return summary