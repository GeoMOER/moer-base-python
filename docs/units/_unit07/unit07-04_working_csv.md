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
### 📋 Get Column Names

```python
print(df.columns)
```

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
df.iloc[1:3]   # Rows 5 to 7
```
---

###  Access values from column

NumPy array that contains only the raw data from the "Name" column — without index, formatting, or metadata.
```python
df["Name"].values
```
---

### Search for a Value in a Row 

```python
# This line takes row 1 of the DataFrame and converts it into a regular Python list.
row_list = df.iloc[1].tolist()

if 'Bob' in row_list:
    print("Found Bob in row 2!")
```
---

### 🔁 Loop Through All Rows

```python
for index, row in df.iterrows():
    print("Row " + str(index) + ": " + row["Name"]) 
```

```python
for index, row in df.iterrows():
    if "Alex" in row.to_string():
        print("Row " + str(index) + ": " + row["Name"])
```

---

### ✅ Filter Rows by Condition

```python

print(df["Name"]== "Anna") #looks like it's coming from a loop, but actually no loop is written. 
      # That’s one of the most powerful features of Pandas - Vectorized operations.
      # Results:
      # 0     True
      # 1    False
      # 2    False
      # 3    False
      # 4    False
      # 5    False
      # 6    False
      # 7    False
      # 8    False
      # 9    False
      
      
df_anna = ""
if "Anna" in df["Name"].values:
    
    df_anna = df[df["Name"] == "Anna"] # Rows(true) where the value in column 'Name' is 'Anna'
    
    print("New DataFrame with Anna only:")
    print(df_anna)
else:
    df_anna = pd.DataFrame()  # Leerer DataFrame als Fallback
```


---

### ⚙️ Use `.apply()` for Custom Actions

```python

df["FullName"] = df.apply(lambda row: row["FirstName"] + " " + row["LastName"], axis=1)

print(df[["FirstName", "LastName", "FullName"]])


 # df.apply(...): Applies a function to each row of the DataFrame.

 # lambda row: ...: Defines a short function that combines two values from the row.

 # row["FirstName"] + " " + row["LastName"]: Concatenates the first and last name with a space in between.

 # axis=1: Means the function is applied row-wise (not column-wise).

 # df["FullName"] = ...: Stores the result in a new column called "FullName"
```
---



