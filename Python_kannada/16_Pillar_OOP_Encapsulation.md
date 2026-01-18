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
