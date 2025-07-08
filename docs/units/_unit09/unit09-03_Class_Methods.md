---
title: LM | Class Methods
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "Object-oriented programming concept"
  caption: "Image concept and AI prompt: Spaska Forteva — Generated with ChatGPT/DALL·E"
---


A **method** is a function that is defined inside a class and operates on objects (instances) of that class.  

Methods allow your objects to perform actions or return information based on their attributes.

## Syntax

```python
class ClassName:
    .
    .
    .
    def method_name(self, other_parameters):
        # code block

```

### Important points

The first parameter of every instance method must be self.
self refers to the current object (instance) calling the method.
You can access and modify attributes inside a method using self.attribute_name.


## Example

```python
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I am {self.age} years old.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age}.")

    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} is an adult.")
        else:
            print(f"{self.name} is not an adult yet.")
```

### Usage

```python
person1 = Human("Liam", 17)

person1.introduce()
person1.is_adult()

person1.celebrate_birthday()
person1.is_adult()
```

### Output

- Hi, I'm Liam and I am 17 years old.
- Liam is not an adult yet.
- Happy Birthday, Liam! You are now 18.
- Liam is an adult.


## Example: Vehicle

Let's add another example with a Vehicle class that includes a method to calculate the vehicle's age.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_info(self):
        print(f"This is a {self.brand} vehicle.")

    def calculate_age(self, build_year):
        current_year = 2025
        age = current_year - build_year
        print(f"The {self.brand} vehicle is {age} years old.")
```

### Usage

```python
my_vehicle = Vehicle("Toyota")

my_vehicle.show_info()
my_vehicle.calculate_age(2018)
```

### Output

- This is a Toyota vehicle.
- The Toyota vehicle is 7 years old.


## Summary

- Methods define what an object can do.

- Always include self as the first parameter.

- You can access or update object attributes inside methods using self.attribute.