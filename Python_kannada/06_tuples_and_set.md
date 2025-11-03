# Tuples and Sets in Python

## 1. Tuples in Python

A **tuple** is a collection of items that is **ordered** and **immutable** (unchangeable).  
Tuples are similar to lists, but once a tuple is created, you cannot modify it.  
They are often used to group related data together.

### Syntax
```python
my_tuple = (element1, element2, element3, ...)
```

### Example
```python
my_tuple = ("apple", "banana", "cherry")
numbers_tuple = (1, 2, 3, 4)
```

### Creating a Tuple with One Element
To create a tuple with only one element, include a trailing comma:
```python
single_element_tuple = ("apple",)
```
---
## 2. Accessing Tuple Elements

You can access elements in a tuple using indexing, just like with lists.  
Tuples also support **negative indexing**.

### Example
```python
fruits = ("apple", "banana", "cherry")
print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: cherry
```

### Slicing Tuples
You can also slice tuples to access a subset of the elements.
```python
print(fruits[1:3])  # Output: ('banana', 'cherry')
```
---
## 3. Tuple Operations

Although tuples are immutable, you can perform various operations with them.

### Tuple Concatenation
You can combine two or more tuples using the **+** operator.
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)
```

### Tuple Repetition
You can repeat a tuple multiple times using the **\*** operator.
```python
repeated_tuple = (1, 2) * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)
```

### Checking Membership
You can check if an item exists in a tuple using the **in** operator.
```python
print("apple" in fruits)  # Output: True
```

---
