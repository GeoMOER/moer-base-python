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
To make your code easier to understand — both for yourself and for others who review your work — it's important to use comments. In Python, everything following a `#` on a line is treated as a comment and is ignored by the interpreter.

Comments do not affect how your program runs, but they are extremely useful for:

- Explaining what your code does
- Structuring your code clearly
- Making your assignments easier to read and grade

```python
# This is a comment. Comments help you understand your code later.
# Use them often to clarify what your code does.

print("Welcome to Python")
```

---

## Create Your First Python File in Visual Studio Code

### 1. Create a New Folder for This Unit
- Open **Visual Studio Code**.
- Click on **File → Open Folder...** and create a new folder named:
  ```
  unit01_EX
  ```

### 2. Create a New Python File
- Inside the folder `unit01_EX`, create a new file called:
  ```
  first_steps_hello.py
  ```

### 3. Write Your First Script with a Comment
```python
# Unit 01 – First Print Example
# This is my first Python program

print("Hello World")
```

- Save the file with <kbd>Ctrl</kbd> + <kbd>S</kbd>.

### 4. Open the Terminal in VS Code
- Go to **View → Terminal** or press <kbd>Ctrl</kbd> + <kbd>`</kbd>.
- Navigate to the folder using:
  ```sh
  cd unit01_EX
  ```

### 5. Run Your Script
```sh
python first_steps_hello.py
```

---

## Using `input()` to Pause or Interact

### 1. Create a New File
- In the same folder `unit01_EX`, create a file called:
  ```
  first_steps_input.py
  ```

### 2. Write a Script with Input
```python
# Unit 01 – Using input()
# This script pauses until the user presses Enter
name = input("Enter your name please ")
print(name)
input("Press Enter to continue...")
print("Thanks!")
```

### 3. Save and Run the Script
- Save the file and run it in the VS Code terminal:
  ```sh
  python first_steps_input.py
  ```

This is your first interactive Python script!