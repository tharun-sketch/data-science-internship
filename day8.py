import matplotlib.pyplot as plt

# Sample Data
students = ["Tharun", "Rahul", "Priya", "Anjali", "Kiran"]
marks = [85, 90, 88, 95, 75]

print("===== DAY 8 - DATA VISUALIZATION =====")

# 1. Bar Chart
plt.figure(figsize=(6,4))
plt.bar(students, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Line Chart
plt.figure(figsize=(6,4))
plt.plot(students, marks, marker="o")
plt.title("Student Marks - Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart
plt.figure(figsize=(6,6))
plt.pie(marks, labels=students, autopct="%1.1f%%", startangle=90)
plt.title("Student Marks Distribution")
plt.show()

print("===== DAY 8 COMPLETED SUCCESSFULLY =====")