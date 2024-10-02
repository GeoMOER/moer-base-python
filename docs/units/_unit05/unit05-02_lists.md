---
title: "Lists"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "neon data"
  caption: "Photo by [Franki Chamaki](https://unsplash.com/@franki?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) [from unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)"
---

<!--more-->
## Object Type Lists
Lists in Python are versatile objects that allow you to store multiple items in a single variable. They are one of the most commonly used data structures in Python due to their flexibility. A list can contain elements of different data types, including numbers, strings, functions, and even other lists. This makes lists ideal for grouping related items together and managing collections of data.

## What Are Lists Used For?
Lists are used for a wide variety of tasks in Python programming, such as:

- Storing Collections of Data: Lists can hold multiple items, making them useful for storing sequences of data like names, numbers, or other collections.
- Organizing Data: You can organize data into lists to perform operations like sorting, filtering, or iterating through items.
- Complex Data Structures: Lists can be nested within other lists, allowing you to create complex data structures like matrices or trees.
- Dynamic : Lists can grow or shrink in size, as you can add, remove, or modify elements at any time.

## Creating and Accessing Lists
A list is typically created using square brackets `[]`, with elements separated by commas. Here's an example:
```python

# Create a list
names = ["Maria", "Evi", "Simon", "Peter"]
numbers = [44,34,5,6]

# Creating a list with multiple elements
mlist = [[2, 5, 3], 21.3, 'Artur']
```
In this example, `mlist` contains a sublist `[2, 5, 3]`, a floating-point number `21.3`, and an name.

## List Methods in Python

### Access the elements in the list
You can access list elements using square brackets `[]`. Using single square brackets returns the element while preserving its structure as a list. To access the value inside, you again use `[]` to access the values

```python
# Accessing elements
print(list1[0])  # Output: [2, 5, 3]
print(list1[1])  # Output: 21.3
print(list1[2])  # Output: <built-in function sum>

# Accessing elements within a sublist
print(list1[0][1])  # Output: 5
```

### Modifying
Lists in Python are mutable, meaning you can change their contents after they are created. Here are some examples of modifying lists:

```python
# Modifying an element in the list
list1[1] = 42.0
print(list1)  # Output: [[2, 5, 3], 42.0, <built-in function sum>]
```

### Adding
```python
list1.append("new item")
print(list1)  # Output: [[2, 5, 3], 42.0, <built-in function sum>, 'new item']
```
## Removing an element from the list
```python
list1.remove(42.0)
print(list1)  # Output: [[2, 5, 3], <built-in function sum>, 'new item']

## List Methods in Python

### Common List Methods

- **append(x)**: Adds an item `x` to the end of the list.
- **extend(iterable)**: Extends the list by appending elements from the iterable.
- **insert(i, x)**: Inserts an item `x` at a given position `i`.
- **remove(x)**: Removes the first item from the list whose value is equal to `x`.
- **pop([i])**: Removes and returns the item at the given position `i` in the list. If no index is specified, `pop()` removes and returns the last item in the list.
- **clear()**: Removes all items from the list.
- **index(x[, start[, end]])**: Returns the index of the first item whose value is equal to `x`. Raises a `ValueError` if not found.
- **count(x)**: Returns the number of times `x` appears in the list.
- **sort(key=None, reverse=False)**: Sorts the items of the list in place (the arguments can be used for sort order).
- **reverse()**: Reverses the elements of the list in place.
- **copy()**: Returns a shallow copy of the list.

## List Methods in Python

| Method               | Description                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------|
| `append(x)`          | Adds an item `x` to the end of the list.                                                      |
| `extend(iterable)`   | Extends the list by appending elements from the iterable.                                      |
| `insert(i, x)`       | Inserts an item `x` at a given position `i`.                                                  |
| `remove(x)`          | Removes the first item from the list whose value is equal to `x`.                              |
| `pop([i])`           | Removes and returns the item at the given position `i`. If no index is specified, it removes and returns the last item. |
| `clear()`            | Removes all items from the list.                                                                |
| `index(x[, start[, end]])` | Returns the index of the first item whose value is equal to `x`. Raises a `ValueError` if not found. |
| `count(x)`           | Returns the number of times `x` appears in the list.                                         |
| `sort(key=None, reverse=False)` | Sorts the items of the list in place.                                           |
| `reverse()`          | Reverses the elements of the list in place.                                                   |
| `copy()`             | Returns a shallow copy of the list.                                                           |


```