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
## Difference between a compiler and an interpreter.
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
  
## Why Python?
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

---
## Key Features of Python
Python is a high-level, interpreted programming language known for its simplicity and readability. Key features include dynamic typing, automatic memory management (garbage collection), a large standard library, and support for multiple programming paradigms (procedural, object-oriented, and functional).

- Types of Languages
  - Low-Level Language
Machine language consists of binary code that directly corresponds to the instructions executed by the CPU.
0s and 1s executed directly by the CPU.
    - **Characteristics:** Extremely fast, hardware-specific.
    - **Not portable:** code depends on CPU architecture, Harder to learn and maintain.
    - **Examples:** Pure machine language (binary opcodes).
  
- **High-Level Language**
High-level programming languages use human-readable code
and require compilation or interpretation before execution.
**Characteristics:**
    - Use natural English-like syntax.
    - Portable across operating systems.
    - Automatic memory management (mostly).
    - Require a compiler or interpreter to convert to machine code.
**Examples:**
  **Python** (simple syntax, dynamic typing)
  **Java** (object-oriented, runs on JVM)
  **Python ,JavaScript**

### Compiler
A compiler translates the entire source code into machine code or an intermediate code while languages like C++ and Java typically use compilers.
- Checks all errors before running.
- Program runs faster after compilation.

### Interpreter
An interpreter translates and execute  code line by line.Python and JavaScript are examples of languages that use interpreters.
- Easier debugging; errors show immediately when a faulty line runs.
- Slower than a compiled program.

### Assembler:
Converts **assembly language** instructions  into machine code (binary).
Low-level hardware programming, embedded systems.

### Dynamically typed
You don’t need to declare variable types explicitly. Type is determined at runtime.

### Automatic Memory Management (Garbage Collection)
Python keeps track of objects you create and automatically frees memory that’s no longer in use, so you rarely need to handle memory manually.

### Debugging
Debugging is the process of identifying and fixing errors, or bugs, in a program. It is
crucial in programming because it ensures that the software functions correctly and
produces the desired results.

### Algorithm
An algorithm is a step-by-step procedure or set of instructions for solving a particular problem or performing a specific task. It is a fundamental concept in programming and is used to design and implement solutions in code.

### PEP8 - Program Enhancement Proposal.
PEP 8 is the Python Enhancement Proposal that defines the style guide for writing
Python code. It promotes consistency and readability by specifying conventions for
naming, indentation, and code structure. Adhering to PEP 8 helps maintain clean and
maintainable code.

### PATH environment
The purpose of the PATH environment variable during Python installation
on Windows specifies a list of directories where executable files are located. Adding Python's installation directory to the PATH allows you to run Python from any command prompt without specifying the full path to the Python executable.

### Translator:
A translator is software that converts human-readable source code into machine-readable instructions that the computer can understand and execute.
- Compiler
- interpreter
- Assembler

### Python Paradigm:
A  Paradigm is a styleot approach to structuring and thinking about code
- Procedural (Imperative) Programming: Code is organized into procedures or functions that run step by step.

def greet():
    print("Hello!")
greet()

- Object-Oriented Programming (OOP):
  Focuses on creating **objects** (data + behavior) using classes.

class Dog:
    def bark(self):
        print("Woof!")
d = Dog()
d.bark()

- Functional Programming:
Treats computation as evaluation of **pure functions** and avoids changing state.

Uses higher-order functions, `map`, `filter`, `lambda`.
```Python
nums = [1, 2, 3]
squares = list(map(lambda x: x**2, nums))
```
---

### .py and .pyc

**.py**

- Contains the original Python source code you write.
- Human-readable and editable with any text editor.
- Executed directly by the Python interpreter.

**.pyc**

- Compiled bytecode version of a `.py` file.
- Generated automatically inside the `__pycache__` folder.
- Used by Python for faster module loading during imports.

---

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

---

## Difference between Python2 and Python 3

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

