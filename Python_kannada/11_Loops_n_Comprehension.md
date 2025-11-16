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
