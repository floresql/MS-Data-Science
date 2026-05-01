# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "gensim>=4.4.0",
#     "ipython>=9.12.0",
#     "marimo>=0.23.3",
#     "matplotlib>=3.10.8",
#     "nltk>=3.9.4",
#     "numpy>=2.4.4",
#     "pandas>=3.0.2",
#     "pyldavis>=3.4.1",
#     "scikit-learn>=1.8.0",
#     "seaborn>=0.13.2",
#     "wordcloud>=1.9.6",
# ]
# ///

import marimo

__generated_with = "0.23.3"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Text Analytics
    <img align="right" style="padding-right:10px;" src="figures_wk8/text_mining.png" width=400>

    Text analytics is the process of uncovering insights, trends, and patterns out of written communication (known as text).

    ## Text Analysis vs Text Analytics - What's the difference?
    The terms text analysis, and text analytics are often used interchangeably. The goal for both is the same, analyzing unstructured text to obtain insights. However, there are slight difference between the terms.

    Text Analysis is about parsing text to create structured data from unstructured text. Text analytics aggregates these results and turns them into something that can be quantified and visualized through charts and reports. Text analysis and text analytics often work together to provide a complete understanding of all kinds of text, like emails, social media posts, surveys, customer support tickets, and more.

    For example, you can use text analysis tools to find out how people feel toward a brand on social media (sentiment analysis), or understand the main topics in product reviews (topic detection). Text analytics, on the other hand, leverages the results of text analysis to identify patterns, such as a spike in negative feedback, and provides you with actionable insights you can use to make improvements, like fixing a bug that’s frustrating your users.

    Reference:
    > Text Analytics Basics: A Beginner's Guide<br>
    > https://monkeylearn.com/blog/what-is-text-analytics/
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Other Related Terms

    ### Text Mining
    Text mining is the process of deriving high-quality information from text. Hmmm... Seems like I've heard a very similar definition to that recently. Depending on who you talk to, which article you read, etc., texting mining is either the same process as text analysis or text analytics.

    ### Natural Language Processing (NLP)?
    Natural Language Processing is the  categorizing, clustering and tagging text, summarizing data sets, creating taxonomies, and extracting information about things like word frequencies and relationships between data entities. Analytical models are then run to generate findings that can help drive business strategies and operational actions.

    References:
    > What is Text Mining, Text Analytics and Natural Language Processing?
    > https://www.linguamatics.com/what-text-mining-text-analytics-and-natural-language-processing

    > Top 10 Python Libraries for Natural Language Processing (2023_updated)
    > https://www.kdnuggets.com/2023/04/guide-top-natural-language-processing-libraries.html/"
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Text Analytics - 20 NewsGroups Dataset
    The 20 newsgroups dataset comprises around 18000 newsgroups posts on 20 topics.

    ### Libraries and Data
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    import warnings
    warnings.filterwarnings("ignore")

    # '%matplotlib inline' command supported automatically in marimo
    sns.set_theme()
    return pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-danger">
    <b>Important::</b> This dataset is a fairly large, and the following step could take several minutes to complete, the first time you download the dataset!
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Luckily, sklearn allows us to remove the headers and footers when loading the data and this in theory, saves time for us when loading the dataset.
    """)
    return


@app.cell
def _():
    import joblib
    from sklearn.datasets import fetch_20newsgroups

    # Download once, reuse from local cache

    news = fetch_20newsgroups(subset='train', remove=('headers', 'footers'))
    joblib.dump(news, 'news.pkl')

    news = joblib.load('news.pkl')
    return (news,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-info">
    <b>sklearn datasets::</b> The sklearn datasets are loaded into a sklearn.utils.Bunch data object. A `bunch` is a dictionary-like object that is customized for the specified dataset. <br>
    <br>
    Here are some of the keys that we will use for this dataset: <br>
        - data: returns the contents of the news post <br>
        - target: return an integer referencing the target value <br>
        - target_names: returns a list of all the targets within the dataset <br>
    <br>
    You can read more about on the sklearn website: https://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets

    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's take a look at the data for one of the posts.
    """)
    return


@app.cell
def _(news):
    print(news.data[3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Well, that helped things out quite a bit. Time to see what other information we have for these posts.
    """)
    return


@app.cell
def _(news):
    news.target[3]
    return


@app.cell
def _(news):
    news.target_names
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Move the data into a Pandas dataframe
    I'm going to move our dataset into a Pandas dataframe because I find them easier to work with.
    """)
    return


@app.cell
def _(news, pd):
    cols = ['raw_text']
    news_df = pd.DataFrame(news.data, columns=cols)
    news_df.head(10)
    return (news_df,)


@app.cell
def _(news, news_df, pd):
    news_df['target'] = pd.Series(news.target)
    news_df.head(10)
    return


@app.cell
def _(news, news_df):
    news_df['target_category'] = news_df.target.apply(lambda x: news.target_names[x])
    news_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-info">
    <b>Artform vs Exact Science::</b> There is more than one way to achieve the analysis shown in this lecture. I am demostrating a programming approach to manipulate the data to acheive the desired results. There are a number of packages that provide functions that make text analysis effortless and efficient.  However, I want to showcase another approach in this demo.<br>
    </div>

    ### Basic Text Analysis Metrics
    We can extract a number of basic metrics about our new posts at this point.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Word Count
    One of the most basic metrics we can extract is the number of words in each news post. The thought process behind this is type of metric is that negative posts generally contain a lesser amount of words than positive posts do.

    To do this, we simply use the split function in python:
    """)
    return


@app.cell
def _(news_df):
    news_df['word_cnt'] = news_df.raw_text.apply(lambda x: len(str(x).split(" ")))
    return


@app.cell
def _(news_df):
    news_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Character Count
    This metric is also based on the previous feature intuition. Here, we calculate the number of characters in each post.
    """)
    return


@app.cell
def _(news_df):
    news_df['char_cnt'] = news_df.raw_text.str.len()
    news_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Generally, while solving an NLP problem, the first thing we do is to remove the stopwords. But sometimes calculating the number of stopwords can also give us some extra information which we might have been losing before.

    Here, we have imported stopwords from NLTK, which is a basic NLP library in python.
    """)
    return


@app.cell
def _():
    # '%pip install nltk' command supported automatically in marimo
    import nltk
    nltk.download('stopwords')
    return (nltk,)


@app.cell
def _(news_df):
    from nltk.corpus import stopwords
    _stop = stopwords.words('english')
    news_df['stopwords'] = news_df.raw_text.apply(lambda x: len([x for x in x.split() if x in _stop]))
    return (stopwords,)


@app.cell
def _(news_df):
    news_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data Cleaning and Prep
    As we've seen in prior weeks, after loading our dataset we need to take the time to cleaning and prep the data for further analysis. I'm going to load the cleaned data into another column within the dataframe so that we can observe how the data changes as we progress.

    In working with textual data, the cleaning and prep processing generally involves:
    * converting to lowercase
    * removing punctuation
    * removing numbers
    * removing stopwords
    * word tokenization
    * data stemming or lemmization or both

    We will only be using lemmatization in this notebook. However, there are a number of tutorials that demonstrate the process of stemming online.

    <i>Note:: Depending on the type of textual data you are working with, there might be other areas you need to address.</i>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Convert Text to Lowercase
    The first data cleaning step we will do is transform our posts into lower case. This avoids having multiple copies of the same words. For example, ‘Analytics’ and ‘analytics’ will appear as two different words.
    """)
    return


@app.cell
def _(news_df):
    news_df['clean_text'] = news_df.raw_text.apply(lambda x: " ".join(x.lower() for x in x.split()))
    news_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Removing Web Addresses and User_ids
    Hmmm... I see that our data has web addresses and user_ids within the data. These will not add to our analysis, so I'm going to remove those at this point.

    Why now? Well, if I wait to do this until after I remove punctuation, I lose that ablitiy to match off of the specific patterns I'm looking for
    """)
    return


@app.cell
def _(news_df):
    news_df['clean_text'] = news_df.clean_text.str.replace('\S+@\S+','') #looking for the case of XXXX@XXXX
    news_df['clean_text'] = news_df.clean_text.str.replace('http\S+','') #looking for http or https web addresses
    news_df['clean_text'] = news_df.clean_text.str.replace('\S+.com','') #looking for email addresses that end in '.com'
    news_df['clean_text'] = news_df.clean_text.str.replace('\S+.edu','') #looking for email addresses that end in '.edu'
    news_df['clean_text'] = news_df.clean_text.str.replace('\S+.uucp','') #looking for email addresses that end in '.uucp'
    news_df['clean_text'] = news_df.clean_text.str.replace('[^A-Za-z0' '9]+',' ') #removing special characters
    news_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Removing Punctuation
    The next step is to remove punctuation, as it doesn’t add any extra information while treating text data.
    """)
    return


@app.cell
def _(news_df):
    news_df['clean_text'] = news_df.clean_text.str.replace('[^\w\s]','')
    news_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Removing Digits
    Time to remove digits from the individual posts. Like punctuations, digits don’t add any extra information to our analysis.
    """)
    return


@app.cell
def _(news_df):
    news_df['clean_text'] = news_df.clean_text.str.replace('\d+','')
    news_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-info">
    <b>Another thought::</b> Here's another approach to removing digits from textual data <br>

    news_df.raw_text.apply(lambda x: " ".join([word for word in x.split() if word.isalpha()] ))
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Removing Stopwords
    As we discussed earlier, stop words (or commonly occurring words) should be removed from the text data. For this purpose, we can either create a list of stopwords ourselves or we can use predefined libraries. As I did above, I'll use the nltk for my stopword list.
    """)
    return


@app.cell
def _(news_df, stopwords):
    from nltk.corpus import words
    _stop = stopwords.words('english')
    news_df['clean_text'] = news_df.clean_text.apply(lambda x: ' '.join((w for w in x.split() if w not in _stop)))
    news_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Word Tokenization
    Tokenization refers to dividing the text into a sequence of words or sentences
    """)
    return


@app.cell
def _(news_df):
    tokens = ' '.join(news_df.clean_text).split()
    tokens[:200]
    return (tokens,)


@app.cell
def _(tokens):
    print(len(tokens))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Lemmatization
    Lemmatization converts the word into its root word, rather than just stripping the suffices. It makes use of the vocabulary and does a morphological analysis to obtain the root word. This will allow us to group similar words together.
    """)
    return


@app.cell
def _(nltk):
    from nltk.stem import WordNetLemmatizer
    nltk.download('wordnet')
    #establish the lemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()
    return (WordNetLemmatizer,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's see how lemmatization works!
    """)
    return


@app.cell
def _(WordNetLemmatizer):
    wordnet_lemmatizer_1 = WordNetLemmatizer()
    _words = ['cry', 'cries', 'studies', 'studying', 'writes']
    print(f"{'Word':<10} | {'Default (Noun)':<15} | {'With POS=Verb'}")
    print('-' * 45)
    for w in _words:
        default_lemma = wordnet_lemmatizer_1.lemmatize(w)
        verb_lemma = wordnet_lemmatizer_1.lemmatize(w, pos='v')
        print(f'{w:<10} | {default_lemma:<15} | {verb_lemma}')
    return (wordnet_lemmatizer_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Alright! Time to apply this to our dataset. I will be writing this data to a new column in the dataframe.
    """)
    return


@app.cell
def _(news_df, wordnet_lemmatizer_1):
    news_df['clean_text'] = news_df.clean_text.apply(lambda x: ' '.join((wordnet_lemmatizer_1.lemmatize(w, pos='v') for w in x.split())))
    news_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Okay, I think that's all of the data cleansing and prep that I'm going to do at this point. I do need to do a bit of data prep for some of our analytics coming up. As we did with the data cleaning, I'll be creating additional columns within the dataframe for us to see how things morph as we progress.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Text Analytics
    Time to take a look at some of the more common Text Analytic techniques.

    #### Text Visualization - WordCloud
    A word cloud is a clustering of the words within a text. The bigger and bolder the word appears, the more often it’s mentioned within a given text and the more important it is.

    The first thing we need to do is generate a frequency dictionary for our text data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-success">
    <b>Installations::</b> You might need to install the package for WordCloud<br>
    pip install wordcloud
    </div>
    """)
    return


@app.cell
def _(news_df, pd):
    # '%pip install wordcloud' command supported automatically in marimo
    from wordcloud import WordCloud
    freq = pd.Series(' '.join(news_df.clean_text).split()).value_counts().to_dict()

    # although dictionaries are useful data structures, they are hard to 'slice-off' specific secions, so we use a list of this
    list(freq.items())[:20]
    return (WordCloud,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hmmm... Looks like we have a couple of other "words" that don't seem to be part of the English language. From what we can tell at this point all these are single letter "words". Not sure where they came from, but they are easily removed.
    """)
    return


@app.cell
def _(news_df, pd):

    news_df['clean_text'] = news_df.clean_text.apply(lambda x: ' '.join((x for x in x.split() if len(x) > 1)))
    news_df['clean_text']= news_df.clean_text.apply(lambda x: x.replace("|>", '').strip())
    news_df['clean_text']= news_df.clean_text.apply(lambda x: x.replace(">>", '').strip())
    news_df['clean_text']= news_df.clean_text.apply(lambda x: x.replace("--", '').strip())
    freq_1 = pd.Series(' '.join(news_df.clean_text).split()).value_counts().to_dict()
    list(freq_1.items())[:20]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hmmm...  I have no idea what a 'maxaxaxaxaxaxaxaxaxaxaxaxaxaxax' is...  I'm going to remove it too
    """)
    return


@app.cell
def _(news_df, pd):
    remove = "max>'ax>'ax>'ax>'ax>'ax>'ax>'ax>'ax>'ax>'ax>'ax>'ax>'ax>'ax>'"
    news_df['clean_text'] = news_df.clean_text.str.replace(remove, '')
    freq_2 = pd.Series(' '.join(news_df.clean_text).split()).value_counts().to_dict()
    list(freq_2.items())[:20]
    return (freq_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That looks better! Time actually build the WordCloud and display it.
    """)
    return


@app.cell
def _(WordCloud, freq_2):
    #install worldcloud
    #!pip install wordcloud
    #from wordcloud import WordCloud
    wc = WordCloud(width=1000, height=600, max_words=200).generate_from_frequencies(freq_2)
    return (wc,)


@app.cell
def _(plt, wc):
    plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Not bad at all, if I do say so myself!  I can see that the top 2 words within our dataset are 'would', 'one'.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### N-grams
    N-grams are the combination of multiple words used together. N-grams with N=1 are called unigrams. Similarly, bigrams (N=2), trigrams (N=3) and so on can also be used.

    Unigrams do not usually contain as much information as compared to bigrams and trigrams. The basic principle behind n-grams is that they capture the language structure, like what letter or word is likely to follow the given one.

    The longer the n-gram (the higher the n), the more context you have to work with. Optimum length really depends on the application – if your n-grams are too short, you may fail to capture important differences. On the other hand, if they are too long, you may fail to capture the “general knowledge” and only stick to particular cases.

    I'm going to use nltk's `bigram()` to create bigrams for our dataset. First thing we need to do is create a list of individual words within our cleaned text.  This is known as tokenization, resulting in a list of tokens.
    """)
    return


@app.cell
def _(news_df):
    #regenerate the tokens list, remember we did more data cleaning since we last generated this list
    tokens_1 = ' '.join(news_df.clean_text).split()
    return (tokens_1,)


@app.cell
def _(nltk, pd, tokens_1):
    # creating the bigrams
    ngrams_2 = nltk.bigrams(tokens_1)
    freq_2grams = pd.Series(ngrams_2).value_counts().to_dict()
    # freq distribution for these
    list(freq_2grams.items())[:20]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Awesome!  Let's try generating `trigrams()` now.
    """)
    return


@app.cell
def _(nltk, pd, tokens_1):
    # creating the bigrams
    ngrams_3 = nltk.trigrams(tokens_1)
    freq_3grams = pd.Series(ngrams_3).value_counts().to_dict()
    # freq distribution for these
    list(freq_3grams.items())[:20]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Comparing the bigrams with the trigrams, we can see that same of the trigrams contain a lot of information as to what the post is about.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Part of Speech (POS)
    Back in elementary school you learnt the difference between nouns, verbs, adjectives, and adverbs. These "word classes" are not just the idle invention of English teachers, but are useful categories for many language processing tasks.

    The process of classifying words into their parts of speech and labeling them accordingly is known as part-of-speech tagging, POS-tagging, or simply tagging. Parts of speech are also known as word classes or lexical categories. The collection of tags used for a particular task is known as a tagset. Our emphasis in this chapter is on exploiting tags, and tagging text automatically.
    """)
    return


@app.cell
def _(nltk, tokens_1):
    nltk.download('averaged_perceptron_tagger_eng')
    from nltk.tag import pos_tag
    pos_tags = pos_tag(tokens_1)
    pos_tags[:20]
    return (pos_tag,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Okay?  What does all of that mean?  NN? VBG?

    Those are the tags assocaiated with the POS tagging process.
    'NN' --> singular noun, 'VBG' -->present verb, 'WRB' --> adverb.

    You can read more about the individual classes in POS tagging [here](https://www.learntek.org/blog/categorizing-pos-tagging-nltk-python/).

    How about we see about creating a frequency distribution for the parts of speech in our dataset?
    """)
    return


@app.cell
def _(pos_tag, tokens_1):
    from collections import Counter
    Counter([j for i, j in pos_tag(tokens_1)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Interesting!  So what can we do with this information (aka analytics) at this point.  Well, you could create a histogram showing the distribution of the POS tags. I'll leave that as an exercise for you to work through.

    How could this type of analysis be useful? If you had multiple documents, you could create a POS distribution for each document and then compare the language structure between the documents. As an example, an author develops a style of writing that is unique to the author. You could do a POS analysis to to compare the structure between authors or even documents from the same author.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Topic Modeling with Gensim
    Topic modeling is a machine learning technique that automatically analyzes text data to determine cluster words for a set of documents. This is known as ‘unsupervised’ machine learning because it doesn’t require a predefined list of tags or training data that’s been previously classified by humans.

    Topic modeling involves counting words and grouping similar word patterns to infer topics within unstructured data. Let’s say you’re a software company and you want to know what customers are saying about particular features of your product. Instead of spending hours going through heaps of feedback, in an attempt to deduce which texts are talking about your topics of interest, you could analyze them with a topic modeling algorithm.

    By detecting patterns such as word frequency and distance between words, a topic model clusters feedback that is similar, and words and expressions that appear most often. With this information, you can quickly deduce what each set of texts are talking about. Remember, this approach is ‘unsupervised’ meaning that no training is required.

    Now, let’s say you train a model to detect specific topics. That’s a whole different kettle of fish, and a step that’s needed for topic classification algorithms – a supervised technique. Let’s compare the two topic analysis algorithms to further understand the differences between them.

    References:
    > Topic Modeling: An Introduction <br>
    > https://monkeylearn.com/blog/introduction-to-topic-modeling/

    > Topic Modeling with Gensim (Python) <br>
    > https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/

    First thing we are going to need is a list of list of our lemmatized text. This means each row of lemmatized text --> list  of individual lemmas, then each row list is added to a larger list.
    """)
    return


@app.cell
def _(news_df):
    lem_ls = list(news_df.clean_text.apply(lambda x: list(x.split())))
    print(lem_ls[:2])
    return (lem_ls,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-success">
    <b>Installations::</b> You might need to install Gensim and pyLDAvis<br>
    pip install -U gensim <br>
    pip install pyLDAvis <br>
    pip install --upgrade smart_open <br>
    pip install funcy
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are a number of models available to use for topic modeling.  I have decided to use the Gensim package which uses Latent Dirichlet Allocation (LDA). LDA’s approach to topic modeling is it considers each document as a collection of topics in a certain proportion. And each topic as a collection of keywords, again, in a certain proportion.
    """)
    return


@app.cell
def _():
    # Gensim
    #install gensim
    #!pip install gensim
    import gensim
    import gensim.corpora as corpora

    return corpora, gensim


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    At this point we will need to construct a dictionary of our lemmatized terms and a term document frequency (TDF) for our dataset.

    TDF is a matrix that track the number of times each word, across the entire dataset, appears within each document in the the dataset. As an example, our TDF will track the number of times the word 'messge' appears in each of the posts within our dataset.
    """)
    return


@app.cell
def _(corpora, lem_ls):
    # Create Dictionary
    id2word = corpora.Dictionary(lem_ls)

    # Term Document Frequency Corpus
    #texts = lem_ls
    corpus = [id2word.doc2bow(post) for post in lem_ls]
    return (id2word,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have everything required to train the LDA model. In addition to the corpus and dictionary, you need to provide the number of topics as well.

    `random_state` is the same as we have seen with our other ML lessons. `chunksize` is the number of documents to be used in each training chunk. `passes` controls how oftern we train the model on the entire corpus.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div class="alert alert-block alert-danger">
    <b>Patience is a Virtue::</b> The topic model will take some time to build
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I'll trim the extreme values since they slow down the model.
    """)
    return


@app.cell
def _(id2word, lem_ls):
    id2word.filter_extremes(no_below=5, no_above=0.95)
    corpus_final  = [id2word.doc2bow(post) for post in lem_ls] 
    return (corpus_final,)


@app.cell
def _(corpus_final, gensim, id2word):
    # Build Basic LDA model
    lda_model = gensim.models.LdaMulticore(corpus=corpus_final,
                                           id2word=id2word,
                                           num_topics=10, 
                                           random_state=42,
                                           chunksize=2000,
                                           passes=5,
                                           workers=3,
                                           per_word_topics=False)
    return (lda_model,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Time to look at the results!
    """)
    return


@app.cell
def _(lda_model):
    # Print the Keyword in the 10 topics
    print(lda_model.print_topics())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### View Model Output
    How to interpret this?

    Topic 0 is represented as ('0.011*"use" + 0.005*"get" + 0.005*"one" + 0.004*"file" + 0.004*"would" + 0.004*"also" + 0.004*"program" + 0.004*"system" + 0.004*"data" + 0.004*"drive"').

    Meaning the top 10 words in Topic 0 are: use, get, one, file, would, also, program, system, data and drive.

    The numeric values in front of each word reflects the importance of that word within the topic.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Evaluation of Model
    All of the information above is great, but the larger question is how do we evaluate the performance of our model? As we saw in our supervised and unsupervised learning exercises in prior weeks, the evaluation of a model is important. Your results are only as good as the accuracy of your model to represent your data.

    For Topic Modeling, we use coherence score to evaluate our model.

    <b>Coherence:</b> a set of statements or facts is said to be coherent, if they support each other. Thus, a coherent fact set can be interpreted in a context that covers all or most of the facts. An example of a coherent fact set is “the game is a team sport”, “the game is played with a ball”, “the game demands great physical efforts”.

    Here are a couple of the different coherence scores that can be used in evaluating your topic model:
    * **c_v:** measure is based on a sliding window, one-set segmentation of the top words and an indirect confirmation measure that uses normalized pointwise mutual information (NPMI) and the cosine similarity
    * **c_p:** based on a sliding window, one-preceding segmentation of the top words and the confirmation measure of Fitelson’s coherence
    * **c_uci:** measure is based on a sliding window and the pointwise mutual information (PMI) of all word pairs of the given top words
    * **c_a:** baseed on a context window, a pairwise comparison of the top words and an indirect confirmation measure that uses normalized pointwise mutual information (NPMI) and the cosine similarity

    References:
    > Evaluate Topic Models: Latent Dirichlet Allocation (LDA)<br>
    > https://towardsdatascience.com/evaluate-topic-model-in-python-latent-dirichlet-allocation-lda-7d57484bb5d0

    We will be using c_v for our coherence evaluation.
    """)
    return


@app.cell
def _(id2word, lda_model, lem_ls):
    from gensim.models import CoherenceModel
    _coherence_model_lda = CoherenceModel(model=lda_model, texts=lem_ls, dictionary=id2word, coherence='c_v')
    # compute the coherence score
    _coherence_lda = _coherence_model_lda.get_coherence()
    #print the coherence score
    print('\nCoherence Score: ', _coherence_lda)
    return (CoherenceModel,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Well, .42 isn't all the great.  But remember, we haven't done anything about optimizing the base model. Plus, we randomly picked the number of topics.

    ##### Optimizing the Model
    Like we saw with our KNN and kMeans algorithms, the number of neighbors or cluster, effects the performance of an algorithm. so let's vary the number of topics and compare coherence scores.

    <div class="alert alert-block alert-danger">
    <b>Remember - Patience is a Virtue::</b> We are building several models this time around.
    """)
    return


@app.cell
def _(CoherenceModel, corpus_final, gensim, id2word, lem_ls):
    scores = []
    for i in range(2, 15):
        print(f'Calculating for {i} topics')
        lda_model_1 = gensim.models.LdaMulticore(corpus=corpus_final, id2word=id2word, num_topics=i, random_state=42, chunksize=2000, passes=5, workers=3, per_word_topics=False)
        _coherence_model_lda = CoherenceModel(model=lda_model_1, texts=lem_ls, dictionary=id2word, coherence='c_v')
        _coherence_lda = _coherence_model_lda.get_coherence()
        scores.append((i, _coherence_lda))
    return (scores,)


@app.cell
def _(scores):
    scores
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Okay... It looks like 2 topics does the best for these parameters.  There are several more parameters that we could play with to increase our coherence score, however, that is out of scope for this course.

    Let's create a best_fit model, based on the best coherence score above.
    """)
    return


@app.cell
def _(corpus_final, gensim, id2word):
    bf_lda_model = gensim.models.LdaMulticore(corpus=corpus_final,
                                           id2word=id2word,
                                           num_topics=2, 
                                           random_state=42,
                                           chunksize=2000,
                                           passes=2,
                                           #use all available cores
                                            workers=3,
                                           per_word_topics=False)
    return (bf_lda_model,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Visualizing the Topics
    pyLDAvis produces an interactive visual of your topic model. A good topic model will have equal sized, non-overlapping, bubbles evenly scattered throughout the chart.

    This chart is interactive and will change as you mouse-over various objects (bubbles, word list, etc) in the graph.
    * Each bubble represents a topic. The larger the bubble, the higher percentage of of news articles represented by the topic.
    * Blue bars represent the overall frequency of each word in the corpus. If no topic is selected, the blue bars of the most frequently used words will be displayed.
    * Red bars give the estimated number of times a given term was generated by a given topic.
    * The further the bubbles are away from each other, the more different they are.
    """)
    return


@app.cell
def _(bf_lda_model, corpus_final, id2word):
    # Packages necessry to support the visualization of the topic model
    #install pyLDAvis
    #pip install pyLDAvis
    #import ipython
    #import ipython
    import pyLDAvis
    import pyLDAvis.gensim_models
    #pyLDAvis.enable_notebook()
    # Visualize the topics
    LDAvis_prepared = pyLDAvis.gensim_models.prepare(bf_lda_model, corpus_final, id2word)
    LDAvis_prepared
    return LDAvis_prepared, pyLDAvis


@app.cell
def _(LDAvis_prepared, mo, pyLDAvis):
    # Convert to HTML string and wrap in mo.Html — never call pyLDAvis.display()
    html_str = pyLDAvis.prepared_data_to_html(LDAvis_prepared)
    mo.Html(html_str)

    import base64
    #making viz work in marimo by encoding the html string as base64 and then embedding it in an iframe
    html_bytes = html_str.encode("utf-8")
    b64 = base64.b64encode(html_bytes).decode("utf-8")
    mo.Html(f'<iframe src="data:text/html;base64,{b64}" width="100%" height="800px" frameborder="0"></iframe>')

    return (html_str,)


@app.cell
def _(html_str):
    #save vis to html file
    with open("lda_vis.html", "w") as f:
        f.write(html_str)
    return


if __name__ == "__main__":
    app.run()
