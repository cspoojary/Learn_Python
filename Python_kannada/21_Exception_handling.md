# Errors and Exception Handling in Python

## What is an Error?
- An error is a problem in a program that stops the execution.
- Errors can happen due to:
  - Wrong code
  - Unexpected input
  - External factors (like missing files, network issues)
## Two Types of Errors in Python
| Type           | Meaning                                                                 |
|----------------|-------------------------------------------------------------------------|
| Syntax Errors  | Mistakes in the code structure (missing colon, brackets, etc.)          |
| Exceptions     | Errors that happen during execution (e.g., divide by zero)              |

##  Example of Syntax Error
```Python
if True:
  print("Hello")
```
Output:
```Python
SyntaxError: expected ':'
```
## Example of Runtime Exception
```Python
a = 10
b = 0
print(a / b)
```
Output:
```Python
ZeroDivisionError: division by zero
```
## Common Exception Types in Python
Here’s a table of frequently occurring exceptions you might see:
| Exception Name       | When it Happens                                   | Example Code              |
|----------------------|--------------------------------------------------|---------------------------|
| ZeroDivisionError    | Divide by 0                                      | `10 / 0`                  |
| TypeError            | Wrong data type used                             | `"2" + 2`                 |
| ValueError           | Correct type but wrong value                     | `int("abc")`              |
| IndexError           | List index out of range                          | `my_list[10]`             |
| KeyError             | Accessing missing key in dictionary              | `my_dict["not_found"]`    |
| AttributeError       | Accessing non-existent attribute or method       | `5.append(2)`             |
| ImportError          | Module not found                                 | `import somethingfake`    |
| NameError            | Using variable not defined                       | `print(x)`                |
| FileNotFoundError    | Trying to open a file that doesn’t exist          | `open("missing.txt")`     |

## What is Exception Handling?
Exception Handling is a way to protect your program from crashing when an error occurs.
