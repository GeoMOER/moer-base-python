---
title: "LM | Store and manage data"
toc: true
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---


<!--more-->


In any programming language, the ability to **store and manage data** is fundamental. Variables in Python provide a way to **keep track of information** and **reuse** it throughout your program.

Imagine writing a mathematical formula where you need to reuse results again and again — without variables, you would have to recompute everything manually. Variables allow you to **assign names to results**, making your code **clearer**, **shorter**, and **more flexible**.

---

## Why Use Variables?

At first glance, it seems easy to perform basic calculations directly in Python:

```python
3 + 5
# Output: 8

```

But imagine a more complex calculation, repeated many times. Without variables, the code would become long, confusing, and error-prone.

Instead, Python allows you to **store results in variables**, so that you can **reuse**, **modify**, and **organize** your information:

```python
sum_result = 3 + 5
difference = 312 - 43
product = 7 * 2
```

Variables make it possible to **structure** your work — just like using labeled boxes in an archive rather than writing everything on loose sheets of paper.

---
{% include figure image_path="/assets/images/unit_images/u03/container.webp" %}

## Variables as Memory References

In Python, a **variable acts as a label** pointing to a location in memory where a value is stored.

When you create a variable, you are not creating a new physical box, but rather attaching a **name** to a **reference** to a value.

For example:

```python
city = "Marburg"  # String (Text)
temperature = 18.5  # Float (Decimal number)
cloud_coverage = 75  # Integer (Whole number)
is_sunny = False  # Boolean (True/False)
```

In the image above, you can think of variables as labels stuck onto containers. The labels can easily be changed, and the contents can be updated.

---

## Important: Variables are not permanent containers

One important concept to understand:  
A variable can only **point to one value at a time**.  
If you assign a new value to the same variable, the old value is **overwritten**:

```python
a = 5
print(a)  # Output: 5

a = 7
print(a)  # Output: 7
```

Here, the variable `a` first refers to `5`, and then later to `7`.  
The previous value (`5`) is no longer accessible through `a`.

This flexibility is what makes programming powerful — but also why you need to **carefully track** your variable names and values.

---
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
c = 0.888 # Float
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

