# Pandas Techniques Reference
### From: `1_Defined_Analytical_questions.py`

---

## 1. Importing Libraries

**What it is:** The first step in any Python script — loading external packages that provide the tools you'll use throughout your analysis.

**How it works:** The `import` keyword loads a library into memory. The `as` keyword gives it a shorter alias so you don't have to type the full name every time. Libraries only need to be imported once per script.

```python
import pandas as pd
import seaborn as sns

sns.set_theme()   # applies a clean visual style to all plots
```

---

## 2. Loading a CSV File — `pd.read_csv()`

**What it is:** Reads a comma-separated values file from disk and loads it into a Pandas DataFrame — the core data structure used for all analysis.

**How it works:** Pass the file path as a string. Pandas automatically detects column headers from the first row and infers data types for each column.

```python
df = pd.read_csv('data_wk1/titanic.csv')
```

---

## 3. Inspecting Shape — `df.shape`

**What it is:** A quick way to see the dimensions of your DataFrame.

**How it works:** Returns a tuple of `(rows, columns)`. Access individual values using index notation — `df.shape[0]` for rows, `df.shape[1]` for columns.

```python
df.shape        # e.g. (891, 15)
df.shape[0]     # 891  — number of rows
```

---

## 4. Previewing Data — `df.head()`, `df.tail()`, `df.sample()`

**What it is:** Methods to peek at a portion of the DataFrame without printing the whole thing.

**How it works:** `head(n)` returns the first `n` rows (default 5), `tail(n)` returns the last `n` rows, and `sample(n)` returns `n` randomly selected rows — useful for spotting patterns or anomalies that might not appear at the top or bottom.

```python
df.head(10)     # first 10 rows
df.tail()       # last 5 rows (default)
df.sample(10)   # 10 random rows
```

---

## 5. Listing Column Names — `df.columns`

**What it is:** Retrieves the names of all columns in the DataFrame.

**How it works:** Returns an Index object containing all column name strings. Useful for verifying what data you have loaded and for building column reference lists.

```python
df.columns
# Index(['survived', 'pclass', 'sex', 'age', 'fare', ...])
```

---

## 6. Data Types & Non-Null Counts — `df.info()`

**What it is:** Prints a concise summary of the DataFrame including the data type and number of non-null values for each column.

**How it works:** Iterates over each column and reports its dtype (`int64`, `float64`, `object`, etc.) and how many entries are non-null. Columns with fewer non-null values than the total row count contain missing data.

```python
df.info()
# RangeIndex: 891 entries, 0 to 890
# Column        Non-Null Count  Dtype
# survived      891 non-null    int64
# age           714 non-null    float64   ← 177 missing values
```

---

## 7. Descriptive Statistics — `df.describe()`

**What it is:** Generates summary statistics for all numeric columns, covering central tendency and dispersion.

**How it works:** By default, returns count, mean, std, min, 25th/50th/75th percentiles, and max for numeric columns. Pass `include='all'` to also summarize text columns. Use `.T` to transpose the result for easier reading when there are many columns.

```python
df.describe()           # numeric columns only
df.describe(include='all')  # all columns
df.describe().T         # transposed for readability
```

---

## 8. Histogram — `plt.hist()`

**What it is:** A bar chart that shows the frequency distribution of a single numeric variable.

**How it works:** Divides the range of values into `bins` (buckets) and counts how many values fall into each. Passing `.dropna()` first removes missing values that would otherwise cause an error. Use `plt.title()` to label the chart.

```python
import matplotlib.pyplot as plt

plt.hist(df['age'].dropna(), bins=30)
plt.title("Histogram of age")
plt.show()
```

---

## 9. Box Plot — `df.boxplot()`

**What it is:** A visual summary of a column's distribution using five-number statistics: minimum, Q1, median, Q3, and maximum. Outliers appear as individual dots.

**How it works:** Called directly on the DataFrame with the column name as an argument. The box spans Q1 to Q3 (the interquartile range), the line inside is the median, and the "whiskers" extend to the min/max within 1.5× the IQR.

```python
df.boxplot('age')
```

---

## 10. Referencing Columns

**What it is:** Two equivalent ways to select a single column from a DataFrame.

**How it works:** Bracket notation (`df['col']`) works for all column names, including those with spaces or special characters. Dot notation (`df.col`) is a shorthand that works only when the column name is a valid Python identifier and doesn't conflict with a built-in method name.

```python
df['age'].head()    # bracket notation — always works
df.age.head(10)     # dot notation — shorthand
```

---

## 11. Selecting Multiple Columns with a List

**What it is:** Selects a subset of columns from the DataFrame by passing a list of column names.

**How it works:** Pass a Python list inside the square brackets. The result is a new DataFrame containing only the specified columns, in the order listed.

```python
cols = ['survived', 'pclass', 'age']
df[cols].head()
```

---

## 12. Row & Column Slicing — `df.iloc[]`

**What it is:** Selects rows and/or columns by their integer position (index number), independent of any labels.

**How it works:** Uses Python's standard slice syntax `start:stop` (stop is exclusive). Use `:` as a wildcard meaning "all." Double square brackets `[[...]]` are needed when passing a list of positions rather than a range.

```python
df.iloc[0]          # first row
df.iloc[[1, 10, 100]]   # rows at positions 1, 10, and 100
df.iloc[5:8, :]     # rows 5–7, all columns
df.iloc[:, 0:2]     # all rows, first 2 columns
df.iloc[5:8, 0:2]   # rows 5–7, first 2 columns
```

---

## 13. Copying a DataFrame — `df.copy()`

**What it is:** Creates a fully independent duplicate of a DataFrame so that changes to the copy do not affect the original.

**How it works:** Without `.copy()`, assigning a DataFrame to a new variable creates a *view* — modifying it can unexpectedly change the original. `.copy()` guarantees a true, separate copy.

```python
df_copy = df.copy()
```

---

## 14. Dropping Rows & Columns — `df.drop()`

**What it is:** Removes specified rows or columns from a DataFrame.

**How it works:** Specify the row index or column name to remove. By default, `drop()` returns a new DataFrame without modifying the original. Use `inplace=True` to modify the DataFrame directly, or reassign: `df = df.drop(...)`. Use the `columns=` keyword to drop by column name.

```python
df_copy.drop(df_copy.index[0], inplace=True)        # drop first row
df_copy.drop(columns=['deck'], inplace=True)         # drop a column
```

---

## 15. Detecting Missing Values — `df.isnull()`

**What it is:** Identifies missing (`NaN`) values across the DataFrame and can summarize how many exist per column.

**How it works:** `isnull()` returns a boolean DataFrame of the same shape. Chaining `.sum()` counts the `True` values (i.e., nulls) per column. Dividing by `.count()` gives the proportion. `pd.concat()` can combine these into a readable summary table.

```python
# Count nulls per column
missing = df.isnull().sum()

# Show only columns that have at least one null
missing = missing[missing > 0]
missing.sort_values(inplace=True)
missing.plot.bar()

# Null count + percentage table
total   = df.isnull().sum().sort_values(ascending=False)
percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
```

---

## 16. Unique Values — `df['col'].unique()`

**What it is:** Returns an array of all distinct values found in a column.

**How it works:** Iterates over the column and collects values that appear at least once, in order of first occurrence. Useful for inspecting categorical columns to see what categories exist and to spot typos or inconsistencies.

```python
df['sex'].unique()
# array(['male', 'female'], dtype=object)
```

---

## 17. Custom Functions with `apply()`

**What it is:** Applies a user-defined function to every element in a column (or row), row by row.

**How it works:** Write a function that accepts a single value as input and returns a transformed value. Pass the function name (without parentheses) to `.apply()`. Pandas calls it once per row on that column's value and assembles the results into a new Series. The result is typically stored as a new column.

```python
def return_gender(sex):
    if sex == 'male':
        return 0
    elif sex == 'female':
        return 1
    else:
        return -999   # fallback for unexpected values

df['gender'] = df['sex'].apply(return_gender)
```

---

## 18. Aggregation — `df.agg()`

**What it is:** Computes one or more summary statistics across a column or the entire DataFrame in a single call.

**How it works:** Pass a list of function name strings to run multiple aggregations at once. Alternatively, pass a dictionary where keys are column names and values are lists of functions — this lets you aggregate different columns with different functions simultaneously.

```python
# Single column, multiple functions
df['fare'].agg(['sum', 'mean', 'median', 'min', 'max', 'std', 'var'])

# Multiple columns with different functions (dictionary syntax)
df.agg({'fare': ['sum', 'mean'],
        'sex':  ['count']})
```

---

## 19. Grouping — `df.groupby()`

**What it is:** Splits the DataFrame into groups based on unique values in one or more columns, then applies an aggregation to each group separately.

**How it works:** Pass a list of column names to group by. Chaining `.agg()` afterward runs summary functions on each group independently. Pass `'describe'` to `agg()` to get full descriptive statistics per group. Chain `.round(n)` to control decimal places.

```python
# Aggregate fare stats grouped by embarkation city
df.groupby(['embark_town']).agg({'fare': ['sum', 'mean', 'median', 'min', 'max']})

# Full describe() per group
df.groupby(['embark_town']).agg({'fare': 'describe'}).round(2)
```

---

## 20. Counting with Groupby — `count()`, `nunique()`, `size()`

**What it is:** Three distinct counting functions used after `groupby()`, each with a subtle difference in behaviour.

**How it works:**
- `count()` — counts non-null values only
- `nunique()` — counts the number of distinct (unique) values
- `size()` — counts all rows including nulls

The difference between `count` and `size` only becomes visible when a column contains `NaN` values.

```python
df.groupby(['deck']).agg({'embark_town': ['count', 'nunique', 'size']})
```

---

## 21. Lambda Functions

**What it is:** An anonymous (unnamed) single-line function, typically used for quick transformations that don't need a full `def` block.

**How it works:** The syntax is `lambda input: expression`. Everything to the right of `:` is automatically returned. Lambdas can include conditionals using inline `if/else`. They are most commonly passed directly into `.apply()`.

```python
# Basic lambda
caps = lambda s: s.capitalize()
caps('male')   # 'Male'

# Lambda with conditional
caps_female = lambda s: s.capitalize() if s == 'female' else s

# Applied directly to a column
df['sex'] = df['sex'].apply(lambda s: s.capitalize() if s == 'female' else s)
```

---

## 22. Formatting Output — `style.format()`

**What it is:** Applies display formatting to a DataFrame for presentation purposes, such as adding currency symbols or controlling decimal places. Requires the `jinja2` package.

**How it works:** Chain `.style.format()` onto a DataFrame or groupby result. The format string follows Python's string formatting syntax: `'${0:,.2f}'` adds a `$` prefix, commas as thousands separators, and 2 decimal places. This only affects *display* — the underlying data is unchanged.

```python
import jinja2

df.groupby(['embark_town']).agg({'fare': ['sum', 'mean', 'median', 'min', 'max']}) \
  .style.format('${0:,.2f}')

# No decimal places
df.groupby(['embark_town']).agg({'fare': ['sum', 'mean']}) \
  .style.format('${0:,.0f}')
```

---

## 23. Highlighting Min & Max — `highlight_max()` / `highlight_min()`

**What it is:** Applies background colour highlighting to the highest and lowest values in each column of a styled DataFrame.

**How it works:** Chained after `.style.format()`. Pass a CSS colour name or hex code to the `color` argument. Green is commonly used for maximum values and red for minimums, making it easy to spot extremes at a glance.

```python
(df.groupby(['embark_town'])
   .agg({'fare': ['sum', 'mean', 'median', 'min', 'max']})
   .style.format('${0:,.2f}')
   .highlight_max(color='green')
   .highlight_min(color='red'))
```

---

## 24. Subsetting for Analysis — `df.iloc[]` + `.copy()`

**What it is:** The pattern used in the analytical question section to extract only the columns relevant to a specific investigation.

**How it works:** Use `iloc[]` to select a range of columns by position, then immediately chain `.copy()` to ensure the subset is independent from the original DataFrame. This is best practice before any column modifications or targeted analysis.

```python
# Select first 4 columns and make an independent copy
q1_df = df.iloc[:, 0:4].copy()
q1_df.info()
```

---

## 25. Groupby for Analytical Questions — `groupby().mean()`

**What it is:** The core technique used to answer the analytical question by comparing a numeric metric across groups.

**How it works:** Group the subsetted DataFrame by two categorical columns simultaneously (e.g., `survived` and `sex`), then call `.mean()` on a numeric column. The result shows the average value of that column for every combination of the grouping variables.

```python
# Average age, broken down by survival status and gender
q1_df.groupby(['survived', 'sex']).age.mean()
```

---

*Reference books used in this course:*
- **Pandas for Everyone** — Daniel Y. Chen (Addison-Wesley, 2023)
- **Hands-On Exploratory Data Analysis with Python** — Mukhiya & Ahmed (Packt, 2020)
