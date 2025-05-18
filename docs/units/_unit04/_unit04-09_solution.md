---
title: "Python Exercise - Solutions"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u02/header.png
  image_description: "thinking"
  caption: "Image by [pexels](https://pixabay.com/de/users/pexels-2286921/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1559046) [from pixabay](https://pixabay.com/de/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1559046)"
---

## Task 1: Age Verification

### Solution:
```python
# Get user input
age = int(input("Enter your age: "))

# Check age
if age >= 18:
    print("You are an adult.")

```

---

## Task 2: Even or Odd Number

### Solution:
```python
# Get user input
number = int(input("Enter a number: "))

# Check even or odd
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

```

---

## Task 3: Grade Evaluation

### Solution:
```python
# Get user input
grade = int(input("Enter your points (0-100): "))

# Grade evaluation
if grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Good")
elif grade >= 70:
    print("Satisfactory")
elif grade >= 60:
    print("Pass")
elif grade >= 50:
    print("Poor")
else:
    print("Fail")
```

---

## Task 4: Temperature Classification

### Solution:
```python
# Task 4: Temperature Classification

# Get user input
temperature = int(input("Enter a temperature in Celsius: "))

# Temperature classification
if temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
elif temperature >= 10:
    print("Cool")
else:
    print("Cold")
```

---