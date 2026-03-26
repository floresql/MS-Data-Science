# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "pandas>=3.0.1",
#     "pyzmq>=27.1.0",
#     "seaborn>=0.13.2",
#     "altair>=5.0.1",
#     "matplotlib>=3.7.1",
#     "vega_datasets>=0.9.0",
#     "vegafusion>=2.0.3",
#     "vl-convert-python>=1.9.0.post1",
#     "pyarrow>=23.0.1",
#     "mistune>=3.2.0",
#     "plotly>=6.6.0",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import subprocess

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 2 - Deriving Insights through Descriptive Statistics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Book Recommendation**: Both of these books are great references that provide working examples in python.

    <img align="left" style="padding-right:50px;" src="figures_wk2/pandas_everyone.png" width=100><br>
    >**Pandas for Everyone - Python Data Analysis** by Daniel Y. Chen<br>
    >**Publisher**: Addison-Wesley - Data &Analytics Series; 2nd edition (2023)<br>
    >**ISBN-13**: 978-0137891153<br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:50px;" src="figures_wk2/eda_with_python.png" width=100><br>
    >**Hands-On Exploratory Data Analysis with Python** by Suresh Kumar Mukhiya and Usman Ahmed <br>
    >**Publisher**: Packt>; 1st edition (2020)<br>
    >**ISBN-13**: 978-1789537253<br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lecture Outline
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Descriptive Statistics - Drawing Insights from Descriptive Statisitcs
    - What is Descriptive Statistics?
    - Understanding You Data
        * Categorical vs Numeric Data
        * Why is knowing the data type important
    - Designing Your Analytical Approach
        * Understand the Business and Defining the Problem Statement
        * Development of Analytical Questions
        * Univariate vs Multivariate Analysis
    - Demo: Analyzing a dataset through Desciptive Statistics
        * Understanding the Business and Defining a Problem Statement
        * Loading the data
        * Developing our Analytical Approach
        * Anaylsis: Customer Loyality
        * Anaylsis: Foot Traffic
        * Insight Recap: What has our analysis revealed?
        * Summarizing the Analysis
    - Additional Note About Univariant Analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What is Descriptive Statistics?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Descriptive statistics serves as the initial step in understanding and summarizing data. It involves organizing, visualizing, and summarizing raw data to create a coherent picture. The primary goal of descriptive statistics is to provide a clear and concise overview of the data’s main features. This helps us identify patterns, trends, and characteristics within the data set without making broader inferences.

    Using descriptive statistics techniques, data can become clearer, patterns might emerge, and some conclusions might be evident. However, descriptive statistics do not allow us to reach any conclusion beyond the data being analyzed. For this reason, descriptive statistics are often not useful for decision-making processes. However, descriptive statistics still hold value in explaining high-level summaries of a set of information such as the mean, median, mode, variance, range, frequencies and proportions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Understanding Your Data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before diving into any analytical effort, it is crucial to identify the data type under analysis. Different disciplines store different kinds of data for different purposes. For example, medical researchers store patients' data, universities store students' and teachers' data, and real estate industries store building and property datasets.

    A dataset contains many observations about a particular object. For instance, a dataset about patients in a hospital can contain many observations. A patient can be described by a patient identifier (ID), name, address, weight, date of birth, address, email, and gender. Each of these features that describes a patient is a variable. Each observation can have a specific value for each of these variables. For example, a patient can have the following:

    >PATIENT_ID = 1001 <br>
    Name = Yoshmi Mukhiya <br>
    Address = Mannsverk 61, 5094, Bergen, Norway <br>
    Date of birth = 10th July 2018 <br>
    Email = yoshmimukhiya@gmail.com <br>
    Weight = 10  <br>
    Gender = Female <br>

    These datasets are stored in hospitals and are presented for analysis. Most of this data is stored in some sort of database management system in tables/schema.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Catergorical vs Numeric Data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:50px;" src="figures_wk2/kinds_data.png" width=550><br>
    Most data broadly falls into one of two groups: categorical and numerical data.

    * **Categorical Data:** Qualitative data is also known as categorical data, and it measures data represented by a name or symbol. Examples include the names of each department in your organization, office locations, and many other categorical data names.
        - **Nominal Data:** Nominal data are categories or named data with no inherent hierarchy or structure. They explain the category without any order. If you had an e-commerce shopping store, this could be the different clothing categories you offer (i.e., shoes, tops, pants, etc.). You could categorize and analyze the different nominal data to understand your business offerings.
        Ordinal Data:** Ordinal data demonstrates a specific order, hierarchy, or understood structure through the categorical names. This could be demonstrated through job titles, such as assistant, manager, or director—these are all names that denote a specific position in the company that is understood by its categorical name.

    * **Numerical Data:**  Also known as quantitative data, its values will always be in a number form. An example of numerical data would be the number of sales made in a particular business quarter. Put simply, if the answer is a number, the data is quantitative (numerical).
        - **Discrete Data:** Discrete data, also called discrete values, is data that only takes certain values. Commonly in the form of whole numbers or integers, this data can be counted and has a finite number of values. These values must be able to fall within certain classifications and are unable to be broken down into smaller parts.
        - **Continous Data:** Continuous data refers to data that can be measured. This data has values that are not fixed and have an infinite number of possible values. These measurements can also be broken down into smaller individual parts. Some examples of continuous data would include the height or weight of a person. Continuous data can be further broken down.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Why is knowing the data type important?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Different data types require different analytical techniques. Choosing the appropriate analysis method depends on the data types involved.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:50px;" src="figures_wk2/nominal_ordinal.png" width=600><br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:50px;" src="figures_wk2/discrete_continuous.png" width=600><br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Designing Your Analytical Approach
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:50px;" src="figures_wk2/arrows.png" width=200><br>
    Show of hands, who believes that the most crucial aspect of an analytics effort is the data. If you raised your hand, I have some sad news for you. Along with your data, you also need a plan or approach for your analytics.
    > **"If you aim at nothing, you will hit it every time"** ~ Zig Ziglar.

    Factors such as the type of analysis, the goal, and the specific questions you want to answer are all important.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Understand the Business and Defining the Problem Statement
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:50px;" src="figures_wk2/crisp_dm.png" width=350><br>
    Any good project starts with a deep understanding of the customer’s needs. [CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/) is a methodology readily used in the data science community to guide a researcher's analytical efforts.

    During the **Business Understanding** phase the focus centers around understanding the objectives and requirements of the project. One of the steps within this phrase is defining the analytical objectives, also known as the problem statement, for the analysis.

    **Problem Statement:** Before trying to extract useful insight from the data, it is essential to define the business problem to be solved. The problem definition works as the driving force for a data analysis plan execution.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Development of Analytical Questions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Once the problem statement has been established, one or more analytical questions can be developed to further guide the analysis. It is important to ensure that each analytical question supports the business problem defined in the problem statement.

    <img align="center" style="padding-right:50px;" src="figures_wk2/analytical_questions.png" width=600><br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Univariate vs Multivariate Analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:50px;" src="figures_wk2/question2feature.png" width=350><br>
    After establishing the analytical questions associated with your analysis, you now need to identify the variables within your dataset.

    **Univariate analysis** utilizes only one variable from the dataset in deriving insights. Univariant analysis is used to identify characteristics of a single trait and is not used to analyze any relationships or causations.

    For example, imagine a room full of high school students. Say you wanted to gather the average age of the individuals in the room. This univariate data is only dependent on one factor: each person's age. By gathering this one piece of information from each person and dividing by the total number of people, you can determine the average age.

    **Multivariant analysis** utilized more than one dataset variable during the analysis. Multivariant analysis examines the individual variables and their relationships to each other.

    As an example, let's say each high school student in the example above takes a college assessment test, and we want to see whether older students are testing better than younger students. In addition to gathering the age of the students, we need to gather each student's test score. Then, using data analytics, we mathematically or graphically depict whether there is a relationship between student age and test scores.

    <i><b> Did you notice</b></i>, in the visual for this section, that not all of data variables supported the anaytical questions being analyzed? Also, the last analytical question wasn't supported by any of the dataset variables. <u>This is why designing your analytical approach is so important.</u>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Demo: Analyzing a Dataset Through Descriptive Statistics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For this demonstration, we will be using a retail transactions dataset for a bakery. We will start by loading and looking at a sample of the data.

    In addition to examining the dataset within this notebook, I also looked at this dataset in a text editior outside of this notebook to inspect the entire dataset.

    **Dataset Variables:**<br>
    Based on that inspection, I was about to determine the dataset features are:
    - order_id: unique identifier of the dataset
    - customer_id: unique identifier for each customer
    - order_date: date of the sales transactions
    - quantity: the number of items in the sales transaction
    - product_id: the item sold in the sales transaction
    - unit_price: the price of the individual item being sold
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Loading the Data
    """)
    return


@app.cell
def _():
    import pandas as pd
    import seaborn as sns

    return pd, sns


@app.cell
def _(pd):
    bakery = pd.read_csv('data_wk2/transactions.csv')
    return (bakery,)


@app.cell
def _(bakery):
    bakery.sample(10)
    return


@app.cell
def _(bakery):
    bakery.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Developing our Analytical Approach
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since we are working with a generic dataset, we will develop a fictious business scenario and business problem that is supported by our dataset.

    **Business Understanding and Problem Statement:** <br>
    HoneyBee Sweet Shop opened for business in January 2018. HoneyBee Sweet Shop specializes in offering bakery items sweetened with locally sourced honey rather than sugar. Recently, HoneyBee Sweet Shop reached its 100,000th sale. As a niche bakery, HoneyBee Sweet Shop wants to understand how well their 100% honey-sweetened products are being received across their targeted market. In particular, HoneyBee Sweet Shop would like to understand their customer’s loyalty to their brand and foot traffic over those first 100,000 transactions.

    **Analytical Questions:** <br>
    - Customer Loyalty: How often does each HoneyBee Sweet Shop customer visit the bakery?
    - Foot Traffic: What is the range of sales per business day?

    **Identification of dataset features for analysis:**
    - Customer Loyalty: customer_id
    - Foot Traffics: order_date
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Anaylsis: Customer Loyality
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Based on our analytical approach defined above, to gain insights about the loyalty amongst HoneyBee Sweet Shop’s customers, we can conduct a univariant analysis of the customer_id dataset feature and descriptive statistics.

    We will start by grouping the customer_id by the values contained in this variable. Since a unique customer_id was assigned to each customer, this will provide the number of times each customer has visited HoneyBee Sweet Shop.
    """)
    return


@app.cell
def _(bakery, mo):
    mo.ui.dataframe(bakery)
    return


@app.cell
def _(bakery):
    bakery.customer_id.value_counts()
    return


@app.cell
def _(bakery):
    bakery.groupby('customer_id').order_id.size().sort_values()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Okay, so it looks like the number of times a customer has visited HoneyBee Sweet Shop ranges between 1 and 12.
    """)
    return


@app.cell
def _(bakery):
    bakery.groupby('customer_id').order_id.size()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Based on this information, we can see that HoneyBee Sweet Shop has interacted with 33,039 different customers during their first 100,000 sales transactions. The number of visits for each customer ranges between one and twelve times.

    Let's create a histogram for HoneyBee Sweet Shop's customer's visits.
    """)
    return


@app.cell
def _(bakery):
    #note that you'll need to install in command prompt:
    import matplotlib.pyplot as plt
    import numpy as np
    freq_customers = bakery.groupby('customer_id').order_id.size()
    freq_customers.hist(bins=13, grid=False, edgecolor='black')
    plt.xlabel('Number of Orders')
    plt.ylabel('Number of Customers')
    plt.title('Distribution of Orders per Customer')
    plt.show()
    return (freq_customers,)


@app.cell
def _(bakery):
    import altair as alt
    hist= alt.Chart(bakery.groupby('customer_id').order_id.size().reset_index(name='order_count')).mark_bar().encode(
        x=alt.X('order_count:Q', bin=alt.Bin(maxbins=20)),
        y='count()'
    ).properties(
        title='Distribution of Orders per Customer'
    )
    hist
    return alt, hist


@app.cell
def _(hist, mo):
    #display in marimo
    chart=mo.ui.altair_chart(hist, chart_selection=True, legend_selection=False)
    mo.vstack([chart, mo.ui.table(chart.value)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    That interesting, it appears that visitng over 6 times is an outlier. Let's confirm this assumption with a boxplot.
    """)
    return


@app.cell
def _(alt, bakery):
    #create a boxplot to visualize the distribution of order counts per customer in marimo
    alt.data_transformers.enable("vegafusion")
    boxplot = alt.Chart(bakery.groupby('customer_id').order_id.size().reset_index(name='order_count')).mark_boxplot().encode(
        y='order_count:Q'
    ).properties(
        title='Boxplot of Orders per Customer'
    )
    boxplot

    return


@app.cell
def _(freq_customers, sns):
    sns.boxplot(x=freq_customers.values)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The boxplot suggests that for a customer to visit over 7 times would be unlikely and 25% of those customers only visiting once. Plus, half of their customers visited HoneyBee Sweet Shop between two and four times. Additionally, 50% of the HoneyBee Sweet Shop customers visited between 2 and 4 times with the median being 3 visits.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Anaylsis: Foot Traffic
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similar to our analysis of customer loayalty, for the investigation into the foot traffic at HoneyBee Sweet Shop we can conduct a univariant analysis of the feature order_date. The data within this feature will be grouped to determine the total sales per business day at HoneyBee Sweet Shop.
    """)
    return


@app.cell
def _(bakery):
    bakery.order_date.min()
    return


@app.cell
def _(bakery):
    bakery.order_date.max()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, roughly 33 months. What has the average number of sales per day been like?
    """)
    return


@app.cell
def _(bakery):
    sales= bakery.order_date.value_counts()
    sales.describe()


    return (sales,)


@app.cell
def _(bakery, sales):
    #add sales variable to bakery df
    bakery['sales'] = bakery.order_date.map(sales)
    return


@app.cell
def _(alt, bakery):
    #create a hisotogram of sales
    sales_hist=alt.Chart(bakery).mark_bar().encode(
        x=alt.X('sales', bin=alt.Bin(maxbins=6)),
        y='count()'
    ).properties(
        title='Distribution of Sales per Day'
    )
    sales_hist
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Good News! HoneyBee Sweet Shop has had sales everyday, with the daily sales totals ranging between 51 and 107.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The daily sales histogram, depicts a slightly bimodal distribution with the two peaks within the IQR. This behavior typically means that an average day at HoneyBee Sweet Shop is more likely to fall closer to 71 or 83 rather than the median of 77 sales transactions. Additionally, the sharply declining tails indicate the possible presence of outliers within the daily sales totals.
    """)
    return


@app.cell
def _(alt, bakery):
    #create a box plot of sales
    sales_boxplot=alt.Chart(bakery).mark_boxplot().encode(
        y='sales'
    ).properties(
        title='Boxplot of Sales per Day'
    )
    sales_boxplot
    return


@app.cell
def _(bakery):
    Q1 = bakery.groupby('order_date').size().quantile(q=.25)
    Q3 = bakery.groupby('order_date').size().quantile(q=.75)
    LF = Q1 - (1.5 * (Q3-Q1))
    UF = Q3 + (1.5 * (Q3-Q1))
    print ('lower:', LF,' upper:',UF)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The boxplot confirms the presence of outliers at both ends of the daily sales transactions. To better understand those outliers, the lower and upper fences (whiskers in the plot) are calculated. The lower and upper fences are deemed to be 1.5 times the IQR away from the median value, showing that HoneyBee Sweet Shop’s expected range of daily transactions is between 53 and 101.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Insight Recap: What has our analysis revealed?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Analysis of customer loyalty**
    - there are 33,039 unique customers
    - the number of times an individual customer visited ranged between 1 and 12 times
    - 1/4 of those customers only visited once
    - the median number of visits was 3
    - IQR is between 2 and 4 visits - accounts for 50% of the customers.
    - outliers visits existed at 8 and above

    **Analysis of foot traffic**
    - sales range from 01/01/2018 through 09/09/2020 - accounts for 1297 unique sales dates
    - min number of sales per day is 51 and max number is 107
    - mean number of sales is 77
    - IQR is between 71 and 83 sales
    - sales outside of 53 and 101 would be considered rare and unusual
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Summarizing the Analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So what would you report back to HoneyBee Sweet Shop? The trick here is to summarize your insights into a concise and descriptive format.

    **Report to HoneyBee Sweet Shop**
    In your first 33 months of business, HoneyBee Sweet Shop attracted just over 33,000 customers. Despite being about to attract new customers to your bakery, custormer loyalty to your brand appears to be relatively low. The data showed that that 50% of our customers visited between 2 and 4 times during those 33 months. Additionally, 25% of your customers only visited the bakery once during this time period. While some customers visited the bakery more frequently, our analysis found that for a customer to visit over 7 times would be a rare and unlikely event.

    There appears to be a steady flow of customers visiting HoneyBee Sweet Shop each day. Our analysis showed the expected range of daily sales to be between 53 and 101. However, a more realistic daily sales range would be between 71 and 83, which aligns with 50% of the dates within the dataset.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Additional Note About Univariant Analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    While the primary analytical techniques used in univariate analysis involve calculating summary statistics, generating frequency distributions, and feature visualizations, several approaches exist in univariant analysis.

    In the demo above, we saw two different appraoches:
    1) For the foot traffic analysis, the feature order_date was used.
    2) For the customer loyalty, we analyzed the results of grouping the feature customer_id.

    The approach used for analyzing customer loyalty is known as a **Segmented Univariant Analysis***. Segmented univariant analysis summarizes data segments, permitting the detection of patterns within the subsets across the various segments. This can be accomplished by grouping the feature to be analyzed or utilizing other feature(s) in the dataset to segment the data before analysis.
    """)
    return


if __name__ == "__main__":
    app.run()
