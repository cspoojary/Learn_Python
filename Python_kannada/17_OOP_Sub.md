# Getters, Setters, Method Overloading & Overriding, super(), Abstract Classes

## 1. Getters and Setters
- Definition: Getters and setters are methods that allow controlled access to an object's attributes.
- Purpose: They help in validating data, protecting data from accidental modification, and providing controlled access.

#### Example
```Python
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # Private attribute

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Validation
            self.__age = age
        else:
            print("Invalid age")

# Usage
student = Student("Anita", 20)
print("Age:", student.get_age())  # Accessing age with getter
student.set_age(21)  # Modifying age with setter
print("Updated Age:", student.get_age())
```
Output :
```Python
Age: 20
Updated Age: 21
```
Here:
- get_age() provides read-only access to __age, while set_age() enables controlled modification.

---
## 2. Method Overloading
- Definition: Method overloading is the ability to define multiple methods with the same name but different parameters.
- Note: Python doesn’t support method overloading directly, but we can achieve it by using default parameters or by handling varying numbers of arguments with *args or **kwargs.

Example:
```Python
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c  # Handles both 2 and 3 parameter cases

# Usage
math = MathOperations()
print(math.add(5, 10))     # Two arguments
print(math.add(5, 10, 15)) # Three arguments
```
Output: 
```Python
15
30
```
Here:
- The method add can accept either two or three arguments, handling both cases within the same method.
