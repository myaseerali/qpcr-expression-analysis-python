import pandas as pd


REQUIRED_COLUMNS = [
    "Well",
    "Sample",
    "Group",
    "Target",
    "Ct",
    "Replicate"
]


def load_qpcr_data(file_path):
    df = pd.read_csv(file_path)

    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    return df