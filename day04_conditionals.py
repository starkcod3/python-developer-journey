
# Day 4: Conditional Statements

age = 20

if age >= 18:
    print("You are eligible to register.")

print("Program completed.")


# Day 4: If-Else Statement

age = 16

if age >= 18:
    print("You are eligible to register.")
else:
    print("You are not eligible to register.")

print("Program completed.")


# Day 4: If-Elif-Else Statement

marks = 82

if marks >= 90:
    print("Grade A: Excellent")
elif marks >= 75:
    print("Grade B: Very Good")
elif marks >= 50:
    print("Grade C: Pass")
else:
    print("Grade F: Fail")

print("Grade calculation completed.")


"""Your practice task
Run the program with marks = 82. Then change marks to these values one at a time:
- 95 — should display Grade A.
- 60 — should display Grade C.
- 35 — should display Grade F."""

marks = 82

if marks >= 90:
    print("Gread A : Excellent")
elif marks >= 55:
    print("Grade C: Good")
else:
    print("Grade F : you failed")
print("grade calculation completed")


# Day 4: Nested If Statements

username = "vamsi"
password = "python123"

if username == "vamsi":
    print("Username is correct.")

    if password == "python123":
        print("Login successful.")
    else:
        print("Incorrect password.")

else:
    print("Incorrect username.")


# Age eligibility
# Create an age variable. If the age is 18 or above, print “Eligible”; otherwise, print “Not eligible.”

age = 20

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Even or odd
# Given number = 17, print whether the number is even or odd.

number = 17

if number // 2 == 0:
    print("even number")
else:
    print("odd number")

# Positive, negative, or zero
# Given number = -5, print whether it is positive, negative, or zero.

number = -5

if number > 0:
    print("positive number")
elif number < 0:
    print("negative number")
else:
    print("number is zero")


# Grade calculator
# Given marks = 76, print A for 90+, B for 75–89, C for 50–74, and Fail below 50.

marks = 76

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("fail better luck next time")

# Login validation
# Use nested if statements to check a username and password. Print success only when both match.

username = "bahubali"
password = "why katappa kill bahubali"

if username == "bahubali":
    print("username correct")

    if password == "why katappa kill bahubali":
        print("password is correct")
    else:
        print("password wrong")
else:
    print("username wrong")


# Discount eligibility
# A customer gets a 10% discount if their purchase is at least ₹1,000. If they are also a member, give them a 20% discount instead. Calculate and print the final price.

total = 1200
is_member = True

if total >= 1000 and is_member:
    discount_percent = 20
elif total >= 1000:
    discount_percent = 10
else:
    discount_percent = 0

discount_amount = total * discount_percent / 100
final_price = total - discount_amount

print("Discount:", discount_amount)
print("Final price:", final_price)

# leet code problem
root = [10, 4, 6]
root_left_value = root[1]
root_right_value = root[2]

root_value = root_left_value + root_right_value

if root_value == root[0]:
    print(True)
else:
    print(False)
