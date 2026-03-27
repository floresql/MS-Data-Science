# EDA Concepts Reference Guide
### Based on `3_EDA.py` — Exploratory Data Analysis with Palmer Penguins

---

## Overview

**Exploratory Data Analysis (EDA)** is the process of getting to know your data before modeling. Rather than testing a pre-existing hypothesis, EDA helps you *uncover* relationships so you can form hypotheses. It is the first step in virtually every machine learning pipeline.

The file follows Jason Brownlee's framework from *Data Preparation for Machine Learning*, organized into five major areas:

1. Data Cleaning
2. Feature Selection
3. Data Transforms
4. Feature Engineering
5. Dimensionality Reduction

---

## 1. Loading and Inspecting Data

**What it is:** The first step in any EDA — getting your data into a usable structure and taking an initial look at it.

**How it works:** The file uses Seaborn's `load_dataset()` to pull the Palmer Penguins dataset directly from GitHub into a Pandas DataFrame. Basic inspection functions are then used to understand the shape and contents.

```python
import seaborn as sns
import pandas as pd

penguins = sns.load_dataset('penguins')

type(penguins)       # Confirm it's a DataFrame
penguins.shape       # (344, 7) — rows x columns
penguins.head()      # First 5 rows
penguins.info()      # Column names, non-null counts, data types
penguins.describe()  # Summary statistics (mean, std, min, max, quartiles)
penguins.describe().T  # Transposed version — swaps rows and columns for easier reading
```

---

## 2. Missing Data Detection

**What it is:** Identifying which rows and columns have missing (null/NaN) values, and how many.

**How it works:** Pandas provides `isnull()` which returns a boolean mask. Combined with `sum()`, it counts missing values per column. You can also filter to show *only* rows with at least one missing value.

```python
# Count missing values per column
penguins.isnull().sum()

# Show all rows that have ANY missing value
penguins[penguins.isnull().values.any(axis=1)]

# Calculate percentage of missing values in a column
penguins.sex.isnull().sum() / penguins.shape[0] * 100
```

---

## 3. Handling Missing Data — Filtering Rows

**What it is:** Removing rows where a critical column is null, rather than the entire row.

**How it works:** Instead of using `dropna()` (the "sledgehammer"), the file uses boolean indexing with `notna()` to copy only the valid rows into a new DataFrame. This is a more controlled approach.

```python
# Keep only rows where body_mass_g is not null
penguins_1 = penguins[penguins.body_mass_g.notna()]

penguins_1.info()  # Verify only 2 rows were removed
```

> **Note:** The file emphasizes that *dropping rows should not be the first tool you reach for.* There are usually better options (imputation, inference, etc.).

---

## 4. Categorical Data & Encoding

**What it is:** Converting text/string columns into a numeric format that machine learning algorithms can process.

**How it works:** Columns like `species`, `island`, and `sex` are strings. Pandas has a `category` dtype that stores strings for human readability while using numbers internally. Two encoding strategies are demonstrated:

### 4a. `astype('category')` — Convert to Pandas Category Type

```python
penguins_1.species = penguins_1.species.astype('category')
penguins_1.island  = penguins_1.island.astype('category')
penguins_1.sex     = penguins_1.sex.astype('category')
```

### 4b. `pd.get_dummies()` — One-Hot Encoding

Creates a new binary (0/1) column for each unique value in a category column. This avoids implying any numeric ordering between categories.

```python
peng_encoded = pd.get_dummies(penguins_1, columns=['island', 'species'],
                               prefix=['island', 'species'])
# Result: new columns like island_Biscoe, island_Dream, species_Adelie, etc.
```

### 4c. Manual `.map()` — Binary Encoding

For a two-value category, you can map directly to 0/1:

```python
peng_encoded['sex'] = peng_encoded['sex'].map({'Male': 0, 'Female': 1})
```

### 4d. `LabelEncoder` (scikit-learn) — Integer Encoding

Assigns each unique string value an integer. Useful for tree-based models, but can imply false ordering for others.

```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in house_1.columns:
    if house_1[col].dtype == 'object':
        house_1[col] = le.fit_transform(house_1[col])
```

---

## 5. Imputing Missing Data with Machine Learning

**What it is:** Using a trained ML model to *predict* the missing values in a column, rather than filling with a mean or dropping the row.

**How it works:** Rows with complete data become the training set. The column with missing values becomes the target (`y`). After training, the model predicts the values for the incomplete rows.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Separate complete and incomplete records
X = peng_encoded[peng_encoded.sex.notnull()].loc[:, columns]
y = peng_encoded[peng_encoded.sex.notnull()]['sex']

# Split into train/test
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(x_train, y_train)

# Evaluate accuracy
y_pred = clf.predict(x_test)
print(f'Model accuracy = {metrics.accuracy_score(y_test, y_pred)}')

# Predict missing values
x_missing = peng_encoded[peng_encoded.sex.isnull()].loc[:, columns]
y_missing = clf.predict(x_missing)
```

---

## 6. Data Variance

**What it is:** Checking whether a column has enough variation to be analytically useful. A column with only one unique value has zero variance and contributes nothing to a model.

**How it works:** `nunique()` counts how many distinct values each column has. Columns with very few unique values may be useless or might actually be categories disguised as numbers.

```python
oil.nunique()  # Count unique values per column
# Columns with 1 unique value (like column 22) have zero variance
```

---

## 7. Boxplots

**What it is:** A visualization that shows the distribution of a numeric variable, highlights the median, quartiles, and outliers at a glance.

**How it works:** The box spans the interquartile range (Q1 to Q3). The line inside is the median. The "whiskers" extend to min/max. Points beyond the whiskers are outliers. Pandas can generate boxplots directly.

```python
# Boxplot of multiple columns
penguins_1.boxplot(['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm'])

# Useful for comparing variance — a flat box = low variance
oil.boxplot([22, 36, 45, 49])
```

---

## 8. Duplicate Row Detection

**What it is:** Identifying and removing rows that appear more than once in the dataset, which can bias model training.

**How it works:** Pandas `duplicated()` returns a boolean Series. `any()` tells you if *any* duplicates exist. `drop_duplicates()` removes them.

```python
iris.duplicated()          # Boolean mask — True where row is a duplicate
iris.duplicated().any()    # Quick check: are there ANY duplicates?

dupes = iris.duplicated()
print(iris[dupes])         # Show which rows are duplicates

# Remove duplicates (inplace modifies the original DataFrame)
iris.drop_duplicates(inplace=True)
print(f'Before: {iris.shape}')
print(f'After:  {iris.shape}')
```

---

## 9. Outlier Detection

**What it is:** Identifying data points that fall far outside the normal range of observations. Outliers can distort model training and reduce predictive accuracy.

**How it works:** Two visual methods are shown (scatter plots, boxplots), plus automatic detection with scikit-learn's `LocalOutlierFactor`.

### 9a. Visual — Scatter Plot

```python
import matplotlib.pyplot as plt

plt.scatter(oil[2], oil[3])
plt.show()
```

### 9b. Automatic — `LocalOutlierFactor`

Assigns a score to each data point based on how isolated it is relative to its neighbors. Points labeled `-1` are outliers.

```python
from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor()
yhat = lof.fit_predict(X_train)

# Keep only non-outliers (label != -1)
mask = yhat != -1
X_train_clean = X_train[mask]
y_train_clean = y_train[mask]
```

> Removing outliers improved MAE (Mean Absolute Error) in the linear regression example, demonstrating that outliers can bias model learning.

---

## 10. Train/Test Split

**What it is:** Dividing your dataset into a training portion (used to fit the model) and a testing portion (used to evaluate it on unseen data).

**How it works:** `train_test_split()` randomly shuffles and splits the data. `test_size` controls the proportion held out. `random_state` makes the split reproducible.

```python
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# 70% training, 30% testing
```

---

## 11. Linear Regression

**What it is:** One of the simplest supervised ML models. It finds the best-fit straight line through the training data and uses it to make numerical predictions.

**How it works:** The model fits a line `y = mx + b` that minimizes prediction error. New inputs are mapped to an `(x, y)` position on that line to get a predicted value.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

model = LinearRegression()
model.fit(X_train, y_train)

yhat = model.predict(X_test)
mae = mean_absolute_error(y_test, yhat)
print('MAE: %.3f' % mae)
```

**Mean Absolute Error (MAE):** The average of the absolute differences between predicted and true values. Lower is better.

---

## 12. Feature Selection

**What it is:** The process of deciding which columns (features) to include in your model. Including irrelevant features can reduce accuracy and increase training time.

**How it works:** Three approaches are demonstrated in the file:

### 12a. Pairplot

Plots every feature against every other feature in a grid. Useful for spotting linear relationships visually.

```python
import seaborn as sns

sns.pairplot(penguins_1)
# Each cell is a scatter plot of two features; diagonal shows distributions
```

> **Caution:** On large datasets, pairplots are computationally expensive. Only use on subsets.

### 12b. Correlation Matrix + Heatmap

`corr()` computes Pearson correlation coefficients between all numeric feature pairs (values from -1 to +1). A heatmap makes it easy to read.

```python
# Compute correlation matrix
corrmat = penguins_1.corr(numeric_only=True)

# Display as heatmap
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(corrmat, vmax=0.8, square=True)

# With annotation (show values in cells)
sns.heatmap(corrmat, cbar=True, annot=True, square=True, fmt='.2f')
plt.show()

# Top 10 features most correlated with a target variable
k = 10
cols = house_cor.nlargest(k, 'SalePrice')['SalePrice'].index
```

### 12c. Statistical Selection

The type of statistical test to use depends on whether your input/output variables are numerical or categorical:

| Input Variable | Output Variable | Suggested Method |
|---|---|---|
| Numerical | Numerical | Pearson Correlation |
| Numerical | Categorical | ANOVA / similar |
| Categorical | Numerical | Correlation ratio |
| Categorical | Categorical | Chi-squared test |

---

## 13. Feature Importance via RandomForest

**What it is:** Using a trained RandomForest model to rank which features had the most influence on its predictions — a data-driven approach to feature selection.

**How it works:** Decision trees make splits based on which feature reduces prediction error the most at each node. RandomForest aggregates many trees and tracks how often and how much each feature contributed. This is exposed through `feature_importances_`.

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(X, y)

# Pair feature names with importance scores and sort
importance_list = list(zip(X.columns, model.feature_importances_))
sorted_importance = sorted(importance_list, key=lambda x: x[1], reverse=True)

# Pretty-print
max_len = len(max(X.columns, key=len))
for feature, rank in sorted_importance:
    dots = max_len - len(feature)
    print(f'{feature}: {"."*dots} {rank*100:.2f}%')
```

> **Pro tip from the file:** Add a column of random numbers to your dataset. Any feature less important than the random column is probably not worth including.

---

## 14. GroupBy and Aggregation

**What it is:** Splitting a DataFrame into groups based on one or more columns, then computing aggregate statistics (min, max, mean, etc.) within each group.

**How it works:** `groupby()` partitions rows by the specified column(s). `agg()` applies one or more functions to the resulting groups.

```python
# Get min, max, mean body mass grouped by species AND sex
peng_mass = penguins_1.groupby(['species', 'sex']).agg({'body_mass_g': ['min', 'max', 'mean']})
```

This produces a multi-level (hierarchical) index. To flatten it:

```python
peng_mass_1 = peng_mass.reset_index()

# Flatten multi-level column names to single strings
peng_mass_1.columns = peng_mass_1.columns.to_flat_index().str.join('_')
# Results in columns like: species_, sex_, body_mass_g_min, body_mass_g_max, body_mass_g_mean
```

---

## 15. Interactive Visualizations with Marimo & Altair

**What it is:** Creating interactive charts where users can click, select, and filter data points — and have the selected data reflected in a linked table.

**How it works:** The file uses `marimo` (the notebook framework) combined with `altair` (a declarative charting library). `mo.ui.altair_chart()` wraps an Altair chart to make it interactive inside Marimo.

```python
import altair as alt
import marimo as mo

penguins_chart = mo.ui.altair_chart(
    alt.Chart(penguins).mark_point().encode(
        x=alt.X('flipper_length_mm:Q', title='Flipper Length (mm)'),
        y=alt.Y('body_mass_g:Q', title='Body Mass (g)'),
        color=alt.Color('species:N', title='Species'),
    )
)

# Stack chart and a reactive table that shows selected points
mo.vstack([penguins_chart, mo.ui.table(penguins_chart.value)])
```

---

## Summary Table

| # | Concept | Primary Tool(s) | Purpose |
|---|---|---|---|
| 1 | Loading & Inspecting Data | `sns.load_dataset`, `.info()`, `.describe()` | Understand data shape and types |
| 2 | Missing Data Detection | `.isnull()`, `.sum()` | Find where data is absent |
| 3 | Filtering Missing Rows | `.notna()`, boolean indexing | Remove truly unusable rows |
| 4 | Categorical Encoding | `astype('category')`, `get_dummies()`, `LabelEncoder` | Convert strings to numbers for ML |
| 5 | ML-Based Imputation | `RandomForestClassifier` | Predict missing values intelligently |
| 6 | Data Variance | `.nunique()` | Identify zero/low-variance columns |
| 7 | Boxplots | `.boxplot()` | Visualize spread, outliers, variance |
| 8 | Duplicate Detection | `.duplicated()`, `.drop_duplicates()` | Remove redundant rows |
| 9 | Outlier Detection | `LocalOutlierFactor`, scatter plots | Find and remove anomalous points |
| 10 | Train/Test Split | `train_test_split` | Evaluate model on unseen data |
| 11 | Linear Regression | `LinearRegression`, MAE | Predict numeric values |
| 12 | Feature Selection | Pairplot, Heatmap, `corr()` | Choose the most relevant features |
| 13 | Feature Importance | `RandomForestRegressor.feature_importances_` | Rank features by predictive power |
| 14 | GroupBy & Aggregation | `.groupby()`, `.agg()` | Compute group-level statistics |
| 15 | Interactive Visualization | `altair`, `marimo` | Explore data interactively |
