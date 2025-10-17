---
title: "EX | Strings"
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

```
### Special Characters

strasse = 'Ku'damm‘ – Error

Solution -> Backslash
strasse = 'Ku\'damm'


## Basis String Operations

### The String Function print()
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


### Indexing
Strings are indexed, starting at 0. A sequence of characters is stored in a string data type. So you can access each character of a string when using `[]`.
```python
my_string = "Hello"
print(my_string[0]) # Output: H
print(my_string[1]) # Output: e
```


### Slicing (`:`)

Slicing allows you to extract a portion of a string, list, or any sequence using indices. The general syntax is:

```python
sequence[start:end]
```

- **start**: The index to begin the slice (inclusive).
- **end**: The index where the slice ends (exclusive).
- If **start** or **end** is omitted, Python uses the default (start = 0, end = length of sequence).



Basic Example

```python
sample = "Hello, World!"
```
`sample[0:5]`

```python
print(sample[0:5])  # Output: 'Hello'
```
- Starts at index 0 → `"H"`
- Ends **before** index 5 → `"o"`
- Does **not** include the comma at index 5



`sample[:5]`

```python
print(sample[:5])  # Output: 'Hello'
```
- Starts from the beginning (index 0 by default)
- Returns the **first 5 characters**



`sample[:-1]`

```python
print(sample[:-1])  # Output: 'Hello, World'
```
- Starts from the beginning
- Ends **one character before the last**
- Omits the last character `"!"`


Negative Indices

Python supports **negative indexing**:
- `-1` refers to the **last** element
- `-2` refers to the second-to-last, and so on


####  Summary Table

| Expression     | Description                                 |
|----------------|---------------------------------------------|
| `s[0:5]`       | Characters from index 0 to 4                |
| `s[:5]`        | First 5 characters                          |
| `s[:-1]`       | All except the last character               |
| `s[-3:]`       | Last 3 characters                           |
| `s[::2]`       | Every second character (step = 2)           |



### Concatenation (`+`)
Concatenation is the process of joining two or more strings together using the + operator.
```python
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)
# Output: "Hello, Alice!"
```

### Repetition (`*`)
Repetition is the process of repeating a string multiple times using the `*` operator.
```python
repeat_greeting = "Hello! " * 3
print(repeat_greeting)
# Output: "Hello! Hello! Hello! "
```

