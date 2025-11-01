 Lists in Python

## 1. What is a List?
A **list** is a collection of items that are **ordered**, **mutable** (changeable), and allow **duplicate elements**.  
Lists can hold items of different data types, such as integers, strings, or even other lists.

### Syntax:
```python
my_list = [element1, element2, element3, ...]
```

### Example:
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 3, True]
```
---

## 2. Accessing List Elements
You can access individual elements in a list using **indexing**.  
Remember that Python uses **zero-based indexing**, so the first item is at index `0`.

### Syntax:
```python
list_name[index]
```

### Example:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry
```

You can also use **negative indexing** to access elements from the end of the list:

```python
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana
```
---

## 3. Modifying Lists
Lists are **mutable**, which means you can change the value of items in a list.

### Changing a specific element:
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']
```

### Adding elements:

#### append(): Adds an element to the end of the list.
```python
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']
```

#### insert(): Inserts an element at a specific index.
```python
fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'cherry']
```

### Removing elements:

#### remove(): Removes the first occurrence of an element.
```python
fruits.remove("orange")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry']
```

#### pop(): Removes the element at a specific index (or the last item if no index is provided).
```python
fruits.pop()  # Removes the last item
print(fruits)  # Output: ['apple', 'kiwi']

fruits.pop(0)  # Removes the first item
print(fruits)  # Output: ['kiwi']
```

#### clear(): Removes all elements from the list.
```python
fruits.clear()
print(fruits)  # Output: []
```
---
## 4. Slicing Lists
You can extract a portion of a list using **slicing**.

### Syntax:
```python
list_name[start:stop:step]
```
- **start**: The index to start the slice (inclusive).  
- **stop**: The index to stop the slice (exclusive).  
- **step**: The number of steps to skip elements (default is 1).

### Examples:
```python
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3]
print(numbers[:4])   # Output: [0, 1, 2, 3]
print(numbers[2:])   # Output: [2, 3, 4, 5, 6]
print(numbers[::2])  # Output: [0, 2, 4, 6]
```
---
