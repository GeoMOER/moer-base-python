---
title: "A | Assignment"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "computer"
  caption: "Photo by [Free-Photos](https://pixabay.com/photos/) [Pixabay](https://pixabay.com/de/)"
---

Please complete Exercises write your solutions in a single Python script named `unit08_assigment.py`.  


Save all scripts in the same `unit08_assigment` folder, compress the folder into a `.zip` file, and upload it to ILIAS.

For more information, please visit the following link:  
https://geomoer.github.io/moer-base-python/unit00/unit00-04_submission_guidelines.html

Make sure your code is clearly structured and includes comments where helpful.



## Dataset World Bank – Total Population by Country and Year

```python
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
df = pd.read_csv(url)
```

Analyze and compare population development of selected countries and visualize the results.

---

### Task 1 – Data Exploration

1. Print the column names.
2. Display the first 5 rows of the dataset.
3. Determine:
   - the minimum year in the dataset
   - the maximum year in the dataset

---

### Task 2 - Line Plot: Population Over Time

1. Create **one line plot** showing population development over time for the following five African countries:
   - Nigeria
   - Egypt
   - Ethiopia
   - South Africa
   - Kenya
2. Each country must have its **own line** in the plot.
3. Explicitly define the x-axis so that it starts at the **minimum year** and ends at the **maximum year** in the dataset.  
   You can use the function `plt.xlim()` for this.
4. Add:
   - a descriptive title
   - an x-axis label
   - a y-axis label
   - a legend

---

### Task 3 - Population Comparison for One Year

1. Select the year **2020**.
2. Filter the data so that it contains **only the following five European countries**:
   - Germany
   - France
   - United Kingdom
   - Italy
   - Spain
   
*Hint:* There is a pandas function that allows you to check whether values are contained in a list (2020).

3. Create:
   - a **bar chart** comparing the population sizes of these countries in 2020
   - a **pie chart with percentages** showing each country’s share of the total population

*Hint:* Make sure that both charts are based on the same filtered dataset (year 2020 and the selected countries).

---

## Titanic Data Visualization – Python Homework

Dataset (used for all tasks)

```python
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
```

---

### Task 4 – Survivors vs. Non-Survivors

1. Access the column `Survived`.
2. Count survivors and non-survivors using `value_counts()`.
3. Create:
   - a bar chart
   - a pie chart with percentages
4. Add titles and axis labels.

---

### Task 5 – Gender Distribution

1. Use the column `Sex`.
2. Count male and female passengers.
3. Create a pie chart with percentages.

---

### Task 6 – Passenger Class Distribution

1. Use the column `Pclass`.
2. Count passengers per class.
3. Create a bar chart or pie chart.


---

### Bonus Task – Multiple Plots in One Figure

Create a figure with multiple subplots (e.g. 2x2) including:
- Survivors
- Gender distribution
- Passenger class distribution

Each subplot must have its own title and one global figure title.
