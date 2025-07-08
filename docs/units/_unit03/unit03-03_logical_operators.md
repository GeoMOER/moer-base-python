---
title: LM | Logical Operators
toc: true
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---
Logical operators in Python are used to combine multiple conditions and perform logical operations. These operators are fundamental for decision-making in your code, allowing you to control code based on multiple conditions.

## Logical AND (and)
The and operator returns True if both operands are True; otherwise, it returns False. This operator is commonly used to ensure that multiple conditions are met before executing a block of code.

```python
x = True
y = False
print(x and y)
# Output: False

x = True
y = True
print(x and y)
# Output: True

x = False
y = False
print(x and y)
# Output: False
```

## Logical OR (or)
The or operator returns True if at least one of the operands is True. It is used when you want to execute code if one or more conditions are met.
```python
x = True
y = False
print(x or y)
# Output: True
```

## Logical NOT (not)
The not operator is a unary operator that inverts the Boolean value of its operand. If the operand is True, not makes it False, and vice versa.
```python
x = True
result = not x
print(result)
# Output: False
```