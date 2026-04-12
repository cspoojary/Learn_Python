# Reverse a String
# Input: "hello"
# Output: "olleh"
'''
str1 = input("Enter a string: ")
reverse = str1[::-1]
print(f"The string is {str1} and the reversed string is {reverse}")
'''
'''
str1 = input("Enter a string: ")
reverse = ""
for ch in str1:
    reverse = ch + reverse
print("The reversed string is: ", reverse)
'''
'''
def revrsed(s):
    reverse = ""
    for ch in s:
        reverse = ch + reverse
    return reverse

print("The reversed string is", revrsed("Chaithanya"))
'''

# Check Palindrome
# Example: "madam" → True
'''
str1 = input("Enter the string: ")
str2 = str1[::-1]
if str1 == str2:
    print("The entered string is palidrome.")
else:
    print("The entered string is not a palindrome.")
'''
'''
str1 = input("Enter the string: ")
str2 = ''
for ch in str1:
    str2 = ch + str2
if str1 == str2:
    print("The entered string is a palidrome.")
else:
    print("The entered string is not a palindrome.")
'''
'''
def palindrome(s):
    str2 = ''
    for ch in s:
        str2 = ch+str2

    if s == str2:
        return True
    else:
        return False

print(palindrome("Chaithu"))
print(palindrome("madam"))
'''

# Find Largest Number in a List
# Input: [10, 45, 2, 99]
# Output: 99
"""
Input = [10, 45, 2, 99]
largest = max(Input)
print(largest)
"""

"""
Input = [10, 45, 2, 99]
largest = 0
for i in Input:
    if i > largest:
        largest = i
    else:
        continue
print(largest)
"""
'''
def largest(num):
    large = 0
    for i in num:
        if i > large:
            large = i
        else:
            continue
    return large

num = [10, 45, 2, 99]
print("The largest number is",largest(num))
'''

# Count Vowels in a String
# Input: "python"
# Output: 1
"""
input = "Chaithanya"
count = 0
for ch in input:
    if ch in "aeiouAEIOU":
        count = count + 1
    else:
        continue
print(f"The total count of vowels in {input} is {count}")
"""
"""
input = "Chaithanya"
Count = sum(1 for ch in input if ch.lower() in "aeiou")
print(Count)
"""

# Sum of Digits
# Input: 1234
# Output: 10
"""
input = 1234
sum = 0
while input > 0:
    digit = input % 10
    sum = sum + digit
    input  = input // 10

print(sum)
"""
"""
input = 1234
print(sum(int(d) for d in str(input)))
"""
"""
def sum_of_digits(input):
    total = 0
    while input > 0:
        digit = input % 10
        total = total + digit
        input = input // 10
    return total

input = 1234
print(sum_of_digits(input))
"""