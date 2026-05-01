# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.3",
#     "nltk>=3.9.4",
#     "pandas>=3.0.2",
#     "numpy>=2.4.4",
#     "matplotlib>=3.10.8",
#     "seaborn>=0.13.2",
#     "scikit-learn>=1.8.0",
#     "gensim>=4.4.0",
#     "wordcloud>=1.9.6",
#     "pyldavis>=3.4.1",
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
    # Week 8 Assignment: Text Analytics
    **Dataset:** BBC News Articles (bbc.csv)
    2225 BBC news articles from 2004-2005 across five topics: business, entertainment, politics, sport, tech.
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
    sns.set_theme()
    return pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Load the Dataset

    The BBC dataset has three columns: `id`, `news` (the article text), and `type` (the topic label).
    We load it into a Pandas DataFrame, which we will use for all subsequent steps.
    """)
    return


@app.cell
def _(pd):
    bbc_df = pd.read_csv('bbc.csv')
    print(bbc_df.shape)
    print(bbc_df['type'].value_counts())
    bbc_df.head(3)
    return (bbc_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Basic Text Metrics

    Before cleaning, we extract three simple numeric features from the raw text:
    - `word_cnt`: number of space-separated tokens per article
    - `char_cnt`: total character count per article
    - `stopwords`: number of NLTK English stopwords present in each article

    These give a baseline sense of article length and composition across the five topic categories.
    """)
    return


@app.cell
def _(bbc_df):
    import nltk
    nltk.download('stopwords', quiet=True)
    from nltk.corpus import stopwords

    bbc_df['word_cnt'] = bbc_df['news'].apply(lambda x: len(str(x).split(" ")))
    bbc_df['char_cnt'] = bbc_df['news'].str.len()

    _stop = stopwords.words('english')
    bbc_df['stopwords'] = bbc_df['news'].apply(
        lambda x: len([w for w in x.split() if w in _stop])
    )

    bbc_df[['word_cnt', 'char_cnt', 'stopwords']].describe()
    return nltk, stopwords


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Data Cleaning

    Raw news text contains mixed-case words, punctuation, digits, and URLs. We clean the text
    in the following order so each step builds on the last:

    1. **Lowercase** -- so "Economy" and "economy" are treated as the same word
    2. **Remove URLs and special patterns** -- strips http links and .com/.co.uk addresses
    3. **Remove punctuation** -- removes all non-word, non-space characters
    4. **Remove digits** -- numbers do not carry topic meaning here
    5. **Remove stopwords** -- filters high-frequency words like "the", "is", "and" that add noise

    The result is stored in a new `clean_text` column.
    """)
    return


@app.cell
def _(bbc_df, stopwords):
    # Step 1 -- lowercase
    bbc_df['clean_text'] = bbc_df['news'].apply(
        lambda x: " ".join(tok.lower() for tok in x.split())
    )

    # Step 2 -- remove URLs and web patterns
    bbc_df['clean_text'] = bbc_df['clean_text'].str.replace(r'http\S+', '', regex=True)
    bbc_df['clean_text'] = bbc_df['clean_text'].str.replace(r'\S+\.com', '', regex=True)
    bbc_df['clean_text'] = bbc_df['clean_text'].str.replace(r'\S+\.co\.uk', '', regex=True)
    bbc_df['clean_text'] = bbc_df['clean_text'].str.replace(r'[^A-Za-z0-9]+', ' ', regex=True)

    # Step 3 -- remove punctuation
    bbc_df['clean_text'] = bbc_df['clean_text'].str.replace(r'[^\w\s]', '', regex=True)

    # Step 4 -- remove digits
    bbc_df['clean_text'] = bbc_df['clean_text'].str.replace(r'\d+', '', regex=True)

    # Step 5 -- remove stopwords
    _stop = stopwords.words('english')
    bbc_df['clean_text'] = bbc_df['clean_text'].apply(
        lambda x: ' '.join(w for w in x.split() if w not in _stop)
    )

    # Also remove single-character tokens
    bbc_df['clean_text'] = bbc_df['clean_text'].apply(
        lambda x: ' '.join(w for w in x.split() if len(w) > 1)
    )

    print("Sample cleaned article (first 200 chars):")
    print(bbc_df['clean_text'][0][:200])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Word Frequency -- Top 10 and Bottom 10

    We tokenize the entire thing into a flat list of words and use `pd.Series.value_counts()`
    to count how often each word appears. The 10 most and 10 least frequent words are printed.
    """)
    return


@app.cell
def _(bbc_df, pd):
    tokens = ' '.join(bbc_df['clean_text']).split()
    freq = pd.Series(tokens).value_counts()

    print("Top 10 most frequent words:")
    print(freq.head(10).to_string())

    print("\nTop 10 least frequent words:")
    print(freq.tail(10).to_string())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Lemmatization

    Lemmatization reduces words to their dictionary roots (e.g., "says" becomes "say"),
    preventing frequency counts from being split across different forms. We use NLTK’s
    WordNetLemmatizer in verb mode for better accuracy with news text. Post-processing,
    we re-evaluate word frequencies; common words may rise as variants merge, while rare
    inflections of common words often disappear.
    """)
    return


@app.cell
def _(bbc_df, nltk, pd):
    from nltk.stem import WordNetLemmatizer
    nltk.download('wordnet', quiet=True)

    wordnet_lemmatizer = WordNetLemmatizer()

    bbc_df['lem_text'] = bbc_df['clean_text'].apply(
        lambda x: ' '.join(wordnet_lemmatizer.lemmatize(w, pos='v') for w in x.split())
    )

    lem_tokens = ' '.join(bbc_df['lem_text']).split()
    lem_freq = pd.Series(lem_tokens).value_counts()

    print("Top 10 most frequent words AFTER lemmatization:")
    print(lem_freq.head(10).to_string())

    print("\nTop 10 least frequent words AFTER lemmatization:")
    print(lem_freq.tail(10).to_string())
    return (lem_freq,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Comparing the before and after frequency lists shows how lemmatization consolidates word
    counts. Words like "said" and "says" now map to "say", so "say" climbs in rank while
    "said" and "says" drop out. Rare words that were simply inflections of common words also
    disappear from the bottom of the list, leaving only genuinely unique vocabulary there.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Word Cloud

    A word cloud renders words at a size proportional to their frequency. Larger words appear
    more often across all 2225 articles. This gives an immediate visual summary of the most
    prominent vocabulary in the BBC corpus. We use the lemmatized frequency dictionary to build the cloud so that word variants are
    consolidated before visualization.
    """)
    return


@app.cell
def _(lem_freq, plt):
    from wordcloud import WordCloud

    freq_dict = lem_freq.to_dict()

    wc = WordCloud(width=1000, height=500, max_words=200).generate_from_frequencies(freq_dict)

    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud -- BBC News Corpus (Lemmatized)", fontsize=14)
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7. N-grams -- Bigrams and Trigrams

    A single word loses context. An n-gram is a sequence of n consecutive words that preserves
    that context. Bigrams (n=2) and trigrams (n=3) often surface meaningful phrases that
    individual tokens do not.

    We use `nltk.bigrams()` and `nltk.trigrams()` on the lemmatized token list, then count
    with `pd.Series.value_counts()`.
    """)
    return


@app.cell
def _(bbc_df, nltk, pd):
    _tokens = ' '.join(bbc_df['lem_text']).split()

    ngrams_2 = nltk.bigrams(_tokens)
    freq_2grams = pd.Series(list(ngrams_2)).value_counts()
    print("Top 10 Bigrams:")
    print(freq_2grams.head(10).to_string())

    print()

    ngrams_3 = nltk.trigrams(_tokens)
    freq_3grams = pd.Series(list(ngrams_3)).value_counts()
    print("Top 10 Trigrams:")
    print(freq_3grams.head(10).to_string())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8. Part-of-Speech (POS) Tagging

    POS tagging labels each token with its grammatical role: noun, verb, adjective, etc.
    NLTK's `pos_tag()` uses the Penn Treebank tag set. We tag the first 2000 tokens from
    the lemmatized corpus and print the most common grammatical categories.
    """)
    return


@app.cell
def _(bbc_df, nltk):
    from nltk.tag import pos_tag
    from collections import Counter

    nltk.download('averaged_perceptron_tagger_eng', quiet=True)

    _tokens = ' '.join(bbc_df['lem_text']).split()
    pos_tags = pos_tag(_tokens[:2000])

    print("Sample tags (first 15):", pos_tags[:15])
    print()

    pos_counts = Counter(tag for _, tag in pos_tags)
    print("POS Frequency Distribution (top 15):")
    for tag, count in sorted(pos_counts.items(), key=lambda x: -x[1])[:15]:
        print(f"  {tag:<6} {count:>6}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 9. Topic Modeling with LDA

    Latent Dirichlet Allocation (LDA) is an unsupervised technique that discovers topics
    by finding groups of words that frequently co-occur across documents. No labeled data
    is required. Each document is treated as a mixture of topics and each topic as a mixture
    of words.
    """)
    return


@app.cell
def _(bbc_df):
    import gensim
    import gensim.corpora as corpora

    lem_ls = list(bbc_df['lem_text'].apply(lambda x: list(x.split())))

    id2word = corpora.Dictionary(lem_ls)
    id2word.filter_extremes(no_below=5, no_above=0.95)
    corpus_final = [id2word.doc2bow(doc) for doc in lem_ls]

    print(f"Dictionary size after filtering: {len(id2word):,} unique terms")
    print(f"Corpus size: {len(corpus_final):,} documents")
    return corpus_final, gensim, id2word, lem_ls


@app.cell
def _(corpus_final, gensim, id2word):
    lda_model = gensim.models.LdaMulticore(
        corpus=corpus_final,
        id2word=id2word,
        num_topics=5,
        random_state=42,
        chunksize=500,
        passes=5,
        workers=3,
        per_word_topics=False
    )
    print("Top keywords per topic:")
    for topic in lda_model.print_topics():
        print(f"  Topic {topic[0]}: {topic[1][:100]}")
    return (lda_model,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Reading the output:** Each topic is shown as a ranked list of words with weights.
    The weight (e.g. `0.005*"government"`) reflects how strongly that word defines the topic.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 10. Finding the Optimal Number of Topics

    Coherence score measures how semantically consistent the top words within each topic are.
    A higher `c_v` coherence score indicates more meaningful topics. We loop from 2 to 9
    topics, train a model at each value, and record the coherence score. The number of topics
    at the peak (or elbow) of the resulting line chart is the best fit for this data.
    """)
    return


@app.cell
def _(CoherenceModel, corpus_final, gensim, id2word, lem_ls, plt):
    scores = []
    for i in range(2, 10):
        print(f'Calculating for {i} topics')
        _lda = gensim.models.LdaMulticore(
            corpus=corpus_final, id2word=id2word, num_topics=i,
            random_state=42, chunksize=500, passes=5, workers=3, per_word_topics=False
        )
        _cm = CoherenceModel(model=_lda, texts=lem_ls, dictionary=id2word, coherence='c_v')
        scores.append((i, _cm.get_coherence()))
        print(f"  Topics={i}  Coherence={scores[-1][1]:.4f}")

    topic_nums = [s[0] for s in scores]
    coh_vals = [s[1] for s in scores]

    plt.figure(figsize=(8, 4))
    plt.plot(topic_nums, coh_vals, marker='o')
    plt.xlabel("Number of Topics")
    plt.ylabel("Coherence Score (c_v)")
    plt.title("LDA Coherence Score by Number of Topics -- BBC News")
    plt.tight_layout()
    plt.show()
    return (scores,)


@app.cell
def _(id2word, lda_model, lem_ls):
    from gensim.models import CoherenceModel
    _cm = CoherenceModel(model=lda_model, texts=lem_ls, dictionary=id2word, coherence='c_v')
    print(f"Coherence Score (5 topics): {_cm.get_coherence():.4f}")
    return (CoherenceModel,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 11. Best-Fit Topic Model - Two Displays

    Using the optimal topic count identified from the coherence search, we train a final
    best-fit model. Results are shown two ways:

    **Display 1 -- Print topics:** The top 10 keywords for each topic are printed. Reading
    across the words, we can assign a readable label to each topic and check whether
    they align with the five BBC categories.
    """)
    return


@app.cell
def _(corpus_final, gensim, id2word, scores):
    best_n = max(scores, key=lambda x: x[1])[0]
    print(f"Best number of topics from coherence search: {best_n}")

    bf_lda_model = gensim.models.LdaMulticore(
        corpus=corpus_final,
        id2word=id2word,
        num_topics=best_n,
        random_state=42,
        chunksize=500,
        passes=5,
        workers=3,
        per_word_topics=False
    )

    print("\nBest-Fit Topics:")
    for t in bf_lda_model.print_topics(num_words=10):
        print(f"  Topic {t[0]}: {t[1]}")
    return best_n, bf_lda_model


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Insights from printed topics:** Each topic's keyword list can be read as a rough theme.
    We look for coherent clusters matching the known BBC labels (business, entertainment,
    politics, sport, tech). Topics with high-weight words like "government", "minister",
    "election" point to politics. Words like "player", "match", "club" point to sport.
    Words like "company", "market", "growth" point to business. Mixed topics may indicate
    areas where the corpus vocabulary overlaps across categories.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Display 2 -- Bar chart:** A horizontal bar chart plots the top 8 words per topic so
    the keyword weights can be compared visually across topics.
    """)
    return


@app.cell
def _(best_n, bf_lda_model, plt):
    fig, axes = plt.subplots(1, best_n, figsize=(4 * best_n, 5), sharey=False)

    if best_n == 1:
        axes = [axes]

    for idx, ax in enumerate(axes):
        topic_terms = bf_lda_model.show_topic(idx, topn=8)
        words = [t[0] for t in topic_terms]
        weights = [t[1] for t in topic_terms]
        ax.barh(words[::-1], weights[::-1])
        ax.set_title(f"Topic {idx}")
        ax.set_xlabel("Weight")

    plt.suptitle("Top Words per Topic -- BBC Best-Fit LDA", fontsize=13)
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Insights from bar chart:** The bar chart makes word weights directly comparable within
    and across topics. A topic with one dominant word and steeply falling bars is more focused
    than a topic where weights are spread evenly across many words. Topics where several words
    have similar weights are harder to label and may benefit from further cleaning or a
    different number of topics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## References

    Anthropic. (2026, April 30). *Text Analytics*

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Generative AI chat]. Claude Sonnet 4.6. https://claude.ai/share/98a67af8-084f-4f47-ab50-8ece0f7106af

    Python max function using “key” and Lambda Expression. Stack Overflow. https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression

    ---

    # Appendix

    ## Request
    Could you make me a list of the concepts in  the 8_Text_Analytics.py file and describe
    what each one is used for and how it works? put them in numerical order. provide the
    results in a Marimo style file with code windows for example code snippets when appropriate.
    the format should be markdown window describing the concept, code window with the code, and
    a markdown window explaining results and what the code is doing. provide a summary of our
    conversation in markdown code to be used in a reference appendix section

    ## Constraints Applied
    - No em dashes used anywhere.
    - No code written outside what appears in the project files.
    - No analysis or conclusions provided beyond what the code demonstrates.
    - All code snippets are direct references from `8_Text_Analytics.py`.

    ## Concepts Covered (in order)

    | # | Concept | Key Tool / Function |
    |---|---|---|
    | 1 | Loading the Dataset (sklearn Bunch) | `fetch_20newsgroups`, `joblib` |
    | 2 | Loading Data into a Pandas DataFrame | `pd.DataFrame`, `lambda` with `target_names` |
    | 3 | Basic Text Metrics (word count, char count, stopword count) | `str.split`, `str.len`, NLTK stopwords |
    | 4 | Convert Text to Lowercase | `str.lower` via lambda |
    | 5 | Remove Web Addresses, User IDs, Special Characters | `str.replace` with regex patterns |
    | 6 | Remove Punctuation and Digits | regex `[^\w\s]` and `\d+` |
    | 7 | Remove Stopwords | NLTK `stopwords.words('english')` |
    | 8 | Word Tokenization | `str.split`, flat token list |
    | 9 | Lemmatization | NLTK `WordNetLemmatizer`, `pos='v'` |
    | 10 | Word Cloud | `wordcloud.WordCloud`, frequency dict, `matplotlib` |
    | 11 | N-grams (Bigrams and Trigrams) | `nltk.bigrams`, `nltk.trigrams`, `pd.Series.value_counts` |
    | 12 | Part-of-Speech (POS) Tagging | NLTK `pos_tag`, `collections.Counter` |
    | 13 | Topic Modeling with LDA | Gensim `LdaMulticore`, `corpora.Dictionary`, `doc2bow` |
    | 14 | Coherence Score (Model Evaluation) | Gensim `CoherenceModel`, c_v metric |
    | 15 | Best-Fit LDA Model and pyLDAvis Visualization | `gensim.models.LdaMulticore`, `pyLDAvis` |
    """)
    return


if __name__ == "__main__":
    app.run()
