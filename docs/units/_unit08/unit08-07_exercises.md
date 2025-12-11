---

title: "EX | Exercises"
toc: true
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "if logic structure"
  caption: "Photo by [Gerd Altman](https://pixabay.com/de/users/geralt-9301/) [from Pixabay](https://pixabay.com)"
---

## ✨ Simple Visualization Practice Tasks

These tasks are designed to help you practice simple data visualization in Python using Matplotlib. You will use a CSV file as a data source, load it into a DataFrame, and create different plots. The total estimated time for all tasks is about 20 minutes.

---

### 🔥 Task 1: Plot a single product line

1. Download the provided CSV file (`data.csv`) or load it directly **read_csv(url)** from the URL: [https://geomoer.github.io/moer-base-python/assets/tests/unit08/data.csv](https://geomoer.github.io/moer-base-python/assets/tests/unit08/data.csv) using `pandas`.
2. Create a line plot that shows the revenue of **Product A** over the years(X-Axis).
3. Add a descriptive title to your plot (e.g., "Revenue of Product A over Time").
4. Label the x-axis as "Year" and the y-axis as "Revenue in USD".
5. Use a solid line style (e.g., linestyle='-') so that the line appears as "----".
6. Add different markers to your line using marker(see the table on https://geomoer.github.io/moer-base-python/unit08/unit08-04_creating.html.

---

### 📘 Task 2: Exploring the Titanic Dataset 

In this exercise, you will load the Titanic dataset and perform a basic first exploration using Pandas. This will help you understand the structure of the data before creating diagrams with Matplotlib.

---

#### 🔹  Load and Inspect the Dataset

1. **Load** the Titanic CSV file into a Pandas DataFrame  
   ```python
   import pandas as pd
   df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

   ```

2. **Display the first rows** of the dataset  
   ```python
   df.head()
   ```

3. **Show basic information** about the dataset**  
   - Number of rows and columns  
   - Column names  
   - Data types  
   - Missing values  
   ```python
   df.info()
   ```

4. **Generate basic descriptive statistics**  
   ```python
   df.describe()
   ```

5. **Count how many passengers are in each category**, for example:  
   - Number of males and females  
   - Number of passengers in each passenger class  
   ```python
   df['Sex'].value_counts()
   df['Pclass'].value_counts()
   ```
   
6. **Create Basic Visualizations**

   - **A bar chart showing the number of male vs. female passengers**
    Use the categories from `df['Sex'].value_counts().index` as the x-axis labels.
    Use the counts from `df['Sex'].value_counts().values` as the bar heights.
    ```python
    categories = df['Pclass'].value_counts().index
    ```

   - **A bar chart showing the number of passengers in each passenger class (Pclass)**
    Use the categories from `df['Pclass'].value_counts().index` as the x-axis labels.
    Use the counts from `df['Pclass'].value_counts().values` as the bar heights.
