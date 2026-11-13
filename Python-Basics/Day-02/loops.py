# 1. Print numbers from 1 to 10
print("Exercise 1: Numbers from 1 to 10")

for i in range(1, 11):
    print(i)


# 2. Multiplication table
print("\nExercise 2: Multiplication Table")

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 3. Sum of even numbers
print("\nExercise 3: Sum of Even Numbers")

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print("Sum of even numbers:", total)


# 4. Factorial using while loop
print("\nExercise 4: Factorial")

n = int(input("Enter a number: "))

if n < 0:
    print("Invalid input")
else:
    factorial = 1
    i = 1

    while i <= n:
        factorial *= i
        i += 1

    print("Factorial:", factorial)


# 5. Star pattern using nested loops
print("\nExercise 5: Star Pattern")

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()