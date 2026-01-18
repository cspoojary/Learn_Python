'''
Day 4:Loops
Concepts: for, while
Project: Multiplication Table Generator

Print tables
    Loop-based logic
'''
number = int(input("Enter the number which you need multiplication value: "))

for i in range(1,11):
    print(f"{number} X {i} = {number*i}")