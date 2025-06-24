---

title: "A | Solutions"
toc: TRUE
toc\_float: TRUE
header:
image: /assets/images/unit\_images/u02/header.png
image\_description: "thinking"
caption: "Image by [username](https://pixabay.com) from pixabay"
----------------------------------------------------------------

# Solutions: Loops in Python

Please save your solutions for Exercises 1 to 4 in a single Python script named `unit06__ex(1-4)code.py`.
For Bonus Exercise, use a separate script named `unit06__ex5code.py`.

---

## ✅ Task 1: Create a List of Numbers

```python
numbers = []
for i in range(3, 31, 3):
    numbers.append(i)
print(numbers)
```

---

## ✅ Task 2: Filter the List

```python
filtered_numbers = []
for number in numbers:
    if number > 15:
        filtered_numbers.append(number)
print(filtered_numbers)
```

---

## ✅ Task 3: Convert to Strings with Tags

```python
tagged_numbers = []
for number in filtered_numbers:
    tagged = "Value: " + str(number)
    tagged_numbers.append(tagged)
print(tagged_numbers)
```

---

## ✅ Task 4: Enter Numbers, Find Maximum and Minimum, and Sort the List

```python
number_list = []
attempt = 0

while attempt < 5:
    value = int(input("Enter a number: "))
    number_list.append(value)
    attempt += 1

print("Entered numbers:", number_list)
print("Minimum:", min(number_list))
print("Maximum:", max(number_list))

number_list.sort()
print("Sorted list:", number_list)
```

---

## ⭐ Task 5: Bonus - Password Input with Limited Attempts

```python
correct_password = "findesraus"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    entered = input("Please enter the password: ")
    if entered == correct_password:
        print("Password correct!")
        break
    else:
        print("Incorrect password. Try again.")
        attempts = attempts + 1
else:
    print("Too many incorrect attempts. Access denied.")
```

---
