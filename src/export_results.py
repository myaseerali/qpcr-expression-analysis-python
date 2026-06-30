def export_results(fold_change_df, summary_df, p_values_df, report_df):
    fold_change_df.to_csv("results/fold_change_results.csv", index=False)
    summary_df.to_csv("results/group_summary.csv")
    p_values_df.to_csv("results/statistical_results.csv", index=False)
    report_df.to_csv("results/final_report.csv", index=False)

    print()
    print("Results exported successfully to results folder")