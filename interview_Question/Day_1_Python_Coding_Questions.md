# Day 1 — Python Coding Questions: Data Types & Variables

### Swap Two Variables
#### Write a Python program to swap two variables without using a third variable.'''
```python
a = 5
b = 6

a, b = b, a
print('a=',a,'and b =',b)

a = a + b   # a = 11
b = a - b   # b = 5
a = a - b   # a = 6

print('a=',a,'and b =',b)
```

### Type Conversion
#### Write a program that takes a number as a string (e.g., "123") and converts it to an integer and a float.

```python
str1 = "123"
print(type(str1))
intgr = int(str1)
print(type(intgr))
flt = float(str1)
print(type(flt))
```

### Data Type Identification
#### Write a Python function that takes any value and prints its type (e.g., int, float, str, list, etc.).

```python
name = 'Chaithanya'
print(type(name))
```
### Multiple Assignment
```python
a,b,c = 3,4,7
print('a =',a)
print('b =',b)
print('c =',c)
```

### Immutable vs Mutable Behavior
```python
list1 = [10,20,30]

list2 = list1

list1.append(40)

print('list1 = ',list1)
print('list2 = ',list2)
```
### Count Data Types in a List
```python
data = [1, "hi", 3.5, True, [1,2], (4,5),2]

type_count = {}

for i in data:
    t = type(i)
    type_count[t] = type_count.get(t,0)+1

for t,c in type_count.items():
    print(f"{t.__name__}:{c}")
```

### Sum of Digits from a String
```python
Input= "a1b2c3"
sum = 0
for i in Input:
    if i.isdigit():
        i = int(i)
        sum = sum + i
print(sum)
print(sum(int(i) for i in "a1b2c3" if i.isdigit()))
```

### Convert Temperature
```python
print("Temperature Conversion")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")

else:
    print("Invalid choice! Please enter 1 or 2.")
```
### Dynamic Variable Creation
```python
variable = {}

name = input("Enter variable name: ")
value = input("Enter variable value: ")

variable[name] = value

print(f"Variable '{name}' created with value: {variable[name]}")
```

### Variable Scope Demo
```python
x = 10

def change_global():
    global x
    x = 20  # modifies global x
    print("Inside function:", x)

change_global()
print("Outside function:", x)
```
