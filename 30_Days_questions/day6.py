"Finding second largest number"
# arr=[2, 5, 4, 9, 8]
# largest = second_largest = float('-inf')

# for num in arr:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
    
# print("second_largest number is",second_largest)

# print(arr)
# arr.sort()
# print(arr)
# print("Second largest number is",arr[-2])

'''
Reverse a Number
'''
# num = "123"
# reversed=""
# for i in num:
#     reversed = i + reversed
# print(int(reversed))

# num = 12345
# rev = int(str(num)[::-1])
# print(rev)

"""
Check Palindrome
"""
# str = "madam"
# reversed = ''
# for char in str:
#     reversed = char + reversed
# if reversed == str:
#     print(f"The Given string {str} is a palindrom.")
# else:
#     print(f"The Given string {str} is not a palindrom.")

# str = "naman"
# if str == str[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

'''
Lenthiest word in the text
'''
# text = "Python is a programming language"
# Result = text.split()
# print(Result)
# lenthiest = ''
# for i in Result:
#     for j in Result:
#         if len(i) > len(j):
#             lenthiest = i
#         elif len(j) > len(i):
#             lenthiest = j
#         else: 
#             continue
# print(lenthiest)

'''
Prime number
'''
# num = 5
# if num <= 1:
#     print("Not a prime")
# else:
#     for i in range(2,int(num**0.5)+1):
#         if num % 2 == 0:
#             print("not prime")
#             break
#     else:
#         print("Prime")

"""
Fibonacci Series
"""
# n = 9

# a, b = 0, 1
# for i in range(n): 
#     print(a, end=" ")
#     a , b = b , a+b


'''Factorial number'''

# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i

# print(fact)

# def factorail(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorail(n-1)

# num = 5
# print(factorail(num))
    
"""
Count Vowels in a String
"""

# vowel = "aeiou"
# string = "Chaithanya"
# count = 0
# for i in string.lower():
#     if i in vowel:
#         count = count + 1
#     else:
#         continue
# print(count)

"""
Find Largest Element in an Array
"""

# arr = [2,5,3,8,9,6]

# largest = arr[0]

# for i in arr:
#     if i > largest:
#         largest = i

# print(largest)


# arr = [2,5,3,8,9,6]

# largest = []

# for i in arr:
#     for j in arr:
#         if i > j:
#             largest = i
#         elif j > i:
#             largest = j
#         else:
#             continue
# print(largest)


'''
Sum of Digits
'''

# digit = '2456'
# sum = 0
# for i in digit:
#     sum = sum + int(i)
# print(sum)


"""
Swap Two Numbers
"""
# a = 10
# b = 20

# b = a+b
# a = b - a
# b = b - a
# print("a", a)
# print("b", b)

'''
Check Armstrong Number
'''
# num = "153"
# count = 0
# for i in num:
#     count = count + (int(i) ** 3)

# if count == num:
#     print("Armstrong number")
# else:
#     print("Not a armstrong number")

"""
Display Count of each vowels in a string
"""
# vowel = "aeiou"
# name = "Chaithanya"
# count = {}
# for i in name.lower():
#     if i in vowel:
#         if i in count:
#             count[i] = count[i] +1
#         else:
#             count[i] = 1
            
# print(count)