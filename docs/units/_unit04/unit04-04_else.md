---
title: LM | if, elif and else
header:
  image: /assets/images/unit_images/u04/header.png
  image_description: "if logic structure"
  caption: "Photo by [Markus Spiske](https://unsplash.com/@markusspiske) [from Unsplash](https://unsplash.com/photos/code-on-laptop-screen-FXFz-sW0uwo)"
---

The `else` statement in Python is used to define a block of code that will execute **if none of the preceding `if` or `elif` conditions are `True`**. It acts as a *default case* and ensures that your program can respond appropriately even when no specific conditions match.

## 🔍 Why use `else`?

Without `else`, your program simply does nothing if no condition is `True`. This can lead to silent errors or unexpected behavior if you forget to handle certain cases.

With `else`, you can define a fallback behavior – something that always runs when all other options have failed.

## ⚖️ `if - elif - elif` vs. `if - elif - else`

You can technically use multiple `elif` statements to cover various specific conditions. However, if you want to make sure that **"something" always happens**, even when all other checks fail, `else` is the right choice.

Here’s the difference:

### ✅ Using only `if - elif - elif`
```python
x = 50

if x > 100:
    print("x is large")
elif x > 70:
    print("x is medium-large")
elif x > 40:
    print("x is medium")
# If x <= 40, nothing happens!
```

In this case, if `x` is 40 or less, the program just skips all conditions and prints nothing.

### ✅ Using `if - elif - else`
```python
x = 50

if x > 100:
    print("x is large")
elif x > 70:
    print("x is medium-large")
else:
    print("x is small or medium")
```

Now, the `else` ensures that something is printed **no matter what**.

## 💡 How else Works

An `else` statement is typically placed at the end of an if-elif chain:

- Python checks the `if` condition first. If it's `True`, the `if` block runs, and all other conditions are skipped.
- If the `if` condition is `False`, Python checks each `elif` in order.
- If **none** of the conditions match, the `else` block runs.

## 🧪 Examples of `else` Usage

### Example 1
```python
a = 15.0

if a > 20:
    print("a is larger than 20")
elif a < 20:
    print("a is smaller than 20")
else:
    print("a is exactly 20")
```

### Example 2
```python
temperature = 0

if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a nice day.")
elif temperature > 10:
    print("It's a bit chilly.")
else:
    print("It's cold outside.")
```

### Example 3: Only `if` and `else`
```python
a = 15.0
b = 20.0

if a < b:
    print("a is smaller than b")
else:
    print("a is not smaller than b")
```
