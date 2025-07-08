---
title: LM | FOR Loop in range()
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u06/header.png
  image_description: "loop"
  caption: "Photo by [Christopher Kuszajewski](https://pixabay.com)"
---


## 🔁 What are For-Loops?

For-loops are a core structure in Python that repeat a block of code multiple times. They are ideal when the number of repetitions is **known in advance**. In Python, the most common way to repeat something a fixed number of times is by using the `range()` function.

---

## ▶️ Basic Example

```python
for i in range(5):
    print(i)
```

### Output:
```
0
1
2
3
4
```

You can use `range(start, stop)` to repeat something from a starting number up to, but not including, a stopping number:

```python
for i in range(7, 11):
    print(i)
```

### Output:
```
7
8
9
10
```

> 🧠 `range(7, 11)` includes 7 but excludes 11. 

The variable `i` is updated automatically in each step. You should **not change it** inside the loop body.

---

## 🪜 Stepping Through the Range

You can also define a **step size** with `range(start, stop, step)`.

### Example 1: Every second number

```python
for i in range(0, 10, 2):
    print(i)
```

### Output:
```
0
2
4
6
8
```
### Example 1: Check for even numbers
 
 ```python
 for i in range(6):
    if i % 2 == 0:
        print(i, "is even")
> 📌 The loop starts at 0 and goes up in steps of 2, stopping before 10.

---

## ⬇️ Counting Down

If you want to count **backwards**, use a **negative step**:

```python
for i in range(5, 0, -1):
    print(i)
```

### Output:
```
5
4
3
2
1
```

> ❗ Make sure that the `start` is greater than the `stop` when using a negative step.

---

## 🔚 Summary

- `range(n)` loops from 0 to n-1.
- `range(start, stop)` loops from `start` to `stop - 1`.
- `range(start, stop, step)` controls how much the number increases (or decreases).
- You can loop forwards or backwards using `range()`.

These loops are very useful when you want to do something a specific number of times or when working with positions like indexes in a list.
