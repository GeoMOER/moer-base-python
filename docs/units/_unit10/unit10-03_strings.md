---
title: LM | Working with Strings and Simple Operators
header:
  image: /assets/images/unit_images/u10/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "Mobile Android operating system market share by version worldwide from 2018 to 2020: [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---

## What are strings?

Strings are **sequences of characters**, used to store and work with text data in Python. You can think of them as ordered collections of letters, digits, symbols, or whitespace.

Strings in Python are **immutable**, which means that once a string is created, it cannot be changed. Instead, any "modifications" create a new string. This property ensures safety and consistency when working with text.

Strings are also **sequential data types**, so you can iterate over them character by character, slice them, and perform many common sequence operations.

## Examples

```python
text = "Hello, world!"

# Accessing individual characters
first_letter = text[0]  # "H"

# Slicing
greeting = text[0:5]    # "Hello"

# Iterating over a string
for char in text:
    print(char)

# String methods
print(text.upper())     # "HELLO, WORLD!"
print(text.lower())     # "hello, world!"
print(text.replace("world", "Python"))  # "Hello, Python!"
```

# Simple operators

You also reviewed basic operators, including:

- **Arithmetic operators** (e.g., `+`, `-`, `*`, `/`)
- **Comparison operators** (e.g., `==`, `!=`, `<`, `>`)
- **Logical operators** (e.g., `and`, `or`, `not`)
