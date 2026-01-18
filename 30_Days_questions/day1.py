# 1️⃣ Print “Hello Python” 5 times using a loop.
'''
for i  in range(1,6):
    print("Hello Python")
'''

# 2️⃣ Take two numbers from the user and print their sum, difference, product, and division.
'''
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
print("Sum of 2 number: ",num1+num2)
print("Difference of 2 number: ",num1-num2)
print("Product of 2 number: ",num1*num2)
print("Division of 2 number: ",num1/num2)
'''

# 3️⃣ Write a program to check if a number is even or odd.
'''
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
'''

# 4️⃣ Write a program to find the largest of three numbers.
'''
num1 = 54
num2 = 34
num3 = 66
if num1 > num2 and num1 > num3:
    print(num1,"is the largest number.")
elif num2 > num1 and num2 > num3:
    print(num2,"is the largest number.")
else:
    print(num3,"is the largest number.")
'''

# 5️⃣ Take a string from the user and print it in reverse.
'''
str1 = input("Enter the string: ")
reversed = ''
for ch in str1[::-1]:
    reversed = reversed + ch

print(reversed)
'''
# 6️⃣ Star Pattern – Right Triangle
'''
*
**
***
****
*****
'''
'''
n = 6
for i in range(1,n):
    x = '*' * i
    print(x)
'''

# 7️⃣ Number Pattern – Increasing
'''
1
12
123
1234
12345

'''
'''
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()
'''

# 8️⃣ Alphabet Pattern
'''
A
BB
CCC
DDDD
EEEEE
'''
'''
str1 = 'ABCDE'
for i in range(len(str1)):
    print(str1[i]*(i+1))
'''
# 9️⃣ Inverted Star Pattern
'''
*****
****
***
**
*
''' 
'''   
for i in range(5,0,-1):
    print('*'* i, end ='')
    print()

'''
# 🔟 Square Box Pattern
'''
*****
*   *
*   *
*   *
*****
'''
'''
n = 5
for i in range(1,n+1):
    if i == 1 or i == n:
        print("*"*n, end = ' ')
        print()
    else:
        print("*",' ' * (n-4),"*")
'''








































































