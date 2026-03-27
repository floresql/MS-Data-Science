# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "jinja2>=3.1.6",
#     "marimo>=0.20.2",
#     "pandas>=3.0.1",
#     "pyzmq>=27.1.0",
#     "seaborn>=0.13.2",
# ]
# ///

import marimo

__generated_with = "0.20.3"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import subprocess

    return


@app.cell
def _():
    #run in powershell
    #python -m marimo convert 1_Defining_Analytical_questions_working.ipynb "-o" 1_Defined_Analytical_questions.py
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 1 - Defining Analytical Questions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Book Recommendation**: Both of these books are great references that provide working examples in python.

    <img align="left" style="padding-right:50px;" src="figures_wk1/textbook_cover.png" width=100><br>
    >**Pandas for Everyone - Python Data Analysis** by Daniel Y. Chen<br>
    >**Publisher**: Addison-Wesley - Data &Analytics Series; 2nd edition (2023)<br>
    >**ISBN-13**: 978-0137891153<br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    >**Hands-On Exploratory Data Analysis with Python** by Suresh Kumar Mukhiya and Usman Ahmed <br>
    >**Publisher**: Packt>; 1st edition (2020)<br>
    >**ISBN-13**: 978-1789537253<br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Lecture Material Outline:**
    - Data Analytics Overview
    - Demo: Data Exploration using Pandas
    - Demo: Defining and Analyzing An Analytical Question
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Data Analytics Overview
    Data analytics is the science of analyzing raw data to make conclusions about that information. Any type of data can be subjected to data analytics techniques to get insight that can be used to improve things. All data analysis stems from a question(s) that are then analyzed through various data analytic techniques. Data analytic techniques can reveal trends and metrics that would otherwise be lost in the mass of information. This information can then be used to optimize processes to increase the overall efficiency of a business or system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What are analytical questions?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Analytical questions help you parse data and information to develop creative, rational solutions.

    An important step in data analytics is to ask a good analytical question: one that poses a challenging way of thinking about your data. Establishing that question won’t be your first step—you will need to do some data exploration prior to developing your analytical question(s).

    Tips to keep in mind:
    * Good analytical questions have the potential to highlight relationships between different sources or phenomena: patterns, connections, contradictions, dilemmas, and problems.
    * Good analytical questions can also ask about some implications or consequences of your analysis.
    * “How” and “why” questions generally require more analysis and complex thinking than “who,” “what,” “when,” and “where” questions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Analytic Tools
    Data science analysis tasks can be done in a variety of different programming languages and programs. Each one has pros and cons which must be evaluated against the tasks being performed, knowledge and skill of the analyst, type of data being analyzed, etc. Historically, the two most popular languages are **R** and **Python**. Over time we have seen a shift in popularity from R to Python, possibly as a consequence of data science moving out of the realm of pure statistics and incorporating more algorithmic, programming-heavy tasks such as machine learning.

    This week we will introduce the "Swiss army knife" of data analysis in Python -- **Pandas**. We start by discussing advantages of using Python and Pandas in data science, followed by basic dataframe operations, and finish with some analysis using grouping and aggragating functions.

    At the end of this unit, the student should be able to load tabular data files and perform rudimentary analysis. The student should also have a solid foundation from which to use online resources to find more advanced techniques.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Why Python?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:10px;" src="figures_wk1/languages.png" width=800><br>

    Python is a free, open source, general-purpose programming language that has been in existence since 1991. It is already known and in use by millions of programmers and relatively easy to learn for those new to the language. Since it is a general-purpose language, it can be used for more than just analysis.

    R is a free, open source statistical analysis package made popular by university researchers due to the low cost of ownership. Being a specialized language, it can be difficult to learn, particularly for those who already know programming. While R is, indeed, superior at the statistics aspect, it falls short of Python in both data manipulation ("data wrangling") and machine learning, and it is not really possible to write an "R program" that stands alone as can be done with Python. This means in many business contexts when analytical code is deployed for general usage, it must be translated from R to another language.



    **Reference:**
    - https://www.datasciencecentral.com/profiles/blogs/best-languages-for-data-science-and-statistics-in-one-picture*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Why Pandas?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As mentioned in the Overview, the Pandas library is the "Swiss army knife," or all-purpose tool, used in manipulating row - column oriented data. It is popularly said in the data science community that 70% or more of a data scientist's time is spent "wrangling data" -- cleaning, transforming, etc.

    Under the covers, Pandas relies on the high-performance Numpy mathematical library for many of its operations and over the years has been refined and optimized to be exceptionally good at its purpose.

    Pandas makes it very easy to operate on rows, columns, or entire tables (called **dataframes**).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Demo: Data Exploration using Pandas Functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's stop and review using Pandas to explore a dataset. For this demo we will be using the Titanic dataset.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Look at your data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The first step in any type of data analysis is to **look** at your data.

    The actual data file is in the data_wk1 directory (if you downloaded the notebook and data files), and is called `titanic.csv`. The `.csv` means that the file is Comma Separated Values, which means the file is already organized in row and column format. Usually (**but not always**) the first row is a header row that contains the column names.
    """)
    return


@app.cell
def _():
    import os
    print(os.getcwd())
    return (os,)


@app.cell
def _(os):
    files = os.listdir(".")
    print(files)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-info">
    <b>Helpful Hint::</b> You can execute os commands from within your notebook by starting the command with '!'.  <br> <br>
    For example, to list out all the files in a directory,<br>
    * On a PC:  type files : os.listdir(".")
    print(files) <br>
    * On a MAC: type files : os.listdir(".")
    mo.ui.table(files) <br>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data files and file loading
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We first have to import the Pandas library. You only have to do imports once per notebook.
    """)
    return


@app.cell
def _():
    # Import necessary libraries
    import pandas as pd
    import seaborn as sns   # This and next line to make graphs look better

    sns.set_theme()
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's load the data into a dataframe:
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('data_wk1/titanic.csv')
    df
    return (df,)


@app.cell
def _(df, mo):
    mo.ui.dataframe(df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dataframes
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A dataframe can be considered to be a representation of the data in table form. Dataframes have rows and columns. Each row can be cansidered an "observation" in terms of experimentation, or as one complete data point. Each column represents a "variable" or "feature" that can be measured, quantified, or qualified in some way. These terms will become clearer as we look at our example data.

    First, let's look at the size of the dataframe.
    """)
    return


@app.cell
def _(df):
    df.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This tells us there are 891 rows and 15 columns.

    The `(891, 15)` is called a **tuple**. According to Wikipedia, the name comes from naming the numeric progression: single, double, triple, quadruple, quadruple, quintuple, sextuple, septuple, octuple, ..., n‑tuple, ..., . (https://en.wikipedia.org/wiki/Tuple)

    Anyway, they are just like lists except you can't change them. So, to access the first element:
    """)
    return


@app.cell
def _(df):
    df.shape[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's look at the first few rows:
    """)
    return


@app.cell
def _(df):
    df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And the bottom of the data:
    """)
    return


@app.cell
def _(df):
    df.tail()
    return


@app.cell
def _(df):
    df.sample(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, the column names:
    """)
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Descriptive Statistics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Descriptive statistics are used to describe basic features of the data in a study. When describing a single variable (univariate analysis), or column in our case, descriptive statistics are:

    * Distribution
    * Central tendency
    * Dispersion

    Before we do anything fancy, though, let's look at some facts about each column:
    """)
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On the second line down, we see `RangeIndex: 891 entries, 0 to 890` meaning we have 891 rows in the dataframe.

    After that we have a list of each column, how many **non-null** values are in it(this will be important later), and what data type the column is.

    Next, we can look at distribution with a histogram:
    """)
    return


@app.cell
def _(df, mo):
    #select only the numeric columns
    numeric_df = df.select_dtypes(include='number')

    dropdown = mo.ui.dropdown(df.select_dtypes("number").columns, 
                              label="Select variable")

    dropdown
    return (dropdown,)


@app.cell
def _(df, dropdown):
    import matplotlib.pyplot as plt

    plt.figure()
    plt.hist(df[dropdown.value].dropna(), bins=30)
    plt.title(f"Histogram of {dropdown.value}")
    plt.show()
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pandas chose the number of bins for us but we could have stated it explicitly also, like so:
    """)
    return


@app.cell
def _(df, dropdown, plt):
    plt.hist(df[dropdown.value].dropna(), bins=4)
    plt.title(f"Histogram of {dropdown.value}")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, we can look at central tendency and dispersion with the `describe()` function:
    """)
    return


@app.cell
def _(df):
    df.describe(include='all')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That might be easier to look at if it was rotated (Transposed):
    """)
    return


@app.cell
def _(df):
    df.describe().T
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or, if you would like to see that in a box and whisker plot:
    """)
    return


@app.cell
def _(df):
    df.boxplot('age')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rows
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are a few different ways to work with rows, some of which can be a bit confusing. Probably the easiest and safest way to refer to rows is to use their index number (although sometimes that number can be hidden. That is outside the scope of this class).

    If we wanted to look at the first row, an easy way to do so would be to use `iloc[]`:
    """)
    return


@app.cell
def _(df):
    df.iloc[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice that `iloc[]` has square brackets on the end, **NOT** parentheses. This makes looking at multiple rows look a little weird:
    """)
    return


@app.cell
def _(df):
    df.iloc[[1, 10, 100]] # Two sets of square brackets?
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since `iloc[]` uses square brackets, when we pass a **list** to it, like we did above, it gives the double-square bracket syntax.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Columns
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We saw earlier how to get a list of column names:
    """)
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Columns can also be referenced by name:
    """)
    return


@app.cell
def _(df):
    df['age'].head()
    return


@app.cell
def _(df):
    df.age.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And you can specify groups of columns with lists:
    """)
    return


@app.cell
def _(df):
    slice = ['survived','pclass','age']
    df[slice].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Slices
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A slice of some container, like a list or dataframe, just means a section or segment of that container.

    Some examples -- remember, a string is just a list of characters...
    """)
    return


@app.cell
def _():
    import string

    return (string,)


@app.cell
def _(string):
    alpha = string.ascii_letters
    alpha
    return (alpha,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A slice of the first five characters:
    """)
    return


@app.cell
def _(alpha):
    alpha[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And, since the default starting position is 0, above is equivalent to this:
    """)
    return


@app.cell
def _(alpha):
    alpha[:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To get the last character:
    """)
    return


@app.cell
def _(alpha):
    alpha[-1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The last 5:
    """)
    return


@app.cell
def _(alpha):
    alpha[-5:]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When we start discussing more dimensions, like nested lists or dataframes (tables), things get more complicated. The syntax looks like this:

    ```
    df[ row_start : row_stop, column_start : column_stop ]
    ```

    So, if you wanted rows 5, 6, 7 and all columns:
    """)
    return


@app.cell
def _(df):
    df.iloc[5:8, :]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we wanted all rows but only the first two columns:
    """)
    return


@app.cell
def _(df):
    df.iloc[:, 0:2]
    return


@app.cell
def _(mo):
    mo.md(r"""
    This extracts rows 5-8 and the the first 2 columns. Python is zero- indexed.
    """)
    return


@app.cell
def _(df):
    df.iloc[5:8,0:2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Deleting rows and columns
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A necessary part of data analytics is the cleansing of your data. We often have to remove rows or columns. This is accomplished with the `drop()` function.

    First, let's make a copy of the dataframe so we don't mess up our original data.
    """)
    return


@app.cell
def _(df):
    df_copy = df.copy()
    df_copy.head()
    return (df_copy,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, let's drop the first row of the copy:
    """)
    return


@app.cell
def _(df_copy):
    df_copy.drop(df_copy.index[0])
    return


@app.cell
def _(df_copy):
    df_copy.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What happened? The `drop()` showed us the dataframe without the row, but `head()` shows it still there?

    `drop()` returns the dataframe with the row(s) or column(s) dropped, but does not change the actual dataframe. To make a permanent change you have 2 choices:

    `df_copy.drop(df_copy.index[0], inplace=True)`

    or

    `df_copy = df_copy.drop(df_copy.index[0])`

    Both methods have advantages. In this case, I know we won't ever want that row back, so I'll use `inplace=True`.
    """)
    return


@app.cell
def _(df_copy):
    df_copy.drop(df_copy.index[0], inplace=True)
    return


@app.cell
def _(df_copy):
    df_copy.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, let's look at columns. As we saw above, a couple of the columns have very few actual values. Let's look at that graphically:
    """)
    return


@app.cell
def _(df_copy):
    missing = df_copy.isnull().sum()
    missing = missing[missing > 0]
    missing.sort_values(inplace=True)
    missing.plot.bar()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or, in numbers:
    """)
    return


@app.cell
def _(df_copy, pd):
    total = df_copy.isnull().sum().sort_values(ascending=False)
    percent = (df_copy.isnull().sum()/df_copy.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    missing_data.head(20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    77% of the 'deck' column is null. I would normally drop a column with this many NaNs before conducting any data analysis or modeling.
    """)
    return


@app.cell
def _(df_copy):
    df_copy.drop(columns=['deck'], inplace=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And, it is **always** smart to check your work to make what you think happened actually happened.
    """)
    return


@app.cell
def _(df_copy, pd):
    total_1 = df_copy.isnull().sum().sort_values(ascending=False)
    percent_1 = (df_copy.isnull().sum() / df_copy.isnull().count()).sort_values(ascending=False)
    missing_data_1 = pd.concat([total_1, percent_1], axis=1, keys=['Total', 'Percent'])
    missing_data_1.head(20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Much better!

    Now, on to...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Apply
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `apply()` function is a bit of a "cheat code," to borrow video gamer terminology. `apply()` allows you to custom-write a function and apply it to rows, columns, or the entire dataframe, thus giving us the ability to create new functionality that isn't inherent in Pandas.

    For example, let's look at the unique values in the `sex` column:
    """)
    return


@app.cell
def _(df):
    df['sex'].unique()
    #df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `sex` is actually a categorical variable that divides the Titanic passengers on the boat. In this way, it could serve as a sorting value for the passengers -- might be useful if we want to test the old "women and children first" saying. The problem is, machine learning algorithms don't like text (mostly). Scikit-Learn has functions to help us encode categorical columns like this, but let's do it manually to see how `apply()` works.

    We are going to write a little function that takes one variable as input (value of sex in any given row) and returns a numerical code. We will store that number in a new column called `gender`.

    Remember, this is a demonstration. There are many ways to handle creating columns and re-categorizing content.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First, we are going to create a custom function that takes one variable as input:
    """)
    return


@app.function
def return_gender(sex):
    if sex == 'male':
        return 0
    elif sex  == 'female':
        return 1
    else:
        return -999


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then we will put it into the `apply()` function. The magic of `apply()` says if we use it on a specific column, `apply()` will go row by row, applying your function to the current value. That is why our function needs to take an input variable -- that is the row's value we want to change.

    You may be wondering about the -999. That is just insurance in case there is something we don't expect in the column -- Someone misspelled 'male' as 'mail', perhaps. Most machine learning algorithms are smart enough to deal with these types of 'wildly different' entries, like -999, so they don't influence the model training.
    """)
    return


@app.cell
def _(df):
    df['gender'] = df['sex'].apply(return_gender)
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, we added the new column with values based on what is in the 'sex' column.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Aggregating

    *Reference: https://pbpython.com/groupby-agg.html*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aggregating, in this context, means taking a bunch of values and using some summary function to return (usually) a single value. Most times, the summary function is a simple summation or mean.

    An example:
    """)
    return


@app.cell
def _(df):
    df['fare'].agg( ['sum', 'mean'] )  #extra spaces for clarity
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the example above, we passed a list of functions to `agg()` and got the results of each back out.

    There are multiple ways to call aggragation functions but, in my opinion, the most useful is using a dictionary. We will call the `agg()` function on the entire dataframe and pass it a dictionary where the keys are the column names and the values are functions to be applied.

    ```
    df.agg( {'Fare' : ['sum', 'mean'],
             'Sex' : ['count'] } )
    ```
    """)
    return


@app.cell
def _(df):
    df.agg( {'fare' : ['sum', 'mean'],
             'sex' : ['count'] } )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, the most-often used aggragation functions:
    """)
    return


@app.cell
def _(df):
    df['fare'].agg( ['sum', 'mean', 'median', 'min', 'max', 'std', 'var', 'prod'] )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `prod` is the product of all the entries in the column. Probably not that useful, but included for completeness.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Groupby
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Descriptive statistics

    The `groupby()` function adds a powerful ability to group aggragation results based on values in the 'fare' column. Let's do the last aggragation and group it by the embarkation city:
    """)
    return


@app.cell
def _(df):
    df.groupby(['embark_town']).agg( {'fare':['sum', 'mean', 'median', 'min', 'max', 'std', 'var', 'prod']} )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You could also run the `describe()` function with the grouping:
    """)
    return


@app.cell
def _(df):
    df.groupby(['embark_town']).agg ( {'fare' : 'describe'} ).round(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Counting
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It is also common to want to count values grouped various ways.

    Let's use `count()`, `nunique()`, and `size()` to show how passengers from different embarkation cities were spread over different decks:
    """)
    return


@app.cell
def _(df):
    df.groupby(['deck']).agg( {'embark_town' : ['count', 'nunique', 'size']} )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice for deck B the `count` and `size` are different. That is because `count()` skips NaNs but `size()` does not. Subtle distinction that you should be aware of.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lambda functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Speaking of your own functions, sometimes you need a little, single-use function and it really isn't worth the energy to go through the whole

    ```
    def some_function(x):
        blah
        blah
        blah
    ```

    for times like that, we have **lambda functions**.

    For example, let's assume you wanted to capitalize the `sex` column. An easy way to do that to the whole column is to use `apply()`, but `apply()` needs a function. Seems like a lot of work just to call the string's `capitalize()` function.

    Let's say I wanted a lambda function that just takes a string as input, calls the string's `capitalize()` function and returns the capitalized string. It would look something like this:

    ```
    lambda s: s.capitalize()
    ```

    That's it! `s` is our input variable and the result of whatever is on the right side of the `:` gets returned. We could even set a variable equal to it so it looks a bit more like a regular function. Let's see that in action.
    """)
    return


@app.cell
def _():
    caps = lambda s: s.capitalize()

    caps('male')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Basically, anything you can cram on one line is fair game. For loops are common, so are if-else conditions. Let's see one of those:
    """)
    return


@app.cell
def _():
    caps_1 = lambda s: s.capitalize() if s == 'female' else s
    return (caps_1,)


@app.cell
def _(caps_1):
    caps_1('female')
    return


@app.cell
def _(caps_1):
    caps_1('male')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    OK, what happened there? The logic makes sense if you read it left to right and add a word or two...

    "Return s.capitalize() if s is female, else return s."

    Not so hard, right?

    As I mentoned above, the whole `caps = ` this is just a name. Actually, more like a "handle" to store the lambda function in memory and be able to get it back. **But**, we generally don't use assignment like that when using lambda functions in `apply()` (or others).

    For example:
    """)
    return


@app.cell
def _(df):
    df['sex'] =  df['sex'].apply(lambda s: s.capitalize() if s == 'female' else s)
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Formatting
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, a bit of fun.

     Pandas allows formatting of cells and cell contents. This means displaying dollar cells with only 2 decimal places, fill min or max value backgrounds with a color, and more. This is accomplished using the dataframe `style.format()`. With Python 3.13 version, you might need to install jinja2 for `style.format` to work.

    Let's see some examples:
    """)
    return


@app.cell
def _(df):
    # magic command not supported in marimo; please file an issue to add support
    # install jinja2
    import jinja2
    df.groupby(['embark_town']).agg( {'fare':['sum', 'mean', 'median', 'min', 'max']} ).style.format('${0:,.2f}')
    #fix the format
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Much of string formatting is a holdover from the old 'C' programming days and somewhat complicated. Google is your friend.

    Let's look at that same aggregation above but with no decimal places:
    """)
    return


@app.cell
def _(df):
    df.groupby(['embark_town']).agg( {'fare':['sum', 'mean', 'median', 'min', 'max']} ).style.format('${0:,.0f}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's do the same thing and highlight min and max values. I know, not very exciting with only 3 rows, but it will get the idea across.
    """)
    return


@app.cell
def _(df):
    (df.groupby(['embark_town'])
    .agg( {'fare':['sum', 'mean', 'median', 'min', 'max']} )
    .style.format('${0:,.2f}')
    .highlight_max(color = 'green')
    .highlight_min(color='red'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Demo: Defining and Analyzing An Analytical Question
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Phew! So at this point we have explored our dataset in a number of ways. It's important to note that level of your data exploration directly relates to the complexity of the analytical question(s) you formulate. Meaning, as the complexity of your analytical questions increases, so does the amount of data exploration.

    Let's take a look a defining and analyzing an analytical question for our dataset.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Question: Were women and children given priority in the evacuation process abroad the Titanic?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are several ways we could approach this question. For our demonstration, I'm going to limit my analysis to a comparison of the average age of survivors between male and female passengers. My reasoning is that if women and children where given priority in the evacuation process, we'd expect to see a lower average male survivor age than with the female passengers.

    I'm going to subset the orginal dataset to only include the columns that I think might be support my analysis.
    """)
    return


@app.cell
def _(df):
    q1_df = df.iloc[:, 0:4].copy()
    return (q1_df,)


@app.cell
def _(q1_df):
    q1_df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's compare the average age across the columns 'survived' and 'sex'.
    """)
    return


@app.cell
def _(q1_df):
    q1_df.groupby(['survived','sex']).age.mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hmmm...  For this dataset survived = 1 denotes a passenger that survived the Titanic disaster. So, this is showing us that amongst the survivors, the average age between males and females is roughly equal. Based on how we defined our analytical question above, I could conclude that I cannot support the claim that women and children where given priority in the evacuation process.

    **Important:** I purposely limited the scope of my investigation for this demo. To fully answer this question, I'd need to examine this question from a number of hypotheses/approaches.
    """)
    return


if __name__ == "__main__":
    app.run()
