# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.22.4",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.4",
#     "pandas>=3.0.2",
#     "scikit-learn>=1.8.0",
#     "seaborn>=0.13.2",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App()


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Unsupervised Machine Learning: Concepts Guide
    
    This notebook walks through the key concepts covered in `6_Unsupervised_Machine_Learning.py`,
    presented in the order they appear in the file.  
    Each section includes a description of the concept, an example code snippet,
    and an explanation of what the code is doing and what results to expect.
    """)
    return


# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    from sklearn.datasets import make_blobs
    from sklearn.metrics import silhouette_score
    from sklearn.decomposition import PCA
    from sklearn import metrics
    return KMeans, PCA, make_blobs, metrics, mo, np, pd, plt, silhouette_score


# ===========================================================================
# CONCEPT 1 – Supervised vs. Unsupervised Learning
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 1. Supervised vs. Unsupervised Learning

    **What it is:**  
    These are the two main branches of machine learning.

    **Supervised learning** trains a model on *labeled* data. Every row has both
    input features and a known output (the label). The goal is to learn a mapping
    so the model can *predict* an output for new, unseen inputs.  
    Examples: regression to predict salary; classification to predict benign/malignant.

    **Unsupervised learning** works with *unlabeled* data. There are no known outputs.
    Instead of predicting, the algorithm finds hidden structure -- most commonly by
    grouping similar data points into **clusters**.  
    Because there is no ground-truth label, traditional accuracy cannot be calculated.
    A metric called the **silhouette score** is used instead to measure cluster quality.

    **When to use unsupervised learning:**  
    - You want to discover natural groupings in data (customer segments, gene expression
      patterns, image regions, etc.)
    - You do not have labeled training examples.
    - Your dataset is too large or expensive to label by hand.
    """)
    return


@app.cell
def _(make_blobs, np):
    # Supervised: we have labels (y_sup).
    # Unsupervised: we only have features (X_demo) -- labels are hidden.
    X_demo, y_sup = make_blobs(n_samples=200, centers=3, random_state=0)
    X_unlabeled = X_demo          # pretend we do not have y_sup
    print("Supervised   -- features shape:", X_demo.shape, "  labels shape:", y_sup.shape)
    print("Unsupervised -- features shape:", X_unlabeled.shape, "  (no labels available)")
    return X_demo, X_unlabeled, y_sup


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    `make_blobs` creates a synthetic dataset with 200 points in 3 natural groups.
    In the supervised framing we keep both `X` (features) and `y` (labels).
    In the unsupervised framing we throw away `y` and work only with `X`.
    The print statements confirm the shapes -- 200 rows, 2 feature columns, and
    (in the supervised case) 200 integer class labels.
    """)
    return


# ===========================================================================
# CONCEPT 2 – K-Means Clustering
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 2. K-Means Clustering

    **What it is:**  
    K-Means is the most widely used clustering algorithm. You choose a target number
    of clusters **k**, and the algorithm partitions every data point into one of those
    k groups by minimizing the total within-cluster variance (the "sum of squared
    distances" from each point to its cluster center).

    **How it works (step by step):**  
    1. Randomly place k centroids in the feature space.  
    2. Assign each data point to the nearest centroid.  
    3. Recompute each centroid as the mean of all points assigned to it.  
    4. Repeat steps 2-3 until the centroids stop moving (convergence) or a maximum
       number of iterations is reached.

    The word *"means"* refers to the averaging step used to recompute centroids.

    **Key parameter:** `n_clusters` (k) -- you must choose this before fitting.
    """)
    return


@app.cell
def _(KMeans, X_demo, plt):
    # Fit K-Means with k=3 on the synthetic data
    km = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels_km = km.fit_predict(X_demo)
    centroids_km = km.cluster_centers_

    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.scatter(X_demo[:, 0], X_demo[:, 1], c=labels_km, cmap='tab10', s=30, alpha=0.7)
    ax1.scatter(centroids_km[:, 0], centroids_km[:, 1],
                c='red', s=200, marker='X', label='Centroids')
    ax1.set_title("K-Means Clustering (k=3)")
    ax1.set_xlabel("Feature 1")
    ax1.set_ylabel("Feature 2")
    ax1.legend()
    plt.tight_layout()
    plt.show()
    print("Centroid coordinates:\n", centroids_km)
    return centroids_km, fig1, km, labels_km


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    - `KMeans(n_clusters=3)` creates the model object with k=3.  
    - `fit_predict(X_demo)` trains the model and immediately returns the cluster
      label (0, 1, or 2) for each data point.  
    - `cluster_centers_` is a model attribute that stores the (x, y) coordinates of
      each centroid after convergence -- printed below the plot.  
    - The scatter plot colors each point by its assigned cluster; the red X markers
      show where the centroids settled.  
    - Because the blobs were generated with 3 true centers, K-Means with k=3 should
      recover them almost perfectly.
    """)
    return


# ===========================================================================
# CONCEPT 3 – Silhouette Score
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3. Silhouette Score

    **What it is:**  
    The silhouette score is the primary way to measure clustering quality when you
    have no ground-truth labels. It answers the question: *"Is each point more
    similar to its own cluster than to the nearest neighboring cluster?"*

    **How it is calculated (for a single point):**  
    - **a** = mean distance from the point to all other points in the *same* cluster.  
    - **b** = mean distance from the point to all points in the *nearest other* cluster.  
    - Silhouette value = (b - a) / max(a, b)

    **Interpreting the score (averaged over all points):**  
    | Score range | Meaning |
    |:-----------:|:--------|
    | Close to +1 | Points are well inside their clusters, far from neighbors -- great separation. |
    | Near 0      | Points lie on or near the boundary between two clusters. |
    | Negative    | Points may have been assigned to the wrong cluster. |

    **Usage in the file:** Used both to evaluate a single k value and to loop over
    multiple k values to find the best one.
    """)
    return


@app.cell
def _(KMeans, X_demo, silhouette_score):
    # Compare silhouette scores for k = 2, 3, 4, 5
    for k_val in [2, 3, 4, 5]:
        km_s = KMeans(n_clusters=k_val, random_state=42, n_init=10)
        lbl_s = km_s.fit_predict(X_demo)
        sc = silhouette_score(X_demo, lbl_s)
        print(f"k={k_val}  -->  silhouette score = {sc:.4f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    We fit K-Means four times with k = 2, 3, 4, and 5, computing the silhouette
    score each time. Because the synthetic data has exactly 3 natural groups,
    you should see the highest score at k=3.
    A higher silhouette score means the clusters are more compact and better
    separated -- so the k with the highest score is the best choice for this data.
    """)
    return


# ===========================================================================
# CONCEPT 4 – make_blobs (Synthetic Data Generation)
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4. Synthetic Data Generation with `make_blobs`

    **What it is:**  
    `sklearn.datasets.make_blobs` creates artificial clustering datasets. It is used
    throughout the file to build quick, controllable examples without needing a real
    dataset. This lets you verify that an algorithm works correctly before applying it
    to messy real-world data.

    **Key parameters:**  
    - `n_samples` -- total number of data points.  
    - `centers` -- number of blob centers (the true k).  
    - `cluster_std` -- how spread out each blob is (larger = more overlap).  
    - `random_state` -- seed for reproducibility.

    `make_blobs` returns `X` (the feature matrix) and `y` (the true cluster labels,
    which are ignored in unsupervised demos).
    """)
    return


@app.cell
def _(make_blobs, plt):
    # Generate blobs with different spreads and visualize
    X_tight, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.5, random_state=1)
    X_loose, _ = make_blobs(n_samples=300, centers=4, cluster_std=2.0, random_state=1)

    fig2, (ax_t, ax_l) = plt.subplots(1, 2, figsize=(10, 4))
    ax_t.scatter(X_tight[:, 0], X_tight[:, 1], s=15, alpha=0.6)
    ax_t.set_title("Tight blobs (std=0.5)")
    ax_l.scatter(X_loose[:, 0], X_loose[:, 1], s=15, alpha=0.6)
    ax_l.set_title("Loose blobs (std=2.0)")
    plt.tight_layout()
    plt.show()
    return X_loose, X_tight, ax_l, ax_t, fig2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    Two datasets with the same centers but different `cluster_std` values are plotted
    side by side. The tight blobs (std=0.5) are compact and easy for K-Means to
    separate; the loose blobs (std=2.0) overlap significantly, making clustering
    harder. This illustrates why `cluster_std` matters for testing algorithm behavior.
    """)
    return


# ===========================================================================
# CONCEPT 5 – Predicting Cluster Membership for New Points
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5. Predicting Cluster Membership for New Points

    **What it is:**  
    After a K-Means model is fitted, you can call `.predict()` on new data points to
    find out which cluster they belong to. This is similar to calling `.predict()` on
    a supervised model, except the output is a cluster label (an integer) rather than
    a target value.

    **Important detail -- array shape:**  
    `sklearn` expects a 2-D array as input. A single point created with `np.array([x, y])`
    is 1-D and must be reshaped with `.reshape(1, -1)` before it can be passed to
    `.predict()`. The file explicitly demonstrates this step.

    **Model attributes used:**  
    - `kmeans.labels_` -- the cluster assignment for every point in the training data.  
    - `kmeans.predict(new_point)` -- cluster assignment for a new, unseen point.
    """)
    return


@app.cell
def _(KMeans, X_demo, np):
    # Fit a model, then predict for a brand-new point
    km_p = KMeans(n_clusters=3, random_state=42, n_init=10)
    km_p.fit(X_demo)

    # A single new point -- must be 2-D for sklearn
    new_point = np.array([-3.0, -3.0])
    new_point_2d = new_point.reshape(1, -1)   # shape (1, 2)

    cluster_id = km_p.predict(new_point_2d)
    print(f"New point {new_point} was assigned to cluster {cluster_id[0]}")
    print(f"\nFirst 10 training labels: {km_p.labels_[:10]}")
    return cluster_id, km_p, new_point, new_point_2d


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    - After fitting, `km_p.labels_` holds the cluster index (0, 1, or 2) for every
      one of the 200 training points.  
    - `new_point.reshape(1, -1)` converts the 1-D array `[-3.0, -3.0]` into a 2-D
      array of shape `(1, 2)` that sklearn can accept.  
    - `km_p.predict(new_point_2d)` returns the cluster index of the nearest centroid
      to that new point.  
    - The printed result tells you which cluster the point (-3, -3) falls into.
    """)
    return


# ===========================================================================
# CONCEPT 6 – Data Cleaning for Unsupervised Learning
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 6. Data Cleaning for Unsupervised Learning

    **What it is:**  
    Before applying K-Means (or any ML algorithm), the data must be in a consistent,
    numeric format. The Wisconsin Breast Cancer demo in the file shows two common
    cleaning steps:

    1. **Dropping irrelevant columns** -- The `sample` column is just an ID number
       with no clustering meaning, so it is removed with `df.drop()`.

    2. **Handling missing values** -- The `bare_nuclei` column contains the string
       `'?'` for 16 missing values. The file replaces these with `'1'`
       (the most common value) and then converts the column to integer type.

    These steps are necessary because K-Means computes distances between points,
    which requires all features to be numeric and complete.
    """)
    return


@app.cell
def _(pd):
    # Simulate the cleaning steps from the cancer dataset
    data_raw = pd.DataFrame({
        'sample':      [1000025, 1002945, 1015425],
        'thickness':   [5, 5, 3],
        'bare_nuclei': ['1', '?', '3'],
        'class':       [2, 2, 2]
    })
    print("Before cleaning:\n", data_raw.dtypes, "\n")
    print(data_raw)

    # Step 1: drop the ID column
    data_clean = data_raw.drop('sample', axis=1)

    # Step 2: replace '?' and convert to int
    data_clean['bare_nuclei'] = data_clean['bare_nuclei'].replace('?', '1')
    data_clean['bare_nuclei'] = data_clean['bare_nuclei'].astype(int)

    print("\nAfter cleaning:\n", data_clean.dtypes, "\n")
    print(data_clean)
    return data_clean, data_raw


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    - Before cleaning, `bare_nuclei` is an object (string) dtype because of the `'?'`
      characters, and `sample` is an integer ID that should not influence clustering.  
    - After `drop('sample', ...)`, the ID column is gone.  
    - After `replace('?', '1')` and `.astype(int)`, `bare_nuclei` is now an integer
      column with no missing values.  
    - The final dataframe is entirely numeric and ready for K-Means.
    """)
    return


# ===========================================================================
# CONCEPT 7 – Scree Plot / Elbow Method
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 7. Scree Plot and the Elbow Method

    **What it is:**  
    K-Means requires you to specify k before fitting. The elbow method helps you
    choose a good k by plotting **inertia** (the total sum of squared distances from
    each point to its centroid) against different values of k.

    **How to read the plot:**  
    - As k increases, inertia always decreases (more clusters means smaller groups
      that are tighter around their centers).  
    - At some point the improvement slows down and the curve bends -- this bend is
      the **elbow** and is a good candidate for the optimal k.  
    - The "elbow" is the point of diminishing returns: adding more clusters beyond
      it does not substantially reduce inertia.

    **Model attribute used:** `kmeans.inertia_` -- returns the within-cluster sum of
    squares after fitting.
    """)
    return


@app.cell
def _(KMeans, X_demo, plt):
    k_range_demo = range(2, 12)
    inertias = []
    for n_c in k_range_demo:
        km_e = KMeans(n_clusters=n_c, random_state=42, n_init=10)
        km_e.fit(X_demo)
        inertias.append(km_e.inertia_)

    fig3, ax3 = plt.subplots(figsize=(7, 4))
    ax3.plot(list(k_range_demo), inertias, 'bx-')
    ax3.set_xlabel("Number of clusters (k)")
    ax3.set_ylabel("Inertia (sum of squared distances)")
    ax3.set_title("Scree / Elbow Plot")
    plt.tight_layout()
    plt.show()
    return ax3, fig3, inertias, k_range_demo, km_e, n_c


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    We loop from k=2 to k=11, fit a K-Means model each time, and record
    `model.inertia_` (the within-cluster sum of squared distances).
    The values are then plotted as a line.  
    Because the synthetic data has 3 true groups, the curve should show a clear
    bend ("elbow") at k=3 -- after which inertia keeps dropping but much more slowly.
    That elbow is your signal to choose k=3.
    """)
    return


# ===========================================================================
# CONCEPT 8 – Silhouette Score Loop (Choosing k Programmatically)
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 8. Using a Silhouette Score Loop to Choose k

    **What it is:**  
    Instead of (or in addition to) reading an elbow plot visually, the file uses a
    Python loop to compute the silhouette score for each value of k and print all
    results. The k with the highest silhouette score is the best-performing one
    algorithmically.

    This is the "python-like way" mentioned in the file -- automating the search
    rather than eyeballing a plot.
    """)
    return


@app.cell
def _(KMeans, X_demo, metrics):
    # Loop over k values and print silhouette scores
    for _n in range(2, 8):
        _model = KMeans(n_clusters=_n, random_state=42, n_init=10)
        _model.fit(X_demo)
        _preds = _model.predict(X_demo)
        _score = metrics.silhouette_score(X_demo, _preds)
        print(f"Silhouette score for {_n} clusters: {_score:.4f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    For each k from 2 to 7 we fit a fresh K-Means model, predict cluster labels for
    all training points, and compute the mean silhouette score with
    `metrics.silhouette_score()`.  
    The printout lets you compare all scores at once. The k with the highest score
    (closest to +1) is the best-supported number of clusters for this data.
    For the 3-blob synthetic data, k=3 should win.
    """)
    return


# ===========================================================================
# CONCEPT 9 – PCA (Principal Component Analysis)
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 9. PCA -- Principal Component Analysis

    **What it is:**  
    PCA is a technique for **dimensionality reduction**. When a dataset has many
    features (dimensions), PCA remaps it to a smaller set of new variables called
    **principal components** (PCs) that capture as much of the original variance as
    possible.

    **Two uses in this file:**  
    1. **Feature reduction** -- reducing many features to fewer to avoid the "curse
       of dimensionality" (needing exponentially more data as features grow).  
    2. **Visualization** -- reducing to exactly 2 components so the high-dimensional
       cluster assignments can be displayed in a 2-D scatter plot.

    **Steps before applying PCA (from the file):**  
    1. Center the data: subtract the column mean so each feature has mean = 0.  
    2. Optionally rescale (divide by standard deviation) for features on very
       different scales.  
    3. Fit PCA and transform the data into the new coordinate system.

    **Key parameter:** `n_components` -- how many principal components to keep.
    """)
    return


@app.cell
def _(KMeans, PCA, X_demo, pd, plt):
    # Center the data, run PCA to 2 components, then plot cluster assignments
    X_ctr = X_demo - X_demo.mean(axis=0)

    pca = PCA(n_components=2)
    X_reduced = pca.fit_transform(X_ctr)
    X_reduced_df = pd.DataFrame(X_reduced, columns=['PC1', 'PC2'])

    # Get cluster labels for coloring
    km_pca = KMeans(n_clusters=3, random_state=42, n_init=10)
    pca_labels = km_pca.fit_predict(X_ctr)

    fig4, ax4 = plt.subplots(figsize=(6, 4))
    scatter4 = ax4.scatter(X_reduced_df['PC1'], X_reduced_df['PC2'],
                           c=pca_labels, cmap='rainbow', s=20, alpha=0.8)
    ax4.set_xlabel('PC1')
    ax4.set_ylabel('PC2')
    ax4.set_title('Projection of K-Means clustering onto PCA axes')
    plt.colorbar(scatter4, ax=ax4, label='Cluster')
    plt.tight_layout()
    plt.show()

    print(f"Variance explained by PC1: {pca.explained_variance_ratio_[0]:.2%}")
    print(f"Variance explained by PC2: {pca.explained_variance_ratio_[1]:.2%}")
    return X_ctr, X_reduced, X_reduced_df, ax4, fig4, km_pca, pca, pca_labels, scatter4


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    - `X_demo - X_demo.mean(axis=0)` centers each column by subtracting its mean.  
    - `PCA(n_components=2).fit_transform(X_ctr)` projects the centered data into
      the 2-D subspace defined by the two principal components.  
    - The scatter plot colors each point by its K-Means cluster label. Well-separated
      blobs of color indicate the clusters are distinct in the reduced space.  
    - `pca.explained_variance_ratio_` shows what fraction of total variance each PC
      captures -- together PC1 and PC2 should account for most of the variance in
      this 2-feature synthetic dataset (likely near 100%).
    """)
    return


# ===========================================================================
# CONCEPT 10 – User-Defined Functions (UDFs) for Reusable Workflows
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 10. User-Defined Functions (UDFs) for Reusable Workflows

    **What it is:**  
    The Color Quantization section of the file introduces several small helper
    functions (UDFs) to break the image-processing pipeline into reusable pieces.
    This is a software engineering best practice: instead of repeating the same code
    for 64-color, 8-color, and 3-color versions of the image, each step is wrapped
    in a function that can be called with different parameters.

    **The four UDFs defined in the file:**  

    | Function | Purpose |
    |:---------|:--------|
    | `to_floats(pic)` | Converts pixel values from 0-255 integers to 0.0-1.0 floats for `plt.imshow`. |
    | `transform2d(pic)` | Reshapes a 3-D image array (width x height x 3) into a 2-D array (pixels x 3) so K-Means can treat each pixel as a data point. |
    | `fit_kmeans(colors, image_array)` | Fits K-Means on a random 1000-pixel sample (for speed) and returns the trained model. |
    | `predict_labels(kmeans, image_array)` | Runs `.predict()` on the full image array to assign a cluster (color) to every pixel. |
    | `recreate_image(codebook, labels, w, h)` | Rebuilds the image by replacing each pixel with the color of its cluster centroid. |
    """)
    return


@app.cell
def _(np):
    # Demonstrate each UDF with a tiny synthetic "image"

    # UDF 1: convert uint8 pixels to floats in [0, 1]
    def to_floats(pic):
        return np.array(pic, dtype=np.float64) / 255

    # UDF 2: reshape 3-D image to 2-D pixel list
    def transform2d(pic):
        w, h, d = pic.shape
        assert d == 3
        return np.reshape(pic, (w * h, d))

    # UDF 3: recreate image from cluster centroids
    def recreate_image(codebook, labels, w, h):
        d = codebook.shape[1]
        image_out = np.zeros((w, h, d))
        label_idx = 0
        for i in range(w):
            for j in range(h):
                image_out[i][j] = codebook[labels[label_idx]]
                label_idx += 1
        return image_out

    # Test with a tiny 4x4 synthetic image (random RGB pixels)
    rng = np.random.default_rng(0)
    fake_image_uint8 = rng.integers(0, 256, size=(4, 4, 3), dtype=np.uint8)

    float_image = to_floats(fake_image_uint8)
    pixels_2d  = transform2d(float_image)

    print("Original shape (4x4 image, 3 channels):", fake_image_uint8.shape)
    print("After to_floats -- dtype:", float_image.dtype,
          " value range: [{:.2f}, {:.2f}]".format(float_image.min(), float_image.max()))
    print("After transform2d -- shape:", pixels_2d.shape,
          "  (16 pixels, each with 3 RGB values)")
    return (
        fake_image_uint8,
        float_image,
        pixels_2d,
        recreate_image,
        rng,
        to_floats,
        transform2d,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    - `to_floats` divides pixel values by 255, changing the dtype from `uint8`
      (integers 0-255) to `float64` (decimals 0.0-1.0). `matplotlib` requires float
      images to be in the range [0, 1].  
    - `transform2d` flattens the 4x4x3 array into a 16x3 array. This is critical:
      K-Means sees each pixel as a single 3-D data point (its R, G, B values) rather
      than understanding the spatial layout of the image.  
    - `recreate_image` does the inverse: given the centroid colors (codebook) and a
      label for each pixel, it builds a new image where every pixel has been replaced
      by the color of its nearest centroid. This is how the compressed image is
      reconstructed.
    """)
    return


# ===========================================================================
# CONCEPT 11 – Color Quantization (K-Means on Images)
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 11. Color Quantization -- K-Means on Image Data

    **What it is:**  
    Color quantization is a real-world application of K-Means clustering where the
    "data points" are individual pixels and the "features" are the three color
    channels (Red, Green, Blue). The algorithm clusters pixels into k color groups
    and replaces every pixel with the color of its cluster centroid.

    **Why it works:**  
    - A typical photo may contain tens of thousands of unique colors.  
    - By reducing to k=64, 8, or 3 colors we dramatically compress the image.
      (A single byte can address up to 256 colors, versus 3 bytes per pixel for full
      RGB -- the same principle used by the GIF file format.)  
    - The result is a quantized image that approximates the original with far fewer
      distinct colors.

    **Connection to earlier concepts:**  
    The UDFs from Concept 10 are used here in sequence:
    `to_floats` -> `transform2d` -> `fit_kmeans` -> `predict_labels` -> `recreate_image`.

    Below we illustrate the idea with a small synthetic image rather than the bird
    photo (which requires the original file path).
    """)
    return


@app.cell
def _(KMeans, np, plt, recreate_image, to_floats, transform2d):
    # Build a small gradient image and quantize it to 2 and 4 colors
    gradient = np.zeros((20, 60, 3), dtype=np.uint8)
    for col_i in range(60):
        gradient[:, col_i, 0] = int(col_i * 255 / 59)       # red increases
        gradient[:, col_i, 2] = int((59 - col_i) * 255 / 59) # blue decreases

    float_grad = to_floats(gradient)
    pixels_grad = transform2d(float_grad)
    w_g, h_g, _ = float_grad.shape

    fig5, axes5 = plt.subplots(1, 3, figsize=(12, 2))
    axes5[0].imshow(float_grad)
    axes5[0].set_title("Original (continuous gradient)")
    axes5[0].axis('off')

    for idx_q, n_colors in enumerate([4, 2]):
        km_q = KMeans(n_clusters=n_colors, random_state=0, n_init=10).fit(pixels_grad)
        lbl_q = km_q.predict(pixels_grad)
        recon = recreate_image(km_q.cluster_centers_, lbl_q, w_g, h_g)
        axes5[idx_q + 1].imshow(recon)
        axes5[idx_q + 1].set_title(f"Quantized ({n_colors} colors)")
        axes5[idx_q + 1].axis('off')

    plt.tight_layout()
    plt.show()
    return (
        axes5,
        col_i,
        fig5,
        float_grad,
        gradient,
        h_g,
        idx_q,
        km_q,
        lbl_q,
        n_colors,
        pixels_grad,
        recon,
        w_g,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code shows:**  
    - A 20x60 gradient image transitions smoothly from blue on the left to red on
      the right, containing many unique RGB combinations.  
    - `transform2d` reshapes it to 1200 pixels x 3 channels so K-Means treats each
      pixel as a point in 3-D color space.  
    - `KMeans(n_clusters=4)` finds 4 representative colors (centroids in RGB space)
      and assigns every pixel to its nearest one.  
    - `recreate_image` replaces each pixel with its centroid color, producing the
      banded, quantized version.  
    - With 4 colors you see 4 distinct bands; with 2 colors only 2 bands remain.
      The fewer the colors, the more information is lost -- exactly the trade-off the
      file explores with the bird photo at k=64, 8, and 3.
    """)
    return


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Summary of Concepts

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
    """)
    return


if __name__ == "__main__":
    app.run()
