---
title: "Overview"
toc: TRUE
toc_float: TRUE
---

## 🧭 Overview of Loops in Python

In Python, loops allow you to execute a block of code repeatedly. The two main types are **for-loops** and **while-loops**. Knowing which loop to choose depends on the task and whether you know how many repetitions are needed.

---

## 🔁 For-Loops

A **for-loop** is used when you know beforehand how many times the loop should run, usually based on an iterable like a list, tuple, string, or a range of numbers.


### Common Use Cases
- Running a fixed number of repetitions with `range()`
- Iterating over a list or string

---

## 🔄 While-Loops

A **while-loop** runs as long as a specified condition is true. It's useful when you don't know how many iterations you’ll need.



### Common Use Cases
- Waiting for user input
- Looping until a stop condition is met
- Reading data until the end of a file


---

## 🔍 Comparison Table

| Feature           | For-Loop                        | While-Loop                           |
|-------------------|----------------------------------|--------------------------------------|
| Repetition Count  | Known                           | Unknown                              |
| Control Variable  | Automatic via iterable          | Manually updated                     |
| Best For          | Lists, ranges, sequences        | Conditions that evolve over time     |
| Risk              | Low – typically ends naturally  | High – may run forever if not stopped |
| Exit Strategy     | Automatic at end of iterable    | Manual condition must become False   |

> ⚠️ **Important:** With while-loops, the risk of an infinite loop is higher if you forget to update the condition. Always make sure the loop has a clear exit strategy!

---

## ✅ Tips for Using Loops

- Always make sure your `while` loop has a clear exit condition.
- When using `for`, consider whether you need the index (`for i in range(len(list))`) or just the value (`for item in list`).
- Use `break` to exit a loop early, and `continue` to skip to the next iteration.

---

