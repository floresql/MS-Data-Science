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
    # Week 2 Assignment: Deriving Insight via Descriptive Statistics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1) Inspect the wages.csv dataset (outside of your notebook) and provide a detailed description of the dataset.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Before loading the dataset into this notebook, I opened `wages.csv` to look at the raw fdataile and get a sense of what variables were included and what the values looked like.

    The dataset contains **174 rows** (employees) and **9 columns** (variables).

    | Variable | Description | Data Type |
    |---|---|---|
    | `Surname` | Employee's last name | Categorical – Nominal |
    | `Name` | Employee's first name | Categorical – Nominal |
    | `Age` | Employee's age in years | Numerical – Discrete |
    | `Gender` | Employee's gender | Categorical – Nominal |
    | `Ethnicity` | Employee's self-reported ethnicity | Categorical – Nominal |
    | `Start_date` | The date the employee was hired | Categorical – Ordinal (date) |
    | `Department` | The department the employee works in | Categorical – Nominal |
    | `Position` | The employee's job title | Categorical – Ordinal |
    | `Salary` | The employee's annual salary | Numerical – Continuous |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 2) Create a fictitious business that fits the wages.csv dataset.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Vandelay Industries** is a New York-based manufacturer of latex products. The company produces a wide range of latex goods and employs staff across multiple departments including Production, Sales, IT/IS, Software Engineering, and Administration.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 3) Develop a problem statement and 5 analytical questions to be investigated during your analysis.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Problem Statement

    Vandelay Industries has grown a ton lately and hired lots of new people. Now, they're looking at their employee data to see how pay is spread out across different groups and departments. This analysis will help them make better, fairer decisions as the company keeps getting bigger.

    ### Analytical Questions

    1. **(Segmented Univariant)** How does annual salary vary across different departments at Vandelay Industries?
    2. **(Segmented Univariant)** Is there a difference in salary distribution between male and female employees?
    3. **(Segmented Univariant)** How does salary vary across employee age groups?
    4. What does the overall distribution of employee salaries look like across the company?
    5. What is the age distribution of Vandelay Industries's workforce?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Loading and Preparing Data
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    return pd, plt


@app.cell
def _(pd):
    # load the dataset
    wages = pd.read_csv('assign_wk2/wages.csv')
    wages.sample(10)
    return (wages,)


@app.cell
def _(wages):
    wages.info()
    return


@app.cell
def _(mo):
    mo.md(r"""
    The `Salary` column is stored as a string (object type). Before analysis, I need to strip out the `$` and commas so we can treat it as a number.
    """)
    return


@app.cell
def _(pd, wages):
    # clean the Salary column - remove $ and commas, convert to float
    wages['Salary_clean'] = wages['Salary'].str.replace('[$,]', '', regex=True).astype(float)

    # also create age groups for Q3
    bins = [24, 30, 40, 50, 70]
    labels = ['25-30', '31-40', '41-50', '51+']
    wages['Age_Group'] = pd.cut(wages['Age'], bins=bins, labels=labels)

    print('Salary column cleaned. Quick check:')
    wages[['Salary', 'Salary_clean']].head()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 4) Utilize descriptive statistics to analyze each of your analytical questions.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Analytical Question 1 (Segmented Univariant): How does annual salary vary across departments?

    For this question, we segment the `Salary_clean` feature by `Department`.
    """)
    return


@app.cell
def _(wages):
    # salary stats by department
    dept_salary = wages.groupby('Department')['Salary_clean'].describe()
    dept_salary.round(2)
    return


@app.cell
def _(wages):
    # median salary by department - sorted high to low
    dept_median = wages.groupby('Department')['Salary_clean'].median().sort_values(ascending=False)
    print('Median salary by department:')
    print(dept_median)
    return


@app.cell
def _(plt, wages):
    # boxplot for salary by department
    dept_order = wages.groupby('Department')['Salary_clean'].median().sort_values(ascending=True).index

    wages.boxplot(column='Salary_clean', by='Department', grid=False,
                  figsize=(10, 5), vert=False)
    plt.xlabel('Annual Salary ($)')
    plt.ylabel('Department')
    plt.title('Salary Distribution by Department')
    plt.suptitle('')  # removes the default pandas title
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    This is probably the most interesting chart in the whole analysis because the pay gaps between departments are huge.

    - Sales and IT/IS have the highest medians, with both over $110,000.
    - Production makes up most of the staff—106 out of 174 people—but their median is only around $49,000. That is basically half of what the Sales team makes.
    - Admin Offices sits in the middle with a median of about $65,000.
    - Software Engineering is also up there at $100,000, but it’s a bit lower than expected since some of those are entry-level jobs.

    The boxplot for Production is really small, which means almost everyone there gets paid about the same. Sales is the opposite and has a way wider spread. This massive gap between Production and everyone else is definitely something the HR team at Vandelay should look into.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    #### Analytical Question 2 (Segmented Univariant): Is there a salary difference between male and female employees?

    Again, we are still only analyzing one variable (salary), but we're segmenting it by `Gender` to see if there are any noticeable patterns.
    """)
    return


@app.cell
def _(wages):
    # salary descriptive stats by gender
    wages.groupby('Gender')['Salary_clean'].describe().round(2)
    return


@app.cell
def _(wages):
    # also look at median specifically
    print('Median salary by gender:')
    print(wages.groupby('Gender')['Salary_clean'].median())
    print()
    print('Mean salary by gender:')
    print(wages.groupby('Gender')['Salary_clean'].mean().round(2))
    return


@app.cell
def _(plt, wages):
    # boxplot for salary by gender
    wages.boxplot(column='Salary_clean', by='Gender', grid=False, figsize=(7, 5))
    plt.xlabel('Gender')
    plt.ylabel('Annual Salary ($)')
    plt.title('Salary Distribution by Gender')
    plt.suptitle('')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(plt, wages):
    # side by side histograms
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

    for ax, (gender, group) in zip(axes, wages.groupby('Gender')):
        group['Salary_clean'].hist(bins=12, edgecolor='black', grid=False, ax=ax, color='mediumpurple')
        ax.set_title(f'{gender} (n={len(group)})')
        ax.set_xlabel('Annual Salary ($)')
        ax.set_ylabel('Number of Employees')

    plt.suptitle('Salary Distribution by Gender')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    There is a pretty clear gap in pay between men and women here. On average, men make around $72,301 while women make $65,737, which is a difference of about $7K.

    Both charts are right-skewed, but the chart for men shows a bigger group of high earners compared to the one for women.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    #### Analytical Question 3 (Segmented Univariant): How does salary vary across age groups?

    For this question, we created four age groups (25-30, 31-40, 41-50, 51+) to segment the salary data. This helps us understand whether more experienced (older) employees are earning more, as would be typical in most organizations.
    """)
    return


@app.cell
def _(wages):
    # salary stats by age group
    wages.groupby('Age_Group', observed=True)['Salary_clean'].describe().round(2)
    return


@app.cell
def _(wages):
    # median salary by age group
    print('Median salary by age group:')
    print(wages.groupby('Age_Group', observed=True)['Salary_clean'].median())
    print()
    print('Employee count per age group:')
    print(wages['Age_Group'].value_counts().sort_index())
    return


@app.cell
def _(plt, wages):
    # boxplot for salary by age group
    wages.boxplot(column='Salary_clean', by='Age_Group', grid=False, figsize=(9, 5))
    plt.xlabel('Age Group')
    plt.ylabel('Annual Salary ($)')
    plt.title('Salary Distribution by Age Group')
    plt.suptitle('')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(plt, wages):
    # bar chart of median salary by age group
    median_by_age = wages.groupby('Age_Group', observed=True)['Salary_clean'].median()
    median_by_age.plot(kind='bar', color='teal', edgecolor='black', rot=0)
    plt.xlabel('Age Group')
    plt.ylabel('Median Annual Salary ($)')
    plt.title('Median Salary by Age Group')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    The way age and salary relate here is pretty interesting, but it isn't just a straight line up:

    - The 25-30 age group has the lowest median at about $41,600. This makes sense since younger employees are usually just starting out in entry-level jobs.
    - The 31-40 age group jumps up to around $49,920, but it’s not as big of a raise as you might expect.
    - The 41-50 age group has the highest median at $110,240, which is a massive increase from the younger groups.
    - The 51+ group stays high but the range is much wider. This is probably because older employees can range from top executives to those who have been in production for a long time.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    #### Analytical Question 4: What does the overall distribution of employee salaries look like?

    Before we start breaking salary down by subgroups, it helps to look at the overall salary picture first. This gives us a comparison for later.
    """)
    return


@app.cell
def _(wages):
    # descriptive stats for the overall salary distribution
    wages['Salary_clean'].describe()
    return


@app.cell
def _(mo):
    mo.md(r"""
    Looking at this we can see a few things that stand out. The mean salary is $68K but the median is $52K, a $16K difference. This usually means the values are skewed by some higher numbers on the right. Also, looking at the min and max we can see the range is also huge, going from $29K to $166K. This could mean there are a wide variety of pay levels.
    """)
    return


@app.cell
def _(plt, wages):
    # histogram of overall salary
    wages['Salary_clean'].hist(bins=15, edgecolor='black', color='steelblue', grid=False)
    plt.xlabel('Annual Salary ($)')
    plt.ylabel('Number of Employees')
    plt.title('Distribution of Employee Salaries at Vandelay Industries')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(plt, wages):
    # boxplot to see spread and outliers
    wages.boxplot(column='Salary_clean', grid=False, vert=False)
    plt.xlabel('Annual Salary ($)')
    plt.title('Boxplot of Employee Salaries at Vandelay Industries')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(wages):
    # calculate the lower and upper bounds to identify outliers
    Q1 = wages['Salary_clean'].quantile(0.25)
    Q3 = wages['Salary_clean'].quantile(0.75)
    IQR = Q3 - Q1
    lower_fence = Q1 - (1.5 * IQR)
    upper_fence = Q3 + (1.5 * IQR)
    print(f'Q1: ${Q1:,.2f}')
    print(f'Q3: ${Q3:,.2f}')
    print(f'IQR: ${IQR:,.2f}')
    print(f'Lower Fence: ${lower_fence:,.2f}')
    print(f'Upper Fence: ${upper_fence:,.2f}')
    return


@app.cell
def _(mo):
    mo.md(r"""
    The histogram shows that right skew we were looking for. Most people are making under $60K, and then there is a long tail that goes all the way out to $170K.

    The boxplot confirms this. Since the upper limit is $213,200, there actually aren't any outliers. Even the CEO making $166,400 technically counts as "normal" because the data is so spread out.

    The middle 50% of workers make anywhere from $41,600 to $110,240. That is a huge gap for the middle of a company. It really shows the divide at Vandelay Industries between the regular staff and the higher-paid managers or tech roles.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    #### Analytical Question 5: What is the age distribution of Vandelay Industries's workforce?
    """)
    return


@app.cell
def _(wages):
    # age descriptive stats
    wages['Age'].describe()
    return


@app.cell
def _(plt, wages):
    # histogram of employee ages
    wages['Age'].hist(bins=12, edgecolor='black', color='coral', grid=False)
    plt.xlabel('Age (years)')
    plt.ylabel('Number of Employees')
    plt.title('Age Distribution of Vandelay Industries Employees')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(plt, wages):
    # boxplot for age
    wages.boxplot(column='Age', grid=False, vert=False)
    plt.xlabel('Age (years)')
    plt.title('Boxplot of Employee Ages at Vandelay Industries')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(wages):
    # age fences
    Q1_age = wages['Age'].quantile(0.25)
    Q3_age = wages['Age'].quantile(0.75)
    IQR_age = Q3_age - Q1_age
    lower_fence_age = Q1_age - (1.5 * IQR_age)
    upper_fence_age = Q3_age + (1.5 * IQR_age)
    print(f'Q1: {Q1_age} years')
    print(f'Q3: {Q3_age} years')
    print(f'IQR: {IQR_age} years')
    print(f'Lower Fence: {lower_fence_age} years')
    print(f'Upper Fence: {upper_fence_age} years')
    return


@app.cell
def _(wages):
    # look at how many employees fall in each age group
    wages['Age_Group'].value_counts().sort_index()
    return


@app.cell
def _(mo):
    mo.md(r"""
    The average age at Vandelay is 38, with a median of 36. Most of the workers are between 31 and 43, so the main group is basically in their 30s and early 40s. The upper limit for age is 61, but since there is one person who is 67, they technically count as an outlier.

    The histogram shows the data is right-skewed, meaning the company leans younger. This makes sense for a place with a lot of production jobs. The 31–40 group is the biggest by far, which shows that Vandelay has a lot of mid-career staff. This is actually a good thing because people have experience but aren't close to retiring yet.

    ---
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 5) Recap of all your insights.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Here is a summary of what the analysis showed for each of the five analytical questions:

    **Q1 – Salary by Department (Segmented):**
    - Sales and IT/IS are the highest-paying departments, both with median salaries over $110,000
    - Production has a median salary of about $49,000
    - The Production department accounts for 61% of all employees but has the lowest pay

    **Q2 – Salary by Gender (Segmented):**
    - There are 98 female and 76 male employees
    - Male mean salary is $72,301 and Female mean salary is $65,737
    - Male median is $56,160 and Female median is $50,440
    - Both distributions are right-skewed; males have a slightly higher share of top earners

    **Q3 – Salary by Age Group (Segmented):**
    - The 25-30 group has the lowest median salary (~$42K)
    - Salary increases with age, with the 41-50 group earning the highest median (~$110K)
    - The 51+ group has the widest salary spread, reflecting a mix of senior executives and long-tenured production workers
    - Younger employees show small salary ranges, most are in entry-level or production roles

    **Q4 – Overall Salary Distribution:**
    - Mean salary: ~$69K
    - Median salary: $52K
    - Salaries range from $29,120 to $166,400
    - Most employees earn below $60,000, but a small group of higher earners pull up the average

    **Q5 – Age Distribution:**
    - Average age is 37.8 years, median is 36 years
    - Ages range from 25 to 67
    - The IQR is 31 to 43 years, the majority of workers are in their 30s and early 40s
    - One employee (age 67) is above the upper fence of 61 and is a statistical outlier
    - The 31-40 age group is the largest

    &nbsp;

    ---
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 6) Summarize your findings for our fictitious business.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Vandelay Industries Workforce Analysis**

    After looking at the Vandelay data, a few things really stand out. Most of the 174 employees are in their 30s and 40s, which is a good mid-career mix, though they have one person at 67 who might retire soon.

    The biggest issue is the pay gap between departments. Over 60% of the staff is in Production making a median of $49K, which is less than half of what Sales or IT makes. Vandelay needs to make sure those Production wages are actually competitive so people don't quit.

    There is also a gender pay gap, with men making about $6,500 more than women on average. We can't prove it's discrimination just from this, but it’s definitely something the company should look into. Also, since pay jumps way up for people in their 40s, they might want to show younger workers a clearer path to those management roles to keep them around.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    &nbsp;

    ---

    ## References

    Anthropic. (2026, March 21). *Descriptive statistics concepts and applications*

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Generative AI chat]. Claude Sonnet 4.6. https://claude.ai/share/238a11a7-cc55-45d4-b77c-74f2a281b981

    &nbsp;
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---

    ## Appendix: AI-Generated Content

    **Tool:** Claude Sonnet 4.6 (Anthropic)

    **Date:** March 24, 2026

    **Topic:** Descriptive statistics concepts and applications

    &nbsp;
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Prompt Submitted to AI:
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Could you make me a list of the concepts in  2_DescriptiveStatistics_DerivingInsights.py and describe what each one is used for and how it works? put them in numerical order. provide the results in a markdown file with code windows for example code snippets when appropriate
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### AI Response:
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Viewed 2 filesViewed 2 filesNow I have a full picture of the file. Let me create the markdown document.Created a file, read a fileCreated a file, read a fileHere's your reference guide with all 19 concepts from the notebook, numbered and in order of appearance. Here's a quick breakdown of what's covered:

    1–3 cover the foundational theory — what descriptive statistics is, and the categorical vs. numerical data taxonomy (nominal, ordinal, discrete, continuous).

    4–8 cover the analytical design process — problem statements, analytical questions, and the difference between univariate, segmented univariate, and multivariate analysis.

    9–12 cover the core pandas tools used in the demo — loading data, value_counts(), describe(), and groupby().

    13–17 cover the statistical and visual techniques applied — histograms, boxplots, IQR, outlier fences, and the bimodal distribution observation.

    18–19 cover the supporting libraries — Altair for interactive charting and Marimo for the reactive notebook interface.

    Each entry includes a plain-language explanation plus code snippets pulled directly from the notebook where applicable.
    """)
    return


if __name__ == "__main__":
    app.run()
