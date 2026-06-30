import matplotlib.pyplot as plt


def plot_heatmap(summary_df):
    """
    Plot heatmap of mean fold change values.

    Parameters:
        summary_df (pandas.DataFrame):
            DataFrame containing group-wise mean fold changes.

    Saves:
        results/heatmap.png
    """

    genes = ["FC_IFNG", "FC_IL2RA", "FC_TNFA"]
    groups = summary_df.index.tolist()

    data = summary_df[genes].values

    plt.figure(figsize=(6, 4))
    plt.imshow(data, aspect="auto")
    plt.colorbar(label="Fold Change")

    plt.xticks(range(len(genes)), genes)
    plt.yticks(range(len(groups)), groups)

    plt.title("Gene Expression Heatmap")
    plt.tight_layout()

    plt.savefig("results/heatmap.png")
    plt.show()