---
title: "LM | Essential Pandas Functions for Data Analysis & Plotting"
toc: true
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "if logic structure"
  caption: "Photo by [Gerd Altman](https://pixabay.com/de/users/geralt-9301/) [from Pixabay](https://pixabay.com)"
---


## 🧩 1. Essential Pandas Functions for Data Analysis & Plotting

To create statistical diagrams with Matplotlib later on, students should be familiar with the following Pandas functions and workflow steps:

---

| Topic | Important Functions | Meaning |
|-------|----------------------|----------|
| Load a file | `pd.read_csv()` | Load a CSV file |
| Quick look | `df.head()`, `df.tail()` | Show the first/last rows |
| Information | `df.info()` | Columns, data types, missing values |
| Statistics | `df.describe()` | Basic statistical summary |
| Count values | `df['col'].value_counts()` | e.g., number of males/females |
| Categories of value_counts | `df['col'].value_counts().index` | Returns category names (e.g., `['male','female']`) |
| Frequencies of value_counts | `df['col'].value_counts().values` | Returns counts (e.g., `[577, 314]`) |
| Select one column | `df['col']` | Extract a single column |
| Select multiple columns | `df[['col1', 'col2']]` | Extract several columns |
| Filter rows | `df[df['Age'] > 18]` | Select rows matching a condition |
| Filter with multiple conditions | `df[(df['Sex']=='female') & (df['Survived']==1)]` | Combine logical conditions |
| Filter by multiple values | `df[df['col'].isin(list)]` | Select rows where values are in a given list |
| Sort data | `df.sort_values('col')` | Sort DataFrame by column |
| Check missing values | `df.isna().sum()` | Count missing values per column |
| Drop missing rows | `df.dropna()` | Remove rows with missing values |
| Fill missing values | `df.fillna(value)` | Replace missing values |
| Create a new column | `df['new'] = ...` | Add derived/computed values |
| Group data | `df.groupby('col')` | Group rows by a category |
| Aggregate data | `df.groupby('col').mean()` | Compute statistics per group |
| Set x-axis limits (plots) | `plt.xlim(min, max)` | Define start and end of the x-axis |


