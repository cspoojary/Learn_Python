"""
Your task is to print the string Hello World.
"""
# print("Hello Word")

"""
Your task is to print the first five letters of the English alphabet.
A
B
C
D
E
"""
# print("A")
# print("B")
# print("C")
# print("D")
# print("E")

"""
*****
****
***
**
*
"""
# for i in range(5,0,-1):
#     print("*"*i)

"""
*****
   *
  *
 *
*****
"""
# for i in range(1,6):
#     if i == 5 or i == 1:
#         print("*"*5)
#     else:
#         print(" "*(5-(i+1)),"*")

"""
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
"""
# n = 5
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

"""
You are given the length and breadth of a rectangle. Your task is to calculate its area and perimeter.

The formulas are:

Area = length × breadth
Perimeter = 2×(length+breadth)
"""
# length , breadth = map(int, input("Enter the values: ").split())
# Area = length * breadth
# Perimeter = 2 * (length * breadth)
# print("Area =", Area)
# print("Perimater = ", Perimeter)

"""
You are given an integer N.Your task is to print the multiplication table of N from 1 to 10.
"""
# n = int(input("Enter the number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

"""
You are given two integers N and M. Your task is to compute and print the results of the following operations:
N+M
N−M
N×M
N÷M (integer division)
N mod M

input
N : 6
M : 4

input:
N : 1000000000
M : 1000000000
"""
# N , M = map(int, input("Enter the value: ").split())
# print("Addition =", N+M)
# print("Substraction =", N-M)
# print("multiplication =", N * M)
# print("Division =", N / M)
# print("Modulus =", N // M)

"""
You are given two integers N and M. Your task is to find the sum of the last digits of N and M.
N : 169
M : 125
"""
# N, M = map(int, input("Enter the values: ").split())
# Last_digit_N = N % 10
# Last_digit_M = M % 10
# sum = Last_digit_N + Last_digit_M
# print("The sum of last digit is =",sum)

"""
You are given an integer N. Your task is to determine whether the number is even or odd.
"""
# n = int(input("Enter the number: "))
# if n / 2 == 0:
#     print("Even")
# else:
#     print("Odd")

"""
You are given two integers N and F. Your task is to check whether F is a factor of N.

A number F is said to be a factor of N if N is divisible by F.

n = 36
f = 6

Output: 
    Yes if F is a factor of N
    No otherwise
"""
# N , F = map(int, input("Enter the Number : ").split())
# if N % F == 0:
#     print("Yes, N divides F")
# else:
#     print("No, N is not divisible by F")


"""
You are given two integers N and M. Your task is to check whether M is a multiple of N.

A number M is said to be a multiple of N if M is a multiple of N.
n = 6
m  = 36

Output:
    Yes if M is a multiple of N
    No otherwise
"""
# N, M = map(int, input("Enter the values: ").split())
# if M % N == 0:
#     print("Yes")
# else:
#     print("No") 

"""
You are given the marks obtained by a student. Your task is to check whether the student has passed or failed.
A student is considered to have passed if the marks obtained are at least 35.

Output:
Pass if the student has passed
Fail otherwise
"""
# mark = int(input("Enter the marks: "))
# if mark >= 35:
#     print("Pass")
# else :
#     print("Fail")

"""
You are given two integers A and B. Your task is to find the minimum and maximum among them.

Output:
Min = X
Max = Y
"""
# A , B = map(int, input("Enter the intergers: ").split())
# if A > B:
#     print("Max =", A)
#     print("Min =", B)
# else:
#     print("Min =", A)
#     print("Max =", B)

"""
You are given two integers A, B and C. Your task is to find the minimum and maximum among them.

input : 12 9 15

Output
Min = X
Max = Y
"""
# A, B , C = map(int, input("Enter values: ").split())
# #For minimum
# if A < B and A < C:
#     Minimum = A
# elif B < A and B < C:
#     Minimum = B
# else:
#     Minimum = C

# #For Maximum
# if A > B and A > C:
#     Maximum = A
# elif B > A and B > C:
#     Maximum = B
# else:
#     Maximum = C

# print("Minimum =", Minimum)
# print("Maximum = ", Maximum)

"""
You are given the marks obtained by a student. Based on the marks, display an appropriate performance message according to the following rules:
- If marks are greater than 90, print Excellent
- Else if marks are greater than 80 and less than or equal to 90, print Good
- Else if marks are greater than 70 and less than or equal to 80, print Fair
- Else if marks are greater than 60 and less than or equal to 70, print Meets Expectations
- Else (marks less than or equal to 60), print Below Par
"""
# Marks = int(input("Enter your marks(Out of 100): "))
# if Marks > 90:
#     print("Excellent")
# elif Marks > 80:
#     print("Good")
# elif Marks >  70:
#     print("Fair")
# elif Marks > 60:
#     print("Meete expectations")
# else:
#     print("Below Expectations")

"""
You are given the coordinates of a point (X,Y)
 on a Cartesian plane. Your task is to determine the location of the point.

The possible locations are:

Origin — if X=0 and Y=0
X axis — if Y=0 and X≠0
Y axis — if X=0 and Y≠0
1st Quadrant — if X>0 and Y>0
2nd Quadrant — if X<0 and Y>0
3rd Quadrant — if X<0 and Y<0
4th Quadrant — if X>0 and Y<0
"""
x = int(input("Enter x quadrant: "))
y = int(input("Enter y quadrant: "))

if x == 0 and y == 0:
    print("Origin")
elif y == 0:
    print("X axis")
elif x == 0:
    print("Y axis")
elif x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
else:
    print("4th Quadrant")