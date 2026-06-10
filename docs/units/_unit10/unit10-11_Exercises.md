---
title: EX | Exercises
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u10/header.png
  image_description: "Object-oriented programming concept"
  caption: "Image concept and AI prompt: Spaska Forteva – Generated with ChatGPT/DALL·E"
---

## 1. Basic Data Types – "What is it?"

> **Task:**  
> You have defined the following variables:
> ```python
> a = 42
> b = 3.14
> c = "Hello"
> d = True
> e = [1, 2, 3]
> ```
>
> **Question:**  
> Which of the following statements is **false**?  
> A) `a` is an `int`  
> B) `b` is a `float`  
> C) `c` is a `str`  
> D) `d` is a `bool`  
> E) `e` is a `list`  
> F) `a` can be used as a `float`  
> G) `c` can be concatenated with a number using `+`  
>
> **Explain why the false statement is incorrect.**

---

## 2. Working with Strings and Operators – "What comes out?"

> **Task:**  
> What is printed when the following code runs?
> ```python
> text = "Python"
> num = 3
> result = text * num + " is awesome!"
> print(result)
> ```
>
> **Questions:**  
> - Why is `text * num` not interpreted as addition?  
> - What happens if you try `text + num`?  
> - How can you convert `num` to a string so that concatenation works?

---

## 3. Conditionals – "Which condition fits?"

> **Task:**  
> You have a function that checks if a student passed:
> ```python
> def check_pass(mark):
>     if mark >= 50:
>         return "Passed"
>     elif mark >= 40:
>         return "Not passed, but retake possible"
>     else:
>         return "Not passed"
> ```
>
> **Question:**  
> Which of the following statements is **correct**?  
> A) All test cases are correct.  
> B) Only `check_pass(40)` is wrong.  
> C) `check_pass(45)` should return "Passed".  
> D) The function is flawed because 40 is not eligible for a retake.  
>
> **Explain why your answer is correct.**

---

## 4. Object Data Types – "Which structure fits?"

> **Task:**  
> You want to store the following data:
> - Names of 5 students  
> - Their grades in Math, German, and English  
> - The average grade per student  
>
> **Question:**  
> Which data structure (list, array, DataFrame) is **best suited**?  
> Justify your choice with **at least three reasons**.  
> How would you calculate the average grade?  
> **Write your solution in Python.**

---

## 5. Loops – "What is the output?"

> **Task:**  
> What is printed when this loop runs?
> ```python
> for i in range(1, 6):
>     if i % 2 == 0:
>         print(f"{i} is even")
>     else:
>         print(f"{i} is odd")
> ```
>
> **Questions:**  
> - What happens if you replace `range(1, 6)` with `range(0, 6)`?  
> - How can you modify the `range()` to print only even numbers?  
> **Write your solution.**

---

## 6. Working with Files (CSV) – "Find the error"

> **Task:**  
> You have the following code to read a CSV file:
> ```python
> import pandas as pd
> df = pd.read_csv("books.csv")
> print(df.head())
> ```
>
> **Question:**  
> Could the following **three errors** cause the code to fail?  
> - The file is in the wrong format (e.g., `.xlsx`)  
> - The encoding is incorrect  
> - The delimiter is wrong  
>
> **How can you catch and prevent these errors?**  
> **Write a robust version of the code using `try`/`except` blocks.**

---

## 7. Simple Visualisations – "What does it say?"

> **Task:**  
> You have a DataFrame with the following data:
> ```python
> data = {
>     "Month": ["Jan", "Feb", "Mar", "Apr"],
>     "Sales": [100, 150, 200, 180]
> }
> df = pd.DataFrame(data)
> ```
>
> You create a bar chart using `df.plot(kind='bar')`.
>
> **Questions:**  
> - What does the chart show?  
> - Why is a **bar chart** better than a **pie chart** for this data?  
> - How could you improve the chart (e.g., with title, axis labels)?

---

## 📌 8. Creative Task – "Write your own function" (Creativity & Application)

> **Task:**  
> Write a function that:
> - Takes a list of numbers  
> - Filters only the **even numbers**  
> - Calculates the **average** of the even numbers  
> - Prints a message:
>   - If average ≥ 50: "Good performance!"  
>   - If average < 50: "Still room for improvement."  
>
> **Write the function in Python.**  
>
> **Hint:**  
> - Use `for` loop or list comprehension  
> - Use `sum()` and `len()`  
> - Use `print()` to output results

---

