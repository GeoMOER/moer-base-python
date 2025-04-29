---
title: "Working with Strings: Functions and Methods"
toc: true
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---

<!--more-->


## Built-in String Functions

Python provides several built-in functions for string manipulation.

### `print()`

Outputs strings (or other data types) to the console.

```python
# Print a string
print("Hello, World!")  # Output: Hello, World!

# Print a string variable
message = "Hello, Python!"
print(message)  # Output: Hello, Python!
```

String concatenation in `print()` can be done using commas or f-strings:

```python
var1 = "Hello"
var2 = "World"

print(var1, var2)  # Hello World
print(f"{var1}, {var2}!")  # Hello, World!
```

### `len()`

Returns the length of a string.

```python
length = len("Hello, World!")
print(length)  # Output: 13
```

### `str()`

Converts other data types to strings.

```python
number = 42
number_string = str(number)
print(number_string)  # Output: '42'
```

### `type()`

Shows the type of a value or variable.

```python
text = "Marburg"
print(type(text))  # <class 'str'>

zahl = 42
print(type(zahl))  # <class 'int'>
```

### `sorted()`

Returns a sorted list of characters from a string.

```python
print(sorted("Marburg"))  # ['M', 'a', 'b', 'g', 'r', 'r', 'u']
```

### `list()`

Converts a string into a list of individual characters.

```python
print(list("Marburg"))  # ['M', 'a', 'r', 'b', 'u', 'r', 'g']
```

## Built-in String Methods

### `replace()`

Replaces parts of a string without modifying the original.

```python
original_string = "Hello, World!"
new_string = original_string.replace("World", "Python")
print(new_string)  # Output: Hello, Python!
```

### `strip()`

Removes leading and trailing whitespace.

```python
text = "  hello  "
print(text.strip())  # Output: hello
```

### `find()` and `rfind()`

Find first or last occurrence of a substring.

```python
text = "Hello, World! Hello, Python!"
print(text.find("Hello"))      # Output: 0
print(text.rfind("Hello"))     # Output: 13
```

### `count()`

Counts how many times a substring appears.

```python
text = "Hello, World! Hello, Python!"
print(text.count("Hello"))  # Output: 2
```

### `split()`

Splits string into substrings based on a separator.

```python
sentence = "Hello, World! How are you?"
words = sentence.split(" ")
print(words)
# Output: ['Hello,', 'World!', 'How', 'are', 'you?']
```

### `splitlines()`

Splits string at line breaks.

```python
multiline_string = """This is line one.
This is line two.
This is line three."""

lines = multiline_string.splitlines()
print(lines)
# Output: ['This is line one.', 'This is line two.', 'This is line three.']
```

### `upper()`, `lower()`, `title()`, `capitalize()`

```python
text = "marburg an der lahn"

print(text.upper())       # MARBURG AN DER LAHN
print(text.lower())       # marburg an der lahn
print(text.title())       # Marburg An Der Lahn
print(text.capitalize())  # Marburg an der lahn
```

### `join()`

Joins a list of strings into one string.

```python
words = ["Hello", "Python", "World"]
joined = " ".join(words)
print(joined)  # Output: Hello Python World
```

### `startswith()` and `endswith()`

```python
text = "hello world"
print(text.startswith("hello"))  # True
print(text.endswith("world"))    # True
```

### `isdigit()`, `isalpha()`, `isalnum()`

```python
print("123".isdigit())    # True
print("abc".isalpha())    # True
print("abc123".isalnum()) # True
```

### `format()`

Inserts values into a string using placeholders.

```python
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))
# Output: Name: Alice, Age: 30
```

### `zfill()` – Zero padding

```python
num = "42"
print(num.zfill(5))  # Output: 00042
```

### `center()` – Align text

```python
text = "Hi"
print(text.center(10, "-"))  # Output: ----Hi----
```

### `casefold()` – Aggressive lowercase conversion

```python
print("Straße".casefold() == "strasse".casefold())  # True
```

## 📋 String Methods in Python

| Method / Function               | Description                                                                                       |
|--------------------------------|---------------------------------------------------------------------------------------------------|
| `str.lower()`                  | Converts all characters to lowercase.                                                             |
| `str.upper()`                  | Converts all characters to uppercase.                                                             |
| `str.title()`                  | Capitalizes the first letter of each word.                                                       |
| `str.capitalize()`             | Capitalizes the first character of the string.                                                    |
| `str.strip()`                  | Removes leading and trailing whitespace.                                                          |
| `str.split(separator)`         | Splits the string into a list using the specified separator.                                      |
| `str.join(iterable)`           | Joins elements of a list or tuple into a single string.                                           |
| `str.replace(old, new)`        | Replaces all occurrences of `old` with `new`.                                                     |
| `str.find(substring)`          | Returns the first index of the substring or -1 if not found.                                     |
| `str.rfind(substring)`         | Returns the last index of the substring or -1 if not found.                                      |
| `str.count(substring)`         | Counts the number of times a substring appears.                                                  |
| `str.startswith(prefix)`       | Returns `True` if the string starts with `prefix`.                                                |
| `str.endswith(suffix)`         | Returns `True` if the string ends with `suffix`.                                                  |
| `str.isdigit()`                | Returns `True` if the string contains only digits.                                                |
| `str.isalpha()`                | Returns `True` if the string contains only letters.                                               |
| `str.isalnum()`                | Returns `True` if the string contains letters and numbers.                                        |
| `str.format(*args, **kwargs)`  | Formats strings using placeholders.                                                               |
| `str.zfill(width)`             | Pads the string with zeros on the left, until it reaches the desired width.                      |
| `str.center(width, fillchar)`  | Centers the string using the specified fill character.                                            |
| `str.casefold()`               | Aggressively lowercases the string for case-insensitive comparison.                              |

---

## Strings are immutable.

The String Methods and Functions create a New String!
→ The original remains unchanged!
A string is stored as a single object in memory, even if it consists of multiple characters.

All characters are stored as a unit.
You cannot change individual characters directly! (because the entire string is stored as a single block in memory)

✅ You're now ready to work efficiently with strings in Python!
