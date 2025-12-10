---
title: "LM | Installing"
toc: true
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "if logic structure"
  caption: "Photo by [Gerd Altman](https://pixabay.com/de/users/geralt-9301/) [from Pixabay](https://pixabay.com)"
---


If you don’t yet have a development tool installed for working with Python on your computer, you can use Thonny.
Thonny is a very simple and beginner-friendly Python environment, ideal for new learners.

Alternatively, you can use Visual Studio Code, PyCharm, or RStudio.

Here is a detailed installation guide for Thonny.

---
## Installing Thonny (Beginner-Friendly Python IDE)

Thonny is a simple development environment designed for Python beginners.  
The installation is quick and easy.

---

### 1. Download Thonny

1. Open the website: **https://thonny.org**
2. Click **Download Thonny for Windows**.
3. Download the installer file (e.g., `thonny-4.x.x.exe`).

---

### 2. Run the Installer

1. Double-click the downloaded file.
2. Choose **Next** → **Install**.
3. Keep the default settings.

---

### 3. Python Selection on First Start

#### If Python is **not installed**:
- Select **“Use Thonny’s built-in Python”**  
  → Recommended for beginners  
  → Python will be installed automatically

#### If Python **is already installed**:
- Either use **Thonny’s built-in Python** (recommended), or  
- Choose your existing Python installation.

---

### 4. Test the Installation

1. Open Thonny.
2. Type:

```python
print("Hello Python!")
```

3. Press **Run ▶**.

If `Hello Python!` appears, Thonny is working correctly.

---
Installing Python Packages in Thonny  
*(Example: pandas and matplotlib)*

### 5. Install `pandas` or `matplotlib`

1. Open Thonny.
2. Go to: **Tools → Manage packages…**
3. In the search box, type:

   - `pandas`  
   - or `matplotlib`

4. Click **Search**, then **Install**.

Thonny will download and install the package automatically.

---

### 6. Test if the packages work

#### Test pandas:

```python
import pandas as pd
print(pd.__version__)
```

#### Test matplotlib:

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [3, 1, 4])
plt.show()
```

If a plot window appears, matplotlib is installed correctly.

---

### Done!
You can now use Thonny to write Python programs and visualize data using packages like pandas and matplotlib.

---

If you are using **RStudio**, **Visual Studio Code**, or **PyCharm** as your Python environment,  
please install the package **matplotlib** before the next session.


## Installing matplotlib for Your Python Environment

### 👉 Installation via `pip` (recommended)

Open your **terminal** or **command prompt** and run:

```python
pip install matplotlib
```

If you have multiple Python versions installed, you may need to run:

```python
python -m pip install matplotlib
```


### 🔄 Restart Required
After installing a new Python package, it is usually necessary to **restart your editor**  
(e.g., Visual Studio Code, RStudio, PyCharm).  
Otherwise, the environment may not detect the newly installed package.


---

### ✔ Test whether matplotlib works

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [3, 1, 4])
plt.show()
```

### 📚 Further Reading

* [Matplotlib Installation Guide](https://matplotlib.org/stable/users/installing.html)
* [Pyplot API Documentation](https://matplotlib.org/stable/api/pyplot_api.html)
* [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
