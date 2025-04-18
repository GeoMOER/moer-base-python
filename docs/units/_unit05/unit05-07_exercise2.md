---
title: "Python Exercise - Loops 2"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u03/header.png
  image_description: "keyboard"
  caption: "Image by [username](https://pixabay.com) from pixabay"
---

# Introduction

This unit covers how to work with user input and loops in Python. You will practice collecting input from the user, performing operations on lists, and implementing password checks with limited attempts.

## Task 1: Enter Numbers, Find Maximum and Minimum, and Sort the List

### Description:
Write a program that asks the user to enter 5 numbers, stores them in a list, finds the minimum and maximum numbers, and outputs the sorted list.

### Explanation:
1. **Initialize an empty list**: `number_list` is initialized as an empty list to store the entered numbers.
2. **Loop**: The `while` loop runs as long as the `attempt` is less than or equal to 5.
3. **Enter numbers**: Inside the loop, the user is asked to input a number, which is then added to the `number_list` using `append()`.
4. **Find minimum and maximum**: After all numbers are entered, the minimum is found using `min(number_list)` and the maximum using `max(number_list)`.
5. **Sort the list**: The list `number_list` is sorted using the `sort()` method.
6. **Output**: The stored numbers, the minimum, and the maximum are displayed.

---

## Task 2: Password Input with Limited Attempts

### Description:
Write a program that implements a password prompt. The program asks the user for a password and allows them to guess up to five times. If the correct password is entered, the program displays a success message. After five incorrect attempts, the program displays an error message.

### Explanation:
1. **Correct password**: The correct password is defined.
2. **Initialize variables**: The number of attempts is set to 0, and the maximum number of attempts is set to 5.
3. **Loop**: The `while` loop runs as long as the number of attempts is less than the maximum number of attempts.
4. **Password input**: Inside the `while` loop, the user is asked to input the password.
5. **Password verification**: The entered password is checked.
   - If the password is correct, a success message is displayed and the loop is terminated using `break`.
   - If the password is incorrect and the number of attempts has not been exhausted, an error message is displayed.
   - If the number of attempts is exhausted, an error message is displayed stating that too many incorrect attempts have been made.
