---
title: "A | Assignment"
header:
  image: /assets/images/unit_images/u07/header.png
  image_description: "loop"
  caption: "Photo by [Christopher Kuszajewski](https://pixabay.com/de/users/kuszapro-369349/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=583537) [from Pixabay](https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=583537)"
---

## 🧩 Strings: Functions and Methods

### Exercise 1 – String Functions and Methods

#### Version A: Use a specific text
Use the following text:
```python
text = "Python is fun and powerful!"
```

Write code that:
- Prints the text in **uppercase**
- Prints the text in **lowercase**
- Prints the **number of characters**
- Checks if the word `"Python"` is **in the text**

#### Version B: General version
Use a variable like this:
```python
text = "Your example sentence here."
```
and perform the same operations as in Version A.

---

### Exercise 2 – `len()` and `print(text, text)`

Use this string:
```python
sentence = "Learning Python is exciting"
```

Write code that:
- Prints the sentence **two times in one line**, separated by a space
- Prints the **total number of characters** in the sentence (including spaces)

*Hint:* Use `print(sentence, sentence)` and `len(sentence)`

---

### Exercise 3 – `find()` and `count()` (Bonus)

Use this string:
```python
quote = "Practice makes perfect. Keep practicing to improve."
```

Write code that:
- Finds the **position** of the first occurrence of the word `"practice"` (case-sensitive!)
- Counts how many times the word `"practice"` appears (case-sensitive)

*Hint:* Try using `.find("practice")` and `.count("practice")`

---

## 🧠  Logical Operators

### Exercise 4 – Boolean Logic

Use the variables:
```python
a = True
b = False
```

Calculate and print the results of:
- `a and b`
- `a or b`
- `not a`

Add comments explaining the output.

---

### Exercise 5 – Logical Expression Without `if`

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

Expected output:
```
True
```

---

## Comparison Operators

### Exercise 6 – Comparing Strings

Use:
```python
name1 = "Alice"
name2 = "Bob"
```

Write code that:
- Checks if the names are **equal**
- Compares their **lengths** and prints which one is longer or if they are the same length

---

### Exercise 7 – Range Check

Use a variable:
```python
number = 35
```

Write code that checks whether the number is **between 10 and 50**, inclusive, and prints the result.

---

## athematical Operators

### Exercise 8 – Basic Calculations

Use:
```python
a = 12
b = 5
```

Perform and print the result of each of the following:
- `a + b` (Addition)
- `a - b` (Subtraction)
- `a * b` (Multiplication)
- `a / b` (Division)
- `a // b` (Integer Division)
- `a % b` (Modulus / Remainder)
- `a ** b` (Exponentiation)

---

### Exercise 9 – BONUS: Combined String Methods

Use the following string:
```python
text = "Success is not the key to happiness. Happiness is the key to success."
```

Write code that:
- Counts how many times the word `"key"` appears in the text (case-sensitive)
- Finds the position of the **second occurrence** of the word `"success"` (case-insensitive!)
- Calculates and prints the **number of characters** *without spaces*

*Hints:*
- Use `.count()`, `.lower()`, `.find()`, and string slicing.
- For the second occurrence, find the first position, then search again **starting just after that position**.
- To remove spaces, use `.replace(" ", "")` before applying `len()`.

