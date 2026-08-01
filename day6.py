import pandas as pd

print("===== DAY 6 - DATA FILTERING =====")

# Create Sample Dataset
data = {
    "Name": ["Tharun", "Rahul", "Priya", "Anjali", "Kiran"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 88, 95, 75]
}

df = pd.DataFrame(data)

print("\n1. Original Dataset")
print(df)

# Filter Rows (Marks greater than or equal to 85)
print("\n2. Students with Marks >= 85")
filtered = df[df["Marks"] >= 85]
print(filtered)

# Select Columns
print("\n3. Name and Marks Columns")
print(df[["Name", "Marks"]])

# Sort Dataset by Marks
print("\n4. Dataset Sorted by Marks (Highest to Lowest)")
sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df)

print("\n===== DAY 6 COMPLETED SUCCESSFULLY =====")