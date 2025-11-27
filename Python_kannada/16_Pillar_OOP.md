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
