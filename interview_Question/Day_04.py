# Find Factorial (Using Function)
# Input: 5
# Output: 120
"""
input = 5
factorial = 1
for i in range(1,imput+1):
    factorial = factorial*i
print(factorial)
"""
"""
def fact(input):
    factorial = 1
    for i in range(1,input+1):
        factorial = factorial*i
    return factorial

input = 5
print(fact(input))
"""
"""
import math

input = 5
result = math.factorial(input)
print(result)
"""

# Fibonacci Series
'''
input = 10
a, b = 0, 1
for i in range(input+1):
    print(a, end=" ")
    a, b = b, a+b
'''
"""
def fib(input):
    a,b = 0,1
    for i in range(input+1):
        print(a, end= " ")
        a,b = b, a+b

input = 10
fib(input)
"""
"""
input = 10
def fib(input):
    if input <= 1:
        return input
    return fib(input-1)+fib(input-2)

for i in range(input):
    print(fib(i), end=" ")
"""

# Print first n numbers
"""
input = 10
for i in range(1,input+1):
    print(i, end=" ")
"""
"""
input = 10
i = 1
while i != input+1:
    print(i, end = " ")
    i = i+1
"""
"""
def num(input):
    for i in range(1,input+1):
        print(i, end=" ")
    
input = 10
num(input)
"""

# Check Prime Number
# Input: 7
# Output: Prime


# Remove Duplicates from List
# Input: [1,2,2,3,4,4]
# Output: [1,2,3,4]

# Find Second Largest Number
# Input: [10, 20, 4, 45, 99]
# Output: 45