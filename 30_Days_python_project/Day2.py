'''
Day 2
Variables & Data Types

Concepts:
int, float, string, boolean
input/output

Project:
Personal Profile Generator
Take name, age, skills
Print formatted output
'''
print("Hey.. Hi Welcome to the Profile Generator\n")

first_name = input("Enter your first name: ")
second_name = input("Enter your second name: ")
age = int(input("Enter your age: "))
skills = input("Enter your skills (comma separated): ")
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

print("\n----- PROFILE DETAILS -----")
print(f"Name        : {first_name} {second_name}")
print(f"Age         : {age} years")
print(f"Skills      : {skills}")
print(f"Student     : {is_student}")
print("---------------------------")
