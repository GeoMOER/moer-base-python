---
title: LM | if Statement
header:
  image: /assets/images/unit_images/u04/header.png
  image_description: "if logic structure"
  caption: "Photo by [Markus Spiske](https://unsplash.com/@markusspiske) [from Unsplash](https://unsplash.com/photos/code-on-laptop-screen-FXFz-sW0uwo)"
---

In Python, `if` statements are used to control the flow of a program by executing certain blocks of code only when specific conditions are met. The basic form of an `if` statement checks a condition and executes the following indented block of code `if` the condition is True

## Basic `if` Statement
Here’s an example of a simple `if` statement:
```python
a = 5.0
b = 10.0
if a < b:
    print("a is smaller than b")
# Output:
# a is smaller than b
```

## Using logical operators in `if` Statements
You can also use more complex boolean expressions within if statements to make more precise decisions:
```python
c = 5
if a < b and a == c:
  print("a is smaller than b and equal to c")
# Output:
# a is smaller than b and equal to c
```

## Negating Conditions with `not`
The `not` operator can be used to check if a condition is `False`:
```python
if not a > b:
    print("a is smaller than b")
# Output:
# a is not smaller than b
```
If you would exclude the `not`, the condition would be `False` and you wound't get an output.