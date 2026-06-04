import numpy as np
import time
import sys

# Python List vs NumPy Performance

size = 1000000

py_list = list(range(size))

start = time.time()
sq_list = [x**2 for x in py_list]
end = time.time()

print("Python List Time:", end-start)

np_arr = np.array(py_list)

start = time.time()
sq_arr = np_arr ** 2
end = time.time()

print("NumPy Array Time:", end-start)

# Memory Usage

print("Python List Size:", sys.getsizeof(py_list))
print("NumPy Array Size:", np_arr.nbytes)

# Broadcasting

arr1 = np.array([1,2,3,4])

arr2 = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

print(arr1 + arr2)

# Normalization Example

arr = np.array([[1,2],[3,4]])

normalized = arr / np.mean(arr)

print(normalized)
