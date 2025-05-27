---
title: For-loops
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u07/header.png
  image_description: "loop"
  caption: "Photo by [Christopher Kuszajewski](https://pixabay.com/de/users/kuszapro-369349/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=583537) [from Pixabay](https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=583537)"
---

For-loops are the mother of all repeating structures which enable the execution of certain code blocks for multiple times. For-loops are useful if the number of necessary repetitions is known at the starting time of the loop (which is not necessarily the starting time of the program!).

In for loops, the number of repeated executions is given at the start time either by a variable which is defined during the runtime of the previous code or by a constant supplied by the programmer. Imaging that we know already how many times the loop has to be repeated, one can implement it simply as:

```python
for i in range(7, 11):
    print(i)
# Output:
# 7
# 8
# 9
# 10

# Remember that the last number of a range is excluded
```
Note that the variable i which controls the for loop must not be changed within the loop.

Of course, you can nest for loops:

```python
for a in range(7, 11):
    print(f"Outer loop value of a: {i}")  # f-string with {i} embedded
    if i < 10:
        lower_border = i + 1
    else:
        lower_border = i
    for c in range(10, lower_border - 1, -1): # range(start, stop, step size)
        print(f"   Inner loop value of c: {j}")  # f-string with {j} embedded
# Outer loop value of a: 7
#    Inner loop value of c: 10
#    Inner loop value of c: 9
#    Inner loop value of c: 8
# Outer loop value of a: 8
#    Inner loop value of c: 10
#    Inner loop value of c: 9
# Outer loop value of a: 9
#    Inner loop value of c: 10
# Outer loop value of a: 10
#    Inner loop value of c: 10
```

The loop might look complicated but the reason for that is just the if-else statement. It is necessary since the second loop must run from `c` to the integer value just larger than `a` (i.e. 8, 9, 10). Therefore, `a` must be increased by 1 if it is smaller than 10 but stay 10 if it equals 10.

Instead of defining the number of repetitions in the for loop statement, one can also use any vector variable. The number of iterations will always be equal to the length of the vector. This is not surprising, since the `range` function used so far also simply returns an iterable, e.g.:

```r
t = range(7, 11)
print(t)
# Output: 
# 7  8  9 10
```




