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
