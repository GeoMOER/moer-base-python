---
title: "EX | Exercises"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u06/header.png
  image_description: "books"
  caption: "Generated Book Dataset"
---

## 📚 In-Class Tasks (20 Min): Working with Books CSV

Use the online CSV file and follow the steps to explore the dataset using `pandas`.

**📥 CSV URL**:  
[https://geomoer.github.io/moer-base-python/assets/tests/unit07/books.csv](https://geomoer.github.io/moer-base-python/assets/tests/unit07/books.csv)

---

### ✅ Task 1: Load Data and Print with `.values`

1. Import the `pandas` library.  
2. Load the CSV file using `pd.read_csv()` from the URL.  
   Assign custom column names `"Name"`, `"Autor"`, `"Jahr"`, and `"Genre"` by using the `names` parameter together with `header=None`.  
3. Print the column names.  
4. Print all values of the DataFrame using `.values`.  
5. Print the value from the second row.

---

### 🔁 Task 2: Loop and Search for Author with `iterrows()` 

Note: From this task on, use the original column names from the CSV file.

1. Load the CSV file using `pd.read_csv()` from the URL. 
2. Loop through all rows using `df.iterrows()`.  
3. Use a direct comparison to check if the `"Author"` is equal to a specific name (e.g. `"George Orwell"`).  
4. If found, print the row index and the book title.


---

### 🔍 Task 3: Change the Year and Export the Data

1. Loop through all rows using `df.iterrows()`.  
2. Search for the book titled **"The Alchemist"** by checking row["Title"].
3. If the book is found, change the value in the `"Year"` column to **1990**.  
4. Print the updated row to verify that the change was successful.  
5. Export the updated DataFrame to a new CSV file using `df.to_csv("filename.csv", index=False)`.  
   → You only need to write the filename (e.g. `"books_modified.csv"`), without a full path.  
   → The CSV file will be saved in the same folder where your Python file is located.  
   → If you are using **Visual Studio Code**, you will find the file in the **current working directory** (the folder you see in the file explorer on the left side).

