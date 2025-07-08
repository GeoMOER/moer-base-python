---
title: LM | if and elif
header:
  image: /assets/images/unit_images/u04/header.png
  image_description: "if logic structure"
  caption: "Photo by [Markus Spiske](https://unsplash.com/@markusspiske) [from Unsplash](https://unsplash.com/photos/code-on-laptop-screen-FXFz-sW0uwo)"
---

The `elif` statement in Python, short for "else if," allows you to check multiple conditions in sequence. It provides a way to handle more than just two possible outcomes (as with a simple if and else). With `elif`, you can check for additional conditions after the initial `if` statement, and only the first condition that evaluates to `True` will have its corresponding block of code executed.

## Example of elif Usage
Here’s a basic example:
```python
a = 10.0
b = 10.0

if a < b:
    print("a is smaller than b")
elif a == b:
    print("a equals b")
```

In this example, the first `if` condition `a < b` is `False`, so Python checks the `elif` condition `a == b`, which is `True`, so the message "a equals b" is printed.

## Multiple `elif` Statements
You can include multiple `elif` statements to check for a variety of conditions:
```python
x = 25

if x < 10:
    print("x is less than 10")
elif x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
```
In this example, Python evaluates each condition in sequence.