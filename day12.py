import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# DAY 12 - PROJECT IMPROVEMENT
# Student Marks Data Analysis
# =========================================================

# Create sample dataset
data = {
    "Students": ["Tharun", "Rahul", "Priya", "Anjali", "Kiran"],
    "Marks": [85, 90, 88, 95, 75]
}

# Create DataFrame
df = pd.DataFrame(data)

# =========================================================
# DATA ANALYSIS
# =========================================================

total_marks = df["Marks"].sum()
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

print("===== DAY 12 - DATA ANALYSIS =====")
print()
print(df)
print()
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

# =========================================================
# CHART 1 - BAR CHART
# =========================================================

plt.figure(figsize=(8, 5))

plt.bar(df["Students"], df["Marks"])

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.tight_layout()

# Save chart
plt.savefig("day12_bar_chart.png")

# Close chart
plt.close()

# =========================================================
# CHART 2 - LINE CHART
# =========================================================

plt.figure(figsize=(8, 5))

plt.plot(
    df["Students"],
    df["Marks"],
    marker="o"
)

plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.tight_layout()

# Save chart
plt.savefig("day12_line_chart.png")

# Close chart
plt.close()

# =========================================================
# FINAL MESSAGE
# =========================================================

print()
print("===== DAY 12 COMPLETED SUCCESSFULLY =====")
print("Project formatting, comments, charts and code readability improved.")
print()
print("Files created:")
print("1. day12_bar_chart.png")
print("2. day12_line_chart.png")