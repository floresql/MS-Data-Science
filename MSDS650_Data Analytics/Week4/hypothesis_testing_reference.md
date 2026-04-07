# Hypothesis Testing Concepts Reference
### From `4_Hypothesis_Testing.py`

---

## 1. Descriptive vs. Inferential Statistics

**What it is:** The foundation for understanding why hypothesis testing exists. Descriptive statistics summarize what is in your data (mean, median, charts). Inferential statistics go further and let you draw conclusions about a broader population based on a sample.

**How it works:** Descriptive stats use tools like central tendency and variance. Inferential stats use probability and sample data to make predictions or test claims about a population.

| Descriptive | Inferential |
|---|---|
| Summarizes known data | Makes predictions beyond the data |
| Uses charts, mean, std dev | Uses hypothesis tests, confidence intervals |
| Results are factual | Results are probabilistic |

---

## 2. Sampling Techniques

**What it is:** Methods for selecting a subset of a population to analyze, so that the sample represents the population fairly.

**How it works:** Four common methods are used depending on the situation:

- **Simple Random Sampling:** every member has an equal chance of selection
- **Systematic Sampling:** members are chosen at regular intervals from a list
- **Stratified Sampling:** population is divided into subgroups, then sampled from each
- **Cluster Sampling:** subgroups are randomly selected in their entirety

---

## 3. Null and Alternative Hypothesis (H0 and H1)

**What it is:** The starting point for any hypothesis test. You define two competing claims about the population before running any statistics.

**How it works:** The null hypothesis (H0) is the default assumption -- that there is no effect or no difference. The alternative hypothesis (H1) is what you are trying to find evidence for.

**Example from the notebook:**
- H0: There is no difference in salaries between male and female employees
- H1: There is a difference in salaries between male and female employees

---

## 4. Type I and Type II Errors

**What it is:** The two ways a hypothesis test can be wrong.

**How it works:**
- **Type I Error:** Rejecting H0 when it is actually true (a "false positive")
- **Type II Error:** Failing to reject H0 when it is actually false (a "false negative")

Understanding these helps you choose an appropriate significance level for your test.

---

## 5. Significance Level (Alpha) and P-value

**What it is:** The tools used to make a decision about your hypothesis.

**How it works:**
- **Alpha (α):** The threshold you set before the test. Commonly 0.05 (5%). This is the probability of making a Type I error you are willing to accept.
- **P-value:** The probability of observing your results if H0 were true.

**Decision rule:**
- If `p-value <= alpha`: reject H0
- If `p-value > alpha`: fail to reject H0

```python
alpha = 0.05
if pval < alpha:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")
```

---

## 6. Normality Testing

**What it is:** Before running most hypothesis tests, you need to check whether your data is normally distributed, since most tests assume this.

**How it works:** Two approaches are used:

### Graphical Methods

**Histogram** -- gives a visual sense of the distribution shape:

```python
import matplotlib.pyplot as plt
plt.hist(data)
plt.show()
```

**Normal Probability Plot (Q-Q Plot)** -- if data is normal, points fall along a straight line:

```python
from scipy import stats
stats.probplot(data['value'], dist="norm", plot=plt)
plt.show()
```

### Shapiro-Wilk Test (Statistical Method)

**What it is:** A statistical test that quantifies how likely it is that data came from a normal distribution. Best used with smaller samples (under a few thousand observations).

```python
from scipy.stats import shapiro
stat, p = shapiro(data)
print('Statistics=%.3f, p=%.3f' % (stat, p))

if p > 0.05:
    print("Fail to reject null hypothesis -- data looks normal")
else:
    print("Reject null hypothesis -- data does not look normal")
```

---

## 7. One-Sample T-test

**What it is:** Tests whether the mean of a single sample is significantly different from a known or assumed population mean.

**When to use it:** When you have one group and want to compare it to a benchmark value. Best when sample size is under 30 or population variance is unknown.

**Example from the notebook:** Testing whether the average age of 14 people is significantly different from 30.

```python
from scipy.stats import ttest_1samp
ages = [32, 34, 29, 29, 22, 39, 38, 37, 38, 36, 30, 26, 22, 22]
tset, pval = ttest_1samp(ages, 30)
print(f'p-value: {pval}')
```

---

## 8. Paired T-test

**What it is:** Compares the means of two related groups -- for example, measurements taken from the same subjects before and after a treatment.

**When to use it:** When the same group is measured twice (before/after), making the samples dependent on each other.

- H0: The mean difference between the two samples is 0
- H1: The mean difference is not 0

**Example from the notebook:** Testing whether a new athletic coaching method improved performance.

```python
from scipy import stats
ttest, pval = stats.ttest_rel(df['before'], df['after'])
print(f'p-value: {pval}')
```

---

## 9. Two-Sample (Independent) T-test

**What it is:** Compares the means of two independent groups to see if they are significantly different.

**When to use it:** When you have two separate, unrelated groups (like male vs. female employees) and want to compare their means. Used when population variance is unknown and sample size is over 30.

**Example from the notebook:** Comparing male and female salaries at Spark Industries.

```python
from scipy import stats
ttest, pval = stats.ttest_ind(male_salaries, female_salaries, alternative='two-sided')
print(f'p-value: {pval}')
```

---

## 10. One-Sample Z-test

**What it is:** Similar to the one-sample t-test, but used when the sample size is large (over 30) or the population variance is known.

**When to use it:** When you want to test a sample mean against a known benchmark value and your sample is large enough.

**Example from the notebook:** Testing whether the average starting blood pressure in the dataset is 156.

```python
from statsmodels.stats import weightstats as stests
ztest, pval = stests.ztest(df2['bp_before'], x2=None, value=156)
print(f'p-value: {pval}')
```

---

## 11. Two-Sample Z-test

**What it is:** Compares the means of two independent groups, used when sample sizes are large (over 30).

**When to use it:** Same situation as the two-sample t-test, but with larger samples. Also useful because the sign of the z-statistic tells you which group has the higher mean.

- Positive z-statistic: the first group's mean is higher
- Negative z-statistic: the second group's mean is higher

**Example from the notebook:** Comparing blood pressure before and after treatment, and later comparing older male vs. female employee salaries.

```python
from statsmodels.stats import weightstats as stests
zstat, pval = stests.ztest(df2['bp_before'], x2=df2['bp_after'], value=0)
print(f'z-statistic: {zstat}, p-value: {pval}')
```

---

## 12. Subsetting Data for Group Comparisons

**What it is:** A data preparation step where you filter a dataframe into separate groups before running a hypothesis test.

**How it works:** Use boolean indexing to create two Series or DataFrames, one per group. These are then passed into the test function.

**Example from the notebook:** Splitting employees by gender, and then further by age group.

```python
female_salaries = df[df.Gender == 'Female'].Salary
male_salaries = df[df.Gender == 'Male'].Salary

younger_employees = df[df.Age <= 40]
older_employees = df[df.Age > 40]
```

---

## 13. Cleaning and Preparing String Data for Analysis

**What it is:** A data cleaning step needed before numeric analysis can be done on columns that were imported as strings.

**How it works:** Use `str.replace()` with regex to strip non-numeric characters, then cast the column to a numeric type with `.astype()`.

**Example from the notebook:** The Salary column was stored as a string like `$85,000` and needed to be converted to a float.

```python
df.Salary = df.Salary.replace('[\\$,]', '', regex=True).astype(float)
```

---

## 14. Exploratory Descriptive Statistics Before Hypothesis Testing

**What it is:** A step done before formal hypothesis testing to visually and numerically explore group differences.

**How it works:** Use `groupby()` and `mean()` to compare group averages, and use a boxplot to see the distribution and spread of each group. This helps you understand the data and check whether a difference even seems likely before committing to a test.

```python
df.groupby('Gender').Salary.mean()

import seaborn as sns
sns.boxplot(data=df, x='Gender', y='Salary')
```

---

## 15. Degrees of Freedom and When T-test Equals Z-test

**What it is:** A concept that explains when a t-test and z-test will give the same result.

**How it works:** Degrees of freedom are calculated as the sample size minus one. When a sample has more than 50 degrees of freedom (roughly over 50 observations), the t-distribution becomes nearly identical to the normal distribution, and both tests produce the same p-value.

**Example from the notebook:** The `ttest_ind` from statsmodels returns a third value -- the degrees of freedom -- which you can use to verify this.

```python
from statsmodels.stats.weightstats import ttest_ind
tstat, pval, degrees_of_freedom = ttest_ind(male_salaries, female_salaries, alternative='two-sided')
print(f'degrees of freedom: {degrees_of_freedom}')
```

---

*Reference: `4_Hypothesis_Testing.py` lecture materials*
