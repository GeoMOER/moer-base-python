---
title: Installing Libraries
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

## **Create a Virtual Environment with Miniconda**

A virtual environment is an isolated environment that allows you to manage libraries for different projects separately. This is crucial for several reasons:

1. **Dependency Management**: Different projects might require different versions of libraries. Virtual environments allow you to maintain these dependencies without conflicts.
2. **Project Isolation**: Each virtual environment is independent, ensuring that changes in one project do not affect another.
3. **Reproducibility**: Virtual environments help in replicating the development environment, making it easier to share and collaborate on projects.
4. **Cleaner System**: By using virtual environments, you avoid installing packages globally, keeping your base system clean and organized.

Creating a virtual environment ensures that your projects remain manageable, reproducible, and free from dependency conflicts.

### **Now let's create a virtual environment with Miniconda:**

1. Open your Miniconda PowerShell.
2. Create a new virtual environment by running the following command:
   ```sh
   conda create -n myenv python=3.9
   ```
   Replace `myenv` with the name you want for your environment and `3.9` with the desired Python version.
3. Activate your new virtual environment by calling its name and downloading necessary libraries for the course:
   ```sh
   conda activate myenv
   ```
4. Now you can install the libraries needed inside that virtual environment:
   ```sh
   conda install numpy
   conda install pandas
   conda install matplotlib
   ```
   These libraries are needed for numerical computations and array handling (`NumPy`), data manipulation and analysis (`pandas`), and creating visualizations (`Matplotlib`).

---

## **Using the Conda Virtual Environment in Visual Studio Code**

Once you have created and activated your Conda environment, you need to configure Visual Studio Code to use it:

### **Option 1: Select the Conda Environment as the Python Interpreter**

1. Open **Visual Studio Code**.
2. Press **Ctrl + Shift + P** to open the **Command Palette**.
3. Type **Python: Select Interpreter** and select this option.
4. If your Conda environment appears in the list, select it.
5. If it does not appear, click **Enter interpreter path** → **Find** and manually locate your Conda environment’s Python path:
   ```sh
   C:\Users\YourUsername\Miniconda3\envs\myenv\python.exe
   ```
6. Now, Visual Studio Code will use the Conda environment as the active Python interpreter.

### **Option 2: Activate Conda in the VS Code Terminal**

1. Open Visual Studio Code.
2. Open the terminal inside VS Code (**Ctrl + `** or **View → Terminal**).
3. Activate your Conda environment manually:
   ```sh
   conda activate myenv
   ```
4. Now you can run Python scripts and Jupyter notebooks using the selected Conda environment.

### **Using Jupyter Notebook with Conda in VS Code**

1. Make sure Jupyter is installed in your Conda environment:
   ```sh
   conda install -c conda-forge jupyter
   ```
2. Open **Visual Studio Code**.
3. Install the **Jupyter extension** (`Ctrl + Shift + X`, search for "Jupyter" and install).
4. Open a `.ipynb` file or create a new one.
5. Select your **Conda environment** as the active kernel.
6. Now, you can execute Jupyter notebooks inside VS Code using your Conda environment.

---

## **Setting Up Environment Variables for Miniconda as a Normal User**

If you installed Miniconda as a normal user (not as an administrator), you should ensure that the **environment variables** are properly set up in the **User Path** instead of the **System Path**. This avoids permission issues when installing libraries.

### **Steps to Configure User Environment Variables:**

1. **Open Windows Environment Variables:**
   - Press `Win + R`, type `sysdm.cpl`, and hit Enter.
   - Go to the **Advanced** tab and click on **Environment Variables**.

2. **Edit User Variables:**
   - Under **User Variables**, find `Path` and click **Edit**.
   - Add the following paths (adjust if Miniconda is installed elsewhere):
     ```
     C:\Users\YourUsername\Miniconda3
     C:\Users\YourUsername\Miniconda3\Scripts
     C:\Users\YourUsername\Miniconda3\Library\bin
     ```

3. **Apply Changes and Restart VS Code:**
   - Click **OK** to save.
   - Restart **VS Code** and verify by running:
     ```sh
     where conda
     ```
   - It should output the correct Conda installation path.

By setting up these environment variables under the **User Path**, you ensure that Conda and its environments work smoothly without requiring admin privileges.

Now you are ready to work with Conda environments seamlessly in Visual Studio Code! 🚀

