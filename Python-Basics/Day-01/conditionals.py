
# Day 01 - Python Fundamentals

# Exercise 1: Even or Odd Checker

print("===== Even or Odd Checker =====")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is an Even number")
else:
    print(number, "is an Odd number")

# Exercise 2: Student Grade Calculator

print("\n===== Student Grade Calculator =====")

marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

elif marks >= 90:
    print("Grade: A")

elif marks >= 80:
    print("Grade: B")

elif marks >= 70:
    print("Grade: C")

elif marks >= 60:
    print("Grade: D")

elif marks >= 40:
    print("Grade: E")

else:
    print("Grade: F")