---
title: "LM | Lists"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from Unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---

<!--more-->

## 📦 Object Type: Lists

Lists in Python are versatile data containers that allow you to store multiple items in a single variable. They are one of the most commonly used data structures in Python due to their flexibility.

A list can contain elements of different data types, including numbers, strings, functions, and even other lists. This makes lists ideal for grouping related items and managing dynamic collections of data.

---

## What Are Lists Used For?

- **Storing collections of values** like numbers, names, or items in a cart  
- **Lists in Python are mutable**, meaning their contents can be changed after creation.
- **Dynamic operations**: adding, removing, or replacing items  
- **Iteration and filtering** using loops or conditions  
- **Nesting for complex structures**, e.g. lists of lists (matrices, trees)

---

## 🔧 Creating and Accessing Lists

### ✅ Basic creation

```python
names = ["Maria", "Evi", "Simon", "Peter"]
numbers = [44, 34, 5, 6]
mixed = ["hello", 3.14, True, [1, 2, 3]]
```

### ✅ Accessing elements by index-

Lists in Python are zero-indexed, which means the first element has index 0, the second has index 1, and so on.

You can access elements using square brackets [] and the element’s index:

```python
print(names[0])       # Output: Maria
print(mixed[3])       # Output: [1, 2, 3]
print(mixed[3][1])    # Output: 2 (accessing inside the nested list)
```

---

## ✏️ Modifying Lists

```python
names = ["Anna", "Ben", "Clara"]
names[1] = "Bernd"
print(names)  # ['Anna', 'Bernd', 'Clara']
```

## ➕ Using the + Operator with Lists

```python
list1 = [1, 2, 3]
list2 = [4, 5]
combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4, 5]
```
➡️ Note: The + operator does not modify the original lists. It creates a new list instead.

---

## 📏 The `len()` Function

The built-in Python function `len()` returns the number of elements in a list.

```python
my_list = [10, 20, 30]
print(len(my_list))  # Output: 3
```

## Common List Methods

### ➕ Adding Elements  - append() , insert(pos, element), extend()
```python
# Append - Adds a single element to the end of the list. 
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# If x is a list, it will be added as a nested list.
fruits.append(["date", "elderberry"])
# ['apple', 'banana', 'cherry', ['date', 'elderberry']]

# Insert
fruits.insert(1, "orange")
print(fruits)  # ['apple', 'orange', 'banana', 'cherry', ['date', 'elderberry']]

# Extend - Adds each element of an iterable (like a list or tuple) to the list individually.
fruits.extend(["grape", "melon"])
print(fruits)  # ['apple', 'orange', 'banana', 'cherry', ['date', 'elderberry'], 'grape', 'melon']
```

---

### ➖ Removing Elements - remove(), pop(index), clear()

```python
# Remove by value - Removes the first matching element found in the list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry']

# Pop by index
removed_element = fruits.pop(1)
print(removed_element)  # cherry
print(fruits)   # ['apple']

# Clear the entire list
fruits.clear()
print(fruits)  # []
```

---

### 🔄 Sorting and Reversing

```python
numbers = [4, 1, 8, 3]

# Sort ascending
numbers.sort()
print(numbers)  # [1, 3, 4, 8]

# Sort descending
numbers.sort(reverse=True)
print(numbers)  # [8, 4, 3, 1]

# Reverse
numbers.reverse()
print(numbers)  # [1, 3, 4, 8]
```

---

### 🔁 More Methods and Examples

```python
colors = ["red", "green", "blue", "green"]

# index()
print(colors.index("green"))  # 1

# count()
print(colors.count("green"))  # 2

# copy()
copy_colors = colors.copy()
print(copy_colors)  # ['red', 'green', 'blue', 'green']
```

---

## ✅ Key List Methods and Functions

| Function / Method       | Description                                               |
|-------------------------|-----------------------------------------------------------|
| `len(list)`             | Returns the number of elements in the list                |
| `append(x)`             | Adds `x` to the end of the list                           |
| `extend(iterable)`      | Adds all elements from `iterable` to the end              |
| `insert(i, x)`          | Inserts `x` at position `i`                               |
| `remove(x)`             | Removes the **first occurrence** of `x`                   |
| `pop([i])`              | Removes and returns element at index `i` (last if omitted)|
| `clear()`               | Removes all elements from the list                        |
| `index(x)`              | Returns index of the first occurrence of `x`              |
| `count(x)`              | Counts how many times `x` appears in the list             |
| `sort()`                | Sorts the list in ascending order (in-place)              |
| `reverse()`             | Reverses the order of the list (in-place)                 |



## 🧠 Summary

- Lists are flexible containers for storing multiple items in Python.  
- They are mutable, indexable, and support many built-in methods.  
- Lists can contain different data types – even other lists!
