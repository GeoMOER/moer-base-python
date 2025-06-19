---
title: "EX | Exercises"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u06/header.png
  image_description: "books"
  caption: "Generated Book Dataset"
---

## 📚 In-Class Tasks: Working with Books CSV

Use the file `book_list.csv` and follow the steps below in a Jupyter notebook or Python script.

---

### ✅ Task 1: Import and Print All Rows

1. Import the `pandas` library.
2. Load the CSV file using `pd.read_csv()`.
3. Print all rows of the DataFrame.

```python
import pandas as pd

df = pd.read_csv("book_list.csv")
print(df)
```

---

### 🔍 Task 2: Search for a Book by Author and Print It

1. Use a condition to find all books written by **George Orwell**.
2. Print only the rows that match.

```python
print(df[df["Author"] == "George Orwell"])
```

---

### ✏️ Task 3: Replace the Author and Save New File

1. Change the author's name **"George Orwell"** to **"Orwell, George"**.
2. Print the updated row to verify.
3. Save the modified DataFrame to a new CSV file.

```python
df.loc[df["Author"] == "George Orwell", "Author"] = "Orwell, George"
print(df[df["Author"] == "Orwell, George"])

df.to_csv("book_list_modified.csv", index=False)
```

---

Make sure to check your folder for the newly saved file `book_list_modified.csv`.
