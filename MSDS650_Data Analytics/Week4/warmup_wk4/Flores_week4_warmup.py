# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "pandas>=3.0.1",
#     "seaborn>=0.13.2",
#     "matplotlib>=3.7.1",
#     "numpy>=2.0.0",
# ]
# ///

import marimo

__generated_with = "0.22.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Warmup for Week 4 - EDA
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Analytical Question

    **Do cardiovascular stress indicators - specifically maximum heart rate achieved (thalach),
    exercise-induced angina (exang), and resting blood pressure (trestbps) - differ
    meaningfully between patients with and without heart disease?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 1: Load and Describe the Data
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set()
    return np, pd, plt, sns


@app.cell
def _(pd):
    df_raw = pd.read_csv('warmup_wk4/heart_disease.data')
    df_raw.head(10)
    return (df_raw,)


@app.cell
def _(df_raw):
    df_raw.shape
    return


@app.cell
def _(df_raw):
    df_raw.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1a. Data Types: Categorical vs Continuous Variables

    Based on the dataset documentation, we can classify each column:

    | Column | Description | Type |
    |--------|-------------|------|
    | age | Age in years | Continuous |
    | sex | Sex (1 = male, 0 = female) | Categorical (Nominal) |
    | cp | Chest pain type (1-4) | Categorical (Ordinal) |
    | trestbps | Resting blood pressure (mm Hg) | Continuous |
    | chol | Serum cholesterol (mg/dl) | Continuous |
    | cigs | Cigarettes per day | Continuous |
    | years | Years as a smoker | Continuous |
    | fbs | Fasting blood sugar > 120 mg/dl (1=yes, 0=no) | Categorical (Nominal) |
    | dm | History of diabetes (1=yes, 0=no) | Categorical (Nominal) |
    | famhist | Family history of CAD (1=yes, 0=no) | Categorical (Nominal) |
    | restecg | Resting ECG results (0, 1, 2) | Categorical (Ordinal) |
    | thalach | Maximum heart rate achieved | Continuous |
    | exang | Exercise-induced angina (1=yes, 0=no) | Categorical (Nominal) |
    | thal | Thalassemia type (3=normal, 6=fixed, 7=reversible) | Categorical (Nominal) |
    | num | Heart disease diagnosis (0=absent, 1-4=present) | Categorical (Ordinal / Target) |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1b. Statistical Summary

    The dataset documentation states missing values are stored as -9. We replace them
    with NaN before computing statistics so they do not distort the results.
    """)
    return


@app.cell
def _(df_raw, np):
    df = df_raw.replace(-9, np.nan)
    df.describe().T
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A few things stand out:

    - **age** ranges from 29 to 77 with a mean near 54 - an older adult population.
    - **chol** has a max of 564 mg/dl. Values above 400 are clinically unusual and worth flagging.
    - **trestbps** has a max of 200 mm Hg, which is at the upper clinical extreme.
    - **thalach** ranges from 71 to 202 bpm. The low end is plausible for an older patient with disease.
    - **num** ranges 0-4 confirming multiple disease severity levels are present.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1c. Categorical Variable Distributions
    """)
    return


@app.cell
def _(df, plt):
    df['sex'].value_counts().plot.bar(title='Sex (0=Female, 1=Male)', edgecolor='black')
    plt.ylabel('Count')
    plt.show()
    return


@app.cell
def _(df, plt):
    df['cp'].value_counts().sort_index().plot.bar(
        title='Chest Pain Type (1=Typical Angina, 2=Atypical, 3=Non-Anginal, 4=Asymptomatic)',
        edgecolor='black'
    )
    plt.ylabel('Count')
    plt.show()
    return


@app.cell
def _(df, plt):
    df['exang'].value_counts().sort_index().plot.bar(
        title='Exercise-Induced Angina (0=No, 1=Yes)',
        edgecolor='black'
    )
    plt.ylabel('Count')
    plt.show()
    return


@app.cell
def _(df, plt):
    df['thal'].value_counts().sort_index().plot.bar(
        title='Thalassemia Type (3=Normal, 6=Fixed Defect, 7=Reversible Defect)',
        edgecolor='black'
    )
    plt.ylabel('Count')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - The dataset is male-heavy (about 68% male).
    - The most common chest pain type is asymptomatic (type 4), characteristic of patients
      referred for cardiac evaluation who may already have significant disease.
    - Most patients do not have exercise-induced angina.
    - The most common thalassemia result is normal (3), followed by reversible defect (7).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Section 2: Data Cleaning
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2a. Identify Missing Values
    """)
    return


@app.cell
def _(df, pd):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    missing_data.head(20)
    return (missing_data,)


@app.cell
def _(missing_data, plt):
    missing = missing_data[missing_data['Total'] > 0]['Total']
    missing.plot.bar(title='Missing Value Counts by Column', edgecolor='black')
    plt.ylabel('Count')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Four columns contain missing values (originally stored as -9):

    | Column | Missing | % Missing | Decision |
    |--------|---------|-----------|----------|
    | dm (diabetes history) | 259 | 91.8% | **Drop column** - nearly all values missing |
    | cigs (cigarettes/day) | 5 | 1.8% | **Impute with median** |
    | years (years smoking) | 5 | 1.8% | **Impute with median** |
    | thal (thalassemia type) | 2 | 0.7% | **Impute with mode** (categorical) |

    The `dm` column has 91.8% missing. Keeping it would add almost no analytical value,
    so we drop it. The remaining columns have very few missing values and can be safely imputed.
    """)
    return


@app.cell
def _(df):
    df_clean = df.copy()

    # drop dm - 91.8% missing
    df_clean.drop(columns=['dm'], inplace=True)

    # impute cigs and years with median (continuous)
    df_clean['cigs'] = df_clean['cigs'].fillna(df_clean['cigs'].median())
    df_clean['years'] = df_clean['years'].fillna(df_clean['years'].median())

    # impute thal with mode (categorical)
    df_clean['thal'] = df_clean['thal'].fillna(df_clean['thal'].mode()[0])

    df_clean.isnull().sum()
    return (df_clean,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2b. Identify and Handle Outliers

    We use the IQR method to identify outliers. The lower and upper fences are
    1.5 times the IQR away from Q1 and Q3.
    """)
    return


@app.cell
def _(df_clean):
    df_clean.boxplot(['age', 'trestbps', 'chol', 'thalach'])
    return


@app.cell
def _(df_clean):
    df_clean.boxplot(['cigs', 'years'])
    return


@app.cell
def _(df_clean, pd):
    cont_cols = ['age', 'trestbps', 'chol', 'cigs', 'years', 'thalach']
    outlier_rows = []
    for col in cont_cols:
        Q1 = df_clean[col].quantile(q=0.25)
        Q3 = df_clean[col].quantile(q=0.75)
        LF = Q1 - (1.5 * (Q3 - Q1))
        UF = Q3 + (1.5 * (Q3 - Q1))
        n_out = ((df_clean[col] < LF) | (df_clean[col] > UF)).sum()
        outlier_rows.append({'Column': col, 'Q1': round(Q1, 1), 'Q3': round(Q3, 1),
                             'Lower Fence': round(LF, 1), 'Upper Fence': round(UF, 1),
                             'Outlier Count': n_out})
    pd.DataFrame(outlier_rows)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Outlier handling decisions:**

    - **chol**: The max value is a clinical extreme. We cap at the upper fence shown in the table above.
    - **trestbps**: The max value is above the upper fence. We cap it as well.
    - **cigs / years**: Outliers represent a plausible heavy long-term smoker. Left as-is.
    - **age / thalach**: No outliers detected.
    """)
    return


@app.cell
def _(df_clean):
    df_final = df_clean.copy()

    Q1_c = df_final['chol'].quantile(q=0.25)
    Q3_c = df_final['chol'].quantile(q=0.75)
    UF_c = Q3_c + (1.5 * (Q3_c - Q1_c))
    df_final['chol'] = df_final['chol'].clip(upper=UF_c)

    Q1_t = df_final['trestbps'].quantile(q=0.25)
    Q3_t = df_final['trestbps'].quantile(q=0.75)
    UF_t = Q3_t + (1.5 * (Q3_t - Q1_t))
    df_final['trestbps'] = df_final['trestbps'].clip(upper=UF_t)

    print('chol max after capping:', df_final['chol'].max())
    print('trestbps max after capping:', df_final['trestbps'].max())
    return (df_final,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We also create a binary `disease` column for analysis. The original `num` column
    has values 0-4, where 0 means no disease and 1-4 indicate disease is present.
    """)
    return


@app.cell
def _(df_final):
    df_final['disease'] = (df_final['num'] > 0).astype(int)
    df_final['disease'].value_counts()
    return


@app.cell
def _(df_final, mo):
    mo.ui.dataframe(df_final)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Section 3: Feature Selection - Graphical Visualization and Relationships
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3a. Histograms of the Three Stress Indicators
    """)
    return


@app.cell
def _(df_final, plt):
    plt.hist(df_final['thalach'].dropna(), bins=20)
    plt.title('Max Heart Rate Achieved (thalach)')
    plt.xlabel('bpm')
    plt.ylabel('Count')
    plt.show()
    return


@app.cell
def _(df_final, plt):
    plt.hist(df_final['trestbps'].dropna(), bins=20)
    plt.title('Resting Blood Pressure (trestbps)')
    plt.xlabel('mm Hg')
    plt.ylabel('Count')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3b. Boxplots of the Three Stress Indicators by Disease Status
    """)
    return


@app.cell
def _(df_final, sns):
    sns.boxplot(data=df_final, x='disease', y='thalach')
    return


@app.cell
def _(df_final, sns):
    sns.boxplot(data=df_final, x='disease', y='trestbps')
    return


@app.cell
def _(df_final, sns):
    sns.boxplot(data=df_final, x='disease', y='exang')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The boxplots show a clear difference in thalach between groups - disease patients
    have a visibly lower median max heart rate. The trestbps and exang separations are
    smaller but still present.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3c. Correlation Matrix and Heatmap
    """)
    return


@app.cell
def _(df_final):
    corrmat = df_final[['thalach', 'trestbps', 'exang', 'age', 'chol', 'disease']].corr(numeric_only=True)
    corrmat
    return (corrmat,)


@app.cell
def _(corrmat, plt, sns):
    _f, _ax = plt.subplots(figsize=(9, 7))
    _hm = sns.heatmap(corrmat, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10})
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    From the heatmap:

    - **thalach** has the strongest negative correlation with disease of the three indicators.
      Higher max heart rate means lower disease likelihood.
    - **exang** has the strongest positive correlation with disease of the three indicators.
      Patients with exercise-induced angina are much more likely to have disease.
    - **trestbps** shows the smallest positive correlation with disease of the three.
    - **age** moderately correlates with disease and negatively with thalach,
      which makes physiological sense - older patients tend to have lower max heart rates.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3d. Pairplot of the Stress Indicators
    """)
    return


@app.cell
def _(df_final, sns):
    sns.pairplot(df_final[['thalach', 'trestbps', 'exang', 'age', 'disease']])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The pairplot reinforces that thalach provides the clearest visual separation between
    disease and no-disease patients. The thalach vs age scatter shows disease patients
    clustering in the older, lower heart rate region.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Section 4: Insights and Findings
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4a. Mean Stress Indicator Values by Disease Group
    """)
    return


@app.cell
def _(df_final):
    df_final.groupby('disease').agg({'thalach': ['mean', 'median', 'min', 'max'],
                                     'trestbps': ['mean', 'median', 'min', 'max'],
                                     'exang': ['mean', 'sum']}).round(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4b. Exercise-Induced Angina and Disease Rate
    """)
    return


@app.cell
def _(df_final):
    df_final.groupby('exang').disease.mean().round(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Patients with exercise-induced angina (exang=1) have a substantially higher disease
    rate than patients without it, as shown in the output above.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4c. Scatterplot - Age vs Max Heart Rate by Disease
    """)
    return


@app.cell
def _(df_final, sns):
    sns.scatterplot(data=df_final, x='age', y='thalach', hue='disease')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4d. Summary of Findings

    **Returning to our analytical question:** Do thalach, exang, and trestbps differ
    meaningfully between patients with and without heart disease?

    **Yes. Here is what the data shows:**

    1. **thalach (max heart rate) shows the strongest difference.** The groupby table in
       4a shows disease patients achieve a noticeably lower mean and median max heart rate.
       The heatmap in 3c shows this is the strongest correlation with disease among the
       three indicators.

    2. **exang (exercise-induced angina) is a strong categorical separator.** The groupby
       in 4b shows disease patients have a substantially higher rate of exercise-induced
       angina. The heatmap confirms it has the strongest positive correlation with disease
       of the three indicators.

    3. **trestbps (resting blood pressure) shows a smaller but real difference.** The
       groupby table in 4a shows disease patients have a higher mean resting blood pressure.
       The heatmap shows this is the weakest correlation of the three indicators.

    Among the three stress indicators, thalach and exang are the most informative.
    A patient with a low max heart rate who also develops angina during exercise is
    substantially more likely to carry a positive heart disease diagnosis.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
