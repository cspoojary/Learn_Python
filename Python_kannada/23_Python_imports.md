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
