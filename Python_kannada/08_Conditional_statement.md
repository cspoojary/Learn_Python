# Conditional Statements in Python: if, elif, and else

In programming, conditional statements are used to perform different actions based on different conditions. Python uses `if`, `elif`, and `else` statements to allow your program to make decisions.

---

## 1. The if Statement

The `if` statement is used to test a condition. If the condition is `True`, the block of code under the `if` statement is executed.

### Syntax:
```python
if condition:
    # Code block to execute if the condition is True
```
### Example:
Let's say you want to check if it's time for dinner (assuming dinner time is 8 PM).

```python
time = 20  # 20 represents 8 PM in 24-hour format
if time == 20:
    print("It's time for dinner!")
```

---

## 2. The else Statement

The `else` statement provides an alternative block of code to execute when the `if` condition is `False`.

### Syntax:
```python
if condition:
    # Code block if the condition is True
else:
    # Code block if the condition is False
```

### Example:
```python
time = 18  # 6 PM
if time == 20:
    print("It's time for dinner!")
else:
    print("It's not dinner time yet.")
```
## 3. The elif Statement

The `elif` (short for "else if") statement checks another condition if the previous `if` or `elif` condition was `False`.

### Syntax:
```python
if condition1:
    # Code block if condition1 is True
elif condition2:
    # Code block if condition2 is True
else:
    # Code block if none of the above conditions are True
```

### Example:
```python
time = 15  # 3 PM

if time == 8:
    print("It's breakfast time!")
elif time == 13:
    print("It's lunch time!")
elif time == 20:
    print("It's dinner time!")
else:
    print("It's not a meal time.")
```
---
## 4. Comparison Operators in if Statements

You can use comparison operators to compare values in `if` statements:

| Operator | Description |
|-----------|--------------|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

### Example:
```python
age = 19

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```
---

## 5. Logical Operators in if Statements

You can also use logical operators to combine multiple conditions:

| Operator | Description |
|-----------|--------------|
| `and` | Returns True if both conditions are True |
| `or` | Returns True if at least one condition is True |
| `not` | Reverses the result of a condition |

### Example:
```python
age = 16
has_student_id = True

if age < 18 and has_student_id:
    print("You are eligible for the student discount!")
else:
    print("You are not eligible for the student discount.")
```
---

## 6. Example: Checking Bus Ticket Prices

```python
age = 65

if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")
```
---
## 7. Nested if Statements

```python
day = "Saturday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")
```
---
## 8. Indentation in Python

Python uses **indentation** to define blocks of code.

### Example:
```python
age = 19

if age >= 18:
    print("You are eligible to vote.")
    print("Remember to bring your voter ID.")
else:
    print("You are not eligible to vote.")
```
---
