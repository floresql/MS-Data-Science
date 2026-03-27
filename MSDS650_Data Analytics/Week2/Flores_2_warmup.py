# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "pandas>=3.0.1",
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


@app.cell
def _():
    import subprocess

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Warmup Exercise - Defining and Answering Analytical Questions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As follow-on from week1, this week's warmup exercise will involve developing your own questions about a given dataset and  then answer those questions using python's Pandas library.

    ### Our Dataset

    **Dataset Name::** supermarket_sales.csv <br>
    The growth of supermarkets in most populated cities are increasing and market competitions are also high. The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data.

    |Column Name|Column Description|
    |---|---|
    |Invoice id| Computer generated sales slip invoice identification number|
    |Branch| Branch of supercenter (3 branches are available identified by A, B and C)|
    |City| Location of supercenters|
    |Customer type| Type of customers, recorded by Members for customers using member card and Normal for without member card|
    |Gender| Gender of customer|
    |Product line| General item categorization groups (Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel)|
    |Unit price| Price of each product in dollars|
    |Quantity| Number of products purchased by customer|
    |Tax| 5% tax fee for customer buying|
    |Total| Total price including tax|
    |Date| Date of purchase (Record available from January 2019 to March 2019)|
    |Time| Purchase time (10am to 9pm)|
    |Payment| Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)|
    |COGS| Cost of goods sold|
    |Gross margin percentage| Gross margin percentage|
    |Gross income| Gross income|
    |Rating| Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)|
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercise

    ### Define 3 in-depth questions to investigate within this dataset.

    ***Prework:*** Import necessary libraries, look at data make up, and sample.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    First step is alway to import necessary libraries
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    import seaborn as sns
    import jinja2 

    sns.set_theme(style="whitegrid")
    return plt, sns


@app.cell
def _(mo):
    mo.md(r"""
    Now lets read in the file and use some typical techniques to look at the makeup of the data.
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('supermarket_sales.csv')

    df.shape
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""
    The shape method shows us that there are 1,000 records and 17 columns.
    Let's take a look at those columns.
    """)
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(mo):
    mo.md(r"""
    Now that we know what columns are in the data, lets dig a little deeper and get some details like data types.
    """)
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(mo):
    mo.md(r"""
    Finally, lets look at a sample of the data.
    """)
    return


@app.cell
def _(df):
    df.head(10)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### ***Question 1:*** Does customer type (Member vs. Normal) drive higher spending and customer satisfaction?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Having looked at the data, we can now select a subset of columns from the DataFrame that are relevant to question 1.
    """)
    return


@app.cell
def _(df):
    cols = ['Customer type', 'Gender', 'Product line',
            'Quantity', 'Total', 'gross income', 'Rating']

    q1_df = df[cols].copy()
    q1_df.head(10)
    return (q1_df,)


@app.cell
def _(mo):
    mo.md(r"""
    Using `groupby()` to split the data into Members and Normal customers, then `agg()` to calculate summary statistics for each group.
    """)
    return


@app.cell
def _(q1_df):
    q1_df.groupby('Customer type').agg(
        Transactions  = ('Total',    'count'),
        Avg_Spend     = ('Total',    'mean'),
        Median_Spend  = ('Total',    'median'),
        Total_Revenue = ('Total',    'sum'),
        Avg_Quantity  = ('Quantity', 'mean'),
        Avg_Rating    = ('Rating',   'mean'),
    ).round(2)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Now we can use `style.format()` to make things easier to read; add dollar signs and highlight the highest values in green
    """)
    return


@app.cell
def _(q1_df):
    (q1_df.groupby('Customer type')
          .agg({'Total':    ['mean', 'median', 'sum'],
                'Quantity': ['mean'],
                'Rating':   ['mean']})
          .style.format('${0:,.2f}', subset=['Total'])
          .highlight_max(color='green')
          .highlight_min(color='red'))
    return


@app.cell
def _(mo):
    mo.md(r"""
    We can use a **lambda function** to label each transaction as Low, Medium, or High spend.
    """)
    return


@app.cell
def _(q1_df):
    classify = lambda x: 'High' if x >= 500 else ('Medium' if x >= 200 else 'Low')
    q1_df['Spend Tier'] = q1_df['Total'].apply(classify)

    q1_df.groupby(['Customer type', 'Spend Tier']).size().unstack('Spend Tier').fillna(0).astype(int)
    return


@app.cell
def _(mo):
    mo.md(r"""
    And now we can visualize each of the three measures, making it much easier to spot patterns.
    """)
    return


@app.cell
def _(plt, q1_df):
    fig1, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig1.suptitle("Member vs. Normal — Spending & Satisfaction", fontsize=14, fontweight='bold')

    palette = {'Member': '#4C72B0', 'Normal': '#DD8452'}

    # Average spend
    avg_spend = q1_df.groupby('Customer type')['Total'].mean().reset_index()
    axes[0].bar(avg_spend['Customer type'], avg_spend['Total'],
                color=[palette[c] for c in avg_spend['Customer type']])
    axes[0].set_title('Avg. Transaction Total ($)')
    axes[0].set_ylabel('Mean ($)')
    for a, v in enumerate(avg_spend['Total']):
        axes[0].text(a, v + 2, f'${v:.2f}', ha='center', fontweight='bold')

    # Average quantity
    avg_qty = q1_df.groupby('Customer type')['Quantity'].mean().reset_index()
    axes[1].bar(avg_qty['Customer type'], avg_qty['Quantity'],
                color=[palette[c] for c in avg_qty['Customer type']])
    axes[1].set_title('Avg. Quantity per Transaction')
    axes[1].set_ylabel('Items')
    for a, v in enumerate(avg_qty['Quantity']):
        axes[1].text(a, v + 0.05, f'{v:.2f}', ha='center', fontweight='bold')

    # Average rating
    avg_rating = q1_df.groupby('Customer type')['Rating'].mean().reset_index()
    axes[2].bar(avg_rating['Customer type'], avg_rating['Rating'],
                color=[palette[c] for c in avg_rating['Customer type']])
    axes[2].set_title('Avg. Customer Rating (out of 10)')
    axes[2].set_ylabel('Rating')
    axes[2].set_ylim(0, 10)
    for a, v in enumerate(avg_rating['Rating']):
        axes[2].text(a, v + 0.1, f'{v:.2f}', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.gca()
    return (v,)


@app.cell
def _(mo):
    mo.md(r"""
    Now let's look at the spread of spend using box plots, these show not just the average but the full distribution:
    """)
    return


@app.cell
def _(plt, q1_df, sns):
    fig2, axes2 = plt.subplots(1, 2, figsize=(12, 5))
    fig2.suptitle("Spend & Rating Distribution", fontsize=13, fontweight='bold')

    sns.boxplot(data=q1_df, x='Customer type', y='Total',
                hue='Customer type', palette={'Member': '#4C72B0', 'Normal': '#DD8452'},
                legend=False, ax=axes2[0])
    axes2[0].set_title('Transaction Total ($)')
    axes2[0].set_xlabel('')

    sns.boxplot(data=q1_df, x='Customer type', y='Rating',
                hue='Customer type', palette={'Member': '#4C72B0', 'Normal': '#DD8452'},
                legend=False, ax=axes2[1])
    axes2[1].set_title('Customer Rating')
    axes2[1].set_xlabel('')

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### ***Conclusion:***
    The differences between Members and Normal customers are very small across all three measures. Members spend slightly more on average (+$9.67), buy very slightly more items, but actually rate their experience *slightly lower* than Normal customers. Based on this analysis, **membership does not appear to drive meaningfully higher spending or satisfaction.**

    &nbsp;

    ---
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### ***Question 2:*** How does time of day and day of week affect transaction volume, basket size, and customer ratings?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    We already imported the libraries before, so lets just read in the csv file into a new dataframe.

    *Note: I just learned Marimo doesn't let you redefine a variable. interesting.*
    """)
    return


@app.cell
def _(pd):
    df2 = pd.read_csv('supermarket_sales.csv')
    df2.info()
    return (df2,)


@app.cell
def _(df2):
    df2.head(10)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Lets keep only the columns we need for question 2.
    """)
    return


@app.cell
def _(df):
    cols2 = ['Date', 'Time', 'Quantity', 'Total', 'Rating']
    q2_df = df[cols2].copy()
    q2_df.head()
    return (q2_df,)


@app.cell
def _(mo):
    mo.md(r"""
    Using the info() method above we could see the date and time columns were strings. We need to convert them to the right format in order to get the correct time of day and day of the week we need to answer our question.
    """)
    return


@app.cell
def _(pd, q2_df):
    # Convert Date and Time from text to datetime format
    q2_df['Date'] = pd.to_datetime(q2_df['Date'])
    q2_df['Time'] = pd.to_datetime(q2_df['Time'], format='%H:%M')

    # Extract the hour (e.g. 13 for 1pm) and day name (e.g. 'Monday')
    q2_df['Hour']        = q2_df['Time'].dt.hour
    q2_df['Day_of_Week'] = q2_df['Date'].dt.day_name()

    q2_df.head()
    return


@app.cell
def _(mo):
    mo.md(r"""
    Lets look at the data and see what time and days the store is open.
    """)
    return


@app.cell
def _(q2_df):
    print("Hour range:", q2_df['Hour'].min(), "to", q2_df['Hour'].max())
    print("Days in dataset:", q2_df['Day_of_Week'].unique().tolist())
    return


@app.cell
def _(mo):
    mo.md(r"""
    We can see the store is open from 10am to 8pm. To make things a little easier to read, lets make that Morning, Afternoon, and Evening.
    """)
    return


@app.cell
def _(q2_df):
    classify_tod = lambda h: 'Morning (10–12)' if h < 13 else ('Afternoon (13–17)' if h < 18 else 'Evening (18–20)')
    q2_df['Time of Day'] = q2_df['Hour'].apply(classify_tod)

    # Preview the new column
    q2_df[['Hour', 'Time of Day']].drop_duplicates().sort_values('Hour')
    return


@app.cell
def _(mo):
    mo.md(r"""
    Now we can groupby our new time of day column and see the average spend, quantity, and rating for each.
    """)
    return


@app.cell
def _(q2_df):
    tod_order = ['Morning (10–12)', 'Afternoon (13–17)', 'Evening (18–20)']

    tod_summary = (q2_df.groupby('Time of Day')
                        .agg(
                            Transactions = ('Total',    'count'),
                            Avg_Spend    = ('Total',    'mean'),
                            Avg_Quantity = ('Quantity', 'mean'),
                            Avg_Rating   = ('Rating',   'mean'),
                        )
                        .reindex(tod_order)
                        .round(2))

    tod_summary
    return (tod_summary,)


@app.cell
def _(mo):
    mo.md(r"""
    Now lets do the same thing by day.
    """)
    return


@app.cell
def _(q2_df):
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    day_summary = (q2_df.groupby('Day_of_Week')
                        .agg(
                            Transactions = ('Total',    'count'),
                            Avg_Spend    = ('Total',    'mean'),
                            Avg_Quantity = ('Quantity', 'mean'),
                            Avg_Rating   = ('Rating',   'mean'),
                        )
                        .round(2))

    day_summary
    return (day_summary,)


@app.cell
def _(mo):
    mo.md(r"""
    Now we can visual each measure, first by time of day.

    *Note: I'm not sure I like this Marimo 'feature' where I can't redefine variables.*
    """)
    return


@app.cell
def _(plt, tod_summary, v):
    fig3, axes3 = plt.subplots(1, 3, figsize=(14, 5))
    fig3.suptitle("Time of Day — Volume, Basket Size & Ratings", fontsize=14, fontweight='bold')

    colors = ['#5aA0D0', '#F28E2B', '#76B7B2']
    tod_labels = tod_summary.index.tolist()

    # Transactions
    axes3[0].bar(tod_labels, tod_summary['Transactions'], color=colors)
    axes3[0].set_title('Transaction Volume')
    axes3[0].set_ylabel('Number of Transactions')
    for i, x in enumerate(tod_summary['Transactions']):
        axes3[0].text(i, x + 1, str(v), ha='center', fontweight='bold')

    # Avg Quantity
    axes3[1].bar(tod_labels, tod_summary['Avg_Quantity'], color=colors)
    axes3[1].set_title('Avg. Basket Size (Items)')
    axes3[1].set_ylabel('Mean Quantity')
    for i, x in enumerate(tod_summary['Avg_Quantity']):
        axes3[1].text(i, x + 0.03, f'{v:.2f}', ha='center', fontweight='bold')

    # Avg Rating
    axes3[2].bar(tod_labels, tod_summary['Avg_Rating'], color=colors)
    axes3[2].set_title('Avg. Customer Rating')
    axes3[2].set_ylabel('Mean Rating (out of 10)')
    axes3[2].set_ylim(0, 10)
    for i, x in enumerate(tod_summary['Avg_Rating']):
        axes3[2].text(i, x + 0.1, f'{v:.2f}', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    Now lets look at it by day of week.

    *Note: I **am** sure I don't like this Marimo 'feature' where I can't redefine variables!*
    """)
    return


@app.cell
def _(day_summary, plt, v):
    fig4, axes4 = plt.subplots(1, 3, figsize=(16, 5))
    fig4.suptitle("Day of Week — Volume, Basket Size & Ratings", fontsize=14, fontweight='bold')

    day_labels = day_summary.index.tolist()
    bar_color  = '#4C72B0'

    # Transactions
    axes4[0].bar(day_labels, day_summary['Transactions'], color=bar_color)
    axes4[0].set_title('Transaction Volume')
    axes4[0].set_ylabel('Number of Transactions')
    axes4[0].tick_params(axis='x', rotation=30)
    for i2, v2 in enumerate(day_summary['Transactions']):
        axes4[0].text(i2, v2 + 1, str(v), ha='center', fontsize=8, fontweight='bold')

    # Avg Quantity
    axes4[1].bar(day_labels, day_summary['Avg_Quantity'], color=bar_color)
    axes4[1].set_title('Avg. Basket Size (Items)')
    axes4[1].set_ylabel('Mean Quantity')
    axes4[1].tick_params(axis='x', rotation=30)
    for i2, v2 in enumerate(day_summary['Avg_Quantity']):
        axes4[1].text(i2, v2 + 0.03, f'{v:.2f}', ha='center', fontsize=8, fontweight='bold')

    # Avg Rating
    axes4[2].bar(day_labels, day_summary['Avg_Rating'], color=bar_color)
    axes4[2].set_title('Avg. Customer Rating')
    axes4[2].set_ylabel('Mean Rating (out of 10)')
    axes4[2].set_ylim(0, 10)
    axes4[2].tick_params(axis='x', rotation=30)
    for i2, v2 in enumerate(day_summary['Avg_Rating']):
        axes4[2].text(i2, v2 + 0.1, f'{v:.2f}', ha='center', fontsize=8, fontweight='bold')

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    And finally we'll look at hourly transaction volume.
    """)
    return


@app.cell
def _(plt, q2_df):
    hourly = q2_df.groupby('Hour').agg(
        Transactions = ('Total',    'count'),
        Avg_Rating   = ('Rating',   'mean'),
    ).round(2)

    fig5, axes5 = plt.subplots(1, 2, figsize=(13, 4))
    fig5.suptitle("Hourly Trends", fontsize=13, fontweight='bold')

    axes5[0].plot(hourly.index, hourly['Transactions'], marker='o', color='#4C72B0', linewidth=2)
    axes5[0].set_title('Transaction Volume by Hour')
    axes5[0].set_xlabel('Hour of Day')
    axes5[0].set_ylabel('Number of Transactions')
    axes5[0].set_xticks(hourly.index)

    axes5[1].plot(hourly.index, hourly['Avg_Rating'], marker='o', color='#DD8452', linewidth=2)
    axes5[1].set_title('Avg. Rating by Hour')
    axes5[1].set_xlabel('Hour of Day')
    axes5[1].set_ylabel('Mean Rating')
    axes5[1].set_ylim(5, 9)
    axes5[1].set_xticks(hourly.index)

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### ***Conclusion:***

    **Key Findings:**

    - **Afternoon is the busiest period** nearly 44% of all transactions happen between 1pm and 5pm, and basket sizes are slightly larger too.
    - **Morning customers rate their experience highest** despite fewer transactions, morning shoppers give an average rating of 7.07 vs. 6.93 in the afternoon.
    - **Saturday drives the most foot traffic**, but Sunday customers buy the most items per visit on average.
    - **Monday is the quietest day** but has the highest average rating.
    - **Ratings are relatively stable across the day and week** (all between 6.8 and 7.2), meaning time alone is not a strong predictor of satisfaction.

    &nbsp;

    ---
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### ***Question 3:*** How does payment method interact with gender, product line, and average spend?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    We'll start by keeping the columns needed for this question.
    """)
    return


@app.cell
def _(df):
    pay_cols = ['Payment', 'Gender', 'Product line', 'Quantity', 'Total', 'Rating']
    q3_df = df[pay_cols].copy()
    q3_df.head()
    return (q3_df,)


@app.cell
def _(mo):
    mo.md(r"""
    Lets start by looking at payment methods and how they compare to each other.
    """)
    return


@app.cell
def _(q3_df):
    pay_summary = q3_df.groupby('Payment').agg(
        Transactions = ('Total',    'count'),
        Avg_Spend    = ('Total',    'mean'),
        Avg_Quantity = ('Quantity', 'mean'),
        Avg_Rating   = ('Rating',   'mean'),
    ).round(2)

    pay_summary
    return (pay_summary,)


@app.cell
def _(mo):
    mo.md(r"""
    Now we can break that out by gender.
    """)
    return


@app.cell
def _(q3_df):
    # Count of transactions: rows = Payment, columns = Gender
    pay_gender_count = (q3_df.groupby(['Payment', 'Gender'])
                              .size()
                              .unstack('Gender'))

    pay_gender_count
    return (pay_gender_count,)


@app.cell
def _(mo):
    mo.md(r"""
    Looking at the percentage of the total paints a clearer picture, so lets do that.
    """)
    return


@app.cell
def _(pay_gender_count):
    # Convert counts to row percentages
    pay_gender_pct = pay_gender_count.apply(lambda row: (row / row.sum() * 100).round(1), axis=1)
    pay_gender_pct.columns = [f'{c} (%)' for c in pay_gender_pct.columns]

    pay_gender_pct
    return


@app.cell
def _(mo):
    mo.md(r"""
    Now let's see whether spend differs across the combination of payment method and gender.
    """)
    return


@app.cell
def _(q3_df):
    pay_gender_spend = (q3_df.groupby(['Payment', 'Gender'])['Total']
                              .mean()
                              .unstack('Gender')
                              .round(2))

    (pay_gender_spend.style
                     .format('${:,.2f}')
                     .highlight_max(color='green')
                     .highlight_min(color='red'))
    return


@app.cell
def _(mo):
    mo.md(r"""
    Let's now count how many transactions each payment method has per product line, then look at average spend per combination.
    """)
    return


@app.cell
def _(q3_df):
    # Transaction counts: Payment × Product line
    pay_product_count = (q3_df.groupby(['Payment', 'Product line'])
                               .size()
                               .unstack('Product line'))

    pay_product_count
    return


@app.cell
def _(q3_df):
    pay_product_spend = (q3_df.groupby(['Payment', 'Product line'])['Total']
                               .mean()
                               .unstack('Product line')
                               .round(2))

    (pay_product_spend.style
                      .format('${:,.2f}')
                      .highlight_max(color='green')
                      .highlight_min(color='red'))
    return


@app.cell
def _(mo):
    mo.md(r"""
    Lets look at this data in some bar charts to make it easier to see.
    """)
    return


@app.cell
def _(pay_summary, plt, v):
    pay_palette = ['#4C72B0', '#DD8452', '#59A14F']
    pay_labels  = pay_summary.index.tolist()

    fig_pay, axes_pay = plt.subplots(1, 3, figsize=(14, 5))
    fig_pay.suptitle("Payment Method — Overview", fontsize=14, fontweight='bold')

    # Transactions
    axes_pay[0].bar(pay_labels, pay_summary['Transactions'], color=pay_palette)
    axes_pay[0].set_title('Transaction Volume')
    axes_pay[0].set_ylabel('Number of Transactions')
    for ii, vv in enumerate(pay_summary['Transactions']):
        axes_pay[0].text(ii, vv + 1, str(v), ha='center', fontweight='bold')

    # Avg Spend
    axes_pay[1].bar(pay_labels, pay_summary['Avg_Spend'], color=pay_palette)
    axes_pay[1].set_title('Avg. Transaction Total ($)')
    axes_pay[1].set_ylabel('Mean ($)')
    for ii, vv in enumerate(pay_summary['Avg_Spend']):
        axes_pay[1].text(ii, vv + 2, f'${v:.2f}', ha='center', fontweight='bold')

    # Avg Rating
    axes_pay[2].bar(pay_labels, pay_summary['Avg_Rating'], color=pay_palette)
    axes_pay[2].set_title('Avg. Customer Rating')
    axes_pay[2].set_ylabel('Mean Rating (out of 10)')
    axes_pay[2].set_ylim(0, 10)
    for ii, vv in enumerate(pay_summary['Avg_Rating']):
        axes_pay[2].text(ii, vv + 0.1, f'{v:.2f}', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    Now lets look at gender side by side.
    """)
    return


@app.cell
def _(plt, q3_df, sns):
    pay_gender_avg = (q3_df.groupby(['Payment', 'Gender'])['Total']
                            .mean()
                            .reset_index())

    fig_gender, ax_gender = plt.subplots(figsize=(9, 5))
    sns.barplot(data=pay_gender_avg, x='Payment', y='Total', hue='Gender',
                palette={'Female': '#E377C2', 'Male': '#4C72B0'}, ax=ax_gender)
    ax_gender.set_title('Avg. Spend by Payment Method & Gender', fontsize=13, fontweight='bold')
    ax_gender.set_xlabel('Payment Method')
    ax_gender.set_ylabel('Mean Transaction Total ($)')
    ax_gender.legend(title='Gender')

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    a **heatmap** is the clearest way to show average spend across all combinations at once.
    """)
    return


@app.cell
def _(plt, q3_df, sns):
    pay_prod_pivot = (q3_df.groupby(['Payment', 'Product line'])['Total']
                            .mean()
                            .unstack('Product line')
                            .round(2))

    fig_heat, ax_heat = plt.subplots(figsize=(11, 4))
    sns.heatmap(pay_prod_pivot, annot=True, fmt='.0f', cmap='YlGnBu',
                linewidths=0.5, ax=ax_heat, cbar_kws={'label': 'Avg Spend ($)'})
    ax_heat.set_title('Avg. Spend ($) by Payment Method × Product Line',
                      fontsize=13, fontweight='bold')
    ax_heat.set_xlabel('Product Line')
    ax_heat.set_ylabel('Payment Method')

    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### ***Conclusion:***

    **Key Findings:**

    Payment method alone is not a strong predictor of spend, the differences across methods are small (less than $8 on average). However, meaningful patterns are seen when gender and product line are combined with payment method, suggesting **customer demographics and product choices are better predictors of how — and how much — people spend** than payment method on its own.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## References

    Anthropic. (2026, March 21). *Pandas data analysis techniques reference from Python notebook.*

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Generative AI chat]. Claude Sonnet 4.6. https://claude.ai/share/b65e24ce-0422-4b95-88f9-2d2cf53e4106

    &nbsp;

    ---
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Appendix: AI-Generated Content

    **Tool:** Claude Sonnet 4.6 (Anthropic)
    **Date:** March 21, 2026
    **Topic:** Pandas Data Analysis Techniques


    ### Prompt Submitted to AI:

    could you make me a list of the techniques demonstrated in 1_defined_analytical_questions.py
    and describe what each one is used for and how it works? put them in numerical order.
    provide the results in a markdown file with code windows for code snippets of each technique



    ### Full-Text AI Response:

    The markdown file covers all **25 techniques** demonstrated in the notebook, in the order
    they appear, each with a code snippet. Here's a quick overview of what's covered:

    1–6: Setup basics — loading CSVs, the interactive viewer, shape, head/tail/sample, column
    names, and `info()`

    7–10: Descriptive stats — `describe()`, histograms, the dropdown widget, and box plots

    11–13: Indexing — `iloc` row/column selection, column access by name, and Python slicing

    14–15: Data cleaning — `drop()` for rows/columns, and identifying/quantifying missing values

    16–17: Transformation — `apply()` with custom functions, and `agg()` for aggregation

    18–19: Grouping — `groupby()` with aggregations, and the `count`/`nunique`/`size` distinctions

    20–21: Advanced Pandas — lambda functions inline with `apply()`, and `style.format()` with
    color highlights

    22–25: Applied analysis — subsetting with `iloc` for a focused question, and grouped `.mean()`
    for comparison


    The full detailed response is contained in the attached markdown file:
    pandas_techniques_reference.md
    """)
    return


if __name__ == "__main__":
    app.run()
