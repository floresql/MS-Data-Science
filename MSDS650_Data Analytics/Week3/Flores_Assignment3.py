# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.3",
#     "pandas>=3.0.1",
#     "scikit-learn>=1.8.0",
#     "seaborn>=0.13.2",
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
    # Week 3 Assignment


    ## Supermarket Sales, Exploratory Data Analysis

    ---

    ## Questions

    1. **Q1: Product performance:** Which product lines generate the most revenue?
    2. **Q2: Peak demand:** When is the store busiest, and is it driven by volume or spend?
    3. **Q3: Customer segmentation:** Do gender or membership affect spending patterns?
    4. **Q4: Branch equity:** Are the three branches performing comparably?
    5. **Q5: Rating drivers:** What, if anything, predicts a high satisfaction rating?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 1 — Describing the Data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Libraries
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set()
    return pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Standard imports, pandas for data handling, numpy for math, matplotlib and seaborn for visualisation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Load the dataset
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('supermarket_sales.csv')
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We load the dataset into a pandas DataFrame. It gives us a first look at the raw data, the column names, the types of values, and the general shape.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Check the type
    """)
    return


@app.cell
def _(df):
    type(df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Confirming we have a pandas DataFrame. This tells us which methods and functions we can use.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Check the shape
    """)
    return


@app.cell
def _(df):
    df.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The dataset has **1,000 rows** (one transaction each) and **17 columns** (features). This is a manageable size, no sampling is needed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### First five rows
    """)
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A quick visual scan of the raw data. We can already see that `Tax 5%`, `cogs`, `Total`, and `gross income` look mathematically related.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data types and null counts
    """)
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `info()` tells us three important things at once:
    - **Data types** - 7 object (string/categorical) columns, 7 float, 1 int.
    - **Non-null counts** - all 1,000 rows show 1000 non-null for every column, meaning **zero missing values**.
    - **Memory usage** - small dataset, no performance concerns.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Statistical summary
    """)
    return


@app.cell
def _(df):
    df.describe().T
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The `.T` transposes the table (swaps rows and columns) for easier reading.

    Key observations:
    - `Unit price` ranges $10–$100 with mean ~$55.67, roughly uniform across the price spectrum.
    - `Quantity` is 1–10 with mean 5.51, also pretty uniform.
    - `gross margin percentage` has **std = 0** It is the exact same value (4.76%) in every row. This column carries no analytical information and will be dropped.
    - `Rating` minimum is 4.0, no transaction scored below 4, suggesting a possible data collection floor effect.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Unique values per categorical column
    """)
    return


@app.cell
def _(df):
    cats = ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']
    for col in cats:
        print(f'{col}: {df[col].unique().tolist()}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This confirms the cardinality of each categorical feature:
    - Branch (A, B, C) maps **one-to-one** with City (Yangon, Mandalay, Naypyitaw), `City` is redundant.
    - Customer type and Gender are both binary.
    - 6 product lines and 3 payment methods.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Date range — confirmed from the data
    """)
    return


@app.cell
def _(df):
    print(df['Date'].min())
    print(df['Date'].max())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Transactions span **January 1 to March 30, 2019**, a 3-month window.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Verify the derived columns
    """)
    return


@app.cell
def _(df):
    print('Tax 5% == cogs x 0.05:    ', (abs(df['Tax 5%'] - df['cogs'] * 0.05) < 0.01).all())
    print('Total == cogs + Tax 5%:   ', (abs(df['Total'] - (df['cogs'] + df['Tax 5%'])) < 0.01).all())
    print('gross income == Tax 5%:   ', (abs(df['gross income'] - df['Tax 5%']) < 0.01).all())
    print('gross margin % unique values:', df['gross margin percentage'].nunique())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All four derived column relationships are confirmed mathematically:
    - `Tax 5%` = `cogs × 0.05` always.
    - `Total` = `cogs + Tax 5%` always.
    - `gross income` is **identical** to `Tax 5%`, a perfect duplicate.
    - `gross margin percentage` has only **1 unique value** constant, zero variance.

    These columns add no independent information and will be dropped in Section 2.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Section 2 — Data Cleaning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Check for missing values
    """)
    return


@app.cell
def _(df):
    df.isnull().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Zero missing values** across all 17 columns. This is consistent with data from a point-of-sale system that enforces completeness at entry. Every field must be filled before a transaction is committed. No imputation or row removal is needed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Check for duplicate rows
    """)
    return


@app.cell
def _(df):
    df.duplicated().any()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    No duplicate rows. Each `Invoice ID` represents a unique transaction.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Check unique values per column & spot low-variance columns
    """)
    return


@app.cell
def _(df):
    df.nunique()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `nunique()` counts distinct values per column. `gross margin percentage` shows 1, confirming it is a constant with zero variance. It gets dropped below.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Boxplot: Check for outliers
    """)
    return


@app.cell
def _(df):
    df.boxplot(['Unit price', 'Quantity', 'Rating'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The boxplot shows:
    - `Unit price` and `Quantity` are clean, symmetric with no extreme outliers.
    - `Rating` has a visible floor at 4.0 but no extreme high outliers.
    - All three look analytically healthy.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Boxplot: Total on its own scale
    """)
    return


@app.cell
def _(df):
    df.boxplot(['Total'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `Total` has a few points above the upper whisker. The IQR method flags these as outliers. However, `Total = Unit price × Quantity × 1.05`. A $99 item bought 10 times legitimately produces ~$1,042. These are **real high-value transactions, not errors**. Decision: retain all 1,000 rows.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Drop redundant and zero-variance columns
    """)
    return


@app.cell
def _(df):
    df.drop(columns=['gross margin percentage', 'gross income', 'City'], inplace=True)
    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Three columns removed:

    | Column | Reason |
    |--------|--------|
    | `gross margin percentage` | Constant 4.76%, zero variance |
    | `gross income` | Identical to `Tax 5%`, duplicate |
    | `City` | 1-to-1 with `Branch`, redundant |

    The cleaned dataset retains **1,000 rows × 14 columns**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Parse date and extract Hour and Month
    """)
    return


@app.cell
def _(df, pd):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
    df['Month'] = df['Date'].dt.month
    df[['Date', 'Time', 'Hour', 'Month']].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We parse `Date` into a proper datetime, then extract `Hour` (integer 10–20) and `Month` (1–3) so we can analyse temporal patterns in Sections 3 and 4.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Section 3 — Feature Selection & Relationship Analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Revenue by product line
    """)
    return


@app.cell
def _(df, plt):
    df.groupby('Product line')['Total'].sum().sort_values().plot(kind='barh')
    plt.xlabel('Total Revenue ($)')
    plt.title('Total Revenue by Product Line')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Answer to Q1:** Food and beverages leads at ~$56,145 but all six product lines fall within a narrow 15% band. No single category dominates. The weakest performer, Health and beauty, is the most actionable target for improvement.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Transaction count by hour
    """)
    return


@app.cell
def _(df, plt):
    df.groupby('Hour')['Total'].count().plot(kind='bar')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Transactions')
    plt.title('Transaction Count by Hour')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Transaction volume peaks sharply at **19:00** with 113 transactions, the clear busiest hour of the day.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Revenue by hour
    """)
    return


@app.cell
def _(df, plt):
    df.groupby('Hour')['Total'].sum().plot(kind='bar')
    plt.xlabel('Hour of Day')
    plt.ylabel('Revenue ($)')
    plt.title('Total Revenue by Hour')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Answer to Q2:** Revenue mirrors the transaction count peak. 19:00 generates ~$39,700, nearly 62% more than the quietest hour (20:00 at ~$22,970). The 13:00 lunch hour is a secondary peak. Staffing and restocking should focus on the evening rush.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Revenue by month
    """)
    return


@app.cell
def _(df, plt):
    df.groupby('Month')['Total'].sum().plot(kind='bar')
    plt.xlabel('Month')
    plt.ylabel('Revenue ($)')
    plt.title('Total Revenue by Month')
    plt.xticks([0, 1, 2], ['January', 'February', 'March'], rotation=0)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    February shows a clear dip (~$97,219) vs January (~$116,292) and March (~$109,456). Even adjusting for fewer days, the daily average remains lower, a seasonal pattern worth investigating.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Branch revenue
    """)
    return


@app.cell
def _(df, plt):
    df.groupby('Branch')['Total'].sum().plot(kind='bar')
    plt.ylabel('Total Revenue ($)')
    plt.title('Total Revenue by Branch')
    plt.xticks(rotation=0)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Answer to Q4:** All three branches are within 4% of each other in revenue. Branch C (Naypyitaw) leads narrowly, suggesting consistent operational standards across locations.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Branch average rating
    """)
    return


@app.cell
def _(df, plt):
    df.groupby('Branch')['Rating'].mean().plot(kind='bar')
    plt.ylabel('Average Rating')
    plt.title('Average Customer Rating by Branch')
    plt.xticks(rotation=0)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Branch C also leads in average rating (7.07) while Branch B trails at 6.82. The differences are small but Branch B may warrant closer attention.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Gender vs product line — mean spend
    """)
    return


@app.cell
def _(df, plt):
    df.pivot_table('Total', 'Gender', 'Product line', aggfunc='mean').T.plot(kind='bar')
    plt.ylabel('Mean Transaction ($)')
    plt.title('Mean Spend by Gender and Product Line')
    plt.xticks(rotation=25)
    plt.legend(title='Gender')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Answer to Q3:** Gender shapes *which* products customers buy, not *how much* overall:
    - **Female** customers significantly outspend males in Home and lifestyle and Food and beverages.
    - **Male** customers outspend females in Health and beauty and Sports and travel.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Payment method distribution
    """)
    return


@app.cell
def _(df, plt):
    df['Payment'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Payment Method Distribution')
    plt.ylabel('')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All three payment methods are used at nearly equal frequency. Ewallet (34.5%), Cash (34.4%), Credit card (31.1%). No single method dominates.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Method 1 — Pearson Correlation Matrix
    """)
    return


@app.cell
def _(df):
    corrmat = df.corr(numeric_only=True)
    corrmat
    return (corrmat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The raw correlation matrix is hard to interpret as a table. A heatmap is much clearer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Correlation heatmap
    """)
    return


@app.cell
def _(corrmat, plt, sns):
    _f, _ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corrmat, vmax=0.8, square=True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The pattern is visible but let's add the actual numbers for precision.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Correlation heatmap with values
    """)
    return


@app.cell
def _(corrmat, plt, sns):
    _hm = sns.heatmap(corrmat, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10})
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Key findings:**
    - `Quantity` (r = 0.71) and `Unit price` (r = 0.63) both strongly predict `Total`.
    - `Unit price` and `Quantity` are nearly **uncorrelated with each other** (r = 0.011).
    - **`Rating` is essentially uncorrelated with everything** (r ≈ −0.04 with Total). Spend does not predict satisfaction.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Pairplot all feature relationships at once
    """)
    return


@app.cell
def _(df, plt, sns):
    sns.pairplot(df[['Unit price', 'Quantity', 'Total', 'Rating']])
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The fan-shaped scatter between `Unit price` and `Total` reflects the multiplicative relationship. The flat clouds involving `Rating` visually confirm what the heatmap showed. No linear relationship between rating and any financial variable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Method 2 — Principal Component Analysis (PCA)
    """)
    return


@app.cell
def _(df, pd):
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA

    features = df[['Unit price', 'Quantity', 'Total', 'Rating', 'Tax 5%', 'cogs']]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    pca = PCA()
    pca.fit(scaled)

    pd.Series(pca.explained_variance_ratio_ * 100,
              index=[f'PC{i}' for i in range(1, len(features.columns)+1)],
              name='Explained Variance %')
    return features, pca


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **PC1 alone explains 65.4%** of variance, dominated by `Total`, `Tax 5%`, and `cogs`. **PC2 and PC3** (~16.5% each) capture the independent `Quantity` and `Unit price` dimensions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Cumulative explained variance
    """)
    return


@app.cell
def _(features, pca, pd):
    explained = pca.explained_variance_ratio_ * 100
    pd.Series(explained.cumsum(),
              index=[f'PC{i}' for i in range(1, len(features.columns)+1)],
              name='Cumulative Variance %')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **3 components capture 98.6% of all variance.** The 6-dimensional numeric space can be reduced to 3 dimensions with virtually no information loss.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Section 4 — Insights & Findings
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rating vs Total spend
    """)
    return


@app.cell
def _(df, plt, sns):
    sns.scatterplot(data=df, x='Total', y='Rating')
    plt.title('Customer Rating vs Transaction Total')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The flat, structureless cloud confirms the heatmap. No meaningful relationship between how much a customer spends and how satisfied they report being.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rating vs Unit price
    """)
    return


@app.cell
def _(df, plt, sns):
    sns.scatterplot(data=df, x='Unit price', y='Rating')
    plt.title('Customer Rating vs Unit Price')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Same result for unit price, satisfaction is not driven by item cost.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rating vs Quantity
    """)
    return


@app.cell
def _(df, plt, sns):
    sns.scatterplot(data=df, x='Quantity', y='Rating')
    plt.title('Customer Rating vs Quantity')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Answer to Q5:** All three scatter plots show a flat cloud. Satisfaction is driven by **intangible service factors**. Staff, wait times, product availability, not transaction size.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Member vs Normal customer spend
    """)
    return


@app.cell
def _(df):
    df.groupby('Customer type')['Total'].describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Members and Normal customers have nearly identical average spend ($327.79 vs $318.12) and similar transaction counts (501 vs 499). The loyalty programme does not drive meaningfully higher basket sizes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rating distribution
    """)
    return


@app.cell
def _(df, plt):
    df['Rating'].plot(kind='hist', bins=15)
    plt.xlabel('Customer Rating')
    plt.title('Distribution of Customer Satisfaction Ratings')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The distribution is remarkably **flat and uniform** from 4.0 to 10.0, not the typical bell curve. The hard floor at 4.0 may indicate a data collection issue where deeply dissatisfied customers do not complete the survey.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Section 5 (Bonus) — Feature Engineering
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Motivation — Unit price and Quantity are independent
    """)
    return


@app.cell
def _(df, plt, sns):
    sns.scatterplot(data=df, x='Unit price', y='Quantity')
    plt.title('Unit Price vs Quantity — Nearly Uncorrelated (r = 0.011)')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Customers buying expensive items don't buy more of them, and vice versa. These are genuinely independent purchasing decisions, which means `Total` conflates two distinct revenue effects. We need a normalised metric to separate them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create: Revenue Per Unit = Total / Quantity
    """)
    return


@app.cell
def _(df):
    df['revenue_per_unit'] = df['Total'] / df['Quantity']
    df['revenue_per_unit'].describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `revenue_per_unit` isolates the per-item value of each transaction, independent of quantity purchased.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Revenue per unit by product line
    """)
    return


@app.cell
def _(df, plt):
    df.groupby('Product line')['revenue_per_unit'].mean().sort_values().plot(kind='barh')
    plt.xlabel('Average Revenue Per Unit ($)')
    plt.title('Engineered Feature: Revenue Per Unit by Product Line')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Finding:** Fashion accessories ($60.01/unit) and Sports and travel ($59.84/unit) command the highest per-unit revenue. Electronic accessories has the **lowest per-item value ($56.23)** despite being the third-highest in total revenue. It compensates through higher quantities per transaction. This insight is **invisible in raw revenue totals**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Additional engineered features
    """)
    return


@app.cell
def _(df, pd):
    # Peak hour flag — proven high-traffic hours
    df['is_peak_hour'] = df['Hour'].isin([13, 19]).astype(int)

    # High-value transaction flag — top ~15%
    df['high_value'] = (df['Total'] > df['Total'].quantile(0.85)).astype(int)

    # Quantity tier — ordinal grouping
    df['qty_tier'] = pd.cut(df['Quantity'], bins=[0, 3, 7, 10],
                             labels=['Low (1-3)', 'Medium (4-7)', 'High (8-10)'])

    df[['is_peak_hour', 'high_value', 'qty_tier', 'revenue_per_unit']].head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    | Feature | Definition | Use Case |
    |---------|-----------|----------|
    | `revenue_per_unit` | Total ÷ Quantity | Decouples price vs volume effects |
    | `is_peak_hour` | 1 if Hour ∈ {13, 19} | Staffing and promotion timing |
    | `high_value` | 1 if Total > 85th percentile | Targeting high-spend customers |
    | `qty_tier` | Low / Medium / High | Segmenting by purchase behaviour |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Final dataset
    """)
    return


@app.cell
def _(df):
    print(f'Final shape: {df.shape}')
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The final dataset is ready for machine learning or further modelling, Redundant features removed, temporal features parsed, and new analytical features added.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Summary

    | Question | Finding |
    |----------|---------|
    | Q1 — Top product line? | Food & Beverages (~$56,145), but all 6 within 15% of each other |
    | Q2 — Peak hour? | 19:00 - 113 transactions, ~$39,700 revenue |
    | Q3 — Gender differences? | Similar total spend; strong product-line preferences by gender |
    | Q4 — Branch equity? | All three branches within 4% of each other in revenue |
    | Q5 — Rating drivers? | Rating is uncorrelated with all financial variables (r ≈ −0.04) |

    **Bonus feature highlight:** `revenue_per_unit = Total / Quantity` reveals that Electronic accessories, despite strong total revenue, has the lowest per-item value, compensating through volume. Invisible in raw totals alone.
    """)
    return


if __name__ == "__main__":
    app.run()
