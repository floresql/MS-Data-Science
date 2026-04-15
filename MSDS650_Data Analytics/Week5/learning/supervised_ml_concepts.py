# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.22.0",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.3",
#     "pandas>=3.0.1",
#     "scikit-learn>=1.8.0",
#     "seaborn>=0.13.2",
# ]
# ///

import marimo

__generated_with = "0.22.0"
app = marimo.App()


# ---------------------------------------------------------------------------
# Title
# ---------------------------------------------------------------------------
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Supervised Machine Learning: Concept Reference Guide

    This notebook walks through every concept introduced in
    `5_Supervised_Machine_Learning.py`, in the order they appear.
    Each concept has a description, an example code block, and an
    explanation of what the code is doing and what the results mean.
    """)
    return


# ---------------------------------------------------------------------------
# Imports shared across all cells
# ---------------------------------------------------------------------------
@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
    from sklearn.model_selection import train_test_split, KFold, cross_val_score
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline, make_pipeline
    from sklearn.linear_model import LinearRegression, Lasso, ElasticNet
    from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
    from sklearn.svm import SVR, SVC
    from sklearn.ensemble import (
        RandomForestRegressor, GradientBoostingRegressor,
        ExtraTreesRegressor, AdaBoostRegressor,
        RandomForestClassifier, GradientBoostingClassifier,
        ExtraTreesClassifier, AdaBoostClassifier,
    )
    from sklearn.linear_model import LogisticRegression
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import r2_score
    import warnings
    warnings.filterwarnings("ignore")
    return (
        AdaBoostClassifier, AdaBoostRegressor,
        DecisionTreeClassifier, DecisionTreeRegressor,
        ElasticNet, ExtraTreesClassifier, ExtraTreesRegressor,
        GaussianNB, GradientBoostingClassifier, GradientBoostingRegressor,
        KFold, KNeighborsClassifier, KNeighborsRegressor,
        Lasso, LinearDiscriminantAnalysis, LinearRegression,
        LogisticRegression, Pipeline, RandomForestClassifier,
        RandomForestRegressor, SVC, SVR, StandardScaler,
        cross_val_score, make_pipeline, mo, np, pd, plt,
        r2_score, sns, train_test_split,
    )


# ===========================================================================
# CONCEPT 1 -- Supervised vs Unsupervised Learning
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 1. Supervised vs Unsupervised Learning

    **What it is:**
    Machine learning splits into two broad camps based on whether the
    training data has labels (known correct answers).

    - **Supervised learning** trains on labeled data. The model learns
      the relationship between inputs and known outputs so it can
      predict outputs for new, unseen inputs.
    - **Unsupervised learning** trains on unlabeled data. The model
      discovers hidden structure on its own (e.g., clustering).

    **Why it matters:** Choosing the wrong type of learning for your
    data is a fundamental mistake. If you have labels (a target column),
    use supervised learning. If you only have features and want to find
    natural groupings, use unsupervised learning.

    **Two sub-types of supervised learning:**

    | Type | Target | Example |
    |---|---|---|
    | Classification | Discrete category | Is this email spam? |
    | Regression | Continuous number | What will the mpg be? |
    """)
    return


@app.cell
def _(np):
    # Toy illustration: labeled data (supervised) vs unlabeled data (unsupervised)
    labeled_data = np.array([
        [5,  3,  "Purple"],
        [55, 52, "Red"],
        [71, 80, "Red"],
    ])
    unlabeled_data = np.array([
        [5,  3],
        [55, 52],
        [71, 80],
    ])
    print("Labeled (supervised) data -- we know the class:")
    print(labeled_data)
    print("\nUnlabeled (unsupervised) data -- no class column:")
    print(unlabeled_data)
    return labeled_data, unlabeled_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    The first array has three columns: two numeric features and a string
    label. This represents supervised data because we already know which
    class each row belongs to. The second array has only the two numeric
    features. Without the label column, the model has nothing to "learn
    toward," which is the unsupervised scenario. The key takeaway is
    that the presence or absence of a target column is what determines
    which approach you use.
    """)
    return


# ===========================================================================
# CONCEPT 2 -- K-Nearest Neighbors (KNN) Algorithm
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 2. K-Nearest Neighbors (KNN) Algorithm

    **What it is:**
    KNN is a simple supervised algorithm that makes predictions by
    finding the K training points that are closest (nearest) to a new
    data point and letting those neighbors vote on the outcome.

    - It is a **lazy learner** -- it stores all training data and does
      no computation until a prediction is needed.
    - It is **non-parametric** -- it makes no assumptions about the
      shape of the data distribution.

    **How it works (step by step):**
    1. Calculate the distance from the new point to every training point
       (most commonly Euclidean distance: sqrt of sum of squared diffs).
    2. Sort those distances and pick the K smallest (the K nearest neighbors).
    3. For **classification**: majority vote among the K neighbors decides the class.
       For **regression**: average the K neighbors' target values.

    **The key hyperparameter is K.** A small K is more sensitive to
    noise; a large K is smoother but may miss local patterns.
    """)
    return


@app.cell
def _(np):
    # Reproduce the KNN logic from the source file
    training_data = np.array([
        (5, 3, 0), (10, 15, 0), (15, 12, 0), (24, 10, 0), (30, 45, 0),
        (55, 52, 1), (60, 78, 1), (71, 80, 1), (80, 91, 1), (85, 70, 1)
    ])

    def run_knn(k, test_point, data):
        # Step 1: Euclidean distance from test_point to every training point
        distances = np.sqrt(np.sum((data[:, :2] - test_point) ** 2, axis=1))
        # Step 2: indices of the K nearest neighbors
        nearest_indices = np.argsort(distances)[:k]
        # Step 3: majority vote on class label
        classes = data[nearest_indices, 2].astype(int)
        prediction = np.bincount(classes).argmax()
        return prediction, nearest_indices

    test_point = np.array([45, 50])
    pred, neighbors = run_knn(k=3, test_point=test_point, data=training_data)
    label = "Red" if pred == 1 else "Purple"
    print(f"Test point {test_point} classified as: {label}")
    print(f"Neighbor indices used: {neighbors}")
    return label, neighbors, pred, run_knn, test_point, training_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    `run_knn` mirrors the implementation in the source file exactly.
    `np.sqrt(np.sum(..., axis=1))` computes Euclidean distance from
    the test point to every row in the training data simultaneously.
    `np.argsort` returns indices that would sort the distances array,
    so slicing `[:k]` gives the K rows with the smallest distances.
    `np.bincount(...).argmax()` counts how many neighbors belong to
    each class and returns the class with the highest count -- that is
    the majority vote. With K=3 and test point (45, 50), two of the
    three nearest neighbors belong to the Red class, so the point is
    classified as Red.
    """)
    return


# ===========================================================================
# CONCEPT 3 -- KNN Regressor vs KNN Classifier
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3. KNN Regressor vs KNN Classifier

    **What it is:**
    The KNN algorithm can be applied to two different kinds of targets,
    and scikit-learn provides separate classes for each.

    | Class | Target type | Prediction method |
    |---|---|---|
    | `KNeighborsRegressor` | Continuous (e.g., mpg) | Average of K neighbors |
    | `KNeighborsClassifier` | Discrete category (e.g., species) | Majority vote of K neighbors |

    **Why the distinction matters:**
    If you use a regressor on a categorical target, the averaged
    numeric output will not correspond to any valid class. Choosing the
    correct class prevents meaningless predictions.
    """)
    return


@app.cell
def _(KNeighborsClassifier, KNeighborsRegressor, np):
    # Simple side-by-side demo
    X_demo = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
    y_reg  = np.array([1.2, 2.1, 2.9, 4.0, 5.1, 6.0, 6.8, 8.2])   # continuous
    y_cls  = np.array([0,   0,   0,   0,   1,   1,   1,   1  ])    # discrete

    reg = KNeighborsRegressor(n_neighbors=3)
    reg.fit(X_demo, y_reg)

    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_demo, y_cls)

    test = np.array([[4.5]])
    print(f"Regressor prediction for x=4.5 : {reg.predict(test)[0]:.2f}  (continuous output)")
    print(f"Classifier prediction for x=4.5: {clf.predict(test)[0]}       (class label output)")
    return X_demo, clf, reg, test, y_cls, y_reg


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    Both models are fit on the same 8 training points but with
    different targets -- one continuous and one binary. When asked to
    predict for x=4.5, the regressor averages the target values of the
    3 nearest neighbors, producing a decimal number. The classifier
    takes a majority vote among those same 3 neighbors and returns the
    winning integer class label. The outputs confirm that the two
    variants solve fundamentally different problems even though the
    underlying distance logic is identical.
    """)
    return


# ===========================================================================
# CONCEPT 4 -- Loading Data and Exploratory Data Analysis (EDA)
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4. Loading Data and EDA Before Modeling

    **What it is:**
    Before building any model, the source file performs a brief EDA
    step using a correlation heatmap. This is used to decide which
    features are worth keeping and which can be dropped.

    **Why it matters:**
    Including irrelevant or weakly correlated features adds noise and
    can reduce model accuracy. The correlation matrix is a quick way to
    see which numeric columns have a strong linear relationship with
    the target variable.

    A correlation value near -1 or +1 indicates a strong relationship.
    A value near 0 indicates little to no linear relationship.
    """)
    return


@app.cell
def _(pd, plt, sns):
    auto = pd.read_csv('auto_dt_nona.csv')
    # Correlation heatmap -- same approach as the source file
    sns.heatmap(auto.corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Auto Dataset Correlation Matrix")
    plt.tight_layout()
    plt.show()
    return (auto,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    `auto.corr()` computes the Pearson correlation coefficient between
    every pair of numeric columns. `sns.heatmap` renders these values
    as a color-coded grid. In the source file, this step revealed that
    mpg has a strong negative correlation with cylinders, displacement,
    horsepower, and weight. Based on that finding, `acceleration`,
    `model.year`, and `origin` were dropped before modeling because
    their correlations with mpg were weaker. Dropping weak features
    keeps the model focused on the most predictive signals.
    """)
    return


# ===========================================================================
# CONCEPT 5 -- Defining Features (X) and Target (y)
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5. Defining Features (X) and Target (y)

    **What it is:**
    Supervised machine learning requires explicitly separating the
    input columns (features, called X) from the output column (target,
    called y).

    - **X** is the matrix of all predictor columns.
    - **y** is the 1-D array of values the model is trying to predict.

    The X/y naming convention is standard across scikit-learn and most
    ML literature. There is nothing magical about the letters; they are
    just a widely adopted shorthand.
    """)
    return


@app.cell
def _(auto, pd):
    # Drop columns not used in the source file
    auto_trimmed = auto.drop(['acceleration', 'model.year', 'origin'], axis=1)
    auto_trimmed = auto_trimmed[['mpg', 'displacement', 'horsepower', 'weight', 'cylinders']]

    array = auto_trimmed.values
    X = array[:, 0:4]   # features: mpg, displacement, horsepower, weight
    y = array[:, 4]     # target: cylinders

    print("X shape (features):", X.shape)
    print("y shape (target) :", y.shape)
    print("\nFirst 3 rows of X:\n", X[:3])
    print("\nFirst 3 values of y:", y[:3])
    return X, array, auto_trimmed, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    `.values` converts the pandas DataFrame into a plain NumPy array.
    Array slicing with `[:, 0:4]` selects all rows and the first four
    columns as features. `[:, 4]` selects all rows of the fifth column
    as the target. The printed shapes confirm X is a 2-D matrix
    (samples x features) and y is a 1-D array (one target per sample),
    which is exactly what scikit-learn models expect.
    """)
    return


# ===========================================================================
# CONCEPT 6 -- Train/Test Split
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 6. Train/Test Split

    **What it is:**
    Before fitting a model, the dataset is split into two non-overlapping
    subsets:

    - **Training set** -- the data the model learns from.
    - **Test set (holdout set)** -- data the model has never seen,
      used only to evaluate final performance.

    **Why it matters:**
    If you evaluate a model on the same data it trained on, you are
    measuring memorization, not generalization. The test set simulates
    "real world" predictions on unseen data.

    **Key parameters:**
    - `test_size` -- fraction of data reserved for testing (0.2 = 20%).
    - `random_state` -- a seed so the split is reproducible every run.
    """)
    return


@app.cell
def _(X, train_test_split, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Full dataset  : {X.shape[0]} rows")
    print(f"Training set  : {X_train.shape[0]} rows  (80%)")
    print(f"Test set      : {X_test.shape[0]} rows  (20%)")
    return X_test, X_train, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    `train_test_split` from scikit-learn randomly shuffles the rows
    and then divides them according to `test_size`. Setting
    `random_state=42` means the same rows will always end up in the
    same split, making the experiment reproducible. The printed counts
    confirm the 80/20 split. The training data is passed to `.fit()`;
    the test data is held back until evaluation time.
    """)
    return


# ===========================================================================
# CONCEPT 7 -- Fitting a Model and Making Predictions
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 7. Fitting a Model and Making Predictions

    **What it is:**
    Once the data is split, you instantiate a model object, call
    `.fit(X_train, y_train)` to train it, and then call
    `.predict(X_test)` to generate predictions.

    **How it works:**
    - `.fit` stores all training points (for KNN) or computes model
      parameters (for other algorithms).
    - `.predict` runs the learned logic on new inputs and returns
      an array of predictions, one per row of X_test.
    """)
    return


@app.cell
def _(KNeighborsRegressor, X_test, X_train, r2_score, y_test, y_train):
    model = KNeighborsRegressor(n_neighbors=3, n_jobs=-1)
    model.fit(X_train, y_train)          # train
    preds = model.predict(X_test)        # predict

    print("First 5 actual values :", y_test[:5])
    print("First 5 predictions   :", preds[:5].round(2))
    print(f"\nR-squared score: {r2_score(y_test, preds):.4f}")
    return model, preds


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    `KNeighborsRegressor(n_neighbors=3)` creates a KNN regressor set
    to use 3 neighbors. `.fit(X_train, y_train)` memorizes all training
    rows. `.predict(X_test)` loops through each test row, finds its 3
    nearest training neighbors, and returns their average target value.
    Comparing the printed actuals and predictions gives a qualitative
    sense of accuracy. The R-squared score at the end formalizes this
    -- a score of 1.0 is perfect; 0.0 means the model is no better
    than always predicting the mean.
    """)
    return


# ===========================================================================
# CONCEPT 8 -- Model Evaluation: R-Squared
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 8. Model Evaluation: R-Squared (R2) Score

    **What it is:**
    R-squared (coefficient of determination) measures how much of the
    variance in the target variable is explained by the model.

    - Best possible score: **1.0** (perfect predictions).
    - A score of **0.0** means the model does no better than always
      predicting the mean of y.
    - Negative scores are possible and mean the model is actively worse
      than the mean baseline.

    **When to use it:**
    R2 is the standard evaluation metric for regression problems. Use
    `sklearn.metrics.r2_score` or call `model.score(X_test, y_test)`
    directly (which returns R2 for KNN regressors).
    """)
    return


@app.cell
def _(KNeighborsRegressor, X_test, X_train, plt, r2_score, y_test, y_train):
    # Loop through k values and record R2 -- mirrors the source file exactly
    scores = []
    for k_val in range(2, 20):
        m = KNeighborsRegressor(n_neighbors=k_val, n_jobs=-1)
        m.fit(X_train, y_train)
        scores.append(m.score(X_test, y_test))

    plt.plot(range(2, 20), scores, marker='o')
    plt.xticks(range(2, 20))
    plt.xlabel("K (number of neighbors)")
    plt.ylabel("R2 Score")
    plt.title("R2 Score vs K Value")
    plt.grid()
    plt.show()

    best_k = range(2, 20)[scores.index(max(scores))]
    print(f"Best K: {best_k}  |  Best R2: {max(scores):.4f}")
    return best_k, scores


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    This loop tries every K from 2 to 19, fits a fresh KNN model for
    each, and records the R2 score on the test set. Plotting the
    results shows how model accuracy changes with K. The source file
    found that K=13 produced the highest R2 (approximately 0.79),
    which is why the final model in that file uses 13 neighbors. The
    plot is a visual "elbow chart" for selecting the optimal
    hyperparameter.
    """)
    return


# ===========================================================================
# CONCEPT 9 -- K-Fold Cross-Validation
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 9. K-Fold Cross-Validation

    **What it is:**
    K-fold cross-validation is a technique that reduces the variance
    (luck) in a single train/test split by repeating the evaluation
    multiple times on different subsets of the data.

    **How it works:**
    1. Split the dataset into K equal parts (folds).
    2. For each fold: train on all other folds, test on that one fold.
    3. Collect K performance scores and summarize with mean and
       standard deviation.

    **Why it is the "gold standard":**
    Every row gets to be in the test set exactly once. This gives a
    much more reliable estimate of how the model will perform on truly
    unseen data. K is typically set to 5 or 10.

    The reported mean is the expected accuracy; the std dev tells you
    how stable that accuracy is across different data splits.
    """)
    return


@app.cell
def _(KFold, KNeighborsRegressor, X, cross_val_score, np, y):
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    knn_model = KNeighborsRegressor(n_neighbors=13, n_jobs=-1)

    cv_scores = cross_val_score(knn_model, X, y, cv=kf, scoring='r2')

    print("R2 score for each fold:", cv_scores.round(4))
    print(f"Mean R2  : {np.mean(cv_scores):.4f}")
    print(f"Std Dev  : {np.std(cv_scores):.4f}")
    return cv_scores, kf, knn_model


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    `KFold(n_splits=5, shuffle=True, random_state=42)` creates an
    object that defines how to partition the data into 5 folds.
    `cross_val_score` automates the train/test loop: it fits and
    scores the model once per fold and returns an array of 5 scores.
    The mean of those scores is the best single-number summary of
    model performance. A small standard deviation means the model is
    consistent regardless of which data ends up in the test fold.
    """)
    return


# ===========================================================================
# CONCEPT 10 -- StandardScaler and Pipeline
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 10. StandardScaler and Pipeline

    **What it is:**
    Some algorithms (especially KNN and SVR) are sensitive to the
    scale of features. A column measured in thousands (like weight)
    will dominate distance calculations over a column measured in
    single digits (like cylinders). `StandardScaler` fixes this by
    transforming each feature to have mean=0 and standard deviation=1.

    A `Pipeline` chains preprocessing steps and a model into a single
    object. This is important because the scaler must be fit only on
    training data; using a pipeline inside cross-validation ensures
    the scaler never "sees" test data during fitting, which prevents
    data leakage.

    **Key rule:** Always scale inside a pipeline when using
    cross-validation, not before.
    """)
    return


@app.cell
def _(KFold, SVR, StandardScaler, X, cross_val_score, make_pipeline, np, y):
    pipeline = make_pipeline(StandardScaler(), SVR())
    kf2 = KFold(n_splits=5, shuffle=True, random_state=42)
    scaled_scores = cross_val_score(
        pipeline, X, y, cv=kf2, scoring='neg_mean_squared_error'
    )
    rmse = np.sqrt(-scaled_scores)
    print("RMSE per fold:", rmse.round(4))
    print(f"Mean RMSE: {rmse.mean():.4f}")
    print(f"Std Dev  : {rmse.std():.4f}")
    return kf2, pipeline, rmse, scaled_scores


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    `make_pipeline(StandardScaler(), SVR())` creates a two-step
    pipeline: first scale the features, then train the SVR model.
    When `cross_val_score` runs each fold, the pipeline fits the
    scaler on the training folds only and applies that learned scaling
    to the test fold. This is correct practice. The scoring metric
    `neg_mean_squared_error` returns negative MSE (scikit-learn
    convention for metrics where higher is better). Taking
    `np.sqrt(-scores)` converts it back to RMSE in the original units
    (mpg for this dataset). Lower RMSE is better.
    """)
    return


# ===========================================================================
# CONCEPT 11 -- Comparing Multiple Regression Algorithms
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 11. Comparing Multiple Regression Algorithms

    **What it is:**
    No single algorithm is universally best. The source file compares
    seven regression algorithms on the same dataset using the same
    K-fold cross-validation setup so the comparison is fair.

    **Algorithms compared:**

    | Category | Algorithm |
    |---|---|
    | Linear | Linear Regression, Lasso, Elastic Net |
    | Non-linear | KNN, Decision Tree, SVR, Random Forest |

    **How to read the results:**
    Lower average RMSE = better average prediction error. The standard
    deviation column shows how consistent the algorithm is across folds.
    """)
    return


@app.cell
def _(
    DecisionTreeRegressor, ElasticNet, KFold, KNeighborsRegressor,
    Lasso, LinearRegression, RandomForestRegressor, SVR, StandardScaler,
    X, cross_val_score, make_pipeline, np, pd, plt, sns, y,
):
    model_map = {
        "Linear Regression": LinearRegression(),
        "Lasso"            : Lasso(),
        "Elastic Net"      : ElasticNet(),
        "KNN"              : KNeighborsRegressor(),
        "Decision Tree"    : DecisionTreeRegressor(),
        "SVR"              : SVR(),
        "Random Forest"    : RandomForestRegressor(),
    }

    all_results = []
    kf3 = KFold(n_splits=5, shuffle=True, random_state=42)
    for name, mdl in model_map.items():
        pipe = make_pipeline(StandardScaler(), mdl)
        s = cross_val_score(pipe, X, y, cv=kf3, scoring='neg_mean_squared_error')
        rmse_s = np.sqrt(-s)
        all_results.append({"Model": name, "Avg RMSE": rmse_s.mean(), "Std Dev": rmse_s.std()})

    comparison_df = pd.DataFrame(all_results).sort_values("Avg RMSE")
    print(comparison_df.to_string(index=False))

    sns.barplot(x="Avg RMSE", y="Model", data=comparison_df, palette="viridis")
    plt.title("Regression Model Comparison (5-fold CV, scaled)")
    plt.xlabel("Avg RMSE (lower is better)")
    plt.tight_layout()
    plt.show()
    return all_results, comparison_df, kf3, model_map, name, pipe


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    Each model is wrapped in a pipeline with `StandardScaler` before
    being evaluated with `cross_val_score`. This ensures every model
    receives identically scaled data, making the comparison fair.
    Results are collected into a DataFrame, sorted by RMSE, and
    visualized as a horizontal bar chart. The bar chart makes it easy
    to see at a glance which algorithm produces the lowest average
    prediction error. In the source file, Random Forest came out on
    top among these "simple" algorithms even without any tuning.
    """)
    return


# ===========================================================================
# CONCEPT 12 -- Ensemble Methods (Boosting and Bagging)
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 12. Ensemble Methods: Boosting and Bagging

    **What it is:**
    Ensemble methods combine many "weak" models to produce a stronger
    overall model. The source file covers two families:

    **Boosting** trains models sequentially. Each new model focuses
    on the errors of the previous one.
    - `AdaBoostRegressor` -- re-weights misclassified points so future
      models pay more attention to them.
    - `GradientBoostingRegressor` -- minimizes the loss function
      (prediction error) step by step, following the gradient.

    **Bagging** (Bootstrap Aggregating) trains many models in parallel
    on random sub-samples of the data and averages their results.
    - `RandomForestRegressor` -- a forest of decision trees, each
      trained on a bootstrap sample and a random subset of features.
    - `ExtraTreesRegressor` -- similar to Random Forest but uses
      random thresholds for splits, adding more randomness and often
      reducing variance further.
    """)
    return


@app.cell
def _(
    AdaBoostRegressor, ExtraTreesRegressor, GradientBoostingRegressor,
    KFold, RandomForestRegressor, StandardScaler, X_train,
    cross_val_score, np, y_train,
):
    from matplotlib import pyplot
    ensembles = [
        ('AdaBoost',        AdaBoostRegressor()),
        ('GradientBoosting', GradientBoostingRegressor()),
        ('RandomForest',    RandomForestRegressor(n_estimators=10)),
        ('ExtraTrees',      ExtraTreesRegressor(n_estimators=10)),
    ]

    results_ens = []
    names_ens   = []
    kf_ens = KFold(n_splits=5, shuffle=True, random_state=42)

    for ens_name, ens_model in ensembles:
        from sklearn.pipeline import Pipeline as _Pipe
        ens_pipe = _Pipe([('scaler', StandardScaler()), ('model', ens_model)])
        cv_ens = cross_val_score(ens_pipe, X_train, y_train,
                                 cv=kf_ens, scoring='neg_mean_squared_error')
        rmse_ens = np.sqrt(-cv_ens)
        results_ens.append(rmse_ens)
        names_ens.append(ens_name)
        print(f"{ens_name}: mean={rmse_ens.mean():.4f}  std={rmse_ens.std():.4f}")

    fig_ens = pyplot.figure()
    fig_ens.suptitle("Ensemble Algorithm Comparison (RMSE)")
    ax_ens = fig_ens.add_subplot(111)
    pyplot.boxplot(results_ens)
    ax_ens.set_xticklabels(names_ens, rotation=15)
    pyplot.ylabel("RMSE (lower is better)")
    pyplot.show()
    return (
        ax_ens, ens_model, ens_name, ens_pipe, ensembles, fig_ens,
        kf_ens, names_ens, pyplot, results_ens,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    Each ensemble is placed inside a pipeline with `StandardScaler`
    and evaluated with 5-fold cross-validation. The box plot shows the
    distribution of RMSE across the 5 folds for each algorithm. A
    shorter box with a lower median is ideal -- it indicates low error
    and high consistency. In the source file, even un-tuned ensemble
    methods outperformed most of the simple algorithms in Concept 11,
    which illustrates why ensemble methods are popular in practice.
    """)
    return


# ===========================================================================
# CONCEPT 13 -- KNN Classifier and Dummy Encoding
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 13. KNN Classifier and Dummy Encoding Categorical Features

    **What it is:**
    KNN (and most ML algorithms) only work with numeric data.
    When a dataset contains categorical columns (strings or boolean
    categories), they must be converted to numbers before fitting.

    `pd.get_dummies` (one-hot encoding) creates one binary column per
    category level. For example, a column `island` with values
    `Biscoe`, `Dream`, `Torgersen` becomes three columns:
    `island_Biscoe`, `island_Dream`, `island_Torgersen`, each
    containing 0 or 1.

    **Important rule:** Do NOT encode the target column. Only encode
    the feature columns. The target stays as-is for the model to learn.
    """)
    return


@app.cell
def _(KNeighborsClassifier, pd, plt, sns, train_test_split):
    penguins = sns.load_dataset('penguins')
    penguins_clean = penguins[penguins.body_mass_g.notna()]
    penguins_clean = penguins_clean[penguins_clean.sex.notna()]

    # Encode island and sex but NOT species (the target)
    peng_encoded = pd.get_dummies(penguins_clean, columns=['island', 'sex'],
                                  prefix=['island', 'sex'])
    print("Columns after encoding:", list(peng_encoded.columns))

    arr = peng_encoded.values
    X_p = arr[:, 1:]    # all columns except species
    y_p = arr[:, 0]     # species column

    X_tr_p, X_te_p, y_tr_p, y_te_p = train_test_split(
        X_p, y_p, test_size=0.2, random_state=42
    )

    # Find best K
    scores_p = []
    for k_p in range(2, 20):
        clf_p = KNeighborsClassifier(n_neighbors=k_p, n_jobs=-1)
        clf_p.fit(X_tr_p, y_tr_p)
        scores_p.append(clf_p.score(X_te_p, y_te_p))

    plt.plot(range(2, 20), scores_p, marker='o')
    plt.xticks(range(2, 20))
    plt.xlabel("K")
    plt.ylabel("Accuracy")
    plt.title("KNN Classifier: Accuracy vs K (Penguin Species)")
    plt.grid()
    plt.show()
    print(f"Best K: {range(2,20)[scores_p.index(max(scores_p))]}  |  Max accuracy: {max(scores_p)*100:.1f}%")
    return (
        X_p, X_te_p, X_tr_p, arr, clf_p, k_p, peng_encoded,
        penguins, penguins_clean, scores_p, y_p, y_te_p, y_tr_p,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    After removing rows with missing values, `pd.get_dummies` expands
    the two categorical columns into binary indicator columns. The
    target (`species`) is excluded from encoding because the model
    needs to predict it, not learn it as a numeric pattern. The K-loop
    then evaluates classifier accuracy (fraction of test rows correctly
    classified) for each K. The source file found K=8 gave the highest
    accuracy. Unlike the regression case where `.score` returns R2,
    `KNeighborsClassifier.score` returns classification accuracy
    (correct predictions / total predictions).
    """)
    return


# ===========================================================================
# CONCEPT 14 -- Comparing Multiple Classifier Algorithms
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 14. Comparing Multiple Classifier Algorithms

    **What it is:**
    Just as with regression, the source file compares a range of
    classification algorithms on the same dataset to find the best
    performer. The evaluation metric switches from RMSE to accuracy
    (because the target is now a discrete class, not a continuous value).

    **Algorithms compared:**

    | Category | Algorithm |
    |---|---|
    | Linear | Logistic Regression, Linear Discriminant Analysis |
    | Non-linear | KNN, Decision Tree, Gaussian Naive Bayes, SVM |
    | Ensemble (Boosting) | AdaBoost, Gradient Boosting |
    | Ensemble (Bagging) | Random Forest, Extra Trees |

    **How to read results:** Higher accuracy = better. Standard
    deviation shows consistency across folds.
    """)
    return


@app.cell
def _(
    AdaBoostClassifier, DecisionTreeClassifier, ExtraTreesClassifier,
    GaussianNB, GradientBoostingClassifier, KFold, KNeighborsClassifier,
    LinearDiscriminantAnalysis, LogisticRegression, RandomForestClassifier,
    SVC, X, cross_val_score, make_pipeline, np, pd, plt, sns, y,
):
    clf_map = {
        "Logistic Regression"         : LogisticRegression(),
        "Linear Discriminant Analysis": LinearDiscriminantAnalysis(),
        "KNN"                         : KNeighborsClassifier(),
        "Decision Tree"               : DecisionTreeClassifier(),
        "Gaussian Naive Bayes"        : GaussianNB(),
        "SVM"                         : SVC(gamma='auto'),
        "AdaBoost"                    : AdaBoostClassifier(),
        "Gradient Boosting"           : GradientBoostingClassifier(),
        "Random Forest"               : RandomForestClassifier(n_estimators=10),
        "Extra Trees"                 : ExtraTreesClassifier(n_estimators=10),
    }

    clf_results = []
    kf_clf = KFold(n_splits=5, shuffle=True, random_state=42)

    for clf_name, clf_mdl in clf_map.items():
        clf_pipe = make_pipeline(clf_mdl)
        s_clf = cross_val_score(clf_pipe, X, y, cv=kf_clf, scoring='accuracy',
                                error_score='raise')
        clf_results.append({
            "Model"   : clf_name,
            "Accuracy": s_clf.mean(),
            "Std Dev" : s_clf.std()
        })

    clf_df = pd.DataFrame(clf_results).sort_values("Accuracy", ascending=False)
    print(clf_df.to_string(index=False))

    sns.barplot(x="Accuracy", y="Model", data=clf_df, palette="magma")
    plt.title("Classifier Comparison (5-fold CV)")
    plt.xlabel("Average Accuracy (higher is better)")
    plt.tight_layout()
    plt.show()
    return (
        clf_df, clf_map, clf_mdl, clf_name, clf_pipe, clf_results, kf_clf,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What the code is doing:**
    Each classifier is wrapped in a pipeline and evaluated with
    `cross_val_score` using `scoring='accuracy'`. Accuracy is the
    fraction of test samples the model classified correctly in each
    fold. The results are sorted from best to worst accuracy and
    displayed as a bar chart. Notice that unlike the regression
    comparison, no `StandardScaler` is included in the pipeline for
    the linear models (which is valid for tree-based methods) -- the
    source file's classifier section uses simpler pipelines to
    demonstrate that even without scaling, some algorithms can still
    perform well. The ensemble methods (AdaBoost, GBM, RF, ET) are
    typically among the top performers.
    """)
    return


# ===========================================================================
# CONCEPT 15 -- Recap: Algorithm Selection and Tuning
# ===========================================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 15. Recap: Algorithm Selection, Scaling, and Tuning

    **What it is:**
    The source file closes with a summary of three key lessons from
    the week's work.

    **1. Many algorithms exist for a reason.**
    No single algorithm always wins. Different algorithms make
    different assumptions about data shape, noise, and feature
    relationships. Testing multiple algorithms (as done in Concepts 11
    and 14) is the practical way to find the best one for your data.

    **2. Scaling and normalization can improve accuracy.**
    Some algorithms (KNN, SVR, logistic regression) rely on distances
    or gradient calculations that are thrown off by features on very
    different numeric scales. Applying `StandardScaler` (mean=0,
    std=1) levels the playing field. It might not always help, but
    it rarely hurts and is easy to test with a pipeline.

    **3. Hyperparameter tuning matters.**
    Every algorithm has settings that can be adjusted:
    - KNN has K (number of neighbors).
    - Random Forest has `n_estimators` (number of trees).
    - SVM has C and gamma.

    The K-loop in Concepts 8 and 13 is a simple example of manual
    hyperparameter search. `GridSearchCV` and `RandomizedSearchCV`
    automate this process for more complex cases.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Summary table of all concepts covered:**

    | # | Concept | Key Tool |
    |---|---|---|
    | 1 | Supervised vs Unsupervised | Conceptual |
    | 2 | KNN Algorithm | Custom numpy implementation |
    | 3 | Regressor vs Classifier | `KNeighborsRegressor` / `KNeighborsClassifier` |
    | 4 | EDA Before Modeling | `sns.heatmap`, `auto.corr()` |
    | 5 | Features and Target | Array slicing, X / y convention |
    | 6 | Train/Test Split | `train_test_split` |
    | 7 | Fit and Predict | `.fit()`, `.predict()` |
    | 8 | R-Squared Score | `r2_score`, K-loop |
    | 9 | K-Fold Cross-Validation | `KFold`, `cross_val_score` |
    | 10 | StandardScaler and Pipeline | `StandardScaler`, `make_pipeline` |
    | 11 | Comparing Regression Algorithms | Multiple sklearn regressors |
    | 12 | Ensemble Methods | `AdaBoost`, `GBM`, `RandomForest`, `ExtraTrees` |
    | 13 | Classifier and Dummy Encoding | `pd.get_dummies`, `KNeighborsClassifier` |
    | 14 | Comparing Classifier Algorithms | Multiple sklearn classifiers |
    | 15 | Recap: Selection and Tuning | Conceptual summary |
    """)
    return


if __name__ == "__main__":
    app.run()
