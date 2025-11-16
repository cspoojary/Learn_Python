# Lists and Dictionaries with For Loops, List Comprehension, and Dictionary Comprehension

## 1. Looping Through Lists

### Example: Sum of all numbers in a list

``` python
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total sum:", total)
```

Output:

    Total sum: 150

### Example: Doubling each number in a list

``` python
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print("Doubled List:", doubled)
```

### Example: Printing Kannada food items

``` python
foods = ["Dosa", "Idli", "Vada", "Bisibelebath"]

for food in foods:
    print(f"I like {food}")
```

------------------------------------------------------------------------
## 2. Looping Through Dictionaries

### Example: Iterating over dictionary keys

``` python
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student in student_marks:
    print(student)
```

### Example: Iterating over dictionary values

``` python
for marks in student_marks.values():
    print(marks)
```

### Example: Iterating over both keys and values

``` python
for student, marks in student_marks.items():
    print(f"{student} scored {marks} marks")
```

------------------------------------------------------------------------
## 3. For Loops with `range()`

### Example:

``` python
students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]

student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)
```

------------------------------------------------------------------------
