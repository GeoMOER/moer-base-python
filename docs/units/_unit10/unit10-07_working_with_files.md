---
title: LM | Working with Files (CSV)
header:
  image: /assets/images/unit_images/u10/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "Mobile Android operating system market share by version worldwide from 2018 to 2020: [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---

# Working with Files (CSV)

Reading and writing files, especially CSV files, is crucial for data analysis and sharing results. In Python, you can use:

- The built-in `open()` function
- The `csv` module for simple CSV operations
- The `pandas` library for powerful data import and export

Practicing file handling helps you work with real-world data in your projects.

## Example: Importing CSV with pandas

```python
import pandas as pd

# Read a CSV file
df = pd.read_csv("data.csv")

# Show the first few rows
print(df.head())

# Write to a new CSV file
df.to_csv("output.csv", index=False)
```

Using pandas makes working with CSV files fast and convenient, especially for data analysis tasks.
