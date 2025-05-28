---
title: "LM | Data Frames"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---

<!--more-->

## Object Type: Data Frames

In Python, data frames are provided by the `pandas` library. A data frame is a two-dimensional structure, similar to a table. Each column represents a variable, and each row is an observation or case.

Unlike matrices, data frames can hold different types of data in each column (e.g. numbers, text, booleans). This makes them ideal for representing real-world datasets. You create a data frame with the `pd.DataFrame()` function.

```python
import pandas as pd

# Creating lists
a = ["Peter", "Sabine", "Rachel", "Ray", "Ashley"]
b = [24, 42, 12, 56, 57]
c = [1.54, 1.85, 1.30, 1.97, 1.64]
d = [True, False, False, True, False]

# Creating a data frame with column names
patients = pd.DataFrame({
    'Name': a,
    'Age': b,
    'Height': c,
    'Ill': d
})

print(patients)
```

Data frames have column names and row labels. You can access columns with the dot operator or square brackets. You can also set custom row labels.

```python
# Assign custom row labels
patients.index = ["ID_001", "ID_002", "ID_003", "ID_004", "ID_005"]

# Accessing columns
print(patients.Name)         # Dot operator
print(patients['Name'])      # Bracket notation

# Accessing rows by index and label
print(patients.iloc[0])      # First row by position
print(patients.loc["ID_001"])  # First row by label
```

You can add new columns by direct assignment:

```python
# Add a new column
patients['Last_Name'] = ['Müller','Schmidt','Smith','Brown','Rodriguez']
print(patients)
```

## Pandas DataFrame Methods

| Method/Function                   | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| `pd.DataFrame(data)`              | Creates a DataFrame from a dictionary, list, or array.                      |
| `df.head(n)`                      | Returns the first `n` rows.                                                 |
| `df.tail(n)`                      | Returns the last `n` rows.                                                  |
| `df.describe()`                   | Summary statistics for numeric columns.                                     |
| `df.info()`                       | Overview of data types and memory usage.                                    |
| `df.shape`                        | Tuple with (rows, columns).                                                 |
| `df.columns`                      | Returns the column names.                                                   |
| `df.iloc[row, col]`               | Access by index position.                                                   |
| `df.loc[row, col]`                | Access by label.                                                            |
| `df.drop(labels, axis)`           | Removes rows or columns.                                                    |
| `df.fillna(value)`                | Fills missing values.                                                       |
| `df.groupby(by)`                  | Groups data by one or more columns.                                         |
| `df.sort_values(by)`              | Sorts by column.                                                            |
| `df.to_csv('filename.csv')`       | Exports to a CSV file.                                                      |
