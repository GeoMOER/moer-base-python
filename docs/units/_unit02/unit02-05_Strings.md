---
title: "Strings"
toc: true
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---

<!--more-->

## What are Strings
Strings are sequences of characters enclosed in quotes. They can be created using single quotes ('), double quotes ("), or triple quotes (''' or """) for strings that span multiple lines.
```python
# Examples of strings
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_quote_string = """This is a 
multi-line string."""
```
### Special Characters

strasse = 'Ku'damm‘ – Error

Solution -> Backslash
strasse = 'Ku\'damm'


### Strings are immutable.

The String Methods and Functions create a New String!
→ The original remains unchanged!
A string is stored as a single object in memory, even if it consists of multiple characters.

All characters are stored as a unit.
You cannot change individual characters directly! (because the entire string is stored as a single block in memory)

## Basis String Operations

#### Indexing
Strings are indexed, starting at 0. A sequence of characters is stored in a string data type. So you can access each character of a string when using `[]`.
```python
my_string = "Hello"
print(my_string[0]) # Output: H
print(my_string[1]) # Output: e
print(my_string[4]) # Output: o
```

#### Concatenation (`+`)
Concatenation is the process of joining two or more strings together using the + operator.
```python
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)
# Output: "Hello, Alice!"
```

#### Repetition (`*`)
Repetition is the process of repeating a string multiple times using the `*` operator.
```python
repeat_greeting = "Hello! " * 3
print(repeat_greeting)
# Output: "Hello! Hello! Hello! "
```

#### Slicing (`:`)
Slicing allows you to extract a portion of a string using indices. The slice operator `:` is used to specify the start and end indices of the substring.
```python
sample_string = "Hello, World!"
substring = sample_string[0:5]
print(substring)
# Output: "Hello"
```

## The String Function print()
Python provides several built-in methods for string manipulation.

The `print()` function outputs strings (or other data types) to the console. We have used that function before.
```python
# Print a string
print("Hello, World!")
# Output: Hello, World!

# Print a string variable
message = "Hello, Python!"
print(message)
# Output: Hello, Python!
```
String concatenation in print() can be done using commas to separate variables or by using f-strings for more readable formatting:
```python
print(var1, var2)        
print(f"{var1} text {var2}")
```

