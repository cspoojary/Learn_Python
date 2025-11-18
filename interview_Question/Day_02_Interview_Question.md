## 1.Write a Python program that prints using while loop: 
  ### a) The first 10 even numbers 
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
  ### b) The first 10 odd numbers 
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
  ### c) The first 10 natural numbers 
```Python
num = 1
print("The first 10 naturals numbers:" )
while num <= 10:
    print(num)
    num = num + 1
```

  ### d) The first 10 whole numbers
```Python
num  = 0
count = 1
print("The first 10 whole numbers: ")
while count <= 10:
    print(num)
    num = num + 1
    count = count + 1
```
