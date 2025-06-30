---
title: "LM | Install Matplotlib"
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "if logic structure"
  caption: "Photo by [Gerd Altman](https://pixabay.com/de/users/geralt-9301/) [from Pixabay](https://pixabay.com)"
---

## 💻 Installing Matplotlib

Matplotlib is not included in the standard Python installation, so you need to install it first. The most common way is using `pip`.

```bash
pip install matplotlib
```

If you are using a Jupyter notebook, you might also want to run:

```python
%pip install matplotlib
```

## 🐍 Importing Matplotlib

Once installed, you can import Matplotlib in your Python code. Most often, we use the `pyplot` module and import it with the alias `plt`.

```python
import matplotlib.pyplot as plt
```

## ✅ Check Your Installation

After importing, you can check the version to ensure it was installed correctly:

```python
print(matplotlib.__version__)
```

## 📚 Further Reading

* [Matplotlib Installation Guide](https://matplotlib.org/stable/users/installing.html)
* [Pyplot API Documentation](https://matplotlib.org/stable/api/pyplot_api.html)
