import pandas as pd
from scipy.stats import ttest_ind


def summarize_fold_change(fold_change_df):
    summary_df = fold_change_df.groupby("Group")[
        ["FC_IFNG", "FC_IL2RA", "FC_TNFA"]
    ].mean()

    return summary_df


def perform_t_test(fold_change_df):
    active = fold_change_df[fold_change_df["Group"] == "Active_TB"]
    control = fold_change_df[fold_change_df["Group"] == "Control"]
    latent = fold_change_df[fold_change_df["Group"] == "Latent_TB"]

    results = {}

    genes = ["FC_IFNG", "FC_IL2RA", "FC_TNFA"]

    for gene in genes:
        active_vs_control = ttest_ind(active[gene], control[gene])
        latent_vs_control = ttest_ind(latent[gene], control[gene])

        results[gene] = {
            "Active_vs_Control_p": active_vs_control.pvalue,
            "Latent_vs_Control_p": latent_vs_control.pvalue
        }

    return pd.DataFrame(results).T