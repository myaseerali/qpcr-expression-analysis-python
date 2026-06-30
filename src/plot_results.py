import matplotlib.pyplot as plt


def plot_fold_change(fold_change_df):
    mean_ifng = fold_change_df["FC_IFNG"].mean()
    mean_il2ra = fold_change_df["FC_IL2RA"].mean()
    mean_tnfa = fold_change_df["FC_TNFA"].mean()

    genes = ["IFNG", "IL2RA", "TNFA"]
    values = [mean_ifng, mean_il2ra, mean_tnfa]

    plt.figure(figsize=(8, 5))
    plt.bar(genes, values)

    plt.title("Mean Fold Change in Active TB")
    plt.xlabel("Genes")
    plt.ylabel("Fold Change")

    plt.savefig("results/fold_change_plot.png")
    plt.show()