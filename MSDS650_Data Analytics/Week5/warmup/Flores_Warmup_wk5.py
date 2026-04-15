# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.3",
#     "pandas>=3.0.1",
#     "pyzmq>=27.1.0",
#     "scipy>=1.17.1",
#     "seaborn>=0.13.2",
#     "statsmodels>=0.14.6",
#     "traitlets>=5.14.3",
# ]
# ///

import marimo

__generated_with = "0.23.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Warmup Exercise for Week 5

    ---
    This report investigates potential pay gaps across three demographic dimensions:

    1. **Ethnicity** -- White vs. Non-White employees
    2. **Gender across Ethnicities** -- Male vs. Female within each ethnic group
    3. **Manager Salaries across Departments**

    For each category, we define formal null and alternative hypotheses, select an appropriate
    statistical test, execute that test, and summarize the findings.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup: Imports and Data Loading
    """)
    return


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import pandas as pd
    from scipy import stats
    from statsmodels.stats import weightstats as stests
    from statsmodels.stats.weightstats import ttest_ind as ttest_ind
    import warnings
    warnings.filterwarnings('ignore')
    sns.set_theme()
    return mo, pd, sns, stats, stests


@app.cell
def _(pd):
    df = pd.read_csv('wages.csv')
    df.head(10)
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data Prep

    Before analysis we clean up the data. We drop the name columns since they are identifiers,
    not analytical variables. We also convert the Salary column from a string to a float by
    stripping the leading dollar sign and commas.
    """)
    return


@app.cell
def _(df):
    cols_drop = ['Surname', 'Name']
    df.drop(columns=cols_drop, inplace=True)
    df.Salary = df.Salary.replace('[\\$,]', '', regex=True).astype(float)
    df.head(10)
    return


@app.cell
def _(df):
    df.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Part 1

    ## Ethnicity: White vs. Non-White

    ### 1. Hypotheses

    **H0 (Null Hypothesis):** There is no statistically significant difference in the mean salary
    between White employees and Non-White employees at Spark Fortress, Inc.

    **Ha (Alternative Hypothesis):** There is a statistically significant difference in the mean
    salary between White employees and Non-White employees at Spark Fortress, Inc.

    This is a two-tailed test because we are investigating whether any gap exists, not the
    direction of the gap.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exploratory Look at the Data

    We start by examining the salary distributions for White and Non-White employees.
    Non-White is defined as any employee whose Ethnicity is not listed as White.
    """)
    return


@app.cell
def _(df):
    white_sal = df[df.Ethnicity == 'White'].Salary
    nonwhite_sal = df[df.Ethnicity != 'White'].Salary
    return nonwhite_sal, white_sal


@app.cell
def _(df, mo):
    mo.md(f"""
    | Group | n | Mean Salary |
    |:------|--:|------------:|
    | White | {(df.Ethnicity == 'White').sum()} | ${df[df.Ethnicity == 'White'].Salary.mean():,.2f} |
    | Non-White | {(df.Ethnicity != 'White').sum()} | ${df[df.Ethnicity != 'White'].Salary.mean():,.2f} |
    """)
    return


@app.cell
def _(df, sns):
    sns.boxplot(data=df[df.Ethnicity == 'White'], x='Ethnicity', y='Salary')
    return


@app.cell
def _(df, sns):
    sns.boxplot(data=df[df.Ethnicity != 'White'], x='Ethnicity', y='Salary')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. Choosing the Test

    We have two independent groups: White (n=112) and Non-White (n=62). Both groups have n >= 30,
    so the Central Limit Theorem applies and we use a **two-sample z-test** to compare the means.
    The z-test is appropriate because:

    - The two samples are independent
    - Both sample sizes exceed 30
    - We are comparing means of a continuous variable (Salary)
    """)
    return


@app.cell
def _(mo, nonwhite_sal, stests, white_sal):
    z_eth, p_eth = stests.ztest(white_sal, nonwhite_sal, value=0, alternative='two-sided')

    conclusion_eth = "**Reject H0**" if p_eth < 0.05 else "**Fail to Reject H0**"

    mo.md(f"""
    ### Z-Test Results -- White vs. Non-White

    | Metric | Value |
    |:-------|------:|
    | White Mean Salary | ${white_sal.mean():,.2f} |
    | Non-White Mean Salary | ${nonwhite_sal.mean():,.2f} |
    | Z-statistic | {z_eth:.4f} |
    | P-value | {p_eth:.4f} |
    | Alpha | 0.05 |
    | Conclusion | {conclusion_eth} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. Summary of Findings -- Ethnicity

    With a p-value of approximately **0.506**, we **fail to reject H0**. The p-value is far above
    the significance threshold of 0.05, meaning there is insufficient statistical evidence to
    conclude that White and Non-White employees are paid differently at Spark Fortress, Inc.
    The nominal difference in mean salaries is not statistically distinguishable from random
    sampling variation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Gender Across Ethnicities

    ### 1. Hypotheses


    **H0 (Null Hypothesis):** Within each ethnic group, there is no statistically significant
    difference in mean salary between Male and Female employees at Spark Fortress, Inc.

    **Ha (Alternative Hypothesis):** Within at least one ethnic group, there is a statistically
    significant difference in mean salary between Male and Female employees at Spark Fortress, Inc.

    Each test is two-tailed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exploratory Look at the Data

    We examine mean salary by gender within each ethnic group using `groupby`.
    """)
    return


@app.cell
def _(df):
    df.groupby('Ethnicity').Salary.mean()
    return


@app.cell
def _(df):
    df.groupby('Gender').Salary.mean()
    return


@app.cell
def _(df, sns):
    sns.boxplot(data=df[df.Ethnicity == 'White'], x='Gender', y='Salary')
    return


@app.cell
def _(df, sns):
    sns.boxplot(data=df[df.Ethnicity == 'Black or African American'], x='Gender', y='Salary')
    return


@app.cell
def _(df, sns):
    sns.boxplot(data=df[df.Ethnicity == 'Asian'], x='Gender', y='Salary')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. Choosing the Test

    For each ethnic group we compare the mean salary of two independent groups (Male vs. Female).
    We check sample sizes to determine whether to use a **t-test** (n < 30) or a **z-test**
    (n >= 30), following the same selection rule used in the Week 4 demo.

    | Ethnicity | Male n | Female n | Test Used |
    |:----------|-------:|---------:|:----------|
    | White | 50 | 62 | z-test (both >= 30) |
    | Black or African American | 15 | 21 | t-test (both < 30) |
    | Asian | 5 | 10 | t-test (both < 30) |
    | Two or more races | 4 | 5 | t-test (both < 30) |
    | Hispanic | 2 | 0 | insufficient data |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### White Employees
    """)
    return


@app.cell
def _(df):
    white_m = df[df.Ethnicity == 'White'][df.Gender == 'Male'].Salary
    white_f = df[df.Ethnicity == 'White'][df.Gender == 'Female'].Salary
    return white_f, white_m


@app.cell
def _(mo, stests, white_f, white_m):
    z_w, p_w = stests.ztest(white_m, white_f, value=0, alternative='two-sided')
    mo.md(f"""
    **White -- Z-Test Results**

    | Metric | Value |
    |:-------|------:|
    | Male Mean | ${white_m.mean():,.2f} |
    | Female Mean | ${white_f.mean():,.2f} |
    | Z-statistic | {z_w:.4f} |
    | P-value | {p_w:.4f} |
    | Conclusion | {"**Reject H0**" if p_w < 0.05 else "**Fail to Reject H0**"} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Black or African American Employees
    """)
    return


@app.cell
def _(df):
    baa_m = df[df.Ethnicity == 'Black or African American'][df.Gender == 'Male'].Salary
    baa_f = df[df.Ethnicity == 'Black or African American'][df.Gender == 'Female'].Salary
    return baa_f, baa_m


@app.cell
def _(baa_f, baa_m, mo, stats):
    t_baa, p_baa = stats.ttest_ind(baa_m, baa_f, alternative='two-sided')
    mo.md(f"""
    **Black or African American -- T-Test Results**

    | Metric | Value |
    |:-------|------:|
    | Male Mean | ${baa_m.mean():,.2f} |
    | Female Mean | ${baa_f.mean():,.2f} |
    | T-statistic | {t_baa:.4f} |
    | P-value | {p_baa:.4f} |
    | Conclusion | {"**Reject H0**" if p_baa < 0.05 else "**Fail to Reject H0**"} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Asian Employees
    """)
    return


@app.cell
def _(df):
    asian_m = df[df.Ethnicity == 'Asian'][df.Gender == 'Male'].Salary
    asian_f = df[df.Ethnicity == 'Asian'][df.Gender == 'Female'].Salary
    return asian_f, asian_m


@app.cell
def _(asian_f, asian_m, mo, stats):
    t_as, p_as = stats.ttest_ind(asian_m, asian_f, alternative='two-sided')
    mo.md(f"""
    **Asian -- T-Test Results**

    | Metric | Value |
    |:-------|------:|
    | Male Mean | ${asian_m.mean():,.2f} |
    | Female Mean | ${asian_f.mean():,.2f} |
    | T-statistic | {t_as:.4f} |
    | P-value | {p_as:.4f} |
    | Conclusion | {"**Reject H0**" if p_as < 0.05 else "**Fail to Reject H0**"} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Two or More Races Employees
    """)
    return


@app.cell
def _(df):
    two_m = df[df.Ethnicity == 'Two or more races'][df.Gender == 'Male'].Salary
    two_f = df[df.Ethnicity == 'Two or more races'][df.Gender == 'Female'].Salary
    return two_f, two_m


@app.cell
def _(mo, stats, two_f, two_m):
    t_two, p_two = stats.ttest_ind(two_m, two_f, alternative='two-sided')
    mo.md(f"""
    **Two or More Races -- T-Test Results**

    | Metric | Value |
    |:-------|------:|
    | Male Mean | ${two_m.mean():,.2f} |
    | Female Mean | ${two_f.mean():,.2f} |
    | T-statistic | {t_two:.4f} |
    | P-value | {p_two:.4f} |
    | Conclusion | {"**Reject H0**" if p_two < 0.05 else "**Fail to Reject H0**"} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 43. Summary of Findings -- Gender Across Ethnicities

    Across all ethnic groups where a test was possible, every p-value exceeds 0.05. We fail to
    reject H0 in all cases. There is no statistically significant evidence of a gender-based pay
    gap within any individual ethnic group at Spark Fortress, Inc.

    Important caveats:
    - The Asian and Two or more races subgroups have very small sample sizes (n < 10 per gender),
      which reduces statistical power. A true difference would be harder to detect in these groups.
    - The Hispanic group could not be tested due to only two total records.
    - The White group had the strongest statistical power (n=50 male, n=62 female) and still
      produced a p-value of 0.376, providing the clearest evidence of no gap within that group.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Manager Salaries Across Departments

    ### 1. Hypotheses

    **H0 (Null Hypothesis):** There is no statistically significant difference in mean manager
    salary between the Production, Sales, and IT/IS departments at Spark Fortress, Inc.

    **Ha (Alternative Hypothesis):** At least one department has a mean manager salary that is
    statistically significantly different from at least one other department.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Isolating the Manager Groups

    We filter to each department and then exclude the non-management positions using the same
    `!=` filtering pattern used in the Week 4 demo to remove the CEO from the dataset.
    """)
    return


@app.cell
def _(df):
    # Production managers: exclude Production Technician I and II
    prod = df[df.Department == 'Production']
    prod_mgr = prod[prod.Position != 'Production Technician I']
    prod_mgr = prod_mgr[prod_mgr.Position != 'Production Technician II']
    prod_mgr.shape
    return (prod_mgr,)


@app.cell
def _(df):
    # All Sales employees hold management-level titles
    sales_mgr = df[df.Department == 'Sales']
    sales_mgr.shape
    return (sales_mgr,)


@app.cell
def _(df):
    # IT/IS managers: exclude individual contributor roles
    it = df[df.Department == 'IT/IS']
    it_mgr = it[it.Position != 'Network Engineer']
    it_mgr = it_mgr[it_mgr.Position != 'Database Administrator']
    it_mgr = it_mgr[it_mgr.Position != 'IT Support']
    it_mgr = it_mgr[it_mgr.Position != 'Sr. Network Engineer']
    it_mgr.shape
    return (it_mgr,)


@app.cell
def _(it_mgr, mo, prod_mgr, sales_mgr):
    mo.md(f"""
    | Department | Manager n | Mean Salary |
    |:-----------|----------:|------------:|
    | Production | {prod_mgr.shape[0]} | ${prod_mgr.Salary.mean():,.2f} |
    | Sales | {sales_mgr.shape[0]} | ${sales_mgr.Salary.mean():,.2f} |
    | IT/IS | {it_mgr.shape[0]} | ${it_mgr.Salary.mean():,.2f} |
    """)
    return


@app.cell
def _(prod_mgr, sns):
    sns.boxplot(data=prod_mgr, x='Department', y='Salary')
    return


@app.cell
def _(sales_mgr, sns):
    sns.boxplot(data=sales_mgr, x='Department', y='Salary')
    return


@app.cell
def _(it_mgr, sns):
    sns.boxplot(data=it_mgr, x='Department', y='Salary')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. Choosing the Test

    We are comparing the mean salaries of three department manager groups. Because all three
    groups have n < 30 (Production n=10, Sales n=26, IT/IS n=5), we use **two-sample t-tests**
    for each pairwise comparison. We perform three comparisons:

    - Production vs. Sales
    - Sales vs. IT/IS
    - Production vs. IT/IS
    """)
    return


@app.cell
def _(mo, prod_mgr, sales_mgr, stats):
    t_ps, p_ps = stats.ttest_ind(prod_mgr.Salary, sales_mgr.Salary, alternative='two-sided')
    mo.md(f"""
    **Production vs. Sales -- T-Test Results**

    | Metric | Value |
    |:-------|------:|
    | Production Mean | ${prod_mgr.Salary.mean():,.2f} |
    | Sales Mean | ${sales_mgr.Salary.mean():,.2f} |
    | T-statistic | {t_ps:.4f} |
    | P-value | {p_ps:.4f} |
    | Conclusion | {"**Reject H0**" if p_ps < 0.05 else "**Fail to Reject H0**"} |
    """)
    return


@app.cell
def _(it_mgr, mo, sales_mgr, stats):
    t_si, p_si = stats.ttest_ind(sales_mgr.Salary, it_mgr.Salary, alternative='two-sided')
    mo.md(f"""
    **Sales vs. IT/IS -- T-Test Results**

    | Metric | Value |
    |:-------|------:|
    | Sales Mean | ${sales_mgr.Salary.mean():,.2f} |
    | IT/IS Mean | ${it_mgr.Salary.mean():,.2f} |
    | T-statistic | {t_si:.4f} |
    | P-value | {p_si:.4f} |
    | Conclusion | {"**Reject H0**" if p_si < 0.05 else "**Fail to Reject H0**"} |
    """)
    return


@app.cell
def _(it_mgr, mo, prod_mgr, stats):
    t_pi, p_pi = stats.ttest_ind(prod_mgr.Salary, it_mgr.Salary, alternative='two-sided')
    mo.md(f"""
    **Production vs. IT/IS -- T-Test Results**

    | Metric | Value |
    |:-------|------:|
    | Production Mean | ${prod_mgr.Salary.mean():,.2f} |
    | IT/IS Mean | ${it_mgr.Salary.mean():,.2f} |
    | T-statistic | {t_pi:.4f} |
    | P-value | {p_pi:.4f} |
    | Conclusion | {"**Reject H0**" if p_pi < 0.05 else "**Fail to Reject H0**"} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. Summary of Findings -- Managers Across Departments

    The pairwise t-tests reveal the following:

    - **Production vs. Sales** (p = 0.055): We narrowly fail to reject H0. There is no
      statistically significant difference in mean manager salary between these two departments
      at the 0.05 level, though the result is close to the threshold.
    - **Sales vs. IT/IS** (p ~ 0.000): We reject H0. IT/IS managers are paid significantly
      more than Sales managers.
    - **Production vs. IT/IS** (p ~ 0.000): We reject H0. IT/IS managers are paid significantly
      more than Production managers.

    IT/IS management commands a statistically significant salary premium over both Production
    and Sales management, consistent with market rates for technology leadership roles. The
    Software Engineering Manager salary of $56,160 is anomalously low compared to all other
    managers and warrants a direct review by the CEO.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Part 2: Summary for the CEO

    | Analysis | Test | Statistic | P-value | Decision | Interpretation |
    |:---------|:-----|----------:|--------:|:---------|:---------------|
    | White vs. Non-White | z-test | -0.664 | 0.506 | Fail to Reject H0 | No evidence of ethnicity-based pay gap |
    | Gender -- White | z-test | 0.886 | 0.376 | Fail to Reject H0 | No gender pay gap in White group |
    | Gender -- Black/AA | t-test | 0.513 | 0.611 | Fail to Reject H0 | No gender pay gap in Black/AA group |
    | Gender -- Asian | t-test | -0.301 | 0.768 | Fail to Reject H0 | No gender pay gap in Asian group |
    | Gender -- Two+ Races | t-test | 0.357 | 0.731 | Fail to Reject H0 | No gender pay gap in Two+ races group |
    | Managers: Production vs. Sales | t-test | -1.988 | 0.055 | Fail to Reject H0 | No significant difference at alpha=0.05 |
    | Managers: Sales vs. IT/IS | t-test | -14.860 | ~0.000 | **Reject H0** | IT/IS managers paid significantly more than Sales |
    | Managers: Production vs. IT/IS | t-test | -8.087 | ~0.000 | **Reject H0** | IT/IS managers paid significantly more than Production |

    **Key takeaways for Spark Fortress, Inc.:**
    - There is no statistically significant evidence of pay inequity based on ethnicity or gender
      in any group with sufficient sample size to test.
    - IT/IS manager compensation is statistically significantly higher than both Production and
      Sales manager compensation. This may be justifiable by technology market rates, but should
      be confirmed and documented.
    - The Software Engineering Manager salary of $56,160 is anomalously low compared to all
      other managers and warrants a review.
    - Small sample sizes for Hispanic, Asian, and Two or more races employees limit statistical
      power for those subgroups. These analyses should be revisited as the employee base grows.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## References

    Anthropic. (2026, March 21). *Hypothesis testing concepts and examples*

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Generative AI chat]. Claude Sonnet 4.6.

    &nbsp;

    ---

    ## Appendix: AI-Generated Content

    **Tool:** Claude Sonnet 4.6 (Anthropic)
    **Date:** April 13, 2026
    **Topic:** Supervised Machine Learning Concepts

    ---

    ### Prompt Submitted to AI:

    Could you make me a list of the concepts in the 5_supervised_machine_learning.py file and
    describe what each one is used for and how it works? put them in numerical order. provide
    the results in a marimo style file with code windows for example code snippets when
    appropriate. the format should be markdown window describing the concept, code window with
    the code, and a markdown window explaining results and what the code is doing.

    ---

    ### Full-Text AI Response:

    Here is the marimo file covering all 15 concepts from `5_Supervised_Machine_Learning.py`
    in numerical order. Each concept follows the format you asked for: a markdown cell
    describing the concept, a code cell with a working example drawn directly from the source
    file, and a markdown cell explaining what the code is doing and what the results mean.

    Here is a quick overview of the 15 concepts covered:

    1.  Supervised vs Unsupervised Learning -- the foundational distinction between labeled
        and unlabeled data
    2.  KNN Algorithm -- how distance calculation and majority voting work under the hood
    3.  Regressor vs Classifier -- when to use KNeighborsRegressor vs KNeighborsClassifier
    4.  EDA Before Modeling -- using a correlation heatmap to decide which features to keep
    5.  Features (X) and Target (y) -- how to separate predictor columns from the target column
    6.  Train/Test Split -- why you need a holdout set and how train_test_split works
    7.  Fit and Predict -- the .fit() / .predict() workflow
    8.  R-Squared Score -- the standard regression evaluation metric and the K-loop for
        finding optimal K
    9.  K-Fold Cross-Validation -- the gold standard evaluation technique using KFold and
        cross_val_score
    10. StandardScaler and Pipeline -- scaling features to prevent distance-based algorithms
        from being misled by feature magnitude
    11. Comparing Regression Algorithms -- testing seven regressors on the same data to find
        the best performer
    12. Ensemble Methods -- how boosting (AdaBoost, GBM) and bagging (Random Forest,
        Extra Trees) work
    13. Classifier and Dummy Encoding -- converting categorical columns with pd.get_dummies
        before classification
    14. Comparing Classifier Algorithms -- testing ten classifiers on the same data with
        accuracy as the metric
    15. Recap: Selection, Scaling, and Tuning -- summary of the three key takeaways from
        the week

    The full detailed response is contained in the reference link.
    """)
    return


if __name__ == "__main__":
    app.run()
