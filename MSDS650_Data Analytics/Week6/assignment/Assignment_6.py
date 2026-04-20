# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.22.0",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.4",
#     "pandas>=3.0.2",
# ]
# ///

import marimo

__generated_with = "0.22.0"
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
    This week's assignment will focus completeing a K-Means analysis.

    ## Our Dataset:
    **Dataset:** Multiple data sets on attention metrics related to the U.S. from 2020-2025. Link to data and where you can learn more [here](https://github.com/lukeslp/us-attention-data?tab=readme-ov-file).

    ## Unsupervised Learning
    Decide on one or multiple datasets to analyze and perform a K-Means analysis.

    **Objective:**
       - Use K-Means for this analysis: State and defend all your assumptions about the dataset. Defend yourself!!!
           * Make sure you cleanup your data, including the readability of your dataset
           * EDA: Explore your data!
           * Categorical vs numeric columns in your dataset
           * Would normalizing your dataset help?
           * Decide on a category to cluster to see if there are some natural groupings
       - Use PCA to plot the clusters
       - Discover any insights from this analysis? (include numbers/graphs corresponding to your reasoning)
           * Summarize your findings.
           * What does the PCA plot tell you about your clustering?

           I am providing some starter code to get you going...
    """)
    return


@app.cell
def _():
    import json
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    import numpy as np
    from datetime import datetime
    import marimo as mo


    return json, mo, pd


@app.cell
def _(json):
    # Load all datasets
    with open('C:\\Users\\kpolson\\OneDrive - Regis University\\GitHub\\MSDS650\\week6\\us-attention-data-main\\trends_data.json') as f:
        trends = json.load(f)

    with open('C:\\Users\\kpolson\\OneDrive - Regis University\\GitHub\\MSDS650\\week6\\us-attention-data-main\\wikipedia_pageviews.json') as f:
        wikipedia_pageviews = json.load(f)

    with open('C:\\Users\\kpolson\\OneDrive - Regis University\\GitHub\\MSDS650\\week6\\us-attention-data-main\\wikipedia_trending.json') as f:
        wikipedia_trending = json.load(f)
    return trends, wikipedia_trending


@app.cell
def _(mo, pd, trends, wikipedia_trending):
    trends_df = pd.DataFrame(trends)
    wikipedia_trending_df = pd.DataFrame(wikipedia_trending)
    #wikipedia_pageviews_df = pd.DataFrame(wikipedia_pageviews)

    mo.ui.tabs(
        {
            "wikipedia_trending": mo.lazy(mo.ui.table(wikipedia_trending_df.describe()))
        }
    )
    return (wikipedia_trending_df,)


@app.cell
def _(wikipedia_trending_df):
    wikipedia_trending_df.info()
    return


@app.cell
def _(wikipedia_trending_df):
    wikipedia_trending_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
