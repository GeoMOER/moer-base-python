---
title: "LM | Import"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u07/header.png
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

#### Example 

```python
import pandas as pd

df = pd.read_csv(
    "data.csv",             # Path to your CSV file
    sep=",",                # Separator used in the file (e.g., ',' or ';')
    header=0,               # Row number to use as column names (0 = first row)
    names=[None],             # Custom column names (e.g., ['A', 'B', 'C']), overrides header
    index_col=None,         # Column to use as the row index
    usecols=None,           # List of columns to read (e.g., ['Name', 'Age'])
    dtype=None,             # Data types for columns (e.g., {'Age': int})
    engine="python",        # Parser engine ('c' or 'python')
    skiprows=0,             # Number of lines to skip at the start
    na_values=["NA", ""],   # Additional strings to recognize as NA/NaN
    nrows=None,             # Number of rows to read (e.g., 100)
    encoding="utf-8",       # Character encoding (e.g., 'utf-8', 'latin1')
    parse_dates=False,      # Parse date columns as datetime
    dayfirst=False,         # When parsing dates, set to True if day comes first
    thousands=",",          # Character used as thousands separator
    decimal=".",            # Character used as decimal point
    quotechar='"',          # Character used to quote fields
    skip_blank_lines=True   # Skip over blank lines
)

print(df.head())  # Show the first 5 rows of the DataFrame standart
```

