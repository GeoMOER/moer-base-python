---
title: " EX | Exercises"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "confused"
  caption: "Image by [slon_pics](https://pixabay.com/de/users/www_slon_pics-5203613/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021) [from pixabay](https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021)"
---

# Introduction

This unit covers Python's data structures, including lists and data frames (using pandas). You will work through various tasks to build familiarity with these concepts.


## 🧪 Task 1: Working with Lists

### 📋 Description:
In this task, you will practice using Python lists. You’ll define lists, access elements, and apply key list methods such as `append()`, `remove()`, and `extend()`.

### ️ Instructions:
1. Define two lists:

```python
list1 = [19, 20, 3]
list2 = [48, 5, 6]
```

2. Perform the following operations:
   - Concatenate `list1` and `list2` to create a new list called `my_list`.
   - Calculate the sum of `list1` (use Accessing elements by index, no loops).
   - Find the length of `list1` using the `len()` function.
   - Print the second element of `list2`.

3. Modify `my_list`:
   - Append a new element `'apple'` using `append()`.
   - Remove the value `19` from the list using `remove()`.
   - Extend the list with another list `['tree', 'leave', 'root']` using `extend()`.
   - Finally, print the updated length of `my_list`.

### 💡 Reminder:
- `append()` adds a single item.
- `extend()` adds each element from another iterable.
- Lists are **mutable**, so you can modify them in place.

---


## 🧪 Task 2: Compare Array Elements

### 📋 Description:
You will create a NumPy array and use an `if-else` statement to compare specific elements. No loops are required.

### ️ Instructions:
1. Import the NumPy library.
2. Create an array called `scores` with the values `[88, 92, 75, 91]`.
3. Compare the first and last elements of the array using an `if-else` statement:
    - If the first element is greater than the last, print: `"First score is higher."`
    - Otherwise, print: `"Last score is higher or equal."`

---

## Task 3: Data Frames

### Description:
Learn how to create and manipulate data frames using pandas.

### Instructions:
1. Create a data frame using pandas with the following data:
    - `Name = ['Alice', 'Bob', 'Charlie']`
    - `Age = [25, 30, 35]`
    - `Salary = [50000, 60000, 70000]`
2. Perform the following operations:
    - Display the first two rows of the data frame.
    - Add a new column called `Department` with values `['Human Resources', 'Engineering', 'Marketing']`.
    - Select the `Name` and `Salary` columns.
    - Filter the data frame to only show rows where `Age > 28`.
    
---

## Task 3: Matrices

### Description:
Learn how to create and manipulate matrices using numpy.

### Instructions:
1. Create a 2x3 matrix with the following values:
    ```
    [[1, 2, 3],
     [4, 5, 6]]
    ```
2. Perform the following operations:
    - Transpose the matrix.
    - Calculate the sum of all elements.
    - Multiply each element of the matrix by 2.
    - Access the element at row 1, column 2.

---



Happy coding!