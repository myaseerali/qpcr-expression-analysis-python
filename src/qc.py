def check_replicate_quality(df, threshold=0.5):
    grouped = df.groupby(["Sample", "Target"])

    bad_groups = []

    for (sample, target), group in grouped:
        ct_values = group["Ct"]

        spread = ct_values.max() - ct_values.min()

        if spread > threshold:
            bad_groups.append({
                "Sample": sample,
                "Target": target,
                "Spread": spread
            })

    return bad_groups