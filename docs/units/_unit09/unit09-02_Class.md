---
title: LM | Class
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "Object-oriented programming concept"
  caption: "Image concept and AI prompt: Spaska Forteva – Generated with ChatGPT/DALL·E"
---

# What is a Class?

A **class** is like a blueprint for creating objects. It defines a set of attributes (characteristics) and methods (actions) that its objects (instances) will have.

## Example
{% include figure image_path="/assets/images/unit_images/u09/person.png" %}


Let’s take the example of a **human**.

A human object has:
- a name
- two legs

It also has methods (actions) such as:
- walk
- work
- rest

## What is a constructor?

A **constructor** is a special method used to initialize (set up) an object's attributes when it is created. In Python, this method is always named `__init__`. The double underscores before and after (`__`) indicate that it is a special or "magic" method.

### Rules for defining a constructor
- It is defined using `def __init__(self, ...)`.
- The first parameter is always `self`, which refers to the current object instance.
- Attributes are usually set inside the constructor using `self.attribute_name = value`.

### Why do we use `self` and underscores?
- `self` is a reference to the current object, allowing each instance to have its own independent data.
- The underscores in `__init__` signal that it is a built-in special method in Python.

## Python code example

```python
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create an object
person1 = Human("Anna", 30)

# Call methods
print(person1.name)
print(person1.age)

```


### Why do we need self in the constructor? Can we do it without?

No — in Python, we need self in the constructor (and in all instance methods).

#### Detailed explanation

When you create an object (for example: person1 = Human("Anna", 30)), Python internally calls the constructor like this:

```python
Human.__init__(person1, "Anna", 30)
```

Here, person1 is automatically passed as the first argument to the method.

The self parameter represents the current instance of the class. It allows you to store or access data specific to that object.

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

If you wrote:
```python
def __init__(name, age):
    name = name
    age = age
    
```

Python would not know which object to store these values in.

name = name only assigns the parameter name to itself (which does nothing), and does not save it inside the object.

Without self, there is no link to the object being created.

### Conclusion

✅ We must use self so that each instance has its own separate data (attributes), and so that methods can access and modify these attributes correctly.