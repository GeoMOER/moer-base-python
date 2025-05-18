---
title: break and continue
header:
  image: /assets/images/unit_images/u07/header.png
  image_description: "loop"
  caption: "Photo by [Christopher Kuszajewski](https://pixabay.com/de/users/kuszapro-369349/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=583537) [from Pixabay](https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=583537)"
---
Understanding break and continue Statements in Python
## break Statement

The break statement is used to exit a loop prematurely. When a break statement is encountered, the loop stops executing, and the program control jumps to the first statement following the loop.
```python
for number in range(10):
    if number == 5:
        break  # Exit the loop when number is 5
    print(number)

# Output: 0, 1, 2, 3, 4
```
In this example, the loop will print numbers from 0 to 4. When the loop reaches 5, the break statement is executed, and the loop terminates.

## continue Statement

The continue statement is used to skip the current iteration of a loop and proceed to the next iteration. When a continue statement is encountered, the rest of the code inside the loop for the current iteration is skipped.
```python
for number in range(10):
    if number % 2 == 0:
        continue  # Skip the even numbers
    print(number)

# Output: 1, 3, 5, 7, 9
```
In this example, the loop iterates through numbers from 0 to 9 but skips printing the even numbers. When an even number is encountered, the continue statement is executed, and the loop moves to the next iteration.

## Summary
 - break: Exits the loop immediately.
 - continue: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
These control statements help you manage the flow of loops effectively, allowing you to implement more complex logic in your programs.