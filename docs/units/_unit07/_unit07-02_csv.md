---
title: "LM | CSV Files"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u07/header.png
  image_description: "computer"
  caption: "Photo by [Free-Photos](https://pixabay.com/photos/) [Pixabay](https://pixabay.com/de/)"
---

> “Torture the data, and it will confess to anything.” – Ronald Coase

<!--more-->

## Quick Introduction to CSV Files

CSV stands for **Comma-Separated Values**. It’s a simple text-based format for storing tabular data, where each line represents a row and values are separated by commas (`,`) or semicolons (`;`).

### Why use CSV files?

CSV files are widely used for data exchange between software tools – like Excel, databases, or Python programs. They are:

- Easy to create and read by both humans and machines.
- Supported by nearly all spreadsheet and data analysis tools.
- Lightweight and plain-text, making them ideal for simple data storage.

### How does a CSV file look?

Here is a small example:

```csv
ID;Name;Email
01;Bob Smith;bob@example.com
02;Alice Jones;alice@example.com
```

Each line is a new data row. In some files, values are enclosed in quotation marks, especially if they contain commas or line breaks.

### Opening and Saving CSV files

Most spreadsheet programs (like Excel or Google Sheets) support CSV:

- **To save:** Use “File > Save As” and choose “CSV (Comma delimited)”.
- **To open:** Simply double-click the file, or open it via “File > Open”.

In Python, you can load CSV data using the `csv` module or the `pandas` library for more advanced tasks.

CSV files are a go-to format for quickly storing and exchanging structured data.

