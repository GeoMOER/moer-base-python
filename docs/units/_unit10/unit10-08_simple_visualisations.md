---
title: LM | Simple Visualisations
header:
  image: /assets/images/unit_images/u10/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "Mobile Android operating system market share by version worldwide from 2018 to 2020: [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---

# Simple Visualisations

Visualization is a key skill for communicating your data insights. In Python, you often use:

- `matplotlib` for creating plots and charts
- `pandas` integrated plotting functions for quick visual checks

You learned to create line plots, bar charts, and histograms to better understand and present your data.

## Example

```python
import pandas as pd
import matplotlib.pyplot as plt

# Example data
data = {
    "Year": [2020, 2021, 2022],
    "Sales": [100, 150, 200]
}
df = pd.DataFrame(data)

# Line plot
plt.plot(df["Year"], df["Sales"], marker="o")
plt.title("Sales over Years")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
```

Creating simple plots helps you quickly explore trends and share your findings visually.
