
# Day 3: Python Operators

# Arithmetic operators
a = 10
b = 3

print("Addition:", a + b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# Comparison operators
print("Is a greater than b?", a > b)
print("Are they equal?", a == b)

# Logical operators
age = 20
has_id = True

print("Can access:", age >= 18 and has_id)

# Assignment operators
score = 10
score += 5
print("Updated score:", score)


# Beginner — Arithmetic
# Set a = 17 and b = 5. Print their sum, difference, product, quotient, floor quotient, and remainder.

a = 17
b = 5

print("sum :", a + b)
print("difference :", a - b)
print("product :", a * b)
print("quotient :", a / b)
print("floor quotient :", a // b)
print("remainder :", a % b)

# Beginner — Comparison
# Set age = 20. Print whether the age is at least 18, less than 18, and exactly 20.

age = 20
print("whether the age is at least 18 :", age >= 18)
print("age is less then 18 :", age < 18)
print("age exactly 20 :", age == 20)

# Intermediate — Logical operators
# Set age = 22, has_id = True, and has_ticket = False. Print the result of age >= 18 and has_id, has_id and has_ticket, and has_id or has_ticket.

age = 22
has_id = True
has_ticket = False

print(age >= 18 and has_id)
print(has_id and has_ticket)
print(has_id or has_ticket)

# Intermediate — Assignment
# Start with balance = 1000. Add 500, subtract 200, multiply by 2, and divide by 4 using compound assignment operators. Print the balance after each operation.

balance = 1000
print("first balance :", balance)

balance += 500
print("balance after adding 500 :", balance)

balance -= 200
print("balance after subtracting 200 :", balance)

balance *= 2
print("balance after multiplying by 2 :", balance)

balance /= 4
print("balance after dividing with 4 :", balance)

# Challenge — Operator precedence

result = 10 + 2 * 3 ** 2
print(result)

# Advanced — Discount calculator
# Set price = 1500 and discount_percent = 20. Calculate the discount amount and final price. Then use a comparison operator to check whether the final price is less than 1200.

price = 1500
discount_percent = 20
discount_amount = (price * (discount_percent/100))
final_price = (price - discount_amount)

print(discount_amount)
print(final_price)
print(final_price <= 1200)
