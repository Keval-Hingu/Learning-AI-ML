
# Normal Python List
a = [4,5,9,8]
b = [1,2,3,4]
c = []

for i in range(len(a)):
    c.append(a[i]+b[i])

print(c)

# Numpy Array

# Why Numpy Array?
# 1. Faster than Python List
# 2. Less Memory
# 3. More Functionality
# 4. Easy to use

import numpy as np

a = np.array([4,5,9,8])
b = np.array([[1,2,3,4],[5,6,7,8]])

# Properties of Numpy Array

# 1. Shape -> It gives the dimensions of the array
print(a.shape) # (4,) -> 1D Array with 4 elements
print(b.shape) # (2,4) -> 2D Array with 2 rows and 4 columns

# 2. ndim -> It gives the number of dimensions of the array
print(a.ndim) # 1 -> 1D Array -> 1 Dimension
print(b.ndim) # 2 -> 2D Array -> 2 Dimensions

# 3. size -> It gives the total number of elements in the array
print(a.size) # 4 -> Total 4 elements in the array
print(b.size) # 8 -> Total 8 elements in the array

# 4. dtype -> It gives the data type of the elements in the array
print(a.dtype) # int64 -> Data type of the elements in the array is int64
print(b.dtype) # int64 -> Data type of the elements in the array is int64

# commonly used data types in numpy
# int -> int32 or int64 depending on the system
# float -> float32 or float64 depending on the system
# bool -> bool

# example of creating numpy array with specific data type
c = np.array([1,2,3,4], dtype=np.float64)
print(c) # [1. 2. 3. 4.] -> The elements are now float64
print(c.dtype) # float64 -> Data type of the elements in the array is float64

# why use specific data type?
# 1. Memory Efficiency -> Using a specific data type can save memory. For example,
# - if you know that your data will only contain integers, using int32 instead of int64 can save memory.
# 2. Performance -> Using a specific data type can improve performance. For example, using float32 instead of float64 can improve performance in some cases, especially when working with large arrays.
