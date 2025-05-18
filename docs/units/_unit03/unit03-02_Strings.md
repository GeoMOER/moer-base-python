---
title: "EX | Strings: Functions and Methods"
toc: true
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---

<!--more-->

## 🧩 What is a Function?
A function is a reusable block of code that performs a specific task. You call it by its name, followed by parentheses containing any values (parameters) it needs to work with.

Python provides several built-in functions for string manipulation.


```python
function_name(parameter1, parameter2, ...)
```
## String Functions

### `print()`

Displays output in the console.
You can print text, variables, or multiple values by separating them with commas.

```python
name = "Alice"
age = 25
print("Name:", name, "| Age:", age)

```

### `len()`

Returns the length of a string.

```python
length = len("Hello, World!")
print(length)  # Output: 13
```


## 🧩 What is a Method?

A **method** is similar to a function, but it is **attached to an object** (like a string)  
and is called using **dot notation (`.`)**. It performs a task that is specific to that object.

Example:  
```python
myString = "Hello"
myString.method_name(parameter1, parameter2, ...)
```

## String Methods


### `replace()`

Replaces parts of a string. The replace() method can take up to three parameters:

```python
string.replace(old, new, count)
```

- **old**: The part of the string you want to replace  
- **new**: What you want to replace it with  
- **count** *(optional)*: How many times to replace it (from left to right)

```python
textA = "apple apple apple"
textB = textA.replace("apple", "banana")
print(textB)  
# Output: banana banana banana

print(text.replace("apple", "banana", 1))  
# Output: banana apple apple
```


### `find()``

Searches for a substring in a string and returns the index of its first occurrence. If the substring is not found, it returns -1.

The find() method can take up to three parameters:
```python
string.find(sub, start, end)
```
- **sub**: The substring you want to search for  
- **start** *(optional)*: The index to start the search from  
- **end** *(optional)*: The index to stop the search (not inclusive)

```python
text = "environmental informatics"

print(text.find("informatics"))   # Output: 14
print(text.find("a", 5))          # Output: 11
print(text.find("i", 5, 10))      # Output: -1
```
text.find("informatics")

"informatics" beginnt bei Index 14
text.find("a", 5)
Suche "a" ab Index 5 → erstes "a" ist bei 11 (in "mental")
text.find("i", 5, 10)
Bereich ist "nment" (Index 5–9) → kein "i" enthalten → -1

### `count()`

Counts how many times a substring appears in a string.

The count() method can take up to three parameters:
```python
string.count(sub, start, end)
```
- **sub**: The substring you want to count  
- **start** *(optional)*: The index to start counting from  
- **end** *(optional)*: The index to stop counting (not inclusive)

```python
text = "banana banana banana"
print(text.count("banana"))         # Output: 3
print(text.count("banana", 10))     # Output: 2
print(text.count("banana", 10, 20)) # Output: 1
```

### `upper()`, `lower()`, `title()`, `capitalize()`

```python
text = "marburg an der lahn"
textUpper = text.upper() 
print(textUpper)       # MARBURG AN DER LAHN
print(text.lower())       # marburg an der lahn
print(text.title())       # Marburg An Der Lahn
print(text.capitalize())  # Marburg an der lahn
```

### `split()`

Splits a string into a list, using a specified separator.

The split() method can take up to two parameters:
```python
string.split(sep, maxsplit)
``

- **sep** *(optional)*: The delimiter to split the string on (default is any whitespace)  
- **maxsplit** *(optional)*: The maximum number of splits to perform

```python
text = "apple,banana,cherry"
textList = text.split(",")
print(textList)         # Output: ['apple', 'banana', 'cherry']

text2 = "one two three four"
print(text2.split(" ", 2))     # Output: ['one', 'two', 'three four']

```


## Bonus - String Methods in Python

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
