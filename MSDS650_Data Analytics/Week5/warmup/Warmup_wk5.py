import marimo

__generated_with = "0.22.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:10px;" src="logo.png" width=300><br>
    ## Warmup Exercise for Week 5


    For this week's warmup exercise we will be investigating the wages at a ficticous company (Spark Fortress, Inc.) to determine if there is a gap in the pay between various segments of the employees.

    **Dataset:** wage_gap.csv (provided)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise

    **Part 1:** <br>
    Pretend you have been engaged as an data analyst for Spark Fortress, Inc., and you have been asked by the chief executive officer (CEO) to analyze the fairness of the firm’s salaries with regard to the following demographics. <br>
       - Ethnicity (white vs non-white)
       - Genders across the various ethnicities
       - Managers across the various departments

    For each of those categories, do the following:<br>
       1. Defined a null and alternative hypothesis (Ho and Ha) for the dataset
          - Be specific and clear in your definitions
       2. Hypothesis testing
          - Explain why you chose the test(s) you are using
          - Summarize your findings from the test(s) you performed
       3. Summarize your findings based on your analysis.

    **Part 2:** <br>
    The CEO does not have a background in statistics, so you will need to explain, in general layman’s terms, your findings and provide enough information to support your findings. This is the only part that you will cover in your readout to the class. Make sure you cover all the points outlined in part 1.
    """)
    return


if __name__ == "__main__":
    app.run()
