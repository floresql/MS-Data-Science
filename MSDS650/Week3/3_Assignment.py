import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Assignment Requirements

    Complete an Exploratory data analysis for your chosen dataset. Your analysis should include the following. For each of the following sections, please provide a narritive of your approach, reasoning for your treatment of the data and insights or conclusions that you have reached.

    Define a few questions that you wish to discover about your dataset to guide your EDA effort.
       1. Describe the data within the dataset.
           - Data types: Categorical vs Continuous variables
           - Statistical summary, etc.
       2. Data Cleaning
           - Identify and handle missing values
           - Identify and handle outliers
       3. Feature Selection
           - Graphical visualization of features
           - Examine the relationships within the dataset - using 2 different methods
           - Reduction of the dimensionality of the dataset
       4. Insights and Findings
           - Describe an insights and/or findings from within the datset.
       5. Bonus: Feature Engineering
           - Create a new feature based for findings.

    **Important:** Make sure your provide complete and thorough explanations for all of your analysis steps. You need to defend your thought processes and reasoning.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Deliverables:
    Upload your .py file and any other files necessary for me to be able to rerun your analysis to the corresponding location in WorldClass. Also, you will need to provide a copy of your dataset.

    **Note::** Make sure you have clearly indicated each assignment requirement within your notebook.
    """)
    return


if __name__ == "__main__":
    app.run()
