import pandas as pd

print("===== DAY 7 - DATA ANALYSIS =====")

# Sample Dataset
data = {
    "Name": ["Tharun", "Rahul", "Priya", "Anjali", "Kiran"],
    "Marks": [85, 90, 88, 95, 75]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

# Total Marks
print("\n1. Total Marks:")
print(df["Marks"].sum())

# Average Marks
print("\n2. Average Marks:")
print(df["Marks"].mean())

# Minimum Marks
print("\n3. Minimum Marks:")
print(df["Marks"].min())

# Maximum Marks
print("\n4. Maximum Marks:")
print(df["Marks"].max())

# Count of Students
print("\n5. Total Number of Students:")
print(df["Marks"].count())

print("\n===== DAY 7 COMPLETED SUCCESSFULLY =====")