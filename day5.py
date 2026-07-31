import pandas as pd

print("===== DAY 5 - DATA CLEANING =====")

# Sample dataset with missing values and duplicates
data = {
    "Name": ["Tharun", "Rahul", "Priya", "Rahul", None],
    "Age": [20, 21, None, 21, 22],
    "Marks": [85, 90, 88, 90, None]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

# 1. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Name"] = df["Name"].fillna("Unknown")

# 2. Remove duplicate records
df = df.drop_duplicates()

# 3. Correct data types
df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(int)

print("\nCleaned Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\n===== DAY 5 COMPLETED SUCCESSFULLY =====")