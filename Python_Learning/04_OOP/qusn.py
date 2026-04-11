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
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.balance = self.balance + amount
#             print(f'Deposited: {amount}')
#         else:
#             print("Invalid deposit amount")

#     def withdraw(self,amount):
#         if amount <= 0:
#             print(" invalid withdrawal amount")
#         elif amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance = self.balance - amount
#             print(f'withdrawn: {amount}')

#     def check_balance(self):
#         print("Balance=",self.balance)

# s1 = BankAccount('CH01',5000)

# s1.withdraw(500) 
# s1.deposit(1500) 
# s1.check_balance()      


'''
Car Class

Create a class Car with attributes:
    brand
    model
    year

Method:
    display_info()
'''

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")

# car1 = Car("Benz", "C-Class", 2020)

# car1.display_info()

'''
Employee Salary Calculation

Create a class Employee with:
    name
    salary

Method:
    calculate_bonus() (10% of salary)
'''

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary
    
#     def calculate_bonus(self):
#         print("Name = ", self.name)
#         print("Salary = ", self.salary)

#         print("Total Salary = ", self.salary + self.salary * 0.10)

# bonus = Employee("Chaithanya", 75000)
# bonus.calculate_bonus()


'''
Inheritance Example

Create a base class Animal with method:
    sound()

Create derived classes:
    Dog
    Cat

Each class should print its own sound.
'''
# class Animal:
#     def Sound(self):
#         print("Animal make sounds")

# class Dog(Animal):
#     def Sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def Sound(self):
#         print("Cat meows")

# dog = Dog()
# cat = Cat()

# dog.Sound()
# cat.Sound()

'''
Library Management Class

Create a class Library with:
    book_name
    author

Methods:
    add_book()
    display_books()
'''
# class Library:
#     def __init__(self):
#        self. books = []
        
#     def add_book(self, book_name, author):
#         book = {
#             'book_name': book_name,
#             'author':author
#         }
#         self.books.append(book)
#         print(f"Book '{book_name}' added successfully!")

#     def display_books(self):
#         if not self.books:
#             print("No books in the library.")
#         else:
#             print("Library Books :")
#             for i,book in enumerate(self.books, start = 1):
#                 print(f"{i}. {book['book_name']} by {book['author']}")

# lib = Library()

# lib.add_book("Python", "Rossum")
# lib.add_book("Data and information", "Shreyas")

# lib.display_books()

'''
Rectangle Area and Perimeter

Create a class Rectangle with:
    length
    width

Methods:
    area()
    perimeter()
'''
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return 2 * (self.length * self.width )
    
# rect = Rectangle(10, 5)

# print(rect.area())
# print(rect.perimeter())

        
'''
Calculator Class

Create a class Calculator with methods:
    add()
    subtract()
    multiply()
    divide()
'''
# class Calculator: 

#     def add(self, a, b):
#         return a+b
    
#     def subtract(self, a, b):
#         return a-b
    
#     def multiply(slef, a, b):
#         return a*b
    
#     def divide(self, a, b):
#         if b == 0:
#             print("ZeroDivisionError")
#         return a/b
    
# cal =  Calculator()

# print(cal.add(10,4))
# print(cal.subtract(10,4))
# print(cal.multiply(10,4))
# print(cal.divide(10,4))


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
# class StudentResult:
#     def __init__(self, Name, mark1, mark2, mark3):
#         self.Name  = Name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3

#     def display_name(self):
#         return self.Name

#     def total_marks(self):
#         return self.mark1+self.mark2+self.mark3
    
#     def average_marks(self):
#         return self.total_marks()/3
    
#     def grade(self):
#         avg = self.average_marks()
#         if avg >= 90:
#             return "A"
#         if avg >= 75:
#             return "B"
#         if avg >= 60:
#             return "C"
#         else:
#             return "Fail"
        
# student = StudentResult("Chaithanya", 77, 81, 80)

# print(f"Name:", student.display_name())
# print(f"Total: ",student.total_marks())
# print(f"average:",student.average_marks())
# print(f"grade: ", student.grade())
        

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
class ShoppingCart:
    def __init__(self, Product_Name, Price, Quantity):
        self.Product_Name = Product_Name
        self.price = Price
        self.Quantity = Quantity

    def add_product(self, qty):
        self.Quantity += qty
        return self.Quantity
    
    def remove_product(self,qty):
        if qty > self.Quantity:
            return "Cannot remove more that available quantity"
        self.Quantity -= qty
        return self.Quantity
    
    def total_price(self):
        return self.price * self.Quantity
        
cart = ShoppingCart("Laptop", 50000, 1)

cart.add_product(2)
cart.remove_product(1)

print(cart.total_price())