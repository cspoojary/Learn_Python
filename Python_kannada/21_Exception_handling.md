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
