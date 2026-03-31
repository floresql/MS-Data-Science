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

    return (mo,)


@app.cell
def _():
    import subprocess

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Warmup Exercise - Answering Questions with Pandas
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:10px;" src="warmup_figures_wk3/grocery.png" width=300><br>

    As follow-on from the prior weeks, this week's warmup exercise will involve developing your own investigative questions and answer them using the tools from the prior weeks.

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
    This exercise maybe worked on in groups or individually. This exercise will be be turned in and graded for your discussion grade.

    1) Define a couple of in-depth questions you would like to investigate within this dataset. Then demonstrate a subbset of the following functions through the analysis of your questions:

        * `groupby`
        * `value_counts`
        * `describe`
    """)
    return


@app.cell
def _():
    import pandas as pd

    return (pd,)


@app.cell
def _(pd):
    sales = pd.read_csv('supermarket_sales.csv')
    return (sales,)


@app.cell
def _(sales):
    sales.info()
    return


@app.cell
def _(sales):
    sales.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Which branch × product line drives the most revenue?
    Each branch stocks all six product lines, but do certain categories dominate at specific locations?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Revenue
    """)
    return


@app.cell
def _(sales):
    branch_product = (
        sales.groupby(["Branch", "Product line"])["Total"]
        .agg(Total_Revenue="sum", Avg_Transaction="mean", Num_Transactions="count")
        .round(2)
    )
    branch_product
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Branch Level
    """)
    return


@app.cell
def _(sales):
    branch_summary = (
        sales.groupby("Branch")[["Total", "gross income", "Rating"]]
        .agg({"Total": "sum", "gross income": "sum", "Rating": "mean"})
        .round(2)
    )
    branch_summary
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Numeric summary of key financial + rating columns
    """)
    return


@app.cell
def _(sales):
    sales[["Unit price", "Quantity", "Total", "gross income", "Rating"]].describe().round(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    How many transactions per product line?
    """)
    return


@app.cell
def _(sales):
    sales["Product line"].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Key Findings

    Branch C's Food & Beverages category led all 18 combinations with $23,767 total revenue and the highest average transaction at $360. Branch B's Health & Beauty had the highest per-transaction average ($377) despite fewer transactions.

    Using the describe() function we see a high standard deviation in Total ($246 on a $323 mean) signaling highly variable basket sizes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ### Do payment method and customer type influence spending?

    With three payment methods and two customer segments roughly evenly split, we can test whether being a Member or paying by Credit card meaningfully changes how much someone spends per transaction.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Distribution of payment methods and customer types
    """)
    return


@app.cell
def _(sales):
    sales["Payment"].value_counts()


    return


@app.cell
def _(sales):
    sales["Customer type"].value_counts()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Spending statistics by Payment × Customer Type
    """)
    return


@app.cell
def _(sales):
    pay_cust = (
        sales.groupby(["Payment", "Customer type"])["Total"]
        .describe()
        .round(2)[["count", "mean", "50%", "max"]]
    )
    pay_cust.columns = ["Transactions", "Avg Spend", "Median Spend", "Max Spend"]
    pay_cust
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Key Findings

    Credit card Members have the highest average spend ($335.88), but differences across all six segments are small, only a $26 spread between the highest and lowest group average. Normal credit card users have a notably low median ($202.82 vs $275 for Members), suggesting they cluster around smaller purchases.

    USing value_counts() we see payment methods are nearly equally distributed (Ewallet 345, Cash 344, Credit card 311) and customer types are almost perfectly split (501 Members vs 499 Normal). This balance means any spending differences are genuinely behavioral, not unequal group sizes.
    """)
    return


if __name__ == "__main__":
    app.run()
