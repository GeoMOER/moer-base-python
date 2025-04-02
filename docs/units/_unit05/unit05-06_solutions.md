---
title: "Python Exercise - Solution 1"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u02/header.png
  image_description: "thinking"
  caption: "Image by [username](https://pixabay.com) from pixabay"
---

# Introduction

This unit covers Python loops, focusing on `for` loops. You will practice using loops to solve various tasks that involve iterating through ranges and lists.

## Task 1: Even and Odd Numbers

### Solution:
```python
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```
---

## Task 2: Sum of Even Numbers

### Solution:
```python
even_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
print(f"Sum of even numbers from 1 to 100 is {even_sum}")

```
---

## Task 3: D3TD5T

### Solution:
```python
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: D3TD5T")
    elif i % 3 == 0:
        print(f"{i}: D3T")
    elif i % 5 == 0:
        print(f"{i}: D5T")
    else:
        print(i)
```
---

## Task 4: Find a Friend

### Solution:
```python
friends = ["Anna", "Ben", "Clara", "David", "Eva"]
search_friend = "Clara"
for friend in friends:
    if friend == search_friend:
        print(f"{search_friend} found!")
        break
```
---

## Task 5: Replace a Character in a List of Fruits

### Solution:
```python
fruits = ["apple", "banana", "cherry"]
modified_fruits = [fruit.replace("a", "o") for fruit in fruits]
print(modified_fruits)

```
---

## Task 6: Modify a List of Friends

### Solution:
```python
friends = ["Anna", "Ben", "Clara", "David", "Eva"]

# Replace 'Anna' with 'Bella'
friends[0] = "Bella"

# Remove 'Ben' and add 'Felix' at position 2
for i, friend in enumerate(friends):
    if friend == "Ben":
        friends.pop(i)
        friends.insert(2, "Felix")

print(friends)
```