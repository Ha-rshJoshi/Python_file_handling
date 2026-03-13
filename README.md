# 📂 Python File Handling & Modules Lab

A Python lab project demonstrating **file handling, custom modules, module importing techniques, packages, and module reloading**.

This project is useful for beginners learning how Python programs interact with files and how modules are created, imported, and reused.

---

# 📌 Objectives

The main goals of this project are:

* Learn how to **read data from text files**
* Count **number of lines and characters in a file**
* Create and use **custom Python modules**
* Understand different **import methods**
* Automatically execute code using `__name__ == "__main__"`
* Work with **client modules**
* Learn **package imports**
* Experiment with **module reloading**

---

# 🗂 Project Structure

```
Python-File-Handling-Lab
│
├── sample.txt          # Example text file
├── readfile.py         # Reads entire text file
├── mymod.py            # Custom module with counting functions
├── myclient.py         # Client program that imports mymod
└── mypkg
    └── mymod.py        # Module placed inside a package
```

---

# 🧾 Exercise Description

## 1️⃣ Read an Entire Text File

This program reads and prints the full contents of a text file.

### File

```
readfile.py
```

### Features

* Opens a file in **read mode**
* Reads entire file content
* Displays content on screen

---

# 2️⃣ Custom Python Module

A module called **mymod.py** is created containing three functions.

### Functions

### `countLines(filename)`

Counts the total number of lines in the file.

### `countChars(filename)`

Counts the total number of characters in the file.

### `test(filename)`

Calls both functions to display results.

Example:

```
Number of lines: 5
Number of characters: 120
```

---

# 3️⃣ Testing the Module

The module can be tested using different import styles.

### Method 1 – Normal Import

```python
import mymod
mymod.test("sample.txt")
```

### Method 2 – Specific Import

```python
from mymod import countLines
countLines("sample.txt")
```

### Method 3 – Import All

```python
from mymod import *
test("sample.txt")
```

---

# 4️⃣ Running Module as Script

The module includes:

```python
if __name__ == "__main__":
    test("sample.txt")
```

This ensures that:

* The test function runs **only when the module is executed directly**
* It does **not run when imported**

---

# 5️⃣ Client Module

A second module called **myclient.py** imports and tests the functions from `mymod`.

### Example

```python
import mymod

mymod.countLines("sample.txt")
mymod.countChars("sample.txt")
```

This demonstrates how **one Python program can use another module**.

---

# 6️⃣ Package Import

A package called **mypkg** is created and the module is placed inside it.

Directory structure:

```
mypkg/
   mymod.py
```

Import example:

```python
import mypkg.mymod

mypkg.mymod.test("sample.txt")
```

This demonstrates **Python package imports**.

---

# 7️⃣ Module Reload Experiment

Python modules can be **reloaded without restarting the interpreter**.

Example:

```python
import importlib
import mymod

importlib.reload(mymod)
```

This is useful when **editing a module while testing it**.

---

# 🛠 Technologies Used

* Python 3
* File Handling
* Python Modules
* Python Packages

---

# ▶ How to Run the Project

1️⃣ Clone the repository

```
git clone https://github.com/yourusername/python-file-handling-lab.git
```

2️⃣ Open the folder

```
cd python-file-handling-lab
```

3️⃣ Run the programs

```
python readfile.py
python mymod.py
python myclient.py
```

---

# 📚 Learning Outcomes

After completing this project you will understand:

* Python **file handling**
* Creating **reusable modules**
* Different **module import techniques**
* Working with **packages**
* Running modules as **scripts**
* Reloading modules during development

---

# 👨‍💻 Author

**Harsh Joshi**

Python Programming Lab – File Handling & Modules
