---
title: "Python Exercise - Solution 2"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "keyboard"
  caption: "Image by [username](https://pixabay.com) from pixabay"
---

# Introduction

This unit covers how to work with user input and loops in Python. You will practice collecting input from the user, performing operations on lists, and implementing password checks with limited attempts.

## Task 1: Enter Numbers, Find Maximum and Minimum, and Sort the List

### Solution:
```python
# Step 1: Initialize an empty list to store the numbers
number_list = []

# Step 2: Use a while loop to get 5 numbers from the user
attempt = 1
while attempt <= 5:
    number = int(input(f"Enter number {attempt}: "))
    number_list.append(number)
    attempt += 1

# Step 4: Find the minimum and maximum values
minimum = min(number_list)
maximum = max(number_list)

# Step 5: Sort the list
number_list.sort()

# Step 6: Output the sorted list, the minimum, and the maximum
print(f"Sorted List: {number_list}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")

```
---

## Task 2: Password Input with Limited Attempts

### Solution:
```python
# Step 1: Define the correct password
correct_password = "secret"

# Step 2: Initialize variables
attempts = 0
max_attempts = 5

# Step 3: While loop to allow up to 5 attempts to guess the password
while attempts < max_attempts:
    password_input = input("Please enter the password: ")

    # Step 5: Check if the entered password is correct
    if password_input == correct_password:
        print("Success! The password is correct.")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print(f"Incorrect password. Attempt {attempts} of {max_attempts}.")
        else:
            print("Too many incorrect attempts. Access denied.")
```