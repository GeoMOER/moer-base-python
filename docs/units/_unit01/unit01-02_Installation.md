---
title: "Installation"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "Mobile Android operating system market share by version worldwide from 2018 to 2020: [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---
*Installation Guide for Python, Miniconda, and Visual Studio Code*
<!--more-->

## Installation Guide for Python, Miniconda, and Visual Studio Code

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

### **Step 2: Download and Install Miniconda**

1. **Go to the Miniconda download page**  
   - Visit the official [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html).

2. **Choose the correct installer**  
   - Select the appropriate version for your operating system:
     - **Windows**: `.exe` installer  
     - **macOS**: `.pkg` file or `bash` version for terminal use  
     - **Linux**: `.sh` script

3. **Start the installation**  
   - Run the installer and follow the instructions.
   - Choose the option to add Miniconda to the system PATH if available.

4. **Verify the installation**  
   - Open a terminal or command prompt and enter:
     ```sh
     conda --version
     ```
   - If no error appears, Miniconda is successfully installed.

---

### **Step 3: Download and Install Visual Studio Code**

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

### **Step 4: Install Extensions in Visual Studio Code**

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

#### **3. (Optional) Additional useful extensions**

- **Pylance** (better code completion for Python)
- **Conda** (simplifies managing Conda environments in VS Code)
- **Live Share** (for collaborative work)

---

### **Additional Tests After Installation**

#### **Run Python in VS Code**

1. Open VS Code.
2. Create a new file `test.py` with the following content:
   ```python
   print("Hello, world!")
   ```
3. Press `F5` or go to **Run** → **Run Python File**.

#### **Test Jupyter Notebook**

1. Open VS Code.
2. Create a new file `test.ipynb`.
3. Add a new cell and write:
   ```python
   print("Jupyter Notebook is running!")
   ```
4. Run the cell.

If any issues arise:
- Check if Python and Miniconda are correctly installed.
- Select the correct Python interpreter (`Ctrl+Shift+P` → "Python: Select Interpreter").

This guide should now cover all essential steps! 😊
```


{% include figure image_path="/assets/images/unit_images/u01/flowchart_python.png" %}

<!--
## Further reading

add some day
-->
