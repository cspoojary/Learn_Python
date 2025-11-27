# The Four Pillars of OOP
## 1. Encapsulation
- Definition: Encapsulation involves wrapping data and methods that operate on that data within one unit, such as a class. This protects the data from external interference and misuse, improving security and maintainability.
- Real-World Example: Imagine an ATM machine—you interact with a limited interface (e.g., withdraw, deposit, check balance) but do not have access to the inner mechanics or backend functions.
Real-World Example in Code:
```Python
class ATM:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance")

atm = ATM(1000)
atm.deposit(500)
atm.withdraw(300)
```
Here, __balance is a private attribute, ensuring only the deposit() and withdraw() methods can modify it.

Programming Example in Code:
Consider a User class for storing login information:
```Python
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private attribute

    def get_username(self):
        return self.username

    def check_password(self, password):
        return password == self.__password

user = User("dev_karnataka", "pass1234")
print(user.get_username())  # Access allowed
print(user.check_password("wrong_pass"))  # Returns False
print(user.check_password("pass1234"))  # Returns True
```
Encapsulation here hides __password from direct access.

---
2. Abstraction
- Definition: Abstraction hides the complex inner workings of an object, exposing only the essential parts for interaction.
- Real-World Example: Think about driving a car. You use the steering wheel and pedals to control the car, without needing to know the engine mechanics or braking systems.
Real-World Example in Code:
```Python
class Car:
    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Car accelerating")

    def brake(self):
        print("Car stopping")

car = Car()
car.start_engine()  # Abstracts complex internal workings
car.accelerate()
car.brake()
```
Here, Car abstracts internal functions like ignition and fuel management, presenting only basic methods for interaction.

Programming Example in Code:
Using a Database class:
