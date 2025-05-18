---
title: "A | Assignment"
header:
image: /assets/images/unit\_images/u07/header.png
image\_description: "loop"
caption: "Photo by [Christopher Kuszajewski](https://pixabay.com/de/users/kuszapro-369349/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=583537) [from Pixabay](https://pixabay.com/de/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=583537)"
---

## 🧹 Strings: Functions and Methods. Simple operators

Please save your solution Exercises 1 to 8 and write your solutions in a single Python script named `unit03__ex(1-8)code.py`.  
For Bonus Exercise 8, use a separate Python script named `unit03__ex10code.py`.

Save all scripts in the same `unit03` folder, compress the folder into a `.zip` file, and upload it to ILIAS.

For more information, please visit the following link:  
https://geomoer.github.io/moer-base-python/unit00/unit00-04_submission_guidelines.html

Make sure your code is clearly structured and includes comments where helpful.

### Exercise 1 – Short Text Questions

Answer the following questions in complete sentences:

* What are strings in Python?
* What does it mean that strings are *immutable*?
* What operators do you know in Python?

---

### Exercise 2 – String Functions and Methods

Use the following text:

```python
text = "Python is fun and powerful!"
```

Write code that:

* Prints the text in **uppercase**
* Prints the **number of characters** using `len()`
* Replaces the word `"fun"` with `"easy"`
* Splits the text into a list of words

---

### Exercise 3 – `len()` and `print()` with multiple parameters

Use this string:

```python
sentence = "Learning Python is exciting"
```

Write code that:

* Prints the sentence **two times in one line**, separated by a space
* Prints the **total number of characters** in the sentence (including spaces)

---

### Exercise 4 – `find()` and `count()` with optional parameters

Use this string:

```python
quote = "Practice makes perfect. Keep practicing to improve."
```

Write code that:

* Finds the **position** of the first occurrence of the word `"practice"` (case-sensitive!)
* Counts how many times the word `"practice"` appears (case-sensitive)
* Searches for the word `"e"` starting from index 10
* Counts how many times the word `"e"` appears between index 10 and 30

---

## 🧠 Logical Operators

### Exercise 5 – Boolean Logic

Use the variables:

```python
a = True
b = False
```

Calculate and print the results of:

* `a and b`
* `a or b`
* `not a`

Add short comments explaining the output.

---

### Exercise 6 – Logical Expression Without `if`

Use:

```python
x = 150
y = 25
```

Create a variable `result` that stores the result of this logical expression:

```python
(x > 100 or y > 100) and x > 0 and y > 0
```

Then print the value of `result`.

---

## 📊 Comparison Operators

### Exercise 7 – Comparing Strings

Use:

```python
name1 = "Alice"
name2 = "Bob"
```

Write code that:

* Checks if the names are **equal**
* Compares their **lengths** and prints which one is longer or if they are the same length

---

### Exercise 8 – Range Check

Use a variable:

```python
number = 35
```

Write code that checks whether the number is **between 10 and 50**, inclusive, and prints the result.

---

## 📈 Mathematical Operators

### Exercise 9 – Basic Calculations

Use:

```python
a = 12
b = 5
```

Perform and print the result of each of the following:

* `a + b`
* `a - b`
* `a * b`
* `a / b`
* `a % b`

---

### Exercise 10 – BONUS: Combined String Methods

Use the following string:

```python
text = "Success is not the key to happiness. Happiness is the key to success."
```

Write code that:

* Counts how many times the word `"key"` appears in the text (case-sensitive)
* Finds the position of the **second occurrence** of the word `"success"` (case-insensitive)
* Capitalizes the first letter of the sentence
* Replaces the second `"key"` with the word `"secret"`

*Hints:*

* Use `.count()`, `.lower()`, `.rfind()`, `.capitalize()`, and `.replace()`
* To find the second occurrence, first find the index of the first and start a second search from just after that position
