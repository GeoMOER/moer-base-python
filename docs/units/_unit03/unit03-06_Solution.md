---
title: "Python Exercise - Solutions"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "confused"
  caption: "Image by [slon_pics](https://pixabay.com/de/users/www_slon_pics-5203613/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021) [from pixabay](https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021)"
---

# Introduction

This document contains solutions to the tasks related to operators and data structures in Python. Let's go through each task and its solution step-by-step.

## Task 1: Operators

### Solution:

```python
# Defining variables
a = 10
b = 5

# Modulus
modulus = a % b
print(f"Modulus: {modulus}")

# Exponentiation
exponentiation = a ** b
print(f"Exponentiation: {exponentiation}")

# Comparison operators
equal = a == b
not_equal = a != b
greater_than = a > b
less_than = a < b
greater_equal = a >= b
less_equal = a <= b
print(f"Equal: {equal}, Not Equal: {not_equal}, Greater than: {greater_than}, Less than: {less_than}")
print(f"Greater or equal: {greater_equal}, Less or equal: {less_equal}")

# Logical operators
logical_and = (a > 5) and (b > 3)
logical_or = (a > 15) or (b > 3)
logical_not = not (a > 5)
print(f"Logical AND: {logical_and}, Logical OR: {logical_or}, Logical NOT: {logical_not}")
```
---

## Task 2: Lists

### Solution:
```python
# Defining lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenating lists
my_list = list1 + list2
print(f"Concatenated list: {my_list}")

# Sum
sum_list = sum(my_list)
print(f"Sum: {sum_list}")

# Length of list1
length_list1 = len(list1)
print(f"Length of list1: {length_list1}")

# Accessing second element of list2
second_element = list2[1]
print(f"Second element of list2: {second_element}")

# Appending a new element to the list
my_list.append('apple')
print(f"List after appending 'apple': {my_list}")

# Removes the second element (index 1)
del list1[1]  
print(f"List after removing the second element: {list1}")

# Appending a nested list
my_list.append(['tree', 'leave', 'root'])
print(f"List after appending nested list: {my_list}")

# Accessing second element of the nested list
nested_second_element = my_list[-1][1] # -1 refering to the last element
print(f"Second element of nested list: {nested_second_element}")

# Length of my_list
length_my_list = len(my_list)
print(f"Length of my_list: {length_my_list}")

```

---

## Task 3: Data Frames

### Solution:
```python
import pandas as pd

# Creating a data frame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# Displaying first two rows
print(df.head(2))

# Adding new column 'Department'
df['Department'] = ['Human Resources', 'Engineering', 'Marketing']
print(df)

# Selecting Name and Salary columns
name_salary = df[['Name', 'Salary']]
print(name_salary)

# Filtering rows where Age > 28
filtered_df = df[df['Age'] > 28]
print(filtered_df)
```
---

## Task 4: Matrices

### Solution:
```python
import numpy as np

# Creating a 2x3 matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Transposing the matrix
transposed_matrix = matrix.T
print(f"Transposed matrix:\n{transposed_matrix}")

# Calculating sum of all elements
sum_elements = matrix.sum()
print(f"Sum of all elements: {sum_elements}")

# Multiplying each element by 2
multiplied_matrix = matrix * 2
print(f"Matrix after multiplying by 2:\n{multiplied_matrix}")

# Accessing the element at row 1, column 2
element = matrix[1, 2]
print(f"Element at row 1, column 2: {element}")
```
---

## Task 5: Arrays

### Solution:
```python
# Creating a 3D array with shape (2, 2, 2)
array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Accessing element at position (1, 1, 0)
element = array[1, 1, 0]
print(f"Element at position (1, 1, 0): {element}")

# Slicing the array to get the first 2D matrix
first_matrix = array[0]
print(f"First 2D matrix:\n{first_matrix}")

# Reshaping the array into a 2x4 array
reshaped_array = array.reshape(2, 4)
print(f"Reshaped array:\n{reshaped_array}")
```
---

## Task 6: Factors

### Solution:
```python
# Creating a pandas Categorical object
categories = pd.Categorical(['low', 'high', 'medium', 'medium', 'low'], categories=['low', 'medium', 'high'])

# Printing categories and their frequency
print(categories)
print(pd.value_counts(categories))

# Converting to ordered categorical type
ordered_categories = categories.as_ordered()
print(f"Ordered categories:\n{ordered_categories}")

# Sorting categories
sorted_categories = sorted(ordered_categories)
print(f"Sorted categories: {sorted_categories}")
```
---