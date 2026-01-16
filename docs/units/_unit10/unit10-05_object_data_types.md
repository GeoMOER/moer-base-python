---
title: LM | Object Data Types
header:
  image: /assets/images/unit_images/u10/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "Mobile Android operating system market share by version worldwide from 2018 to 2020: [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---

# Object Data Types (Lists, Arrays, DataFrames)

Python offers various complex data types to store collections of data:

- **Lists**: Ordered, mutable collections of items
- **Arrays**: More efficient arrays of homogeneous data, often using `numpy`
- **DataFrames**: Tabular data structures from the `pandas` library, ideal for data analysis

Mastering these types allows you to work efficiently with larger and more complex data sets.

## Examples

```python
# List example
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# Array example (requires numpy)
import numpy as np
numbers = np.array([1, 2, 3, 4])
print(numbers * 2)

# DataFrame example (requires pandas)
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}
df = pd.DataFrame(data)
print(df)
```
