import matplotlib.pyplot as plt


def plot_heatmap(summary_df):
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