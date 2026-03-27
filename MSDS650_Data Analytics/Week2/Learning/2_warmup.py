# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "pandas>=3.0.1",
#     "pyzmq>=27.1.0",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return mo, pd


@app.cell
def _():
    import subprocess

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Warmup Exercise - Defining and Answering Analytical Questions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As follow-on from week1, this week's warmup exercise will involve developing your own questions about a given dataset and  then answer those questions using python's Pandas library.

    ### Our Dataset

    **Dataset Name::** supermarket_sales.csv <br>
    The growth of supermarkets in most populated cities are increasing and market competitions are also high. The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data.

    |Column Name|Column Description|
    |---|---|
    |Invoice id| Computer generated sales slip invoice identification number|
    |Branch| Branch of supercenter (3 branches are available identified by A, B and C)|
    |City| Location of supercenters|
    |Customer type| Type of customers, recorded by Members for customers using member card and Normal for without member card|
    |Gender| Gender of customer|
    |Product line| General item categorization groups (Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel)|
    |Unit price| Price of each product in dollars|
    |Quantity| Number of products purchased by customer|
    |Tax| 5% tax fee for customer buying|
    |Total| Total price including tax|
    |Date| Date of purchase (Record available from January 2019 to March 2019)|
    |Time| Purchase time (10am to 9pm)|
    |Payment| Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)|
    |COGS| Cost of goods sold|
    |Gross margin percentage| Gross margin percentage|
    |Gross income| Gross income|
    |Rating| Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)|
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise
    This exercise maybe worked on in groups or individually. This exercise will be graded. Please post your group responses on the discussion forum.

    1) Define 3 in-depth questions you would like to investigate within this dataset.
    2) Use the techniques demonstrated in the week1 lecture materials to answer each of your questions.

    After you have dervied at an answer for each of your analytical questions, open the **analytical_questions_warmup.pptx** and follow the instructions in the pptx.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Load the data
    """)
    return


@app.cell
def _(pd):
    sales = pd.read_csv('supermarket_sales.csv')
    return (sales,)


@app.cell
def _(sales):
    sales.info()
    return


@app.cell
def _(mo, sales):
    mo.ui.data_explorer(sales)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercise

    ### Define 3 in-depth questions to investigate within this dataset.

    ***Question 1:*** Does customer type (Member vs. Normal) drive higher spending and customer satisfaction?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    First step is alway to import necessary libraries
    """)
    return


@app.cell
def _():
    import pandas as pd
    #import matplpotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    import seaborn as sns
    import jinja2 

    sns.set_theme(style="whitegrid")
    return (pd,)


@app.cell
def _(mo):
    mo.md(r"""
    Now lets read in the file and use some typical techniques to look at the makeup of the data.
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('supermarket_sales.csv')

    df.shape
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""
    The shape method shows us that there are 1,000 records and 17 columns.
    Let's take a look at those columns.
    """)
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(mo):
    mo.md(r"""
    Now that we know what columns are in the data, lets dig a little deeper and get some details like data types.
    """)
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ***Question 2:*** How does time of day and day of week affect transaction volume, basket size, and customer ratings?
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""
    ***Question 3:*** How does payment method interact with gender, product line, and average spend?
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## References

    Anthropic. (2026, March 21). *Pandas data analysis techniques reference from Python notebook* [Generative AI chat]. Claude Sonnet 4.6. https://claude.ai
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Appendix: AI-Generated Content

    **Tool:** Claude Sonnet 4.6 (Anthropic)
    **Date:** March 21, 2026
    **Topic:** Pandas Data Analysis Techniques

    ---

    ### Prompt Submitted to AI:

    could you make me a list of the techniques demonstrated in 1_defined_analytical_questions.py
    and describe what each one is used for and how it works? put them in numerical order.
    provide the results in a markdown file with code windows for code snippets of each technique

    ---

    ### Full-Text AI Response:

    The markdown file covers all **23 techniques** demonstrated in the notebook, in the order
    they appear, each with a code snippet. Here's a quick overview of what's covered:

    1–6: Setup basics — loading CSVs, the interactive viewer, shape, head/tail/sample, column
    names, and `info()`
    7–10: Descriptive stats — `describe()`, histograms, the dropdown widget, and box plots
    11–13: Indexing — `iloc` row/column selection, column access by name, and Python slicing
    14–15: Data cleaning — `drop()` for rows/columns, and identifying/quantifying missing values
    16–17: Transformation — `apply()` with custom functions, and `agg()` for aggregation
    18–19: Grouping — `groupby()` with aggregations, and the `count`/`nunique`/`size` distinctions
    20–21: Advanced Pandas — lambda functions inline with `apply()`, and `style.format()` with
    color highlights
    22–23: Applied analysis — subsetting with `iloc` for a focused question, and grouped `.mean()`
    for comparison

    The full detailed response is contained in the attached markdown file:
    pandas_techniques_reference.md
    """)
    return


if __name__ == "__main__":
    app.run()
