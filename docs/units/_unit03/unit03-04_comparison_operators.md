---
title: LM | Comparison Operators
toc: true
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---

Comparison operators in Python allow you to compare values and determine their relationships. These operators are fundamental in making decisions and controlling the flow of your program.

| Operator  | Description                          | Example     |
|-----------|--------------------------------------|-------------|
| **Comparison Operators**                         ||
| `<`       | Test if x is smaller than y          | `x < y`     |
| `>`       | Test if x is greater than y          | `x > y`     |
| `==`      | Test if x is exactly equal to y      | `x == y`    |
| `>=`      | Test if x is greater than or equal to y | `x >= y` |
| `<=`      | Test if x is smaller than or equal to y | `x <= y` |
| `!=`      | Test if x is not equal to y          | `x != y`    |

## Less Than (<)
The < operator checks if the value on the left is less than the value on the right.
```python
x = 5
y = 10
result = x < y
print(result)
# Output: True
```

## Greater Than (>)
The > operator checks if the value on the left is greater than the value on the right.
```python
x = 10
y = 5
result = x > y
print(result)
# Output: True
```

## Equal To (==)
The == operator checks if the value on the left is exactly equal to the value on the right. This operator is commonly used in conditions to test equality.
```python
x = 10
y = 10
result = x == y
print(result)
# Output: True
```

## Greater Than or Equal To (>=)
The >= operator checks if the value on the left is greater than or equal to the value on the right.
```python
x = 10
y = 10
result = x >= y
print(result)
# Output: True
```

## Less Than or Equal To (<=)
The <= operator checks if the value on the left is less than or equal to the value on the right.
```python
x = 5
y = 10
result = x <= y
print(result)
# Output: True
```

## Not Equal To (!=)
The != operator checks if the value on the left is not equal to the value on the right. This is useful for testing inequality.
```python
x = 10
y = 5
result = x != y
print(result)
# Output: True
```