import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import marimo as mo

    return mo, pd


@app.cell
def _(mo):
    mo.md(r"""
    # Week 1 Assignment: Defining and Investigating Analytical Questions
    ## Eddie Flores
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Reading in our dataset.** The dataset is comprised of 3 separate files: movies.dat, ratings.dat, users.dat.
    """)
    return


@app.cell
def _(mo, pd):
    m_cols = ['movie_id', 'title', 'genres']
    movies_df = pd.read_csv('assign_wk1/movies.dat', sep=';', names=m_cols, encoding='latin1')
    mo.ui.data_explorer(movies_df)
    return (movies_df,)


@app.cell
def _(pd):
    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings_df = pd.read_csv('assign_wk1/ratings.dat', sep=';', names=r_cols)
    ratings_df.head(10)
    return (ratings_df,)


@app.cell
def _(pd):
    u_cols = ['user_id','sex', 'age', 'occupation', 'zip_code']
    users_df = pd.read_csv('assign_wk1/users.dat', sep=';', names=u_cols)
    users_df.head(10)
    return (users_df,)


@app.cell
def _(mo):
    mo.md(r"""
    **Merge the three files**
    """)
    return


@app.cell
def _(movies_df, pd, ratings_df, users_df):
    movie_ratings_df = pd.merge(movies_df, ratings_df)
    lens_df = pd.merge(movie_ratings_df, users_df)
    lens_df.head(20)
    return (lens_df,)


@app.cell
def _(lens_df):
    lens_df.to_csv('movie_lens_merged.csv', index=False)
    return


@app.cell
def _(lens_df):
    lens_df.info()
    return


@app.cell
def _(lens_df):
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
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # **Assignment**

    ## Section 1: info() and shape

    * **Describe what both of these functions are used for?**

        Both info() and shape are functions used to describe the data you are looking at.

    * **What information is returned from these functions?**

        info() is a function that shows you the column names, how many rows aren't empty, and the data types.

        shape is a property that just gives you the total number of rows and columns.

    * **Why is this information helpful?**

        info() is helpful because it tells you if you have missing data or if a column of numbers is being read as text by mistake.

        shape is helpful for a quick check to see if a file loaded correctly or if a merge changed the size of your table in a way you didn't expect.

        Basically, shape tells you how big the data is, while info() tells you exactly what is inside it.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Section 2: Using Marimo's interactive elements to answer the following questions
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Question 1: Which movie(s) have the highest and lowest average rating?

    We group by title and compute the mean rating for each movie. A minimum threshold
    of 50 ratings is applied to avoid obscure movies with only a handful of ratings
    skewing the results.
    """)
    return


@app.cell
def _(lens_df):
    # Group by title, calculate mean rating and total count of ratings
    avg_ratings_df = (
        lens_df.groupby('title')
        .agg(avg_rating=('rating', 'mean'), num_ratings=('rating', 'count'))
        .round(2)
        .reset_index()
    )

    # Filter out movies with fewer than 50 ratings to ensure statistical relevance
    avg_ratings_df = avg_ratings_df[avg_ratings_df['num_ratings'] >= 50]
    return (avg_ratings_df,)


@app.cell
def _(avg_ratings_df, mo):
    # Sort descending to find the highest rated movies, display top 10
    highest_rated = avg_ratings_df.sort_values('avg_rating', ascending=False).head(10)
    table1 = mo.ui.table(highest_rated)
    return (table1,)


@app.cell
def _(table1):
    table1
    return


@app.cell
def _(avg_ratings_df, mo):
    # Sort ascending to find the lowest rated movies, display bottom 10
    lowest_rated = avg_ratings_df.sort_values('avg_rating', ascending=True).head(10)
    table2 = mo.ui.table(lowest_rated)
    return (table2,)


@app.cell
def _(table2):
    table2
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Question 2: Which movie(s) have the most ratings in the dataset?

    A high rating count tells us which movies were most actively reviewed — a measure
    of popularity independent of how good the movie actually was.
    """)
    return


@app.cell
def _(lens_df, mo):
    # Group by title, count total ratings per movie, return top 10
    most_rated_df = (
        lens_df.groupby('title')
        .agg(num_ratings=('rating', 'count'))
        .reset_index()
        .sort_values('num_ratings', ascending=False)
        .head(10)
    )
    table3 = mo.ui.table(most_rated_df)
    return (table3,)


@app.cell
def _(table3):
    table3
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Question 3: Which 10 users have rated the most movies?

    Identifying the most active users can be useful for understanding engagement patterns.
    Power users who rate many movies may also have an outsized influence on average ratings.
    """)
    return


@app.cell
def _(lens_df, mo):
    # Group by user_id, count total ratings per user, return top 10
    most_active_users = (
        lens_df.groupby('user_id')
        .agg(num_ratings=('rating', 'count'))
        .reset_index()
        .sort_values('num_ratings', ascending=False)
        .head(10)
    )
    table4 = mo.ui.table(most_active_users)
    return (table4,)


@app.cell
def _(table4):
    table4
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Section 3: Five Analytical Questions

    Below I define and investigate 5 analytical questions about the MovieLens dataset.
    Each question is scoped to a specific aspect of the data and demonstrates a variety
    of pandas functions and visualization techniques.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Question 1: What is the distribution of ratings across the entire dataset?

    **Scope:** We want to understand how users tend to rate movies overall. Are most ratings
    clustered around 3-4 stars, or is the distribution more spread out? We will use a
    histogram to visualize the distribution of all ratings.
    """)
    return


@app.cell
def _(lens_df):
    # describe() gives us a statistical summary of the rating column
    lens_df['rating'].describe()
    return


@app.cell
def _(lens_df):
    import plotly.express as px

    # Histogram of all ratings across the dataset
    fig1 = px.histogram(
        lens_df,
        x='rating',
        nbins=9,
        title='Distribution of Movie Ratings',
        labels={'rating': 'Rating', 'count': 'Number of Ratings'},
        color_discrete_sequence=['steelblue']
    )
    fig1.update_layout(bargap=0.1)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Question 2: Do male and female users rate movies differently?

    **Scope:** We want to compare the rating behavior between male and female users.
    We will use a boxplot to compare the spread and median of ratings by gender,
    and groupby() with agg() to get summary statistics for each group.
    """)
    return


@app.cell
def _(lens_df):
    # groupby gender and aggregate rating stats
    gender_stats = (
        lens_df.groupby('sex')
        .agg(
            avg_rating=('rating', 'mean'),
            median_rating=('rating', 'median'),
            num_ratings=('rating', 'count')
        )
        .round(2)
        .reset_index()
    )
    gender_stats
    return


@app.cell
def _(lens_df):
    import plotly.express as px_2

    # Sample 10,000 rows to avoid rendering issues
    sample_df = lens_df.sample(n=10000, random_state=42)

    fig2 = px_2.box(
        sample_df,
        x='sex',
        y='rating',
        title='Rating Distribution by Gender',
        labels={'sex': 'Gender', 'rating': 'Rating'},
        color='sex',
        color_discrete_map={'M': 'steelblue', 'F': 'salmon'}
    )
    return (fig2,)


@app.cell
def _(fig2):
    fig2
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Question 3: Which genres receive the highest average ratings?

    **Scope:** Movies in this dataset can belong to multiple genres, stored as a pipe-separated
    string (e.g. "Action|Comedy"). We will use apply() and lambda() to extract the first
    listed genre for each movie, then group by that genre to compare average ratings.
    We will also drop the full genres column after extracting what we need, demonstrating
    dataframe column removal.
    """)
    return


@app.cell
def _(lens_df):
    # Copy only the columns we need for this analysis
    genre_df = lens_df[['title', 'genres', 'rating']].copy()

    # Use apply() and lambda() to extract the first genre from the pipe-separated string
    genre_df['primary_genre'] = genre_df['genres'].apply(lambda g: str(g).split('|')[0])

    # Drop the original genres column since we now have primary_genre
    genre_df = genre_df.drop(columns=['genres'])

    genre_df.head()
    return (genre_df,)


@app.cell
def _(genre_df):
    # Group by primary genre and calculate average rating and count
    genre_stats = (
        genre_df.groupby('primary_genre')
        .agg(
            avg_rating=('rating', 'mean'),
            num_ratings=('rating', 'count')
        )
        .round(2)
        .reset_index()
        .sort_values('avg_rating', ascending=False)
    )
    genre_stats
    return (genre_stats,)


@app.cell
def _(genre_stats):
    import plotly.express as px_3

    # Bar chart of average rating by primary genre
    fig3 = px_3.bar(
        genre_stats,
        x='primary_genre',
        y='avg_rating',
        title='Average Rating by Primary Genre',
        labels={'primary_genre': 'Genre', 'avg_rating': 'Average Rating'},
        color='avg_rating',
        color_continuous_scale='Blues'
    )
    fig3.update_layout(xaxis_tickangle=-45)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Question 4: Does a user's age group affect how they rate movies?

    **Scope:** The dataset encodes age as a numeric code (1, 18, 25, 35, 45, 50, 56).
    We will use apply() and lambda() to map these codes to readable age group labels,
    then use groupby() and agg() to compare average ratings across age groups.
    A boxplot will show whether older or younger users tend to rate differently.
    """)
    return


@app.cell
def _(lens_df):
    # Map numeric age codes to readable labels using apply() and lambda()
    age_map = {1: 'Under 18', 18: '18-24', 25: '25-34',
               35: '35-44', 45: '45-49', 50: '50-55', 56: '56+'}

    age_df = lens_df[['age', 'rating']].copy()
    age_df['age_group'] = age_df['age'].apply(lambda x: age_map.get(x, 'Unknown'))

    # Show shape to confirm no rows were lost
    print(age_df.shape)

    age_df.head()
    return (age_df,)


@app.cell
def _(age_df):
    # Aggregate average rating and count per age group
    age_stats = (
        age_df.groupby('age_group')
        .agg(
            avg_rating=('rating', 'mean'),
            num_ratings=('rating', 'count')
        )
        .round(2)
        .reset_index()
        .sort_values('avg_rating', ascending=False)
    )
    age_stats
    return


@app.cell
def _(age_df):
    import plotly.express as px_4

    # Sample 10,000 rows to avoid rendering issues
    age_df_sample = age_df.sample(n=10000, random_state=42)

    fig4 = px_4.box(
        age_df_sample,
        x='age_group',
        y='rating',
        title='Rating Distribution by Age Group',
        labels={'age_group': 'Age Group', 'rating': 'Rating'},
        color='age_group'
    )
    return (fig4,)


@app.cell
def _(fig4):
    fig4
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Question 5: Which movies are most polarizing (highest rating variance)?

    **Scope:** A movie with a high average rating is not necessarily universally loved.
    Some movies split audiences — some viewers love them while others hate them. We can
    identify these polarizing movies by looking at the variance of ratings. We will filter
    to movies with at least 100 ratings, then use agg() to compute variance, and apply
    conditional formatting to highlight the most and least polarizing films.
    """)
    return


@app.cell
def _(lens_df):
    # Group by title, compute mean, variance and count of ratings
    polarizing_df = (
        lens_df.groupby('title')
        .agg(
            avg_rating=('rating', 'mean'),
            rating_variance=('rating', 'var'),
            num_ratings=('rating', 'count')
        )
        .round(3)
        .reset_index()
    )

    # Filter to movies with at least 100 ratings for statistical reliability
    polarizing_df = polarizing_df[polarizing_df['num_ratings'] >= 100]

    # Sort by variance descending to find the most polarizing movies
    polarizing_df = polarizing_df.sort_values('rating_variance', ascending=False)

    # Show info() to confirm structure before formatting
    polarizing_df.info()
    return (polarizing_df,)


@app.cell
def _(polarizing_df):
    import jinja2

    # Top 15 most polarizing movies with conditional formatting
    top_polarizing = polarizing_df.head(15)

    (top_polarizing
     .style.format({
         'avg_rating': '{:.2f}',
         'rating_variance': '{:.3f}',
         'num_ratings': '{:,}'
     })
     .highlight_max(subset=['rating_variance'], color='salmon')
     .highlight_min(subset=['rating_variance'], color='lightgreen')
     .set_caption("Top 15 Most Polarizing Movies (min. 100 ratings)"))
    return


if __name__ == "__main__":
    app.run()
