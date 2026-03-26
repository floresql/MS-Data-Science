# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Descriptive Statistics — Concepts Reference Guide

    Based on `2_DescriptiveStatistics_DerivingInsights.py`

    ---
    """)
    return


# ── TABLE OF CONTENTS ─────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Table of Contents

    | # | Concept |
    |---|---------|
    | 1 | Descriptive Statistics |
    | 2 | Categorical Data |
    | 3 | Numerical Data |
    | 4 | Problem Statement |
    | 5 | Analytical Questions |
    | 6 | Univariate Analysis |
    | 7 | Segmented Univariate Analysis |
    | 8 | Multivariate Analysis |
    | 9 | `pandas` — Data Loading and Inspection |
    | 10 | `value_counts()` |
    | 11 | `describe()` |
    | 12 | `groupby()` |
    | 13 | Histogram |
    | 14 | Boxplot |
    | 15 | Interquartile Range (IQR) |
    | 16 | Lower and Upper Fences (Outlier Detection) |
    | 17 | Bimodal Distribution |
    | 18 | Altair — Interactive Charting |
    | 19 | Marimo — Reactive Notebook Framework |
    """)
    return


# ── CONCEPT 1 ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 1. Descriptive Statistics

    **What it is:** The initial step in understanding and summarizing data. It involves organizing,
    visualizing, and summarizing raw data to create a coherent picture of a dataset's main features.

    **Used for:** Identifying patterns, trends, and characteristics within a dataset — without making
    broader inferences or predictions. Common summary outputs include mean, median, mode, variance,
    range, frequencies, and proportions.

    > **Note:** Descriptive statistics describe only the data at hand and do not allow conclusions
    > to be drawn beyond that data. They are often paired with visualizations to communicate findings clearly.
    """)
    return


# ── CONCEPT 2 ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 2. Categorical Data

    **What it is:** Qualitative data represented by names, labels, or symbols rather than numbers.
    It falls into two subtypes:

    - **Nominal Data** — Categories with no inherent order or hierarchy
      *(e.g., clothing types: shoes, tops, pants)*
    - **Ordinal Data** — Categories that imply a specific order or ranking
      *(e.g., job titles: assistant, manager, director)*

    **Used for:** Grouping and counting observations, frequency analysis, and understanding the
    composition of a dataset.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    # Example: counting occurrences of a categorical column
    bakery['product_id'].value_counts()
    ```
    """)
    return


# ── CONCEPT 3 ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3. Numerical Data

    **What it is:** Quantitative data whose values are always expressed as numbers.
    It falls into two subtypes:

    - **Discrete Data** — Countable values with a finite set of possibilities, typically whole
      numbers *(e.g., number of orders)*
    - **Continuous Data** — Measurable values with infinite possible values that can be broken
      into smaller parts *(e.g., height, weight, price)*

    **Used for:** Mathematical operations such as calculating averages, ranges, and distributions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    # Example: inspecting a numerical column
    bakery['unit_price'].describe()
    ```
    """)
    return


# ── CONCEPT 4 ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4. Problem Statement

    **What it is:** A clear definition of the business problem to be solved before any analysis
    begins. Rooted in the **CRISP-DM** methodology *(Cross-Industry Standard Process for Data
    Mining)*, specifically the *Business Understanding* phase.

    **Used for:** Focusing analytical efforts so that results are relevant and actionable.
    Acts as the driving force for the data analysis plan.

    > **Example from the notebook:**
    > *"HoneyBee Sweet Shop wants to understand how well their products are being received —
    > specifically, customer loyalty and foot traffic over the first 100,000 transactions."*
    """)
    return


# ── CONCEPT 5 ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5. Analytical Questions

    **What it is:** One or more specific questions derived from the problem statement that further
    guide the analysis. Each question must be supportable by variables present in the dataset.

    **Used for:** Breaking a broad problem statement into targeted, measurable inquiries.

    > **Example from the notebook:**
    > - *Customer Loyalty:* How often does each customer visit the bakery?
    > - *Foot Traffic:* What is the range of sales per business day?
    """)
    return


# ── CONCEPT 6 ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 6. Univariate Analysis

    **What it is:** Analysis that examines a **single variable** at a time. It identifies
    characteristics of one feature without exploring relationships between variables.

    **Used for:** Understanding the distribution, central tendency, and spread of an individual feature.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    # Example: counting how many times each customer visited
    bakery.groupby('customer_id').order_id.size().sort_values()
    ```
    """)
    return


# ── CONCEPT 7 ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 7. Segmented Univariate Analysis

    **What it is:** A variation of univariate analysis where data is **grouped or segmented**
    before the single-variable analysis is performed. The segmentation is typically done using
    another feature in the dataset.

    **Used for:** Detecting patterns within subsets of data rather than across the whole dataset at once.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    # Example: group by customer_id, then analyze order frequency
    freq_customers = bakery.groupby('customer_id').order_id.size()
    freq_customers.describe()
    ```
    """)
    return


# ── CONCEPT 8 ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 8. Multivariate Analysis

    **What it is:** Analysis that examines **more than one variable** simultaneously and explores
    the relationships between them.

    **Used for:** Understanding correlations, dependencies, and interactions between two or more
    features *(e.g., does student age correlate with test scores?)*.

    > **Note:** The notebook introduces multivariate analysis conceptually as a contrast to
    > univariate analysis. The demo focuses on univariate techniques.
    """)
    return


# ── CONCEPT 9 ─────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 9. `pandas` — Data Loading and Inspection

    **What it is:** A Python library for data manipulation and analysis. The notebook uses it to
    load, explore, and transform the bakery transactions dataset.

    **Used for:** Reading data from files, inspecting structure, computing summary statistics,
    and transforming data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    import pandas as pd

    # Load data
    bakery = pd.read_csv('data_wk2/transactions.csv')

    # Inspect structure (dtypes, nulls, row count)
    bakery.info()

    # View a random sample of 10 rows
    bakery.sample(10)
    ```
    """)
    return


# ── CONCEPT 10 ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 10. `value_counts()`

    **What it is:** A pandas Series method that returns the count of each unique value,
    sorted from most to least frequent.

    **Used for:** Quickly understanding the frequency distribution of a categorical or discrete feature.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    # How many times does each customer appear in the dataset?
    bakery.customer_id.value_counts()

    # How many sales occurred on each date?
    sales = bakery.order_date.value_counts()
    ```
    """)
    return


# ── CONCEPT 11 ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 11. `describe()`

    **What it is:** A pandas method that generates summary statistics for a Series or DataFrame,
    including **count, mean, standard deviation, min, max,** and **quartile values** (25%, 50%, 75%).

    **Used for:** Getting a quick statistical overview of numerical data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    # Summary statistics for daily sales counts
    sales = bakery.order_date.value_counts()
    sales.describe()

    # Output includes:
    # count  — number of unique dates
    # mean   — average daily sales
    # std    — standard deviation
    # min    — lowest single-day sales
    # 25%    — Q1
    # 50%    — median
    # 75%    — Q3
    # max    — highest single-day sales
    ```
    """)
    return


# ── CONCEPT 12 ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 12. `groupby()`

    **What it is:** A pandas method that **splits data into groups** based on the values of one
    or more columns, allowing aggregate operations to be applied to each group.

    **Used for:** Segmenting data and calculating per-group statistics *(e.g., order count per
    customer, sales per date)*.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    # Count orders per customer
    bakery.groupby('customer_id').order_id.size()

    # Count orders per date, then get the 25th percentile
    bakery.groupby('order_date').size().quantile(q=0.25)
    ```
    """)
    return


# ── CONCEPT 13 ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 13. Histogram

    **What it is:** A chart that displays the **frequency distribution** of a numerical variable
    by grouping values into bins and plotting bar heights proportional to the count in each bin.

    **Used for:** Visualizing the shape of a distribution — whether it is symmetric, skewed,
    or bimodal.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    import matplotlib.pyplot as plt

    freq_customers = bakery.groupby('customer_id').order_id.size()
    freq_customers.hist(bins=13, grid=False, edgecolor='black')
    plt.xlabel('Number of Orders')
    plt.ylabel('Number of Customers')
    plt.title('Distribution of Orders per Customer')
    plt.show()
    ```

    Or using Altair:

    ```python
    import altair as alt

    hist = alt.Chart(
        bakery.groupby('customer_id').order_id.size().reset_index(name='order_count')
    ).mark_bar().encode(
        x=alt.X('order_count:Q', bin=alt.Bin(maxbins=20)),
        y='count()'
    ).properties(title='Distribution of Orders per Customer')
    ```
    """)
    return


# ── CONCEPT 14 ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 14. Boxplot

    **What it is:** A chart that summarizes a distribution using **five statistics**:
    minimum, Q1 (25th percentile), median (50th percentile), Q3 (75th percentile), and maximum.
    Points beyond the whiskers are plotted individually as potential outliers.

    **Used for:** Identifying the spread, skewness, and outliers in a numerical variable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    import seaborn as sns

    # Seaborn boxplot
    sns.boxplot(x=freq_customers.values)
    ```

    Or using Altair:

    ```python
    import altair as alt

    boxplot = alt.Chart(
        bakery.groupby('customer_id').order_id.size().reset_index(name='order_count')
    ).mark_boxplot().encode(
        y='order_count:Q'
    ).properties(title='Boxplot of Orders per Customer')
    ```
    """)
    return


# ── CONCEPT 15 ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 15. Interquartile Range (IQR)

    **What it is:** The difference between the **75th percentile (Q3)** and the
    **25th percentile (Q1)** of a dataset. It represents the middle 50% of the data.

    **Used for:** Measuring the spread of data and, combined with fences, identifying outliers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    Q1 = bakery.groupby('order_date').size().quantile(q=0.25)
    Q3 = bakery.groupby('order_date').size().quantile(q=0.75)
    IQR = Q3 - Q1
    print('IQR:', IQR)
    ```
    """)
    return


# ── CONCEPT 16 ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 16. Lower and Upper Fences (Outlier Detection)

    **What it is:** Boundaries calculated as **1.5× the IQR** below Q1 (lower fence) and above
    Q3 (upper fence). Values outside these fences are considered outliers.

    **Used for:** Determining what counts as an unusual or extreme value in the dataset.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    Q1 = bakery.groupby('order_date').size().quantile(q=0.25)
    Q3 = bakery.groupby('order_date').size().quantile(q=0.75)

    LF = Q1 - (1.5 * (Q3 - Q1))   # Lower fence
    UF = Q3 + (1.5 * (Q3 - Q1))   # Upper fence

    print('Lower fence:', LF, ' Upper fence:', UF)
    # Result: expected daily sales range is 53–101
    ```
    """)
    return


# ── CONCEPT 17 ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 17. Bimodal Distribution

    **What it is:** A distribution that has **two distinct peaks (modes)** rather than one.
    It often signals that there are two underlying subgroups or behaviors in the data.

    **Used for:** Detecting that a single average may not fully represent the data, and that
    there may be two typical "states" for a variable.

    > **From the notebook:** The daily sales histogram showed a slightly bimodal distribution,
    > suggesting that a typical day at HoneyBee Sweet Shop is more likely to have ~71 or ~83
    > sales than exactly the median of 77.
    """)
    return


# ── CONCEPT 18 ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 18. Altair (`alt`) — Interactive Charting

    **What it is:** A Python **declarative visualization library** based on the Vega-Lite grammar.
    Charts are defined by mapping data columns to visual properties (encodings).

    **Used for:** Creating interactive histograms and boxplots inside the Marimo notebook environment.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    import altair as alt

    # Enable vegafusion transformer for large datasets
    alt.data_transformers.enable("vegafusion")

    hist = alt.Chart(
        bakery.groupby('customer_id').order_id.size().reset_index(name='order_count')
    ).mark_bar().encode(
        x=alt.X('order_count:Q', bin=alt.Bin(maxbins=20)),
        y='count()'
    ).properties(title='Distribution of Orders per Customer')

    hist
    ```
    """)
    return


# ── CONCEPT 19 ────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 19. Marimo (`mo`) — Reactive Notebook Framework

    **What it is:** A Python notebook framework where each cell is a pure function.
    The `mo` object provides UI components such as:

    - `mo.md()` — render markdown text
    - `mo.ui.dataframe()` — interactive table viewer
    - `mo.ui.altair_chart()` — interactive chart with selection support
    - `mo.vstack()` / `mo.hstack()` — stack UI elements vertically or horizontally

    **Used for:** Displaying formatted markdown explanations, rendering interactive charts,
    and creating reactive data exploration interfaces within the notebook.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```python
    import marimo as mo

    # Render markdown text
    mo.md("## Section Title")

    # Interactive dataframe explorer
    mo.ui.dataframe(bakery)

    # Interactive Altair chart with click-to-filter selection
    chart = mo.ui.altair_chart(hist, chart_selection=True, legend_selection=False)

    # Stack chart above a reactive data table
    mo.vstack([chart, mo.ui.table(chart.value)])
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    *End of concepts reference guide.*
    """)
    return


if __name__ == "__main__":
    app.run()
