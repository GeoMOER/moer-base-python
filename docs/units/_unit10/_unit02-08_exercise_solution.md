---
title: "Python Exercise - Solutions"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "confused"
  caption: "Image by [slon_pics](https://pixabay.com/de/users/www_slon_pics-5203613/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021) [from pixabay](https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021)"
---

# Introduction

This document contains the solutions to the Python exercise tasks. Let's go through each task and its solution step-by-step.

## Task 1: Add, Subtract, and Multiply Two Numbers

### Solution:

```python
# Defining two numbers
number1 = 10
number2 = 5

# Adding, subtracting, and multiplying
sum_result = number1 + number2
sub_result = number1 - number2
mul_result = number1 * number2

# Printing the results
print(f"Sum: {sum_result}, Subtraction: {sub_result}, Multiplication: {mul_result}")
```

---

## Task 2: Variables and Types

### Solution:

```python
# Defining variables
zahl1 = 10 # Integer
zahl2 = 2.5 # Float
text = "Hello, World!" # String

# Displaying values
print(f"Zahl1: {zahl1}, Zahl2: {zahl2}, Text: {text}")

# Calculating sum of zahl1 and zahl2
sum_var = zahl1 + zahl2
print(f"Sum of zahl1 and zahl2: {sum_var}")

# Printing data types
print(f"Type of zahl1: {type(zahl1)}, Type of zahl2: {type(zahl2)}, Type of text: {type(text)}")

```

---

## Task 3: String Manipulation

### Solution:

```python
# Defining strings
string1 = "Hello"
string2 = "World"

# Concatenating strings
concatenated_string = string1 + " " + string2
print(f"Concatenated string: {concatenated_string}")

# Length of concatenated string
length_concatenated = len(concatenated_string)
print(f"Length of concatenated string: {length_concatenated}")

# Replacing characters in string1
replaced_string1 = string1.replace("l", "x")
print(f"Replaced string1: {replaced_string1}")

# Finding character in string2
position_char = string2.find("o")
print(f"Position of 'o' in string2: {position_char}")

# Splitting string2
split_string2 = string2.split("o")
print(f"Split string2: {split_string2}")

# Counting occurrences of character in string1
count_l_in_string1 = string1.count("l")
print(f"Occurrences of 'l' in string1: {count_l_in_string1}")

# Changing string1 to uppercase and lowercase
uppercase_string1 = string1.upper()
lowercase_string1 = string1.lower()
print(f"Uppercase string1: {uppercase_string1}, Lowercase string1: {lowercase_string1}")

# Extracting substring from string1
substring_string1 = string1[1:4]
print(f"Extracted substring from string1: {substring_string1}")
```

---

## Task 4: Replace Characters in a String Using Input

### Solution:
```python
# Asking user for input
sentence = input("Enter a sentence: ")
char_to_replace = input("Enter the character to be replaced: ")
replacement_char = input("Enter the replacement character: ")

# Replacing characters
new_sentence = sentence.replace(char_to_replace, replacement_char)

# Printing the result
print(f"Modified sentence: {new_sentence}")
```
---