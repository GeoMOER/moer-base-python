---
title: "LM | Installing"
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "if logic structure"
  caption: "Photo by [Gerd Altman](https://pixabay.com/de/users/geralt-9301/) [from Pixabay](https://pixabay.com)"
---


Matplotlib is not included in the standard Python installation, so you need to install it first. The most common way is using `pip`.

```bash
pip install matplotlib
```

## 💡 Installing in Visual Studio Code

If you are using Visual Studio Code (VS Code) instead of the Windows shell directly, you can install Matplotlib easily in the integrated terminal:

1️⃣ Open your Python project folder in VS Code.
2️⃣ Open the integrated terminal (`Terminal` > `New Terminal`).
3️⃣ Make sure your Python interpreter is selected correctly (check in the bottom-right corner or press `Ctrl+Shift+P` and type `Python: Select Interpreter`).
4️⃣ In the terminal, run:

```bash
pip install matplotlib
```

After installation, you can start writing your Python scripts in `.py` files and use Matplotlib just as you would anywhere else. VS Code will detect the package automatically if the correct interpreter is set.

## 🐍 Importing Matplotlib

Once installed, you can import Matplotlib in your Python code. Most often, we use the `pyplot` module and import it with the alias `plt`.

```python
import matplotlib.pyplot as plt
```

## ✅ Check Your Installation

After importing, you can check the version to ensure it was installed correctly:

```python
import matplotlib
print(matplotlib.__version__)
```

## 📚 Further Reading

* [Matplotlib Installation Guide](https://matplotlib.org/stable/users/installing.html)
* [Pyplot API Documentation](https://matplotlib.org/stable/api/pyplot_api.html)
* [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
