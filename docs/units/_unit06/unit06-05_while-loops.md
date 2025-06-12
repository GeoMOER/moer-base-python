---
title: LM | While-Loops
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u07/header.png
  image_description: "loop"
  caption: "Photo by [Christopher Kuszajewski](https://pixabay.com)"
---

## 🔁 What is a While-Loop?

A `while`-loop is a control structure that repeats a block of code **as long as a condition is true**.

Use it when you **don’t know in advance** how many times something should repeat — it depends on when the condition becomes false.

---

## ▶️ Basic Example

```python
a = 7
b = 10

while a <= b:
    print(a)
    a += 1
```

### Output:
```
7
8
9
10
```

This loop prints values from `a` to `b`, stopping once `a > b`.

---

## ⚠️ Infinite Loops

If the loop condition never becomes `False`, the loop runs forever.

```python
a = 0
while a < 5:
    print("Still looping...")
# ❌ a is never changed, so the loop never ends!
```

✅ To avoid this, always make sure something inside the loop **changes the condition**.

---

## 🚨 Using `break` to Exit a Loop Early

Sometimes you want to stop a loop before the condition becomes false. Use `break` for that:

```python
a = 0
while a < 10:
    print(a)
    if a == 4:
        break
    a += 1
```

### Output:
```
0
1
2
3
4
```

The loop ends immediately when `a == 4` because of the `break`.

---

## ♾️ While True Loop (Controlled Inside)

You can create a loop that runs forever unless you manually stop it using `break`.

```python
count = 0
while True:
    print("Counting:", count)
    count += 1
    if count == 3:
        break
```

### Output:
```
Counting: 0
Counting: 1
Counting: 2
```

> `while True` is common in programs that wait for user input or conditions, and rely on `break` to stop.

---

## 🔢 Counting Backwards

You can also count down using a while-loop:

```python
i = 5
while i > 0:
    print(i)
    i -= 1
```

### Output:
```
5
4
3
2
1
```

---

## The continue Statement

With the continue statement we can stop the current iteration, and continue with the next:
```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
``` 

### Output:
```
1
2
4
5
6
```
## ✅ Summary

| Feature                 | While-Loop                     |
|-------------------------|--------------------------------|
| Repetition Count        | Unknown                        |
| Condition Placement     | Before each iteration          |
| Use Case                | Wait for condition to become false |
| Special Keywords        | `break`                        |
| Common Pattern          | `while True:` with internal stop |

Use while-loops when repetition depends on changing conditions, not a fixed number.
