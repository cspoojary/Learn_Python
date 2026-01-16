'''
Day 3: Conditional Statements
Concepts: if, elif, else
Project: Student Grade System
    - Input marks
    - Display grade & result
''' 
print("STUDENT GRADE SYSTEM")
Name = input("Enter your name: ")
Mark = int(input("Enter your marks(1-100): "))
print("Name :",Name)
if Mark >= 85:
    print("You are grade is A.")
elif Mark >= 70:
    print("You are grade is B.")
elif Mark >= 60:
    print("You are grade is C.")
elif Mark >= 50:
    print("You are grade is D.")
else:
    print("You are grade is F.")

