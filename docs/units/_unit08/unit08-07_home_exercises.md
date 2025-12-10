---

title: "A | Assignment
toc: true
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "if logic structure"
  caption: "Photo by [Gerd Altman](https://pixabay.com/de/users/geralt-9301/) [from Pixabay](https://pixabay.com)"
---

Please save your solutions for Exercises 1 to 4 in a single Python script named `unit08__ex(1-4)code.py`.  

Save the script in the `unit08` folder, compress the folder into a `.zip` file, and upload it to ILIAS.

For more information, please visit the following link:  
https://geomoer.github.io/moer-base-python/unit00/unit00-04_submission_guidelines.html

Make sure your code is clearly structured and includes comments where helpful.


## ✨ Simple Visualization Practice Tasks

These tasks are designed to help you practice simple data visualization in Python using Matplotlib. You will use a CSV file as a data source, load it into a DataFrame, and create different plots. The total estimated time for all tasks is about 20 minutes.

---

### 🔥 Task 1: Plot a single product line

1. Download the provided CSV file (`data.csv`) or load it directly from the URL: [CSV file](https://geomoer.github.io/moer-base-python/assets/tests/unit07/books.csv) using `pandas`.
2. Create a line plot that shows the revenue of **Product A** over the years.
3. Add a descriptive title to your plot (e.g., "Revenue of Product A over Time").
4. Label the x-axis as "Year" and the y-axis as "Revenue in USD".

---

### 🟢 Task 2: Compare multiple products

1. Extend your plot from Task 1 by adding lines for **Product B** and **Product C**.
2. Use different colors and line styles for each product to make them easy to distinguish.
3. Add a legend to clearly indicate which line corresponds to each product.

---

### Task 3: Add markers
Improve your plot from Task 2 by adding markers (e.g., circles o, squares s, or triangles ^) to each product line.

Choose different marker styles for each product so that they remain distinguishable even if printed in black and white.

Optionally adjust the marker size and color for better visibility.

### 💾 Task 4: Save your plot

1. Save the plot you created in Task 2 as a PNG image file named `revenue_comparison.png`.
2. Make sure to save the file **before** calling `plt.show()` so that it is properly written to disk.

---

## 💡 Tips & Reminders

* To see column names in your DataFrame, use `df.columns`.
* To access a specific column, you can use `df['ColumnName']`.
* Use `plt.plot()` for each product series and always include a legend when showing multiple lines on the same plot.
* Check your file after saving to confirm it looks as expected.

---

## 📄 CSV File Columns

The CSV file you will use contains the following columns:

* `Year`
* `Revenue_Product_A`
* `Revenue_Product_B`
* `Revenue_Product_C`

---

### ✅ Have fun visualizing and comparing your data!
