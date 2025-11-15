# For Loops in Python

In Python, a for loop is used to iterate over a sequence (like a list,
tuple, string, or range) and execute a block of code repeatedly for each
element in the sequence.

---

## 1. The Basic Structure of a for Loop

A for loop allows you to repeat a block of code a fixed number of times,
or once for each element in a sequence.

**Syntax:**

``` python
for item in sequence:
    # Code to execute for each item in the sequence
```

**Example:**

``` python
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)
```

**Output:**

    Bengaluru
    Mysuru
    Hubballi
    Mangaluru
---
## 2. Using range() with for Loops

The `range()` function generates a sequence of numbers.

**Syntax:**

    range(start, stop, step)

**Example: Counting from 1 to 10**

``` python
for i in range(1, 11):
    print(i)
```

**Example: Counting by 2s**

``` python
for i in range(1, 11, 2):
    print(i)
```
---
## 3. Looping Over Strings

``` python
name = "Karnataka"
for letter in name:
    print(letter)
```
---
## 4. Nested for Loops

Example: Multiplication Table

``` python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()
```
---
## 5. Using break in a for Loop

``` python
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        print(f"Found {city}!")
        break
    print(city)
```
---
## 6. Using continue in a for Loop

``` python
for city in cities:
    if city == "Hubballi":
        continue
    print(city)
```
---
## 7. Looping with enumerate()

``` python
for index, city in enumerate(cities):
    print(f"City {index + 1}: {city}")
```
---

## 8. Using else with for Loops

``` python
for city in cities:
    print(city)
else:
    print("No more cities!")
```
---
## 9. Real-Life Example: Distributing Laddus

``` python
laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya"]

for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
        laddus -= 1
    else:
        print("No laddus left!")
```
---
## Homework

### 1. Multiples of 3

Print all multiples of 3 between 1 and 30.

### 2. Sum of First 10 Numbers

Calculate the sum of numbers from 1 to 10.

### 3. Print Your Name Letter by Letter

Input your name and print each letter.

### 4. Count Vowels in a String

Count how many vowels are in a given string.
