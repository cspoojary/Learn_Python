# Python Basics 

## Variables in Python
Variables are used to store data values.  
You don’t need to declare their type (Python is dynamically typed).

###  Syntax:
```python
x = 5        # integer
y = "Hello"  # string
```

###  Rules for Naming Variables:
- Must start with a letter or underscore `_`
- Can contain letters, digits, and underscores
- Case-sensitive (`Name` and `name` are different)

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
```python
x = 10
print(type(x))  # Output: <class 'int'>
```

---

## Type Conversion
You can convert between data types using:
`int()`, `float()`, `str()`, etc.

### Example:
```python
x = "10"      # string
y = int(x)    # convert to integer
z = float(y)  # convert to float
print(z)      # Output: 10.0
```

---

## Arithmetic Operators
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
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

## Assigning Values to Multiple Variables
You can assign multiple values at once:
```python
x, y, z = 10, 20, 30
print(x, y, z)
```

Or assign one value to multiple variables:
```python
x = y = z = 100
print(x, y, z)
```

---

## Variable Reassignment
Variables can be changed anytime:
```python
x = 5
print(x)
x = 10
print(x)
```

---

## Homework

### 🧮 **1. Arithmetic Practice**
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

