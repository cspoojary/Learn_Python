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
## 4. Recursion
Recursion occurs when a function calls itself. It's used to solve problems that can be broken down into smaller, similar problems.

Example: Recursive function to calculate factorial
```Python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```
Output:
```Python
120
```
Here are the sections for Nested Functions and Local/Global Variables:

---
## 5. Nested Functions
A nested function is a function defined inside another function. The inner function is only accessible within the outer function, allowing for more modular and controlled code execution.

Example: Nested function in Python
```Python
def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()

outer_function("Anand")
```
Output:
```Python
Hello, Anand!
```
In this example, the inner_function() is called within outer_function() and uses the name parameter of the outer function.








