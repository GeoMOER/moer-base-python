---
title: A | Thesis Sommer 2025 Base Python Kurs
header:
  image: /assets/images/unit_images/u10/header.png
  image_description: "Android Market-share Worldwide 2018-2020"
  caption: "Mobile Android operating system market share by version worldwide from 2018 to 2020: [StatCounter](https://gs.statcounter.com/android-version-market-share/mobile/worldwide/#monthly-201907-202001) [via Statista](https://www.statista.com/statistics/921152/mobile-android-version-share-worldwide/)"
---

## 🎯 Simple Tasks for Warm-up

### Task 1: Even and Odd Numbers *(6 points)*

Write a program that loops through the numbers from 1 to 20 and prints whether each number is even or odd.

1️⃣ Create a loop from 1 to 20. *(2 points)*  
2️⃣ Use an if-else statement to check even or odd. *(2 points)*  
3️⃣ Print each number with the label "even" or "odd". *(2 points)*

---

### Task 2: Sum of Even Numbers *(6 points)*

Write a program that calculates and prints the sum of all even numbers from 1 to 1000.

1️⃣ Create a loop from 1 to 1000. *(2 points)*  
2️⃣ Use a condition to select only even numbers. *(2 points)*  
3️⃣ Calculate and print the final sum. *(2 points)*

---

### Task 3: D3TD5T *(6 points)*

Write a program that loops through the list of numbers. 

1️⃣ Create a list of numbers (e.g., 1 to 50). *(2 points)*  
2️⃣ Check divisibility by 3, 5, and both. *(2 points)*  
3️⃣ Print the correct label or number. *(2 points)*

---

### Task 4: Finding a Friend *(6 points)*

Write a program that loops through a list of friends  and looks for a specific friend.
- If the friend is found, print a message.

1️⃣ Define a list of friends. *(1 points)*  
2️⃣ Loop through the list to search for a given name. *(3 points)*  
3️⃣ Print a message if found (or if not found). *(2 points)*

---

### Task 5: Replace Characters *(6 points)*

Write a program that goes through a list of fruits and replaces all occurrences of a specific character (e.g., "a") in each word with another character (e.g., "o").


1️⃣ Define a list of fruits. *(1 points)*  
2️⃣ Loop through each fruit and replace a character. *4 points)*  
3️⃣ Print each modified fruit name. *(1 s)*

---

### Task 6: Remove and Add Friends with Loop and Replace *(6 points)*

Write a program that:
- Loops through a list of friends.
- Removes "Ben" if present.
- Adds a new friend "Felix" at position 2.
- Replaces "Anna" directly with "Bella".


1️⃣ Remove "Ben" from the list if present. *(2 points)*  
2️⃣ Add "Felix" at position 2. *(2 points)*  
3️⃣ Replace "Anna" with "Bella". *(2 points)*

---

### 🔍 Task 7: Loop through each name in the list *(15 points)*

**Description:**

In this task, you will practice iterating over a list and stopping a search as soon as a condition is met.

---

**Preparation:**

- Create a string variable my_name containing your own first name.
- Create a boolean variable found, initialized as False.

---

**Steps:**

1️⃣ Loop through the list using an iterator.  
2️⃣ Check if name matches my_name.  
3️⃣ If a match is found:
- Set found = True.
- Immediately **break** the loop.

4️⃣ After the loop, check found:
- If still False, print:  
No registration found for user {searched_name}. You are not yet registered for the course "Python Base Course".
- Replace {searched_name} with your actual my_name variable.

1️⃣ Define my_name and found variables. *1 points)*  
2️⃣ Loop through the list using an iterator, check for a match; if found, set found = True and immediately **break** the loop. *8 points)*  
3️⃣ After the loop, check found:
- If False, print:  
  No registration found for user {searched_name}. You are not yet registered for the course "Python Base Course".
- Replace {searched_name} with your my_name. *(5 points)*


---

### Task 8: 🎲 Game — "Lucky String Duel: You vs Computer" *(15 points)*

**Description:**

In this advanced mini-game, you will play a "lucky string draw" duel against the computer!  
Imagine you both have access to a magical bag containing 100 surprise words.



**Preparation:**

- Create these six variables:
  - myResultB (int, initialized to 0): Counts words starting with "S".
  - myResultBo (int, initialized to 0): Counts words starting with "St".
  - myStrike (int, initialized to 0): Bonus if "Strike" is drawn.
  - comResultB, comResultBo, comStrike: Same for the computer.


**Steps:**

1️⃣ Roll a virtual dice (0 to 99) five times each (you and computer).  
2️⃣ For each roll, pick the word at that index from the list.

---

**Rules:**

- Starts with "S" → +1 point.
- Starts with "St" → +10 points.
- Exactly "Strike" → +100 points.

---

**After all rolls:**

- Calculate total points for both.
- Print a winner message based on scores.
- Print a detailed summary with all variable values.

1️⃣ Create counters for points and prepare a list of 100 words. *(3 points)*  
2️⃣ Simulate five virtual dice rolls for each player and select words based on index. *(6 points)*  
3️⃣ Calculate scores, determine the winner, and print a detailed summary with all variables. *(6 points)*

---

### Task 9: 🗺️ "Visualizing the Largest Cities in Europe Based on Coordinates" *(15 points)*

**Description:**

You will work with the worldcities.csv file (SimpleMaps).

---

**Instructions:**

1️⃣ Download the World Cities dataset as a ZIP from SimpleMaps.  
👉 Use the **free version**.

2️⃣ Unzip and **note the path** to worldcities.csv.

3️⃣ Load it into a pandas DataFrame and **print column names**.

4️⃣ Filter cities in Europe using:
- Latitude: 35° to 72° N.
- Longitude: -25° to 45° E.

5️⃣ **Print city names** from the filtered DataFrame.

6️⃣ Sort by population (descending).

7️⃣ Create a **bar chart** (Matplotlib) for the top 10 largest cities.
- X-axis: City names.
- Y-axis: Population.
- Add title, e.g., *"Top 10 Largest Cities in Europe (by Population)"*.

1️⃣ *(1 points)*  
2️⃣ *(1 points)*  
3️⃣ *(2 points)*
4.  *(4 points)*
5.  *(1 points)*
6.  *(2 points)*
7.  *(4 points)*
---

## ✅ Final Points Overview

- Tasks 1–6: 6 points each (total 36).
- Task 7: 8 points.
- Task 8: 15 points.
- Task 9: 15 points.
- **Total: 74 points**.