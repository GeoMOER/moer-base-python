---
title: EX | How to Convert
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---
<!--more-->
---

In Python, data types are automatically assigned to variables. You can check the type of any value using the `type()` function. If needed, you can also convert a value to a different data type using functions like `int()`, `float()`, `str()`, and `bool()`.

Python has three numeric types. The most common are `float` (for numbers with decimals) and `int` (for whole numbers). Python will often switch between these automatically, so whether a number like `3` is stored as an `int` or a `float` often doesn’t matter in practice.

However, sometimes you may want to store a number as an integer—especially if it’s used for counting, indexing, or IDs—because integers use less memory. If you're going to do math with decimals, it's better to use floats.

The table below gives an overview of the most common data types in Python.

| Data Type  | check type          | convert      |
|------------|---------------------|--------------|
| integer    | `type(x) == int`    | `int(x)`     |
| float      | `type(x) == float`  | `float(x)`   |
| string     | `type(x) == str`    | `str(x)`     |

<i>Example</i>

```python
value = 23.5

print(type(value))
# Output: <class 'float'>

print(int(value))
print(str(value))

```


