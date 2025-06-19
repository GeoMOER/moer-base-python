---
title: "Overview"
toc: true
toc_depth: 2
header:
  image: /assets/images/unit_images/uXX/header.png
  image_description: "tabular data"
  caption: "Image by [pixabay](https://pixabay.com/)"
---

# 🧾 CSV Files: Overview

## 🔍 What is a CSV File?

CSV (Comma-Separated Values) is a simple file format used to store tabular data, such as spreadsheets or databases. Each line in the file is a row of data, and columns are typically separated by commas or semicolons.

Example:
```
Name,Age,City
Alice,30,Berlin
Bob,25,Hamburg
```

## 🐍 Working with CSV Files in Python

Python offers two common ways to work with CSV files:

### 1. Using the `csv` module
The built-in `csv` module allows you to read and write CSV files using simple Python structures like lists and dictionaries.

```python
import csv

with open("data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
```

### 2. Using `pandas`
The `pandas` library provides powerful tools for reading, writing, and analyzing CSV data as DataFrames.

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
```

## 📌 Common Parameters in `read_csv()`

| Parameter       | Description                                      |
|-----------------|--------------------------------------------------|
| `sep`           | Specify separator (e.g. `;` instead of `,`)      |
| `header`        | Row number to use as column names                |
| `usecols`       | Import only specific columns                     |
| `dtype`         | Define data types for each column                |
| `na_values`     | Specify which values should be treated as NaN    |
| `encoding`      | Useful for special character encodings (e.g. UTF-8, latin1) |

## ✅ Good to Know

- Always check your delimiter (`sep`) when reading European CSV files – often it's a semicolon `;`.
- Use `df.to_csv()` to export data back to a CSV file.
- `pandas` automatically detects headers but you can override this with `header=None`.

## 📚 Further Reading

- [pandas.read_csv Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [Working with CSV files in Python](https://docs.python.org/3/library/csv.html)
