import numpy as np
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original Array:")
print(arr)

# -----------------------------
# Accessing values using index
# -----------------------------
print("\nAccessing Elements:")
print("Element at [0][0]:", arr[0][0])
print("Element at [1][2]:", arr[1][2])
print("Element at [2][3]:", arr[2][3])

# -----------------------------
# Mathematical Operations
# -----------------------------
print("\nAddition (+10):")
print(arr + 10)

print("\nSubtraction (-5):")
print(arr - 5)

print("\nMultiplication (*2):")
print(arr * 2)

print("\nDivision (/2):")
print(arr / 2)

# -----------------------------
# NumPy Methods
# -----------------------------

print("\n1. Shape:")
print(arr.shape)

print("\n2. Size:")
print(arr.size)

print("\n3. Number of Dimensions:")
print(arr.ndim)

print("\n4. Data Type:")
print(arr.dtype)

print("\n5. Sum:")
print(np.sum(arr))

print("\n6. Mean:")
print(np.mean(arr))

print("\n7. Maximum:")
print(np.max(arr))

print("\n8. Minimum:")
print(np.min(arr))

print("\n9. Standard Deviation:")
print(np.std(arr))

print("\n10. Transpose:")
print(arr.T)

print("\n11. Flatten:")
print(arr.flatten())

print("\n12. Reshape (4x3):")
print(arr.reshape(4,3))

print("\n13. Sorted Array:")
print(np.sort(arr))

print("\n14. Square Root:")
print(np.sqrt(arr))

print("\n15. Power (Square):")
print(np.power(arr, 2))
