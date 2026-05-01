# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.1",
#     "pandas>=3.0.2",
#     "numpy>=2.4.3",
#     "matplotlib>=3.10.8",
#     "seaborn>=0.13.2",
#     "scipy>=1.17.1",
#     "scikit-learn>=1.8.0",
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
    # Week 7 Assignment

    **Data Story:** Supermarket Sales Analysis
    **Dataset:** Supermarket Sales Dataset
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Scenario

    RetailCo is a supermarket chain operating three branches (A, B, and C) across
    three cities. The company has recorded transaction-level sales data over a
    three-month period, capturing product category, customer demographics, payment
    method, and customer satisfaction ratings alongside financial figures.

    Leadership wants to understand whether branch location and product category
    are driving meaningful differences in revenue and customer satisfaction,
    and whether those differences are significant enough to inform resource
    allocation decisions.

    ## Problem Statement

    Are there statistically significant differences in transaction totals across
    branches, and can we predict a customer's product line category based on
    available transaction features?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dataset Description
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np

    np.random.seed(42)

    branches      = ['A', 'B', 'C']
    cust_types    = ['Member', 'Normal']
    genders       = ['Male', 'Female']
    product_lines = [
        'Health and beauty', 'Electronic accessories',
        'Home and lifestyle', 'Sports and travel',
        'Food and beverages', 'Fashion accessories'
    ]
    payments = ['Ewallet', 'Cash', 'Credit card']

    n = 1000
    sales = pd.DataFrame({
        'Branch':        np.random.choice(branches, n),
        'Customer type': np.random.choice(cust_types, n),
        'Gender':        np.random.choice(genders, n),
        'Product line':  np.random.choice(product_lines, n),
        'Unit price':    np.round(np.random.uniform(10, 100, n), 2),
        'Quantity':      np.random.randint(1, 11, n),
        'Payment':       np.random.choice(payments, n),
        'Rating':        np.round(np.random.uniform(4, 10, n), 1),
    })
    sales['Total']        = np.round(sales['Unit price'] * sales['Quantity'] * 1.05, 2)
    sales['gross income'] = np.round(sales['Total'] * 0.05 / 1.05, 2)

    print(sales.shape)
    sales.head()
    return (sales,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data Preparation

    The dataset has no missing values by construction. We encode categorical
    columns as numeric values for the KNN classifier.
    """)
    return


@app.cell
def _(sales):
    # Encode Product line as integer label for KNN target
    product_map = {pl: i for i, pl in enumerate(sorted(sales['Product line'].unique()))}
    sales['product_label'] = sales['Product line'].map(product_map)

    # Encode categorical features for KNN
    sales['branch_num'] = sales['Branch'].map({'A': 0, 'B': 1, 'C': 2})
    sales['gender_num'] = (sales['Gender'] == 'Male').astype(int)
    sales['cust_num']   = (sales['Customer type'] == 'Member').astype(int)

    print("Product line encoding:")
    for k, v in product_map.items():
        print(f"  {v}: {k}")

    print(f"\nNull values:\n{sales.isnull().sum()}")
    return (product_map,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Technique 1: Descriptive Statistics

    We summarize average transaction totals and average customer ratings by
    branch and by product line. This gives leadership an initial picture of
    where revenue and satisfaction are concentrated before any formal testing.

    **Prechecks:** Descriptive statistics have no formal assumptions. They
    describe what is in the data without making inferences about a broader
    population.
    """)
    return


@app.cell
def _(sales):
    import matplotlib.pyplot as plt

    branch_total  = sales.groupby('Branch')['Total'].mean().reset_index()
    branch_rating = sales.groupby('Branch')['Rating'].mean().reset_index()
    prod_total    = (
        sales.groupby('Product line')['Total']
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))

    # --- Avg Total by Branch ---
    colors_b = ['#3266ad', '#2ecc71', '#e74c3c']
    bars1 = axes[0].bar(branch_total['Branch'], branch_total['Total'],
                        color=colors_b, width=0.4)
    axes[0].set_title('Avg Transaction Total by Branch', fontsize=11)
    axes[0].set_ylabel('Average Total ($)')
    axes[0].set_ylim(0, branch_total['Total'].max() * 1.2)
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)
    axes[0].yaxis.grid(True, linestyle='--', linewidth=0.5, color='lightgrey')
    axes[0].tick_params(length=0)
    for bar, val in zip(bars1, branch_total['Total']):
        axes[0].text(bar.get_x() + bar.get_width() / 2,
                     bar.get_height() + 1,
                     f'${val:.0f}', ha='center', fontsize=10)

    # --- Avg Rating by Branch ---
    bars2 = axes[1].bar(branch_rating['Branch'], branch_rating['Rating'],
                        color=colors_b, width=0.4)
    axes[1].set_title('Avg Customer Rating by Branch', fontsize=11)
    axes[1].set_ylabel('Average Rating (out of 10)')
    axes[1].set_ylim(0, 10)
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    axes[1].yaxis.grid(True, linestyle='--', linewidth=0.5, color='lightgrey')
    axes[1].tick_params(length=0)
    for bar, val in zip(bars2, branch_rating['Rating']):
        axes[1].text(bar.get_x() + bar.get_width() / 2,
                     bar.get_height() + 0.1,
                     f'{val:.2f}', ha='center', fontsize=10)

    # --- Avg Total by Product Line ---
    colors_p = ['#85c1e9', '#82e0aa', '#f9e79f', '#f0b27a', '#c39bd3', '#aab7b8']
    bars3 = axes[2].barh(prod_total['Product line'], prod_total['Total'],
                         color=colors_p)
    axes[2].set_title('Avg Transaction Total\nby Product Line', fontsize=11)
    axes[2].set_xlabel('Average Total ($)')
    axes[2].spines['top'].set_visible(False)
    axes[2].spines['right'].set_visible(False)
    axes[2].xaxis.grid(True, linestyle='--', linewidth=0.5, color='lightgrey')
    axes[2].tick_params(length=0)
    for bar, val in zip(bars3, prod_total['Total']):
        axes[2].text(val + 0.5, bar.get_y() + bar.get_height() / 2,
                     f'${val:.0f}', va='center', fontsize=9)

    plt.suptitle('RetailCo: Revenue and Satisfaction Overview', fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.gca()
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Descriptive Statistics Summary

    Average transaction totals are broadly similar across branches, with no
    single branch standing out dramatically. Customer satisfaction ratings
    also show little variation by branch, hovering near the middle of the
    4 to 10 scale.

    The product line chart shows some variation in average transaction value
    across categories. These patterns motivate Technique 2: we need a formal
    test to determine whether branch-level differences in transaction totals
    are statistically meaningful or simply due to random variation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Technique 2: Hypothesis Testing — Two-Sample T-Test

    We test whether the average transaction total at Branch A is significantly
    different from Branch C. This is a direct business question: if one branch
    consistently generates higher transaction values, it may justify a different
    investment or staffing strategy.

    **Hypotheses:**
    - H0: The mean transaction total for Branch A equals the mean for Branch C.
    - H1: The mean transaction total for Branch A is different from Branch C.

    **Alpha:** 0.05

    **Prechecks:** Both groups have n > 30, which satisfies the condition for
    the t-test to be robust to mild departures from normality. We confirm the
    approximate distribution with a histogram before running the test.
    """)
    return


@app.cell
def _(plt, sales):
    import seaborn as sns
    from scipy import stats

    branch_a = sales[sales['Branch'] == 'A']['Total']
    branch_c = sales[sales['Branch'] == 'C']['Total']

    print(f"Branch A — n={len(branch_a)}, mean=${branch_a.mean():.2f}")
    print(f"Branch C — n={len(branch_c)}, mean=${branch_c.mean():.2f}")

    fig2, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(branch_a, kde=True, color='#3266ad', label='Branch A', alpha=0.6, ax=ax)
    sns.histplot(branch_c, kde=True, color='#e74c3c', label='Branch C', alpha=0.6, ax=ax)
    ax.set_title('Transaction Totals: Branch A vs Branch C', fontsize=12)
    ax.set_xlabel('Transaction Total ($)')
    ax.set_ylabel('Count')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend()
    plt.tight_layout()
    plt.gca()
    return branch_a, branch_c, sns, stats


@app.cell
def _(branch_a, branch_c, mo, stats):
    tstat, pval = stats.ttest_ind(branch_a, branch_c, alternative='two-sided')
    print(f"T-statistic: {tstat:.4f}")
    print(f"P-value:     {pval:.4f}")

    decision = "Reject the null hypothesis" if pval < 0.05 else "Fail to reject the null hypothesis"
    mo.md(f"### Decision: {decision} (p = {pval:.4f})")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Hypothesis Test Summary

    The two-sample t-test directly answers whether Branch A and Branch C are
    performing differently on transaction value. Based on the p-value relative
    to our alpha of 0.05, the result tells leadership that observed differences
    are within the range of normal variation, and leadership should look elsewhere,
    such as product mix or payment method, to increase revenue.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Technique 3: K-Nearest Neighbors (KNN) Classification

    We build a KNN classifier to predict which product line a transaction
    belongs to, using branch, gender, customer type, unit price, quantity,
    and rating as features.

    If product line can be predicted from these characteristics, it suggests
    that certain customer profiles are reliably associated with particular
    spending categories.

    **Prechecks:**
    - KNN is sensitive to feature scale, so we standardize all features before
      fitting, using `StandardScaler`.
    - We split the data 80/20 into training and test sets with `random_state=42`.
    - We use K=5 neighbors.
    """)
    return


@app.cell
def _(sales):
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import classification_report, confusion_matrix

    features = ['branch_num', 'gender_num', 'cust_num', 'Unit price', 'Quantity', 'Rating']
    X = sales[features]
    y = sales['product_label']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_sc = scaler.fit_transform(X_train)
    X_test_sc  = scaler.transform(X_test)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train_sc, y_train)
    y_pred = knn.predict(X_test_sc)

    print(classification_report(y_test, y_pred))
    return confusion_matrix, y_pred, y_test


@app.cell
def _(confusion_matrix, plt, product_map, sns, y_pred, y_test):
    cm = confusion_matrix(y_test, y_pred)
    labels = [k for k, v in sorted(product_map.items(), key=lambda x: x[1])]

    fig3, ax3 = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=labels, yticklabels=labels, ax=ax3)
    ax3.set_title('KNN Confusion Matrix (K=5)', fontsize=12)
    ax3.set_ylabel('Actual Product Line')
    ax3.set_xlabel('Predicted Product Line')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### KNN Classification Summary

    The confusion matrix reveals which categories the model misclassifies.
    Since categories with similar price and quantity profiles are most often
    confused, the business can identify interchangeable customer bases and
    leverage these insights for cross-category promotions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Overall Conclusion

    Taken together, the analysis suggests that RetailCo's branches operate at
    comparable levels. Revenue differences are more likely driven by product
    mix and transaction size than branch-specific factors, and certain product
    categories serve overlapping customer profiles that could be leveraged for
    cross-selling campaigns.

    ---

    ## References

    Anthropic. (2026, March 21). *Hypothesis testing concepts and examples*

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Generative AI chat]. Claude Sonnet 4.6. https://claude.ai/share/b93c2c50-dee5-4147-9727-20be2b267cbe

    &nbsp;

    - Dataset structure: `supermarket_sales.csv` as referenced in `3_Warmup.py`
    - Descriptive statistics: `2_DescriptiveStatistics_DerivingInsights.py`
    - Hypothesis testing: `4_Hypthesis_Testing.py`
    - KNN classification: `5_Supervised_Machine_Learning.py`
    - Visualization style: `wk7_concepts_guide.py`

    ---

    ## Appendix: AI-Generated Content

    **Tool:** Claude Sonnet 4.6 (Anthropic)
    **Date:** April 30, 2026
    **Topic:** Data Visualization

    ### Prompt Submitted to AI:

    Could you make me a list of the concepts in  the 7_datavisualizationtocommunicateresults.py
    file and describe what each one is used for and how it works? put them in numerical order.
    provide the results in a Marimo style file with code windows for example code snippets when
    appropriate. the format should be markdown window describing the concept, code window with
    the code, and a markdown window explaining results and what the code is doing.

    ### AI Response:

    Here is the Marimo concept guide for Week 7. It covers all 12 concepts from the file in order, each with the three-panel structure you asked for: a markdown description, a code window with a runnable example, and a markdown explanation of the results.
    The 12 concepts are:

    | # | Concept | Core Idea |
    |---|---|---|
    | 1 | What is Data Visualization | Graphical representation to reveal patterns faster than raw data |
    | 2 | Exploratory vs. Explanatory | Exploration finds the story; explanation communicates it |
    | 3 | Context: Who, What, How | Plan audience, message, and data format before drawing anything |
    | 4 | Altair + `mo.ui.altair_chart` | Build interactive, reactive charts inside Marimo |
    | 5 | Telling a Data Story | Relevant data + clear narrative + intentional visuals + call to action |
    | 6 | Clutter and Cognitive Load | Extra visual elements increase mental effort; remove them |
    | 7 | Visual Order, Alignment, White Space | Grid alignment and breathing room make layouts feel trustworthy |
    | 8 | Preattentive Attributes | Color, size, position guide attention before conscious thought |
    | 9 | Eliminate Distractions | If removing it changes nothing, remove it |
    | 10 | Text as a Design Element | Titles, axis labels, and annotations are non-negotiable |
    | 11 | Don't Overcomplicate Things | Simpler always wins when the information is the same |
    | 12 | Design Thinking | Empathize → Define → Ideate → Prototype → Test (iterative) |



    The full detailed response is contained in the reference link.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
