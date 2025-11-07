#Homework
'''1. Arithmetic Practice
Write a program that performs addition, subtraction,
multiplication, and division on two numbers.'''

# Arithmetic operations on two numbers
num1 = 20
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

'''2. Swap Two Variables'''
#Method 1: Using a third variable
x = 10
y = 20

temp = x
x = y
y = temp

print("After swapping: x =", x, ", y =", y)

#Method 2: Without using a third variable
x = 10
y = 20

x, y = y, x

print("After swapping: x =", x, ", y =", y)