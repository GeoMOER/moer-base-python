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

## Built-in String Functions
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

The `len()` function returns the length of a string.

```python
length = len("Hello, World!")
print(length)
# Output: 13
```

The `str()` function converts other data types to strings.
```python
number = 42
number_string = str(number)
print(number_string)
# Output: '42'
```
The `type()` function
```python
text = "Marburg"
print( type(text) )  # <class 'str'>
zahl = 42
print( type(zahl) )  # <class 'int'>
```

The `sorted()` function - Returns a sorted copy of the list (without modifying the original list).
```python
print( sorted("Marburg") )  # ['M', 'a', 'b', 'g', 'r', 'r', 'u']
```
The `list()` function - Returns a list of tuples (index, element).
```python
print( list("Marburg") )  # ['M', 'a', 'r', 'b', 'u', 'r', 'g']
```

## Built-in String Methods
The `replace()` method replaces occurrences of a substring with another substring, but does not modify the original.
The third parameter for the count is optional – 
it specifies how many occurrences should be replaced. If this parameter is not provided, all occurrences will be replaced.
```python
original_string = "Hello, World!"
new_string = original_string.replace("World", "Python")
print(new_string)
# Output: "Hello, Python!"
```
The `strip()` - Removes spaces but does not modify the original.
```python
print( original_string.strip() ) 
```

The `find()` method returns the lowest index of the first occurrence of a substring, while `rfind()` returns the highest index of the last occurrence.
```python
# Find first occurrence
text = "Hello, World! Hello, Python!"
index_hello = text.find("Hello")
# Output: 0

# Find last occurrence
index_hello_last = text.rfind("Hello")
# Output: 13
```

The `count()` method returns the number of occurrences of a substring in a string.
```python
text = "Hello, World! Hello, Python!"
count_hello = text.count("Hello")
# Output: 2
```

The `split()` method splits a string into a list of substrings based on a delimiter.
```python
# Splits string at all spaces
sentence = "Hello, World! How are you?"
words = sentence.split(" ")
# Output: ['Hello,', 'World!', 'How', 'are', 'you?']
```

The `splitlines()` method splits a string at line breaks and returns a list of lines.
```python
# Split string into lines
multiline_string = """This is line one.
This is line two.
This is line three."""
lines = multiline_string.splitlines()
# Output: ['This is line one.', 'This is line two.', 'This is line three.']

```
Additional string methods include `upper()`, `lower()`, `title()`, and `capitalize()`.
```python
text = "Marburg an der Lahn"

print( text.upper() )       # MARBURG AN DER LAHN
print( text.lower() )        # marburg an der lahn
print( text.title() )           # Marburg An Der Lahn
print( text.capitalize() )  # Marburg an der lahn

```
You can find more listed in the table below.
## String Methods in Python

| Method/Function                 | Description                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------------------|
| `str.lower()`                   | Converts all characters in the string to lowercase.                                              |
| `str.upper()`                   | Converts all characters in the string to uppercase.                                              |
| `str.title()`                   | Converts the first character of each word to uppercase and the rest to lowercase.                |
| `str.capitalize()`              | Capitalizes the first character of the string and lowers all other characters.                   |
| `str.strip()`                   | Removes any leading and trailing whitespace from the string.                                      |
| `str.split(separator)`          | Splits the string into a list of substrings based on the specified separator.                    |
| `str.join(iterable)`            | Concatenates a list or tuple of strings into a single string, separated by the string used to call the method. |
| `str.replace(old, new)`         | Replaces all occurrences of a substring with another substring.                                  |
| `str.find(substring)`           | Returns the lowest index of the substring if found in the string; otherwise, it returns -1.     |
| `str.rfind(substring)`          | Returns the highest index of the substring if found in the string; otherwise, it returns -1.     |
| `str.count(substring)`          | Returns the number of occurrences of a substring in the string.                                  |
| `str.startswith(prefix)`        | Returns `True` if the string starts with the specified prefix; otherwise, it returns `False`.   |
| `str.endswith(suffix)`          | Returns `True` if the string ends with the specified suffix; otherwise, it returns `False`.     |
| `str.isdigit()`                 | Returns `True` if all characters in the string are digits; otherwise, it returns `False`.      |
| `str.isalpha()`                 | Returns `True` if all characters in the string are alphabetic; otherwise, it returns `False`.   |
| `str.isalnum()`                 | Returns `True` if all characters in the string are alphanumeric; otherwise, it returns `False`. |
| `str.format(*args, **kwargs)`   | Formats the string using the specified arguments or keyword arguments.                            |
