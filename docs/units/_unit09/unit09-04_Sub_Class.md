---
title: LM | Inheritance
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "Object-oriented programming concept"
  caption: "Image concept and AI prompt: Spaska Forteva — Generated with ChatGPT/DALL·E"
---

# Inheritance

**Inheritance** is a powerful concept in object-oriented programming that allows a new class (called a *child class* or *subclass*) to inherit attributes and methods from an existing class (called a *parent class* or *base class*).  

With inheritance, you can create a hierarchy of classes that share common functionality, and you can add or override behaviors in child classes.

## Example: Vehicle, Car, and Truck
{% include figure image_path="/assets/images/unit_images/u09/vehicle.png" %}

_Image concept and AI prompt: Spaska Forteva — Generated with ChatGPT/DALL·E_
Let's start with a general `Vehicle` class, and then create two subclasses: `Car` and `Truck`.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print(f"The {self.brand} vehicle is moving.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine has started.")

class Truck(Vehicle):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

    def load_cargo(self):
        print(f"The {self.brand} truck is loading {self.capacity} tons of cargo.")
```

### Usage

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



### Summary

- Inheritance allows you to reuse code and create logical relationships between classes.
- Use super() to call the parent class's constructor or methods.
- Child classes can add new behaviors or override existing ones.