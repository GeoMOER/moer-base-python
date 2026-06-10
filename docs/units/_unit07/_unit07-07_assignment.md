---
title: "A | Assignment"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u07/header.png
  image_description: "computer"
  caption: "Photo by [Free-Photos](https://pixabay.com/photos/) [Pixabay](https://pixabay.com/de/)"
---



## 📚  Working with Books CSV


Please save your solutions for Exercises 1 to 3 in a single Python script named `unit07__ex(1-3)code.py`.  
For Bonus Exercise, use a separate script named `unit07__ex4code.py`.

Save both scripts in the same `unit07` folder, compress the folder into a `.zip` file, and upload it to ILIAS.

For more information, please visit the following link:  
https://geomoer.github.io/moer-base-python/unit00/unit00-04_submission_guidelines.html

Make sure your code is clearly structured and includes comments where helpful.


## Introduction
Use the online CSV file and follow the steps to explore the dataset using `pandas`.

**📥 CSV URL**:  
[https://geomoer.github.io/moer-base-python/assets/tests/unit07/books.csv](https://geomoer.github.io/moer-base-python/assets/tests/unit07/books.csv)

---


### 🏠 Task 1: Count Books in the Genre "Fantasy"

1. Filter the DataFrame to find all books where the `"Genre"` is `"Fantasy"`.  
2. Count how many such books there are.  
3. Print the number.


---

### 🏠 Task 2: List All Books Before the Year 1950

1. Filter the DataFrame to include only books with a `"Year"` before 1950.  
2. Print the titles and years of those books.

💡 *Hint:* Don’t forget to convert `"Year"` to `int` before comparing.

---

### 🏠 Task 3: Print All Unique Genres

1. Print a list of all unique values in the `"Genre"` column.  
2. Then, print how many different genres there are in total.

---

### 🌟 Task 4: Mark Old Books with `apply()`

1. Use the `.apply()` method with `axis=1` to create a new column called `"Old"`.  
2. If the `"Year"` of a book is before 1950, set "Old" to "yes" or "no"
3. Export the new DataFrame with the  `"Old"` columns.

💡 *Hint:* Inside your function, make sure to convert `"Year"` to an integer before comparing.

---

### 🧊 Task 5 (Bonis):Titanic Dataset — Beginner Exercises (Python & Pandas)

These exercises are designed to help you practice basic data analysis with the Titanic dataset using Pandas.
Use the dataset from this URL:

https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

Load it with:

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
```

---

#### ✅ Exll passengers younger than 10
Filter the dataset and show all passengers whose age is below 10.

*Hint:* Use a boolean condition on the `Age` column.

---

#### ✅ Eount men and women
Find out:
- how many male passengers are in the dataset  
- how many female passengers are in the dataset

*Hint:* Use `value_counts()`.

---

#### ✅ Everage age per ticket class
Calculate the average age for each passenger class (`Pclass`).

Which class had the highest average age?

---

#### ✅ Eurvival rate by gender
Compute the survival rate for:
- male passengers  
- female passengers  

*Hint:* `groupby("Sex")["Survived"].mean()`.

---

#### ✅ Eassengers whose name contains "Smith"
Show all rows where the passenger's name contains the string `"Smith"`.

*Hint:* Use `.str.contains("Smith")` on the `Name` column.

---

Good luck! 🚢✨
