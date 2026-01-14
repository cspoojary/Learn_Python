# 📌 map(), filter(), and reduce() in Python

- These are functional programming tools in Python. They let you apply functions to iterables (like lists, tuples, sets) in a clean and concise way.
---
## 1. map()
- Definition: Applies a given function to every element of an iterable.
- Syntax:
```Python
map(function, iterable)
```
- Returns a map object (iterator). Usually converted to a list or tuple.

## ✅ Example 1: Squaring numbers
```Python
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

result = map(square, numbers)
print(list(result))  # [1, 4, 9, 16, 25]
```
