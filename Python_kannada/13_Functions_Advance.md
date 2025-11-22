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
## 2. Variable-Length Arguments
You can use *args and **kwargs to accept a variable number of arguments in a function.
Example: Using *args
```Python
def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total_sum(1, 2, 3, 4))
```
Output:
```Python
10
```
Example: Using **kwargs
```Python
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Anand", age=22, course="Python")
```
Output:
```Python
name: Anand
age: 22
course: Python
```
---
## 3. Lambda Functions
A lambda function is a small anonymous function that can take any number of arguments but has only one expression.

Syntax:
```Python
lambda arguments: expression
```
Example: Lambda function to double a number
```Python
double = lambda x: x * 2
print(double(5))
```
Output:
```Python
10
```
----












