# Menu-Driven Programs in Python

## Introduction
- A menu-driven program is a program that allows users to interact by choosing options from a menu.
- These programs are commonly used in applications such as banking systems, shopping carts, or command-line utilities.
- Menu-driven programs are typically implemented using loops and conditional statements (if-elif-else).

---
## Why Use Menu-Driven Programs?
1. Interactive: Provides a user-friendly way to interact with programs.
2. Reusable: Can be easily modified or extended by adding new menu options.
3. Efficient: Reduces the need for users to remember commands by presenting them with a list of options.

---
## Steps to Create a Menu-Driven Program
1. Display the Menu: Use print() statements to display a list of options.
2. Take User Input: Use input() to capture the user's choice.
3. Process the Choice: Use conditional statements to execute actions based on the user's input.
4. Repeat Until Exit: Use a loop (while) to keep displaying the menu until the user chooses to exit.

---
## Basic Structure of a Menu-Driven Program
```Python
def menu():
    print("Welcome to the Menu-Driven Program!")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print("You selected Option 1.")
    elif choice == '2':
        print("You selected Option 2.")
    elif choice == '3':
        print("You selected Option 3.")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```
