import pandas as pd

# Required columns expected in raw qPCR export file
REQUIRED_COLUMNS = [
    "Well",
    "Sample",
    "Group",
    "Target",
    "Ct",
    "Replicate"
]


def load_qpcr_data(file_path):
    """
    Load raw qPCR data from CSV and validate required columns.

    Parameters:
        file_path (str): Path to raw qPCR CSV file

    Returns:
        pandas.DataFrame: Validated qPCR dataset

    Raises:
        ValueError: If required columns are missing
    """
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