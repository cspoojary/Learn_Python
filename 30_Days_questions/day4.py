# Factorial Calculator: Write a function that calculates the factorial of a number using a loop (e.g., 5! = 5×4×3×2×1 = 120).
'''
number = int(input("Enter the number: "))
total = 1
for i in range(1,number+1):
    total = total*i
print("The factorial of the number",total)
'''

# Prime Number Checker: Create a function that determines whether a given number is prime or not.
'''
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
        
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number:")
'''

'''
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
'''

# Fibonacci Sequence: Write a program that generates the first n numbers in the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8...).
'''
n = int(input("Enter the number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a+b 
'''

'''
def fibonacci(n):
    a, b = 0,1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b

n = int(input("Enter number of terms: "))
fibonacci(n) 
'''
# String Character Counter: Build a function that counts how many times each character appears in a string and returns a dictionary with the results.
'''
string = 'chaithanya'

character = {}

for ch in string:
    if ch in character:
        character[ch] = character[ch] + 1
    else:
        character[ch]=1

print(character)
'''

# List Duplicates Remover: Write a function that takes a list and returns a new list with all duplicate elements removed, preserving the original order.
'''
def unique(lst):
    number = []
    for i in lst:
        if i not in number:
            number.append(i)
        else:
            continue
    return number

lst = [1,4,2,6,3,4,2,6,8,7,8,3]
print(unique(lst))
'''

# Number Guessing Game: Create a simple game where the computer picks a random number between 1-100 and the user has to guess it, with hints like "too high" or "too low".
'''
import random
number = random.randint(1,100)
attempt = 0
print("NUMBER GUESSING GAME")
print("Guess the number between 1-100")

while True:
    guess = int(input("Guess the number: "))
    attempt = attempt+1
    if guess > number:
        print("The number is smaller than your guess.")
    elif guess < number:
        print("The number is bigger than your guess.")
    else:
        print(f"Congratulations! you guessed number in {attempt} attemps.")
'''

# Leap Year Checker: Write a function that determines if a given year is a leap year (divisible by 4, except century years must be divisible by 400).
'''
year = int(input("Enter the year to check leap year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year!.")
else:
    print(f"{year} is not leap year.")
'''
    
# Sum of Digits: Create a function that takes an integer and returns the sum of its digits (e.g., 1234 → 10).
'''
def sum(num):
    count = 0
    for i in num:
        count = count + int(i)
    print(count)

num = input("Enter the 5 digit number: ")
sum(num)
'''

# List Reversal: Write a function that reverses a list in place without creating a new list or using built-in reverse methods.
'''
def rev(str):
    print("Reversed String: ",str[::-1])

str = input("Enter the string: ")
rev(str)

'''
# Armstrong Number: Check if a number is an Armstrong number (a number equal to the sum of its digits each raised to the power of the number of digits, e.g., 153 = 1³ + 5³ + 3³).'''
'''
num = int(input("Enter the armstrong number: "))
temp = num
digits = len(str(num))
sum_of_powers = 0

while temp > 0 :
    digit = temp % 10
    sum_of_powers = sum_of_powers + (digit**digits)
    temp //= 10

if sum_of_powers == num:
    print(num,"is a Armstrong number.")
else:
    print(num,"is not a Armstrong number.")

'''

