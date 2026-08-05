import pandas as pd

# Sample dataset
data = {
    "Students": ["Tharun", "Rahul", "Priya", "Anjali", "Kiran"],
    "Marks": [85, 90, 88, 95, 75]
}

# Create DataFrame
df = pd.DataFrame(data)

# Clean dataset (remove duplicates if any)
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

print("===== DAY 10 - EXPORT DATA =====")
print("Cleaned dataset saved successfully!")
print("\nDataset:")
print(df)
print("\nFile Name: cleaned_students.csv")