## ✅ Solutions

### 1. Basic Data Types
> **False statement: G**  
> `c` is a string and cannot be concatenated with a number using `+`.  
> → `TypeError: can only concatenate str (not "int") to str`

### 2. Strings & Operators
> **Output:** `PythonPythonPython is awesome!`  
> `text * num` = string repetition  
> `text + num` → `TypeError`  
> → Fix: `text + str(num)` or `f"{text}{num}"`

### 3. Conditionals
> **Correct answer: A**  
> All test cases are correct.  
> `mark >= 40` is valid for "retake possible" — this is a common grading policy.

### 4. Object Data Types
> **Best structure: DataFrame**  
> - Tabular format → easy to read  
> - Built-in methods for filtering, grouping, and aggregation  
> - Supports mixed data types and column names  
> **Solution:**
> ```python
> import pandas as pd
> data = {
>     "Name": ["Alice", "Bob", "Charlie"],
>     "Math": [85, 70, 90],
>     "German": [75, 80, 85],
>     "English": [90, 75, 80]
> }
> df = pd.DataFrame(data)
> df["Average"] = df[["Math", "German", "English"]].mean(axis=1)
> print(df)
> ```

### 5. Loops
> **Output:**  
> ```
> 1 is odd
> 2 is even
> 3 is odd
> 4 is even
> 5 is odd
> ```
> `range(0, 6)` → adds `0` → "0 is even"  
> **To print only even numbers:**
> ```python
> for i in range(2, 6, 2):
>     print(f"{i} is even")
> ```

### 6. Working with Files (CSV)
> **Errors that cause failure:**
> 1. Wrong file format (e.g., `.xlsx`) → `ValueError`  
> 2. Incorrect encoding (e.g., `latin1` instead of `utf-8`) → `UnicodeDecodeError`  
> 3. Wrong delimiter (e.g., `;` instead of `,`) → `ParserError`  
>
> **Robust solution:**
> ```python
> import pandas as pd
>
> def read_csv_safely(filename):
>     try:
>         df = pd.read_csv(filename)
>         print("✅ File loaded successfully!")
>         return df
>     except FileNotFoundError:
>         print("❌ File not found. Check the path.")
>         return None
>     except pd.errors.ParserError as e:
>         print(f"❌ Parsing error: {e}")
>         print("💡 Try: delimiter=';', encoding='utf-8'")
>         return None
>     except UnicodeDecodeError as e:
>         print(f"❌ Encoding error: {e}")
>         print("💡 Try: encoding='utf-8', 'latin1', or 'cp1252'")
>         return None
>     except Exception as e:
>         print(f"❌ Unexpected error: {e}")
>         return None
>
> df = read_csv_safely("books.csv")
> if df is not None:
>     print(df.head())
> ```

### 7. Visualisations
> **Chart shows:** Sales increased from January to March, then slightly decreased in April.  
> **Bar chart > Pie chart:** Bar charts compare values; pie charts show proportions.  
> **Improvements:** Add `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.tight_layout()`

### 8. Creative Task
> **Solution:**
> ```python
> def analyse_even_numbers(numbers):
>     even_numbers = [num for num in numbers if num % 2 == 0]
>     if len(even_numbers) == 0:
>         print("No even numbers found.")
>         return
>     average = sum(even_numbers) / len(even_numbers)
>     print(f"Even numbers: {even_numbers}")
>     print(f"Average: {average:.2f}")
>     if average >= 50:
>         print("Good performance!")
>     else:
>         print("Still room for improvement.")
>
> # Test
> test_data = [15, 20, 25, 30, 40, 45, 50, 60]
> analyse_even_numbers(test_data)
> ```

> **Output:**
> ```
> Even numbers: [20, 30, 40, 50, 60]
> Average: 40.00
> Still room for improvement.
> ```

---

> ✅ **All exercises are now complete with solutions.**  
> 📥 **Save this file as `exercises.md` and use it for teaching, self-study, or exam prep.**
