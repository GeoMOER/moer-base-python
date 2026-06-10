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

In programming, *libraries* are collections of pre-written code that provide reusable functions, classes, and methods to perform common tasks.  
They help you avoid rewriting standard functionality and instead focus on the logic of your own project.  
Python offers thousands of libraries for topics such as data processing, visualization, web development, and machine learning.

---

## **Why Do We Need Libraries?**

Libraries are important because they:

1. **Save time** – You can use ready-made solutions instead of coding everything from scratch.  
2. **Increase reliability** – Most libraries are well-tested and maintained by large communities.  
3. **Ensure consistency** – Using standard libraries keeps your code easy to understand and maintain.  
4. **Expand functionality** – Libraries give you access to advanced tools and algorithms.

---

## **Built-in Libraries in Python**

When you install Python, it already comes with a large *Standard Library*.  
These libraries are available immediately—no installation required.

#### Example:
```python
import math

print(math.sqrt(25))  # Output: 5.0
```

Other built-in libraries include: `os`, `datetime`, `random`, `json`, and `sys`.

---

## **Installing External Libraries**

If you need functionality that is not part of the standard library, you can install additional libraries from the Python Package Index (PyPI) using the tool **pip**.

You can run `pip` from:

- the **Terminal** (on Windows, macOS, or Linux)

---

### 🧩 Option 1: Install via Terminal

1. Open the **Command Prompt** (Windows) or **Terminal** (macOS/Linux).  
2. Type for example:
   ```bash
   pip install pandas
   ```
3. Wait until the installation completes successfully.

> 💡 On some systems, you may need to use `pip3` instead of `pip`.


---

### 🔐 Note on Administrator Rights

If Python is installed system-wide (for example under `C:\Program Files\Python39`),  
`pip install` may fail without admin rights.  
In that case:
1. Open the Command Prompt **as Administrator**, or  
2. Install the library for your user only:
   ```bash
   pip install --user numpy
   ```

---

## **After Installing: Using a Library in Your Code**

Once a library is installed, you can import it and use its functions:

```python
import pandas as pd

data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})

print(data)
```

---

✅ **Summary**

- Python already includes many useful libraries.  
- You can install more using `pip`.  
- In Jupyter Notebook, use `!pip install library_name`.  
- Always restart the kernel after installing new packages.
