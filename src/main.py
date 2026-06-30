# from data_loader import load_qpcr_data


# def main():
#     file_path = "data/raw/tb_qpcr_export.csv"

#     df = load_qpcr_data(file_path)

#     print("Data loaded successfully")
#     print()
#     print("Shape:", df.shape)
#     print()
#     print(df.head())


# if __name__ == "__main__":
#     main()



# from data_loader import load_qpcr_data
# from qc import check_replicate_quality


# def main():
#     file_path = "data/raw/tb_qpcr_export.csv"

#     df = load_qpcr_data(file_path)
    
#     bad_groups = check_replicate_quality(df, threshold=1.0)
    
#     print("QC RESULTS")
#     print()

#     if len(bad_groups) == 0:
#         print("All technical replicates passed QC")
#     else:
#         print("Failed replicates:")
#         for group in bad_groups:
#             print(group)


# if __name__ == "__main__":
#     main()
from plot_results import plot_fold_change
from fold_change import calculate_fold_change
from statistics import summarize_fold_change, perform_t_test
from report import create_report
from export_results import export_results
from data_loader import load_qpcr_data
from qc import check_replicate_quality
from delta_ct import (
    calculate_mean_ct,
    calculate_delta_ct,
    calculate_delta_delta_ct
)


def main():
    file_path = "data/raw/tb_qpcr_export.csv"

    # Load data
    df = load_qpcr_data(file_path)

    # QC check
    bad_groups = check_replicate_quality(df, threshold=1.0)

    print("QC RESULTS")
    print()

    if len(bad_groups) == 0:
        print("All technical replicates passed QC")
    else:
        print("Failed replicates:")
        for group in bad_groups:
            print(group)

    # Mean Ct
    print()
    print("MEAN CT VALUES")
    print()

    mean_ct_df = calculate_mean_ct(df)
    print(mean_ct_df.head(12))

    # Delta Ct
    delta_ct_df = calculate_delta_ct(mean_ct_df)

    print()
    print("DELTA CT VALUES")
    print()

    print(
        delta_ct_df[
            ["Sample", "Group", "dCt_IFNG", "dCt_IL2RA", "dCt_TNFA"]
        ].head()
    )

    # Delta Delta Ct
    ddct_df = calculate_delta_delta_ct(delta_ct_df)

    print()
    print("DELTA DELTA CT VALUES")
    print()

    print(
        ddct_df[
            ["Sample", "Group", "ddCt_IFNG", "ddCt_IL2RA", "ddCt_TNFA"]
        ].head()
    )

    # Fold Change
    fold_change_df = calculate_fold_change(ddct_df)

    print()
    print("FOLD CHANGE VALUES")
    print()
    
    print()
    print("FOLD CHANGE DATAFRAME")
    print()

    print(fold_change_df.head())
    
    print(
        fold_change_df[
            ["Sample", "Group", "FC_IFNG", "FC_IL2RA", "FC_TNFA"]
        ].head()
    )
    plot_fold_change(fold_change_df)
    
    summary_df = summarize_fold_change(fold_change_df)

    print()
    print("GROUP SUMMARY")
    print()

    print(summary_df)

    p_values_df = perform_t_test(fold_change_df)

    print()
    print("STATISTICAL TEST RESULTS")
    print()

    print(p_values_df)
    report_df = create_report(summary_df, p_values_df)

    print()
    print("FINAL REPORT")
    print()

    print(report_df)
    export_results(
    fold_change_df,
    summary_df,
    p_values_df,
    report_df
)

if __name__ == "__main__":
    main()
    