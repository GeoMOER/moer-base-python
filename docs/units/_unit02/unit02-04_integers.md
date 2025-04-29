---
title: "EX | Numeric"
toc: true
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---

<!--more-->

## Integers
Integers are whole numbers without a decimal point. They can be positive, negative, or zero. 

### Examples:
```python
x = 10     # Positive integer
y = -3     # Negative integer
z = 0      # Zero
```

## Floats
Floats (floating-point numbers) are numbers with a decimal point. They can also be positive, negative, or zero.

### Examples:
```python
a = 3.14   # Positive float
b = -2.5   # Negative float
c = 0.0    # Zero as a float
```

## The `math` Library
Python provides the built-in `math` module, which contains many mathematical functions and constants.

### Importing the `math` Module
To use its functions, you must first import `math`:

```python
import math
```

### Important Functions from `math`

| `math.sqrt(x)` | Returns the square root of `x` |
| `math.pow(x, y)` | Computes `x` raised to the power of `y` |
| `math.floor(x)` | Rounds `x` down to the nearest integer |
| `math.ceil(x)` | Rounds `x` up to the nearest integer |
| `math.pi` | Constant π (3.141592653589793) |
| `math.e` | Constant e (2.718281828459045) |

### Examples:
```python
import math

# Square root
print(math.sqrt(25))  # Output: 5.0

# Power
print(math.pow(2, 3))  # Output: 8.0

# Rounding
print(math.floor(4.7))  # Output: 4
print(math.ceil(4.1))   # Output: 5

# Constants
print(math.pi)  # Output: 3.141592653589793
print(math.e)   # Output: 2.718281828459045
```
