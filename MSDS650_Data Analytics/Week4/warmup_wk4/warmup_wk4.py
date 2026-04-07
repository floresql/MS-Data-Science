import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    ## Warmup for Week 4 - EDA

    **Data Set:** heart_disease.data (provided)
    UCI Riverside Heart Disease dataset
    We will use the heart_disease.data file, which has 14 attributes and 1 target variable

    **Objective:**
    Complete an exploratory analysis of the heart_disease dataset. After defining a question to guide your analysis, complete the following:
       1. Describe the data within the dataset.
           - Data types: Categorical vs Continuous variables
           - Statistical summary, etc.
       2. Data Cleaning
           - For this exercise, you may not use machine learning to clean this dataset.
           - Identify and handle missing values (The heart-disease.names file state missing values are represented as a -9)
           - Identify and handle outliers
       3. Feature Selection
           - Graphical visualization of features
           - Examine and describe the relationships within the dataset
       4. Insights and Findings
           - Describe an insights and/or findings from within the dataset.

    **For the readout portion of this exercise, your team will only be presenting the following:**
    - Approach to cleaning the data.
    - Describe any relationships within the data
    - Any insights within your team has into the dataset.
    """)
    return


if __name__ == "__main__":
    app.run()
