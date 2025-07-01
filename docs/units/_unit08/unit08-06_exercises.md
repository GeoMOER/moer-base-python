---

title: "EX | Exercises"
header:
image: /assets/images/unit\_images/u08/header.png
image\_description: "if logic structure"
caption: "Photo by [Gerd Altman](https://pixabay.com/de/users/geralt-9301/) [from Pixabay](https://pixabay.com)"
----------------------------------------------------------------------------------------------------------------

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

### 💾 Task 3: Save your plot

1. Save the plot you created in Task 2 as a PNG image file named `revenue_comparison.png`.
2. Make sure to save the file **before** calling `plt.show()` so that it is properly written to disk.

---

## 💡 DataFrame Reminders

* To check column names in your DataFrame, use `df.columns`.
* To access a specific column, use `df['ColumnName']` (for example: `df['Revenue_Product_A']`).
* Use `df.head()` to preview the first few rows of your data.

---

## 📄 CSV File Columns

The CSV file you will use contains the following columns:

* `Year`
* `Revenue_Product_A`
* `Revenue_Product_B`
* `Revenue_Product_C`

---

### ✅ Have fun visualizing and comparing your data!
