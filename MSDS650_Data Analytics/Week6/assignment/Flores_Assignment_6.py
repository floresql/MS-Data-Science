# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.22.0",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.4",
#     "pandas>=3.0.2",
#     "scikit-learn>=1.8.0",
# ]
# ///

import marimo

__generated_with = "0.23.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 6 Assignment: Unsupervised Machine Learning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dataset: Wikipedia Trending Articles

    **Source:** `wikipedia_trending.json`

    Each record is one Wikipedia article that appeared in the top-100 most-viewed pages during the collection window.
    The dataset contains 500 articles with the following fields:

    | Column | Description |
    |:-------|:------------|
    | `title` | Article title |
    | `total_views` | Total page views across all tracked days |
    | `days_in_top_100` | How many days the article ranked in the top 100 |
    | `peak_views` | Single highest-day view count |
    | `daily_views` | List of per-day view counts (dropped before modeling) |

    **Goal:** Use K-Means to discover natural groupings among trending articles
    based on their attention patterns, then visualize the clusters with PCA.
    """)
    return


@app.cell
def _():
    import json
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    from sklearn.decomposition import PCA
    from sklearn import metrics
    import marimo as mo

    return KMeans, PCA, json, metrics, mo, np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Load and Inspect the Data
    """)
    return


@app.cell
def _(json, pd):
    with open('wikipedia_trending.json') as f:
        wiki_trending = json.load(f)

    df_raw = pd.DataFrame(wiki_trending)
    print("Shape:", df_raw.shape)
    print()
    print(df_raw.dtypes)
    return (df_raw,)


@app.cell
def _(df_raw):
    df_raw.head(5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Cleaning and Feature Engineering

    **Assumptions and decisions:**

    - `daily_views` is a list column, it cannot be used directly by K-Means, so it is dropped.
    - `title` is a string identifier with no numeric meaning for clustering, so it is also dropped.
    - There are no missing values in the numeric columns (confirmed below).
    - A derived feature `peak_ratio` is added: `peak_views / total_views`.
      A high ratio means one huge day dominated; a low ratio means views were spread out.
    - All three numeric features are on very different scales (views in the millions vs.
      days in the single digits), so **normalizing is necessary** before K-Means.
    """)
    return


@app.cell
def _(df_raw):
    df = df_raw.drop(columns=['daily_views'])
    df['peak_ratio'] = df['peak_views'] / df['total_views']
    print("Null values:")
    print(df.isnull().sum())
    return (df,)


@app.cell
def _(df):
    df.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## EDA: Explore the Numeric Features

    Before clustering, it helps to look at distributions and relationships between features.
    """)
    return


@app.cell
def _(df, plt):
    features = ['total_views', 'days_in_top_100', 'peak_views', 'peak_ratio']

    fig_eda, axes_eda = plt.subplots(1, 4, figsize=(16, 4))
    for i, col in enumerate(features):
        axes_eda[i].hist(df[col], bins=30, color='steelblue', edgecolor='white')
        axes_eda[i].set_title(col)
        axes_eda[i].set_xlabel('Value')
        axes_eda[i].set_ylabel('Count')
    plt.suptitle('Feature Distributions (raw)', fontsize=13)
    plt.tight_layout()
    plt.show()
    return (features,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All four features are right-skewed, a small number of articles have extremely high
    view counts or very long streaks in the top 100. This confirms that normalizing
    (standardizing) before K-Means is the right call.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Normalize the Features

    Subtract the column mean and divide by the standard deviation (z-score normalization).
    """)
    return


@app.cell
def _(df, features, np):
    X = df[features].copy()
    X_mean = X.mean()
    X_std = X.std()
    X_norm = (X - X_mean) / X_std
    print("Normalized feature means (should be ~0):")
    print(np.round(X_norm.mean(), 4))
    print()
    print("Normalized feature stds (should be ~1):")
    print(np.round(X_norm.std(), 4))
    return (X_norm,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Choose k: Elbow Plot and Silhouette Scores

    Two methods are used together to pick the best k:

    1. **Elbow / Scree plot** -- plot inertia vs. k and look for the bend.
    2. **Silhouette score loop** -- the k with the highest score wins.
    """)
    return


@app.cell
def _(KMeans, X_norm, plt):
    k_range = range(2, 9)
    inertias = []
    for n_c in k_range:
        km_e = KMeans(n_clusters=n_c, random_state=42, n_init=10)
        km_e.fit(X_norm)
        inertias.append(km_e.inertia_)

    fig_elbow, ax_elbow = plt.subplots(figsize=(7, 4))
    ax_elbow.plot(list(k_range), inertias, 'bx-')
    ax_elbow.set_xlabel('Number of clusters (k)')
    ax_elbow.set_ylabel('Inertia (sum of squared distances)')
    ax_elbow.set_title('Scree / Elbow Plot')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(KMeans, X_norm, metrics):
    for _n in range(2, 9):
        _model = KMeans(n_clusters=_n, random_state=42, n_init=10)
        _model.fit(X_norm)
        _preds = _model.predict(X_norm)
        _score = metrics.silhouette_score(X_norm, _preds)
        print(f'Silhouette score for {_n} clusters: {_score:.4f}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The elbow plot shows a bend after k=2, and the silhouette score is highest at k=2 (~0.56).
    Both methods agree: **k=2 is the best choice** for this dataset.

    This makes sense, most Wikipedia articles in the top 100 have steady traffic, while a small group of articles spike dramatically for a brief period.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fit K-Means with k=2
    """)
    return


@app.cell
def _(KMeans, X_norm, df, metrics):
    km_final = KMeans(n_clusters=2, random_state=42, n_init=10)
    km_final.fit(X_norm)
    cluster_labels = km_final.predict(X_norm)

    df_result = df.copy()
    df_result['cluster'] = cluster_labels

    final_score = metrics.silhouette_score(X_norm, cluster_labels)
    print(f'Final silhouette score (k=2): {final_score:.4f}')
    print()
    print('Cluster counts:')
    print(df_result['cluster'].value_counts())
    return cluster_labels, df_result


@app.cell
def _(df_result, features):
    print('Cluster means (normalized):')
    print(df_result.groupby('cluster')[features].mean().round(2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## PCA: Visualize the Clusters

    The feature space has 4 dimensions. PCA reduces it to 2 components so the
    cluster assignments can be plotted in a 2-D scatter.
    """)
    return


@app.cell
def _(KMeans, PCA, X_norm, cluster_labels, pd, plt):
    X_ctr = X_norm - X_norm.mean()

    pca = PCA(n_components=2)
    X_reduced = pca.fit_transform(X_ctr)
    X_reduced_df = pd.DataFrame(X_reduced, columns=['PC1', 'PC2'])

    km_pca = KMeans(n_clusters=2, random_state=42, n_init=10)
    pca_labels = km_pca.fit_predict(X_ctr)

    fig_pca, ax_pca = plt.subplots(figsize=(7, 5))
    scatter_pca = ax_pca.scatter(
        X_reduced_df['PC1'], X_reduced_df['PC2'],
        c=cluster_labels, cmap='tab10', s=25, alpha=0.7
    )
    ax_pca.set_xlabel('PC1')
    ax_pca.set_ylabel('PC2')
    ax_pca.set_title('K-Means Clusters Projected onto PCA Axes (k=2)')
    plt.colorbar(scatter_pca, ax=ax_pca, label='Cluster')
    plt.tight_layout()
    plt.show()

    print(f'Variance explained by PC1: {pca.explained_variance_ratio_[0]:.2%}')
    print(f'Variance explained by PC2: {pca.explained_variance_ratio_[1]:.2%}')
    print(f'Total variance explained:  {pca.explained_variance_ratio_.sum():.2%}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Summary of Findings

    **Two natural groupings emerged from K-Means (k=2):**

    - **Cluster 0 -- "Steady audience" articles:** The large majority of the 500 articles
      fall here. These have lower total views, fewer days in the top 100, and a moderate
      peak ratio. They represent articles that attracted consistent but not explosive attention.

    - **Cluster 1 -- "Viral spike" articles:** A small group with very high total views,
      many days in the top 100, and high peak views. These are articles that became
      the focus of a major news event or cultural moment and drew enormous traffic.

    **What the PCA plot tells us:**

    PC1 and PC2 together explain the large majority of the variance in the dataset.
    The PCA plot shows the two clusters are well separated along the PC1 axis,
    confirming that the K-Means boundary is meaningful and not arbitrary.
    The small cluster of viral articles sits far to the right on PC1, isolated from
    the dense mass of steady-audience articles. This separation, combined with a
    silhouette score of ~0.56, indicates the clusters are real groupings in the data
    and not just noise.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## References

    Anthropic. (2026, April 19). *Unsupervised Machine Learning Concepts Guide*

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Generative AI chat]. Claude Sonnet 4.6. https://claude.ai/share/19bb28ef-a549-4d10-ad4e-5233316bf091

    &nbsp;

    ---

    ## Appendix: AI-Generated Content

    **Tool:** Claude Sonnet 4.6 (Anthropic)
    **Date:** April 19, 2026
    **Topic:** Supervised Machine Learning Concepts

    ---

    ### Prompt Submitted to AI:

    Could you make me a list of the concepts in  the 6_unsupervised_machine_learning.py
    file and describe what each one is used for and how it works? put them in numerical
    order. provide the results in a Marimo style file with code windows for example code
    snippets when appropriate. the format should be markdown window describing the concept,
    code window with the code, and a markdown window explaining results and what the code
    is doing.

    ---

    ### Full-Text AI Response:

    Here is a summary of the 11 concepts covered, in the order they appear in the file::

    | # | Concept | Key Tool / Function |
    |:-:|:--------|:--------------------|
    | 1 | Supervised vs. Unsupervised Learning | conceptual framing |
    | 2 | K-Means Clustering | `KMeans`, `fit_predict`, `cluster_centers_` |
    | 3 | Silhouette Score | `silhouette_score` |
    | 4 | Synthetic Data with `make_blobs` | `make_blobs` |
    | 5 | Predicting Cluster Membership | `.predict()`, `.labels_`, `.reshape(1,-1)` |
    | 6 | Data Cleaning for ML | `.drop()`, `.replace()`, `.astype()` |
    | 7 | Scree Plot / Elbow Method | `inertia_`, matplotlib line plot |
    | 8 | Silhouette Score Loop for k Selection | `metrics.silhouette_score` in a for-loop |
    | 9 | PCA -- Dimensionality Reduction | `PCA`, `fit_transform`, `explained_variance_ratio_` |
    | 10 | User-Defined Functions (UDFs) | `def`, reusable helper functions |
    | 11 | Color Quantization (K-Means on Images) | `KMeans` + UDFs on pixel arrays |

    The full detailed response is contained in the reference link.
    """)
    return


if __name__ == "__main__":
    app.run()
