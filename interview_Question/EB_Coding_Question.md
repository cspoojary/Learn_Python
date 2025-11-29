#### 1. Write a program to find the factorial of a number using a loop.
### FOR LOOP
```Python
n = int(input("Enter the number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f"The Factorial of {n} is {fact}.")
```
