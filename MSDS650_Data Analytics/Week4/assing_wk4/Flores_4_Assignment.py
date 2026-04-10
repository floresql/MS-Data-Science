# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "matplotlib>=3.10.8",
#     "numpy>=2.4.3",
#     "pandas>=3.0.1",
#     "pyodbc>=5.3.0",
#     "pyzmq>=27.1.0",
#     "scipy>=1.17.1",
# ]
# ///

import marimo

__generated_with = "0.22.4"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    # Week 4 Assignment: Hypothesis Tesing
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---

    ### Extract the Annual EM Math table from the Microsoft Access Database.

    To achieve this we will use the pyodbc library
    """)
    return


@app.cell
def _():
    import pandas as pd
    import pyodbc

    # Connect to the Access database
    db_path = r'C:\Users\geflo\OneDrive\Documents\DEV\GitHub\MS-Data-Science\MSDS650_Data Analytics\Week4\assing_wk4\SRC2025_Group1.accdb'

    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=' + db_path + ';'
    )

    conn = pyodbc.connect(conn_str)

    # Load the Annual_EM_MATH table into a DataFrame
    df = pd.read_sql('SELECT * FROM Annual_EM_MATH', conn)

    conn.close()

    # Look at the data
    df.head()
    return df, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here we can see there are 671,220 rows and 25 columns.
    """)
    return


@app.cell
def _(df):
    df.shape
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ### Clean the data so that it's ready for analysis.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll start by checking for missing values.
    """)
    return


@app.cell
def _(df, pd):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    missing_data.head(20)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    LEVEL5_COUNT and LEVEL5_%TESTED are over 96% missing. Per the README file, level 5 only applies to a small subset of exams.

    We will drop LEVEL5 columns using drop() with inplace=True
    """)
    return


@app.cell
def _(df):
    df.drop(columns=['LEVEL5_COUNT', 'LEVEL5_%TESTED'], inplace=True)

    # confirm the drop worked
    print(df.shape)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Per the README, suppressed data are indicated with "s". We replace 's' with NaN so numeric columns can be converted to numbers for analysis.

    Upon running this code we see Empty strings also appear in the data and need to be treated the same way
    """)
    return


@app.cell
def _(df):
    def replace_suppressed(val):
        if val == 's' or val == '':
            return None
        else:
            return val

    suppressed_cols = [
        'LEVEL1_COUNT', 'LEVEL1_%TESTED',
        'LEVEL2_COUNT', 'LEVEL2_%TESTED',
        'LEVEL3_COUNT', 'LEVEL3_%TESTED',
        'LEVEL4_COUNT', 'LEVEL4_%TESTED',
        'NUM_PROF', 'PER_PROF',
        'TOTAL_SCALE_SCORES', 'MEAN_SCORE'
    ]

    for col in suppressed_cols:
        df[col] = df[col].apply(replace_suppressed)

    # confirm 's' and empty string values are gone
    print(df['LEVEL1_COUNT'].unique()[:10])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Many columns came in as object/string type because of the suppressed 's' values. Now that those are replaced with NaN we can convert them to numeric for analysis.
    """)
    return


@app.cell
def _(df):
    numeric_cols = [
        'LEVEL1_COUNT', 'LEVEL1_%TESTED',
        'LEVEL2_COUNT', 'LEVEL2_%TESTED',
        'LEVEL3_COUNT', 'LEVEL3_%TESTED',
        'LEVEL4_COUNT', 'LEVEL4_%TESTED',
        'NUM_PROF', 'PER_PROF',
        'TOTAL_SCALE_SCORES', 'MEAN_SCORE'
    ]

    for col2 in numeric_cols:
        df[col2] = df[col2].apply(lambda x: float(x) if x is not None else x)

    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, we verify the cleaned data with describe()
    """)
    return


@app.cell
def _(df):
    df.describe().T
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ### Develop a scenario to provide an overall understanding of the organization represented by the dataset.
        * Define a problem statement to investigate with either t-test or z-test.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Problem Statement

    New York State is said to have an achievement gap between students from low-income families and their peers. Based on 2023-24 math test data for grades 3-8, this project looks at whether there is a significant difference in passing rates between students labeled as economically disadvantaged and those who are not.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * Describe your dataset, including the columns that will support our analysis.
    """)
    return


@app.cell
def _(df):
    analysis_df = df[
        (df['ASSESSMENT_NAME'].isin(['MATH3','MATH4','MATH5','MATH6','MATH7','MATH8'])) &
        (df['YEAR'] == 2024) &
        (df['SUBGROUP_NAME'].isin(['Economically Disadvantaged', 'Not Economically Disadvantaged']))
    ].copy()

    print(analysis_df.shape)
    analysis_df[['ENTITY_NAME', 'ASSESSMENT_NAME', 'SUBGROUP_NAME',
                 'NUM_TESTED', 'PER_PROF', 'MEAN_SCORE']].info()
    return (analysis_df,)


@app.cell
def _(analysis_df):
    analysis_df.groupby('SUBGROUP_NAME')['PER_PROF'].describe().round(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The preliminary describe() results already show a meaningful difference in the means: Economically Disadvantaged students had a mean proficiency rate of 42.69%, while Not Economically Disadvantaged students had a mean of 61.79%. The t-test will determine whether this gap is statistically significant.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The columns used in the analysis and their purpose are:

    | Column | Description | Role in Analysis |
    |---|---|---|
    | `ENTITY_NAME` | Name of the school or district | Identifies the observation |
    | `ASSESSMENT_NAME` | Grade level (MATH3 through MATH8) | Filters to individual grade assessments |
    | `SUBGROUP_NAME` | Economic subgroup label | Used to split the two independent samples |
    | `YEAR` | School year (2024 = 2023-24) | Filters to a single year |
    | `NUM_TESTED` | Number of students with a valid score | Confirms adequate sample size per row |
    | `PER_PROF` | Percent of tested students scoring proficient (Level 3 and above) | **The primary variable for the t-test** |
    | `MEAN_SCORE` | Average scale score | Supporting descriptive context |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ### Describe your test approach
        * Justify your selection of which test you will use.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A two-sample t-test (scipy.stats.ttest_ind) will be used to compare mean math proficiency rates between the two groups, following the same method as the Week 4 lecture’s Spark Industries example. This test is appropriate because:
    - Independent Samples: Students belong to either the "Economically Disadvantaged" or "Not" group, not both.
    - Unknown Variance: Since the true population variance is unknown, a t-test is used instead of a z-test.
    - Sample Size: Both groups have over 30 observations, meeting the requirements for a t-test.
    - Continuous Data: The target variable, PER_PROF, is a numeric percentage from 0 to 100.

    The significance level will be set at alpha = 0.05.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * Define a H0/H1 couplet to support your problem statement.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **H0:** There is no significant difference in average math scores between students from low-income families and those who aren't for the 2023-24 school year.

    **H1:** There is a significant difference in average math scores between students from low-income families and those who aren't for the 2023-24 school year.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ### Conduct your analysis according to your defined parameters above.
        * Include a descriptive analysis as appropriate
    """)
    return


@app.cell
def _():
    from scipy import stats
    import matplotlib.pyplot as plt
    import seaborn as sns

    return plt, sns, stats


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Lets look at the subgroups again.
    """)
    return


@app.cell
def _(analysis_df):
    analysis_df.groupby('SUBGROUP_NAME')['PER_PROF'].describe().round(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Mixing in the assessment name.
    """)
    return


@app.cell
def _(analysis_df):
    analysis_df.groupby(['SUBGROUP_NAME', 'ASSESSMENT_NAME'])['PER_PROF'].describe().round(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Boxplot comparing the two subgroups
    """)
    return


@app.cell
def _(analysis_df, plt, sns):
    sns.boxplot(data=analysis_df, x='SUBGROUP_NAME', y='PER_PROF')
    plt.title('Math Proficiency Rate by Economic Subgroup (2023-24)')
    plt.xlabel('Subgroup')
    plt.ylabel('Percent Proficient')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The results show a gap across all grades. Disadvantaged students had an average score of 42.69%, while the non-disadvantaged group averaged 61.79%. A similar gap was observed in every grade, from 3rd through 8th.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * Prep your data for analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Split into two independent samples
    """)
    return


@app.cell
def _(analysis_df):
    econ = analysis_df[
        analysis_df['SUBGROUP_NAME'] == 'Economically Disadvantaged'
    ]['PER_PROF'].dropna()

    not_econ = analysis_df[
        analysis_df['SUBGROUP_NAME'] == 'Not Economically Disadvantaged'
    ]['PER_PROF'].dropna()

    print('Economically Disadvantaged n:', len(econ))
    print('Not Economically Disadvantaged n:', len(not_econ))
    return econ, not_econ


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Normality check using Shapiro-Wilk
    """)
    return


@app.cell
def _(econ, not_econ, stats):
    stat1, p1 = stats.shapiro(econ)
    stat2, p2 = stats.shapiro(not_econ)

    print(f'Shapiro-Wilk Economically Disadvantaged:     stat={stat1:.4f}, p={p1:.4f}')
    print(f'Shapiro-Wilk Not Economically Disadvantaged: stat={stat2:.4f}, p={p2:.4f}')
    return p1, p2, stat1, stat2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Both Shapiro-Wilk p-values are below 0.05, which suggests the data are not perfectly normal. However, both samples have over 500 observations. The Week 4 lecture notes that for large sample sizes the t-test is robust to departures from normality, which is consistent with the central limit theorem. The t-test will proceed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * Conduct your hypothesis testing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Two-sample t-test

    H0: no difference in mean PER_PROF between groups

    H1: there is a difference in mean PER_PROF between groups

    alpha = 0.05, two-sided
    """)
    return


@app.cell
def _(econ, not_econ, stats):
    tstat, pval = stats.ttest_ind(econ, not_econ, alternative='two-sided')

    print(f'T-statistic: {tstat:.4f}')
    print(f'P-value:     {pval:.4f}')

    alpha = 0.05
    if pval < alpha:
        print('Decision: Reject H0')
    else:
        print('Decision: Fail to reject H0')
    return pval, tstat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The p-value is basically zero and way below our 0.05 alpha, so we reject. This shows a significant difference in math scores between the two groups. The negative t-statistic also confirms that disadvantaged students had the lower average, just like our earlier results showed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ### Based on the results from your analysis in step 3, redefined your H0/H1 couplet to dive deeper into the analysis and repeat steps 2 and 3.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Refined Problem Statement:**

    Does the math proficiency gap between Economically Disadvantaged and Not Economically Disadvantaged students grow larger as students advance from Grade 3 to Grade 8?

    **H0:** There is no statistically significant difference in the mean math proficiency gap between the earlier grades (MATH3, MATH4, MATH5) and the later grades (MATH6, MATH7, MATH8) for Economically Disadvantaged students.

    **H1:** There is a statistically significant difference in the mean math proficiency gap between the earlier grades (MATH3, MATH4, MATH5) and the later grades (MATH6, MATH7, MATH8) for Economically Disadvantaged students.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * Descriptive Analysis
    """)
    return


@app.cell
def _(analysis_df):
    econ_df = analysis_df[
        analysis_df['SUBGROUP_NAME'] == 'Economically Disadvantaged'
    ][['ENTITY_NAME', 'ASSESSMENT_NAME', 'PER_PROF']].copy()

    not_econ_df = analysis_df[
        analysis_df['SUBGROUP_NAME'] == 'Not Economically Disadvantaged'
    ][['ENTITY_NAME', 'ASSESSMENT_NAME', 'PER_PROF']].copy()

    merged = econ_df.merge(
        not_econ_df,
        on=['ENTITY_NAME', 'ASSESSMENT_NAME'],
        suffixes=('_econ', '_not_econ')
    )

    merged['gap'] = merged['PER_PROF_not_econ'] - merged['PER_PROF_econ']

    print(merged.shape)
    merged.head()
    return (merged,)


@app.cell
def _(merged):
    merged.groupby('ASSESSMENT_NAME')['gap'].describe().round(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Boxplot of the gap by grade
    """)
    return


@app.cell
def _(merged, plt, sns):
    sns.boxplot(data=merged, x='ASSESSMENT_NAME', y='gap',
                order=['MATH3','MATH4','MATH5','MATH6','MATH7','MATH8'])
    plt.axhline(0, color='red', linestyle='--')
    plt.title('Proficiency Gap by Grade (Not Econ Dis minus Econ Dis) 2023-24')
    plt.xlabel('Grade')
    plt.ylabel('Proficiency Gap (percentage points)')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The descriptive results show the gap is stable across grades. The mean gap ranged from 12.52 points at MATH8 to 19.84 at MATH6, with no clear upward or downward trend from grade 3 through grade 8.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * Data Prep for Hypothesis Testing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Split gap into early grades and late grades
    """)
    return


@app.cell
def _(merged):
    early = merged[
        merged['ASSESSMENT_NAME'].isin(['MATH3', 'MATH4', 'MATH5'])
    ]['gap'].dropna()

    late = merged[
        merged['ASSESSMENT_NAME'].isin(['MATH6', 'MATH7', 'MATH8'])
    ]['gap'].dropna()

    print('Early grades n:', len(early))
    print('Late grades n:', len(late))
    print()
    print('Early mean gap:', round(early.mean(), 2))
    print('Late mean gap:', round(late.mean(), 2))
    return early, late


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Normality check
    """)
    return


@app.cell
def _(p1, p2, stat1, stat2):
    print(f'Shapiro-Wilk Early Grades: stat={stat1:.4f}, p={p1:.4f}')
    print(f'Shapiro-Wilk Late Grades:  stat={stat2:.4f}, p={p2:.4f}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The early grades group returned a Shapiro-Wilk p-value below 0.05. Both groups have well over 30 observations, so the t-test remains appropriate for the same reason as the prior analysis.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Two-sample t-test on the gap values

    H0: no difference in mean gap between early and late grades

    H1: there is a difference in mean gap between early and late grades
    """)
    return


@app.cell
def _(early, late, pval, stats, tstat):
    tstat1, pval1 = stats.ttest_ind(early, late, alternative='two-sided')

    print(f'T-statistic: {tstat:.4f}')
    print(f'P-value:     {pval:.4f}')

    alpha1 = 0.05
    if pval1 < alpha1:
        print('Decision: Reject H0')
    else:
        print('Decision: Fail to reject H0')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There is no statistically significant evidence that the proficiency gap between Economically Disadvantaged and Not Economically Disadvantaged students changes between the early grades and the late grades. The gap appears in Grade 3 and remains essentially unchanged through Grade 8, suggesting the disadvantage is established before Grade 3 and does not compound or close as students progress through elementary and middle school.

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * Provide a recap of the insights you have gained throughout your analysis.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Analysis Recap

    **Problem Statement**

    This analysis looked at the 2023-24 New York State math scores to see if there’s a gap between students from low-income families and those who aren't. We also looked to see if that gap gets bigger or smaller as kids get older (Grades 3–8).


    **Finding 1:** There is a big gap.

    The first test proved that disadvantaged students score much lower than their peers. Because the p-value was basically zero (way below 0.05), we know this difference isn't just a fluke, it’s a real, statistically significant gap.

    **Finding 2:** The gap stays about the same.

    The second test checked if the gap grows as students move through school. Even though the scores change, the gap between the two groups stayed very similar from 3rd grade all the way through 8th grade. There was no evidence that the gap changes as students get older. It stays pretty much the same the whole time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## References
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Anthropic. (2026, March 21). *Hypothesis testing concepts and examples*

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Generative AI chat]. Claude Sonnet 4.6. https://claude.ai/share/37b7c11c-6f3b-45cb-aea5-a236a40da68b

    &nbsp;

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Appendix: AI-Generated Content

    **Tool:** Claude Sonnet 4.6 (Anthropic)
    **Date:** March 21, 2026
    **Topic:** Pandas Data Analysis Techniques


    ### Prompt Submitted to AI:

    Could you make me a list of the concepts in  the 4_hypothesis_testing.py file and describe what each one is used for and how it works? put them in numerical order. provide the results in a markdown file with code windows for example code snippets when appropriate
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### AI Response Summary:

    The markdown file covers all 15 concepts from the notebook in the order they appear. Here is a quick overview of what is included:

    1-2: Foundations -- descriptive vs. inferential statistics, and sampling techniques

    3-5: Hypothesis setup -- null/alternative hypotheses, Type I/II errors, and alpha/p-value decision rules

    6: Normality testing -- histograms, Q-Q plots, and the Shapiro-Wilk test

    7-11: The five hypothesis tests demonstrated -- one-sample t-test, paired t-test, two-sample t-test, one-sample z-test, and two-sample z-test

    12-14: Applied data skills -- subsetting groups for comparison, cleaning string data, and doing exploratory stats before formal testing

    15: Degrees of freedom and when t-tests and z-tests converge
    """)
    return


if __name__ == "__main__":
    app.run()
