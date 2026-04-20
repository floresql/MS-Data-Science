# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.22.4",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.4",
#     "pandas>=3.0.2",
#     "pillow>=12.2.0",
#     "scikit-learn>=1.8.0",
#     "seaborn>=0.13.2",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Unsupervised Learning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Supervised Review
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:10px;" src="figures_wk6/supervised_unsupervised.png" width=500><br>
    Last week we looked at **Supervised** machine learning -- using labeled data to train and test the model -- and compared performance of several **regression** and **classification** algorithms.

    Supervised algorithms are generally used for **predictive modeling** -- trying to guess or predict some unknown value or category based on past observations.

    Supervised models can be trained on small, medium or large data sets. If the data set is **too large**, `sklearn` has tools to help randomly, but evenly, sample the data to make training easier.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Unsupervised Overview
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In contrast, **Unsupervised** machine learning uses **_unlabeled_** data. Because of this, there is no predictive ability. "Accuracy" can be measured using a silhouette score, which tries to determine if a point is in the correct cluster.

    Unsupervised learning is, therefore, most often used for **clustering** -- finding patterns and associations that may not be easily observable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # K-Means Algorithm
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    K-means is one of the most popular and easiest to understand of the clustering algorithms.

    A cluster refers to a collection of data points aggregated together because of certain similarities.
    **You’ll define a target number k**, which refers to the number of centroids you need in the dataset. A centroid is the imaginary or real location representing the center of the cluster.

    Every data point is allocated to each of the clusters through reducing the in-cluster sum of squares.

    In other words, the K-means algorithm identifies k number of centroids, and then allocates every data point to the nearest cluster, while keeping the errors as small as possible.

    The ‘means’ in the K-means refers to averaging of the data; that is, finding the centroid.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## How the K-means algorithm works
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To process the learning data, the K-means algorithm in data mining starts with a first group of randomly selected centroids, which are used as the beginning points for every cluster, and then performs iterative (repetitive) calculations to optimize the positions of the centroids.

    Here are the steps:
    1. Randomly initilize cluster points: μ1, μ2
    2. Assign each point to a cluster. (Every point goes to the closest neighbor)
    3. Assign new cluster centers, i.e. μj
    4. Repeat this process until

    It halts creating and optimizing clusters when either:
    * The centroids have stabilized — there is no change in their values because the clustering has been successful.
    * The defined number of iterations has been achieved.

    <img align="right" style="padding-right:10px;" src="figures_wk6/kmeans.png" width=500><br>

    The following interactive demo was created with the assistance of Gemini AI.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Demo
    ### Import libraries
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    from sklearn.datasets import make_blobs
    from sklearn.metrics import silhouette_score

    return KMeans, make_blobs, mo, np, pd, plt, silhouette_score


@app.cell
def _(mo):
    # --- UI Elements ---
    k_slider = mo.ui.slider(start=2, stop=10, step=1, value=3, label="Number of Clusters (k)")
    n_samples_slider = mo.ui.slider(start=100, stop=1000, step=50, value=300, label="Number of Points")
    seed_input = mo.ui.number(start=0, stop=100, value=42, label="Random Seed")
    return k_slider, n_samples_slider, seed_input


@app.cell
def _(k_slider, mo, n_samples_slider, seed_input):
    mo.md(
        f"""
        # Interactive K-Means Demo
        Adjust the parameters below to see how the K-Means algorithm partitions the data.

        {mo.hstack([k_slider, n_samples_slider, seed_input], justify="start")}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Generate Data
    We will fit our dataset with the sklearn K-Mean algorithm and then determine the centroids for the 5 clusters. `cluster_centers_` is a model attribute that shows the coordinates of each cluster's center point. Remember, a centroid is the imaginary or real location representing the center of the cluster.
    """)
    return


@app.cell
def _(make_blobs, n_samples_slider, seed_input):
    # --- Data Generation ---
    # This cell will re-run if n_samples or seed changes
    X, _ = make_blobs(
        n_samples=n_samples_slider.value, 
        centers=5, 
        cluster_std=1.0, 
        random_state=seed_input.value
    )
    return (X,)


@app.cell
def _(X, plt):
    #show the data
    plt.scatter(X[:, 0], X[:, 1])
    plt.title("Generated Data Points")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()
    return


@app.cell
def _(kmeans):
    #show the cluster centroids
    kmeans.cluster_centers_
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### K-Means algorithm to determine centroids
    """)
    return


@app.cell
def _(KMeans, X, k_slider, mo, plt, seed_input, silhouette_score):
    # --- K-Means Logic & Visualization ---
    # This cell re-runs if the k_slider changes
    kmeans = KMeans(n_clusters=k_slider.value, random_state=seed_input.value, n_init=10)
    labels = kmeans.fit_predict(X)
    centroids = kmeans.cluster_centers_
    score = silhouette_score(X, labels)

    # Plotting
    fig, ax = plt.subplots(figsize=(8, 5))
    #keep the color scheme blue for the clusters and red for the centroids

    scatter = ax.scatter(X[:, 0], X[:, 1])
    ax.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X', label='Centroids')
    ax.set_title(f"K-Means Clustering (k={k_slider.value})")
    ax.legend()

    # Display results in Marimo
    mo.vstack([
        mo.md(f"### Current Silhouette Score: **{score:.3f}**"),
        mo.as_html(fig)
    ])
    return centroids, kmeans


@app.cell
def _(KMeans, X, mo, seed_input, silhouette_score):
    #put the results of kmeans in a table for each value of k
    results = []
    for k in range(2, 21):
        kmeans_t = KMeans(n_clusters=k, random_state=seed_input.value, n_init=10)
        labels_t = kmeans_t.fit_predict(X)
        score_t = silhouette_score(X, labels_t)
        results.append({"k": k, "Silhouette Score": score_t})

    results_table = mo.ui.table(data=results)
    results_table
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Verify the algorithm labels
    Let's see which cluster our K-Mean algorithm predicts the point (-3,-3) will belong to.
    The `labels_` attribute shows which cluster each point belongs to.
    """)
    return


@app.cell
def _(kmeans):
    kmeans.labels_
    return


@app.cell
def _(np):
    #create a sample test point
    sample_test=np.array([-3.0,-3.0])

    # Array must be reshaped to be 2D
    second_test=sample_test.reshape(1, -1)
    return sample_test, second_test


@app.cell
def _(kmeans, second_test):
    pred = kmeans.predict(second_test)
    return (pred,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    At this point, `pred` will contain the cluster label that the point belongs to:
    """)
    return


@app.cell
def _(pred, sample_test):
    print(f'The point {sample_test} belongs to cluster {pred}')
    return


@app.cell
def _(X, centroids, k_slider, plt):
    plt.scatter(X[ : , 0], X[ : , 1], s =50)
    plt.scatter(-3, -3, s=200)
    #label the clusters with the cluster number
    for i in range(k_slider.value):
        plt.text(centroids[i, 0], centroids[i, 1], str(i), fontsize=12, fontweight='bold', color='white', ha='center', va='center')     

    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Always happy to see when things work out!  The point (-3,-3) does appear to be closer to the lower cluster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## K-Means Demo - Wisconsin Breast Cancer dataset
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For this demo we will be using the Wisconsin Breast Cancer data. Based on the information in breast-cancer-wisconsin.names file, we will assign the column names for our dataframe as follows:

    |Attribute                   | Atribute range           |df column name|
    |:--------------------------:|:------------------------:|:------------:|
    |Sample code number          | id number                | sample       |
    |Clump Thickness             | 1 - 10                   | thickness    |
    |Uniformity of Cell Size     | 1 - 10                   | uc_size      |
    |Uniformity of Cell Shape    | 1 - 10                   | uc_shape     |
    |Marginal Adhesion           | 1 - 10                   | adhesion     |
    |Single Epithelial Cell Size | 1 - 10                   | epithelial   |
    |Bare Nuclei                 | 1 - 10                   | bare_nuclei  |
    |Bland Chromatin             | 1 - 10                   | chromatin    |
    |Normal Nucleoli             | 1 - 10                   | norm_nucleoli|
    |Mitoses                     | 1 - 10                   | mitoses      |
    |Class                       | benign(2) or malignant(4)| class        |
    """)
    return


@app.cell
def _(pd):
    # Assign colum names to the dataset
    names = ['sample', 'thickness', 'uc_size', 'uc_shape', 'adhesion', 'epithelial', 'bare_nuclei',
             'chromatin', 'norm_nucleoli','mitoses','class']

    # Read dataset to pandas dataframe
    cancer = pd.read_csv('data_wk6/breast-cancer-wisconsin.data', names=names)
    return (cancer,)


@app.cell
def _(cancer):
    cancer.head()
    return


@app.cell
def _(cancer):
    class_counts = cancer['class'].value_counts()
    print(class_counts)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before we get too far, we will drop cancer['sample'] since it is just an id for the dataset and has no meaning for our clustering.
    """)
    return


@app.cell
def _(cancer):
    cancer.drop('sample', axis=1, inplace=True)
    return


@app.cell
def _(cancer):
    cancer.shape
    return


@app.cell
def _(cancer):
    cancer.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Cleaning our dataset
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We need to do something about the one categorical column that we have in our dataset.
    """)
    return


@app.cell
def _(cancer):
    # see what the range of values are in cancer.bare_nuclei
    cancer.bare_nuclei.unique()
    return


@app.cell
def _(cancer):
    cancer.bare_nuclei.value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ugh!  We have **missing values** in our dataset. The column cancer.bare_nuclei has 16 **'?'**.

    Upon further inspection, we see that there is a 58% chance that these missing values would have been a value of '1'.  I'm going to replace the missing values with a '1'.
    """)
    return


@app.cell
def _(cancer):
    # replace '?' with '1'
    cancer['bare_nuclei'] = cancer['bare_nuclei'].replace('?', '1')

    # Convert the whole column to integers
    cancer['bare_nuclei'] = cancer['bare_nuclei'].astype(int)
    return


@app.cell
def _(cancer):
    # visually verify the replacement
    cancer.bare_nuclei.unique()
    return


@app.cell
def _(cancer):
    cancer.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Awesome! We have handled all the missing values and our df is all numeric at this point.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Split into features and labels
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We will split our dataset into two groups.
    """)
    return


@app.cell
def _(cancer):
    # split data into features (X) and labels (y)
    X_1 = cancer.iloc[:, 0:9]
    y_1 = cancer.iloc[:, -1]
    return (X_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Determine the optimal number of clusters for a kmeans model
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The K-Means algorithm assumes the number of clusters as part of the input. If you do not know the number of clusters and need to determine it, you will need to run the algorithm multiple times, each time with a different number of clusters. From this, you can observe how a measure of model quality changes with the number of clusters.

    Plots displaying this information help to determine the number of clusters and are often referred to as **scree plots**. The ideal plot will have an **elbow** where the quality measure improves more slowly as the number of clusters increases. This indicates that the quality of the model is no longer improving substantially as the model complexity (i.e. number of clusters) increases. In other words, the **elbow** indicates the number of clusters inherent in the data.

    Note:: We are going to "pretend" that we don't know that the outcome of this dataset is really just k=2 clusters.

    <img align="left" style="padding-right:10px;" src="figures_wk6/elbow_plot.png" width=700><br>

    Another way to evaluate your model is to use silhouette scores.

    <div class="alert alert-block alert-info">
    <b> Silhouette score::</b> a value near +1 indicates that the sample is far away from the neighboring clusters. A value of 0 indicates that the sample is on or very close to the decision boundary between two neighboring clusters and negative values indicate that those samples might have been assigned to the wrong cluster.
    </div>
    """)
    return


@app.cell
def _(KMeans, X_1, mo):
    # --- 2. Pre-computing Scree Plot Data ---
    # We calculate inertia (sum of squares) for a range of k values
    k_range = range(2, 16)
    sum_sq = []
    for n in k_range:
        model_prep = KMeans(n_clusters=n, random_state=42, n_init=10)
        model_prep.fit(X_1)
        sum_sq.append(model_prep.inertia_)

    # --- 3. UI Elements ---
    k_slider_b = mo.ui.slider(start=2, stop=15, step=1, value=2, label="Select k (Clusters)")

    mo.md(
        f"""
        # Interactive Breast Cancer Clustering
        This demo uses PCA to visualize the 9-dimensional Wisconsin Breast Cancer data in 2D. 
        Use the slider to find the "elbow" on the Scree Plot.

        {k_slider_b}
        """
    )
    return k_range, k_slider_b, sum_sq


@app.cell
def _(KMeans, X_1, k_range, k_slider_b, mo, plt, silhouette_score, sum_sq):
    #Dynamic Modeling & Visualization ---
    selected_k = k_slider_b.value
    kmeans_b = KMeans(n_clusters=selected_k, random_state=42, n_init=10)
    labels_b = kmeans_b.fit_predict(X_1)

    # Calculate the mean silhouette score for the current selection
    score_b = silhouette_score(X_1, labels_b)

    # Plotting the Scree Plot
    fig_b, ax_b = plt.subplots(figsize=(8, 5))
    ax_b.plot(k_range, sum_sq, 'bx-', alpha=0.4)

    # Highlight the current k selection with a red dot
    current_inertia = sum_sq[selected_k - 2]
    ax_b.plot(selected_k, current_inertia, 'ro', markersize=10, label=f'Current k={selected_k}')

    ax_b.set_title("Scree Plot (Elbow Method)")
    ax_b.set_xlabel("Number of Clusters (k)")
    ax_b.set_ylabel("Inertia (Sum of Squared Distances)")
    ax_b.legend()

    # Display in Marimo
    mo.vstack([
        mo.md(f"### Current Silhouette Score: **{score_b:.3f}**"),
        mo.as_html(fig_b),
        mo.md(
            "> **Silhouette Score Interpretation:** A value near +1 indicates samples are far from neighboring clusters, "
            "while 0 indicates samples are near decision boundaries."
        )
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It's really a judgement call on what you use.

    <div class="alert alert-block alert-warning">
    <b>Note:</b> There are a wide variety of ways to determine the optimal number of clusters. I have just shown you 2 of the possiblities. The follwing articles present additional ways to accomplish finding the optimal number of k. <br>
    * https://towardsdatascience.com/clustering-metrics-better-than-the-elbow-method-6926e1f723a6 <br>
    * https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html <br>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rerunning with our optimal k value
    """)
    return


@app.cell
def _(KMeans, X_1):
    _model = KMeans(n_clusters=4, random_state=42)
    _model.fit(X_1)
    preds = _model.predict(X_1)
    return (preds,)


@app.cell
def _(preds):
    preds
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Silhouette scores.
    """)
    return


@app.cell
def _(X_1, preds):
    from sklearn import metrics
    _score = metrics.silhouette_score(X_1, preds)
    _score
    return (metrics,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Well, that's a bit disappointing!**  Let's dig into this a bit deeper.  The score above is a mean over all the samples. There might be some clusters that were well seperated and others the are not.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Visualizing our clusters
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can use a silhouette score to tell us how "separated" the clusters are.  Remember this is a mean value across all of the clusters. I generally like to include a PCA visualization in addition to the silhouette score.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### PCA - 2d visualization of data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **PCA** stands for **Principal Component Analysis** -- A technique for reducing the number of dimensions, or features, of a dataset.

    If you have a lot of features in your dataset, PCA can be helpful in feature reduction to avoid the curse of dimensionality (i.e. needing exponentially more data as the number of features grows to do accurate predictions). In this case, PCA remaps the data to a new (smaller) coordinate system which tries to account for the most information possible.

    We can *also* use PCA to visualize the data by reducing the features to 2 dimensions and making a scatterplot.
    You can think of this as  "mashing" the data down into 2d from the 4d we have.

    Steps for PCA:
    1. Center or Normalize each feature to have a mean = 0, standard deviation = 1.
    2. May need to rescale features (dividing each feature by its standard devation). Numbers should be roughly equally distributed) on our own. The PCA algorithm will not do this for us.
    3. Find PCA by maximizing projected subspace or minimize residual
    """)
    return


@app.cell
def _(X_1, pd, preds):
    #Center the data
    X_centered = X_1 - X_1.mean()

    from sklearn.decomposition import PCA
    _pca = PCA(n_components=2)
    _data_reduced = _pca.fit_transform(X_centered)
    _data_reduced = pd.DataFrame(_data_reduced)
    _ax = _data_reduced.plot(kind='scatter', x=0, y=1, c=preds, cmap='rainbow')
    _ax.set_xlabel('PC1')
    _ax.set_ylabel('PC2')
    _ax.set_title('Projection of the clustering on the axis of the PCA')
    return PCA, X_centered


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hmmm... That's interesting! There are discernible clusters from our model, but we do have some overlap.  Which in all honesty, we would expect from this dataset.  We were "pretending" that we didn't know the true number of clusters. But this will give you an idea on how to find the optimal number of clusters.

    Which give me an idea!

    **Let's see if we can use the silhouette score to help us determine the number of clusters in a python-like way.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Use the silhouette score for clusters
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Scikit-learn documentation has a very good demonstration of using silhouette scores for clustering at [https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#sphx-glr-auto-examples-cluster-plot-kmeans-silhouette-analysis-py](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#sphx-glr-auto-examples-cluster-plot-kmeans-silhouette-analysis-py)

    The Scikit-learn demo produces some very nice graphs but I think in this case we can get away with just numbers:
    """)
    return


@app.cell
def _(KMeans, X_centered, metrics):
    for _n in range(2, 30):
        _model = KMeans(n_clusters=_n, random_state=42)
        _model.fit(X_centered)
        preds_1 = _model.predict(X_centered)
        _score = metrics.silhouette_score(X_centered, preds_1)
        print('Silhouette score for ', _n, ' clusters: ', _score)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hmmmm.... Looks like 2 clusters performed the best.  One last thing to do, visualized k=2 in a PCA plot.
    """)
    return


@app.cell
def _(KMeans, X_centered, metrics):
    _model = KMeans(n_clusters=2, random_state=42)
    _model.fit(X_centered)
    preds_2 = _model.predict(X_centered)
    _score = metrics.silhouette_score(X_centered, preds_2)
    _score
    return (preds_2,)


@app.cell
def _(PCA, X_centered, pd, preds_2):
    _pca = PCA(n_components=2)
    _data_reduced = _pca.fit_transform(X_centered)
    _data_reduced = pd.DataFrame(_data_reduced)
    _ax = _data_reduced.plot(kind='scatter', x=0, y=1, c=preds_2, cmap='rainbow')
    _ax.set_xlabel('PC1')
    _ax.set_ylabel('PC2')
    _ax.set_title('Projection of the clustering on the axis of the PCA')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Color Quantization - Visualizing K-Means clustering
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This demo is based from the tutorial [Color Quantization using K-Means](https://scikit-learn.org/stable/auto_examples/cluster/plot_color_quantization.html) provided by sklearn. <br>
    Special thank you to Dr. Michael Busch for converting the original tutorial from R into Python and creating a set of reusable UDFs.

    Performs a pixel-wise Vector Quantization (VQ) of an image of a colorful parrot, reducing the number of colors required to show the image from 96,615 unique colors to 64, 8 and 3, while preserving the overall appearance quality.

    In this example, pixels are represented in a 3D-space and K-means is used to find the respective color clusters. In the image processing literature, the codebook obtained from K-means (the cluster centers) is called the color palette. Using a single byte, up to 256 colors can be addressed, whereas an RGB encoding requires 3 bytes per pixel. The GIF file format, for example, uses such a palette.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Imports that we will need
    """)
    return


@app.cell
def _():
    # Authors: Robert Layton <robertlayton@gmail.com>
    #          Olivier Grisel <olivier.grisel@ensta.org>
    #          Mathieu Blondel <mathieu@mblondel.org>
    #
    # License: BSD 3 clause
    from sklearn.metrics import pairwise_distances_argmin
    from sklearn.datasets import load_sample_image
    from sklearn.utils import shuffle
    from time import time
    # '%matplotlib inline' command supported automatically in marimo
    from PIL import Image

    return Image, shuffle, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## UDFs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To allow us to reuse  the majority of our code, we will create a few User Defined Functions (UDFs).
    """)
    return


@app.cell
def _(np):
    # Convert to floats instead of the default 8 bits integer coding. Dividing by
    # 255 is important so that plt.imshow behaves on float data (need to
    # be in the range [0-1])

    def to_floats(pic):
        return np.array(pic, dtype=np.float64) / 255

    return (to_floats,)


@app.cell
def _(np):
    def transform2d(pic):
        original_shape = tuple(pic.shape)
        w, h, d = original_shape
        assert d == 3
        return np.reshape(pic, (w * h, d))

    return (transform2d,)


@app.cell
def _(KMeans, shuffle, time):
    def fit_kmeans(colors, image_array):
        print("Fitting model on a small sub-sample of the data")
        t0 = time()
        image_array_sample = shuffle(image_array, random_state=0)[:1000]
        kmeans = KMeans(n_clusters=colors, random_state=0).fit(image_array_sample)
        print("done in %0.3fs." % (time() - t0))
        return kmeans

    return (fit_kmeans,)


@app.cell
def _(time):
    # Get labels for all points
    def predict_labels(kmeans, image_array):
        print("Predicting color indices on the full image (k-means)")
        t0 = time()
        labels = kmeans.predict(image_array)
        print("done in %0.3fs." % (time() - t0))
        return labels

    return (predict_labels,)


@app.cell
def _(np):
    def recreate_image(codebook, labels, w, h):
        """Recreate the (compressed) image from the code book & labels"""
        d = codebook.shape[1]
        image = np.zeros((w, h, d))
        label_idx = 0
        for i in range(w):
            for j in range(h):
                image[i][j] = codebook[labels[label_idx]]
                label_idx = label_idx + 1
        return image

    return (recreate_image,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Load original image
    """)
    return


@app.cell
def _(Image, np):
    # Load any photo into a Numpy array
    image = Image.open("data_wk6/ColorfulBird.jpg")
    image = np.array(image)
    image.shape
    return (image,)


@app.cell
def _(image, plt, to_floats):
    image_1 = to_floats(image)
    #show the image and add a label as original image with 96,615 colors
    plt.imshow(image_1)
    plt.title('Original image (96,615 colors)')
    plt.axis('off')
    plt.show()

    return (image_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Color reduction with K-Means
    """)
    return


@app.cell
def _(fit_kmeans, image_1, transform2d):
    image_array = transform2d(image_1)
    kmeans64 = fit_kmeans(64, image_array)
    kmeans8 = fit_kmeans(8, image_array)
    kmeans3 = fit_kmeans(3, image_array)
    return image_array, kmeans3, kmeans64, kmeans8


@app.cell
def _(image_array, kmeans3, kmeans64, kmeans8, predict_labels):
    labels64 = predict_labels(kmeans64, image_array)
    labels8 = predict_labels(kmeans8, image_array)
    labels3 = predict_labels(kmeans3, image_array)
    return labels3, labels64, labels8


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Displaying the new images
    """)
    return


@app.cell
def _(image_1):
    # display image size
    w, h, d = image_1.shape
    print(w, h, d)

    return


@app.cell
def _(image_1, kmeans64, labels64, plt, recreate_image):
    plt.title('Quantized image (64 colors, K-Means)')
    plt.imshow(recreate_image(kmeans64.cluster_centers_, labels64, image_1.shape[0], image_1.shape[1]))
    #plt.clf()
    plt.axis('off')
    plt.show()
    return


@app.cell
def _(image_1, kmeans8, labels8, plt, recreate_image):
    plt.title('Quantized image (8 colors, K-Means)')
    plt.imshow(recreate_image(kmeans8.cluster_centers_, labels8, image_1.shape[0], image_1.shape[1]))
    #plt.clf()
    plt.axis('off')
    plt.show()
    return


@app.cell
def _(image_1, kmeans3, labels3, plt, recreate_image):
    plt.title('Quantized image (3 colors, K-Means)')
    plt.imshow(recreate_image(kmeans3.cluster_centers_, labels3, image_1.shape[0], image_1.shape[1]))
    plt.axis('off')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    References: <br>
    https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1 <br>
    https://www.kaggle.com/bburns/iris-exploration-pca-k-means-and-gmm-clustering <br>
    https://scikit-learn.org/stable/auto_examples/cluster/plot_color_quantization.html <br>
    http://docs.biolab.si/3/visual-programming/widgets/model/knn.html
    """)
    return


if __name__ == "__main__":
    app.run()
