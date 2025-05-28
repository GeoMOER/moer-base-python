---
title: "A | Assignment"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u02/header.png
  image_description: "thinking"
  caption: "Image by [pexels](https://pixabay.com/de/users/pexels-2286921/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1559046) [from pixabay](https://pixabay.com/de/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1559046)"
---

# Lists, Arrays and DataFrames without Loops

Please save your solutions for Exercises 1 to 9 in a single Python script named `unit05__ex(1-9)code.py`.  
For Bonus Exercise 10, use a separate script named `unit05__ex10code.py`.

Save both scripts in the same `unit05` folder, compress the folder into a `.zip` file, and upload it to ILIAS.

For more information, please visit the following link:  
https://geomoer.github.io/moer-base-python/unit00/unit00-04_submission_guidelines.html

Make sure your code is clearly structured and includes comments where helpful.

---

## Exercise 1 – Theory: List vs Array vs DataFrame

**Briefly explain the following (in your own words):**

A) What is the main difference between a list and a NumPy array?  
B) When would you use a DataFrame instead of a list or array?  
C) What does "vectorized operation" mean in NumPy?

---

## Exercise 2 – List Basics

Given the list `my_list = [4, 7, 1, 9]`,  
print the second value, the length of the list, and the sum of all elements.

---

## Exercise 3 – List Condition (if-else)

Use the list `numbers = [12, 8, 22, 5]`.  
Use an `if-else` statement to compare the first and last values and print which one is greater.

---

## Exercise 4 – List Extension

Given the list `colors = ["red", "green"]`,  
append `"blue"` to the list.  
If the length is now 3, print `"List updated."`, else print `"Update failed."`

---

## Exercise 5 – List Value Check (if)

Given the list `grades = [85, 60, 78]`,  
check if the second element is below 65.  
If yes, print `"Needs improvement"`.

---

## Exercise 6 – NumPy Array Comparison (if)

Use the arrays:

```python
import numpy as np
a = np.array([3, 8, 5])
b = np.array([4, 7, 6])
```

Compare the first element of each array using an `if` statement and print which is larger.

---

## Exercise 7 – Array Calculation with if-elif-else

Given the array `values = np.array([12, 18, 25])`,  
check the second element and print:  
- `"Low"` if < 10  
- `"Medium"` if between 10–20  
- `"High"` if > 20

---

## Exercise 8 – DataFrame Basics

Use this DataFrame:

```python
import pandas as pd
df = pd.DataFrame({
    "Name": ["Ali", "Nina", "Tom"],
    "Age": [28, 35, 22],
    "City": ["Berlin", "Leipzig", "Hamburg"]
})
```

Print the `"Age"` column.  
If the second person is older than 30, print `"Senior"`, else `"Junior"`.

---

## Exercise 9 – DataFrame Column Check (if-else)

Use this DataFrame:

```python
df2 = pd.DataFrame({
    "Score": [75, 90, 66]
})
```

If the score in row 0 is >= 80, print `"Excellent"`, otherwise `"Needs improvement"`.

---

## Exercise 10 – Bonus: Voting Statistics (DataFrame Analysis with Conditions)

Use the following DataFrame:

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Sara", "Leo", "Mia", "Jonas", "Ella"],
    "Age": [22, 19, 35, 42, 17],
    "Voted": [True, False, True, False, False]
})
```
Check whether the oldest person in the DataFrame has voted.

**Print:**
"Oldest participant (Name) voted. Thank you!"
or "Oldest participant (Name) did not vote."