'''
Create a Student Class

Create a class Student with attributes:
    name
    age
    marks

Add a method to display student details.
'''
# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display_student(self):
#         print("Name : ", self.name)
#         print("Age :",self.age)
#         print("Marks : ",self.marks)

# s1 = Student("Chaithanya",23,98)
# s1.display_student()

        


'''
Bank Account Class

Create a class BankAccount with:
    account_number
    balance

Methods:
    deposit(amount)
    withdraw(amount)
    check_balance()
'''
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f'Deposited: {amount}')
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if amount <= 0:
            print(" invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print(f'withdrawn: {amount}')

    def check_balance(self):
        print("Balance=",self.balance)

s1 = BankAccount('CH01',5000)

s1.withdraw(500) 
s1.deposit(1500) 
s1.check_balance()      


'''
Car Class

Create a class Car with attributes:
    brand
    model
    year

Method:
    display_info()
'''

'''
Employee Salary Calculation

Create a class Employee with:
    name
    salary

Method:
    calculate_bonus() (10% of salary)
'''

'''
Inheritance Example

Create a base class Animal with method:
    sound()

Create derived classes:
    Dog
    Cat

Each class should print its own sound.
'''

'''
Library Management Class

Create a class Library with:
    book_name
    author

Methods:
    add_book()
    display_books()
'''

'''
Rectangle Area and Perimeter

Create a class Rectangle with:
    length
    width

Methods:
    area()
    perimeter()
'''


'''
Calculator Class

Create a class Calculator with methods:
    add()
    subtract()
    multiply()
    divide()
'''

'''
Student Result System

Create a class StudentResult with:
    name
    marks in 3 subjects

Methods:
    total_marks()
    average_marks()
    grade()
'''

'''
Shopping Cart Class

Create a class ShoppingCart with:
    product name
    price
    quantity

Methods:
    add_product()
    remove_product()
    total_price()
'''
