---
title: "Introduction to Python – Variables and Basic Data Types"
header:
  image: /assets/images/unit_images/u09/header.png
  image_description: "statistics"
  caption: "Photo by [Gerd Altmann](https://pixabay.com/de/users/geralt-9301/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4705451) [from Pixabay](https://pixabay.com/)"
---

## 1. Algorithm: Baking Bread (Everyday Algorithm)

Write a step-by-step algorithm that describes how to bake bread.  
Imagine you are giving instructions to a robot – **each step must be clear, complete, and in the correct order**.

**Example start:**
1. Get a large bowl.  
2. Add 500g of flour.  
3. Measure and add 300ml of warm water.  
4. ...

---

## 2. Python and Artificial Intelligence (AI)

**Answer the following questions in writing:**

- What role does **Python** play in the field of Artificial Intelligence?
- Name at some popular AI or data science libraries in Python.

*(Hint: Consider: readability, rapid development, community support, available libraries...)*

---

## 3. How does Python translate code into machine code?

Answer in your own words.

---

## 4. What are variables and why do we use them?

Answer in writing:

- Define what a variable is in programming.
- Why are variables essential in any program?
- Can variables change their value or data type?

---

## 5. Define 4 variables with meaningful names and different data types

Define the variables yourself using:
- A integer
- A string
- A float
- A boolean

Then, use print() to display each variable together with its data type using the type() function.

Example output format:
```python
print("Price:", price, "| Type:", type(price))
```
---

## 6. Mathematical operations using the `math` library

- Import the `math` module.
- Define two integer variables.
- Use the following math functions:  
  - `pow()`, `sqrt()`, `log()`
- Use `//` (floor division) and `%` (modulo).
- Store the results in new variables.
- Print each result together with its type using `type()`.

Make sure your variable names clearly describe what they store.
👉 Your print() statements should be well-formatted and readable – include clear labels for both the result and the data type.

Example:
```python
print("Square root of x:", root_x, "| Type:", type(root_x))
```
---

## 7. Boolean values and comparisons

- Define at least three boolean variables with meaningful names and print them.
- Define four numeric variables.
- Calculate the square root of each number.
- Compare the square roots using the greater-than operator (`>`).
- Print whether one value is greater than another.

**Bonus:** Try using combinations of comparisons, like:
```python
print(root_a > root_b and root_c > root_d)
```

---

## 8. Strings and slicing

In this task, you will practice working with strings using **only slicing (`[:]`)** – no other string functions or methods.

1. Define the following variables as strings:
   - First name
   - Last name
   - Street address
   - City
   - Age (as string)

2. Use slicing to:
   - Extract the first 3 letters of your first name.
   - Extract the last 2 letters of your last name.
   - Extract the first 5 characters of your address.
   - Extract the last 3 characters of your city.
   - Extract only the first digit of your age string.
   - Print all characters of your first name **except the last one** using `[:-1]` and explain what this slicing does.
   - Replace the first letter of your last name by concatenating slices (e.g., change "Klein" to "Blein").
   - Create a new string from your city where the middle part is removed using slicing.

3. Use `print()` to show the results with labels. All outputs should be clearly formatted.

### 🎯 Goal:
- Understand how slicing works in Python strings.
- Use slicing creatively to modify or extract parts of strings.
- Prepare for similar operations later with Python lists.

---

## 9. Converting Data Types in Python

You are developing a program for managing bakery orders. Simulate user input by defining all inputs as strings:

```python
product_name = "Wholegrain Bread"
price = "3.79"         # net price (without tax)
quantity = "12"
available = "True"
```

### Your tasks:

1. Convert:
   - price → float
   - quantity → int
   - available → boolean

2. Print each converted value and its data type using `type()`.  
   Make sure the output is clearly formatted and easy to read.

3. Calculate total net price:
   - Multiply quantity by net price
   - Store and print result with its type

4. Calculate total gross price (including 19% tax):
   - Calculate 19% of the total net price
   - Add it to the net total
   - Store and print the gross price and its type

5. Bonus – Reverse conversion:
   - Convert the total gross price back to a string
   - Create a sentence like:  
     `"12 Wholegrain Bread cost 45.48 euros (including tax)."`
   - Print the final sentence

---


---
