# SOLID Principles in Python
The SOLID principles are five guidelines that help us write clean, maintainable, and scalable object-oriented code. These are best practices followed by experienced developers to make code better.
- S – Single Responsibility Principle
- O – Open/Closed Principle
- L – Liskov Substitution Principle
- I – Interface Segregation Principle
- D – Dependency Inversion Principle
We’ll go through each one with simple, beginner-friendly examples.

---
## 1. Single Responsibility Principle (SRP)
Definition: A class should have only one reason to change. That means, a class should do only one job.
### ❌ Bad Example:
```Python
class Student:
    def __init__(self, name):
        self.name = name

    def save_to_database(self):
        print("Saving to database...")

    def generate_report_card(self):
        print("Generating report card...")
```
This class is handling both data storage and report generation. Too many responsibilities!

---
### ✅ Good Example:
```Python
class Student:
    def __init__(self, name):
        self.name = name

class StudentDatabase:
    def save(self, student):
        print(f"Saving {student.name} to database...")

class ReportCard:
    def generate(self, student):
        print(f"Generating report card for {student.name}...")
```
Now each class has one job: Student handles data, StudentDatabase saves, ReportCard generates.

---
## 2. Open/Closed Principle (OCP)
Definition: Software entities (classes, functions, etc.) should be open for extension but closed for modification.

### ❌ Bad Example:
```Python
class Discount:
    def get_discount(self, customer_type):
        if customer_type == "regular":
            return 10
        elif customer_type == "premium":
            return 20
```
If we add a new customer type (e.g., VIP), we need to modify this class.

---
### ✅ Good Example:
```Python
class Discount:
    def get_discount(self):
        return 0

class RegularCustomer(Discount):
    def get_discount(self):
        return 10

class PremiumCustomer(Discount):
    def get_discount(self):
        return 20
```
You can now add more customer types by extending, not modifying the existing code.

---
## 3. Liskov Substitution Principle (LSP)
Definition: Subclasses should be able to replace their parent class without breaking the program.

### ❌ Bad Example:
```Python
class Bird:
    def fly(self):
        print("Flying...")

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")
```
Penguin violates LSP because it can’t actually replace Bird.

---
### ✅ Good Example:
```Python
class Bird:
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying...")

class Penguin(Bird):
    def move(self):
        print("Swimming...")
```
Now, both follow LSP because they behave correctly when used as a Bird.

---
## 4. Interface Segregation Principle (ISP)
- Definition: Don’t force a class to implement methods it does not use.
- Python doesn’t have interfaces like Java/C#, but we can still follow this idea using base classes.

### ❌ Bad Example:
```Python
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Robot(Worker):
    def eat(self):
        raise NotImplementedError("Robots don't eat")
```
Robot shouldn’t be forced to have eat().

---
### ✅ Good Example:
```Python
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Workable):
    def work(self):
        print("Robot working")
```
Now, each class only implements the methods it really needs.

---

## 5. Dependency Inversion Principle (DIP)
Definition: High-level modules should not depend on low-level modules. Both should depend on abstractions.
### ❌ Bad Example:
```Python
class Keyboard:
    def input(self):
        return "User typing..."

class Computer:
    def __init__(self):
        self.keyboard = Keyboard()

    def get_input(self):
        return self.keyboard.input()
```
Computer is tightly coupled to Keyboard.

---
## ✅ Good Example:
```Python
