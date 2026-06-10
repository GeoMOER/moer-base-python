---
title: A | Assignment
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "Object-oriented programming concept"
  caption: "Image concept and AI prompt: Spaska Forteva — Generated with ChatGPT/DALL·E"
---

Please save your solutions for Exercises 1 to 3 in a Python script named  
`unit09__ex(1-3)_code.py`.

Save the script in the `unit09` folder, compress the folder into a `.zip` file,  
and upload it to ILIAS.

Submission guidelines:  
https://geomoer.github.io/moer-base-python/unit00/unit00-04_submission_guidelines.html

Make sure your code is clearly structured and includes **meaningful comments**.

---

## Tasks

### 🔥 Base class `Animal`

Please use the `Animal` class from **Unit 09**, including:

- instance variables: `name`, `age`
- class variables for:
  - regions
  - sleep duration
- methods:
  - `region()`
  - `sleep()`

You may reuse or slightly adapt your solution from the exercises.

---

## 1️⃣ Subclass `Bird`

Create a subclass named `Bird` that **inherits from `Animal`**.

### Requirements

- Use `super()` to initialize `name` and `age`.
- Define a **class variable** named `bird_flight_heights`  
  that stores bird names and their typical flying height (in meters).

```python
bird_flight_heights = [
    ["Eagle", 3000],
    ["Parrot", 100],
    ["Penguin", 0]
]
```

### Method: `fly()`

- This method takes **no parameters** (except `self`).
- It uses `self.name` to look up the flying height in the class variable.
- It prints a message such as:
  - `"Eagle can fly up to 3000 meters high."`
- If the bird is not found, print a default message.

---

## 2️⃣ Subclass `Reptile`

Create another subclass named `Reptile` that also **inherits from `Animal`**.

### Requirements

- Use `super()` to initialize `name` and `age`.
- Define a **class variable** named `reptile_lengths`  
  that stores reptile names and their typical length (in meters).

```python
reptile_lengths = [
    ["Python", 6],
    ["Lizard", 0.3],
    ["Crocodile", 5]
]
```

### Method: `crawl()`

- Prints a descriptive message about how the reptile moves.

### Method: `length()`

- Uses `self.name` to look up the reptile length.
- Prints a message such as:
  - `"Python is about 6 meters long."`
- Prints a default message if the reptile is not found.

---

## 3️⃣ Demonstration and testing

In your script:

- Create **at least one object** of each class:
  - `Animal`
  - `Bird`
  - `Reptile`
- Call **all available methods** for each object:
  - inherited methods
  - subclass-specific methods

---

## Instructions

- Use **class variables** for shared knowledge.
- Do **not** pass lists as method parameters.
- Access class variables via the **class name**, not via `self`.
- Use `super()` correctly.
- Keep your code readable and well-commented.

---

## ⭐ Extra Challenge (optional)

Choose **one** of the following:

- Add another subclass (e.g. `Mammal` or `Fish`)
- Replace one list with a **dictionary** and explain why it is better
- Add a method that combines information  
  (e.g. region + sleep duration in one output)

---

## Evaluation focus

Your submission will be evaluated based on:

- correct use of inheritance
- correct use of class variables
- clean and logical structure
- readable output and comments

This assignment tests your understanding of **object-oriented thinking**,  
not just Python syntax.
