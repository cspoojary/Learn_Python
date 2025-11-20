#  Introduction to Python Programming

## History
Python was created by Guido Van Rossum in 1989 at (WI) Netherland and released in 1991.
![Evalution of Python](https://github.com/cspoojary/Learn_Python/blob/main/image.png)

##  What is Python?
- **Python** is a **high-level**, **interpreted** programming language known for its **simplicity** and
**readability**. Key features include **dynamic typing**, **automatic memory management**
(garbage collection), a **large standard library**, and support for **multiple programming
paradigms (procedural, object-oriented, and functional)**.
- It allows developers to write clear and efficient programs for both small and large-scale projects.  
- It was created by Guido van Rossum, and released in 1991.
---
### Difference between a compiler and an interpreter.
- A compiler translates the entire source code into machine code or an intermediate code
all at once before execution. 
- An interpreter, on the other hand, translates and executes
code line by line. Python and JavaScript are examples of languages that use
interpreters, while languages like C++ and Java typically use compilers.
---

## Common Uses of Python:
- **Web Development:** Django, Flask, Fast API
- **Data Science & Machine Learning:** Pandas, NumPy, TensorFlow, Scikit-learn, Pytorch
- **Automation & Scripting:** Automating repetitive tasks  
- **Software Development:** Building applications and tools
- **IOT & Embedded System:** MicroPython,Raspberry pi

---

## What can Python do?
- Python can be used on a server to create web applications.
- Python can be used alongside software to create workflows.
- Python can connect to database systems. It can also read and modify files.
- Python can be used to handle big data and perform complex mathematics.
- Python can be used for rapid prototyping, or for production-ready software development.
---

## Why is Python Popular?

- **Easy to Learn:**  Python’s syntax is simple and close to natural language, making it ideal for beginners.  

- **Strong Community Support:**  Python has a massive global community — tons of tutorials, resources, and open-source libraries.  

- **Cross-Platform:**  Runs seamlessly on **Windows**, **macOS**, and **Linux**.  

- **Versatile:**  Python can be used for almost everything — **web apps**, **data analysis**, **AI/ML**, **automation**, and more.
  
### Why Python?
- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
- Python has a simple syntax similar to the English language.
- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
- Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object-oriented way or a functional way.

---

## Python as an Interpreted Language
Unlike other compiled languages like C or Java, Python executes the code line by line, which makes debugging easy. Python doesn't require you to compile your code into machine language; the Python interpreter takes care of it.

## Benefits of Interpreted Language:
- Easier debugging: Errors are reported line by line.
- Faster development: You can directly run the code without worrying about compiling.
  
## Key Features of Python
- Simple Syntax: Easy to read and write, similar to English.
- Interpreted: Python is executed line by line.
- Dynamically Typed: No need to declare variable types explicitly.
- Object-Oriented: Supports OOP (Object-Oriented Programming) like classes and objects.
- Rich Standard Library: Comes with lots of built-in modules and functions.

## Checking version of Python
### On Windows
```python
python --version
```
### On macOS
```python
python3 --version
```
## Good to know
- The most recent major version of Python is Python 3, which we shall be using in this tutorial.
- In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.

## Python Syntax compared to other programming languages
- Python was designed for readability, and has some similarities to the English language with influence from mathematics.
- Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
- Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

| **Parameter** | **Python 2** | **Python 3** |
| --- | --- | --- |
| **Release Year** | Debuted in **2000** | Debuted in **2008** |
| **print Functionality** | `print` is a **statement** (e.g., `print "hello"`). | `print` is a **function** (e.g., `print("hello")`). |
| **String Storage** | Default string type is **ASCII**. | Default string type is **Unicode**. |
| **Integer Division** | `5/2` → **2** (integer quotient). | `5/2` → **2.5** (floating-point result). |
| **Exception Syntax** | Uses `except Exception, e` **notation**. | Uses `except Exception as e` with **parentheses**. |
| **Global Variable Leak** | Global variables can **leak inside loops**. | Global variables are **stable** and don’t leak inside loops. |
| **Iteration Method** | Uses **`xrange()`** for efficient iteration (lazy). | Uses **`range()`**, which behaves like `xrange()` did in Python 2. |
| **Syntax Simplicity** | **More complex**, less consistent. | **Simpler** and more intuitive. |
| **Library Compatibility** | Many libraries are **not forward-compatible** with Python 3. | Libraries are written to be **strictly compatible** with Python 3. |
| **Current Usage** | **End-of-life since 2020**, rarely used today. | **Actively developed** and the community standard. |
| **Backward Compatibility** | Code can be ported to Python 3 **with effort** (e.g., `2to3`). | **Not backward compatible** with Python 2. |
| **Primary Use** | Historically used for **DevOps/legacy projects**; now obsolete. | Widely used in **software engineering, data science, AI/ML, web**, etc. |
