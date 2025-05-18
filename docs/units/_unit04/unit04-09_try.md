---
title: try and catch
header:
  image: /assets/images/unit_images/u07/header.png
  image_description: "loop"
  caption: "Photo by [Christopher Kuszajewski](https://pixabay.com/de/users/kuszapro-369349/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=583537) [from Pixabay](https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=583537)"
---

try and catch (or except in Python) are considered control structures in programming.hey are part of error handling and allow a program to manage exceptions or errors that may occur during execution. Here's how they fit into the category of control structures:

# How `try` Works in Python

In Python, the `try` statement is used to catch and handle exceptions, allowing your program to continue running even when errors occur. This is an essential feature for writing robust and user-friendly applications. 

## Structure of a `try` Statement

A `try` statement typically consists of the following components:

1. **`try` Block**: This block contains the code that might raise an exception. 
2. **`except` Block**: This block contains the code that executes if an exception occurs in the `try` block.
3. **Optional `else` Block**: If present, this block runs if no exceptions were raised in the `try` block.
4. **Optional `finally` Block**: This block always runs, regardless of whether an exception was raised or not.

## Example

Here is a basic example demonstrating how to use the `try` statement:

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("You can't divide by zero!")
else:
    # Code to execute if no exceptions occur
    print("The result is:", result)
finally:
    # Code that always runs
    print("Execution completed.")
```

## Explanation of the Example
The code inside the try block attempts to divide by zero, which raises a ZeroDivisionError.
The except block catches the exception and executes the error handling code, printing an appropriate message.
The else block does not run because an exception occurred.
The finally block runs regardless of whether an exception occurred, indicating that execution is complete.


## Summary
Using try and except allows developers to manage exceptions gracefully, improving the overall robustness of the application. It helps to prevent the program from crashing and provides a way to handle errors effectively.
