---
title: "Importing CSV Data with Python"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u06/header.png
  image_description: "computer"
  caption: "Photo by [Free-Photos](https://pixabay.com/photos/) [Pixabay](https://pixabay.com/de/)"
---

## 📥 Importing CSV Data with `pandas`

Reading tabular data into a DataFrame is a common task in data analysis. If your CSV file uses commas as separators, periods for decimals, and includes a header row, importing is straightforward using `pandas.read_csv()`:

```python
import pandas as pd

df = pd.read_csv("path/to/your/file.csv")
```

### Custom Parameters

If your file uses different settings (common in Europe), you can adjust the parameters:

```python
df = pd.read_csv("path/to/your/file.csv", sep=";", decimal=",")
```

### Example with Real Data (GENESIS)

This example uses data from the [GENESIS regional statistics portal](https://www.regionalstatistik.de/genesis/online/), which provides official statistics for Germany.

To use such data:
1. Visit the GENESIS portal and download the desired table as a `.csv` file.
2. Save the file locally, then read it with pandas:

```python
import pandas as pd

df = pd.read_csv("AI001_gebiet_flaeche.csv", skiprows=4, header=0, sep=";", decimal=",")
```

**Note:** You cannot directly import GENESIS data via URL because the download requires user interaction. Download the file manually and place it in your working directory.


#### Explanation of Parameters

- `skiprows=4`: Skip metadata rows.
- `header=0`: Use first valid row as header.
- `sep=';'`: Semicolon as column separator.
- `decimal=','`: Comma as decimal point.


### Check First Rows

```python
print(df.head(2))
```

This displays the first 2 rows of your DataFrame, useful for quickly inspecting the structure.
