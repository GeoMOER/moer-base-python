## Thesis Sommer 2025 Base Python Kurs

### 🔍 Bonus Task — "Check Your Registration"

**Description:**

In this task, you will practice iterating over a list and stopping a search as soon as a condition is met.

Next week (during the Q&A session on **24 July 2025**), you will receive a list of first names. 
names = [
    "Anna", "Paul", "Sofia", "Lukas", "Maria", "Jonas", "Emma", "Noah", "Laura", "Leon",
    "Mia", "Felix", "Lina", "Max", "Lea", "Elias", "Clara", "David", "Sarah", "Tim",
    "Hannah", "Julian", "Emily", "Ben", "Johanna", "Niklas", "Amelie", "Jan", "Marie", "Tom",
    "Lena", "Luis", "Lisa", "Erik", "Julia", "Finn", "Sophie", "Samuel", "Charlotte", "Matteo",
    "Isabella", "Moritz", "Ella", "Adrian", "Melina", "Sebastian", "Zoe", "Fabian", "Alina", "Philipp",
    "Nora", "Christian", "Nele", "Alexander", "Luisa", "Marco", "Viktoria", "Daniel", "Carla", "Kevin",
    "Ronja", "Stefan", "Greta", "Johannes", "Elina", "Oliver", "Ida", "Patrick", "Mila", "Dennis",
    "Thea", "Florian", "Tabea", "Marcel", "Jule", "Roman", "Yara", "Anton", "Frieda", "Patrick",
    "Jasmin", "Marvin", "Helene", "Tobias", "Maja", "Raphael", "Leni", "Valentin", "Kira", "Simon",
    "Mathilda", "Jannik", "Stella", "Georg", "Lotta", "Richard", "Pauline", "Henry", "Josephine", "Karl"
]

Your goal: Write a program that checks whether **your own first name** is in this list.

---

**Before starting, prepare:**

- A string variable `my_name` containing your own first name, e.g., `my_name = "Alex"`.
- A **boolean variable** `found`, initialized as `False`.

---

**How it works:**

1️⃣ Loop through the list using an iterator (e.g., `for name in list_of_names`).  
2️⃣ Check if `name` matches `my_name`.  
3️⃣ If a match is found:

- Set `found = True`.
- Immediately **break** the loop to stop searching.

4️⃣ After the loop, check the value of `found`.

- If `found` is still `False`, print:

No registration found for user {searched_name}. You are not yet registered for the course "Python für Fortgeschrittene"

**Hint:** Replace `{searched_name}` with your actual name (the value of `my_name`).

### 🎲 Game Task — "Lucky String Duel: You vs Computer"

words = [
    "Sun", "Storm", "Strike", "Sound", "Star", "Stone", "Smile", "Stream", "Strong", "Start",
    "Shadow", "Stack", "Structure", "Shine", "Spark", "Space", "Street", "Strike", "Storm", 
    "Sky", "Strike", "Snow", "Strike", "Stellar", "Swim", "Strike", "Shape", "Strike", "Star",
    "Strike", "Stream", "Stack", "Stone", "Strike", "Structure", "Storm", "Strike",
    "Harmony", "Echo", "Wave", "Dream", "Light", "Magic", "River", "Ocean", "Mountain", "Forest",
    "Crystal", "Journey", "Flame", "Vision", "Peace", "Energy", "Rhythm", "Gravity", "Thunder", "Shadow",
    "Glitter", "Whisper", "Galaxy", "Moon", "Aurora", "Blaze", "Breeze", "Strike", "Flare", "Lunar", "Nova",
    "Serenity", "Strike", "Twilight", "Mirage", "Pulse", "Drift", "Mystery", "Orbit", "Ray", "Spirit", "Zen",
    "Glow", "Whirl", "Chase", "Fusion", "Nebula", "Rise", "Quest", "Vortex", "Wild", "Breeze",
    "Motion", "Flash", "Wander", "Sparkle", "Strike", "Charm", "Bloom", "Echoes", "Dawn", "Shimmer", "Surge"
]


**Description:**

In this advanced mini-game, you will play a "lucky string draw" **duel** against the computer!  
Imagine you both have access to a magical bag containing **100 surprise words** (you will receive this list online on **24 July 2025**, during the Q&A session).

Each player (you and the computer) will roll a **100-sided virtual dice** five times to draw words from the list.

---

**Before starting, create these six variables:**

- `myResultB` (integer, initialized to 0): Counts how many of **your** words start with "S".
- `myResultBo` (integer, initialized to 0): Counts how many of **your** words start with "St".
- `myStrike` (integer, initialized to 0): Bonus points if you draw "Strike".

- `comResultB` (integer, initialized to 0): Counts how many of the **computer's** words start with "S".
- `comResultBo` (integer, initialized to 0): Counts how many of the **computer's** words start with "St".
- `comStrike` (integer, initialized to 0): Bonus points if the computer draws "Strike".

---

**How it works:**

1️⃣ You and the computer both roll a virtual dice using `random.randint(0, 99)` five times each.  
2️⃣ For each roll, you (and the computer) pick the word at the corresponding index from the list.

---

**Rules:**

- If the word starts with **"S"**, increase `myResultB` or `comResultB` by 1.
- If it starts with **"St"**, increase `myResultBo` or `comResultBo` by 10.
- If the word is exactly **"Strike"**, add 100 points to `myStrike` or `comStrike`.

---

**End of the game:**

After all rolls:

- Calculate your **total points**: `myResultB + myResultBo + myStrike`.
- Calculate the computer's **total points**: `comResultB + comResultBo + comStrike`.

Then:

- If your total is higher, print:  
  `"Congratulations! You win against the computer!" 🎉`
- If the computer's total is higher, print:  
  `"The computer wins this time. Better luck next time!" 🤖`
- If it's a tie, print:  
  `"It's a draw! Well played both!" ⚖️`

---

**Finally, print a detailed summary for both players, showing all variable values clearly.**

---

### 🌡️ Bonus Task — "Visualizing Global Temperature Changes with NASA Data"

**Description:**

In this task, you will work with real climate data from NASA (GISS Surface Temperature Analysis). 
https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv
You will learn how to load a CSV file, extract important information, analyze it, and finally create a plot using Matplotlib.

---



**Instructions:**

1️⃣ Download and read the following CSV file into a pandas DataFrame:

use -> read_csv(url, skiprows=1) from pandas

2️⃣ Print the **header** of the DataFrame to understand its structure.

3️⃣ Create a **list** that contains the years, print this.

3️⃣ Create a **list** that contains the annual  temperature ofeach year.

4️⃣ Find the **maximum** and **minimum** temperature anomaly in all lists.  
Print these values **together with the corresponding year**.

5️⃣ Create a **line plot** using Matplotlib:

- X-axis: Year
- Y-axis: Temperature anomaly (°C)

Label the axes and add a suitable title, e.g., "Global Temperature Anomalies (NASA GISS)".

---

💬 *If anything is unclear, please write to us!*

