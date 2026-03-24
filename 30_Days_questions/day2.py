# 1️⃣ Write a program to calculate the sum of first N natural numbers.
#Example: If N = 5 → Output = 15
'''
sum = 0
for i in range(1,6):
    sum = sum + i
print("Sum of first 5 natural number",sum)
'''

# 2️⃣ Write a program to check whether a number is prime or not.
'''
num = int(input("Enter the number: "))

if num < 2:
    print("Not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
'''

# 3️⃣ Print the multiplication table of a number entered by the user.
'''
num = int(input("Enter the number: "))
for i in range(1,11):
    print(num,"x", i, "=", num*i)
'''

# 4️⃣ Count how many digits a number has.
'''
num = 12345
count = 0
for i in str(num):
    count = count+ 1
print("The count of num:",count)
'''

#5️⃣ Find the factorial of a number using a loop.
'''
num = int(input("Enter the number: "))
fac = 1
for i in range(1,num+1):
    fac = i * fac
print("The factorial of given number is:",fac)
'''

# Pattern Questions
#6️⃣ Star Pyramid Pattern
'''
    *
   ***
  *****
 *******
*********
'''
# n = 9
# for i in range(1,n+1,2):
#     print(" "*((n-i)//2),"*"*i)


# 7️⃣ Number Right Triangle Pattern
'''
1
22
333
4444
55555
'''
# n = 5
# for i in range(1,n+1):
#     print(str(i)*i)

# 8️⃣ Floyd’s Triangle
'''
1
2 3
4 5 6
7 8 9 10
'''
n  = 4
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num, end=' ')
        num = num + 1
    print()


#9️⃣ Inverted Number Pattern
'''
12345
1234
123
12
1
'''
n = 5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end='')
    print()



#🔟 Hollow Triangle Pattern.
'''
    *
   * *
  *   *
 *     *
*********
'''