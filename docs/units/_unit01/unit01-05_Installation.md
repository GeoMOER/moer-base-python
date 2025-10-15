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

## 🐍 Guide for Python Installation

### **Step 1: Download and Install Python**

1. **Go to the Python download page**  
   Visit the official [Python website](https://www.python.org/downloads/).

2. **Download the appropriate installer**  
   Choose the correct version for your operating system:
   - **Windows**: `.exe` installer (**64-bit** recommended)  
   - **macOS**: `.pkg` installer  
   - **Linux**: Python is often pre-installed. If not, install it via your package manager (`apt`, `dnf`, `yum`, etc.).

3. **Start the installation**  
   - Run the downloaded installer.  
   - **Important:** Check the box **“Add Python to PATH”**.  
   - Click **“Install Now”** or choose **“Customize Installation”** if you want to adjust specific options.

4. **Verify the installation**  
   Open a terminal or command prompt and enter:
   ```bash
   python --version
   ```
   or, on some systems:
   ```bash
   python3 --version
   ```
   You should see output like `Python 3.12.6`.  
   If it doesn’t work, restart your computer and ensure Python is added to your system PATH.

---

### **Step 2: Check the Python Path**

To confirm which Python version your system is using and where it’s installed, follow these steps:

#### 🔹 **Windows**
1. Open **Command Prompt** or **PowerShell**  
   (Press `Win + R`, type `cmd` or `powershell`, and press Enter).
2. Enter the command:
   ```bash
   where python
   ```
3. You’ll see one or more paths, for example:
   ```
   C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe
   C:\Program Files\Python39\python.exe
   ```
   The **first path** listed is the default Python interpreter your system uses.

#### 🔹 **macOS / Linux**
1. Open the **Terminal**.
2. Enter one of the following commands:
   ```bash
   which python
   # or, on newer systems:
   which python3
   ```
3. Example output:
   ```
   /usr/bin/python3
   /opt/homebrew/bin/python3
   ```
   The displayed path shows the active Python interpreter on your system.

---

✅ **Tip:**  
To start Python interactively, type:
```bash
python
# or
python3
```
and press **Enter**.  
To exit again, type:
```bash
exit()
```

