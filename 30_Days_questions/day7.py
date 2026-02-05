# Reverse a string
"""
Str = "Chaithanya"
for i in Str[::-1]:
    print(i, end="")
"""
'''
Str = "Chethan"
rev = ""
for i in Str:
    rev = i + rev
print(rev)
'''

# Reverse a number
'''
num = "12345"
for i in num[::-1]:
    print(int(i), end="")
'''

'''
num = "12345"
rev = ""
for i in num:
    rev = i+rev
print(int(rev))
'''

# Check whether a string is a palindrome
'''
str = "naman"
if str == str[::-1]:
    print("Given String is Palindrome")
else:
    print("Given String is not a palidrome.")
'''

'''
str = "Chaithu"
palind =""
for ch in str:
    palind = ch + palind
if palind == str:
    print("Given String is Palindrome")
else:
    print("Given String is not a palidrome.")
'''

# Find the largest and smallest number in a list
'''
lst = [4,8,2,9,3,2]
lst.sort()
print("The largest number is",lst[-1])
print("The smallest number is",lst[0])
'''

'''
lst = [4,8,2,9,3,2]

a = len(lst)
for i in range(a):
    for j in range(0,a-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)
print("The largest number is",lst[-1])
print("The smallest number is",lst[0])
'''

# Count vowels and consonants in a string
'''
str = "Chaithanya"
vowel = 0
consonant = 0
for ch in str.lower():
    if ch in "aeiou":
        vowel = vowel + 1
    else:
        consonant = consonant + 1
print("The vowels in a string",vowel)
print("The consonant in a string", consonant)
'''

# Find the sum of all elements in a list
'''
lst = [4,6,2,8,9]
sum = 0
for i in lst:
    sum = sum + i
print(sum)
'''
# Remove duplicate elements from a list
'''
lst = [3,4,2,3,5,7]
n_lst =[]
for i in lst:
    if i in n_lst:
        continue
    else:
        n_lst.append(i)
print(n_lst)
'''

# Swap two variables without using a third variable
'''
a = 4
b = 5
a = a+b
b = a - b
a = a - b
print("a =",a)
print("b =",b)
'''

# Check whether a number is prime
'''
num = 4
if num <= 1:
    print("Not Prime")
else:
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
'''



# Find the factorial of a number
'''
num = 5
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)
'''

'''
num = 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(num))
'''
        
    