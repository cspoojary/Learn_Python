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
## 5. Using `continue` to Skip an Iteration

```python
sheep_count = 1
while sheep_count <= 5:
    if sheep_count == 4:
        sheep_count += 1
        continue
    print(f"Sheep {sheep_count}")
    sheep_count += 1
```

**Output:**
```
Sheep 1
Sheep 2
Sheep 3
Sheep 5
```

---
## 6. Using while Loops for User Input

```python
pin = ""
correct_pin = "1234"
while pin != correct_pin:
    pin = input("Enter your PIN: ")
    if pin != correct_pin:
        print("Incorrect PIN. Try again.")
print("PIN accepted. You can proceed.")
```

---
## 7. Real-life Example: KSRTC Bus Seats Availability

```python
available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")
```

**Output Example:**
```
5 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
...
All seats are booked!
```

---

## 8. Nested while Loops

```python
snacks_available = 3
money = 10

while snacks_available > 0 and money > 0:
    print(f"Snacks available: {snacks_available}. Money: ₹{money}")
    buy = input("Do you want to buy a snack for ₹5? (yes/no): ").lower()
    
    if buy == "yes" and money >= 5:
        snacks_available -= 1
        money -= 5
        print("Snack purchased!")
    else:
        print("No purchase made.")
        
print("Either snacks are sold out or you are out of money.")
```

---

## Homework

### 🧮 1. Basic Counting with while Loop
Write a program that counts from 1 to 10 using a while loop.

### 🔢 2. Odd Numbers Printer
Create a program that prints all odd numbers between 1 and 20 using a while loop.

### 🚌 3. Ticket Booking Simulation
Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked, the available seats decrease. When there are no seats left, display `"All seats are booked."`

### ⏳ 4. Countdown Timer
Write a program that counts down from 10 to 1 using a while loop and prints `"Happy New Year!"` after the countdown is over.
