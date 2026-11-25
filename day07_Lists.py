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
