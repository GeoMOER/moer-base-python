---
title: LM | Object Data Types
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u10/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "Mobile Android operating system market share by version worldwide from 2018 to 2020: [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---

# Object Data Types (Lists, Arrays, DataFrames)

In Python, **object data types** are used to store and manage **collections of values**.  
They are essential when working with real-world data, which usually consists of **many related values**, not just single numbers or strings.

The most important object data types introduced so far are:

- **Lists**
- **Arrays (NumPy)**
- **DataFrames (pandas)**

Each of these structures serves a different purpose and is optimized for specific tasks.

---

## Lists

A **list** is an ordered and **mutable** collection of elements.

### Key properties of lists:
- Elements can have **different data types**
- Order is preserved
- Elements can be added, removed, or modified
- Indexing starts at **0**

### Typical use cases:
- Storing small to medium collections
- Mixed data types
- Flexible data manipulation

### Example
```python
fruits = [...
```

## Arrays (NumPy)

An array is a data structure provided by the NumPy library.
Unlike lists, NumPy arrays are designed for numerical computations.

### Key properties of arrays:

- All elements must have the same data type
- Much faster than lists for mathematical operations
- Support vectorized operations (no explicit loops needed)

### Typical use cases:

- Numerical data
- Scientific computing
- Mathematical operations on large datasets

###Example
```python
import numpy as np
...
```

##DataFrames (pandas)

A DataFrame is a two-dimensional, table-like data structure provided by the pandas library.

### Key properties of DataFrames:

- Data organized in rows and columns
- Each column has a name
- Columns can have different data types
- Ideal for reading, analyzing, and cleaning data

### Typical use cases:

- CSV / Excel data
- Data analysis
- Statistics and visualization


### Example
```python
import pandas as pd
...






