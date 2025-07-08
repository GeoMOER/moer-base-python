---
title: "A | Assignment"
header:
  image: /assets/images/unit_images/u04/header.png
  image_description: "if logic structure"
  caption: "Photo by [Markus Spiske](https://unsplash.com/@markusspiske) [from Unsplash](https://unsplash.com/photos/code-on-laptop-screen-FXFz-sW0uwo)"
---

# Conditional Statements and Error Handling in Python

Please save your solutions for Exercises 1 to 6  in a single Python script named `unit04__ex(1-6)code.py`.  
For Bonus Exercise 8, use a separate Python script named `unit04__ex7code.py`.

Save all scripts in the same `unit04` folder, compress the folder into a `.zip` file, and upload it to ILIAS.

For more information, please visit the following link:  
https://geomoer.github.io/moer-base-python/unit00/unit00-04_submission_guidelines.html

Make sure your code is clearly structured and includes comments where helpful.
##  Exercise 1 – Theory Test (Multiple Choice)

**Which of the following statements are correct?**

A) An `if` statement can never be used without `else`.  
B) `elif` can only be used once per `if` block.  
C) `try-except` only catches import errors.  
D) `if`, `elif`, `else` allow checking different conditions in sequence.  
E) `try-catch` is the correct syntax for error handling in Python.

> **Select all correct answers.**

---

## Exercise 2 – Temperature Check (if)

Write a program that asks the user to enter a temperature in °C.  
If the temperature is below 0, print:  
`"Warning: Risk of frost!"`

**Example:**
```
Temperature: -3
Warning: Risk of frost!
```

---

## Exercise 3 – Age Check (if-else)

Ask the user for their age.  
If the age is at least 18, print: `"Access granted."`  
Otherwise, print: `"Access for adults only!"`

---

## Exercise 4 – Weekday Checker (if-elif-else)

Ask the user to enter the name of a weekday (`"Monday"` to `"Sunday"`).  
Print whether it's the **start of the week**, **midweek**, or **weekend**.

**Example:**
```
Day: Monday
It is the start of the week.
```

---

## Exercise 5 – Password Strength (nested ifs)

Ask the user to enter a password. Depending on the length, print:

- Length < 4 → `"Way too short!"`  
- Length < 8 → `"Too short"`  
- Length ≥ 8 → `"Strong password"`

**Hint**: Use nested `if` statements.

---

## Exercise 6 – Grade Evaluation (if-elif-else)

Ask the user for a score (0–100) and print a grade:

- 90–100 → `"Very good"`  
- 75–89 → `"Good"`  
- 60–74 → `"Satisfactory"`  
- 50–59 → `"Sufficient"`  
- <50 → `"Failed"`

---

## Exercise 7 – Bonus: Mini Calculator with Error Handling (try-except)

Create a program that asks the user to input two numbers and divides them.  
Use `try-except` to catch division by zero.

**Example:**
```
Number 1: 10
Number 2: 0
Error: Division by zero is not allowed!
```
