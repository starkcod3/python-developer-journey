
# Day 2: Python Variables

name = "Vamsi"
age = 24
hometown = "Kaikaluru"

print(name)
print(age)
print(hometown)

print("My name is", name)
print("I am", age, "years old")
print("My hometown is", hometown)


# Create a variable called student_name and store your name.
student_name = "Ganta Naga Vamsi"
print(student_name)

# Create a variable called student_age and store your age.
student_age = 25
print(student_age)

# Create a variable called learning_goal and store "Python Backend Developer".
learning_goal = "Python Backend Developer"
print(learning_goal)

# Print all three variables using separate print() statements.
my_name = "Naga Vamsi"
my_age = 24
my_goal = "python developer"

print(my_name)
print(my_age)
print(my_goal)


# Day 2: Python Data Types

student_name = "Vamsi"
student_age = 25
percentage = 89.5
is_learning_python = True

print(type(student_name))
print(type(student_age))
print(type(percentage))
print(type(is_learning_python))


# Day 2: Type Conversion

age_text = "25"
age_number = int(age_text)

print(age_number + 1)
print(type(age_number))

price_text = "199.50"
price = float(price_text)

print(price)
print(type(price))

score = 100
score_text = str(score)

print(score_text)
print(type(score_text))


# Exercise 1: String to Integer
# Convert "150" into an integer and add 50. Print the result and its data type.

marks = "100"
orignal_marks = int(marks)

print(orignal_marks)
print(orignal_marks + 50)
print(type(orignal_marks))


# Convert "99.50" into a float and add 10.5. Print the result.
percentage = "99.50"
total_percentage = float(percentage)

print(total_percentage + 10.5)
print(type(total_percentage))

# Convert age = 25 into a string. Print its value and data type.
age = 25
present_age = str(age)

print(present_age)
print(type(present_age))

# The marks are stored as strings. Convert them to integers and calculate the average.
maths = "25"
science = "50"
english = "90"

math = int(maths)
scie = int(science)
eng = int(english)

avg = (math + scie + eng)/3

print(avg)

# Predict the output before running this code:
print(bool("False"))
print(bool(""))
print(bool("0"))
print(bool(0))

# The item prices are stored as strings:
item1 = "199.50"
item2 = "250.75"
item3 = "49.75"

item1 = float(item1)
item2 = float(item2)
item3 = float(item3)

print(item1)
print(item2)
print(item3)

total = (item1 + item2 + item3)

print("total bill:", total)

# Student Marks Calculator
"""Stores three subject marks as strings.
Converts those strings into integers.
Calculates the total and average marks.
Converts the student's name into a string if needed.
Uses a Boolean condition to check whether the average is at least 40.
Prints the student's name, total, average, and whether they passed."""

# Day 2: Student Marks Calculator Challenge

student_name = "Vamsi"

maths_marks = "75"
science_marks = "80"
english_marks = "65"

# Step 1: Convert strings into integers
maths_marks = int(maths_marks)
science_marks = int(science_marks)
english_marks = int(english_marks)

# Step 2: Calculate total marks
total_marks = maths_marks + science_marks + english_marks

# Step 3: Calculate average marks
average_marks = total_marks / 3

# Step 4: Check whether the student passed
passed = average_marks >= 40

# Step 5: Display the results
print("Student Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", round(average_marks, 2))
print("Passed:", passed)
