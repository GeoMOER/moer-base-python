---
title: "LM | Export"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u06/header.png
  image_description: "computer"
  caption: "Photo by [Free-Photos](https://pixabay.com/photos/) [Pixabay](https://pixabay.com/de/)"
---

## 📤 Exporting CSV Data with `pandas`

After data processing, you can save your DataFrame to a CSV file using `to_csv()`:

```python
df.to_csv("path/to/your/output_file.csv", sep=",", decimal=".", index=False)
```

### Explanation of Parameters

- `path_or_buf`: Destination path.
- `sep=','`: Column separator.
- `decimal='.'`: Decimal point.
- `index=False`: Do not write row index.

This creates a clean, portable CSV file readable by most spreadsheet and database tools.
