---
title: "LM | Variables and Assignment"
toc: true
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---


<!--more-->


Understanding how to name, assign, and manage variables is essential for writing clean and effective Python code. In this section, we will cover best practices for naming variables, the concept of dynamic typing, and how to receive user input.

---

## Naming Conventions

> “All things are defined by names. Change the name, and you change the thing.” — Terry Pratchett, *Pyramids*

Clear and consistent variable names make your programs easier to read and maintain.

### Rules for Variable Names
- Variables can contain **letters, numbers, and underscores (`_`)**, but **cannot start with a number**.
- No spaces or special characters are allowed (e.g., `-` is invalid).
- Variable names are **case-sensitive** (`myVar` and `myvar` are different).
- Reserved keywords like `type` or `print` should not be used as variable names.

### Recommended Naming Style
- Use **underscores** to separate words for better readability:

```python
flower_name = "Daisy"
print(flower_name)
```

- Avoid starting variable names with numbers:

```python
3Beta = 4  # Invalid!
```

- Prefer **descriptive names** over short and unclear ones:

```python
x1, xx  # Not recommended
num_students, avg_temperature  # Better!
```

---

## Dynamic Typing

Python uses **dynamic typing**, meaning you don't need to declare a variable's type explicitly — Python determines it at runtime.

Example:

```python
a = 1  # Integer
b = "Peter"  # String
c = [1, 2, 3]  # List
```

Be careful when combining different types:

```python
print(a + b + c)  # Causes an error!
```

This will produce:

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Important:
- Always ensure operations involve compatible data types.

---

## User Input with `input()`

Often, programs need input from users.  
In Python, the `input()` function:

- Displays a prompt for the user,
- Reads input from the keyboard,
- Always returns the input as a **string**.

Example:

```python
name = input("What is your name? ")
print("Hello,", name)
```

### Working with Numbers

Since `input()` always returns a string, you must **convert** the input when working with numbers:

```python
age = input("How old are you? ")  # String input
age = int(age)  # Convert to integer
print("In 5 years, you will be", age + 5)
```

👉 Always remember to convert user input to the appropriate type.

---

## How to Properly Use `input()` in Visual Studio Code (VS Code)

When working in **VS Code**, use the **Terminal** to run scripts that use `input()`:

### Quick Steps:

1. Save your file (e.g., `hello.py`).
2. Open the **Terminal** (`Terminal → New Terminal` or `Ctrl + ~`).
3. Run your file using:

```bash
python hello.py
```
or, if necessary:

```bash
py hello.py
```

Alternatively, right-click inside the editor and select **"Run Python File in Terminal"**.

---

### ⚠️ Common Issues and Solutions

| Problem                            | Reason                                      | Solution                                    |
|------------------------------------|---------------------------------------------|---------------------------------------------|
| `input()` does not wait for input | Script was run in Python Interactive Window | Use "Run in Terminal" instead               |
| Terminal closes immediately        | No pause at end of script                   | Add `input("Press Enter to exit...")`       |
| `'python' is not recognized`       | Python is not installed or not in PATH      | Use `py` or fix your Python installation    |

---

✅ With these practices, you are now ready to manage variables and user input confidently!
