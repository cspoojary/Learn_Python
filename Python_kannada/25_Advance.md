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

### ✅ Example 1: Squaring numbers
```Python
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

result = map(square, numbers)
print(list(result))  # [1, 4, 9, 16, 25]
```
### ✅ Example 2: Using lambda with map
```Python
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result))  # [2, 4, 6, 8, 10]
```
### ✅ Example 3: Multiple iterables
```Python
a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)
print(list(result))  # [5, 7, 9]
```
---
## 2. filter()
- Definition: Filters elements of an iterable based on a condition (returns only those for which the function returns True).
- Syntax:
```Python
filter(function, iterable)
```
### Example 1: Even numbers
```Python
numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

result = filter(is_even, numbers)
print(list(result))  # [2, 4, 6]
```
### Example 2: Using lambda
```Python
numbers = [10, 25, 30, 47, 50]
result = filter(lambda x: x > 25, numbers)
print(list(result))  # [30, 47, 50]
```
## 3. reduce()
- Definition: Applies a function cumulatively to the items of an iterable.
- It’s like rolling computation (reduce the iterable into a single value).
