---

title: "EX | Exercises"
toc: TRUE
toc\_float: TRUE
header:
image: /assets/images/unit\_images/u06/header.png
image\_description: "books"
caption: "Generated Book Dataset"
---------------------------------

## 📚 Solutions: Working with Books CSV

**📥 CSV URL**:
[https://geomoer.github.io/moer-base-python/assets/tests/unit07/books.csv](https://geomoer.github.io/moer-base-python/assets/tests/unit07/books.csv)

---

### ✅ Task 1: Load Data and Print with `.values`

```python
import pandas as pd

# Load the CSV file from the URL
url = "https://geomoer.github.io/moer-base-python/assets/tests/unit07/books.csv"
df = pd.read_csv(url)

# 1. Print all values as NumPy array
print("All data as array:")
print(df.values)

# 2. Print the value in the second row and first column
print("\nSpecific value at [1][0]:")
print(df.values[1][0])
```

---

### 🔁 Task 2: Loop and Search for Author "George Orwell"  using a loop with `iterrows()`

```python
for index, row in df.iterrows():
    if row["Author"] == "George Orwell":
        print(f"Row {index}: {row['Title']} by {row['Author']}")
```

---

### 🔍 Task 3: Search for the book titled **"The Alchemist"** using a loop and direct comparison.

```python
for index, row in df.iterrows():
    if "1949" in row.to_string():
        print(f"\nRow {index} contains the year 1949:")
        print(row)
```

---
