---
title: EX | Installing Libraries
toc: TRUE
toc_float: TRUE
collapsed: TRUE
smooth_scroll: TRUE
header:
  image: /assets/images/unit_images/u05/header.png
  image_description: "work environment"
  caption: "Photo by [Lukas Goumbik](https://pixabay.com/de/users/Goumbik-3752482/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2055522) from [Pixabay](https://pixabay.com)"
---

## **What are Libraries?**

In programming, libraries are collections of pre-written code that provide reusable functions, classes, and methods to perform common tasks. Libraries can significantly simplify your development process by allowing you to leverage existing solutions rather than writing code from scratch. They cover a wide range of functionalities such as data manipulation, machine learning, web development, and more.

## **Why Do We Need Libraries?**

Libraries are essential for several reasons:

1. **Efficiency**: Libraries save time by providing pre-built functions and modules, allowing you to focus on the unique aspects of your project.
2. **Reliability**: Libraries are often tested and optimized by a large community of developers, ensuring robust and efficient code.
3. **Consistency**: Using libraries promotes consistency in your codebase, making it easier to read, maintain, and collaborate with others.
4. **Functionality**: Libraries offer advanced features and capabilities that would be complex and time-consuming to implement on your own.

---

## **Built-in Libraries in Python**

When you install Python, it already comes with many built-in libraries that are ready to use — no additional installation required. These are part of the **Python Standard Library**.

#### Example:
```python
import math

print(math.sqrt(25))  # Output: 5.0
```

Other built-in libraries include: `os`, `datetime`, `random`, `json`, `sys`, and more.

---

## **Installing Python Libraries in Visual Studio**

Visual Studio provides tools to manage Python environments and install libraries using the built-in `pip` package manager.

This uses `pip` under the hood and installs the package into the selected environment.

---

### Use the Terminal to Install Libraries

You can install Python libraries either directly inside **Visual Studio Code** or using the **Command Prompt** (cmd). Depending on where your Python interpreter is installed, you may need administrator rights.

---

#### Inside Visual Studio Code (VS Code)

1. Open **Visual Studio Code**.
2. Go to **View → Terminal**.
3. In the terminal, install libraries using `pip`:
   ```sh
   pip install numpy 
   ```

---

#### Use the Command Prompt (cmd)

1. Press <kbd>Win</kbd> + <kbd>R</kbd>, type `cmd`, and hit Enter.
2. Install packages as usual:
   ```sh
   pip install pandas
   ```

---

#### 🔐 Important: Run as Administrator if Python is in C:\ProgramData

If your Python interpreter is installed in a system-wide location like:
  ```
  C:\Program Files\Python39\python.exe
  ```

Then `pip install` may **fail without admin rights**. In that case:

1. **Right-click** on the Command Prompt or VS Code icon.
2. Select **"Run as administrator"**.
3. Then install the library again:
   ```sh
   pip install matplotlib
   ```

---

##  After Installing: How to Use a Library in Your Python Script

Once a library is installed, you can import it in your code using the `import` statement.

#### Example:
```python
import pandas as pd

data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})

print(data)
```