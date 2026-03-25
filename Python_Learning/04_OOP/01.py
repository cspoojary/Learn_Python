# Encapsulation
'''
- The practice of bundling data (variables) and methods that act on that data into a single unit (a class). 
It involves hiding the internal state of an object and requiring all interaction to occur through public methods.

-  Coding: Using access modifiers like private, protected, and public, and implementing Getters and Setters.

- To understand Encapsulation, think of it as a protective "capsule" around your data. It prevents outside code from 
accidentally (or intentionally) corrupting the internal state of an object.

-  In code, we achieve this by making variables private and providing public methods (Getters and Setters) to access them. 
This allows us to add "validation logic"—for example, preventing a bank balance from being set to a negative number.

'''
class Smartphone:
    def __init__(self, model, battery_level):
        self.model = model
        # __ makes it "private"
        self.__battery_level = 0 
        
        # We use the setter even inside the constructor to ensure validation
        self.set_battery(battery_level)

    # Getter method
    def get_battery(self):
        return f"{self.__battery_level}%"

    # Setter method with validation logic
    def set_battery(self, value):
        if 0 <= value <= 100:
            self.__battery_level = value
            print(f"Battery set to {value}%")
        else:
            print("Error: Invalid battery percentage! Must be between 0 and 100.")

# --- Using the class ---

my_phone = Smartphone("Pixel 8", 85)

# 1. Trying to access private data directly will fail
# print(my_phone.__battery_level)  # This would raise an AttributeError

# 2. Using the Getter
print(f"Current charge: {my_phone.get_battery()}")

# 3. Using the Setter with invalid data
my_phone.set_battery(120)  # Logic prevents this!

# 4. Using the Setter with valid data
my_phone.set_battery(45)
print(f"New charge: {my_phone.get_battery()}")

'''
-Name Mangling: When you use __battery_level, Python internally renames it to _Smartphone__battery_level. 
You could still technically access it if you tried really hard, but the double underscore is a universal "Keep Out" sign for other developers.

The @property Decorator: In professional Python code, we often use the @property decorator to make getters and setters 
look like regular attribute access (e.g., my_phone.battery = 50 instead of calling a function). It makes the code cleaner while keeping the encapsulation logic.
'''

class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        # Use a double underscore __ to make it private
        self.__balance = initial_balance 

    # The "Getter" - allows you to read the balance
    @property
    def balance(self):
        return f"${self.__balance:,.2f}"

    # The "Setter" - allows you to modify the balance with rules
    @balance.setter
    def balance(self, amount):
        print("--- Security Check: Updating Balance ---")
        if amount < 0:
            print("Error: Balance cannot be negative!")
        else:
            self.__balance = amount
            print(f"Update successful for {self.owner}.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: {self.balance}")
        else:
            print("Deposit must be a positive amount.")

# --- Execution ---
my_account = BankAccount("Sarah", 1000)

# 1. Accessing via the getter (looks like a variable, but it's a method!)
print(f"Initial balance: {my_account.balance}")

# 2. Trying to set a negative balance (The setter blocks this)
my_account.balance = -500 

# 3. Depositing money (Internal logic updates the private __balance)
my_account.deposit(250)

# 4. Trying to access private data directly (This will crash)
# print(my_account.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'

'''
- Data Integrity: You cannot set the balance to a negative number or a string. The setter acts as a gatekeeper.

- Implementation Hiding: The user of the class doesn't need to know that the balance is stored as a float or an integer; 
they just see the formatted string returned by the @property.

- Read-Only Options: If you wanted the balance to be strictly read-only, you would simply provide the @property (getter) 
and delete the @balance.setter. Then, the balance could never be changed from outside the class!
'''