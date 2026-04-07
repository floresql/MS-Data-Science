# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "altair>=6.0.0",
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

__generated_with = "0.20.4"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 4 - Inferential Statistics - Hypothesis Testing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:70px;" src="figures_wk4/inferential_stats.png" width=450><br>
    A couple weeks ago, we investigated the use of descriptive statisitcs to drawing insights from a dataset. This week, we will turn our attention to hypothesis testing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Difference Between Descriptive and Inferential Statisitcs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Descriptive statistics organize, summarize, and display the characteristics of a data set using bar graphs, histograms, or pie charts. They involve the measures of central tendency: Mean, Median, and Mode, measures of dispersion as the tools, and measures of variability: Range, variance, and standard deviation.

    Inferential statistics allow us to test a hypothesis and assess whether the data is generalizable to the broader population. Sample data is also used to make inferences and draw conclusions about the people, and the results are in the form of probability.

    | Descriptive Statistics | Inferential Statististics |
    |:----------------------|:-------------------------|
    |Describe the features of populations and/or samples|Use samples to make generalizations about larger populations|
    |Organize and present data in a purely factual way|Help us to make estimates and predict future outcomes|
    |Present final results visually, using tables, charts, or graphs|Present final results in the form of probabilities|
    |Draw conclusions based on known data|Draw conclusions that go beyond the available data|
    |Use measures like central tendency, distribution, and variance|Use techniques like hypothesis testing, confidence intervals, and regression and correlation analysis|
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What is Inferential Statistics?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Inferential statistics can be defined as a field of statistics that uses analytical tools for drawing conclusions about a population by examining random samples. The goal of inferential statistics is to make generalizations about a population. In inferential statistics, a statistic is taken from the sample data (e.g., the sample mean) that used to make inferences about the population parameter (e.g., the population mean).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sampling Techniques
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:70px;" src="figures_wk4/sampling.png" width=400>

    In order to pick out random samples that will represent the population accurately many sampling techniques are used. Some of the comon sampling techniques are:
    * **Simple Random Sampling:** every member of the population has an equal chance of being selected. Your sampling frame should include the whole population<br>
    * **Systematic Sampling:** every member of the population is listed with a number, but instead of randomly generating numbers, individuals are chosen at regular intervals.<br>
    * **Stratified Sampling:** involves dividing the population into subpopulations that may differ in important ways. It allows you draw more precise conclusions by ensuring that every subgroup is properly represented in the sample <br>
    * **Cluster Sampling:** involves dividing the population into subgroups, but each subgroup should have similar characteristics to the whole sample. Instead of sampling individuals from each subgroup, you randomly select entire subgroups<br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Types of Inferential Statistics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:50px;" src="figures_wk4/inferential_types.png" width=300><br>
    Inferential statistics can be classified into hypothesis testing and regression analysis. Hypothesis testing also includes the use of confidence intervals to test the parameters of a population. Given below are the different types of inferential statistics.

    **Hypothesis testing** is a type of inferential statistics that is used to test assumptions and draw conclusions about the population from the available sample data. It involves setting up a null hypothesis and an alternative hypothesis followed by conducting a statistical test of significance. A conclusion is drawn based on the value of the test statistic, the critical value, and the confidence intervals.

    **Regression analysis** is used to quantify how one variable will change with respect to another variable. There are many types of regressions available such as simple linear, multiple linear, nominal, logistic, and ordinal regression. The most commonly used regression in inferential statistics is linear regression. Linear regression checks the effect of a unit change of the independent variable in the dependent variable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Driven Decision Making
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Data-driven decision-making (DDDM) is defined as using facts, metrics, and data to guide strategic business decisions that align with your goals, objectives, and initiatives. When organizations realize the full value of their data, that means everyone is empowered to make better decisions with data, every day.

    <img align="left" style="padding-right:50px;" src="figures_wk4/hypothesis_steps.png" width=350>

    There are four steps in data-driven decision making:
    1) First, you must formulate a hypothesis.
    2) Second, once you have formulated a hypothesis, you will have to find the right test for your hypothesis.
    3) Third, you execute the test.
    4) Fourth, you make a decision based on the result.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hypothesis Testing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The real value of hypothesis testing in business is that it allows professionals to test their theories and assumptions before putting them into action. This essentially allows an organization to verify its analysis is correct before committing resources to implement a broader strategy.

    Remember, hypothesis testing is used to assess the plausibility of a hypothesis by using sample data. The test provides evidence concerning the plausibility of the hypothesis, given the data. Statistical analysts test a hypothesis by measuring and examining a random sample of the population being analyzed.

    An Example of Hypothesis Testing: You say an average student in the class is 25 years old or a boy is taller than a girl. All of these is an assumption that we are assuming and we need some statistical way to prove these. We need some mathematical conclusion whatever we are assuming is true.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What is a Hypothesis?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-left:50px;" src="figures_wk4/what_hypothesis.png" width=300>

    What is a hypothesis? Though there are many ways to define it. The most intuitive I've seen is, a hypothesis is an idea that can be tested. This is not the formal definition, but it explains the point very well.

    So if I tell you that apples in New York are expensive, this is an idea or a statement, but it's not testable until I have something to compare it with. For instance, if I define expensive as any price higher than $1.75 per pound, then it immediately becomes a hypothesis.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Null and Alternative Hypothesis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="center" style="padding-right:10px;" src="figures_wk4/Ho_Ha.png" width=650><br>

    In statistics, the null hypothesis (H0) is a general given statement or default position that there is no relationship between two measured cases or no relationship among groups. In other words, it is a basic assumption or made based on the problem knowledge.
               Example: A company production is = 50 units/per day etc.

    The alternative hypothesis (HA or H1) is the hypothesis used in hypothesis testing that is contrary to the null hypothesis.
               Example: A company’s production is not equal to 50 units/per day etc.

    Let's take a look at an example, According to Glassdoor, the popular salary information website, the median data scientist salary in the US is \$155,000 (as of April, 2025). So, we want to test if their estimate is correct. There are two hypotheses that are made, the null hypothesis denoted H0. And the alternative hypothesis denoted H1 or HA. The null hypothesis is the one to be tested, and the alternative is everything else. In our example, the null hypothesis would be the median data scientist salary is \$155,000. While the alternative, the median data scientist salary is not \$155,000.

    Now, you would want to check if \$155,000 is close enough to the true median predicted by our sample, in case it is you would fail to reject the null hypothesis, otherwise, you would reject the null hypothesis. The concept of the null hypothesis is similar to innocent until proven guilty. We assumed that the median salary is \$155,000. And we try to prove otherwise.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Type I and Type II Errors
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="left" style="padding-right:10px;" src="figures_wk4/type1_type2.png" width=500><br>
    The process of distinguishing between the **null hypothesis** and the **alternative hypothesis** is aided by considering two conceptual types of errors.

    The first type of error occurs when the null hypothesis is wrongly rejected. The second type of error occurs when the null hypothesis is wrongly not rejected. (The two types are known as **Type I and Type II Errors**.)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Significance Level and P-value
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Normally, we aim to reject the null if it is false. However, as with any test, there is a small chance that we could get it wrong and reject a null hypothesis that is true. The significance level is denoted by $\alpha$ and is the probability of rejecting the null hypothesis if it is true, so, the probability of making this error. Typical values for alpha are 0.01, 0.05 and 0.1. It is a value that you select based on the certainty you need. In most cases, the choice of alpha is determined by the context you are operating in, but 0.05 is the most commonly used value.

    *P-value* is the probability of finding the observed/extreme results when the null hypothesis(H0) of a study-given problem is true. If your *p-value* is less than the chosen significance level then you reject the null hypothesis i.e. your sample claims to support the alternative hypothesis. No matter if we are dealing with the normal Students-T binomial or uniform distribution. Whatever the test, the *p-value* rationale holds. If the *p-value* is lower than the level of significance, you reject the null hypothesis.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Common Types of Hypothesis Tests
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are a number of types of test that can be used in hypothesis testing, the selection of test depends of what you are testing for and the sample drawn from your population.

    1. **Tests for Comparing Means**:
        - One-sample z-test: This test is used to compare the mean of a sample to a known population mean. It is used when the population variance is known, or the sample size is large (n ≥ 30).<br>
        - Two-sample z-test: This test is used to compare the means of two independent samples. It is used when the population variances are known, or the sample sizes are large (n ≥ 30). <br>
        - One-sample t-test: This test is used to compare the mean of a sample to a known population mean. It is used when the population variance is unknown, and the sample size is larger than 30 (n > 30). <br>
        - Two-sample t-test: This test is used to compare the means of two independent samples. It is used when the population variances are unknown, and the sample sizes is larger than 30 (n > 30). <br>
        - Paired t-test: This test is used to compare the means of two related samples, such as the before and after measurements of the same group of subjects. It is used when the population variances are unknown, and the sample size is larger than 30 (n > 30).<br>
    2. **Tests for Comparing Proportions** <br>
        - One-sample proportion test: This test is used to compare the proportion of a sample to a known population proportion.  The normal approximation is used when both np≥10 and n(1−p)≥10 (data should have at least 10 "successes" and at least 10 "failures"). <br>
        - Two-sample proportion test: This test is used to compare the proportions of two independent samples. The normal approximation is used when both np≥10 and n(1−p)≥10 (data should have at least 10 "successes" and at least 10 "failures" ). <br>
    3. **Tests for Comparing Variance** <br>
        - Chi-square test for variance: This test is used to compare the variance of a sample to a known population variance. <br>
        - F-test for variance: This test is used to compare the variances of two independent samples.<br>
    4. **Other Common Tests**<br>
        - Goodness of fit test: This test is used to determine whether a sample fits a specific distribution. It is used to compare the observed frequencies of a categorical variable to the expected frequencies under a particular distribution. <br>
        - Testing for independence of two attributes (Contingency Tables): This test is used to determine whether there is a relationship between two categorical variables. It is often used in the form of a chi-square test, which compares the observed frequencies in a contingency table to the expected frequencies under the assumption of independence. <br>
        - ANOVA (Analysis of Variance): This test is used to compare the means of three or more independent samples. It is used to determine whether there is a significant difference between the means of the groups. <br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Is your data normal?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <img align="right" style="padding-right:10px;" src="figures_wk4/normal_data.png" width=370><br>
    Most hypothsesis tests make an assumption about the distribution of the underlying data is normally distributed,and we’re often told that we must carefully check the assumptions!

    There are a number of techniques that you can use to check if your data sample is normally or sufficiently normal to use standard techniques (ie: hypothesis testing).
    * **Graphical Methods**: These are methods for plotting the data and qualitatively evaluating whether the data looks "normally distributed".
    * **Statistical Tests**: These are methods that calculate statistics on the data and quantify how likely it is that the data was drawn from a normal distribution.

    Methods of this type are often called normality tests.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Hypothesis Testing Process
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we have discussed before, there is no single way to approach analytics. However, here is a general guideline to Hypothesis Testing:
    * Collect your data
    * Define your null and alternative hypothesis
    * Determine your alpha
    * Check the distribution of your data
    * Calculate some test statistic and compare to alpha
    * Draw a conclusion about Ho (reject or fail to reject)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Demo: Normality Test of a Dataset
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As stated above, there are a number of techniques that we can use to check to see whether our dataset is normally distributed or not.  For this demo, we will be following along with [A Gentle Introduction to Normality Tests in Python](https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/) tutorial.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Generate a Dataset
    Before we start looking at normality tests, let’s first develop a test dataset that we can use throughout this tutorial.
    """)
    return


@app.cell
def _():
    # some of the common imports that we will need
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    import pandas as pd
    #%pip install statsmodels

    # '%matplotlib inline' command supported automatically in marimo
    sns.set_theme()
    return mo, np, pd, plt, sns


@app.cell
def _(pd):
    # generate normally distributed data
    from numpy.random import seed
    from numpy.random import randn
    from numpy import mean
    from numpy import std

    # seed the random number generator
    seed(1)

    # generate univariate observations
    data = 5 * randn(100) + 50

    #convert to pandas dataframe
    data = pd.DataFrame(data, columns=['value'])
    return (data,)


@app.cell
def _(data, mo):
    # describe the distribution of the data in marimo way
    mo.ui.tabs(
        {
            "data": mo.lazy(mo.ui.table(data.describe()))
        }
    )
    return


@app.cell
def _(data):
    len(data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Graphical Normality Checks
    We can create plots of the data to check whether it is Gaussian (aka normally distributed)

    These checks are qualitative, so less accurate than the statistical methods we will calculate in the next section. Nevertheless, they are fast and like the statistical tests, must still be interpreted before you can make a call about your data sample.

    #### Histogram Plot
    A simple and commonly used plot to quickly check the distribution of a sample of data is the histogram.
    """)
    return


@app.cell
def _(data, plt):
    # histogram plot
    plt.hist(data)
    return


@app.cell
def _(data):
    import altair as alt
    # create a histogram of the data
    hist1 = alt.Chart(data).mark_bar().encode(
        alt.X("value", bin=True),
        y='count()',
    )
    hist1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can see a Gaussian-like shape to the data, that although is not strongly the familiar bell-shape, is a rough approximation.

    <div class="alert alert-block alert-success">
    <b>Helpful Hint::</b> I prefer seaborn for displaying graphical information. Let's see the difference between matplotlib, altair and seaborn.
    </div>
    """)
    return


@app.cell
def _(data, sns):
    # histogram plot - the kde argument adds the line to show the general shape of the distribution
    sns.displot(data,kde=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I've found that the seaborn plots are just nicer overall.

    #### Normal Probability Plot
    The normal probability plot is a graphical technique for assessing whether or not a data set is approximately normally distributed.

    The data are plotted against a theoretical normal distribution in such a way that the points should form an approximate straight line. Departures from this straight line indicate departures from normality.

    The normal probability plot is a special case of the probability plot. We cover the normal probability plot separately due to its importance in many applications.
    """)
    return


@app.cell
def _(data, plt):
    #create normal probability plot of the data
    from scipy import stats
    stats.probplot(data['value'], dist="norm", plot=plt)
    plt.show()
    return (stats,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are a few small deviations, especially at the bottom of the plot, which is to be expected given the small data sample.

    ### Statistical Normality Tests
    There are many statistical tests that we can use to quantify whether a sample of data looks as though it was drawn from a normal distribution.

    Each test makes different assumptions and considers different aspects of the data. However, each of these tests returns at least two things:
    * **Statistic**: A quantity calculated by the test that can be interpreted in the context of the test via comparing it to critical values from the distribution of the test statistic.
    * **p-value**: Used to interpret the test, in this case whether the sample was drawn from a normal distribution.

    Each test calculates a test-specific statistic. This statistic can aid in the interpretation of the result, although it may require a deeper proficiency with statistics and a deeper knowledge of the specific statistical test. Instead, the p-value can be used to quickly and accurately interpret the statistic in practical applications.

    The tests assume that that the sample was drawn from a normal distribution. Technically this is called the null hypothesis, or Ho. A threshold level is chosen called alpha, typically 5% (or 0.05), that is used to interpret the p-value.

    In the SciPy implementation of these tests, you can interpret the p-value as follows.

    * ***p* <= alpha**: reject Ho, not normal.
    * ***p* > alpha**: fail to reject Ho, normal.

    This means that, in general, we are seeking results with a larger p-value to confirm that our sample was likely drawn from a normal distribution.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Shapiro-Wilk Test
    The Shapiro-Wilk test evaluates a data sample and quantifies how likely it is that the data was drawn from a Gaussian distribution, named for Samuel Shapiro and Martin Wilk.

    In practice, the Shapiro-Wilk test is believed to be a reliable test of normality, although there is some suggestion that the test may be suitable for smaller samples of data, e.g. thousands of observations or fewer.
    """)
    return


@app.cell
def _(data, mo):
    from scipy.stats import shapiro
    stat, p = shapiro(data)
    # normality test
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    _alpha = 0.05
    #make criterion based on the p-value
    criterion = "Reject null hypothesis" if p < 0.05 else "Fail to reject null hypothesis"
    # display the decision in markdown tool
    mo.md(f"### Shapiro-Wilk Test Result: {criterion}")

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Demo: Hypothesis Testing
    As stated above, hypothesis testing is a statistical method that is used in making statistical decisions using experimental data. In this demo we will demostrate several different types of hypothesis testing.

    ### T-test
    A t-test is a type of inferential statistic which is used to determine if there is a significant difference between the means of two groups which may be related in certain features. It is mostly used when the data sets, like the set of data recorded as outcome from flipping a coin a 100 times, would follow a normal distribution and may have unknown variances. T- test is used as a hypothesis testing tool, which allows testing of an assumption applicable to a population.

    T-test has 2 types <br>
    1. one sampled t-test
    2. two-sampled t-test.

    #### One Sample T-test
    The One Sample T-test determines whether the sample mean is statistically different from a known or hypothesised population mean.

    Example: You have 14 ages and you are checking whether average age is 30 or not.
    """)
    return


@app.cell
def _(mo, np):
    from scipy.stats import ttest_1samp
    ages = [32, 34, 29, 29, 22, 39, 38, 37, 38, 36, 30, 26, 22, 22]
    print(f'Ages: {ages}')
    ages_mean = np.mean(ages)
    print(f'Mean: {ages_mean}')
    tset, _pval = ttest_1samp(ages, 30)
    print(f'p-value: {_pval}')
    #make decision based on p-value
    decision = "Reject null hypothesis" if _pval < 0.05 else "Fail to reject null hypothesis"

    #display the decision in markdown tool
    mo.md(f'## Decision: {decision}')

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, what does all of that mean. The results show that the p-value (.5605) is greater than our defined alpha(α) of .05. This suggests that the null hypothesis(Ho) cannot not be rejected, and the average age of our dataset **is not significantly different** than 30. Even though the calculated mean is 31.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Paired Sampled T-test
    The paired sample T-test is also called dependent sample t-test. It’s a univariate test that tests for a significant difference between 2 related variables.

    * H0: mean difference between two samples is 0
    * H1: mean difference between two samples is not 0

    For this exercise, we have 10 athletes that were tested before and after the same coach used a new training method.   Our first test will be to compare the effectiveness of the new training method. For this comparison, Ho = there was no improvement from the new training method.
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('data_wk4/coaching.csv')
    df
    return (df,)


@app.cell
def _(df, mo, stats):
    #paired t-test
    _ttest, _pval = stats.ttest_rel(df['before'], df['after'])
    print(f'p-value: {_pval}')
    print(f'stat: {_ttest}')
    #make decision based on p-value
    decision_t = "Reject null hypothesis" if _pval < 0.05 else "Fail to reject null hypothesis"
    #display the decision in markdown tool
    mo.md(f'## Decision: {decision_t}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since the p-value > 0.05, we do not reject Ho.  This means that the new training method **did not significantly** impact the athlete’s performance, positively or negatively.  There was no overall change.

    Let's take a look at another example. This time we will look at the blood pressure of individuals before and after some sort of a treatment.
    """)
    return


@app.cell
def _(pd):
    df2 = pd.read_csv('data_wk4/blood_pressure.csv')
    df2
    return (df2,)


@app.cell
def _(df2, mo, stats):
    #paired t-test
    _ttest1, _pval1 = stats.ttest_rel(df2['bp_before'], df2['bp_after'])
    print(f'p-value: {_pval1}')
    print(f'stat: {_ttest1}')
    if _pval1 < 0.05:
    #make decision based on p-value
        decision_bp = "Reject null hypothesis"
    else:
        decision_bp = "Fail to reject null hypothesis"
    #display the decision in markdown tool
    mo.md(f'## Decision: {decision_bp}')    
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We got a different result this time and Ho is rejected. This means that treatment **did significantly affect** the blood pressure of this group of individuals.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Z-test
    A Z-test is very similar to a T-test, but is generally used when we have a larger sample size.

    You would use a Z test if:
    * Your sample size is greater than 30 and you know what the population variance is. Otherwise, use a t test.
    * Data points should be independent from each other. In other words, one data point isn’t related or doesn’t affect another data point.
    * Your data should be normally distributed. However, for large sample sizes (over 30) this doesn’t always matter.
    * Your data should be randomly selected from a population, where each item has an equal chance of being selected.
    * Sample sizes should be equal if at all possible
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### One Sample Z-test
    We will reuse our blood pressure dataset from above and we are going to define our Ho: average starting blood pressure of 156 for our group of individuals.
    """)
    return


@app.cell
def _(df2):
    # verify that we still have our data
    df2['bp_before']
    return


@app.cell
def _(df2, mo):
    from statsmodels.stats import weightstats as stests
    ztest, pval = stests.ztest(df2['bp_before'], x2=None, value=156)
    # determine if we can reject the null hypothesis
    conclusion= "**Reject null hypothesis**" if pval < 0.05 else "**Fail to reject null hypothesis**"

    #display using marimo'a markdown tool
    mo.md(f"""## Z-test Results     
    - **Z-statistic:** {ztest:.4f}
    - **P-value:** {pval:.4f}
    - **Conclusion:** {conclusion}
    """)    
    return (stests,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To recap, this means that our null hypothesis (Ho) cannot not be rejected, and the average blood pressure of our dataset is not significantly different than 156.

    #### Two Sample Z-test
    In two sample z-test , similar to t-test here we are checking two independent data groups and deciding whether sample mean of two group is equal or not.

    * H0 : mean of two group is 0
    * H1 : mean of two group is not 0

    Let's redo the blood pressure paired t-test from above. Our dataset does have more than 30 individuals in it.
    """)
    return


@app.cell
def _(df2):
    # verify we still have our dataset
    df2
    return


@app.cell
def _(df2, mo, stests):
    #perform two sample z-test
    z_stat_1, p_val_1 = stests.ztest(df2['bp_before'], x2=df2['bp_after'], value=0)

    # Determine the conclusion
    result_text = "**Reject null hypothesis**" if p_val_1 < 0.05 else "**Fail to reject null hypothesis**"

    # Display using marimo's markdown tool
    mo.md(f"""
    ### Two-Sample Z-Test Results
    - **Z-statistic:** {z_stat_1:.4f}
    - **P-value:** {p_val_1:.4f}
    - **Conclusion:** {result_text}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    So, the end result is the same between the paired t-test and the two sample z-test, but the p-value was different between the two tests.

    The take away here is to make sure you match your hypothesis test to your dataset!!!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Demo: Analysis with Hypothesis Testing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For this demo, we will use the dataset from our week2 assignment.
    """)
    return


@app.cell
def _(sns):
    sns.set_theme()
    from statsmodels.stats.weightstats import ttest_ind as ttest_ind
    import warnings
    warnings.filterwarnings('ignore')
    return (ttest_ind,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Loading Dataset
    """)
    return


@app.cell
def _(pd):
    df_1 = pd.read_csv('data_wk4/wages.csv')
    return (df_1,)


@app.cell
def _(df_1):
    df_1.head(10)
    return


@app.cell
def _(df_1):
    df_1.shape
    return


@app.cell
def _(df_1):
    #marimo way of displaying information about the dataset
    df_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Defining Our Problem Statement and Test Approach
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem Statement:** Spark Industries is a 5000+ employee company. The CEO has heard rumors that employee compensation is not equitable at Spark Industries, in particular based on an employee's gender.

    **Test Approach:** Since we have already worked with this dataset, we know that the dataset contains the demographic, position and salary data for 174 randomly selected employees. Additionally, we know that the gender column consists of two values: males and females.

    Based on all this information, we can utilize hypothesis testing to compare the means for the salaries between genders.
    We can subset the dataset into two groups based on gender. This will produce two independent samples drawn from the same population.

    We can assume that each sample is independent beacause the values in one sample reveals no information about the other sample. Additionally, the variance is unknown, but we can assume it is equal since all of our samples come from the same population.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data Prep
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before we get too far into the analysis, we need to prep the data.Based on the results above, we can see that all of our columns are objects. This will not work for hypothesis testing.

    First up, I'm going to drop the two name columns. These columns are used to uniquely identify the employees in the sample, which is counter intuitive to this type of analysis. The other column that I'm going to drop is the Department column. This seems a bit redundant of the information in the Position column.
    """)
    return


@app.cell
def _(df_1):
    cols_drop = ['Surname', 'Name', 'Department']
    df_1.drop(columns=cols_drop, inplace=True)
    return


@app.cell
def _(df_1):
    df_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The last column that needs addressing is the Salary column. For this we need to strip out the leading dollar sign and the commas. Then convert the value to a numeric.
    """)
    return


@app.cell
def _(df_1):
    df_1.Salary = df_1.Salary.replace('[\\$,]', '', regex=True).astype(float)
    return


@app.cell
def _(df_1):
    df_1.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### EDA Through Descriptive Statistics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before we hop straight into the hypthesis testing, we can take a moment and just see what the means across the genders look like.
    """)
    return


@app.cell
def _(df_1):
    df_1.groupby('Gender').Salary.size()
    return


@app.cell
def _(df_1):
    df_1.groupby('Gender').Salary.mean()
    return


@app.cell
def _(df_1, sns):
    sns.boxplot(data=df_1, x='Gender', y='Salary')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can see that the mean of the salaries for Males at Spark Industries is slightly higher than Females. But is there an statistical difference bewteen these two populations?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Defining Our Hypotheses
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **H0:** there is no differece in the salaries of Spark employees based on gender <br>
    **H1:** there is a differece in the salaries of Spark employees based on gender

    Based on the information above, we should be performing a t-test.We will be utilizing the [ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) method from the scipy.stats package for our analysis.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We need to subset our data based on the values in the Gender.
    """)
    return


@app.cell
def _(df_1):
    female_salaries = df_1[df_1.Gender == 'Female'].Salary
    male_salaries = df_1[df_1.Gender == 'Male'].Salary
    return female_salaries, male_salaries


@app.cell
def _(female_salaries):
    female_salaries.head()
    return


@app.cell
def _(male_salaries):
    male_salaries.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If you read the doc page for the statsmodel [ztest](https://www.statsmodels.org/stable/generated/statsmodels.stats.weightstats.ztest.html) you'd see that the test returns two values. The first is the t-test statistic and the second is the p_value. I'm going to capture both and display them.
    """)
    return


@app.cell
def _(female_salaries, male_salaries, mo, stats):
    #perform t-test stats.ttest_ind between males and 
    _ttest, pval1 = stats.ttest_ind(male_salaries, female_salaries, alternative='two-sided')
    #print the results in marimo markdown format
    mo.md(f"""## T-Test Results
    - **T-statistic:** {_ttest:.4f}
    - **P-value:** {pval1:.4f}
    """)    
    return (pval1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I'm going to define our level of significance ($\alpha$) to be 5%.
    """)
    return


@app.cell
def _(mo, pval1):
    # alpha value is 0.05 or 5%
    _alpha = 0.05

    # make decision based on p-value in marimo way
    mo.md(f"### T-Test Conclusion: {'Reject null hypothesis' if pval1 < _alpha else 'Fail to reject null hypothesis'}")

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Based on the p_value from our ztest, we fail to reject H0. Meaning, there is not enough statistical evidence that there is a gender-based wage gap at Spark Industries.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Question: What if there was a hidden wage gap?

    A hidden wage gap? What is that?

    What if there were a few high salaries that were masking or biasing our results? Or perhaps there isn't a wage gap amongst younger employees, but there is for older employees.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's take a look at the upper end of the salaries to see if there are any larger discrepancies.
    """)
    return


@app.cell
def _(df_1):
    df_1.Salary.describe()
    return


@app.cell
def _(df_1):
    df_1[df_1.Salary > 110240].sort_values('Salary', ascending=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Well there is a large gap betweent the CEO's salary and the rest of the sample population. So, let's rerun things without the CEO in the data.

    **H0:** there is no differece in the salaries of Spark employees (without the CEO) based on gender <br>
    **H1:** there is a differece in the salaries of Spark employees (without the CEO) based on gender
    """)
    return


@app.cell
def _(df_1):
    no_ceo = df_1[df_1.Position != 'President & CEO']
    female_salaries2 = no_ceo[no_ceo.Gender == 'Female'].Salary
    male_salaries2 = no_ceo[no_ceo.Gender == 'Male'].Salary
    return female_salaries2, male_salaries2, no_ceo


@app.cell
def _(female_salaries2, male_salaries2, mo, stats):
    _tstat, pval1_1 = stats.ttest_ind(male_salaries2, female_salaries2, alternative='two-sided')
    #print the results in marimo markdown format
    mo.md(f"""## T-Test Results (Excluding CEO)
    - **T-statistic:** {_tstat:.4f}
    - **P-value:** {pval1_1:.4f}
    """)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Okay, the p-value is still larger than our $\alpha$ = 5%, but notice the difference in the p_value overall when we pulled the CEO out of the dataset.

    I'm going to leave her out of the dataset and investigate whether age factors into things at all.

    **H0_a:** there is no differece in the salaries of younger (Age <= 40) Spark employees based on gender <br>
    **H1_a:** there is a differece in the salaries of younger (Age <= 40) Spark employees (without the CEO) based on gender.

    **H0_b:** there is no differece in the salaries of older (Age > 40) Spark employees based on gender <br>
    **H1_b:** there is a differece in the salaries of older (Age > 40) Spark employees (without the CEO) based on gender.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start with the younger Spark employees. We defined younger as Age <= 40. We will need to stop and check that our sample size hasn't crossed the n=30 boundary. We can use the t-test or perform a z-test.
    """)
    return


@app.cell
def _(df_1, no_ceo):
    younger_employees = no_ceo[df_1.Age <= 40]
    younger_employees.shape
    return (younger_employees,)


@app.cell
def _(younger_employees):
    y_f = younger_employees[younger_employees.Gender=='Female'].Salary
    y_m = younger_employees[younger_employees.Gender=='Male'].Salary
    return y_f, y_m


@app.cell
def _(mo, stats, y_f, y_m):
    _tstat, _pval = stats.ttest_ind(y_m, y_f, alternative='two-sided')
    #print the results in marimo markdown format
    mo.md(f"""## T-Test Results (Employees Age 40 and Under)
    - **T-statistic:** {_tstat:.4f}
    - **P-value:** {_pval:.4f}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wow! Look at that p_value. That's really high. With a p_value, it means that there is virtually no gap at all in the wages between the two groups.

    Time to look at the employees over 40.
    """)
    return


@app.cell
def _(df_1, no_ceo):
    older_employees = no_ceo[df_1.Age > 40]
    older_employees.shape
    return (older_employees,)


@app.cell
def _(df_1, no_ceo, older_employees):
    older_employee = no_ceo[df_1.Age > 40]
    o_f = older_employees[older_employees.Gender == 'Female'].Salary
    o_m = older_employees[older_employees.Gender == 'Male'].Salary
    return o_f, o_m


@app.cell
def _(mo, o_f, o_m, stests):
    #perform a z test between older male and female employees
    zstat_age, pval_age = stests.ztest(o_m, o_f, value=0, alternative='two-sided')

    #print the results in marimo markdown format
    mo.md(f"""## Z-Test Results
    - **Z-statistic:** {zstat_age:.4f}
    - **P-value:** {pval_age:.4f}
    """)    
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Interesting, our p_value is smaller than our $\alpha$ = 5%. So we will reject H0. Meaning that there is enough statisitcal evidence to suggest that there is a gap in the wages for older Spark employees based on gender.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    However, we don't know which group has a higher mean salary at this point. This is where the z-test statistic comes into play.

    The z-test value above is positive, which indicates that the mean of the first group used in the ztest is higher. We constructed our z-test with the older_males as the first group. Therefore, we can conclude that wage gap amongst older Spark employees favors Males.

    Don't believe me... Let's flip things around.
    """)
    return


@app.cell
def _(mo, o_f, o_m, stests):
    zstat_age1, pval_age1 = stests.ztest(o_f, o_m, value=0, alternative='two-sided')
    #print the results in marimo markdown format
    mo.md(f"""## Z-Test Results
    - **Z-statistic:** {zstat_age1:.4f}
    - **P-value:** {pval_age1:.4f}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The z-test value in this test is negative. Indicating that the second group's mean is higher.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Findings from our analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **H0 vs H1:**
    * p_value of 0.209, fail to reject H0 -> meaning there is no wage gap
    * CEO salary biased the results, but not enough to change the outcome

    **H0_a vs H1_a:**
    * p_value of 0.979, fail to reject H0
    * high p_value -> means there is virtually no wage gap between the two groups

    **H0_b vs H1_b:**
    * p_value of 0.0063, reject H0
    * z-test indicates that the mean of Males is higher than Females

    **Summary:**<br>
    Based on our analysis, in examining the salaries for the Spark Industries employees as a whole, there isn't enough statisitical evidence to support that there is a wage gap based on gender. However, when we segment the population to include age, we found that amongst younger employee (age <= 40) the salaries between males and females was virtually identical. However, amongst the older employees (age > 40), the was enough statisitical evidence to support the finding that Male salaries were higher than Female saleries.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Interesting Tidbit
    If your sample has over 50 degrees of freedom, than a t-test will produce the same results as a z-test.

    Degrees of freedom are the maximum number of logically independent values, which may vary in a data sample. Degrees of freedom are calculated by subtracting one from the number of items within the data sample.

    Let's rerun a couple of the above z-tests as t-test. We will use the [t-test](https://www.statsmodels.org/stable/generated/statsmodels.stats.weightstats.ttest_ind.html#) from statsmodels.
    """)
    return


@app.cell
def _(female_salaries2, male_salaries2, mo, ttest_ind):
    _tstat, _pval, _d_free = ttest_ind(male_salaries2, female_salaries2, alternative='two-sided')
    #print the results in marimo markdown format

    mo.md(f't-test statistic: {_tstat}, p-value: {_pval}, degrees of freedom: {_d_free}')
    return


@app.cell
def _(female_salaries2, male_salaries2, mo, stests):
    _zstat_gender, _pval_gender = stests.ztest(male_salaries2, female_salaries2, value=0, alternative='two-sided')

    mo.md(f'z-test statistic: {_zstat_gender}, p-value: {_pval_gender}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice how the p-values are roughly the same.
    """)
    return


@app.cell
def _(mo, ttest_ind, y_f, y_m):
    _tstat, _pval, _d_free = ttest_ind(y_m, y_f, alternative='two-sided')
    mo.md(f't-test statistic: {_tstat}, p-value: {_pval}, degrees of freedom: {_d_free}')
    return


@app.cell
def _(mo, o_f, o_m, ttest_ind):
    _tstat, _pval, _d_free = ttest_ind(o_m, o_f, alternative='two-sided')
    mo.md(f't-test statistic: {_tstat}, p-value: {_pval}, degrees of freedom: {_d_free}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The test statistic trick works with a t-test too. However, our degrees of freedom isn't over 50, so the z-test was more appropriate for the older employees.
    """)
    return


if __name__ == "__main__":
    app.run()
