## ENCAPSULATION
- Encapsulation means hiding internal details of a class and only exposing what’s necessary.
- It helps to protect important data from being changed directly and keeps the code secure and organized.
---
We can make variable private inside class by keeping __(name_of_attribute) like this.It cannot accesses directly from outside the class.
```Python
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

emp = Employee("Chaithanya", 50000)
print(emp.name)       
print(emp.__salary)
```
Output:
```Python
Chaithanya
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 8, in <module>
AttributeError: 'Employee' object has no attribute '__salary'
```
Explanation:
- self.name = name: Public attribute, can be accessed directly.
- self.__salary = salary: Private attribute, cannot be accessed directly.
- print(emp.name): Prints "Fedrick" because name is public.
- print(emp.__salary): Raises an error because __salary is private and hidden.

Why do we need Encapsulation?
- Protects data from unauthorized access and accidental modification.
- Controls data updates using getter/setter methods with validation.
- Enhances modularity by hiding internal implementation details.
- Simplifies maintenance through centralized data handling logic.
- Reflects real-world scenarios like restricting direct access to a bank account balance.

## Types of Access Modifier
- Public
- Protected
- Private

### Public 
- Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. By default, all members in Python are public.
- They are defined without any underscore prefix (e.g., self.name).

Example: This example shows how a public attribute (name) and a public method (display_name) can be accessed from outside the class using an object.
```Python
class Employee:
    def __init__(self, name):
        self.name = name  #public attributes

    def display_name(self):    #public mathod
        print(self.name)

emp = Employee("Chaithanya")
emp.display_name()
print(emp.name)
```
Output:
```Python
Chaithanya
Chaithanya
```
Explanation:
- self.name: Declared without underscores, so it is public.
- display_name(): Public method that prints the value of the public attribute.
- emp.name: Directly accessed from outside the class, showing public members are fully accessible.

### Protected
- Protected members are variables or methods that are intended to be accessed only within the class and its subclasses. They are not strictly private but should be treated as internal.
- In Python, protected members are defined with a single underscore prefix (e.g., self._name).

Example: This example shows how a protected attribute (_age) can be accessed within a subclass, demonstrating that protected members are meant for use within the class and its subclasses.
```Python
class Employee:
    def __init__(self, name, age):
        self.name = name    #public
        self._age = age    #protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age: ",self._age) #Accessible in subclass
emp = SubEmployee("Chethan", 25)
print(emp.name)    #Public accessible
emp.show_age()    # Protected accessed through subclass
```
Output:
```
Chethan
Age: 25
```
Explanation:
- self._age: Defined with a single underscore, marking it as protected.
- SubEmployee: Inherits from Employee and can access _age directly.
- Protected members should not be accessed outside the class hierarchy, but Python does not enforce this rule strictly.

### Private
- Private members are variables or methods that cannot be accessed directly from outside the class. They are used to restrict access and protect internal data.
- In Python, private members are defined with a double underscore prefix (e.g., self.__salary). - Python applies name mangling by internally renaming them (e.g., __salary becomes _ClassName__salary) to prevent direct access.

Example: This example shows how a private attribute (__salary) is accessed within the class using a public method, demonstrating that private members cannot be accessed directly from outside the class.
```Python
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Chaithanya", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly
```
Output
```Python
Chaithanya
Salary: 60000
```
Explanation:
- self.__salary: Defined with double underscores, so it is private.
- show_salary(): A public method that provides safe access to the private attribute.
- Attempting emp.__salary causes an AttributeError, proving private members cannot be accessed directly.
  
Declaring Protected and Private Methods
In Python, you can control method access levels using naming conventions:
- Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses.
- Use a double underscore (__) to define a private method accessible only within class due to name mangling.

Example: This example demonstrates how a protected method (_show_balance) and a private method (__update_balance) are used to control access. The private method updates balance internally, while protected method displays it. Both are accessed via a public method (deposit), showing how Python uses naming conventions for encapsulation.
```Python
class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}")  # Protected method

    def __update_balance(self, amount):
        self.balance += amount             # Private method

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance()           # Accessing protected method
        else:
            print("Invalid deposit amount!")
            
account = BankAccount()
account._show_balance()      # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)         # Uses both methods internally
```
Output
```Python
Balance: ₹1000
Balance: ₹1500
```
Explanation:
- _show_balance(): (Protected method) Accessible from outside, but intended for internal or subclass use.
- __update_balance(): (Private method) Only accessible inside class due to name mangling.
- deposit(): Public method that safely uses both private and protected methods.
---
## Getter and Setter Methods
getter and setter methods are used to access and modify private attributes safely. Instead of accessing private data directly, these methods provide controlled access, allowing you to:
- Read data using a getter method.

### Example: 
- This example shows how to use a getter and a setter method to safely access and update a private attribute (__salary).
- Update data using a setter method with optional validation or restrictions.
```Python
class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)   # Update salary using setter
print(emp.get_salary())
```
Output
```Python
50000
60000
```
