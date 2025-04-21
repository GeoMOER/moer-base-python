---
title: "Introduction to Python – Variables and Basic Data Types"
header:
  image: /assets/images/unit_images/u09/header.png
  image_description: "statistics"
  caption: "Photo by [Gerd Altmann](https://pixabay.com/de/users/geralt-9301/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4705451) [from Pixabay](https://pixabay.com/)"
---

## 1. Exercise

### Algorithm: Baking Bread (Everyday Algorithm)

Describe the process of baking bread as a clear, step-by-step algorithm.
Imagine you are giving instructions to a robot – each action must be simple, complete, and in the correct order.

Your task:
Write the algorithm as a numbered list.

Include at least two different loops (repeating actions), for example:

Checking whether the dough has risen enough

Waiting for the oven to reach the correct temperature

Create a simple flowchart that represents the algorithm visually.

You may use tools like draw.io, diagrams.net, PowerPoint, or draw it by hand and take a photo.

**Example start:**
1. Get a large bowl.  
2. Add 500g of flour.  
3. Measure and add 300ml of warm water.  
4. ...

---

## 2. Exercise

### Python and Artificial Intelligence (AI)

**Answer the following questions in writing:**

- What role does **Python** play in the field of Artificial Intelligence?
- Name at some popular AI or data science libraries in Python.

---

## 3. Exercise

### How does Python translate code into machine code?

**Answer in your own words.**


---

## 4. Exercise

### What are variables and why do we use them.

**Answer in your own words.**

- Define what a variable is in programming.
- Why are variables essential in any program?
- Can variables change their value or data type?

---

## 5. Exercise

### Define 4 variables with meaningful names and different data types

**Write your solution as a Python code.**

Use this data types:
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

## 6. Exercise

### Mathematical operations and using the `math` library

**Write your solution as a Python code.**

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

## 7. Exercise

### Boolean values and comparisons

**Write your solution as a Python code.**

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


## 8. Exercise

### Strings and slicing

**Write your solution as a Python code.**

In this task, you will practice working with strings using **only slicing (`[:]`)** – no other string functions or methods.

1. Ask the user to input the following information using the `input()` function:
   - First name
   - Last name
   - Street address
   - City
   - Age (as string)

2. Use slicing to:
   - Extract the first 3 letters of the first name.
   - Extract the last 2 letters of the last name.
   - Extract the first 5 characters of the address.
   - Extract the last 3 characters of the city.
   - Extract only the first digit of the age string.
   - Print all characters of the first name **except the last one** using `[:-1]` and explain what this slicing does.
   - Replace the first letter of the last name by concatenating slices (e.g., change "Klein" to "Blein").
   - Create a new string from the city where the middle part is removed using slicing.

3. Use `print()` to show the results with labels. All outputs should be clearly formatted.

👉 Make sure to test your code with different inputs and see how slicing behaves.

---

## 9. Exercise

### Converting Data Types in Python

**Write your solution as a Python code.**

You are developing a program for managing bakery orders. Simulate user input by defining all inputs as strings:

```python
product_name = "Wholegrain Bread"
price = "3.79"         # net price (without tax)
quantity = "12"
available = "True"
```

Your tasks:

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
