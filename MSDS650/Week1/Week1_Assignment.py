# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "pandas>=3.0.1",
#     "plotly>=6.6.0",
#     "pyzmq>=27.1.0",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 1 Lab: Defining and Investigating Analytical Questions

    As noted in our lecture notebook this week, the main purpose of data analytics is to answer questions about a dataset. This week you will practice developing questions about a dataset and then answer those questions using python's Pandas library.

    ##  Our Dataset
    **Dataset Name::** Movie Lens dataset
    GroupLens Research has collected and made available rating data sets from the MovieLens web site (https://movielens.org).
    The dataset is comprised of 3 separate files: movies.dat, ratings.dat, users.dat.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Reminder:** The first step in any type of data analysis is to <u>look</u> at your data.
    """)
    return


@app.cell
def _(mo):
    mo.ui.file_browser()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It appears that all 3 of our data files do not include a header row.  So we are going to need to define a header row for each of the 3 files. The accompanying README file denotes the fields for each of these files.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-info">
        <b>File Separator::</b> Did you notice that seperator in the file is not a comma?  We will need to account for that when we load each file into a Pandas dataframe. <br> <br>
    The README file has additional useful information that you might want to refer while working on this assignment.
    </div>
    """)
    return


@app.cell
def _(mo, pd):
    # movie.dat fields --> MovieID::Title::Genres

    m_cols = ['movie_id', 'title', 'genres']
    movies_df = pd.read_csv('assign_wk1/movies.dat', sep=';', names=m_cols, encoding='latin1')
    mo.ui.data_explorer(movies_df)
    return (movies_df,)


@app.cell
def _(pd):
    # ratings.dat fields --> UserID::MovieID::Rating::Timestamp
    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings_df = pd.read_csv('assign_wk1/ratings.dat', sep=';', names=r_cols)
    ratings_df.head(10)
    return (ratings_df,)


@app.cell
def _(pd):
    # users.dat fields --> UserID::Gender::Age::Occupation::Zip-code
    u_cols = ['user_id','sex', 'age', 'occupation', 'zip_code']
    users_df = pd.read_csv('assign_wk1/users.dat', sep=';', names=u_cols)
    users_df.head(10)
    return (users_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can merge the individal dataframes into a single dataframe.
    """)
    return


@app.cell
def _(movies_df, pd, ratings_df, users_df):
    # merge movies_df with ratings_df
    movie_ratings_df = pd.merge(movies_df, ratings_df)

    # now movies_ratings_df with users_df
    lens_df = pd.merge(movie_ratings_df, users_df)
    #lens_df.head(20)
    return (lens_df,)


@app.cell
def _(lens_df):
    lens_df.to_csv('movie_lens_merged.csv',index=False)
    return


@app.cell
def _(lens_df):
    lens_df.info()
    return


@app.cell
def _(lens_df):
    #convert data types to save space
    lens_df['movie_id'] = lens_df['movie_id'].astype('int32')
    lens_df['user_id'] = lens_df['user_id'].astype('int32')
    lens_df['rating'] = lens_df['rating'].astype('float32')
    lens_df['age'] = lens_df['age'].astype('int8')
    lens_df['occupation'] = lens_df['occupation'].astype('int8')
    lens_df['zip_code'] = lens_df['zip_code'].astype('category')
    lens_df['title'] = lens_df['title'].astype('category')
    lens_df['genres'] = lens_df['genres'].astype('category')
    lens_df['sex'] = lens_df['sex'].astype('category')
    lens_df.info()
    return


@app.cell
def _(lens_df):
    #take a random sample of 999,000 rows to work with
    lens_df_sample = lens_df.sample(n=999000)
    return (lens_df_sample,)


@app.cell
def _(lens_df_sample, mo):
    mo.ui.table(lens_df_sample)
    return


@app.cell
def _(lens_df):
    lens_df.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Assignment Requirements
    Here are the requirements for this week's assignment. Make sure you address all of the assignment steps in your submission.
    1) Above, I demostrated using a `info()` and `shape` functions with our lens_df data structure.
        * Describe what both of these functions are used for?
        * What information is returned from these functions?
        * Why is this information helpful?
    2) Using Marimo's interactive elements or functions demonstrated in `1_Defining_Analytical_Questions.py` answer the following questions:
        * Which movie(s) has the highest average rating?
            * What about the movie(s) with the lowest rating?
        * Which movie(s) has the most ratings in our dataset?
        * List the 10 users who have rated the most movies?
    3) Define at least 5 analytical questions you would like to investigate for this dataset. As demonstrated in the lecture materials, you can define the scope of your analysis for each of your questions. However, throughout the investigation of questions, make sure you demonstrate each of the following functions at least once:
        * Data Visualization: histrgrams, boxplots
        * Descriptive functions: info(), describe(), shape
        * Dataframe reshaping: removal of rows or columns
        * Functions:
             * apply()
             * lambda()
             * aggregration (.agg)
             * groupby()
        * Conditional formatting in a dataframe
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Deliverables
    Upload your Jupyter Notebook to the corresponding location in WorldClass.

    **Note::** Make sure you have clearly indicated each assignment requirement within your notebook. Also, I <u><i><b>highly encourage</b></i></u> you to use markdown text to create a notebook that integrates your analysis within your code. Refer to the GettingStarted notebook to understand the difference between markdown text and comments.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Additional functionality that might be useful
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The function unstack() and reset_index() might be helpful for your investigation. You can read more about these two functions on the Pandas doc pages.
    * unstack(): https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#
    * reset_index(): https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html

    In the code below, notice how unstack() and reset_index() reshape the output of the groupby() function.
    """)
    return


@app.cell
def _(lens_df):
    lens_df.groupby(['title']).agg({'rating':['count']})
    return


@app.cell
def _(lens_df):
    sum_df = lens_df.groupby('title').agg({'rating':'count'}).unstack()
    sum_df
    return


@app.cell
def _(lens_df):
    sum_df_1 = lens_df.groupby(['title']).agg({'rating': ['count']}).unstack().reset_index()
    sum_df_1
    return


@app.cell
def _(lens_df):
    avg = lens_df.groupby(['title']).agg ( {'rating' : 'mean'} ).round(2).sort_values(by=['rating'], ascending=False)
    avg
    return


if __name__ == "__main__":
    app.run()
