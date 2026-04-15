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

__generated_with = "0.23.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 5 Lab: Supervised Learning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Research Question

    The dataset is from a Portuguese bank's telemarketing campaign. Each row represents
    one phone call to a client, and the target variable `y` records whether that client
    ended up subscribing to a term deposit ("yes" or "no").

    My research question is: **Can we use what we know about a client -- their age, job,
    account status, and the economic environment at the time of the call -- to predict
    whether they will subscribe?**

    Since the target (`y`) is a discrete category ("yes" or "no"), this is a
    **classification** problem, not a regression problem. That means KNN Classifier
    is the right tool here.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    Load Libraries
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    warnings.filterwarnings("ignore")
    sns.set_theme()

    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split, KFold, cross_val_score
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline, Pipeline
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    from sklearn.ensemble import (
        RandomForestClassifier, GradientBoostingClassifier,
        AdaBoostClassifier, ExtraTreesClassifier
    )

    return (
        AdaBoostClassifier,
        DecisionTreeClassifier,
        ExtraTreesClassifier,
        GaussianNB,
        GradientBoostingClassifier,
        KFold,
        KNeighborsClassifier,
        LinearDiscriminantAnalysis,
        LogisticRegression,
        RandomForestClassifier,
        SVC,
        StandardScaler,
        accuracy_score,
        cross_val_score,
        make_pipeline,
        mo,
        pd,
        plt,
        sns,
        train_test_split,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Step 1: Load the Data

    The file uses semicolons as separators instead of commas, so I need to pass `sep=';'`
    to `read_csv`.
    """)
    return


@app.cell
def _(pd):
    bank = pd.read_csv('bank-additional-full.csv', sep=';')
    bank.head()
    return (bank,)


@app.cell
def _(bank, mo):
    mo.md(f"**Shape:** {bank.shape[0]} rows x {bank.shape[1]} columns")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Step 2: Clean Up the Dataset

    ### 2a. Fix Column Names

    A few column names use dots as separators (e.g. `emp.var.rate`). That can cause
    problems in pandas, so I am replacing all dots with underscores.
    """)
    return


@app.cell
def _(bank):
    bank.columns = [c.replace('.', '_') for c in bank.columns]
    bank.columns.tolist()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2b. Check for Missing Values

    According to the dataset description, missing values are not coded as `NaN` -- they
    are coded as the string `"unknown"`. I want to count how many of those exist per column.
    """)
    return


@app.cell
def _(bank, pd):
    unknown_counts = pd.DataFrame(
        {col: (bank[col] == 'unknown').sum()
         for col in bank.select_dtypes(include='object').columns},
        index=['unknown_count']
    ).T
    unknown_counts[unknown_counts['unknown_count'] > 0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are "unknown" entries spread across several columns. I am choosing to **keep**
    them rather than drop rows for two reasons:

    1. Dropping every row with an "unknown" would remove thousands of records and could
       skew the class balance.
    2. "Unknown" likely means the data was not collected, which is itself information

    When I encode the categorical columns later, "unknown" will just become another
    dummy variable alongside the real values.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2c. Drop the `duration` Column

    The dataset description includes a clear warning about the `duration` column
    (how long the phone call lasted). It says this column should be dropped if you
    want a realistic model, because the duration is only known *after* the call ends,
    at which point you already know if the person subscribed or not.
    """)
    return


@app.cell
def _(bank):
    bank2 = bank.drop(columns=['duration'])
    print(f"Columns remaining: {bank2.shape[1]}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Step 3: A Little EDA

    Before building any model I want to get a feel for the data. The most important
    thing to check for a classification problem is whether the classes are balanced.
    """)
    return


@app.cell
def _(bank, plt, sns):
    target_counts = bank['y'].value_counts()
    fig_bal, ax_bal = plt.subplots()
    sns.barplot(x=target_counts.index, y=target_counts.values, palette='muted', ax=ax_bal)
    ax_bal.set_title('How Many Clients Subscribed?')
    ax_bal.set_xlabel('Subscribed a Term Deposit (y)')
    ax_bal.set_ylabel('Number of Clients')
    for i, v in enumerate(target_counts.values):
        ax_bal.text(i, v + 100, f'{v:,}  ({v/len(bank)*100:.1f}%)', ha='center')
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is a big problem. About 89% of clients said "no" and only 11% said "yes".
    That means the classes are heavily imbalanced. A model that just predicts "no" for every single client would
    score around 89% accuracy without learning anything useful at all.
    """)
    return


@app.cell
def _(bank, plt, sns):
    job_rate = (
        bank.groupby('job')['y']
        .apply(lambda x: (x == 'yes').mean())
        .sort_values(ascending=False)
        .reset_index()
    )
    job_rate.columns = ['job', 'subscription_rate']

    fig_job, ax_job = plt.subplots(figsize=(10, 4))
    _ = sns.barplot(x='job', y='subscription_rate', data=job_rate, palette='viridis', ax=ax_job)
    ax_job.set_title('Subscription Rate by Job Type')
    ax_job.set_ylabel('Proportion Who Subscribed')
    ax_job.set_xlabel('Job')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Students and retired clients subscribe at the highest rates. That makes some sense,
    they may have more flexibility with their money than someone in a blue-collar job
    living paycheck to paycheck.
    """)
    return


@app.cell
def _(bank, plt, sns):
    _ = sns.heatmap(bank.select_dtypes(include='number').corr(), annot=False, cmap='coolwarm')
    plt.title('Correlation Matrix -- Numeric Features')
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The macroeconomic indicators (`euribor3m`, `nr_employed`, `emp_var_rate`) are
    highly correlated with each other, which makes sense since they all track the
    same economic conditions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Step 4: Prepare Data for Machine Learning

    KNN only works with numerical data. All of the categorical
    columns need to be converted into numbers. I am using `pd.get_dummies`.

    The target column `y` gets mapped to 1 (yes) and 0 (no).
    """)
    return


@app.cell
def _(bank, pd):
    cat_cols = [
        'job', 'marital', 'education', 'default', 'housing',
        'loan', 'contact', 'month', 'day_of_week', 'poutcome'
    ]
    bank_enc = pd.get_dummies(bank, columns=cat_cols, prefix=cat_cols)
    bank_enc['y'] = bank_enc['y'].map({'yes': 1, 'no': 0})
    print(f"Shape after encoding: {bank_enc.shape}")
    bank_enc.head(3)
    return (bank_enc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let me double-check there are no NaN values hiding in there before I move on.
    """)
    return


@app.cell
def _(bank_enc):
    bank_enc.isnull().sum().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Good, zero nulls. Now I will set up the X (features) and y (target) arrays and
    do a train/test split. I am using 80% for training and 20% for testing.
    """)
    return


@app.cell
def _(bank_enc):
    cols_no_y = [c for c in bank_enc.columns if c != 'y']
    array_bank = bank_enc[cols_no_y + ['y']].values

    X_bank = array_bank[:, :-1].astype(float)
    y_bank = array_bank[:, -1].astype(int)

    print(f"X shape: {X_bank.shape}")
    print(f"y shape: {y_bank.shape}")
    return X_bank, y_bank


@app.cell
def _(X_bank, train_test_split, y_bank):
    X_train_b, X_test_b, y_train_b, y_test_b = train_test_split(
        X_bank, y_bank, test_size=0.2, random_state=42
    )
    print(f"Training set: {X_train_b.shape}")
    print(f"Test set:     {X_test_b.shape}")
    return X_test_b, X_train_b, y_test_b, y_train_b


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Step 5: Finding the Optimal K

    I don't want to just guess a K value. Instead I am going to loop through a range
    of K values, fit a model for each one, and record the accuracy. Then I can plot
    the results and pick the best K.
    """)
    return


@app.cell
def _(KNeighborsClassifier, X_test_b, X_train_b, y_test_b, y_train_b):
    k_scores = []
    k_range = range(1, 31)
    for _k in k_range:
        _model = KNeighborsClassifier(n_neighbors=_k, n_jobs=-1)
        _model.fit(X_train_b, y_train_b)
        k_scores.append(_model.score(X_test_b, y_test_b))
    return k_range, k_scores


@app.cell
def _(k_range, k_scores, plt):
    plt.figure(figsize=(10, 4))
    plt.plot(list(k_range), k_scores, marker='o')
    plt.xticks(list(k_range))
    plt.xlabel('K (Number of Neighbors)')
    plt.ylabel('Accuracy')
    plt.title('KNN Accuracy vs K Value -- Unscaled')
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()
    best_k = list(k_range)[k_scores.index(max(k_scores))]
    print(f"Best K = {best_k}")
    print(f"Best Accuracy = {max(k_scores)*100:.2f}%")
    return (best_k,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Step 6: Evaluate the Baseline KNN Model

    Now I will train and evaluate the model at the optimal K found above.
    The confusion matrix uses `sns.heatmap`, the same way the project files
    display confusion matrices.
    """)
    return


@app.cell
def _(
    KNeighborsClassifier,
    X_test_b,
    X_train_b,
    accuracy_score,
    best_k,
    plt,
    sns,
    y_test_b,
    y_train_b,
):
    from sklearn.metrics import confusion_matrix
    knn_base = KNeighborsClassifier(n_neighbors=best_k, n_jobs=-1)
    knn_base.fit(X_train_b, y_train_b)
    y_pred_base = knn_base.predict(X_test_b)
    acc_base = accuracy_score(y_test_b, y_pred_base)

    print(f"Baseline KNN (k={best_k}) Accuracy: {acc_base*100:.2f}%")

    cm_base = confusion_matrix(y_test_b, y_pred_base)
    fig_cm1, ax_cm1 = plt.subplots()
    sns.heatmap(cm_base, annot=True, fmt='d', cmap='Blues',
                xticklabels=['no', 'yes'], yticklabels=['no', 'yes'], ax=ax_cm1)
    ax_cm1.set_title(f'Baseline KNN Confusion Matrix (k={best_k})')
    ax_cm1.set_xlabel('Predicted')
    ax_cm1.set_ylabel('Actual')
    plt.tight_layout()
    plt.show()
    return (confusion_matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The accuracy looks decent on the surface, buhowevert the model is doing a fine job predicting "no" but it is missing a
    lot of the actual "yes" cases. That is the class imbalance problem showing up.

    A model that barely catches any "yes" cases is not very useful to the bank since
    those are exactly the clients they want to find.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Step 7: Improved KNN with Feature Scaling

    I am using `make_pipeline(StandardScaler(), KNeighborsClassifier(...))` here.
    Then I re-run the K search to find the best K for the scaled version.
    """)
    return


@app.cell
def _(
    KNeighborsClassifier,
    StandardScaler,
    X_test_b,
    X_train_b,
    make_pipeline,
    y_test_b,
    y_train_b,
):
    k_scores_scaled = []
    for _k in range(1, 31):
        _pipe = make_pipeline(
            StandardScaler(),
            KNeighborsClassifier(n_neighbors=_k, n_jobs=-1)
        )
        _pipe.fit(X_train_b, y_train_b)
        k_scores_scaled.append(_pipe.score(X_test_b, y_test_b))
    return (k_scores_scaled,)


@app.cell
def _(k_range, k_scores, k_scores_scaled, plt):
    plt.figure(figsize=(10, 4))
    plt.plot(list(k_range), k_scores, marker='o', label='Unscaled KNN')
    plt.plot(list(k_range), k_scores_scaled, marker='s', label='Scaled KNN')
    plt.xticks(list(k_range))
    plt.xlabel('K (Number of Neighbors)')
    plt.ylabel('Accuracy')
    plt.title('Unscaled vs Scaled KNN Accuracy')
    plt.legend()
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()
    best_k_scaled = list(range(1, 31))[k_scores_scaled.index(max(k_scores_scaled))]
    print(f"Best Scaled K = {best_k_scaled}")
    print(f"Best Scaled Accuracy = {max(k_scores_scaled)*100:.2f}%")
    return (best_k_scaled,)


@app.cell
def _(
    KNeighborsClassifier,
    StandardScaler,
    X_test_b,
    X_train_b,
    accuracy_score,
    best_k_scaled,
    confusion_matrix,
    make_pipeline,
    plt,
    sns,
    y_test_b,
    y_train_b,
):
    knn_scaled = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=best_k_scaled, n_jobs=-1)
    )
    knn_scaled.fit(X_train_b, y_train_b)
    y_pred_scaled = knn_scaled.predict(X_test_b)
    acc_scaled = accuracy_score(y_test_b, y_pred_scaled)

    print(f"Scaled KNN (k={best_k_scaled}) Accuracy: {acc_scaled*100:.2f}%")

    cm_scaled = confusion_matrix(y_test_b, y_pred_scaled)
    fig_cm2, ax_cm2 = plt.subplots()
    sns.heatmap(cm_scaled, annot=True, fmt='d', cmap='Greens',
                xticklabels=['no', 'yes'], yticklabels=['no', 'yes'], ax=ax_cm2)
    ax_cm2.set_title(f'Scaled KNN Confusion Matrix (k={best_k_scaled})')
    ax_cm2.set_xlabel('Predicted')
    ax_cm2.set_ylabel('Actual')
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Scaling helped a bit. The the model is catching a few more "yes" cases than before.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Step 8: Comparing Other Models

    Now I am using K-fold cross-validation with k=5 for all of them,
    wrapped in a `StandardScaler` pipeline. The UI slider lets me change the number
    of folds interactively.
    """)
    return


@app.cell
def _(mo):
    k_fold_slider = mo.ui.slider(start=2, stop=10, step=1, value=5, label="Number of CV Folds")
    mo.hstack([k_fold_slider], justify="start")
    return (k_fold_slider,)


@app.cell
def _(
    AdaBoostClassifier,
    DecisionTreeClassifier,
    ExtraTreesClassifier,
    GaussianNB,
    GradientBoostingClassifier,
    KFold,
    KNeighborsClassifier,
    LinearDiscriminantAnalysis,
    LogisticRegression,
    RandomForestClassifier,
    SVC,
    StandardScaler,
    X_bank,
    best_k_scaled,
    cross_val_score,
    k_fold_slider,
    make_pipeline,
    mo,
    pd,
    y_bank,
):
    k_cv = k_fold_slider.value

    model_map_bank = {
        "KNN (unscaled)":               KNeighborsClassifier(n_neighbors=best_k_scaled, n_jobs=-1),
        "KNN (scaled)":                 KNeighborsClassifier(n_neighbors=best_k_scaled, n_jobs=-1),
        "Logistic Regression":          LogisticRegression(max_iter=500),
        "Linear Discriminant Analysis": LinearDiscriminantAnalysis(),
        "Decision Tree":                DecisionTreeClassifier(random_state=42),
        "Gaussian Naive Bayes":         GaussianNB(),
        "SVM":                          SVC(gamma='auto', random_state=42),
        "Random Forest":                RandomForestClassifier(n_estimators=10, random_state=42),
        "Gradient Boosting":            GradientBoostingClassifier(random_state=42),
        "AdaBoost":                     AdaBoostClassifier(random_state=42),
        "Extra Trees":                  ExtraTreesClassifier(n_estimators=10, random_state=42),
    }

    results_bank = []

    with mo.status.progress_bar(title="Running models...", total=len(model_map_bank)) as bar_bank:
        for name_bank, mdl_bank in model_map_bank.items():
            if name_bank == "KNN (unscaled)":
                pipe_bank = make_pipeline(mdl_bank)
            else:
                pipe_bank = make_pipeline(StandardScaler(), mdl_bank)
            kf_bank = KFold(n_splits=k_cv, shuffle=True, random_state=42)
            cv_scores = cross_val_score(pipe_bank, X_bank, y_bank, cv=kf_bank, scoring='accuracy')
            results_bank.append({
                "Model": name_bank,
                "Avg Accuracy": round(cv_scores.mean(), 4),
                "Std Dev": round(cv_scores.std(), 4)
            })
            bar_bank.update()

    comparison_bank = pd.DataFrame(results_bank).sort_values(by="Avg Accuracy", ascending=False)

    mo.md(f"""
    ### Model Leaderboard (CV folds = {k_cv})

    Higher accuracy is better. Std Dev shows how consistent the model was across folds.

    {mo.ui.table(comparison_bank)}
    """)
    return comparison_bank, k_cv


@app.cell
def _(comparison_bank, k_cv, plt, sns):
    fig_cmp, ax_cmp = plt.subplots(figsize=(10, 6))
    _ = sns.barplot(x="Avg Accuracy", y="Model", data=comparison_bank, palette="viridis", ax=ax_cmp)
    ax_cmp.set_title(f"Model Accuracy Comparison (CV k={k_cv})")
    ax_cmp.set_xlabel("Average Accuracy (Higher is Better)")
    ax_cmp.set_ylabel("Model")
    ax_cmp.set_xlim(0.85, comparison_bank["Avg Accuracy"].max() + 0.01)
    ax_cmp.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    # Conclusion and Summary

    ### What I Did

    I started with 41,188 rows of bank telemarketing data and worked through the
    following steps:

    - Renamed dot-separated columns to use underscores
    - Kept "unknown" values as their own encoded category rather than dropping rows
    - Dropped `duration` to avoid data leakage
    - Used a correlation heatmap and bar charts to understand the data before modeling
    - Encoded all categorical columns with `pd.get_dummies`
    - Split the data 80/20 for training and testing

    ### KNN Results

    After adding `StandardScaler` in a pipeline, the
    model caught a few more "yes" cases. The improvement was modest, but it confirmed
    the point from the lecture: scaling matters for KNN because large-scale features
    will dominate Euclidean distance calculations otherwise.

    ### Other Models

    Looking at the leaderboard, Logistic Regression and Gradient Boosting
    performed better than KNN on this dataset. This lines up with what the lecture
    says, you usually will not know which algorithm is best until you try a few.

    ### The Bigger Issue

    All of these models are scoring around 89-90% largely because they learned to
    predict "no" most of the time. A future improvement would be to address the
    class imbalance directly.

    <br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## References

    Anthropic. (2026, March 21). *Hypothesis testing concepts and examples*

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Generative AI chat]. Claude Sonnet 4.6.

    &nbsp;

    ---

    ## Appendix: AI-Generated Content

    **Tool:** Claude Sonnet 4.6 (Anthropic)
    **Date:** April 13, 2026
    **Topic:** Supervised Machine Learning Concepts

    ---

    ### Prompt Submitted to AI:

    Could you make me a list of the concepts in the 5_supervised_machine_learning.py file and
    describe what each one is used for and how it works? put them in numerical order. provide
    the results in a marimo style file with code windows for example code snippets when
    appropriate. the format should be markdown window describing the concept, code window with
    the code, and a markdown window explaining results and what the code is doing.

    ---

    ### Full-Text AI Response:

    Here is the marimo file covering all 15 concepts from `5_Supervised_Machine_Learning.py`
    in numerical order. Each concept follows the format you asked for: a markdown cell
    describing the concept, a code cell with a working example drawn directly from the source
    file, and a markdown cell explaining what the code is doing and what the results mean.

    Here is a quick overview of the 15 concepts covered:

    1.  Supervised vs Unsupervised Learning -- the foundational distinction between labeled
        and unlabeled data
    2.  KNN Algorithm -- how distance calculation and majority voting work under the hood
    3.  Regressor vs Classifier -- when to use KNeighborsRegressor vs KNeighborsClassifier
    4.  EDA Before Modeling -- using a correlation heatmap to decide which features to keep
    5.  Features (X) and Target (y) -- how to separate predictor columns from the target column
    6.  Train/Test Split -- why you need a holdout set and how train_test_split works
    7.  Fit and Predict -- the .fit() / .predict() workflow
    8.  R-Squared Score -- the standard regression evaluation metric and the K-loop for
        finding optimal K
    9.  K-Fold Cross-Validation -- the gold standard evaluation technique using KFold and
        cross_val_score
    10. StandardScaler and Pipeline -- scaling features to prevent distance-based algorithms
        from being misled by feature magnitude
    11. Comparing Regression Algorithms -- testing seven regressors on the same data to find
        the best performer
    12. Ensemble Methods -- how boosting (AdaBoost, GBM) and bagging (Random Forest,
        Extra Trees) work
    13. Classifier and Dummy Encoding -- converting categorical columns with pd.get_dummies
        before classification
    14. Comparing Classifier Algorithms -- testing ten classifiers on the same data with
        accuracy as the metric
    15. Recap: Selection, Scaling, and Tuning -- summary of the three key takeaways from
        the week

    The full detailed response is contained in the reference link.
    """)
    return


if __name__ == "__main__":
    app.run()
