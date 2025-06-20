---
title: "LM | Edit"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u06/header.png
  image_description: "computer"
  caption: "Photo by [Free-Photos](https://pixabay.com/photos/) [Pixabay](https://pixabay.com/de/)"
---

## 🛠️ Working with CSV Data

Once you’ve imported a CSV file into a pandas DataFrame, you can begin exploring and editing the data.

![CSV Table]({{ site.baseurl }}/assets/images/unit_images/u07/csv_example.jpg)
[📥 Download CSV file]({{ site.baseurl }}/assets/tests/unit07/csv_example.csv)
s
```


### 🔍 View Rows

Use `.head()` and `.tail()` to view the first or last few rows:

```python
import pandas as pd

url = "https://geomoer.github.io/moer-base-python/assets/tests/unit07/csv_example.csv"

df = pd.read_csv(url)
df.head()      # First 5 rows
df.head(10)    # First 10 rows
df.tail(3)     # Last 3 rows
```

---

### 🔢 Access Specific Rows

Use `.iloc[]` to access rows by position:

```python
df.iloc[0]     # First row
df.iloc[1:3]   # Rows 5 to 7
```

🔍 Search for a Value in a Row (Loop)

```python
# row 1 as list
row_list = df.iloc[1].tolist()

if 'Diana' in row_list:
    print("Found Bob in row 2!")
```
---

### ✅ Filter Rows by Condition

```python
# Rows where the value in column 'Name' is 'Alice'
df[df["Name"] == "Alice"]
```


### 🔁 Loop Through All Rows

```python
for index, row in df.iterrows():
    print(f"Row {index}: {row['Name']}")
```

---

### 🔍 Loop to Find some Information

```python
for index, row in df.iterrows():
    if "Alex" in row.to_string():
        print(row)
```

---

### ⚙️ Use `.apply()` for Custom Actions

```python
# Combine two columns into a new one
df["FullName"] = df.apply(lambda row: row["FirstName"] + " " + row["LastName"], axis=1)
print(df[["FirstName", "LastName", "FullName"]])
```
 # df.apply(...): Applies a function to each row of the DataFrame.

 # lambda row: ...: Defines a short function that combines two values from the row.

 # row["FirstName"] + " " + row["LastName"]: Concatenates the first and last name with a space in between.

 # axis=1: Means the function is applied row-wise (not column-wise).

 # df["FullName"] = ...: Stores the result in a new column called "FullName"

---

### 📋 Get Column Names

```python
print(df.columns)
```

---

### ℹ️ Summary Info

```python
df.info()
df.describe()
```

These tools help you explore and work with your CSV data efficiently.
