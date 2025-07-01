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

In this section, you'll learn how to read, explore, and manipulate data from a CSV file using `pandas`.

![CSV Table]({{ site.baseurl }}/assets/images/unit_images/u07/csv_example.jpg)
[📥 Download CSV file]({{ site.baseurl }}/assets/tests/unit07/csv_example.csv)


### 📥 Import CSV into a DataFrame

```python
import pandas as pd

url = "https://geomoer.github.io/moer-base-python/assets/tests/unit07/csv_example.csv"

df = pd.read_csv(url)

```
---
### Iterate over the rows
`df.iterrows()` is a method in pandas that allows you to iterate over the rows of a DataFrame one at a time.

```python
for index, row in df.iterrows():
    # you can access row data like this:
    print(index, row['Name'])
    
```


---
### 📋 Get Column Names

```python
print(df.columns)
```
---

###  Access Values from a Column

```python
df["Name"].values
```
 Returns a NumPy array with the raw data from the "Name" column — without index, formatting, or metadata.
---
### 🔍 View Rows
```python
df.head()      # First 5 rows
df.head(10)    # First 10 rows
df.tail(3)     # Last 3 rows
```

---

### 🔢 Access Specific Rows

Use `.iloc[]` to access rows by position:

```python
df.iloc[0]     # First row
df.iloc[1:3]   # Rows 2 to 3 (index 1 and 2)
```
---

### Search for a Value in a Row 

```python
# This line takes row 1 of the DataFrame and converts it into a regular Python list.
row_list = df.iloc[1].tolist()

if 'Bob' in row_list:
    print("Found Bob")
```
---

### Update DataFrame values by using labels (row index and column names).

Key points
Syntax: df.loc[row_index, column_label]
```python

for index, row in df.iterrows():
  df.loc[3, "Name"] = "Updated Name"
  print(df.loc[3]["Name"])


### 🔁  Search using `iterrows()` — 3 different methods


Each of these does the same task but uses a different technique:

```python
for index, row in df.iterrows():
    if "Maria" in row.to_string():
        print("Row " + str(index) + ": " + row["Name"])
        
for index, row in df.iterrows():
    if "Maria" in row.values:
        print("Row " + str(index) + ": " + row["Name"])
        
for index, row in df.iterrows():
    if "Maria" == row["Name"]:
        print("Row " + str(index) + ": " + row["Name"])
```

---


### ⚙️ Search for a Value in a Row with`.apply()` 

```python

print(df[df["Name"] == "Maria"])
print(df[df.apply(lambda row: row["Name"] == "Maria", axis=1)])
print(df[df.apply(lambda row: "Maria" in row.values, axis=1)])
print(df[df.apply(lambda row: "Maria" in row.to_string(), axis=1)])

# df.apply(...): Applies a function to each row of the DataFrame.
# axis=1: Ensures the function is applied row-wise.
# Each line demonstrates a different way of searching for "Maria" in the rows.


```
---



