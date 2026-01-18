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
