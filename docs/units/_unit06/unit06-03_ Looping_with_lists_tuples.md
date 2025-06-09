---
title: LM | FOR Loop in lists
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u07/header.png
  image_description: "loop"
  caption: "Photo by [Christopher Kuszajewski](https://pixabay.com)"
---

## 📋 Why Use For-Loops with Lists?

For-loops are extremely useful when working with **lists**, because they allow you to access each element in a structured and readable way. Unlike `range()`-based loops that use index numbers, direct iteration is often simpler and less error-prone.

---

## 🔁 Looping Through a List

You can loop directly over the elements of a list:

```python
letters = ["A", "B", "C", "D"]
for element in letters:
    print(element)
```

### Output:
```
A
B
C
D
```

Each item in the list `letters` is accessed one by one using the loop variable `element`.

---

## ✏️ Modify List Elements by Index

To change list elements, you need to access them by index. You can use `range(len(...))` to loop through the indexes:

```python
letters = ["A", "B", "C", "D"]
for i in range(len(letters)):
    letters[i] = letters[i] + "x"
print(letters)
```

### Output:
```
['Ax', 'Bx', 'Cx', 'Dx']
```

---

## 🆕 Creating a New List from an Existing One

If you want to create a new list based on modifications of another list:

```python
a = ["A", "B", "C", "A", "B", "A", "A"]
test = []  # this is an empty list

for i in range(len(a)):
    test.append(a[i].lower())

print(test)
```

### Output:
```
['a', 'b', 'c', 'a', 'b', 'a', 'a']
```

---

## ✅ Summary

- Use `for element in list` for clean and direct access to each value.
- Use `for i in range(len(list))` if you need to modify items by index.
- Lists are mutable, meaning their content can be changed.
