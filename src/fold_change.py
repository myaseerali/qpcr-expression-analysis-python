import numpy as np


def calculate_fold_change(ddct_df):
    """
    Calculate relative gene expression (fold change)
    using the 2^(-ddCt) method.

    Formula:
        Fold Change = 2^(-ddCt)

    Interpretation:
        Fold Change > 1  → Upregulated gene expression
        Fold Change = 1  → No expression change
        Fold Change < 1  → Downregulated gene expression

    Parameters:
        ddct_df (pandas.DataFrame):
            DataFrame containing delta-delta Ct values.

    Returns:
        pandas.DataFrame:
            Original DataFrame with fold change columns added.
    """

    result = ddct_df.copy()

    result["FC_IFNG"] = np.power(2, -result["ddCt_IFNG"])
    result["FC_IL2RA"] = np.power(2, -result["ddCt_IL2RA"])
    result["FC_TNFA"] = np.power(2, -result["ddCt_TNFA"])

    return result