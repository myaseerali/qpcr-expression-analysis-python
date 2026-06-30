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
            p_values_df.loc["FC_IFNG", "Active_vs_Control_p"],
            p_values_df.loc["FC_IL2RA", "Active_vs_Control_p"],
            p_values_df.loc["FC_TNFA", "Active_vs_Control_p"]
        ]
    })

    report_df["Significant"] = report_df["P_Value"] < 0.05

    return report_df