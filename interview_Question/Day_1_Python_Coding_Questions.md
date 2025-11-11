# Day 1 — Python Coding Questions: Data Types & Variables

### Swap Two Variables
```python
a = 5
b = 6

a, b = b, a
print('a=',a,'and b =',b)

a = a + b   # a = 11
b = a - b   # b = 5
a = a - b   # a = 6

print('a=',a,'and b =',b)
```

### Type Conversion
```python
str1 = "123"
print(type(str1))
intgr = int(str1)
print(type(intgr))
flt = float(str1)
print(type(flt))
```

### Data Type Identification
```python
name = 'Chaithanya'
print(type(name))
```
### Multiple Assignment
```python
a,b,c = 3,4,7
print('a =',a)
print('b =',b)
print('c =',c)
```

### Immutable vs Mutable Behavior
```python
list1 = [10,20,30]

list2 = list1

list1.append(40)

print('list1 = ',list1)
print('list2 = ',list2)
```
