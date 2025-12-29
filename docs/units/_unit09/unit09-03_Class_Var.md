---
title: LM | Instance variables vs. class variables
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "Object-oriented programming concept: class variables"
  caption: "Conceptual illustration for educational purposes."
---

In object-oriented programming, data can belong either to  
**a single object** or to **the class itself**.

Understanding this difference is essential for writing **logical and well-structured programs**.

---


## Instance variables

Instance variables store data that belongs to **one specific object**.

They are defined inside the constructor (`__init__`) using `self`.

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Each object has its **own copy** of these variables.

Example:
- one animal has the name `"Lion"`
- another animal has the name `"Penguin"`

---

## Class variables

Class variables store data that belongs to **the class as a whole**,  
not to individual objects.

They are defined **inside the class**, but **outside all methods**.

```python
class Animal:
    animal_regions = [
        ["Lion", "Africa"],
        ["Elephant", "Africa"],
        ["Polar Bear", "Arctic"]
    ]
```

This data exists **only once** and is shared by all objects of the class.

---

## When should we use class variables?

Use a class variable when:

- the data is the same for all objects
- the data represents general or shared knowledge
- the data should not change per object

In our example:
- the region of a lion does not depend on a specific lion object
- it is shared world knowledge
- therefore, it belongs to the class

---

## Accessing class variables

Class variables can be accessed in two ways:

```python
Animal.animal_regions
```

or

```python
self.animal_regions
```

---

## Recommended access style

For learning and clarity, it is recommended to access class variables using the **class name**:

```python
Animal.animal_regions
```

This makes it explicit that the data belongs to the class, not to the instance.

---


## Why not store this data as an instance variable?

If `animal_regions` were an instance variable:

- every object would store its own copy
- memory usage would increase
- program logic would be unclear

Class variables avoid duplication and improve structure.

## Key takeaway

- Instance variables belong to individual objects (`self`)
- Class variables belong to the class itself
- Class variables are defined outside methods
- They are shared by all objects
- Use them for shared or global knowledge

Understanding class variables is a key step toward  
**clean and logical object-oriented programming**.
