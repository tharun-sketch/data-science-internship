import numpy as np

print("===== DAY 3 - NUMPY =====")

# 1. Create Arrays
print("\n1. Creating Arrays")
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# 2. Array Information
print("\n2. Array Information")
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)

# 3. Array Operations
print("\n3. Array Operations")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

# 4. Mathematical Functions
print("\n4. Mathematical Functions")

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 5. Indexing
print("\n5. Indexing")

print("First Element:", arr[0])
print("Last Element:", arr[-1])

print("\n===== DAY 3 COMPLETED SUCCESSFULLY =====")