# Functions - Advanced Concepts
In this part, we'll explore more advanced function concepts, including recursion, lambda functions, and variable-length arguments.

---

## 1. Keyword Arguments
With keyword arguments, you can pass values to a function by specifying the parameter names.
```Python
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Kumar")
```
Output:
```Python
Name: Kumar, Age: 25
```
---
