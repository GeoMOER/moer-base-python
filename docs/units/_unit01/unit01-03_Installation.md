---
title: "Ex | Installation"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "Python und Visual Studio Code Logos nebeneinander"
  caption: "Installation Guide für Python und VS Code"
---

<!--more-->

## Guide for Python and Visual Studio Code

### **Step 1: Download and Install Python**

1. **Go to the Python download page**  
   - Visit the official [Python download page](https://www.python.org/downloads/).

2. **Download the appropriate installer**  
   - Choose the correct version for your operating system:
     - **Windows**: `.exe` installer (64-bit recommended)  
     - **macOS**: `.pkg` file  
     - **Linux**: Python is often pre-installed; otherwise, install it via the package manager (`apt`, `dnf`, `yum`, etc.).

3. **Start the installation**  
   - Run the installer.
   - **Important**: Check the box **"Add Python to PATH"**.
   - Click "Install Now" or "Customize Installation" if you need to adjust specific settings.

4. **Verify the installation**  
   - Open a terminal or command prompt and enter:
     ```sh
     python --version
     ```
   - If the command does not work, restart your computer and check if Python is added to the PATH.

---

### **Step 2: Download and Install Visual Studio Code**

1. **Go to the Visual Studio Code download page**  
   - Visit the [official VS Code download page](https://code.visualstudio.com/Download).

2. **Download the appropriate installer**  
   - Choose the correct installer for your operating system:
     - Windows: `.exe`
     - macOS: `.zip` or `.dmg`
     - Linux: `.deb` or `.rpm`

3. **Start the installation**  
   - Run the installer and follow the instructions.
   - **Windows users**: Enable the option **"Add to PATH"** if available.

4. **Verify the installation**  
   - Open a terminal or command prompt and enter:
     ```sh
     code --version
     ```
   - If VS Code starts or displays the version, the installation was successful.

---

### **Step 3: Install Extensions in Visual Studio Code**

#### **1. Install the Python extension**

1. **Open Visual Studio Code**.
2. **Open the Extensions view**  
   - Click on the **Extensions icon** or press `Ctrl+Shift+X`.
3. **Search for the Python extension**  
   - Type "Python" in the search bar.
   - Select the **Python** extension by **Microsoft** and click **Install**.

#### **2. Install the Jupyter extension**

1. **Open the Extensions view** (`Ctrl+Shift+X`).
2. **Search for the Jupyter extension**  
   - Type "Jupyter" in the search bar.
   - Select the **Jupyter** extension by **Microsoft** and install it.

### **3. Additional Tests After Installation**
**Run Python in VS Code**

1. Open VS Code.
2. Create a new file `test.py` with the following content:
   ```python
   print("Hello, world!")
   ```
3. Press `F5` or go to **Run** → **Run Python File**.

**Test Jupyter Notebook**

1. Open VS Code.
2. Create a new file `test.ipynb`.
3. Add a new cell and write:
   ```python
   print("Jupyter Notebook is running!")
   ```
4. Run the cell.


#### **4. Check and Select the Python Interpreter in VS Code**

After installing Python and Visual Studio Code, it’s important to make sure the correct Python interpreter is selected.

**Use the Command Palette**

1. Open VS Code.
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the **Command Palette**.
3. Type `Python: Select Interpreter` and hit Enter.
4. Select the interpreter you want to use (e.g. a global install, virtual environment, or Conda environment).
5. VS Code will remember your selection per workspace/project.


**💡 Why this is powerful:**

One of the **biggest advantages of VS Code** is that you can assign a **different Python interpreter or environment per project**.  
This means:
- Different Python versions for different projects
- Clean and isolated environments (especially useful for data science or academic projects)
- No interference between project dependencies


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
