import pandas as pd

print("===== DAY 4 - PANDAS =====")

# Create a DataFrame
data = {
    "Name": ["Tharun", "Rahul", "Priya", "Anjali"],
    "Age": [20, 21, 22, 19],
    "Marks": [85, 90, 88, 95]
}

df = pd.DataFrame(data)

print("\n1. DataFrame")
print(df)

print("\n2. First 2 Rows")
print(df.head(2))

print("\n3. Data Information")
print(df.info())

print("\n4. Statistics")
print(df.describe())

print("\n5. Select Name Column")
print(df["Name"])

print("\n6. Average Marks")
print(df["Marks"].mean())

print("\n===== DAY 4 COMPLETED SUCCESSFULLY =====")