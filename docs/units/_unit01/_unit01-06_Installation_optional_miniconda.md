---
title: "EX | Installation"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "Python und Visual Studio Code Logos nebeneinander"
  caption: "Installation Guide für Python und VS Code"
---

<!--more-->



### **(Optional): Install Miniconda**

*Miniconda is optional but useful if you're working in Data Science, AI, or scientific computing.*

#### **What is Miniconda?**
Miniconda is a minimal version of Anaconda. It allows you to create isolated Python environments and install scientific packages more easily.

#### **Install Miniconda**

1. **Download Miniconda**  
   - [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

2. **Run the installer**  
   - For Windows, you may select "Add Miniconda to my PATH environment variable" (only if you are not using another Python version).

3. **Verify the installation**  
   - Open a terminal and run:
     ```bash
     conda --version
     conda create -n myproject python=3.11
     conda activate myproject
     ```


#### (Optional): Use Miniconda with VS Code

Miniconda works seamlessly with Visual Studio Code and is ideal for creating isolated environments with specific Python versions and packages.


1. **Create a new environment**  
   Open your terminal (or Anaconda Prompt on Windows):
   ```bash
   conda create -n myenv python=3.11
   conda activate myenv
   ```

2. **Install packages (optional)**  
   You can install packages like numpy or pandas:
   ```bash
   conda install numpy pandas
   ```

3. **Launch VS Code from the same terminal**  
   This ensures the environment is automatically detected:
   ```bash
   code .
   ```

4. **Or manually select the environment in VS Code**  
   - Open VS Code
   - Press `Ctrl+Shift+P` → `Python: Select Interpreter`
   - Choose the one that looks like: `Python 3.11.x ('myenv': conda)`

---

With this setup, you can work efficiently on multiple Python projects, each with its own isolated environment.
