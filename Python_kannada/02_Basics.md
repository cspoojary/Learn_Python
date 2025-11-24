# Python Basics 
### TOKENS
- Keywords
- Identifiers
- Literals
- Operators
- Punctuators / Delimiters
- Comments
- 
## Variable
- Variables are containers for storing data values.  
- creating a variable is as simple as assigning it a value. Python is dynamically typed, so you don't need to declare the type. The variable is created the moment you first assign a value to it.
- In Python, memory space is allocated automatically without the need for explicit declaration when a value is assigned to a variable. The assignment of values to variables is done using the equal sign (=).

###  Syntax:
```python
x = 5        # Assigning an integer value to the variable x
y = "Hello"  # Assigning a string value to the variable y
```

###  Rules for Naming Variables:
- Variable names can contain letters (a-z, A-Z), numbers (0-9), and underscores (_).
- Variable names must start with a letter or an underscore.
- Variable names are case-sensitive (Name and name are different).

### Example:
```python
age = 25
name = "John"
is_student = True
```
- Redeclaring Variables
    - You can redeclare a variable in Python by assigning a new value to it. This can even change the  variable's type, due to Python's dynamic typing.
    - Example
```Python
    x = 5
    x = "Sara"
    print(x)
```
- Assign Values to Multiple Variables
    - Python allows assigning values to multiple variables in one line, making your code concise and  readable.
    - Example
    ```Python
    a = b = c = 5
    print(a)
    print(b)
    print(c)
    ```
  - Output Variable
    - The Python print() function is often used to output variables.
    - when you try to combine a string and a number with the `+` operator, Python will give you an error.
```Python
x = "Python "
y = "is "
z = "awesome"

print(x + y + z)
```
**NOTE:**  The space character after `"Python "` and `"is "`, without them the result would be "Pythonisawesome".

- Global Variable
    Variables that are created outside of a function are known as global variables.
    
    - Create a variable outside of a function, and use it inside the function
```Python
    x = "awesome"
    def myfunc(): 
        print("Python is " + x)
    myfunc()
```
  - Create a variable inside a function, with the same name as the global variable
  ```Python  
    x = "awesome"
    def myfunc():
       x = "fantastic"  
       print("Python is " + x)
    myfunc()
    
    print("Python is " + x)
  ```
- To create a global variable inside a function, you can use the  global()  keyword.
  ```Python 
    x = "awesome"
    def myfunc():
      global x
      x = "fantastic"
    myfunc()
    print("Python is " + x)
  ```
---

## Data Types in Python
Common built-in types:
| Category        | Data Types                       |
|----------------|----------------------------------|
| Text Type       | str                              |
| Numeric Types   | int, float, complex              |
| Sequence Types  | list, tuple, range               |
| Mapping Type    | dict                             |
| Set Types       | set, frozenset                   |
| Boolean Type    | bool                             |
| Binary Types    | bytes, bytearray, memoryview     |
| None Type       | NoneType                         |


### Type Checking:
You can use the type() function to check the type of a variable.
```python
x = 10
print(type(x))  # Output: <class 'int'>
```

---

## Type Conversion
Python allows you to convert between data types using functions like int(), float(), str(), etc.

### Example:
```python
x = "10"  # x is a string
y = int(x)  # Convert string to integer
z = float(y)  # Convert integer to float
print(z)  # Output: 10.0
```
---

## Assigning Values to Multiple Variables
Python allows you to assign values to multiple variables in a single line.
```python
x, y, z = 10, 20, 30
print(x, y, z)
```

Or You can also assign the same value to multiple variables in one line:
```python
x = y = z = 100
print(x, y, z)
```

---

## Variable Reassignment
You can change the value of a variable at any point in your program.
Example:
```python
x = 5
print(x)  # Output: 5
x = 10
print(x)  # Output: 10
```
---

## Keyword
Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers:
| Keyword   | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| and       | A logical operator                                                          |
| as        | To create an alias                                                          |
| assert    | For debugging                                                               |
| break     | To break out of a loop                                                      |
| class     | To define a class                                                           |
| continue  | To continue to the next iteration of a loop                                 |
| def       | To define a function                                                        |
| del       | To delete an object                                                         |
| elif      | Used in conditional statements, same as else if                             |
| else      | Used in conditional statements                                              |
| except    | Used with exceptions, what to do when an exception occurs                   |
| False     | Boolean value, result of comparison operations                               |
| finally   | Used with exceptions, a block of code executed no matter what               |
| for       | To create a for loop                                                        |
| from      | To import specific parts of a module                                        |
| global    | To declare a global variable                                                |
| if        | To make a conditional statement                                             |
| import    | To import a module                                                          |
| in        | To check if a value is present in a list, tuple, etc.                       |
| is        | To test if two variables are equal                                          |
| lambda    | To create an anonymous function                                             |
| None      | Represents a null value                                                     |
| nonlocal  | To declare a non-local variable                                             |
| not       | A logical operator                                                          |
| or        | A logical operator                                                          |
| pass      | A null statement, a statement that will do nothing                          |
| raise     | To raise an exception                                                       |
| return    | To exit a function and return a value                                       |
| True      | Boolean value, result of comparison operations                              |
| try       | To make a try...except statement                                            |
| while     | To create a while loop                                                      |
| with      | Used to simplify exception handling                                         |
| yield     | To return a list of values from a generator                                 |

---

## NUMBERS

- INT
    Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
```Python
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
```
- FLOAT
    Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
  ```Python
  x = 1.10
  y = 1.0
  z = -35.59
  print(type(x))
  print(type(y))
  print(type(z))
    
- COMPLEX
    Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
```Python
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
```    
- Random Number
    Python does not have a `random()` function to make a random number, but Python has a built-in module called random() that can be used to make random numbers:
    - example:
    Import the random module, and display a random number from 1 to 9:
```Python
    import randomprint(random.randrange(1, 10))
```
---
## CASTING 
Specify a Variable type.

---

### Mutable and Immutable
#### Mutable
- Objects whose value can be changed after creation.
- You can update, add, or remove elements.
- Example
  - List
  - Dictionary
  - Set
- Coding Example
```Python
x = [1, 2, 3]
print(id(x))  # Example: 140232442
x.append(4)
print(id(x))  # Same ID → modified in place
print(x)
```
Output:
```Python
132594068834752
132594068834752
[1, 2, 3, 4]
```
- Performance
  - Faster to update


#### Immutable
- Objects whose value cannot be changed once created.
- Any modification creates a new object.
- Example
  - Tuple
  - String
  - Integer
  - Float
  - Boolean
- Coding Example
```Python
s = "hello"
print(id(s))  # Example: 140232500
s = s + " world"
print(id(s))  # Different ID → new object created
print(s)
```
Output:
```Python
s = "hello"
print(id(s))  # Example: 140232500
s = s + " world"
print(id(s))  # Different ID → new object created
print(s)
```
- Performance
  - Safe but slower to modify
 
---

### Call by Value n Call by Reference
#### 1. Call by Value (concept)
- A copy of the value is passed to the function.
- The original value does not change.

##### Works like this for immutable types:
- int
- float
- string
- tuple
- bool

##### Example
```Python
def modify(x):
    x = x + 10
    print("Inside function:", x)

a = 5
modify(a)
print("Outside function:", a)
```
Output:
```Python
Inside function: 15
Outside function: 5
```
- Original variable does not change → behaves like call by value.

### 2. Call by Reference (concept)
- A reference (address) is passed to the function.
- Changes inside function affect the original object.

##### Happens with mutable types:
- list
- dictionary
- set
##### Example
```Python
def modify(lst):
    lst.append(10)
    print("Inside function:", lst)

a = [1, 2, 3]
modify(a)
print("Outside function:", a)
```
Output
```Python
Inside function: [1, 2, 3, 10]
Outside function: [1, 2, 3, 10]
```
- Original variable changes → behaves like call by reference.

---

## Homework

###  **1. Arithmetic Practice**
Write a program that performs addition, subtraction, multiplication, and division on two numbers.

```python
# Arithmetic operations on two numbers
num1 = 20
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
```

---

###  **2. Swap Two Variables**

####  Method 1: Using a third variable
```python
x = 10
y = 20

temp = x
x = y
y = temp

print("After swapping: x =", x, ", y =", y)
```

####  Method 2: Without using a third variable
```python
x = 10
y = 20

x, y = y, x

print("After swapping: x =", x, ", y =", y)
```
