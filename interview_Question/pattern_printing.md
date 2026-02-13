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
```
#### OutPut:
```Python
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
print(rev)
```
