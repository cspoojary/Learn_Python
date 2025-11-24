# Introduction to OOP Concepts & Classes/Objects
In this video, we will begin our journey into Object-Oriented Programming (OOP) with the foundational concepts of classes and objects.

---
## 1. What is Object-Oriented Programming (OOP)?
- OOP is a programming paradigm that organizes software design around data, or objects, rather than functions and logic.
- It allows for better modularity and code reusability by creating objects that model real-world entities.
- Procedural vs Object-Oriented Programming:
Procedural Programming: Based on functions, where the main focus is on performing actions.
    - Example: Writing multiple functions to process data.
- Object-Oriented Programming: Based on objects and classes. The main focus is on objects (data) and the methods (functions) that manipulate this data.

---

## 2. Classes and Objects
Class:
A class is a blueprint for creating objects. It defines the attributes and behaviors of the objects created from it.

Object:
An object is an instance of a class. Each object has its own attributes (data) and can perform actions through methods (functions).

Example:
```Python
class Car:
    # Attributes
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable

    # Method
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating an object of the class
my_car = Car("Toyota", "Corolla")
my_car.display_info()
```
Output:
```Python
Car Brand: Toyota, Model: Corolla
```
Here:
- Car is the class.
- my_car is an object of the Car class.
- brand and model are attributes of the object.
- display_info() is a method that displays the car's details.
