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