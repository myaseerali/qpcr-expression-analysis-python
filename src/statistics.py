import pandas as pd
from scipy.stats import ttest_ind


def summarize_fold_change(fold_change_df):
    """
    Calculate mean fold change for each study group.

    Parameters:
        fold_change_df (pandas.DataFrame):
            DataFrame containing fold change values.

    Returns:
        pandas.DataFrame:
            Group-wise mean fold change values.
    """

    summary_df = fold_change_df.groupby("Group")[
        ["FC_IFNG", "FC_IL2RA", "FC_TNFA"]
    ].mean()

    return summary_df


def perform_t_test(fold_change_df):
    """
    Perform independent t-tests between groups.

    Comparisons:
        1. Active_TB vs Control
        2. Latent_TB vs Control

    Parameters:
        fold_change_df (pandas.DataFrame):
            DataFrame containing fold change values.

    Returns:
        pandas.DataFrame:
            Table containing p-values for each gene.
    """

    active = fold_change_df[
        fold_change_df["Group"] == "Active_TB"
    ]

    control = fold_change_df[
        fold_change_df["Group"] == "Control"
    ]

    latent = fold_change_df[
        fold_change_df["Group"] == "Latent_TB"
    ]

    results = {}

    genes = ["FC_IFNG", "FC_IL2RA", "FC_TNFA"]

    for gene in genes:
        # Compare Active TB vs Control
        active_vs_control = ttest_ind(
            active[gene],
            control[gene]
        )

        # Compare Latent TB vs Control
        latent_vs_control = ttest_ind(
            latent[gene],
            control[gene]
        )

        results[gene] = {
            "Active_vs_Control_p": active_vs_control.pvalue,
            "Latent_vs_Control_p": latent_vs_control.pvalue
        }

    return pd.DataFrame(results).T