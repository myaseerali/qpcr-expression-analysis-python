import pandas as pd

def create_report(summary_df, p_values_df):
    report_df = pd.DataFrame({
        "Gene": ["IFNG", "IL2RA", "TNFA"],
        "Fold_Change": [
            summary_df.loc["Active_TB", "FC_IFNG"],
            summary_df.loc["Active_TB", "FC_IL2RA"],
            summary_df.loc["Active_TB", "FC_TNFA"]
        ],
        "P_Value": [
            p_values_df.loc[0, "IFNG_pvalue"],
            p_values_df.loc[0, "IL2RA_pvalue"],
            p_values_df.loc[0, "TNFA_pvalue"]
        ]
    })

    report_df["Significant"] = report_df["P_Value"] < 0.05

    return report_df