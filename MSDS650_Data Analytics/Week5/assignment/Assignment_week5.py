import marimo

__generated_with = "0.22.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 5 Lab: Supervised Learning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:10px;" src="figures_wk5/knn.png" width=400><br>
    This week's assignment will focus constructing and improving the performance of a KNN model and trying out other models to see if model performance could be improved.


    ## Dataset:
    **Dataset:** bank-additional-full.csv (Provided in folder assign_wk5)
    ## Assignment Requirements

    After reviewing the dataset's descriptive file (bank-additional-names.txt), define a research question to guide your analysis. Make sure your KNN Analysis addresses the following tasks at a minimum:
       - Cleanup the dataset as you deem appropriate. As always, defend your reasoning!!!
           - Missing values?
           - Column names
       - Prepare the data for machine learning
           - A little EDA goeas a long way
           - Do you need to do anything about data types?
       - KNN Analysis
           - What is your optimal K?
           - Evaluate the accuracy of your model
           - Discuss ways to improve the performance of your KNN model as discussed in the lecture materials.
               * Notice the requirement states **ways** - meaning more than one!
               * Defend and backup your thoughts!
               * Show marimo elements
       - KNN Model Improvement
           - Implement one of those methods to improve your KNN model performance.
           - Did your second model perform better than the first?
       -   Other models?
       - Conclusion/Summary
           - Compare and contrast your results
           - Include numbers/graphs corresponding to your conclusions
           - Defend and backup your thoughts!!!!!!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Deliverables:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Upload your .py file and any other files needed for analysis to the corresponding location in WorldClass.

    **Note::** Make sure you have clearly indicated each assignment requirement within your notebook.

    **Important:** Make sure you have clearly indicated each assignment requirement within your notebook. Also, I highly encourage you to use markdown text to create a notebook that integrates your analysis within your code. The narrative within your notebook will count for 50% of your total grade on this assignment.
    """)
    return


if __name__ == "__main__":
    app.run()
