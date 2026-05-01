# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.1",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.4",
#     "pandas>=3.0.2",
#     "seaborn>=0.13.2",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Warmup Exercise for Week 7
    <img align="right" style="padding-right:50px;" src="penguins.png" width=300><br>

    For this week's warmup exercise we will practice clustering a labeled dataset and compare the results to the known labels.

    **Dataset:** Palmer Penguins via SNS datasets
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise

    For this exercise, complete the following:
    1) Handle the missing values. From prior lectures, we know that there are 2 "blank" rows and then a handful of penguins without and sex value. Clean these observations up and defend your treatment of the data.
    2) Create a copy of your dataset and drop the island feature.
    3) Utilize a Kmeans alogrithm to cluster the dataset without the Species feature
    4) Appended the cluster assignments to the dataset
    5) Compare the cluster assignemnts to the Species and note any insight you have about your resutls.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
 

    return (sns,)


@app.cell
def _(sns):
    penguins = sns.load_dataset('penguins')
    return


if __name__ == "__main__":
    app.run()
