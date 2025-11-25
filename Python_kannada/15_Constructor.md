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
