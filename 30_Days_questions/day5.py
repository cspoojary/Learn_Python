# List Comprehension Practice: Rewrite a traditional for loop that creates a list of squares of numbers 1-20 using list comprehension instead.
'''
square = [i*i for i in range(1,21)]
print(f"The square of number is {square}.")
'''

# Word Counter: Write a function that counts the number of words in a sentence or paragraph (hint: watch out for multiple spaces).
'''
def counter(sen):
    num = sen.split()
    count = 0
    for _ in num:
        count = count + 1
    print(count)

sen = ""
counter(sen)
'''
'''
def counter(sen):
    count = [word for word in sen.split()]
    return len(count)
print(counter("I am learning python      programming language"))
'''

# GCD Calculator: Create a function that finds the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))
'''

# Anagram Checker: Write a function that checks if two strings are anagrams of each other (contain the same letters in different order).
'''
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen","silent"))
print()
print(is_anagram("Hello","World"))
'''

# Matrix Addition: Create a function that adds two matrices (2D lists) and returns the result. Assume both matrices have the same dimensions.
'''
def matrix_add(a, b):
    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        result.append(row)

    return result

m1 = [[1,2],[3,4]]
m2 = [[5,6],[7,8]]

print(matrix_add(m1, m2))
'''

# Sort Without Built-in: Implement a simple sorting algorithm (like bubble sort or selection sort) to sort a list without using Python's built-in sort functions.
'''
lst =[3, 45, 76, 11, 4, 9]

n = len(lst)

for i in range(n):
    for j in range(0,n-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]

print(lst)
'''
# Title Case Converter: Write a function that converts a string to title case (first letter of each word capitalized) without using the built-in title() method.
'''
def to_title_case(s):
    words = s.split()
    result = []

    for word in words:
        first_char = word[0].upper()
        rest_char = word[1:].lower()
        result.append(first_char+rest_char)

    return " ".join(result)
text = "Python PROGRAMMING iS FUN"
print(to_title_case(text))
'''

# LCM Calculator: Create a function that finds the Least Common Multiple (LCM) of two numbers.
'''
def lcm(a, b):
    x, y = a, b

    while y != 0:
        x, y = y, x % y

    gcd = x
    return (a*b) // gcd

print(lcm(48, 18))
'''
# Remove Whitespace: Write a function that removes all whitespace from a string (spaces, tabs, newlines) without using replace() or similar methods.
'''
def remove_whitespace(s):
    result = ""
    for ch in s:
        if not ch.isspace():   # checks space, tab, newline
            result += ch
    return result

text = "Hello \t World \n Python"
print(remove_whitespace(text))
'''
# Binary to Decimal: Create a function that converts a binary number (as a string) to its decimal equivalent without using int(binary, 2).
'''
def binary_to_decimal(binary):
    decimal = 0
    power = 0

    for digit in binary[::-1]:   # traverse from right to left
        if digit == '1':
            decimal += 2 ** power
        power += 1

    return decimal

print(binary_to_decimal("1011"))
'''
