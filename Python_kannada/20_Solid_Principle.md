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
❌ Bad Example:
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
