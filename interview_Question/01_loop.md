## WHILE LOOP 
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

  #### c) The first 10 natural numbers 
```Python
num = 1
print("The first 10 naturals numbers:" )
while num <= 10:
    print(num)
    num = num + 1
```
 #### d) The first 10 whole numbers
```Python
num  = 0
count = 1
print("The first 10 whole numbers: ")
while count <= 10:
    print(num)
    num = num + 1
    count = count + 1
```

### 2. Write a Python program that prints the first 10 integers and their squares using a while loop .
```Python
num = 1
print("The first 10 integers and their squares are:")
while num <= 10:
    print("Integer is",num,"and its square is",num**2)
    num = num+1
```
### 3. Write for loop statement to print the following series: 105,98,91 ……. 7 
```Python
count = 105
while count > 0:
    print(count,end=' ')
    count = count - 7
```
or

```Python
for i in range(105,0,-7):
    print(i, end = ' ')
```
### 4. Write a Python program that print  first 10 natural numbers using while loop in reverse order.
```Python
num = 10
count = 1
print("The first 10 natural number in the reverse order.")
while count <= 10:
    print(num)
    num = num - 1
    count = count + 1
```
### 5.write a program to print table of a number entered from the user.
```Python
num = int(input("Enter number of the table:"))
length_of_table = int(input("how much row you need: "))
count = 1
while count <= length_of_table:
    print(num,'x',count,'=',num*count)
    count = count + 1
```
### 6.prime or not using while For loop.
```Python
num = int(input("Enter the number: "))

if num > 1:
    i = 2
    while i < num:
        if num % i == 0:
            print(num,'is not a prime number.')
            break
        i += 1
    else:
        print(num,'is a prime number.')
else:
    print(num,"is not a prime number.")
```
## FOR LOOP
### 1: Python program to print a multiplication table of a given number.
```Python
num = int(input("Enter the number of the table:"))
length_of_table = int(input("Enter the length of the table."))
for n in range(1,length_of_table+1):
    print(num,'x',n,'=',num*n)
```
### 2: Python program to count the total number of digits in a number.
```Python
num = input("Enter the number: ")
count = 0

for n in num:
    count = count + 1
print("The length of the digit:",count)
```
