---
title: LM | Conditionals
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u10/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "Mobile Android operating system market share by version worldwide from 2018 to 2020: [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---

# Conditionals

Conditionals allow your program to make decisions based on certain conditions. In Python, you use:

- `if` statements
- `elif` (else if) statements
- `else` statements

Conditionals help you create dynamic and responsive programs that can react to different inputs or situations.

## Examples

```python
x = 10

if x > 5:
    print("x is greater than 5")
    
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5 or equal to 5")

# Example with multiple conditions
temperature = 25

if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("The weather is nice.")
elif temperature < -20:
    print("The weather is perfect! :)")
else:
    print("It's a bit cold.")
```

Using conditionals makes your code flexible and able to handle different cases in a clear and structured way.
