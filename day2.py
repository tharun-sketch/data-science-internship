# ============================
# Day 2 - Python Basics
# Name: Tharun
# ============================

print("===== DAY 2 - PYTHON BASICS =====")

# ----------------------------
# 1. Variables and Data Types
# ----------------------------
print("\n1. Variables and Data Types")

name = "Tharun"
age = 20
height = 5.11
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# ----------------------------
# 2. Operators
# ----------------------------
print("\n2. Operators")

a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# ----------------------------
# 3. User Input
# ----------------------------
print("\n3. User Input")

user_name = input("Enter your name: ")
print("Welcome,", user_name)

# ----------------------------
# 4. If-Else
# ----------------------------
print("\n4. If-Else")

marks = int(input("Enter your marks: "))

if marks >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")

# ----------------------------
# 5. For Loop
# ----------------------------
print("\n5. For Loop")

print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# ----------------------------
# 6. While Loop
# ----------------------------
print("\n6. While Loop")

count = 1
while count <= 5:
    print(count)
    count += 1

# ----------------------------
# 7. Functions
# ----------------------------
print("\n7. Functions")

def add(x, y):
    return x + y

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum =", result)

print("\n===== DAY 2 COMPLETED SUCCESSFULLY =====")