
# ✅ Solutions: Introduction to Python – Variables and Basic Data Types

---

## 1. Algorithm: Baking Bread

Get a large bowl.

Add 500g of flour.

Add 1 tsp salt.

Add 1 packet of dry yeast.

Pour in 300ml of warm water.

Mix the ingredients until combined.

Knead the dough for 10 minutes.

Cover the bowl with a towel.

Repeat until the dough has doubled in size:

Wait 10 minutes

Check if dough has risen enough

Preheat the oven to 220°C.

Repeat until oven has reached 220°C:

Wait 2 minutes

Check temperature

Shape the dough and place it on a baking tray.

Put the tray in the oven.

Bake for 35 minutes.

Remove bread from oven and let it cool down.

Slice and serve.
---

## 2. Python and Artificial Intelligence (AI)

- Python is widely used in AI for its clear syntax, readability, and a vast collection of libraries.  
- Popular libraries: `TensorFlow`, `scikit-learn`, `Keras`, `PyTorch`, `pandas`, `NumPy`.

---

## 3. Python and Machine Code

- Python uses an interpreter that converts code into bytecode, which is executed by the Python virtual machine.  
- It allows easier debugging and cross-platform compatibility but may be slower than compiled languages.

---

## 4. Variables

- A variable is a named container used to store values in a program.  
- They are essential for storing data, performing operations, and making code reusable.  
- Yes, in Python, variables can change their value and even their data type.

---

## 5. Python Variables

```python
age = 25                    # Integer
name = "Alice"              # String
price = 4.95                # Float
is_available = True         # Boolean

print("age:", age, "| Type:", type(age))
print("name:", name, "| Type:", type(name))
print("price:", price, "| Type:", type(price))
print("is_available:", is_available, "| Type:", type(is_available))
```

---

## 6. Mathematical Operations

```python
import math

a = 16
b = 3

power = math.pow(a, b)
square_root = math.sqrt(a)
log_b = math.log(b)
floor_div = a // b
modulo = a % b

print("a^b:", power, "| Type:", type(power))
print("sqrt(a):", square_root, "| Type:", type(square_root))
print("log(b):", log_b, "| Type:", type(log_b))
print("a // b:", floor_div, "| Type:", type(floor_div))
print("a % b:", modulo, "| Type:", type(modulo))
```

---

## 7. Boolean Values and Comparisons

```python
is_logged_in = True
has_permission = False
is_admin = True

print("is_logged_in:", is_logged_in)
print("has_permission:", has_permission)
print("is_admin:", is_admin)

x1 = 4
x2 = 9
x3 = 16
x4 = 25

r1 = math.sqrt(x1)
r2 = math.sqrt(x2)
r3 = math.sqrt(x3)
r4 = math.sqrt(x4)

print("r1 > r2:", r1 > r2)
print("r3 > r4:", r3 > r4)
print("r2 > r1 and r4 > r3:", r2 > r1 and r4 > r3)
```

---

## 8. Strings and Slicing

```python
first_name = "Anna"
last_name = "Klein"
address = "Maple Street 12"
city = "Hamburg"
age = "24"

print("First 3 letters of first name:", first_name[:3])
print("Last 2 letters of last name:", last_name[-2:])
print("First 5 characters of address:", address[:5])
print("Last 3 characters of city:", city[-3:])
print("First digit of age:", age[0])
print("First name without last character:", first_name[:-1])  # removes last character
print("Modified last name:", "B" + last_name[1:])  # Replaces first letter
print("City with middle removed:", city[:2] + city[-2:])
```

---

## 9. Data Type Conversion and Calculations

```python
product_name = "Wholegrain Bread"
price = "3.79"
quantity = "12"
available = "True"

price = float(price)
quantity = int(quantity)
available = available == "True"

print("Product:", product_name)
print("Price:", price, "| Type:", type(price))
print("Quantity:", quantity, "| Type:", type(quantity))
print("Available:", available, "| Type:", type(available))

# Net total
total_net = price * quantity
print("Total net:", total_net, "| Type:", type(total_net))

# Tax and gross total
tax = total_net * 0.19
total_gross = total_net + tax
print("Total gross:", total_gross, "| Type:", type(total_gross))

# Final sentence
final_sentence = f"{quantity} {product_name} cost {round(total_gross, 2)} euros (including tax)."
print(final_sentence)
```

---
