# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "altair>=6.0.0",
#     "marimo>=0.22.0",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.3",
#     "pandas>=3.0.1",
#     "plotly>=6.6.0",
#     "pyarrow>=23.0.1",
#     "pyzmq>=27.1.0",
#     "scikit-learn>=1.8.0",
#     "seaborn>=0.13.2",
# ]
# ///

import marimo

__generated_with = "0.22.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Supervised Machine Learning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img style="padding-right:10px;" src="figures_wk5/supervised_unsupervised.png"><br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Supervised and  Unsupervised Machine Learning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:10px;" src="figures_wk5/type_of_learning.png" width=450><br>
    Within the field of machine learning, there are two main types of tasks: **supervised** and **unsupervised**.

    The main difference between the two types is that supervised learning is done using a ground truth, or in other words, we have prior knowledge of what the output values for our samples should be. Therefore, the goal of supervised learning is to learn a function that, given a sample of data and desired outputs, best approximates the relationship between input and output observable in the data. Unsupervised learning, on the other hand, does not have labeled outputs, so its goal is to infer the natural structure present within a set of data points.

    We also have to take into consideration how our data is represented within our datset in determining where to perform supervised or unsupervised learning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Supervised Machine Learning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Supervised learning is typically done in the context of a classification or a regression.<br>
    * **Classification:** when we want to map input to output labels
    * **Regression:** when we want to map input to a continuous output.

    In both regression and classification, the goal is to find specific relationships or structure in the input data that allow us to effectively produce correct output data. That “correct” output is determined entirely from the training data, so while we do have a ground truth that our model will assume is true, it is not to say that data labels are always correct in real-world situations. Noisy, or incorrect, data labels will clearly reduce the effectiveness of your model.

    Common algorithms in supervised learning include logistic regression, naive bayes, support vector machines, artificial neural networks, and random forests.

    <img align="center" style="padding-right:10px;" src="figures_wk5/supervised.png" width=500> <br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Supervised ML: K-nearest Neighbors (KNN)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The K-nearest neighbors (KNN) algorithm is a type of supervised machine learning algorithms. KNN is extremely easy to implement in its most basic form, and yet performs quite complex classification tasks.

    KNN is a lazy learning algorithm since it doesn't have a specialized training phase. Rather, it uses all of the data for training while classifying a new data point or instance.

    KNN is a non-parametric learning algorithm, which means that it doesn't assume anything about the underlying data. This is an extremely useful feature since most of the real world data doesn't really follow any theoretical assumption e.g. linear-separability, uniform distribution, etc.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### A Bit of Theory
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The theory behind the KNN algorithm is one of the simplest  supervised machine learning algorithms.

    KNN simply calculates the distance of a new data point to all other training data points. This distance can be calculated by a variety of methods. The most common are Euclidean, Manhattan, and Minowski.

    KNN then selects the K-nearest data points, where K can be any integer. Finally it assigns the data point to the class to which the majority of the K data points belong.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see this algorithm in action with the help of a simple example. This example was created with the assistance of Gemini AI. Suppose you have a dataset with two variables, which when plotted, looks like the one in the following figure.
    """)
    return


@app.cell
def _(sns):
    import marimo as mo
    import matplotlib.pyplot as plt
    # '%matplotlib inline' command supported automatically in marimo
    sns.set_theme()
    import numpy as np

    # 1. Setup the training data from Source 13
    # Labels: 0 for Purple, 1 for Red
    data = np.array([
        (5, 3, 0), (10, 15, 0), (15, 12, 0), (24, 10, 0), (30, 45, 0), # Purple
        (55, 52, 1), (60, 78, 1), (71, 80, 1), (80, 91, 1), (85, 70, 1) # Red
    ])
    return data, mo, np, plt


@app.cell
def _(data, plt):
    #show the data
    plt.scatter(data[:, 0], data[:, 1], c=data[:, 2], cmap='coolwarm')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Training Data')
    #change the color of the points at the bottom left to purple and the points at the top right to red
    plt.scatter(data[:5, 0], data[:5, 1], c='blueviolet', s=100, edgecolors='white')
    plt.scatter(data[5:, 0], data[5:, 1], c='red', s=100, edgecolors='white')
    plt.show()
    return


@app.cell
def _(data, k_slider, np, plt, x_coord, y_coord):
    # KNN Logic Implementation
    def run_knn(k, test_point):
        # Calculate Euclidean distance 
        # Formula: sqrt(sum((x_i - y_i)^2))
        distances = np.sqrt(np.sum((data[:, :2] - test_point)**2, axis=1))
    
        # Get indices of K nearest neighbors 
        nearest_indices = np.argsort(distances)[:k]
    
        # Majority vote 
        classes = data[nearest_indices, 2].astype(int)
        prediction = np.bincount(classes).argmax()
    
        return prediction, nearest_indices, distances[nearest_indices].max()

    test_p = np.array([x_coord.value, y_coord.value])
    pred, indices, radius = run_knn(k_slider.value, test_p)
    pred_label = "Red" if pred == 1 else "Purple"

    # Visualization
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot training points [cite: 13]
    colors = ['blueviolet' if c == 0 else 'red' for c in data[:, 2]]
    ax.scatter(data[:, 0], data[:, 1], color=colors, s=100, edgecolors='white', label="Training Data")

    # Plot test point X [cite: 14]
    ax.scatter(test_p[0], test_p[1], color='black', marker='x', s=150, label="Point 'X'")

    # Draw the neighborhood circle [cite: 18]
    circle = plt.Circle((test_p[0], test_p[1]), radius, color='gray', fill=True, alpha=0.1, linestyle='--')
    ax.add_patch(circle)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_title(f"KNN Classification (K={k_slider.value})")
    ax.legend()
    plt.grid(alpha=0.3)

    return fig, pred_label


@app.cell
def _(mo):
    mo.md("# KNN Interactive Classifier")
    # 2. Interactive UI Elements
    k_slider = mo.ui.slider(start=1, stop=9, step=2, value=3, label="Set K (Number of Neighbors)")
    x_coord = mo.ui.number(start=0, stop=100, value=45, label="X Coordinate")
    y_coord = mo.ui.number(start=0, stop=100, value=50, label="Y Coordinate")

    mo.hstack([k_slider, x_coord, y_coord], justify="start")
    return k_slider, x_coord, y_coord


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your task is to classify a new data point with 'X' into "Blue" class or "Red" class. The coordinate values of the data point are x=45 and y=50.

    Suppose the value of K is 3, but you can change to a different value with a slider. The KNN algorithm starts by calculating the distance of point X from all the points. It then finds the 3 nearest points with least distance to point X. This is shown in the figure below. The three nearest points have been encircled
    """)
    return


@app.cell
def _(fig, mo, pred_label):
    # 5. Display Results
    mo.vstack([
        mo.as_html(fig),
        mo.md(f"### Result: Point X is classified as **{pred_label}** ")
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The final step of the KNN algorithm is to assign new point to the class to which majority of the three nearest points belong.

    From the figure above we can see that the two of the three nearest points belong to the class "Red" while one belongs to the class "Blue". Therefore the new data point will be classified as "Red".
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### KNN: Regressor vs Classifier
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What's the difference between a KNN Regressor and KNN Classifier?
    * **KNN regression** tries to predict the value of the output variable by using a local average. The regressor model works best when the codomain is continuous.
    * **KNN classification** attempts to predict the class to which the output variable belong by computing the local probability. The classifier model works best when the codomain is discrete.

    As an example, if you were trying to predict the time it took for a pizza delivery company to delivery a pizza, you would be working with a codomain (your target value) that is continuous.

    <div class="alert alert-block alert-warning">
    <b>Important Note::</b> Like many other machine learning algorithms, KNN only works with all numerical data. If your dataset has categorical values, you will need to convert them into numeric representations.<br>

    Here are some resources on how to do this:<br>
    https://www.geeksforgeeks.org/replacing-strings-with-numbers-in-python-for-data-analysis/ <br>
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html  <br>
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # KNN Regression Demo - Auto dataset
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For this demonstration, we will be using a data set that I have already cleaned up (replaced all the NaN). Normally that would be your first step in building a machine learning algorithm.
    """)
    return


@app.cell
def _():
    # pandas
    import pandas as pd

    # sklearn
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.decomposition import PCA

    # plotting
    import seaborn as sns
    import warnings
    warnings.filterwarnings("ignore")
    return KNeighborsRegressor, pd, sns, train_test_split


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Loading our data set
    """)
    return


@app.cell
def _(pd):
    # loading our data set
    auto = pd.read_csv('data_wk5/auto.dt.nona.csv')
    return (auto,)


@app.cell
def _(auto):
    auto.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## EDA - just a little bit
    """)
    return


@app.cell
def _(auto, mo):
    # Display data info
    mo.md(
        f"**Shape:** {auto.shape[0]} rows × {auto.shape[1]} columns"
    )
    return


@app.cell
def _(auto, mo):
    mo.ui.tabs(
        {
            "auto": mo.lazy(mo.ui.table(auto.describe()))
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What are you trying to investigate?
    At this point we need to define a question that we wish to investigate. I'm going to use a correlation matrix to look for possible realtionships within our data set.
    """)
    return


@app.cell
def _(auto, plt, sns):
    _ = sns.heatmap(auto.corr())
    #display the heatmap
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-info">
    <b>Pop Quiz::</b> What does the '_' mean in the cell above? <br>

    Answer: Signifies a temporary variable that we don't intend to use going forward.
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Looking at the correlation matrix, we can see a strong inverse correlation between mpg and cylinders, displacement, horsepower, and weight. We can also see that acceleration has a strong relationship and model.year and origin appear to have less significance to mpg.

    Given this information, I'm going to set mpg as my target variable and remove acceleration,model.year and origin from the dataset.
    """)
    return


@app.cell
def _(auto):
    # trimming our data set
    auto.drop(['acceleration','model.year', 'origin'],axis=1, inplace=True)
    return


@app.cell
def _(auto):
    auto.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Defining our features and targets
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * Target(s) are the values that we are trying to predict. <br>
    * Features are the columns we are using to predict our target.
    """)
    return


@app.cell
def _(auto):
    auto.shape
    return


@app.cell
def _(auto):
    cols = auto.columns
    target_col = 'mpg'
    feat_cols = [c for c in cols if c != target_col]

    # there is nothing magical about the X and y notation here. 
    # however, it seems to be a fairly standard notation, so we will use is here
    array = auto.values

    X = array[:, 1:5]
    y = array[:, 0]
    return X, feat_cols, target_col, y


@app.cell
def _(y):
    y
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Splitting your data set into training and test sets
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we are going to create two new dataframes:

    * One to train the machine learning model.<br>
    * One to test the accuracy of that model. <br>
    * **This can be an iterative process.**

    We make a training set so we can train all of our models on the same data. We can then compare how the models perform by evaluating accuracy on the test set. Train and tests sets should never contain any of the same data. The idea is the model has never seen the test set before, so we can check if our model is overfitting (high variance) and which model works best on unseen data. Sometimes the test data is called the ‘holdout set’.
    """)
    return


@app.cell
def _(X, train_test_split, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_test, X_train, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-info">
    <b>Pop Quiz::</b> What does the 'random_state' mean in the cell above do? <br>

    Answer: random_state sets a seed to the random generator, so that your train-test splits are always deterministic. Meaning your results will be reproducible if you were to re-run this notebook.
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Setting up the KNN Regressor
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since our target value (mpg) is continuous, we will use sklearn.KNeighborsRegressor.

    For right now, we are simply going to use k=3 for our number of clusters. We will look at a way to evaluate different k values a little further down.
    """)
    return


@app.cell
def _(KNeighborsRegressor, X_train, y_train):
    # define and fit our model
    model = KNeighborsRegressor(n_neighbors=3, n_jobs=-1)
    model.fit(X_train, y_train)
    return (model,)


@app.cell
def _(X_test, mo, model, y_test):
    # gather the predictations that our model made for our test set
    preds = model.predict(X_test)

    #printing the actuals for the test data set
    with mo.redirect_stdout():
        print('Actuals for test data set')
    #printthe actuals for the test data set using marimo's markdown
        print(y_test)

    #printing the predictions for the test data set
    with mo.redirect_stdout():
        print('Predictions for test data set')
        print(preds)
    return (preds,)


@app.cell
def _(mo, preds, y_test):
    #compare the two sets for mpg'
    _differs = y_test - preds
    with mo.redirect_stdout():
        print('Differences between the two sets')
        print(_differs)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Just printing out the predictions and differences doesn't really work for a larger data set. [skleam.metric](https://scikit-learn.org/stable/modules/classes.html#sklearn-metrics-metrics) is a great package to look at the accuracy of your model. Just make sure you are matching your evaluation metric with the type of algorithm you used.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-success">
    <b>R^2 (coefficient of determination) regression score function</b> Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of y, disregarding the input features, would get a R^2 score of 0.0.
    </div>
    """)
    return


@app.cell
def _(mo, preds, y_test):
    from sklearn.metrics import r2_score

    with mo.redirect_stdout():
        print('R-squared for the test data set')
        print(r2_score(y_test,preds))
    return (r2_score,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-success">
    <b>Explained variance regression score function</b> Best possible score is 1.0, lower values are worse.
    </div>
    """)
    return


@app.cell
def _(mo, preds, y_test):
    from sklearn.metrics import explained_variance_score

    with mo.redirect_stdout():
        print('Explained variance score for the test data set')
        print(explained_variance_score(y_test,preds))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hmmm... A r2_score of .75 isn't all that bad.  Especially since we just guessed on the number of clusters.  Perhaps there is away to be "smarter" about selecting the number of clusters.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Determining the optimal number of clusters
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's loop through a range of k values and store the accuracy of the various models.   then we can graphically display the accuracy scores to determine the optimal number of clusters.

    Note: For KNeighborsRegressor, score returns the r2_score from sklearn.metrics.<br>
    (https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html)
    """)
    return


@app.cell
def _(
    KNeighborsRegressor,
    X_test,
    X_train,
    feat_cols,
    target_col,
    y_test,
    y_train,
):
    scores = []
    print(f'Features: {feat_cols} \nTarget: {target_col}')
    for _k in range(2, 20):
        print(f'Evaluating {_k} clusters')
        model_1 = KNeighborsRegressor(n_neighbors=_k, n_jobs=-1)
        model_1.fit(X_train, y_train)
        scores.append(model_1.score(X_test, y_test))
    return (scores,)


@app.cell
def _(plt, scores):
    # display the resutls
    plt.plot(range(2, 20), scores)
    plt.scatter(range(2, 20), scores)
    plt.grid()
    _ =plt.xticks(range(2, 20))
    #show the plot
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So what is this plot trying to tell us? <br>

    We loaded accuracy scores into the array that this plot is based off of. We can validate this by comparing the r2_score from our work above with the plot itself.  So, we would expect k=3 to be around .75. (red circle)

    <img align="center" style="padding-right:10px;" src="figures_wk5/plot1.png" width=400><br>

    Yup! we have a match.

    The green arrow is showing that at k=13, we have the highest r2_score value.  That would lead us to believe that 13 is the optimal number of clusters for our data set and this algorithm.

    Let's re-run the model for k=13 and verify our assumptions.
    """)
    return


@app.cell
def _(KNeighborsRegressor, X_test, X_train, mo, y_test, y_train):
    # define and fit our model
    model_2 = KNeighborsRegressor(n_neighbors=13, n_jobs=-1)
    model_2.fit(X_train, y_train)
    preds_1 = model_2.predict(X_test)
    # gather the predictations that our model made for our test set
    with mo.redirect_stdout():
        print('Actuals for test data set')
        print(y_test)
    # display the actuals and predictions for the test set
    with mo.redirect_stdout():
        print('Predictions for test data set')
        print(preds_1)
    return (preds_1,)


@app.cell
def _(preds_1, r2_score, y_test):
    _differs = y_test - preds_1
    print(f'Differences between the two sets:\n{_differs}\n')
    print(f'r2_score: {r2_score(y_test, preds_1)}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hooray! That all turned out as expected. The r2_score for our KNNRegresor with k=13 is approximately .79. Which is a fairly decent score overall.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Other Regression Algorithms
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    K Nearest Neighbor isn't the only regression algorithm out there -- not by a long shot!

    Let's use our **auto** data set to compare some of the others. "Simple" algorithms we'll test are:

    * **Linear**<br>
        * Linear Regression<br>
        * Lasso<br>
        * Elastic Net<br>
    * **Non-Linear**<br>
        * KNN (with default k)<br>
        * Decision Tree<br>
        * SVR<br>

    Then, we'll try using the `StandardScaler` in a `Pipeline` to see if scaling the data makes a difference.

    Finally, we'll look at some "ensemble" algorithms:

    * Ada Boost
    * Gradient Boost
    * Random Forest
    * Extra Trees
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## K-Fold Cross-Validation
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    K-fold cross-validation is a testing technique used to reduce variance. It splits the data set into _k_ parts or _folds_. The algorithm is trained on all but one of the folds, with one being used for testing. After training and testing, you end up with _k_ performance scores that can be summarized with mean and standard deviation.

    K-fold cross-validation gives a more accurate estimate of algorithm performance because each algorithm is trained multiple times with different data each time.

    Care must be used in choosing _k_ so that each chunk of training data is large enough to be representative of the problem. In our case, the **autos** data set is small with 398 rows. If we choose `k = 5` then our data sets will only have about 80 rows in each one.

    **Other variations exist,** including <br>
    * Setting `k =  1` for "Leave one out" testing<br>
    * Manually using `train_test_split` multiple times<br>

    K-fold cross-validation is the **_gold standard_** with _k_ usually being set to 3, 5 or 10.
    """)
    return


@app.cell
def _():
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import KFold
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import LinearRegression
    from sklearn.linear_model import Lasso
    from sklearn.linear_model import ElasticNet
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.svm import SVR
    from sklearn.pipeline import Pipeline
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.ensemble import ExtraTreesRegressor
    from sklearn.ensemble import AdaBoostRegressor
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
    from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
    from matplotlib import pyplot
    from sklearn.pipeline import Pipeline

    return (
        AdaBoostRegressor,
        DecisionTreeRegressor,
        ElasticNet,
        ExtraTreesRegressor,
        GradientBoostingRegressor,
        KFold,
        Lasso,
        LinearRegression,
        Pipeline,
        RandomForestRegressor,
        SVR,
        StandardScaler,
        cross_val_score,
        pyplot,
    )


@app.cell
def _(auto_1):
    auto_1
    return


@app.cell
def _(
    DecisionTreeRegressor,
    ElasticNet,
    KNeighborsRegressor,
    Lasso,
    LinearRegression,
    RandomForestRegressor,
    SVR,
    auto_1,
    mo,
):
    # Model selection mapping
    model_map = {
        "Linear Regression": LinearRegression(),
        "Lasso Regression": Lasso(),
        "Elastic Net": ElasticNet(),
        "K-Nearest Neighbors": KNeighborsRegressor(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        "SVR": SVR()
    }
    # UI Elements
    k_slider_1 = mo.ui.slider(start=2, stop=20, step=1, value=5, label="Number of Folds (k)")
    model_dropdown = mo.ui.dropdown(
        options=list(model_map.keys()), 
        value="Random Forest", 
        label="Select Model"
    )

    mo.md(
        f"""
        # Auto MPG Multi-Model Comparison
    
        Test how different algorithms handle the **{len(auto_1)}** rows of the autos dataset using $k$-fold cross-validation.
    
        {mo.hstack([k_slider_1, model_dropdown], justify="start")}
        """
    )
    return k_slider_1, model_dropdown, model_map


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Scaling the data

    It is possible that the different data scales (tens, hundreds, thousands) are affecting the algorithms' ability to accurately train.

    We will use the `StandardScaler` function to scale the data. `StandardScaler` re-sets the data so each attribute has a mean of 0 and standard deviation of 1.

    We will also use a `pipeline` to insure all of the data is treated the same way for each algorithm.

    <div class="alert alert-block alert-warning">
        <b>Important Note::</b> Here we are showing you how to scale a dataset <i>within</i> a pipeline. You can achieve the same results without using a pipeline. <br>

    Here are some resources on how to do this:<br>
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html <br>
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
    </div>
    """)
    return


@app.cell
def _(
    KFold,
    StandardScaler,
    auto_1,
    cross_val_score,
    k_slider_1,
    mo,
    model_dropdown,
    model_map,
    np,
):
    from sklearn.pipeline import make_pipeline
    # Execution Logic
    k = k_slider_1.value
    selected_model_name = model_dropdown.value

    # Prepare Data
    X_1 = auto_1.drop('mpg', axis=1)
    y_1 = auto_1['mpg']

    # Create a pipeline: Scale data then apply the selected model
    # Note: Scaling is vital for KNN and SVR!
    pipeline = make_pipeline(StandardScaler(), model_map[selected_model_name])

    # Perform K-Fold
    kf = KFold(n_splits=k, shuffle=True, random_state=42)
    scores_1 = cross_val_score(pipeline, X_1, y_1, cv=kf, scoring='neg_mean_squared_error')
    rmse_scores = np.sqrt(-scores_1)

    # Results Summary
    mo.md(
        f"""
        ### {selected_model_name} Performance
        - **Average RMSE:** `{rmse_scores.mean():.3f}`
        - **Standard Deviation (Variance):** `{rmse_scores.std():.3f}`
        - **Fold Size:** ~{len(auto_1)//k} samples
        """
    )
    return X_1, k, make_pipeline, y_1


@app.cell
def _(
    KFold,
    StandardScaler,
    X_1,
    cross_val_score,
    k,
    make_pipeline,
    mo,
    model_map,
    np,
    pd,
    y_1,
):
    # New logic cell to compare all models
    all_results = []

    # Use a progress bar if k or the number of models is high
    with mo.status.progress_bar(title="Calculating all models...", total=len(model_map)) as bar:
        for name, model_a in model_map.items():
            # Build pipeline for each
            pipeline_a = make_pipeline(StandardScaler(), model_a)
        
            # Calculate CV scores
            kf_a = KFold(n_splits=k, shuffle=True, random_state=42)
            scores_a = cross_val_score(pipeline_a, X_1, y_1, cv=kf_a, scoring='neg_mean_squared_error')
            rmse_scores_a = np.sqrt(-scores_a)
        
            all_results.append({
                "Model": name,
                "Avg RMSE": rmse_scores_a.mean(),
                "Std Dev": rmse_scores_a.std()
            })
            bar.update()

    # Convert to DataFrame and sort by performance
    comparison_df = pd.DataFrame(all_results).sort_values(by="Avg RMSE")

    mo.md(
        f"""
        ## Model Leaderboard (k={k})
    
        This table compares all 7 algorithms. The **lower** the Average RMSE, the better the model performed.
    
        {mo.ui.table(comparison_df)}
        """
    )
    return (comparison_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We take the square root of the mean squared error to get to the original units of measustement, i.e. mpg in this case.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Looks like un-tuned Random Forest model actually scored best, one of the **non-linear** algorithms.

    Let's visualize those results:
    """)
    return


@app.cell
def _(comparison_df, k, plt, sns):
    # Compare Algorithms
    _ = sns.barplot(x="Avg RMSE", y="Model", data=comparison_df, palette="viridis")
    plt.title(f"Model Comparison (k={k})")
    plt.xlabel("Average RMSE (Lower is Better)")
    plt.ylabel("Model")
    plt.grid(axis='x', alpha=0.3)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ensemble Methods
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Another way to increase performance is to use **Ensemble** algorithms.

    The Ensemble methods use a variety of sampling methods during the learning process so that they look at the data multiple times and in multiple ways.

    ### Boosting
    Boosting takes a weak decision model (like regression or shallow decision trees) and trains a sequence of many of those models, each one compensating for the weakness of the previous model.
        * **AdaBoost** identifies mis-classified data points and adjusting their weight in subsequent model calculations so they are paid more attention.<br>
        * **Gradient Boosting** focuses on the loss function (error), attempting to minimize it on each subsequent model -- that is the "gradient" part.

    ### Bagging
    "Bagging" is a shortening of **bootstrap aggragating**. This is based off the bootstrap statistical method discussed in Week 2, where many smaller sub-samples of the data are used in calculations and then averaged together.

    **Random Forests** are a group of decision trees, trained on sub-samples of the data. Decision trees are very sensitive to differences in data -- even the same data in a different order can produce a very different decision tree. After training all the smaller decision trees, the results are aggragated into a singular decision model.

    Random forests were the king of machine learning competitions (like Kaggle) until deep learning came along and became feasible for use by the general populace.
    """)
    return


@app.cell
def _(
    AdaBoostRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
    Pipeline,
    RandomForestRegressor,
    StandardScaler,
):
    # ensembles
    ensembles = []
    ensembles.append(('ScaledAB', Pipeline([('Scaler', StandardScaler()),('AB', AdaBoostRegressor())])))
    ensembles.append(('ScaledGBM', Pipeline([('Scaler', StandardScaler()),('GBM', GradientBoostingRegressor())])))
    ensembles.append(('ScaledRF', Pipeline([('Scaler', StandardScaler()),('RF', RandomForestRegressor(n_estimators=10))])))
    ensembles.append(('ScaledET', Pipeline([('Scaler', StandardScaler()),('ET', ExtraTreesRegressor(n_estimators=10))])))
    return (ensembles,)


@app.cell
def _(KFold, X_train, cross_val_score, ensembles, np, y_train):
    #compare the performance of the ensemble models
    results_2 = []
    names_2 = []

    # fallbacks to avoid NameError in this cell
    num_folds = globals().get("num_folds", globals().get("k", 4))
    seed = globals().get("seed", 42)
    scoring = globals().get("scoring", "neg_mean_squared_error")

    for _name, model_5 in ensembles:
        _kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
        _cv_results = cross_val_score(model_5, X_train, y_train, cv=_kfold, scoring=scoring)
        rmse_scores_5 = np.sqrt(-_cv_results)
        results_2.append(rmse_scores_5)
        names_2.append(_name)
        _msg = '%s: %f (%f)' % (_name, rmse_scores_5.mean(), rmse_scores_5.std())
        print(_msg) 
    return names_2, num_folds, results_2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Even un-tuned, some of the ensemble methods scored better than the algorithms above.
    """)
    return


@app.cell
def _(names_2, pyplot, results_2):
    #plot the results for the ensemble models
    _fig = pyplot.figure()
    _fig.suptitle('Scaled Ensemble Algorithm Comparison')
    _ax = _fig.add_subplot(111)
    pyplot.boxplot(results_2)
    _ax.set_xticklabels(names_2)
    pyplot.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # KNN Classifier Demo - Penguins!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Classification** is the type of Machine Learning we do on categorical targets.

    I like penguins, so we are going to use Week 4's Palmer Penguins dataset to look at classification, with **species** as the target.
    """)
    return


@app.cell
def _():
    from sklearn.neighbors import KNeighborsClassifier

    return (KNeighborsClassifier,)


@app.cell
def _(sns):
    penguins = sns.load_dataset('penguins')
    return (penguins,)


@app.cell
def _(penguins):
    penguins.head()
    return


@app.cell
def _(penguins):
    penguins
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In Week 3, we found that there are 2 rows that have essentially no data and 9 rows missing sex entries. At that time, we used a RandomForestClassifier algorithm to guess the missing sex entries.

    For expediency's sake, we will simply drop those 9 rows.
    """)
    return


@app.cell
def _(penguins):
    penguins_1 = penguins[penguins.body_mass_g.notna()]
    penguins_1 = penguins_1[penguins_1.sex.notna()]
    penguins_1
    return (penguins_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Classifier Demo -- Guessing Species
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    3 of the dataset's fields are categories that could be used for classification: **Species**, **Island**, and **Sex**. You've already seen a demo of sex classification, so let's focus on species this time.

    It is tempting to say that since there are 3 species, K should be 3 **BUT** remember, the K-nearest neighbor algorithm works by comparing a point to its' neighbors, and K is the number of neighbors to use in the comparison. We will still need to discover the best K.

    But first, we need to dummy encode our categories. Remember, since **species** is our target, we do not encode it.
    """)
    return


@app.cell
def _(pd, penguins_1):
    peng_encoded = pd.get_dummies(penguins_1, columns=['island', 'sex'], prefix=['island', 'sex'])
    peng_encoded
    return (peng_encoded,)


@app.cell
def _(peng_encoded):
    peng_encoded.shape
    return


@app.cell
def _(peng_encoded):
    array_1 = peng_encoded.values
    return (array_1,)


@app.cell
def _(array_1):
    X_2 = array_1[:, 1:]
    y_2 = array_1[:, 0]
    return X_2, y_2


@app.cell
def _(X_2, train_test_split, y_2):
    X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_2, y_2, test_size=0.2, random_state=42)
    return X_test_2, X_train_2, y_test_2, y_train_2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's jump right in to finding the K value:
    """)
    return


@app.cell
def _(KNeighborsClassifier, X_test_2, X_train_2, y_test_2, y_train_2):
    scores_2 = []
    for _k in range(2, 20):
        print(f'Evaluating {_k} clusters')
        model_6 = KNeighborsClassifier(n_neighbors=_k, n_jobs=-1)
        model_6.fit(X_train_2, y_train_2)
        scores_2.append(model_6.score(X_test_2, y_test_2))
    return (scores_2,)


@app.cell
def _(plt, scores_2):
    # display the resutls
    plt.plot(range(2, 20), scores_2)
    plt.scatter(range(2, 20), scores_2)
    # plt.grid()
    plt.xticks(range(2, 20))
    plt.show()
    print(f'\nMax accuracy = {max(scores_2) * 100}%')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Seems our highest accuracy was actually k = 8.
    """)
    return


@app.cell
def _(scores_2):
    max(scores_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Demo - Comparing Classifiers on the Auto data set
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's compare classification algorithms, for this exercise we will be using the **cylinders** column of the auto dataset as our target variable.
    I'm not going to go into a lot of details here, just showing you the different algorithms. In general, everything runs that same as it did with the regression demo above.

    * **Linear algorithms**:
        * Logistic regression
        * Linear discriminant analysis
    * **Non-linear algorithms**:
        * Classification and regression trees
        * Support vector machines
        * Gaussian naive Bayes
        * KNN
    * **Boosting algorithms**:
        * AdaBoost
        * Gradient Boosting
    * **Bagging algorithms**:
        * RandomForests
        * Extra Trees
    """)
    return


@app.cell
def _():
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import ExtraTreesClassifier

    return (
        AdaBoostClassifier,
        DecisionTreeClassifier,
        ExtraTreesClassifier,
        GaussianNB,
        GradientBoostingClassifier,
        LinearDiscriminantAnalysis,
        LogisticRegression,
        RandomForestClassifier,
        SVC,
    )


@app.cell
def _(auto):
    auto
    return


@app.cell
def _(auto):
    auto.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Re-order the columns to make it easier to designate the target.
    """)
    return


@app.cell
def _(auto):
    auto_1 = auto[['mpg', 'displacement', 'horsepower', 'weight', 'cylinders']]
    return (auto_1,)


@app.cell
def _(auto_1):
    auto_1.head()
    return


@app.cell
def _(auto_1):
    array_2 = auto_1.values
    return (array_2,)


@app.cell
def _(array_2):
    X_3 = array_2[:, 0:4]
    y_3 = array_2[:, 4]
    return X_3, y_3


@app.cell
def _(y_3):
    y_3
    return


@app.cell
def _(X_3, train_test_split, y_3):
    X_train_3, X_test_3, y_train_3, y_test_3 = train_test_split(X_3, y_3, test_size=0.2, random_state=42)
    return


@app.cell
def _(
    DecisionTreeClassifier,
    GaussianNB,
    KNeighborsClassifier,
    LinearDiscriminantAnalysis,
    LogisticRegression,
    SVC,
    mo,
):
     #Model selection mapping
    model_map_b = {
        "Logistic Regression": LogisticRegression(),
        "Linear Discriminant Analysis": LinearDiscriminantAnalysis(),
        "KNN": KNeighborsClassifier(),
        "Decision Tree": DecisionTreeClassifier(),
        "Gaussian Naive Bayes Classifier": GaussianNB(),
        "SVM": SVC(gamma='auto'),
        }

    # UI Elements
    k_slider_2 = mo.ui.slider(start=2, stop=20, step=1, value=5, label="Number of Folds (k)")
    model_dropdown_2 = mo.ui.dropdown(
        options=list(model_map_b.keys()), 
        value="SVM", 
        label="Select Model"
    )


    return k_slider_2, model_dropdown_2, model_map_b


@app.cell
def _(auto_1, k_slider_2, mo, model_dropdown_2):
    k_2=k_slider_2.value
    selected_model_name_b = model_dropdown_2.value

    mo.md(
        f"""
        # Auto Classifier Model Comparison
    
        Test how different algorithms handle the **{len(auto_1)}** rows of the autos dataset using $k$-fold cross-validation.
    
        {mo.hstack([k_slider_2, model_dropdown_2], justify="start")}
        """
    )
    return (k_2,)


@app.cell
def _(
    KFold,
    X_3,
    cross_val_score,
    k_2,
    make_pipeline,
    mo,
    model_map_b,
    pd,
    y_3,
):
    # predict cylinders using the models provided in model_map_b and compare their performance using k-fold cross-validation
    results_3 = []
    #names_3 = []

    # Use a progress bar if k or the number of models is high
    with mo.status.progress_bar(title="Calculating all models...", total=len(model_map_b)) as bar_b:
        for name_b, model_b in model_map_b.items():
            # Build pipeline for each
            pipeline_b = make_pipeline(model_b)
        
            # Calculate CV scores
            kf_b = KFold(n_splits=k_2, shuffle=True, random_state=42)
            scores_b = cross_val_score(pipeline_b, X_3, y_3, cv=kf_b, scoring='accuracy', error_score='raise')
                
            results_3.append({
                "Model": name_b,
                "Accuracy": scores_b.mean(),
                "Std Dev": scores_b.std()})
            bar_b.update()

    # Convert to DataFrame and sort by performance
    comparison_df_b = pd.DataFrame(results_3).sort_values(by="Accuracy", ascending=False)

    mo.md(
        f"""
        ## Model Leaderboard (k={k_2})
    
        This table compares all 6 algorithms. The **higher** the Accuracy, the better the model performed.
    
        {mo.ui.table(comparison_df_b)}
        """
    )
    return (comparison_df_b,)


@app.cell
def _(comparison_df_b, k, plt, sns):
    #plot the results for the Classifier models
    _ = sns.barplot(x="Accuracy", y="Model", data=comparison_df_b, palette="magma")
    plt.title(f"Model Comparison (k={k})")
    plt.xlabel("Average Accuracy (Higher is Better)")
    plt.ylabel("Model")
    plt.grid(axis='x', alpha=0.3)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ensemble Classification
    """)
    return


@app.cell
def _(
    AdaBoostClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
):
    ensembles_1 = []
    ensembles_1.append(('AB', AdaBoostClassifier()))
    ensembles_1.append(('GBM', GradientBoostingClassifier()))
    ensembles_1.append(('RF', RandomForestClassifier(n_estimators=10)))
    ensembles_1.append(('ET', ExtraTreesClassifier(n_estimators=10)))
    return (ensembles_1,)


@app.cell
def _(KFold, X_3, cross_val_score, ensembles_1, num_folds, y_3):
    results_4 = []
    names_4 = []

    # evaluate the ensemble models using k-fold cross-validation and compare their performance
    num_folds_1 = globals().get("num_folds", globals().get("k", 4))
    seed_1 = globals().get("seed", 42)
    for _name_1, model_7 in ensembles_1:
        _kfold_1 = KFold(n_splits=num_folds, random_state=seed_1, shuffle=True)
        _cv_results_4 = cross_val_score(model_7, X_3, y_3, cv=_kfold_1, scoring='accuracy', error_score='raise')
        results_4.append(_cv_results_4)
        names_4.append(_name_1)
        _msg_4 = '%s: %f (%f)' % (_name_1, _cv_results_4.mean(), _cv_results_4.std())
        print(_msg_4)
    return names_4, results_4


@app.cell
def _(names_4, pyplot, results_4):
    _fig = pyplot.figure()
    _fig.suptitle('Ensemble Algorithm Comparison')
    _ax = _fig.add_subplot(111)
    pyplot.boxplot(results_4)
    _ax.set_xticklabels(names_4)
    pyplot.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Recap
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * **Many algorithms exist for a reason**.
        * Some machine learning algorithms are better than others, depending on the data.
        * You probably won't know which is best until you try it.
    * Data can be *scaled*, and/or *normalized* to "tune" it.
        * It **might** improve accuracy.
    * ML Algorithms can be "tuned", also.
        * Like KNN's k-value, among others.
    """)
    return


if __name__ == "__main__":
    app.run()
