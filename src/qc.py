def check_replicate_quality(df, threshold=1.0):
    """
    Check quality of technical replicates using Ct spread.

    The function groups qPCR data by Sample and Target,
    then calculates Ct spread (maximum Ct - minimum Ct)
    across replicates.

    Parameters:
        df (pandas.DataFrame):
            Raw qPCR dataset containing Sample, Target, and Ct columns.

        threshold (float, optional):
            Maximum allowed Ct spread between replicates.
            Default is 1.0.

    Returns:
        list:
            A list of dictionaries containing failed replicate groups.
            Each dictionary contains:
                - Sample
                - Target
                - Spread
    """

    bad_groups = []

    grouped = df.groupby(["Sample", "Target"])

    for (sample, target), group in grouped:

        # Spread = max Ct - min Ct among technical replicates
        ct_spread = group["Ct"].max() - group["Ct"].min()

        if ct_spread > threshold:
            bad_groups.append(
                {
                    "Sample": sample,
                    "Target": target,
                    "Spread": ct_spread
                }
            )

    return bad_groups