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

### 🌟 Task 4 (Bonus): Mark Old Books with `apply()`

1. Use the `.apply()` method with `axis=1` to create a new column called `"Old"`.  
2. If the `"Year"` of a book is before 1950, set "Old" to "yes" or "no"
3. Export the new DataFrame with the  `"Old"` columns.

💡 *Hint:* Inside your function, make sure to convert `"Year"` to an integer before comparing.

---
