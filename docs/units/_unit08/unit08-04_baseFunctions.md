---
title: "LM | Basic Functions for Plots"
header:
  image: /assets/images/unit_images/u08/header.png
  image_description: "if logic structure"
  caption: "Photo by [Gerd Altman](https://pixabay.com/de/users/geralt-9301/) [from Pixabay](https://pixabay.com)"
---


## 🎨 Why Customize Plots?

Adding titles, labels, and legends makes your plots easier to understand and more informative. It helps the audience quickly see what each axis represents and what the data shows.

## 🏷️ Adding Titles and Labels

### Add a title

```python
plt.title("My Awesome Plot")
```

### Add axis labels

```python
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
```

## 🔖 Adding a Legend

If you have multiple data series in one plot, a legend helps distinguish them.

```python
plt.plot([1, 2, 3], [4, 5, 6], label="Series A")
plt.plot([1, 2, 3], [6, 5, 4], label="Series B")
plt.legend()
```

## 💡 Grid and Style Adjustments

### Add grid lines

```python
plt.grid(True)
```

### Change line style and color

```python
plt.plot(x, y, color="green", linestyle="--", marker="o")
```

## ✅ Summary

* Use **titles** and **labels** to explain your plot.
* Add a **legend** when showing multiple series.
* Adjust **style and grid** to improve readability.

---

This section helps you make your plots clear and professional, so they are ready to share or present!
