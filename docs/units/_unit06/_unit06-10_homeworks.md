---
title: "A | Assignment"
toc: TRUE
toc_float: TRUE
header:
  image: /assets/images/unit_images/u07/header.png
  image_description: "loop"
  caption: "Photo by [Christopher Kuszajewski](https://pixabay.com)"
---

# Loops in Python

Please save your solutions for Exercises 1 to 4 in a single Python script named `unit06__ex(1-4)code.py`.  
For Bonus Exercise, use a separate script named `unit06__ex5code.py`.

Save both scripts in the same `unit06` folder, compress the folder into a `.zip` file, and upload it to ILIAS.

For more information, please visit the following link:  
https://geomoer.github.io/moer-base-python/unit00/unit00-04_submission_guidelines.html

Make sure your code is clearly structured and includes comments where helpful.

---

# Introduction

This set of tasks is designed so that each step builds on the previous one. Work through them in order to practice your understanding of loops and list manipulation in Python.

## Task 1: Create a List of Numbers

### Instructions:
1. Create a list called `numbers` that contains every third number from 3 to 30 using a `for` loop and `range()`.
2. Print the list.

---

## Task 2: Filter the List

### Instructions:
1. Use the `numbers` list created in Task 1.
2. Create a new list called `filtered_numbers` containing only the numbers greater than 15.
3. Print the new list.

---

## Task 3: Convert to Strings with Tags

### Instructions:
1. Take the `filtered_numbers` list from Task 2.
2. Convert each number into a string and add the prefix `"Value: "` to each element.
3. Store these values in a list called `tagged_numbers` and print it.

---


## Task 4: Enter Numbers, Find Maximum and Minimum, and Sort the List

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

## Task 5: Bonus - Password Input with Limited Attempts

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

