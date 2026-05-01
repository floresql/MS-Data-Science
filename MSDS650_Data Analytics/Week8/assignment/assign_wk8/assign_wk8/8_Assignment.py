import marimo

__generated_with = "0.23.3"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 8 Assignment: Text Analytics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This week's assignment will focus on text analysis of BBC News articles.

    ## Our Dataset:
    **Dataset:** bbc.csv(Provided in folder assign_wk8)<br>
    Consists of 2225 documents from the BBC news website corresponding to stories in five topical areas from 2004-2005. <br>
    Class Labels: 5 (business, entertainment, politics, sport, tech)

    ## Text Analytics Assignment:

    **Objective:**
    To demostrate all of the text analysis techniques covered int his week's lecture material. Your submission needs to include the following:
       - Preparation of the text data for analysis
           * Things to consider: stopwords, punctuation, digits, mixed case words
       - Identify the 10 most frequently used words in the text
           * How about the ten least frequently used words?
           * How does lemmatization change the most/least frequent words?
               - Explain and demonstrate this topic
       - Generate a world cloud for the text
       - Demonstrate the generation of n-grams and part of speech tagging
       - Create a Topic model of the text
           * Find the optimal number of topics
           * test the accuracy of your model
           * Display your results 2 different ways.
               1) Print the topics and explain any insights at this point.
               2) Graph the topics and explain any insights at this point.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Deliverables:

    Upload your notebook's .py file and any other files needed for analysis including an embedded visualization of the topic model this week.

    **Important:** Make sure your provide complete and thorough explanations for all of your analysis. You need to defend your thought processes and reasoning.
    """)
    return


if __name__ == "__main__":
    app.run()
