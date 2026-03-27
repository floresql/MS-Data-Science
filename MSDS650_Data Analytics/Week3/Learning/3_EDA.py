# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "altair>=6.0.0",
#     "marimo>=0.20.2",
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

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import subprocess

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exploratory Data Analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:10px;" src="figures_wk3/Data-Preparation-for-Machine-Learning.png" width=200><br>


    Exploratory Data Analysis (EDA) is the process of **getting to know your data**.

    Classical statistics tests hypotheses by fitting models that demonstrate relationships among the data. But what if you don't have a hypothesis?

    **Exploratory Data Analysis** helps uncover those relationships so you can form hypotheses. EDA is the first step in virtually every **machine learning** model you will build.

    **_Data Preparation for Machine Learning_** is a great ebook by "machine learning specialist," Jason Brownlee. Even though the book does not explicitly state that it is teaching EDA, that is absolutely the purpose of the demonstrated techniques.


    We will be using the Palmer Penguins data set to demonstrate these concepts. The **Seaborn** graphing package can download and access the data from a repository on GitHub using its `load_dataset()` function.

    <img align="right" style="padding-right:10px;" src="figures_wk3/logo.png" width=200><br>

    Reference:
    > Data Preparation for Machine Learning<br>
    > Jason Brownlee<br>
    > https://machinelearningmastery.com/data-preparation-for-machine-learning/


    >   Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer<br>
    >   Archipelago (Antarctica) penguin data. R package version 0.1.0.<br>
    >   https://allisonhorst.github.io/palmerpenguins/. doi:<br>
    >   10.5281/zenodo.3960218.<br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Bad News
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    EDA is as much art as it is science. The steps you take will depend as much on the data set and your end goal as any set of predefined recipe-like steps I can give you. All I can do is give you an introduction and encourage you to **continue to study the topic on your own**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Good News
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The good news is that there are several tasks that you will need to do with every data set. Jason Brownlee gives us a basic framework for data preparation or EDA:

    * **Data Cleaning**: Finding and fixing errors and problems in the data (outliers, missing data, etc.)<br>
    * **Feature Selection**: Identifying the relationships between variables and their importance in the task.<br>
    * **Data Transforms**: Change the scale or distribution of the numbers in a variable.<br>
    * **Feature Engineering**: Creating new variables from existing variables.<br>
    * **Dimensionality Reduction**: "Compacting" several variables down into a smaller number of variables (i.e. 10 variables down to 3 for easier graphing).<br>

    Graphically, that looks something like this:<br>

    <table>
        <tr>
            <td><img style="padding-right:10px;" src="figures_wk3/Data_cleaning_overview.png"></td>
            <td><img style="padding-right:10px;" src="figures_wk3/Feature_selection_overview.png"></td>
            <td><img style="padding-right:10px;" src="figures_wk3/Data_variable_overview.png"></td>
        </tr>
    </table>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Data Cleaning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Data cleaning is where you will find and handle missing values, look for outliers, detect duplicate rows, check to make sure columns have enough variance, etc.

    Let's demonstrate these ideas with the data set.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Libraries and Data
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    # '%matplotlib inline' command supported automatically in marimo

    # Makes graphics look better
    sns.set()
    return np, pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Palmer Penguins data set is one of the Seaborn "built-in" data sets. That is, a dataset stored in a special GitHub repository that Seaborn knows how to access.
    """)
    return


@app.cell
def _(sns):
    penguins = sns.load_dataset('penguins')
    return (penguins,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img style="padding-right:10px;" src="figures_wk3/lter_penguins.png" width="600"><br>

    First of all, I don't know exactly what kind of variable the data was loaded into. Let's check.
    """)
    return


@app.cell
def _(penguins):
    type(penguins)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Great! Its a Pandas dataframe.

    Now, let's get an initial read on the data and the size of the dataset.
    """)
    return


@app.cell
def _(mo, penguins):
    mo.accordion(
        {
            "penguins": mo.lazy(penguins.head(5))
        }
    )
    return


@app.cell
def _(penguins):
    penguins.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    344 rows by 7 columns.

    Let's look at the first few rows.
    """)
    return


@app.cell
def _(penguins):
    penguins.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img style="padding-right:10px;" src="figures_wk3/culmen_depth.png" width="600"><br>
    """)
    return


@app.cell
def _(penguins):
    penguins.info()
    return


@app.cell
def _(mo, penguins):
    mo.ui.dataframe(penguins)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, the `info()` function tells us how many rows we have, how many non-null in each row, and data type for each row.

    Let's look at some more summary statistics, then we can sort out the missing categorical data.
    """)
    return


@app.cell
def _(mo, penguins):
    mo.ui.tabs(
        {
            "penguins": mo.lazy(mo.ui.table(penguins.describe()))
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can also rotate that display for easier reading:
    """)
    return


@app.cell
def _(penguins):
    penguins.describe().T
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The "T" means "transform" -- in this case, swap rows and columns.

    We will look at this data graphically in a few minutes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Missing Data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Looking at the first 5 rows above, we see one row where almost all the data is missing. Row 3 simply has the species and island filled out. That row probably won't contribute much to analysis and we could **drop it**. BUT, we need to be careful -- there are many ways to deal with missing data, and dropping rows is the sledgehammer approach. **Dropping rows should probably _NOT_ be the first tool you reach for.**
    """)
    return


@app.cell
def _(penguins):
    penguins[penguins.isnull().values.any(axis=1)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, there are only 2 rows missing all data. The others only have sex data missing, **which can be inferred**.

    Another way to look at NaNs:
    """)
    return


@app.cell
def _(penguins):
    penguins.isnull().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First, let's get rid of the entries that do not have a weight -- we will do this by copying all rows that have a weight into a new dataframe.
    """)
    return


@app.cell
def _(penguins):
    penguins_1 = penguins[penguins.body_mass_g.notna()]
    return (penguins_1,)


@app.cell
def _(penguins_1):
    penguins_1.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice that we immediately used `info()` to check and make sure we only dropped two rows.

    It looks like the 'sex' column is the only one that still has missing values. Let's figure out what the percentage of missing values is:
    """)
    return


@app.cell
def _(penguins_1):
    penguins_1.sex.isnull().sum()
    return


@app.cell
def _(penguins_1):
    penguins_1.sex.isnull().sum() / penguins_1.shape[0] * 100
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Only about 2.6% of the values in the 'sex' column are missing. There are various ways we could take care of these values:

    1. As mentioned, we could drop these rows.
    2. We could use one of Scikit-learn's imputer functions to figure out a value for us.
    3. We could use the average (numerical) or the most frequent value (category)
    4. **We could use machine learning to guess the values.**

    \#4 is interesting -- if we consider our column with missing data as being our target, and columns that have data as being our predictor variables, then we can construct a machine learning model using complete records as the train and test data and records with incomplete entries as our general target.

    Let's try it:


    First, we have to make sure our target column has only "Male", "Female", and " ".
    """)
    return


@app.cell
def _(penguins_1):
    penguins_1.loc[(penguins_1.sex != 'Male') & (penguins_1.sex != 'Female')]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First, though, we need to change the **'object'** columns to categories.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Categorical Data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The columns that have an **object** type have non-numeric data in them. That data could be something with little analytical value (like an individual person's name), or it could be something like a category. In this case, we could consider **species, island, and sex** to be categories.

    Most machine learning algorithms won't work with string data, but Pandas has a "category" data type that will display a string for **your** convenience, but actually be a number for the ML.

    There are some complexities to be aware of when converting categories from string to numeric. Numbers imply order. If we number the species like so:

    * 1 - Chinstrap
    * 2 - Adelie
    * 3 - Gentoo

    Does that imply that Chinstrap is *better* than Gentoo? There are more of them? They are bigger? In our case, the numbers have no meaning and we have to make sure the ML algorithms understand that.

    Pandas "category" type can be either ordered or unordered, with unordered being the default. Let's convert those columns now.
    """)
    return


@app.cell
def _(penguins_1):
    penguins_1.species = penguins_1.species.astype('category')
    penguins_1.island = penguins_1.island.astype('category')
    penguins_1.sex = penguins_1.sex.astype('category')
    penguins_1.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Pandas get_dummy()
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Even though the columns are categories, they still need to be encoded, and Pandas has a function to help with that.
    """)
    return


@app.cell
def _(pd, penguins_1):
    peng_encoded = pd.get_dummies(penguins_1, columns=['island', 'species'], prefix=['island', 'species'])
    peng_encoded
    return (peng_encoded,)


@app.cell
def _(peng_encoded):
    peng_encoded.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, just simple 0/1 for 'sex'.
    """)
    return


@app.cell
def _(peng_encoded):
    peng_encoded['sex'] = peng_encoded['sex'].map({'Male':0, 'Female':1})
    return


@app.cell
def _(peng_encoded):
    peng_encoded.isnull().sum()
    return


@app.cell
def _(peng_encoded):
    peng_encoded.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    Scikit-learn also has many types of encoding for categories. You should spend some time investigating them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Impute Missing Data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Typically, we use capital 'x' as the dataset variable and 'y' as the target. We will be using a simple form of **supervised** machine learning, RandomForestClassifier.

    In supervised ML, our training dataset has to have known target values, so we will divide our data for training, testing and prediction.

    Now, for our data, we want all the rows that have a complete set of data and all the columns except 'sex'. That one will go into our training target dataset.
    """)
    return


@app.cell
def _(peng_encoded):
    columns = [c for c in peng_encoded.columns if c != 'sex']
    return (columns,)


@app.cell
def _(columns):
    columns
    return


@app.cell
def _(columns, peng_encoded):
    X = peng_encoded[peng_encoded.sex.notnull()].loc[:,columns]
    X
    return (X,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, we need all the 'sex' values that are not null and corresponding to the array above.

    The first set of square brackets choose which rows we want -- the not null ones -- and the second set choose the column we want.
    """)
    return


@app.cell
def _(peng_encoded):
    y = peng_encoded[peng_encoded.sex.notnull()]['sex']
    y
    return (y,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next, I'm going to split up the training data so I have a testing set and can look at accuracy statistics.
    """)
    return


@app.cell
def _():
    from sklearn.model_selection import train_test_split

    return (train_test_split,)


@app.cell
def _(X, train_test_split, y):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return x_test, x_train, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we import and use the classifier.
    """)
    return


@app.cell
def _():
    from sklearn.ensemble import RandomForestClassifier

    return (RandomForestClassifier,)


@app.cell
def _(RandomForestClassifier):
    clf = RandomForestClassifier(n_estimators=100)
    return (clf,)


@app.cell
def _(clf, x_train, y_train):
    clf.fit(x_train, y_train)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That's all there is to training the Classifier. Let's see how we did:
    """)
    return


@app.cell
def _(clf, x_test):
    y_pred = clf.predict(x_test)
    return (y_pred,)


@app.cell
def _(y_pred):
    y_pred
    return


@app.cell
def _(y_test):
    len(y_test)
    return


@app.cell
def _():
    from sklearn import metrics

    return (metrics,)


@app.cell
def _(metrics, y_pred, y_test):
    print(f'Model accuracy = {metrics.accuracy_score(y_test,y_pred)}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That's almost 90% accurate. Not bad! We could probably get better by segregating island and species, and on larger datasets it would probably be worth it.

    Now, let's get the missing values and move on...
    """)
    return


@app.cell
def _(columns, peng_encoded):
    x_missing = peng_encoded[peng_encoded.sex.isnull()].loc[:,columns]
    x_missing
    return (x_missing,)


@app.cell
def _(clf, x_missing):
    y_missing = clf.predict(x_missing)
    return (y_missing,)


@app.cell
def _(y_missing):
    y_missing
    return


@app.cell
def _(peng_encoded):
    peng_encoded_bk = peng_encoded.copy()
    return


@app.cell
def _(x_missing, y_missing):
    x_missing['sex'] = y_missing.astype('int')
    return


@app.cell
def _(x_missing):
    x_missing
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Interestingly enough, it looks like the original indexes followed the rows all the way through the process. We should be able to use that to put the values back in the original dataframe.
    """)
    return


@app.cell
def _(x_missing):
    x_missing.loc[8]
    return


@app.cell
def _(penguins_1):
    penguins_1.loc[8]
    return


@app.cell
def _(x_missing):
    x_missing.index.to_list()
    return


@app.cell
def _(x_missing):
    x_missing['sex'] = x_missing['sex'].map({0:'Male', 1:'Female'})
    return


@app.cell
def _(x_missing):
    x_missing
    return


@app.cell
def _(penguins_1, x_missing):
    #put the imputed values back into the original data frame

    penguins_1.loc[x_missing.index.to_list()] = x_missing.loc[x_missing.index.to_list()]
    return


@app.cell
def _(penguins_1):
    penguins_1.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, the rows with the missing 'sex' data has the predictions added back in. All that is left to do is add the two dataframes back together and reset the index.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice the **inplace=True** above.

    Let's check to make sure there aren't any NaNs left:
    """)
    return


@app.cell
def _(penguins_1):
    penguins_1.isnull().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Variance
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sometimes columns will have only 1 value or a very small number of unique values. Analytically speaking, these columns aren't worth much.

    **Variance** is defined as the average value from the mean. Therefore, columns that have only one value have **_zero_** variance.

    Let's briefly load a "standard" example machine learning data set to demonstrate.
    """)
    return


@app.cell
def _(pd):
    oil = pd.read_csv('data_wk3/oil-spill.csv', header=None)
    return (oil,)


@app.cell
def _(oil):
    oil.head()
    return


@app.cell
def _(oil):
    oil.shape
    return


@app.cell
def _(oil):
    oil.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll use the Pandas `nunique()` function to see how many unique values exist in each column:
    """)
    return


@app.cell
def _(oil):
    oil.nunique()
    return


@app.cell
def _(oil):
    oil[22].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, Column 22 has only 1 unique value and several columns have fewer than 10 unique values.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Boxplots
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Box-and-whisker plots, or just boxplots, can help detect this type of problem, also. Recall:<br>
    * The top and bottom "whiskers" show min and max values, <br>
    * The bottom of the box shows the first quartile<br>
    * The line in the middle shows the median<br>
    * The top of the box shows the third quartile.<br>
    * Outliers are shown outside of the min/max whiskers.<br>

    Pandas knows how to make boxplots of columns. It can plot all columns (default) or a list of columns. Here are a couple of examples from the oil spill dataset above:
    """)
    return


@app.cell
def _(oil):
    oil.boxplot([2,3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, compare that to columns 22, 36, 45, etc.
    """)
    return


@app.cell
def _(oil):
    oil.boxplot([22, 36, 45, 49])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Something is obviously going on with those columns, and they should be investigated before being used in modeling and analysis. You don't want to throw away a perfectly good categorical column that is already in number form.

    Now, let's go back to our penguins. If we just ask Pandas to create a default boxplot, we see that the body_mass_g column overshadows the others (indicating it may be a good candidate for scaling, later).
    """)
    return


@app.cell
def _(penguins_1):
    penguins_1.boxplot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's look at the columns without body_mass_g:
    """)
    return


@app.cell
def _(penguins_1):
    penguins_1.columns
    return


@app.cell
def _(penguins_1):
    penguins_1.boxplot(['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm'])
    return


@app.cell
def _(penguins_1):
    penguins_1.boxplot(['bill_length_mm', 'bill_depth_mm'])
    return


@app.cell
def _(penguins_1):
    penguins_1.nunique()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Duplicate Rows
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pandas can give us some help in identifying duplicate rows, although it just gives us a True or False. To see it in action, let's look at the **Iris** data set:
    """)
    return


@app.cell
def _(sns):
    iris = sns.load_dataset('iris')
    return (iris,)


@app.cell
def _(iris):
    iris.duplicated()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To really see what is going on, we can use the Python `any()` filter:
    """)
    return


@app.cell
def _(iris):
    iris.duplicated().any()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    OK, so we have some duplicates. Let's put that back in the dataset to see which ones:
    """)
    return


@app.cell
def _(iris):
    dupes = iris.duplicated()
    print(iris[dupes])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pandas also has a `drop_duplicates()` function to help.
    """)
    return


@app.cell
def _(iris):
    print(f'Before: {iris.shape}')
    iris.drop_duplicates(inplace=True)
    print(f'After: {iris.shape}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Outliers
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Outliers are data points that **lie out**side of "normal" observations.

    As we saw earlier, boxplots can show us outliers, and so can scatter plots. Remember, column 3 of the **oil** data set had some outliers:
    """)
    return


@app.cell
def _(mo, oil, plt):
    #plot columns 2 and 3 on a scatter plot

    plt.scatter(oil[2], oil[3])
    ax = mo.ui.matplotlib(plt.gca())
    ax
    return (ax,)


@app.cell
def _(ax, np, oil):
    mask = ax.value.get_mask(oil[2], oil[3])
    np.column_stack([oil[2][mask], oil[3][mask]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It really gets fun when we add color. Let's look at our penguins...

    I'm switching to Seaborn because Pandas can't interpret 'species' unless I convert it to a number.
    """)
    return


@app.cell
def _(mo, penguins):
    #scatter plot of penguins flipper length vs body mass by species
    import altair as alt
    penguins_chart=mo.ui.altair_chart(alt.Chart(penguins).mark_point().encode(
        x=alt.X('flipper_length_mm:Q', title='Flipper Length (mm)'),
        y=alt.Y('body_mass_g:Q', title='Body Mass (g)'),
        color=alt.Color('species:N', title='Species'),

    ))
    return alt, penguins_chart


@app.cell
def _(mo, penguins_chart):
    mo.vstack([penguins_chart, mo.ui.table(penguins_chart.value)])
    return


@app.cell
def _(penguins_1, sns):
    sns.scatterplot(data=penguins_1, x='flipper_length_mm', y='body_mass_g', hue='species')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wow... there is clearly a linear relationship between flipper length and body mass, and Gentoo penguins are obviously larger than the other two species.

    Sometimes the outliers aren't as easy to identify visually. **Jason Brownlee** presents several methods for mathematically determining outliers, including:<br>
    * Standard deviation method<br>
    * Interquartile range method<br>

    Then he introduces **Automatic Outlier Detection** using SciKit-Learn's `LocalOutlierFactor` class and demonstrates how removing outliers improves predictive accuracy using one of the simplest forms of predictive modeling -- linear regression. In a nutshell, linear regression uses the training data to draw a straight "regression" line on the graph of the data. Predictive requests are then matched up to the appropriate (x, y) coordinate and the resulting value returned.

    Mr. Brownlee's code is reproduced below:

    First, **linear regression** leaving the outliers in:
    """)
    return


@app.cell
def _(train_test_split):
    from pandas import read_csv
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error
    df = read_csv('data_wk3/housing.csv', header=None)
    data = df.values
    X_1, y_1 = (data[:, :-1], data[:, -1])
    X_train, X_test, y_train_1, y_test_1 = train_test_split(X_1, y_1, test_size=0.33, random_state=1)
    model = LinearRegression()
    model.fit(X_train, y_train_1)
    _yhat = model.predict(X_test)
    _mae = mean_absolute_error(y_test_1, _yhat)
    print('MAE: %.3f' % _mae)
    return (
        LinearRegression,
        X_test,
        X_train,
        df,
        mean_absolute_error,
        y_test_1,
        y_train_1,
    )


@app.cell
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    According to https://www.statisticshowto.com/absolute-error/, **Absolute Error** measures the difference between a measured value and the "true" value. In this case, it is the difference between the **predicted** value and the true value.

    **Mean Absolute Error (MAE)** measures the mean of all absolute errors in a group of observations (like our test data set).

    Now, let's remove the outliers:
    """)
    return


@app.cell
def _(
    LinearRegression,
    X_test,
    X_train,
    mean_absolute_error,
    y_test_1,
    y_train_1,
):
    from sklearn.neighbors import LocalOutlierFactor
    print(X_train.shape, y_train_1.shape)
    lof = LocalOutlierFactor()
    _yhat = lof.fit_predict(X_train)
    mask_1 = _yhat != -1
    X_train_1, y_train_2 = (X_train[mask_1], y_train_1[mask_1])
    print(X_train_1.shape, y_train_2.shape)
    model_1 = LinearRegression()
    model_1.fit(X_train_1, y_train_2)
    _yhat = model_1.predict(X_test)
    _mae = mean_absolute_error(y_test_1, _yhat)
    print('MAE: %.3f' % _mae)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    The decrease in **Mean Absolute Error** indicates an increase in accuracy. The easy assumption is that the outliers biased the model's learning and thus affected the predictive ability.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Feature Selection
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Features** are, of course, the columns of your dataset.

    **Feature selection** involves deciding which features to include in the training and usage of machine learning models.

    > Many models, especially those based on regression slopes and intercepts, will estimate
    parameters for every term in the model. Because of this, the presence of non-
    informative variables can add uncertainty to the predictions and reduce the overall
    effectiveness of the model.
    >
    > *— Page 488, Applied Predictive Modeling, 2013.*

    Besides accuracy concerns, with many model types, more features will mean increased training time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pairplot
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Seaborn has the ability to plot each feature, one by one, against the others. As you can see below, this is an easy way to uncover linear relationships.

    **Caution:** Doing a pairplot on a large dataset with no restrictions can bring your computer to its knees. Only plot **subsets** of the variables, as appropriate.
    """)
    return


@app.cell
def _(penguins_1, sns):
    sns.pairplot(penguins_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Correlation matrix and heatmaps
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A Pandas dataset knows how to create a correlation matrix showing relationships among all the features. While this can be useful, it outputs a table of numbers that can be hard to intrepret over a large dataset.

    The `corr()` function does a pearson correlation by default, although others are available.
    """)
    return


@app.cell
def _(penguins_1):
    # Pandas' pearson correlation
    corrmat = penguins_1.corr(numeric_only=True)
    corrmat
    return (corrmat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A much better way is to put the correlation matrix into a Seaborn heatmap.

    Note that the heatmap will show both positive and negative correlations.
    """)
    return


@app.cell
def _(corrmat, plt, sns):
    _f, _ax = plt.subplots(figsize=(12, 10))  #setting some parameters of the plot to help readability

    heatmap = sns.heatmap(corrmat, vmax=0.8, square=True)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---

    It might be useful to see the actual correlation values in the heatmap cells. To do that, we can turn on cell annotations with the `annot=True` parameter:
    """)
    return


@app.cell
def _(corrmat, plt, sns):
    #include n
    _hm = sns.heatmap(corrmat, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10})
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    And yet another way to do it with altair to be able to utilize the interactive features.
    """)
    return


@app.cell
def _(alt, corrmat, mo):
    #make heatmap of the correlation matrix interactive with altair
    penguins_heatmap = mo.ui.altair_chart(alt.Chart(corrmat.reset_index().melt('index')).mark_rect().encode(
        x='index:N',
        y='variable:N',
        color='value:Q'
    ).properties(
        width=400,
        height=400)
    )
    penguins_heatmap
    return (penguins_heatmap,)


@app.cell
def _(mo, penguins_heatmap):
    mo.vstack([penguins_heatmap, mo.ui.table(penguins_heatmap.value)])
    return


@app.cell
def _(penguins_1):
    _cols = penguins_1.columns
    _cols
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But what if we have a whole bunch of variables? Remember our housing dataset? Let's look at a version that has headers real quick:
    """)
    return


@app.cell
def _(pd):
    house = pd.read_csv('data_wk3/housing_train.csv')
    house.head()
    return (house,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's drop that Id column. It won't help anything in the analysis.
    """)
    return


@app.cell
def _(house):
    house.drop('Id', axis=1, inplace=True)
    return


@app.cell
def _(house):
    house.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    81 columns should be enough to prove a point.

    First, the heatmap:
    """)
    return


@app.cell
def _(house):
    house_cor = house.corr(numeric_only=True)
    return (house_cor,)


@app.cell
def _(house_cor, sns):
    sns.heatmap(house_cor)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Looks a bit like a pizza!

    Maybe making it bigger will help.
    """)
    return


@app.cell
def _(house_cor, plt, sns):
    _f, _ax = plt.subplots(figsize=(12, 10))  #setting some parameters of the plot to help readability
    sns.heatmap(house_cor, vmax=0.8, square=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That's still a lot of variables. **SalePrice** is often our ML target variable, trying to predict sales price based on other factors. Let's look at the top 10 variables related to SalePrice.
    """)
    return


@app.cell
def _(house, house_cor, np, plt, sns):
    #correlation matrix of the top 10 most correlated features with SalePrice
    k = 10
    _cols = house_cor.nlargest(k, 'SalePrice')['SalePrice'].index
    cm = np.corrcoef(house[_cols].values.T)
    sns.set(font_scale=1.25)    
    _f, _ax = plt.subplots(figsize=(10, 8))
    _hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 14}, yticklabels=_cols.values, xticklabels=_cols.values)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Statistical selection
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Jason Brownlee** very helpfully breaks statistics-based feature selection down based on **input variable** and **output type.** Either one can be numerical or categorical. The output variable type will be determined by the type of problem you are solving.

    **Output Variable**:
    * Numerical -- Regression predictive modeling.
    * Categorical -- Classification predictive modeling.

    <img style="padding-right:10px;" src="figures_wk3/feature_selection_graph.png" ><br>

    Pearson's was demonstrated above with the correlation matrix and heatmaps. Other methods will be demonstrated later and throughout your education.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Feature importance -- RandomForest
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One of my favorite methods of choosing features is to let the RandomForest algorithm tell me what it decided was important.

    Tree-based algorithms operate very much like a single *binary tree*. A starting point is determined, then a decision is made to get down to the next level, over and over, until an answer is reached. The graph above showing variable selection is a good example.

    Classification and regression trees (CART) track the importance of the variables at the decision points.

    A **RandomForest** uses a whole bunch of decision trees to solve a problem, and because many trees are used, many solutions can be tried, improving results.

    Let's use a `RandomForestRegressor` on the housing dataset and see if it agrees with what our heatmap told us.

    **First**, the RandomForestRegressor will only use numeric data, so we are going to ignore the categorical columns, for now. a truly complete picture would include them, of course.

    The correlation matrix dataset above should give us the column names of the numeric columns, so we'll just make a subset using it, but first we'll have to deal with **missing values**. In this case, we will drop them. **If I were really trying to do predictions, I would impute them.**
    """)
    return


@app.cell
def _(house_cor):
    house_cor.columns
    return


@app.cell
def _(house, pd):
    #missing data
    total = house.isnull().sum().sort_values(ascending=False)
    percent = (house.isnull().sum()/house.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    missing_data.head(20)
    return (missing_data,)


@app.cell
def _(house, missing_data):
    #dealing with missing data
    house_1 = house.drop(missing_data[missing_data['Total'] > 1].index, axis=1)
    house_1 = house_1.drop(house_1.loc[house_1['Electrical'].isnull()].index, axis=0)
    house_1.isnull().sum().max()  #just checking that there's no missing data missing...
    return (house_1,)


@app.cell
def _(house_1):
    #dealing with categorical data
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    for col in house_1.columns:
        if house_1[col].dtype == 'string' or house_1[col].dtype == 'object':
            house_1[col] = le.fit_transform(house_1[col])
    house_1.head()
    house_1.columns
    return


@app.cell
def _(house_1):
    #X = df.drop(columns=['target_column']) 
    X_2 = house_1.drop(columns=['SalePrice'])
    X_2
    return (X_2,)


@app.cell
def _(house_1):
    y_2 = house_1['SalePrice'].values
    y_2
    return (y_2,)


@app.cell
def _():
    from sklearn.ensemble import RandomForestRegressor

    return (RandomForestRegressor,)


@app.cell
def _(RandomForestRegressor):
    model_2 = RandomForestRegressor()
    return (model_2,)


@app.cell
def _(X_2, model_2, y_2):
    model_2.fit(X_2, y_2)
    return


@app.cell
def _(X_2, model_2):
    importance_list = list(zip(X_2.columns, model_2.feature_importances_))
    sorted_importance = sorted(importance_list, key=lambda x: x[1], reverse=True)
    # importance = model.feature_importances_
    # X.columns
    sorted_importance
    return (sorted_importance,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You would need to make a decision at what point a feature is not important enough to use. **Many times I'll throw in a column of random numbers and use all the columns that are more important than the randoms.**

    Here is a really fancy way to display the list -- I'll leave it up to you to figure out how it works.
    """)
    return


@app.cell
def _(X_2):
    max_feature_len = len(max(X_2.columns, key=len))
    return (max_feature_len,)


@app.cell
def _(max_feature_len, sorted_importance):
    for feature, rank in sorted_importance:
        dots = max_feature_len - len(feature)
        print(f'{feature}: {"."*dots} {rank*100:.2f}%')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    The section below doesn't really relate to anything beyond some advanced Pandas usage. I just didn't want to throw it away after I got that far and then decided to go a different way.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Bonus -- finding average weights by gender
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Another way to deal with missing 'sex' entries is to try to fill in the values based on weight (or mass, in this case). The cells below make a dataset of the min, max and mean for each species as a start to this method.
    """)
    return


@app.cell
def _(penguins_1):
    penguins_1[(penguins_1.species == 'Adelie') & (penguins_1.sex == 'Male')].body_mass_g.max()
    return


@app.cell
def _(penguins_1):
    penguins_1[(penguins_1.species == 'Adelie') & (penguins_1.sex == 'Male')].body_mass_g.min()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It's great to be able to figure these out one at a time, but what if we had 100 speies? We need to generalize this.
    """)
    return


@app.cell
def _(penguins_1):
    peng_mass = penguins_1.groupby(['species', 'sex']).agg({'body_mass_g': ['min', 'max', 'mean']})
    return (peng_mass,)


@app.cell
def _(peng_mass):
    peng_mass
    return


@app.cell
def _(peng_mass):
    type(peng_mass)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    OK, this is good. this gave us min and max ranges for each species, but our resulting dataframe is some weird multi-indexed thing. We can **reset the index** to fix some of it:
    """)
    return


@app.cell
def _(peng_mass):
    # Remember, this isn't permanent until we use an assignment ('=')
    peng_mass.reset_index()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    But, the min, max, and mean columns are still oddly-named and difficult to access, as seen below:
    """)
    return


@app.cell
def _(peng_mass):
    peng_mass_1 = peng_mass.reset_index()
    peng_mass_1.iloc[0]
    return (peng_mass_1,)


@app.cell
def _(peng_mass_1):
    peng_mass_1.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    OK, one more try. Let's look at the `to_flat_index()` function:
    """)
    return


@app.cell
def _(peng_mass_1):
    peng_mass_1.columns.to_flat_index()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    Getting closer, maybe. Let's combine with a string `join()` function:
    """)
    return


@app.cell
def _(peng_mass_1):
    peng_mass_1.columns.to_flat_index().str.join('_')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    That looks pretty good. Let's make it permanent and see what the columns look like:
    """)
    return


@app.cell
def _(peng_mass_1):
    peng_mass_1.columns = peng_mass_1.columns.to_flat_index().str.join('_')
    peng_mass_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    OK, at this point we have options how to fill in the missing values based on our new table. Unfortunately, there is overlap in the weight ranges between males and females, so we can't just check which range the unknown falls into.
    """)
    return


@app.cell
def _(penguins_1):
    penguins_1[penguins_1.sex.isnull()]
    return


@app.cell
def _(peng_mass_1):
    peng_mass_1[(peng_mass_1.species_ == 'Adelie') & (peng_mass_1.sex_ == 'Female')].body_mass_g_mean
    return


if __name__ == "__main__":
    app.run()
