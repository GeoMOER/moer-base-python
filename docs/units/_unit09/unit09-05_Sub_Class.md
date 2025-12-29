---
title: LM | Inheritance in Object-Oriented Programming
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "Object-oriented programming concept: inheritance"
  caption: "Image concept and AI prompt: Spaska Forteva — Generated with ChatGPT/DALL·E"
---

**Inheritance** is a fundamental concept in object-oriented programming (OOP).  
It allows one class to **inherit attributes and methods** from another class.

- The existing class is called the **parent class** (or *base class*).
- The new class is called the **child class** (or *subclass*).

Inheritance models an **“is-a” relationship**:

> A *Car* **is a** *Vehicle*  
> A *Truck* **is a** *Vehicle*

---

## Why do we use inheritance?

Inheritance helps to:

- avoid code duplication  
- reuse existing functionality  
- create logical class hierarchies  
- extend behavior in a controlled and structured way  

Common functionality is placed in a parent class and reused by child classes.

---

## How inheritance is defined in Python

In Python, inheritance is defined by **passing the parent class name in parentheses**:

```python
class ChildClass(ParentClass):
    pass
```

This tells Python that `ChildClass` inherits all public attributes and methods from `ParentClass`.

---

## Example: Vehicle, Car, and Truck
{% include figure image_path="/assets/images/unit_images/u09/vehicle.png" %}

We start with a general **base class** called `Vehicle`.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print(f"The {self.brand} vehicle is moving.")
```

The `Vehicle` class defines:
- a shared attribute: `brand`
- a shared method: `move()`

---

## Child class: Car

The `Car` class inherits from `Vehicle` and adds its own attributes and behavior.

```python
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine has started.")
```

Important points:
- `class Car(Vehicle)` defines inheritance
- `super().__init__(brand)` calls the parent constructor
- `Car` automatically inherits `brand` and `move()`

---

## Child class: Truck

```python
class Truck(Vehicle):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

    def load_cargo(self):
        print(f"The {self.brand} truck is loading {self.capacity} tons of cargo.")
```

Both `Car` and `Truck` reuse functionality from `Vehicle` and extend it with specialized behavior.

---

## Why is `super()` important?

The `super()` function allows a child class to access methods from its parent class.

In constructors, `super()` ensures that:
- shared attributes are initialized correctly
- parent logic is reused
- code duplication is avoided

Without `super()`, parent logic would need to be rewritten manually.

---

## Using inherited classes

```python
my_car = Car("Toyota", "Corolla")
my_truck = Truck("Mercedes", 10)

my_car.move()
my_car.start_engine()

my_truck.move()
my_truck.load_cargo()
```

### Output

- The Toyota vehicle is moving.
- The Toyota Corolla's engine has started.
- The Mercedes vehicle is moving.
- The Mercedes truck is loading 10 tons of cargo.

---

## Key concept: Method inheritance

Even though `Car` and `Truck` do not define `move()` themselves,  
they can still use it because it is inherited from `Vehicle`.

---

## Summary

- Inheritance creates an **is-a relationship** between classes
- Child classes inherit attributes and methods from parent classes
- In Python, inheritance is defined using `class Child(Parent)`
- `super()` is used to access parent class methods
- Inheritance improves code reuse, structure, and clarity
