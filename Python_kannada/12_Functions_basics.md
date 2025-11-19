## Python Functions Basics
### 1. Basics of Functions
A function is a reusable block of code that performs a specific task when called. Functions are useful to organize code, make it reusable, and reduce redundancy.

### 2. Defining a Function
You define a function using the def keyword followed by the function name, parentheses, and a colon : .
#### Syntax
```Python
def function_name(parameters):
# Block of code
```
#### Basic function to greet a user
```Python
def greet():
print("Hello! Welcome to the Python course.")

greet()

#Output : Hello! Welcome to the Python course.
```
### 3. Function Parameters
Parameters are variables used to pass data into a function.
#### Function with a parameter
```Python
def greet_user(name):
print(f"Hello, {name}! Welcome to the Python course.")

greet_user("Anand")

Output: Hello, Anand! Welcome to the Python course.
```
