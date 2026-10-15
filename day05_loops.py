for i in range(5):
    print("Hello Python")

# Exercise 1 — Print numbers
# Print the numbers from 1 to 10, one number per line.
# Hint: Use range(1, 11).

for i in range(1, 11):
    print(i)


# Exercise 2 — Even numbers
# Print the even numbers from 2 to 20.
# Hint: Use range(2, 21, 2)

for i in range(2, 21, 2):
    print(i)

# Exercise 3 — Multiplication table
# Print the 5 times table, from 5 × 1 through 5 × 10.
# Hint: Use a loop from 1 to 10 and multiply i by 5.

for i in range(1, 11):
    print(i * 5)

# Exercise 4 — Calculate a total
# Calculate the sum of numbers from 1 to 5.
# Hint: Start total at 0 and add i during each iteration.

total = 0

for i in range(1, 6):
    total = total + i

print("Total:", total)

# Exercise 5 — Print 1 to 20
# Easy
# Print numbers from 1 to 20, each on a new line.

for i in range(1, 21):
    print(i)

# Exercise 6 — Countdown
# Easy
# Print numbers from 10 down to 1.

for i in range(10, 0, -1):
    print(i)

# Exercise 7 — Odd numbers
# Easy
# Print all odd numbers from 1 to 19.

for i in range(1, 20, 2):
    print(i)

# Exercise 8 — Multiplication table
# Easy
# Print the 7 times table from 7 × 1 to 7 × 10.

for i in range(1, 11):
    print(i * 7)

# Exercise 9 — Squares
# Medium
# Print each number from 1 to 10 and its square, such as 1 → 1, 2 → 4.

for i in range(1, 11):
    square = i * i
    print(i, "->", square)

# Exercise 10 — Sum from 1 to 10
# Medium
# Calculate and print the sum of all numbers from 1 to 10.
total = 0

for i in range(1, 11):
    total = total + i

print("Total:", total)

# Exercise 11 — Count by 5
# Medium
# Print 5, 10, 15, ... up to 100.

for i in range(1, 21):
    print(i * 5)

# Exercise 12 — Custom sequence
# Medium
# Print 20, 18, 16, ... down to 2.

for i in range(20, 0, -2):
    print(i)

for i in range(5, 51, 5):
    print(i)


total = 0

for i in range(2, 21, 2):
    total = total + i

print("Sum of even numbers:", total)

for i in range(1, 6):
    print("*" * i)
