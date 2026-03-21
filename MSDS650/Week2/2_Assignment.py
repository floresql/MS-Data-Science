import marimo

__generated_with = "0.20.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 2 Assignment: Deriving Insight via Descriptive Statistics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:50px;" src="figures_wk2/descriptive_stats.png" width=350>

    ## Assignment Requirements

    **Dataset Name:** wages.csv (located in the assing_wk2 folder)<br>
    This data contains demographic and wage information for a generic company.

    **Assignment Requirements:** <br>
    As demonstrated in the <u>Demo: Analyzing a Dataset Through Descriptive Statistics</u> section of the lecture notebook, you will be providing an analysis for the wages.csv dataset.

    For your analysis, you will need to:
    1) Inspect the wages.csv dataset (outside of your notebook) and provide a detailed description of the dataset.
        - Include the variable's name, description and data type for each variable in the dataset.
    2) Create a fictitious business that fits the wages.csv dataset.
    3) Develop a problem statement and 5 analytical questions to be investigated during your analysis.
        - For this exercise, you are limited to univariant analysis.
        - At least 3 of your analytical questions should require Segmented Univariant Analysis.
    4) Utilize descriptive statistics to analyze each of your analytical questions.
    5) Recap of all your insights.
    6) Summarize your findings for our fictitious business.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Deliverables
    Upload your Jupyter Notebook to the corresponding location in WorldClass.

    **Note::** Make sure you have <u>clearly indicated</u> each assignment requirement within your notebook. Also, I <i>highly encourage</i> you to use markdown text to create a notebook that integrates your analysis within your code.

    **Important:** This assignment focuses on the insights you can garner for your data. Therefore, the narrative within your notebook will count for 50% of your total grade on this assignment.
    """)
    return


if __name__ == "__main__":
    app.run()
