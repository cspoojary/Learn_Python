# While Loops in Python

A **loop** is a programming structure that repeats a set of instructions as long as a specified condition is `True`. In Python, the `while` loop allows you to repeatedly execute a block of code as long as the condition is `True`.

---
## 1. Basic Structure of a while Loop

The `while` loop repeatedly executes a block of code as long as the condition is `True`.

**Syntax:**
```python
while condition:
    # Code to execute as long as condition is True
```

**Example:**
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

**Output:**
```
1
2
3
4
5
```

---
## 2. Common Example: Counting Sheep

```python
sheep_count = 1
while sheep_count <= 10:
    print(f"Sheep {sheep_count}")
    sheep_count += 1
```

**Output:**
```
Sheep 1
Sheep 2
...
Sheep 10
```

---
## 3. Avoiding Infinite Loops

An infinite loop occurs when the condition never becomes `False`.

**Example of Infinite Loop:**
```python
i = 1
while i <= 5:
    print(i)  # Forgot to update i
```

To fix this, always update the variable inside the loop.

---
## 4. Using `break` to Exit a Loop

```python
sheep_count = 1
while sheep_count <= 10:
    print(f"Sheep {sheep_count}")
    if sheep_count == 5:
        print("That's enough counting!")
        break
    sheep_count += 1
```

**Output:**
```
Sheep 1
Sheep 2
Sheep 3
Sheep 4
Sheep 5
That's enough counting!
```

---
