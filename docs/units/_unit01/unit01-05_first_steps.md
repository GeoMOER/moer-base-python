---
title: "Ex | First steps in Python"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u01/header.png
  image_description: "confused"
  caption: "Image by [slon_pics](https://pixabay.com/de/users/www_slon_pics-5203613/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021) [from pixabay](https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2261021)"
---
*Making your first steps in Python with simple print() operations.*

<!--more-->

## #Hashtag and Run!

Let's open our first Jupyter Notebook.

If you are working locally with the VS User Interface, navigate to the top menu and click on **View** > **Command Palette**. In the search bar that appears, type **Create: New Jupyter Notebook** and select it. VS Code will automatically create the first code block for you.

Now, try entering this line of code:

```python
print('Welcome to Python')
```

To run the code block, simply click on the **Run** button (a small play icon) that appears above the code cell. If you are running the notebook for the first time, the interface will prompt you to select a Python interpreter.

Here, you need to choose either your **local miniconda virtual environment** or an **online Python interpreter (Pyodide)**. After selecting the interpreter, click **Run** again to execute your code.

### Using Comments in Python

You can add comments to your code to make it easier to understand for yourself and others. Python treats the hashtag character **#** in a special way: anything following a **#** on a line is ignored by the interpreter.

This makes hashtags very useful for adding explanations and annotations to your code. Comments are visible to you but do not affect the execution of the program.

```python
# This is a comment. Comments help you understand your code later.
# Use them often to clarify what your code does.

print("Welcome to Python")
```



{% include figure image_path="/assets/images/unit_images/u01/VS_code_first_steps.PNG" caption="VS Code Overview" %}
