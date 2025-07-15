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

---

### Task 2: Sum of Even Numbers *(6 points)*
Write a program that calculates and prints the sum of all even numbers from 1 to 1000.

---

### Task 3: D3TD5T *(6 points)*
Write a program that loops through the list of numbers. 
- For numbers divisible by 3, print "D3T". 
- For numbers divisible by 5, print "D5T". 
- For numbers divisible by both 3 and 5, print "D3TD5T". 
- Print all other numbers as normal.

---

### Task 4: Finding a Friend *(6 points)*
Write a program that loops through a list of friends and looks for a specific friend.
- If the friend is found, print a message.

---

### Task 5: Replace Characters *(6 points)*
Write a program that goes through a list of fruits and replaces all occurrences of a specific character (e.g., "a") in each word with another character (e.g., "o").

---

### Task 6: Remove and Add Friends with Loop and Replace *(6 points)*
Write a program that:
- Loops through a list of friends ["Anna", "Ben", "Clara", "David", "Eva"].
- Removes "Ben" if present.
- Adds a new friend "Felix" at position 2.
- Replaces "Anna" directly with "Bella".

---

### 🔍 Task 7: Loop through each name in the list *(8 points)*

**Description:**

In this task, you will practice iterating over a list and stopping a search as soon as a condition is met.

---

**Preparation:**

- Create a string variable `my_name` containing your own first name.
- Create a boolean variable `found`, initialized as `False`.

---

**Steps:**

1️⃣ Loop through the list using an iterator.  
2️⃣ Check if `name` matches `my_name`.  
3️⃣ If a match is found:
- Set `found = True`.
- Immediately **break** the loop.

4️⃣ After the loop, check `found`:
- If still `False`, print:  
No registration found for user {searched_name}. You are not yet registered for the course "Python Base Course".
- Replace `{searched_name}` with your actual `my_name` variable.

---

### Task 8: 🎲 Game — "Lucky String Duel: You vs Computer" *(15 points)*

**Description:**

In this advanced mini-game, you will play a "lucky string draw" duel against the computer!  
Imagine you both have access to a magical bag containing 100 surprise words.

---

**Preparation:**

- Create these six variables:
  - `myResultB` (int, initialized to 0): Counts words starting with "S".
  - `myResultBo` (int, initialized to 0): Counts words starting with "St".
  - `myStrike` (int, initialized to 0): Bonus if "Strike" is drawn.
  - `comResultB`, `comResultBo`, `comStrike`: Same for the computer.

---

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

---

### Task 9: 🗺️ "Visualizing the Largest Cities in Europe Based on Coordinates" *(15 points)*

**Description:**

You will work with the `worldcities.csv` file (SimpleMaps).

---

**Instructions:**

1️⃣ Download the World Cities dataset as a ZIP from SimpleMaps.  
👉 Use the **free version**.

2️⃣ Unzip and **note the path** to `worldcities.csv`.

3️⃣ Load it into a pandas DataFrame and **print column names**.

4️⃣ Filter cities in Europe using:
- Latitude: 35° to 72° N.
- Longitude: -25° to 45° E.

5️⃣ **Print city names** from the filtered DataFrame.

6️⃣ Sort by `population` (descending).

7️⃣ Create a **bar chart** (Matplotlib) for the top 10 largest cities.
- X-axis: City names.
- Y-axis: Population.
- Add title, e.g., *"Top 10 Largest Cities in Europe (by Population)"*.

---

## ✅ Final Points Overview

- Tasks 1–6: 6 points each (total 36).
- Task 7: 8 points.
- Task 8: 15 points.
- Task 9: 15 points.
- **Total: 74 points**.
