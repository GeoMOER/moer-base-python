---
title: "Python Exercise - Operators and Data Structures"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "confused"
  caption: "Image by [slon_pics](https://pixabay.com/de/users/www_slon_pics-5203613/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021) [from pixabay](https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021)"
---

# Introduction

This unit covers Python's data structures, including vectors (lists), data frames (using pandas), matrices, arrays, lists, and factors. You will work through various tasks to build familiarity with these concepts.


## Task 1: Lists

### Description:
Work with Python lists. You will define lists and perform various operations on them.

### Instructions:
1. Define two lists `list1 = [1, 2, 3]` and `list2 = [4, 5, 6]`.
2. Perform the following operations:
    - Concatenate the two list and name it `my_list`.
    - Calculate the sum.
    - Find the length of `list1`.
    - Access the second element of `list2`.
3. Now append the list:
    - Append a new element `'apple'` to the list.
    - Remove `2` from the list.
    - Append a nested list `['tree', 'leave', 'root']`
    - Access the nested list and retrieve the second element.
    - Find the length of `my_list`.

---

## Task 2: Data Frames

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

## Task 4: Arrays

### Description:
Explore arrays in Python using numpy, which can represent multi-dimensional data structures.

### Instructions:
1. Create a 3-dimensional array with the shape (2, 2, 2) and values ranging from 1 to 8.
2. Perform the following operations:
    - Access the element at position (1, 1, 0).
    - Slice the array to get the first 2D matrix.
    - Reshape the array into a 2x4 array.

---

## Task 5: Factors

### Description:
In Python, you can represent categorical variables using pandas `Categorical` type, similar to R's factors.

### Instructions:
1. Create a pandas Categorical object with the following categories: `['low', 'medium', 'high']`.
2. Perform the following operations:
    - Assign the values `['low', 'high', 'medium', 'medium', 'low']` to a variable `categories`.
    - Print the categories and their frequency.
    - Convert `categories` to an ordered categorical type with the order `['low', 'medium', 'high']`.
    - Sort the categories based on their levels.

---

Happy coding!