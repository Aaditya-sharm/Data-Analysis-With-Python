import numpy as np

# Creating Arrays
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)

arr2 = np.array([1,2,3,4,5,6])
print(arr2)

# Identity Matrix
arr3 = np.eye(4,4)
print(arr3)

# Full Array
arr4 = np.full((2,3),100)
print(arr4)

# Array Properties
print("Shape:", arr4.shape)
print("Size:", arr4.size)
print("Dimensions:", arr4.ndim)
print("Datatype:", arr4.dtype)

# Indexing & Slicing
print(arr2[1:5:2])

# 2D Array
arr2D = np.array([[1,2,3],[4,5,6]])

print(arr2D[0,2])
print(arr2D[:,1:2])

# 3D Array
arr3D = np.array([
    [[1,2],[3,4],[5,6]],
    [[7,8],[9,10],[11,12]]
])

print(arr3D.shape)
print(arr3D[0,2,0])
print(arr3D[:,1:2,:])

# Mathematical Functions
arr5 = np.array([1,2,3,4,5])
print("Mean:", np.mean(arr5))
print("Median:", np.median(arr5))
