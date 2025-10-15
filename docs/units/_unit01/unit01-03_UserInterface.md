---
title: "LM | User Interface"
toc: true
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "User Interface:
  [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---

## Working with Jupyter (Uni Marburg Environment)

Python can be used in different development environments — such as Visual Studio Code, PyCharm, or Thonny — but in this course we will **only use Jupyter** provided by **Philipps-Universität Marburg**.  
Jupyter is web-based, requires **no installation**, and is ideal for beginners and data-driven tasks.

---

### Accessing Jupyter at Uni Marburg

You can access Jupyter directly through your browser at:  
👉 [https://jupyter.uni-marburg.de](https://jupyter.uni-marburg.de)

Log in with your university account to start your personal workspace.  
You can create and save notebooks (`.ipynb` files), run Python code, and explore data — all inside your web browser.

---

### What is Jupyter?

Jupyter offers two main interfaces:

- **Jupyter Notebook** – simple and linear, good for writing code and explanations step by step.  
- **Jupyter Lab** – a modern interface where you can open multiple notebooks, terminals, text files, and folders side by side.

Both environments allow you to combine code, text, and images in one interactive document — perfect for learning, experimenting, and documenting your work.

---

### 🏠 Working on Your Homework with Jupyter

You can work on all exercises directly inside Jupyter.  
Each task can be placed in a new code cell or text cell.  

Follow these steps:

1. Complete all exercises in your Jupyter notebook.  

2. When finished, open a new cell at the top and add:
   ```python
   # unitXX_assignment.py
   # Student ID: 12345678
   # Name: <Your Name>
   ```
3.💡 *All explanations must be written as comments inside your Python code, for example:*
  ```python
  # Task 1: Why is Python popular?
  # - Easy to learn
  # - Many libraries
  # - Free and open source
  ```

---

## 💾 Exporting Your Code as a `.py` file.

You’ll need to **save your Jupyter code as a regular Python file**, to upload it to ILIAS or run it locally.

- Copy your final code from the notebook into a local text editor. 

- Save it as **`unitXX_assignment.py`**.  

---

### 2️⃣ Run the Script Locally

Now you can run your `unitXX_assignment.py` file outside Jupyter:

1. Open a **Command Prompt (Windows)** or **Terminal (macOS/Linux)**.  

2. Navigate to the folder where you saved the file:

   ```bash
   cd path/to/your/folder
   ```
   
3. Run the script:
   ```bash
   python unit01_assignment.py
   ```
   You should see:
   ```
   Hello World
   ```
   
## ❗To uload **this file as zip** to ILIAS – see: [Submission Guidelines](/moer-base-python/unit00/unit00-04_submission_guidelines.html)

### ✨ Advantages of Using Jupyter

- No installation needed — everything runs in your browser.  
- Immediate feedback: execute each cell and see results below.  
- Markdown support for comments, documentation, and equations.  
- Already configured with essential Python libraries at Uni Marburg.  
- Your work is automatically stored in your university account.

---

### 🚀 Summary

In this course we use **Jupyter Uni-Marburg** for all programming activities.  
Although other environments (VS Code, PyCharm, etc.) exist, Jupyter provides the easiest and most consistent setup for everyone.  
You’ll write and test your code directly in Jupyter — and submit your final solutions as a single `.py` file.

👉 [Start here: Jupyter Uni-Marburg](https://jupyter.uni-marburg.de)
