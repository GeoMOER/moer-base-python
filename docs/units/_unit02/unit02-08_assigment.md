---
title: " A | Assignment"
header:
  image: /assets/images/unit_images/u09/header.png
  image_description: "statistics"
  caption: "Photo by [Gerd Altmann](https://pixabay.com/de/users/geralt-9301/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4705451) [from Pixabay](https://pixabay.com/)"
---
Please save your solution for Exercise 1 as a PDF file named `unit02_ex1.pdf` and place it in the `unit02` folder.

Then complete Exercises 2 to 5 and write your solutions in a single Python script named `unit02__ex2-5code.py`.  
For Bonus Exercise 6, use a separate Python script named `unit02__ex6code.py`.

Save all scripts in the same `unit02` folder, compress the folder into a `.zip` file, and upload it to ILIAS.

For more information, please visit the following link:  
https://geomoer.github.io/moer-base-python/unit00/unit00-04_submission_guidelines.html

Make sure your code is clearly structured and includes comments where helpful.


## 1. Exercise

### How do we store and manage data in a program?

**Answer in your own words.**

- Explain how data is stored and managed in a program.
- Why is it important to organize data instead of working only with raw values?
- Can variables change their value or data type?

---

## 2. Exercise

### Define 4 variables with meaningful names and different data types.

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

## 3. Exercise

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

## 4. Exercise

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

## 5. Exercise

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

## 6. Bonus Exercise

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

5. Reverse conversion:
   - Convert the total gross price back to a string
   - Create a sentence like:  
     `"12 Wholegrain Bread cost 45.48 euros (including tax)."`
   - Print the final sentence

---
