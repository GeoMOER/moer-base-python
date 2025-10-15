---
title: "EX | First steps in Python"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "confused"
  caption: "Image by [slon_pics](https://pixabay.com/de/users/www_slon_pics-5203613/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021) [from pixabay](https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021)"
---
*Making your first steps in Python with simple print() operations.*

<!--more-->

## #Hashtag and Run!

### Using Comments in Python

✍️  Add Comments to Structure and Clarify Your Code  
To make your code easier to understand — both for yourself and for others who review your work — it's important to use comments.  
In Python, everything following a `#` on a line is treated as a **comment** and is ignored by the interpreter.

Comments do not affect how your program runs, but they are extremely useful for:

- Explaining what your code does  
- Structuring your code clearly  
- Making your assignments easier to read and understand  

```python
# This is a comment. Comments help you understand your code later.
# Use them often to clarify what your code does.

print("Welcome to Python")
```

---

## Your First Python Steps in **Jupyter (Marburg)**

In this course, we use **Jupyter Notebooks** provided by the University of Marburg.  
They allow you to write, run, and document code interactively in your browser.

---

### 1️⃣ Open Jupyter (Marburg)

1. Go to the **Jupyter Marburg** platform (via your course link).  
2. Create or open a new notebook.  
3. In the first cell, write your Python code.

---

### 2️⃣ Write Your First Program

In a new code cell, type the following:

```python
# First Print Example
# This is my first Python program

print("Hello World")
```

Now press <kbd>Shift</kbd> + <kbd>Enter</kbd>  
➡️ The code runs, and you should see:

```
Hello World
```

Congratulations! 🎉  
You’ve just written and executed your first Python program.

---

## 🗒️ Writing Header Comments

Every homework assignment (Python script) should start with a short header comment before this, please use the following format at the top:
   - ❗include unitXX_assigment.py
   - 🔖 include your **student ID number**
   -  *and your full name*  

Below the header, each exercise or solution should begin with an additional short comment that briefly explains what the code does — this is highly recommended for good programming practice.

Example:
```python
# unit01_assignment.py
# Student ID: 12345678
# Name: <Your Name>


# This script prints a simple greeting message as the first exercise solution.
print("Hello World")
```

---
💡 *Always include such header comments at the top of every `.py` file you submit.*

## 🧠 Try It Yourself – Using `input()`

To make your program interactive, you can ask the user for input.

```python
# unit01_assignment.py
# Student ID: 12345678
# Name: <Your Name>

# Description: Simple program that greets the user by name.

name = input("Enter your name, please: ")
print("Hello,", name)
input("Press Enter to exit...")
print("Thanks!")
```

Run this code in Jupyter first,  
then export it again as `.py` and try to run it locally from the console.


---



---



✅ **Summary**

- In Jupyter Marburg, use code cells to experiment interactively.  
- Always start each program with a **header comment** (`# Unit, Name, Date`).  
- Use `#` to explain what your code does.  
- You can export your notebook as a `.py` file.  
- Local `.py` files can be executed using the **command line** with:
  ```bash
  python filename.py
  ```