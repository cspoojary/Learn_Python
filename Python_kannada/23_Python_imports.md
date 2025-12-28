# Python Imports, Libraries, Modules, and Packages
Understanding these concepts helps you reuse code, organize projects, and use external tools easily — just like importing ingredients while cooking!
## 🧱 What is a Module in Python?
- A module is simply a .py file containing functions, classes, or variables.
- We can import it and use its code in another file.
### 📘 Example: math module (built-in)
```Python
import math
print(math.sqrt(25))  # Output: 5.0
```
##### math is a built-in module. We can use its functions like sqrt(), pow(), etc.

## 🔧 Creating Your Own Module
Let’s say we have a file greetings.py:
```Python
# greetings.py
def namaskara(name):
    print(f"Namaskara {name}!")

def goodbye(name):
    print(f"Goodbye {name}!")
```
Now use it in another file:
```Python
# main.py
import greetings

greetings.namaskara("Ravi")
greetings.goodbye("Meena")
```
✅ This helps split large projects into reusable smaller files.
## 📥 import Variations
| Syntax                     | Use Case                                                                 |
|----------------------------|--------------------------------------------------------------------------|
| `import module`            | General import – use like `module.function()`                             |
| `import module as alias`   | Shorten name, e.g., `import numpy as np`                                  |
| `from module import function` | Import a specific function only                                        |
| `from module import *`     | Imports everything (**❗ Avoid in large projects**)                       |
### 🔹 Example:
```Python
from math import sqrt
print(sqrt(36))  # No need to write math.sqrt()
```
## 📦 What is a Package?
- A package is a folder containing multiple modules and an optional __init__.py file.
- Helps organize large projects into folders.
