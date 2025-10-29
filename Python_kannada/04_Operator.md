# Operators in Python

## 1. Assignment Operators
Assignment operators are used to assign values to variables.  
The simplest one is `=` which assigns the value on the right to the variable on the left.  
There are also compound assignment operators that combine arithmetic operations with assignment.

### Common Assignment Operators:
| Operator | Description |
|-----------|--------------|
| =  | Assigns value on the right to the variable on the left |
| += | Adds right operand to the left operand and assigns the result |
| -= | Subtracts the right operand from the left operand and assigns the result |
| *= | Multiplies the left operand by the right operand and assigns the result |
| /= | Divides the left operand by the right operand and assigns the result |
| %= | Takes modulus of left operand by right operand and assigns the result |

### Example:
```python
x = 5   # Assigns 5 to x
x += 3  # Equivalent to x = x + 3, now x is 8
x -= 2  # Equivalent to x = x - 2, now x is 6
x *= 4  # Equivalent to x = x * 4, now x is 24
x /= 6  # Equivalent to x = x / 6, now x is 4.0

print(x)

