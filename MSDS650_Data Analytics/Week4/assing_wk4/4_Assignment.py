# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.3",
#     "pandas>=3.0.1",
#     "pyodbc>=5.3.0",
#     "pyzmq>=27.1.0",
#     "scipy>=1.17.1",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    # Week 4 Assignment: Hypothesis Tesing
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:50px;" src="figures_wk4/hypothesis_testing.png" width=350><br>
    ## Assignment Requirements

    **Dataset Name::** SRC_2025_Group1.accdb (located in the assing_wk4 folder)<br>
    This data contains data on student test scores at elementary and intermediate levels.
    You'll find the READMe file in the folder for an explanation of the variables.

    **Assignment Requirements:** <br>
    As demonstrated in the <u>Demo: Analyzing with Hypothesis Testing</u> section of the lecture notebook, you will be providing an analysis for the Annual EM Math dataset. This is one of the tables in the SRC_2025_Group1 database.

    For you analysis you will need to:

    1) Extract the Annual EM Math table from the Microsoft Access Database.
    2) Clean the data so that it's ready for analysis.
    3) Develop a scenario to provide an overall understanding of the organization represented by the dataset.
        * Define a problem statement to investigate with either t-test or z-test.
        * Describe your dataset, including the columns that will support our analysis.
    4) Describe your test approach
        * Justify your selection of which test you will use.
        * Define a H0/H1 couplet to support your problem statement.
    5) Conduct your analysis according to your defined parameters above.
        * Include a descriptive analysis as appropriate
        * Prep your data for analysis
        * Conduct your hypothesis testing
    6) Based on the results from your analysis in step 3, redefined your H0/H1 couplet to dive deeper into the analysis and repeat steps 2 and 3.
    7) Provide a recap of the insights you have gained throughout your analysis.
    """)
    return


if __name__ == "__main__":
    app.run()
