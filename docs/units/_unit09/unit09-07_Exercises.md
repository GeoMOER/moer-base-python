---
title: EX | Exercises
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "Object-oriented programming concept"
  caption: "Image concept and AI prompt: Spaska Forteva – Generated with ChatGPT/DALL·E"
---

## Task

In this exercise, you will model an **animal** using object-oriented programming  
and determine its typical region and sleep behavior based on predefined data.

The goal is to understand how:
- objects use **internal data**
- methods make decisions
- shared data belongs to a **class**, not to individual objects

---

## Step 1: Create the class

Create a class named `Animal`.

---

## Step 2: Define the attributes

Each animal object should have:

- `name` — the name of the animal  
- `age` — the age of the animal  

These values are specific to each object.

---

## Step 3: Define shared data (class variables)

Inside the class, define **two class-level data structures**.

### Animal regions

```python
animal_regions = [
    ["Lion", "Africa"],
    ["Elephant", "Africa"],
    ["Polar Bear", "Arctic"],
    ["Penguin", "Antarctica"],
    ["Kangaroo", "Australia"]
]
```

### Animal sleep duration

Define a second list that stores **how long an animal typically sleeps per day**  
(in hours).

```python
animal_sleep = [
    ["Lion", 20],
    ["Elephant", 4],
    ["Polar Bear", 8],
    ["Penguin", 12],
    ["Kangaroo", 15]
]
```

Both lists represent **shared knowledge**:
- they belong to the class
- all objects can access them
- they should not be passed as parameters

---

## Step 4: Define the methods

### `region()`

- This method takes **no parameters** (except `self`)
- It uses `self.name` to look up the animal in `animal_regions`
- It prints the corresponding region
- If the animal is not found, it prints a default message

---

### `sleep()`

- This method takes **no parameters** (except `self`)
- It uses `self.name` to look up the animal in `animal_sleep`
- It prints how many hours the animal typically sleeps per day
- If the animal is not found, it prints a default message

Example output:
- `"The lion sleeps about 20 hours per day."`
- `"Sleep information for this animal is unknown."`

---

## Step 5: Constructor

Define a constructor (`__init__`) that initializes:

- `name`
- `age`

Use `self` to store these values.

---

## Step 6: Create and test objects

- Create one or more animals
- Call `region()` and `sleep()`
- Observe how both methods determine information automatically  
  based on class-level data

---

## Example structure (no full solution)

```python
class Animal:
    animal_regions = [
        ["Lion", "Africa"],
        ["Polar Bear", "Arctic"]
    ]

    animal_sleep = [
        ["Lion", 20],
        ["Polar Bear", 8]
    ]

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def region(self):
        # search for self.name in animal_regions
        pass

    def sleep(self):
        # search for self.name in animal_sleep
        pass
```

---

## Hint

- Use a loop to search through the lists
- Compare the stored name with `self.name`
- Do not add parameters to `region()` or `sleep()`
- Focus on clarity and logical structure

This exercise demonstrates how **multiple class variables**  
can be used to describe different aspects of object behavior.
