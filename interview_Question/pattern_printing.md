### Print 1 To 100 
```python
for i in range(1,101):
    print(i)
```

```Python
n = 100
i = 1
while i <= n:
    print(i)
    i = i +1
```
### Printing 20 to 1
```Python
i = 20
while i > 0:
    print(i)
    i = i - 1
```
```Python
i = 1
n = 20
while i <= n:
    print(i)
    i = i +1
```
### Printing even numbers from 1 to 20
```Python
i = 1
while i <= 20:
    if i % 2 ==0:
        print(i)
    i = i+1
```
```Python
i = 0
while i <= 20:
    print(i)
    i = i + 2
```
### Printing alphabbet
```Python
a = ord('A')
while a <= ord('Z'):
    print(chr(a))
    a += 1
```
### Print multiplication of given number.
```Python
n = int(input("Enter the number: "))
i = 1
while i <= 10:
    print(n,'X',i,'=',n*i)
    i = i + 1

Enter the number: 9
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81
9 X 10 = 90
```


### Reverse
```Python
n = 512
rev = 0
while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("The reverse of the n: ",rev)

Output:
The reverse of the n:  215
```

```Python
n = 1927
rev = 0
while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("The reverse of the n: ",rev)

Output:
The reverse of the n:  7291
```

```Python
n = 9240
rev = 0
while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print(str(rev).zfill(4))

Output:
0429

```
### Digit Sum
```Python
n = 512
sum = 0
while n != 0:
    sum = sum + (n % 10)
    n = n // 10
print(sum)

Output:
8
```
```Python
n = 1927
sum = 0
while n != 0:
    sum = sum + (n % 10)
    n = n // 10
print(sum)

Output:
19
```
```Python
n = 9241
sum = 0
while n != 0:
    sum = sum + (n%10)
    n = n // 10
print(sum)

Output:
16
```
### Count of digit
```Python
n = 3429
count = 0
while n != 0:
    count = count+1
    n = n//10
print(count)

Output:
4
```
### Reverse and store in a variable
```Python
n = 512
rev = 0
while n != 0:
    rev = (rev * 10) + (n % 10)
    n = n // 10
print(rev)

Output:
215
```

```Python
n = 4536
rev = 0
while n != 0:
    rev = (rev * 10) + (n % 10)
    n = n // 10
print(rev)

Output:
6354
```

### Palindrome
```Python
n = 12321
rev = 0
temp = n
while  n != 0:
    rev = (rev * 10) + (n % 10)
    n = n // 10
if rev == temp:
    print("Number is palindrome.")
else:
    print("Number is not a palindrome.")

Output:
Number is palindrome.
```
```Python
n = 1927
rev = 0
temp = n
while n != 0:
    rev = (rev * 10)+(n % 10)
    n = n // 10
if rev == temp:
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")

Output:
Number is not palindrome.
```
