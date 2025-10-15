---
title: "LM | Introduction"
toc: true
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "Mobile Android operating system market share by version worldwide from 2018 to 2020: [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---


## Python: A Versatile and Beginner-Friendly Language

### Introduction  
Python is a high-level, interpreted programming language created by Guido van Rossum, first released in 1991. Its readability, simplicity, and versatility have made it one of the most popular programming languages today.

### Key Features  
- **Readability and Simplicity**: Python’s design philosophy emphasizes clean and readable code. Its syntax allows programmers to express concepts with fewer lines of code compared to languages like C++ or Java. This makes Python an excellent choice for both beginners and seasoned developers.
- **Efficiency**: Python enables developers to write, maintain, and scale code efficiently due to its clear and concise syntax.

---

## Why Do We Need Programming Languages?

Computers can only understand **machine language**, which is a stream of 0s and 1s (binary).  
Writing programs in binary is nearly impossible for humans. Therefore, we use programming languages like Python to **communicate with machines in a human-friendly way**.

---

## Compiler vs Interpreter

There are two major ways to convert code into machine language:

- **Compiler**: Translates the entire program into machine code at once (e.g., C, Java). The compiled file can then be executed independently.
- **Interpreter**: Translates and runs the code **line-by-line**. Python uses this approach.

👉 Python is an **interpreted language**, which means:
- You can run code immediately without waiting for compilation.
- Great for rapid testing, debugging, and interactive sessions (e.g., Jupyter Notebooks).

---

##  Python and AI – Real-World Impact

Python is the go-to language for Artificial Intelligence and Machine Learning due to:
- Simple syntax
- Massive library support (like `scikit-learn`, `TensorFlow`, `PyTorch`)
- Community-driven innovation

### 📖 Example: Reading Text with AI

The open-source tool **Tesseract** is a powerful Optical Character Recognition (OCR) engine that can recognize text in images — from scanned documents to street signs.

It’s **written in C++** but often controlled using **Python wrappers**, making it accessible for automation and analysis:

```python
import pytesseract
from PIL import Image

text = pytesseract.image_to_string(Image.open("document.jpg"))
print(text)
```

👉 This kind of powerful text extraction and evaluation is possible thanks to Python’s ability to combine **AI, image processing**, and **automation** in just a few lines of code.

---

## Ecosystem and Applications

Python offers a rich ecosystem of libraries and frameworks that support various fields:

- **Data Analysis**: NumPy, Pandas  
- **Machine Learning & AI**: TensorFlow, PyTorch, scikit-learn  
- **Image & Text Processing**: OpenCV, Tesseract, NLTK

---

## Community and Support

Python’s large and active community provides extensive resources, documentation, and support, making it easier for developers to learn, collaborate, and solve problems.

Whether you’re automating your daily tasks, building a website, or developing AI models — **Python is a great place to start.**

## ⚙️ What is an Algorithm?

An **algorithm** is a sequence of step-by-step instructions to solve a specific problem or perform a task.

### Algorithm: Baking a Cake

This is an algorithm! Just like a recipe, programming algorithms give exact instructions to achieve a goal.

**Example (in pseudocode):**

```text
Start
  Gather all ingredients
  Mix flour, sugar, eggs, and butter
  IF batter texture is too thick THEN add some milk
  Pour batter into a baking pan
  Preheat oven to 180°C
  Put pan in the oven
  Bake for 30 minutes
  IF cake is not baked through THEN bake for 10 more minutes
  Take cake out of the oven
  Let it cool
  Serve and enjoy
End
```

---