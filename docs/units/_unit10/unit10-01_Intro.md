---
title: LM | Introduction
  image: /assets/images/unit_images/u10/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "Mobile Android operating system market share by version worldwide from 2018 to 2020: [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---


Welcome to the **Base Python course review section**!  

This section is designed to help you **refresh your skills**, strengthen your confidence, and prepare you for applying Python in more advanced projects or real-world tasks.  

Instead of simply repeating concepts, you are encouraged to actively **practice**, explore additional examples, and reflect on how each topic connects to problem-solving in programming.  

Take this time to revisit what you have learned, ask questions, and deepen your understanding — so you can continue your Python journey with a solid and confident foundation.

## 💡 Short Note: Functions in Python

A **function** is a reusable block of code that performs a specific task.  
You define a function using the `def` keyword, followed by the function name and parentheses.

**Example:**

```python
def showName(name):
    print(f"The given name is {name}!")

tempName = input("Bitte deinen Namen schreiben")

showName(tempName)
```

## 💡 Example: Function with Three Parameters and Default Values

You can define default values for function parameters, so they don't have to be provided every time.

**Example:**

```python
def describe_pet(name="Dog", age=2, color="brown"):
    print(f"This is a {color} {name}, and it is {age} years old.")

describe_pet()                 # Uses all default values
describe_pet("Cat", 5, "black") # Uses custom values
describe_pet(age=3)           # Only changes age
```