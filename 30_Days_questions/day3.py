# Hello World Plus: Write a program that asks for your name and age, then prints a greeting message like "Hello [name], you are [age] years old!"
'''
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
print(f"Hello {Name}, you are {Age} years old!")
'''

# Simple Calculator: Create a program that takes two numbers and an operator (+, -, *, /) as input and performs the calculation.
'''
a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))
print("Sum: ",a+b)
print("difference: ",a-b)
print("Product: ",a*b)
print("Quotient: ",a/b)
'''

# Even or Odd: Write a function that checks whether a given number is even or odd and returns the result.
'''
num = int(input("Enter the number: "))
if num % 2 == 0:
    print(f"{num} is a even.")
else:
    print(f"{num} is a odd.")
'''

# Temperature Converter: Build a program that converts temperatures between Celsius and Fahrenheit. Let the user choose the conversion direction.
'''
print("TEMPERATURE CONVERTER")
print("1. Celsius to fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice(1 or 2):  "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius + 9/5) + 32
    print(f"{celsius} deg cel = {fahrenheit:.2f} deg fhn")

elif choice == 2:
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit + 32) +9/5
    print(f"{fahrenheit} dg cs = {celsius:.2f} dg cs") 

else:
    print("Invalid choice! Please select 1 or 2.")
'''

# List Sum: Write a function that takes a list of numbers and returns their sum without using the built-in sum() function.
'''
def sum(number):
    total = 0
    for num in number:
        total = total+num
    return total
result = sum([10,20,30])
print(result)
'''

# Reverse a String: Create a function that takes a string as input and returns it reversed without using slicing shortcuts.
'''
def rev_str(str):
    reversed = " "
    for char in str:
        reversed = char + reversed
    return reversed
print(rev_str("Chaithu"))
'''
# Count Vowels: Write a program that counts the number of vowels (a, e, i, o, u) in a given string.
'''
vow = "aeiou"
count = 0
str = input("Enter the string: ")
string = str.lower()
for char in string:
    if char in vow:
        count = count + 1
    else:
        continue
print("The count of the vow in string is:",count)
'''

# Find Maximum: Create a function that finds the largest number in a list without using the max() function.
'''
def largest(number):
    large = number[0]
    for num in number:
        if num > large:
            large = num
        else:
            continue
    return large
number = largest([10,80,60,40])
print("Largest number is: ",number)
'''

# Multiplication Table: Write a program that prints the multiplication table for a number entered by the user (from 1 to 10).
'''
number = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{number} x {i} = {number*i}")
'''

# Palindrome Checker: Create a function that checks whether a given string is a palindrome (reads the same forwards and backwards).
'''
def palind(str):
    if str[::-1] == str:
        print("The given string is palindrome.")
    else:
        print("The given string is not a palindrome.")
        
str=input("Enter the string to check palindrome: ")
palind(str)
'''
'''
def palind(str):
    rev = ''
    for char in str:
        rev = char + rev
        
    if rev == str:
        print("The given string is palindrome.")
    else:
        print("The given string is not a palindrome.")

str=input("Enter the string to check palindrome: ")
palind(str)
'''