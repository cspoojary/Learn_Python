# Polymorphism
'''
In the world of Object-Oriented Programming (OOP), polymorphism is the ability of different classes to be treated as instances of the same class through inheritance. 
The word itself comes from Greek, meaning "many shapes" (poly = many, morph = form).

Simply put, polymorphism allows a single interface (like a method name) to represent different underlying forms (different implementations).

1. Static Polymorphism (Compile-time)

- This occurs when the compiler determines which method to call at the time of compilation. The most common form is Method Overloading.

- Method Overloading: Defining multiple methods with the same name but different parameters (different types or number of arguments).
  Example: A multiply() function that can handle two integers, or three integers, or two decimals.

  
2. Dynamic Polymorphism (Runtime)
This is the most powerful form of polymorphism. It occurs when the specific method to be executed is determined at runtime. This is achieved through Method Overriding.

Method Overriding: A subclass provides a specific implementation of a method that is already defined in its parent class.

The "Interface" Concept: You can have a list of different objects and call the same method on all of them, and each will respond in its own unique way.
'''

'''
The Banking Example
In this scenario:

Overloading is used to allow a deposit to be made either as a simple amount or with an added "description" tag.

Overriding is used to change how withdraw works for a Savings Account (which might have a limit) vs. a standard Account.
'''
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    # 1. METHOD OVERLOADING (via Default Arguments)
    # Allows depositing with or without a memo/note
    def deposit(self, amount, memo=None):
        self.balance += amount
        if memo:
            print(f"Deposited: ${amount} ({memo}). New Balance: ${self.balance}")
        else:
            print(f"Deposited: ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew: ${amount}. New Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    # 2. METHOD OVERRIDING
    # Savings accounts have a rule: cannot withdraw more than the balance
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Transaction Denied: Insufficient funds for amount ${amount}")
        else:
            # 'super()' calls the original method from BankAccount
            super().withdraw(amount)

# --- Execution ---

# Demonstrating Overloading
basic_acct = BankAccount(1000)
basic_acct.deposit(500)                 # Simple call
basic_acct.deposit(200, "Birthday Gift") # Call with extra argument

print("---")

# Demonstrating Overriding
savings = SavingsAccount(500)
savings.withdraw(1000) # This triggers the OVERRIDDEN logic (Denied)
savings.withdraw(100)  # This works normally