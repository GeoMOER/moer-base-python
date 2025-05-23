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
   
5. **Check the Python Path**  
To find out which Python version your system is using (and where it is installed), you can follow these steps:

   - Windows (Command Prompt or PowerShell).
     Open the **Command Prompt** or **PowerShell** (e.g., with `Win + R`, then type `cmd` or `powershell` and press Enter).
   ```
   #Enter the following command:
   where python
   ```
   You will get one or more paths, for example:
   ```
   C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe
   C:\Program Files\Python39\python.exe
   ```
   The **first path** listed is the Python interpreter your system uses by default.
   
   - macOS / Linux (Terminal).
    Open the **Terminal** and enter the following command:
   ```
   which python
   # or on newer systems:
   which python3
   # You will see something like:
   /usr/bin/python3
   /opt/homebrew/bin/python3
   ```
   The displayed path shows the active interpreter your system is using.

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
3. Press `Ctrg + Alt + N` or go to **Run** → **Run Python File**.

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
2. Press `Ctrl+Shift+P` to open the **Command Palette**.
3. Type `Python: Select Interpreter` and hit Enter.
4. Select the interpreter you want to use (e.g. a global install, virtual environment, or Conda environment).
5. VS Code will remember your selection per workspace/project.


**💡 Why this is powerful:**

One of the **biggest advantages of VS Code** is that you can assign a **different Python interpreter or environment per project**.  
This means:
- Different Python versions for different projects
- Clean and isolated environments (especially useful for data science or academic projects)
- No interference between project dependencies


