# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "altair>=6.0.0",
#     "ipython>=9.12.0",
#     "marimo>=0.23.1",
#     "matplotlib>=3.10.8",
#     "pandas>=3.0.2",
#     "plotly>=6.7.0",
#     "requests>=2.33.1",
#     "seaborn>=0.13.2",
#     "pyarrow>=11.0.0",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 7: Data Visualizations to Communicate Results
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:10px;" src="figures_wk8/textbook_cover.png" width=100><br>
    **Book Suggestion**: <br>

    Storytelling with Data - Let's Practice by Cole Nussbaumer Knaflic <br>
    >ISBN-13: 978-1119621492 <br>
    ISBN-10: 1119621492 <br>

    **Lecture Outline:**
    * What is Data Visualization
    * Importance of Context
    * Telling a Data Story
    * Design Thinking
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What is Data Visualization?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.

    In the world of data science, data visualization tools and technologies are essential to analyze massive amounts of information and make data-driven decisions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Why is data visualization so important?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our eyes are drawn to colors and patterns. We can quickly identify red from blue, square from circle. Our culture is visual, including everything from art and advertisements to TV and movies.

    Data visualization is another form of visual art that grabs our interest and keeps our eyes on the message. When we see a chart, we quickly see trends and outliers. If we can see something, we internalize it quickly. It’s storytelling with a purpose. If you’ve ever stared at a massive spreadsheet of data and couldn’t see a trend, you know how much more effective a visualization can be.

    <img align="center" style="padding-right:10px;" src="figures_wk8/viz_benefits.png" width=800><br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before we get to producing our own visualizations, let's stop and learn more about what goes into a visualization.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Importance of Context
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This may sound counterintuitive, but success in data visualizations does not start with the visualization itself, rather it starts with an understanding of the context that you wish to convey and how you want to convey it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Difference between Exploratory and Explanatory Visualizations
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:10px;" src="figures_wk8/exploratory_explanatory.png" width=150><br>
    Small detour in our conversation before diving into the deep end, we need to understand that there are two types of communication in visuals.
    - **Exploratory:** this type is done to understand the data and figure out what might be worth investigating and highlight to others.
    - **Explanatory:** this type is done when you have a specific story you want to tell to others.

    For this class, we will focus on the **Explanatory** visual communication.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Context - Who, What, How
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When it comes to explanatory visualizations, there are a few things to think and and understand **before** creating any visuals. This is a case where a little planning goes a long way.
    - **Who** are you communicating to?
    - **What** do you want to communicate?
    - **How** can you use data to help make your point?

    It is also important to guide your work by a question to be answered.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's take a look at this visual. By looking at it, can you tell the who, what and how?

    Question being addressed: The creators of this visualization were trying to show the gender disparity in pop culture by breaking down the scripts for 2000 of the biggest movies in cinema history. Each movie tallies up spoken lines of dialogue for male and female characters. For more information on this visualizaion, see here: https://pudding.cool/2017/03/film-dialogue/ and data for the analysis here : https://github.com/matthewfdaniels/scripts/<br>

    <img align="center" style="padding-right:10px;" src="figures_wk8/disney_who_what_how.png" width=1000><br>
    The original visualization created by Hanah Anderson and Matt Daniels. <br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What information is being conveyed in the above example?**<br>

    There are 4 sub-visualizations within the overall visualization <br>
     - a breakdown of Disney movies specifically  <br>
     - an overview of 2000 scripts <br>
     - a simple gradient bar that allows the user to search for movies and explore a few key filters <br>
     - a brief look into the age biases shown towards male and female roles  <br>
    """)
    return


@app.cell
def _():
    import pandas as pd

    #data viz
    import seaborn as sns
    import altair as alt
    import plotly.express as px
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors

    return alt, pd


@app.cell
def _(pd):
    #read the data
    import encodings
    movies=pd.read_csv('scripts-graphs/meta_data7.csv',encoding='latin-1')
    char_list= pd.read_csv('scripts-graphs/character_list5.csv',encoding='latin-1')
    char_mapping=pd.read_csv('scripts-graphs/character_mapping.csv',encoding='latin-1')
    return char_list, char_mapping, movies


@app.cell
def _(mo, movies):
    mo.ui.tabs(
        {
            "movies": mo.lazy(mo.ui.table(movies.describe(include="all")))
        }
    )
    return


@app.cell
def _(movies):
    movies.head()
    return


@app.cell
def _(char_list, mo):
    #see a summary of all characters data with marimo
    mo.ui.tabs(
        {
            "char_list": mo.lazy(mo.ui.table(char_list.describe(include="all")))
        }
    )
    return


@app.cell
def _(char_list):
    char_list.head()
    return


@app.cell
def _(char_mapping, mo):
    mo.ui.tabs(
        {
            "char_mapping": mo.lazy(mo.ui.table(char_mapping.describe(include="all")))
        }
    )
    return


@app.cell
def _():
    #look for studios for each movie using TMDB API
    import requests
    import time


    #API_KEY = '2d02e1fa9b875f74f1629bcec8da908d'  # <-- paste your TMDB key here

    #def get_studio(imdb_id):
        # Step 1: find the TMDB movie ID from the IMDB ID
    #    find_url = f'https://api.themoviedb.org/3/find/{imdb_id}?api_key={API_KEY}&external_source=imdb_id'
    #    try:
    #        r = requests.get(find_url, timeout=5)
    #        results = r.json().get('movie_results', [])
    #        if not results:
    #            return ''
    #        tmdb_id = results[0]['id']
    # 
            # Step 2: get full movie details including production companies
    #        detail_url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}'
    #        r2 = requests.get(detail_url, timeout=5)
    #        companies = r2.json().get('production_companies', [])
    #        return ', '.join(c['name'] for c in companies)

    #    except Exception as e:
    #        print(f"  Error for {imdb_id}: {e}")
    #        return ''

    #studios = []
    #for i, row in movies.iterrows():
    #    studio = get_studio(row['imdb_id'])
    #    studios.append(studio)
    #    print(f"[{i+1}/{len(movies)}] {row['title']} → {studio}")
    #    time.sleep(0.1)
    return


@app.cell
def _():
    #save to csv
    #movies['studio'] = studios
    #movies.to_csv('movies_with_studios.csv', index=False)
    return


@app.cell
def _(pd):
    movies_studio=pd.read_csv('movies_with_studios.csv', encoding='latin-1')
    movies_studio.head()
    return (movies_studio,)


@app.cell
def _(char_list, movies_studio):
    #Merge to get year and gross info

    df = char_list.merge(movies_studio, on='script_id', how='left')  # check exact column name
    #show gender column
    print(df['gender'].value_counts())

    #drop "?" from gender column
    df = df[df['gender'] != '?']
    return (df,)


@app.cell
def _(df):
    #check gender counts again
    print(df['gender'].value_counts())
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df, pd):
    #convert lines_data to numeric, coerce errors to NaN
    df['lines_data'] = pd.to_numeric(df['lines_data'], errors='coerce')
    return


@app.cell
def _(df):
    #print the top 10 studios and their counts
    print(df['studio'].value_counts().head(10))
    #print the least common studios and their counts
    print(df['studio'].value_counts().tail(10))
    return


@app.cell
def _(df):
    #create df with only  Pixar, Walt Disney Animation and Walt Disney Pictures
    studios_of_interest = [ 'Pixar', 'Walt Disney Animation Studios', 'Walt Disney Pictures', 'Walt Disney Feature Animation', 'Walt Disney Productions', 'Walt Disney Pictures']
    df_studios = df[df['studio'].isin(studios_of_interest)]
    print(df_studios['studio'].value_counts())
    return (df_studios,)


@app.cell
def _(df_studios):
    df_studios.info()
    return


@app.cell
def _(df_studios):
    #find top 16 movies by word count
    top_16 = df_studios.groupby('title')['words'].sum().reset_index(name='words').sort_values(by='words', ascending=False).head(16)
    top_16

    return


@app.cell
def _(df_studios):
    # sum words by title+gender
    title_gender = df_studios.groupby(['title', 'gender'])['words'].sum().reset_index()

    # get top 30 titles by total words
    title_total = title_gender.groupby('title')['words'].sum().reset_index()
    top_titles = title_total.nlargest(30, 'words')['title']

    # filter to top 30
    top_30 = title_gender[title_gender['title'].isin(top_titles)].copy()

    # calculate percentage per gender WITHIN each title
    top_30['total_words'] = top_30.groupby('title')['words'].transform('sum')
    top_30['percentage'] = (top_30['words'] / top_30['total_words'] * 100).round(1)

    print(top_30.head(6))  # sanity check — each title should have 2 rows summing to 100%

    return (top_30,)


@app.cell
def _(alt, mo, top_30):
    #create a bar chart of the top 16 movies by word count expressed as a percentage, shaded by gender
    male_order=(top_30[top_30['gender'] == 'm']
                  .sort_values('percentage', ascending=False)['title']
                  .tolist())

    final_plot = mo.ui.altair_chart(
    alt.Chart(top_30).mark_bar().encode(
        x=alt.X('percentage:Q', title='Percent'),
        #sort by percentage instead of word count 
        y=alt.Y('title:N', title='Movie Title', sort=male_order),
        color=alt.Color('gender:N', title='Gender',
                        scale=alt.Scale(
                        domain=['m', 'f'],
                        range=['#3266ad', '#c9a0b5']
                        ))
    ).properties(
        title='Top 16 Disney Movies by Word Count (Percentage), distinguished by Gender',
        width=500,
        height=400)

    )
    final_plot
    return (final_plot,)


@app.cell
def _(final_plot):
    # in a new cell — reactively updates when you click bars
    final_plot.value
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Who - Considering your Audience
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:10px;" src="figures_wk8/who.png" width=100>

    The more specific you can be about your audience the better.  Here are some things to consider:
    - Identify exactly who your audience is. - Be specific.
    - What do they care about?
    - What will resonate with them? - Design your visuals to meet this.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### What - Craft Your Message with the Audience in Mind
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:10px;" src="figures_wk8/what.png" width=250>

    This is the point where you think through how to make what you communicate relevant to your audience and clearly communicate why they should care about what you are saying to them.
     - Do you have a concise message? If not, it's time to rethink things.
     - What tone do you want to create with your message? (Urgent call to action, informative, etc.)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### How - Planning the Content
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:10px;" src="figures_wk8/how.png" width=200>

    At this point we are ready to plan out the content of our visual.
    - What data is available to help make my point?
    - What is the best format to deliver your message? (Brochure, descriptive document, live-presentation, etc.)
    - **What is the "story" I wish to tell?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Telling A Data Story
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:10px;" src="figures_wk8/data_story_telling.png" width=300>

    When you see a great play, watch a captivating movie, or read a fantastic book, you’ve experienced the magic of story. A good story grabs your attention and takes you on a journey, evoking an emotional response. In the middle of it, you find yourself not wanting to turn away or put it down. After finishing it—a day, a week, or even a month later—you could easily describe it to a friend.

    Wouldn’t it be great if we could ignite such energy and emotion in our audiences? Story is a time-tested structure; humans have been communicating with stories throughout history. We can leverage this powerful tool for our business communications. Let’s look to the art forms of plays, movies, and books to understand what we can learn from master storytellers that will help us better tell our own stories with data.

    Over the past few years, data storytelling has taken off. This is not only because data and the role it plays in our lives is increasing. It’s also because storytelling is the way we as humans have always come to understand ourselves and the world we live in.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What is data storytelling?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Data storytelling is the best way to use data to create new knowledge and new decisions or actions. It is an integrative practice that incorporates knowledge and skills from several disciplines, including communication, analysis and design. It is practiced across many fields and is used to address a variety of challenges.

    Storytelling is something most marketers are somewhat familiar with. When we’re talking about data storytelling, we are talking about stories in which data is the center point. The story is meant to explain the data and why it matters. There’s all kinds of stories, and most of them visuals can help tell, but only some have this focus and intent.

    >Data storytelling couples data visualization with compelling narratives that help audiences better comprehend and take action based on data analysis. While effective data visualization helps people grasp and remember key take-aways, data storytelling is essential for helping them understand why those take-aways matter.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Why is data storytelling important?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Data is collected and shared to help us see patterns and have insights we wouldn’t otherwise.

    For example:<br>
    - You can look at your students’ grades to see how they are doing in school.
    - Your doctor can look at your blood work to make recommendations for your lifestyle.
    - Your company can look at changes in revenue to determine how well new business strategies are working.

    Data can help influence how people perceive a topic, especially if they value scientific methods. But with the power of data comes a lot of responsibility for the data storyteller.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:50px;" src="figures_wk8/percent_76.png" width=200>

    If I tell you the simple statement “76% is what matters” you will have no idea if that means 76% is the fraction of my day that I spend working, the percentage of my friends who watch my favorite TV show, or the amount of my diet that consists of ramen.

    Numbers and data need to be put into context for us to understand it. Stories are how we can help numbers make sense, not only to ourselves but to others.

    The best way to do this is through visuals because they allow us to quickly and easily grasp insights and they also help us remember those insights over time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:50px;" src="figures_wk8/percent_76_2.png" width=350>

    I’m willing to bet you remember that meme you saw on social media more than that business memo you read last week. Here too, visuals are powerful and require deliberate use to be effective.

    At the end of the day, we want to use data to help us make better decisions.

    Maybe you are working on a report that helps your team understand where most of your website traffic is coming from, or you want to create materials that will help your team remember important concepts or processes.

    Telling a story with data will help your team get from point A (where they currently are) to point B, which is where they will have the “aha” that will change everything.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What makes a great data story?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:50px;" src="figures_wk8/data_recipe.png" width=300>

    How can you tell a data story that that helps people make better decisions? Let’s consider what makes a data story effective.<br>

    **It needs to be relevant:**
    This means the content (including copy and visuals) needs to fit with the audience’s current level of knowledge and it needs to help them reach a goal of some kind.

    Maybe your audience is internal, like a presentation to leadership about the need to invest in a specific strategy or tactic. Or maybe they are external, such as a campaign to persuade customers to try your solution.

    Either way, think about what matters to them. The best stories speak to people, and the more specific the person, the better.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **It needs to include good data:**
    This means the data should be from a reputable source and/or collected in a way that truly represents what’s needed to tell a truthful story.

    Publicly available data from government entities, intergovernmental organizations, academic researchers, and established leaders in analysis are not only more accessible, they are also transparent and verifiable.

    But having a good data source alone isn’t the only thing to consider. For example, you wouldn’t use data about positive tests for COVID-19 in New York as your only source of data to talk about how COVID-19 is impacting the world, right?

    Since data is the center point, these stories are not about what you think your audience should hear, they are about sharing what the objective data says. This is markedly different from other stories we might tell. The data used should help you tell the honest truth. It should align with the audience’s needs and support them in learning exactly what they need to know to make a key decision.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **There needs to be a clear narrative:**
    When it comes to storytelling, we are all used to a traditional story arc with a beginning, middle, and end.

    For data stories, this usually means you need an introduction to the topic before you dive into the data. You also need to conclude with a specific call to action—this is another thing that makes a data story distinctly different from a straightforward report.

    Also, if your audience is not experts, it’s important to use plain language so you don’t lose them in wonky jargon or confusing acronyms.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **It should include intentional visuals:**
    What does intentional mean? It means whether you use photos, graphs, and/or charts, the visuals you use should help your audience easily understand what the data means.

    Above all, the visuals you include should be:<br>
    - Appropriate for the data
    - Well-labeled
    - Legible
    - Not misleading

    Great data stories pay attention to details like use of color and imagery, including considerations related to accessibility and diversity.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Caution: Watch out for elements that can distract from your story
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Things Might Not Appear As They Seem
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:10px;" src="figures_wk8/misleading_cereal.png" width=300>

    First and foremost, you should never set out to mislead your audience. You never know if there will be someone in your audience that actually knows more than you. The policy is to stick to the facts, that you can support, and be truthful at all times.

    That being said there are an awful lot of misleading visuals produced and you are surrounded by them on a daily basis.

    Take this visual for Kellogg's cereal Rice Krispies. The consumer is lead to believe that this cereal has been fortified with nutrients that will boost your child's immune system. The Federal Trade Commission investigated this claim and eventually ordered Kellogg to halt all advertising that the cereal improved a child's immunity stating the the claims were "dubious."
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Clutter is Your Enemy!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:20px;" src="figures_wk8/clutter.png" width=250><br>
    When you look at the graphic on the right, what do you see? The obvisious answer would be something along the lines of "a lot of stuff" or "a messy room".

    Can you tell me what all is in this picture? Given enough time, you could systematically zoom-in on each section of the picture and document everything you can see in that picture. But that would take  <b><i>A LOT </i></b> of time and effort.

    This principle is known as cognitive load, which is the amount of mental processing power that someone has to exert to discern the information being communicated.

    Now let's apply this same principle to visuals in a presentation. If the audience has to search through the various visualizations to find the meaning or message behind the graphic, is that an effective way to communicate with an audience? Probably not.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### What is Clutter?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:50px;" src="figures_wk8/question_mark.png" width=150>

    According to Dictionary.com, clutter is:
       * noun: a collection of things lying about in an untidy mass
       * verb: to crowd something untidily

    If we search for a definition about visual clutter, we find:
       * a disordered collection of graphical entities in in- formation visualization.

    Our book refers to clutter as **visual elements that take up space but don't increase understanding**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Lack of Visual Order
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When design is thoughtful, it fades into the background so that your audience doesn’t even notice it. When it’s not, however, your audience feels the burden.

    Take a moment to study the figure below, which summarizes survey feedback about factors considered by nonprofits in vendor selection. Note specifically any observations you may have regarding the arrangement of elements on the page.

    <img align="center" style="padding-right:50px;" src="figures_wk8/visual_order1.png" width=700>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you look over the information, you might be thinking, “this looks pretty good.” I’ll concede: it’s not horrible.

    On the positive side, the takeaway is clearly outlined, the graph is well ordered and labeled, and key observations are articulated and tied visually to where we’re meant to look in the graph.

    But when it comes to the overall design of the page and placement of elements, I’d have to disagree with any praise. To me, the aggregate visual feels disorganized and uncomfortable to look at, as if the various components were haphazardly put there without regard for the structure of the overall page. We can improve this visual markedly by making some relatively minor changes.

    <img align="center" style="padding-right:50px;" src="figures_wk8/visual_order2.png" width=600>

    Compared to the original visual, the second iteration feels somehow easier. There is order. It is evident that conscious thought was paid to the overarching design and arrangement of components. Specifically, the latter version has been designed with greater attention to alignment and white space. Let’s look at each of these in detail.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Lack of White Space
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    White space in visual communication is as important as pauses in public speaking. Perhaps you have sat through a presentation that lacked pauses. It feels something like this:
    >There is a speaker up in front of you and possibly due to nerves or perhaps because they’re trying to get through more material than they should in the allotted time they are speaking a mile a minute and you’re wondering how they’re even able to breathe you’d like to ask a question but the speaker has already moved on to the next topic and still hasn’t paused long enough for you to be able to raise your question.

    This is an uncomfortable experience for the audience, similar to the discomfort you may have felt reading through the preceding run-on, unpunctuated sentence.

    That is the same powerful effect that white space used strategically can have on our visual communications. The lack of it—like the lack of pauses in a spoken presentation—is simply uncomfortable for our audience. Audience discomfort in response to the design of our visual communications is something we should aim to avoid. White space can be used strategically to draw attention to the parts of the page that are not white space.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Eliminate Distractions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    While we highlight the important pieces, we also want to eliminate distractions. In his book Airman’s Odyssey, Antoine de Saint-Exupery famously said, “You know you’ve achieved perfection, not when you have nothing more to add, but when you have nothing to take away” (Saint-Exupery, 1943). When it comes to the perfection of design with data visualization, the decision of what to cut or de-emphasize can be even more important than what to include or highlight.

    To identify distractions, think about both clutter and context. We’ve discussed clutter previously: these are elements that take up space but don’t add information to our visuals. Context is what needs to be present for your audience in order for what you want to communicate to make sense. When it comes to context, use the right amount—not too much, not too little. Consider broadly what information is critical and what is not. Identify unnecessary, extraneous, or irrelevant items or information. Determine whether there are things that might be distracting from your main message or point. All of these are candidates for elimination.

    Here are some specific considerations to help you identify potential distractions:<br>
    - **Not all data are equally important.** Use your space and audience’s attention wisely by getting rid of noncritical data or components.
    - **When detail isn’t needed, summarize.** You should be familiar with the detail, but that doesn’t mean your audience needs to be. Consider whether summarizing is appropriate.
    - **Ask yourself: would eliminating this change anything?** No? Take it out! Resist the temptation to keep things because they are cute or because you worked hard to create them; if they don’t support the message, they don’t serve the purpose of communication.
    - **Push necessary, but non-message-impacting items to the background.** Use your knowledge of preattentive attributes to de-emphasize. Light grey works well for this.

    Each step in reduction and de-emphasis causes what remains to stand out more. In cases where you are unsure whether you’ll need the detail that you’re considering cutting, think about whether there is a way to include it without diluting your main message. For example, in a slide presentation, you can push content to the appendix so it’s there if you need it but won’t distract from your main point.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Take a look at the following before and after visuals.  The underlying message is the same in both visuals. However, which one draws you in and focuses your attention? For me the one on the right does that.

    <img align="center" style="padding-left:10px;" src="figures_wk8/eliminate_distractions.png" width=700>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Text is Your Friend
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Thoughtful use of text helps ensure that your data visualization is accessible. Text plays a number of roles in communicating with data: use it to label, introduce, explain, reinforce, highlight, recommend, and tell a story.

    There are a few types of text that absolutely must be present. Assume that every chart needs a title and every axis needs a title (exceptions to this rule will be extremely rare). The absence of these titles—no matter how clear you think it may be from context—causes your audience to stop and question what they are looking at. Instead, label explicitly so they can use their brainpower to understand the information, rather than spend it trying to figure out how to read the visual.

    Don’t assume that two different people looking at the same data visualization will draw the same conclusion. If there is a conclusion you want your audience to reach, state it in words. Leverage preattentive attributes to make those important words stand out.

    When it comes to words in data visualization, it can sometimes be useful to annotate important or interesting points directly on a graph. You can use annotation to explain nuances in the data, highlight something to pay attention to, or describe relevant external factors.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When it comes to words in data visualization, it can sometimes be useful to annotate important or interesting points directly on a graph. You can use annotation to explain nuances in the data, highlight something to pay attention to, or describe relevant external factors. One of my favorite examples of annotation in data visualization is by David McCandless, “Peak Break-up Times According to Facebook Status Updates.”

    <img align="center" style="padding-left:10px;" src="figures_wk8/breakup_times.png" width=700>

    As we follow the annotations from left to right, we see a small increase on Valentine’s Day, then large peaks in the weeks of Spring Break (cleverly subtitled “Spring clean?”). There’s a spike on April Fool’s Day. The trend of break-ups on Mondays is highlighted. A gentle rise and fall in break-ups is observed over summer holiday. Then we see a massive increase leading up to the holidays, but a sharp drop-off at Christmas, because clearly breaking up with someone then would simply be “Too Cruel.”

    Note how a few choice words and phrases make this data so much more quickly accessible than it otherwise would be.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Don't Overcomplicate Things
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:10px;" src="figures_wk8/cursive.png" width=350>

    “If it’s hard to read, it’s hard to do.” This was the finding of research undertaken by Song and Schwarz at the University of Michigan in 2008. First, they presented two groups of students with instructions for an exercise regimen. Half the students received the instructions written in easy-to-read Arial font; the other half were given instructions in a cursive-like font called Brushstroke. Students were asked how long the exercise routine would take and how likely they were to try it. The finding: the fussier the font, the more difficult the students judged the routine and the less likely they were to undertake it. A second study using a sushi recipe had similar findings.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Translation for data visualization: the more complicated it looks, the more time your audience perceives it will take to understand and the less likely they are to spend time to understand it.

    As we’ve discussed, visual affordances can help in this area. Here are some additional tips to keep your visuals and communications from appearing overly complicated:
    - **Make it legible:** use a consistent, easy-to-read font (consider both typeface and size).
    - **Keep it clean:** make your data visualization approachable by leveraging visual affordances.
    - **Use straightforward language:** choose simple language over complex, choose fewer words over more words, define any specialized language with which your audience may not be familiar, and spell out acronyms (at minimum, the first time you use them or in a footnote).
     - **Remove unnecessary complexity:** when making a choice between simple and complicated, favor simple.

    This is not about oversimplifying, but rather not making things more complicated than they need to be. I once sat through a presentation given by a well-respected PhD. The guy was obviously smart. When he said his first five-syllable word, I found myself impressed with his vocabulary. But as his academic language continued, I started to lose patience. His explanations were unnecessarily complicated. His words were unnecessarily long. It took a lot of energy to pay attention. I found it hard to listen to what he was saying as my annoyance grew.

    Beyond annoying our audience by trying to sound smart, we run the risk of making our audience feel dumb. In either case, this is not a good user experience for our audience. Avoid this. If you find it hard to determine whether you are overcomplicating things, seek input or feedback from a friend or colleague.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Design Thinking
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:10px;" src="figures_wk8/dr_seuss.png" width=300>

    >“Think left and think right and think low and think high. Oh, the thinks you can think up if only you try” — Dr. Seuss

    Design thinking is a process used by designers for solving complex problems with creative solutions. It serves as a recipe for whipping up a batch of creativity whenever you are hungry for some fresh ideas. Designers use this process to streamline their ideas and create innovative solutions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Design Thinking Process
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Design thinking is a non-linear, iterative process that teams use to understand users, challenge assumptions, redefine problems and create innovative solutions to prototype and test. Involving five phases—Empathize, Define, Ideate, Prototype and Test—it is most useful to tackle problems that are ill-defined or unknown.

    <img align="center" style="padding-left:10px;" src="figures_wk8/design_thinking.png" width=600>

    - **Empathize:** the goal is to understand the problem you are solving. Embrace an empathetic mindset and immerse yourself in the process. Try to avoid looking at the problem externally. Gain a deep and personal understanding of the challenges and what it’s like to feel their effects.
    - **Define:** get a clear picture of the challenges from the end-user’s perspective, not the provider. Look for patterns and themes. Challenge the common ways of thinking and don’t assume anything.
    - **Ideate:** explore possibilities and let your creativity run wild. Exhaust your ideas. Allow yourself to think outside the box and push beyond the obvious solutions.
    - **Prototype:** create several simple versions of your solution. Allow people outside the process to test them and give you feedback. The idea is to fail fast and adjust until you get it right. This will help you flesh out ideas and see how they work in reality so you can make your solutions better.
    - **Test:** test a finished product made up of the results of Phase 4. You may discover new ideas that you couldn’t see before. These ideas can help train users or can be saved for a new release in the future.
    """)
    return


if __name__ == "__main__":
    app.run()
