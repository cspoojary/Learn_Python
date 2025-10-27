# Python Basics 

## Variables in Python
Variables are used to store data values.  
They are created when you assign a value to them, and you don’t need to declare their type (Python is dynamically typed).

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

---

## Data Types in Python
Common built-in types:
- `int` – integers (e.g., `1`, `-3`)
- `float` – decimal numbers (e.g., `3.14`)
- `str` – strings (e.g., `"Hello"`)
- `bool` – Boolean (`True` or `False`)

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

## Arithmetic Operators
Python supports basic arithmetic operations like addition, subtraction, multiplication, division, and more.
| Operator | Description | Example | Result |
|-----------|--------------|----------|--------|
| `+` | Addition | `10 + 3` | 13 |
| `-` | Subtraction | `10 - 3` | 7 |
| `*` | Multiplication | `10 * 3` | 30 |
| `/` | Division | `10 / 3` | 3.333... |
| `//` | Floor Division | `10 // 3` | 3 |
| `%` | Modulus | `10 % 3` | 1 |
| `**` | Exponentiation | `10 ** 3` | 1000 |

### Example:
```python
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a // b)  # Output: 3 (Floor Division)
print(a % b)  # Output: 1 (Modulus)
print(a ** b)  # Output: 1000 (Exponentiation)
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

