'''
Day-1
1. Basics of Python
    Concepts: variables, data types, input/output, operators

Project: Simple Calculator
    Variables & operators

- input() / print()
- Conditional statements

Features
- Add, subtract, multiply, divide
- Handle invalid input
'''
print("SIMPLE CALCULATOR")
print()
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.End")

choice = int(input("Enter your choice(1/2/3/4/5): "))
if choice == 1:
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))
    addition = a+b
    print("The sum of a and b = ",addition)

if choice == 2:
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))
    difference = a-b
    print("The difference of a and b is ", difference)

if choice == 3:
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))
    sum = a * b
    print("The sum of a and b is ",sum)

if choice == 4:
    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))
    reminder = a/b
    print("The product of a and b is ", reminder)

if choice == 5:
    print("Simple calculator ends here!.")
else:
    print("Invalid input!")
