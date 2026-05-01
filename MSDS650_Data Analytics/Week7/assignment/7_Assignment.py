import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 7 Assignment: Communicating Results
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:50px;" src="figures_wk8/puzzle_pieces.png" width=200>

    This week we will focus on Telling A Data Story and combining data analysis techniques to answer a single problem statement.

    **Dataset::** <br>
    This week you will be working with a dataset of your choice. Your dataset should include both categorical and continuous features. <br>
    Note: <u> You MAY NOT reuse any of the dataset demonstrated throughout this course or MSDS600</u>.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Assignment Requirements:** <br>
    For this week's assignment, you will use several techniques to analyze a single problem statement and then communicate the results as a data story.

    Your data story should be delivered as a PowerPoint(pptx) and include the following:
    * You will present on your data story in class in Week 8 (for in-person and students participating on Zoom) or voice over to tell your story (for students taking the course offline).
    * For voice-over: Voice-over - your audio must be clear enough for me to understand what you are saying and detailed enough to tell your story
    * Do NOT read to our audience!  Talk to them!

    - Your slide deck should consist of
        * Intro slide
        * 7-10 content slides
        * Future works slide
        * Reference slides as needed

    The analysis of your dataset should include:
    * Develop a scenario to provide an overall understanding of the organization represented by your dataset.
    * Define a problem statement that you will investigate within your analysis.
    * Describe your dataset and how it relates to your analysis.
    * If needed, prepare your dataset for analysis.
    * Utilize **three different techniques** to investigate your problem statement.
        * Make sure you address any prechecks or conditions associated with your techniques
        * Summarize the insights and/or results for each technique
    * Provide an overall conclusion based on your analysis.

    Presentation Tips:
    * No code in your presentation
    * Do not assume that your audience has the same degrees as you
    * Relay the significance of any findings
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Deliverables
    Upload your Data Story (pptx), your analysis (python file) and a copy of your dataset to the corresponding location in WorldClass.
    """)
    return


if __name__ == "__main__":
    app.run()
