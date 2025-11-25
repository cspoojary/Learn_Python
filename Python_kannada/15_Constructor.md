# Constructors and the self Keyword
## 1. The __init__() Constructor
- Constructor: The __init__() method in Python is a special method that initializes an object when it’s created. It’s called automatically when you create a new instance of a class.
- Purpose: It allows you to set the initial state of the object by defining its attributes.
Syntax:
```Python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
```
Here, __init__() receives parameters and sets the initial values of object attributes.

---
## 2. Using self in Class Methods
- self: Refers to the instance of the class itself, allowing you to access attributes and methods within a class.
    - It is automatically passed as the first argument to methods within the class.
    - Note: While self is a convention, you can technically use any name (though it's not recommended for readability).
Example:
```Python
class Person:
    def __init__(self, name, age):
        self.name = name  # 'self.name' is an instance variable
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating an object
person1 = Person("Arjun", 22)
person1.introduce()
```
Output:
```Python
My name is Arjun and I am 22 years old.
```
Here:
- self.name and self.age are instance variables.
- introduce() is a method that accesses the instance variables using self.

---
