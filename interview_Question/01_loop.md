### 1.Write a Python program that prints using while loop: 
  #### a) The first 10 even numbers 
```Python
num = 1
count = 1
print("The first 10 Even number is: ")
while count <= 10:
    if num % 2 == 0:
        print(num)
        count = count + 1
    num = num + 1
```
  #### b) The first 10 odd numbers 
```Python
num = 1
count = 1
print("The first 10 odd number: ")
while count <= 10:
    if num %2 != 0:
        print(num)
        count = count+1
    num = num + 1
```
