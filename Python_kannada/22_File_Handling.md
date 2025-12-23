# File Handling in Python
File handling allows us to read from and write to files — a common task in almost every real-world application (storing data, logs, reports, etc.).
## 📁 Why File Handling?
- To save user data permanently (like notes, records, etc.)
- To read content from a file (like student marks, exam results)
- Helps build real applications like:
  - Address books
  - Billing systems
  - Exam report generators

## 📌 Python File Modes
| Mode | Meaning | Description |
|------|--------|-------------|
| `r` | Read | Read an existing file |
| `w` | Write | Write new content (overwrites if file exists) |
| `a` | Append | Add data without deleting old content |
| `x` | Create | Create a new file (fails if file exists) |
| `b` | Binary mode | Used for images, videos, etc. |
| `t` | Text mode | Used for text files (default) |

## ✅ Opening a File
```Python
file = open("students.txt", "r")
```
### Parts:
- "students.txt" → file name
- "r" → mode (read mode)

## ✅ Reading From a File
### 1. read() – Reads entire file
```Python
file = open("notes.txt", "r")
print(file.read())
file.close()
```
### 2. readline() – Reads one line
```Python
file = open("notes.txt", "r")
print(file.readline())
file.close()
```
### 3. readlines() – Reads all lines into a list
```Python
file = open("notes.txt", "r")
lines = file.readlines()
print(lines)
file.close()
```
## ✅ Writing to a File
### rite() – Overwrites entire file
```Python
file = open("data.txt", "w")
file.write("Namaskara Bengaluru!\n")
file.write("Python is awesome!")
file.close()
```
##### 🎯 If the file exists, it clears the old content and writes fresh.
## ✅ Appending to a File
```Python
file = open("data.txt", "a")
file.write("\nThis line is added later.")
file.close()
```
##### 📌 Adds new content without deleting old content.
## ✅ Using with Statement (Best Practice)
```Python
with open("students.txt", "r") as file:
    content = file.read()
    print(content)
```
##### ✅ Automatically closes the file ✅ Clean and professional

## 🗃️ Writing List of Data to File
```Python
students = ["Ravi", "Meena", "Dinesh"]
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")
```
