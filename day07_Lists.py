# Day 7 - Python Lists

# Create a list of five programming languages
languages = ["Python", "Java", "JavaScript", "C", "SQL"]

# Print the complete list
print(languages)

# Access individual items
print(languages[0])
print(languages[2])
print(languages[4])

# Access items using negative indexing
print(languages[-1])
print(languages[-2])


# Updating list items

languages = ["Python", "Java", "JavaScript", "C", "SQL"]

languages[1] = "C++"
languages[3] = "HTML"

print("Updated languages:", languages)


# Day 7 - Python Lists

languages = ["Python", "Java", "JavaScript", "C", "SQL"]

# Add a new language
languages.append("HTML")

print(languages)


# Your first exercise
# Create a list of three fruits and use append() to add two more fruits.

Fruits = ["apple", "banana", "mango"]

Fruits.append("orange")
Fruits.append("grapes")

print(Fruits)


# Your exercise
# Create this list:

# Use insert() to add "Mango" at index 1

fruits = ["apple", "banana", "grapes"]

fruits.insert(1, "mango")

print(fruits)


# Your exercise
# Create this list:
# Remove "C++" using remove() and print the updated list.

languages = ["python", "java", "c++", "javascript", "sql"]

languages.remove("c++")
print(languages)


# Your exercise
# Create this list:
# Use pop() to remove the item at index 2.
# Print the removed language.
# Print the updated list.

languages = ["python", "java", "c++", "javascript", "sql"]

removed_lamguage = languages.pop(2)

print("removed language:", removed_lamguage)
print("updated language:", languages)


# Your exercise
# Create this list:
# The complete list.
# The total number of fruits using len().
# The last item using negative indexing.

fruits = ["apple", "banana", "mango", "grapes", "orange", "kiwi"]
count = len(fruits)

print(fruits)
print("total fruits:", count)
print(fruits[-1])


# Create a list containing 10, 20, 30, 40, 50.
# Use a for loop to print every number.
# Calculate the total of all numbers using a variable named total.
# Print the final total.

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    print(number)
    total = total + number

print("Total:", total)


# Your exercise
# Create this list:
# Use a for loop with range() and len() to print:

numbers = [5, 10, 15, 20, 25]
for i in range(len(numbers)):
    print("index:", i, "value:", numbers[i])


# Your exercise
# Create this list:
# Write a program to print:
# 1. The largest number.
# 2. The smallest number.
# 3. The total of all numbers.
# 4. The number of elements in the list.


numbers = [45, 12, 89, 34, 67, 8, 100]

# Calculate total
total = 0

for number in numbers:
    total = total + number

# Count elements
count = len(numbers)

# Find largest and smallest
largest = max(numbers)
smallest = min(numbers)

# Display results
print("Largest:", largest)
print("Smallest:", smallest)
print("Total:", total)
print("Count:", count)


# Your exercise
# Create the following list:
# Write a program that:
# 1. Checks whether "Vamsi" exists in the list.
# 2. Checks whether "Suresh" exists in the list.
# 3. Prints an appropriate message for each search.

employees = ["Rahul", "Arjun", "Vamsi", "Kiran", "Ravi"]

if "Vamsi" in employees:
    print("Vamsi is exists")
else:
    print("Vamsi does not exists")

if "Suresh" not in employees:
    print("Suresh does not exists")


# Your exercise
# Create this list:
# Write a program to:
# 1. Find the index of "Vamsi".
# 2. Find the index of "Ravi".
# 3. Print both positions.
# 4. Check whether "Suresh" exists before trying to find its index.

employees = ["Rahul", "Arjun", "Vamsi", "Kiran", "Ravi"]

position1 = employees.index("Vamsi")
print("Vamsi position:", position1)

position2 = employees.index("Ravi")
print("Ravi position:", position2)

if "Suresh" not in employees:
    print("Suresh does not exsist")


# Exercise 1: Student Marks Calculator
# Create a list:
# Write a program to:
# 1. Print all marks using a for loop.
# 2. Calculate the total marks.
# 3. Calculate the average marks.
# 4. Find the highest mark.
# 5. Find the lowest mark.
# 6. Count the number of subjects.
# 7. Check whether 95 exists in the list.

marks = [85, 72, 90, 65, 88, 95, 76]
for mark in marks:
    print("Marks:", mark)

total = 0
for mark in marks:
    total = total + mark
print("Total:", total)

total = 0
for mark in marks:
    total = total + mark
average = total / len(marks)
print("Average marks:", round(average, 2))

largest = max(marks)
smallest = min(marks)

print("Highest Mark:", largest)
print("Lowest Mark:", smallest)


count = len(marks)
print("Number of subjects:", count)

if 95 in marks:
    print("95 exists")
else:
    print("95 does not exsist")


# leetcode question & solution

# question

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


# solution

nums = [1, 2, 3, 4]

# Step 1: Initialize running total
running_sum = 0

# Step 2: Create an empty result list
result = []

# Step 3: Visit every number
for number in nums:

    # Step 4: Add current number to previous total
    running_sum = running_sum + number

    # Step 5: Store the updated total
    result.append(running_sum)

    # Step 6: Return the final list
print(result)
