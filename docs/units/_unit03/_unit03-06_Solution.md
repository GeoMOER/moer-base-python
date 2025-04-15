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

This unit covers Python's basic operators, focusing on arithmetic, comparison, and logical operators. You will practice using these operators through multiple tasks to solidify your understanding.

## Task 1: Arithmetic and Comparison Operators

### Solution:
```python
# Define variables
a = 10
b = 5

# Arithmetic operations
modulus_result = a % b
exponentiation_result = a ** b

# Print arithmetic results
print("Modulus (a % b):", modulus_result)
print("Exponentiation (a ** b):", exponentiation_result)

# Comparison operations
is_equal = a == b
is_not_equal = a != b
is_greater = a > b
is_less_or_equal = a <= b

# Print comparison results
print("Is a equal to b?", is_equal)
print("Is a not equal to b?", is_not_equal)
print("Is a greater than b?", is_greater)
print("Is a less than or equal to b?", is_less_or_equal)
```
---

## Task 2: Logical and Combined Operations

### Solution:
```python
# Define variables
a = 10
b = 5

# Combined logical operations
and_result = a > 8 and b < 10
or_result = a == 10 or b == 10
not_result = not (a == b)

# Print logical operation results
print("Is a > 8 and b < 10?", and_result)
print("Is a == 10 or b == 10?", or_result)
print("Not (a == b):", not_result)
```
---