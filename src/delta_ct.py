# def calculate_mean_ct(df):
#     mean_ct = (
#         df.groupby(["Sample", "Group", "Target"])["Ct"]
#         .mean()
#         .reset_index()
#     )

#     mean_ct.rename(columns={"Ct": "Mean_Ct"}, inplace=True)

#     return mean_ct

def calculate_mean_ct(df):
    mean_ct = (
        df.groupby(["Sample", "Group", "Target"])["Ct"]
        .mean()
        .reset_index()
    )

    mean_ct.rename(columns={"Ct": "Mean_Ct"}, inplace=True)

    return mean_ct


def calculate_delta_ct(mean_ct_df):
    pivot_df = mean_ct_df.pivot(
        index=["Sample", "Group"],
        columns="Target",
        values="Mean_Ct"
    ).reset_index()

    pivot_df["dCt_IFNG"] = pivot_df["IFNG"] - pivot_df["GAPDH"]
    pivot_df["dCt_IL2RA"] = pivot_df["IL2RA"] - pivot_df["GAPDH"]
    pivot_df["dCt_TNFA"] = pivot_df["TNFA"] - pivot_df["GAPDH"]

    return pivot_df

def calculate_delta_delta_ct(delta_ct_df):
    control_df = delta_ct_df[delta_ct_df["Group"] == "Control"]

    control_means = {
        "IFNG": control_df["dCt_IFNG"].mean(),
        "IL2RA": control_df["dCt_IL2RA"].mean(),
        "TNFA": control_df["dCt_TNFA"].mean()
    }

    delta_ct_df["ddCt_IFNG"] = (
        delta_ct_df["dCt_IFNG"] - control_means["IFNG"]
    )

    delta_ct_df["ddCt_IL2RA"] = (
        delta_ct_df["dCt_IL2RA"] - control_means["IL2RA"]
    )

    delta_ct_df["ddCt_TNFA"] = (
        delta_ct_df["dCt_TNFA"] - control_means["TNFA"]
    )

    return delta_ct_df