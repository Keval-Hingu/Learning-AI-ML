# Performance Analysis

# Time comparison between Python List and Numpy Array
import time

# Python List
a = np.random.rand(1000000)
start = time.time()
b = [x*2 for x in a]
print(time.time() - start)

# Numpy Array
start = time.time()
c = a * 2
print(time.time() - start)

# NumPy is much faster.

# Why?
# Because NumPy is implemented in C and uses optimized algorithms for performance, while Python loops are interpreted and can be slower.

# Python loop → interpreted
# NumPy → compiled C code


# Memory Layout :

# Python List
a = [1,2,3,4]
print(a) # [1, 2, 3, 4] -> Python List
print(a.__sizeof__()) # 96 -> Memory size of the list in bytes

# Numpy Array
b = np.array([1,2,3,4])
print(b) # [1 2 3 4] -> Numpy Array
print(b.nbytes) # 16 -> Memory size of the array in bytes (4 bytes per element for int32)

# Arrays are stored in contiguous blocks of memory, which allows for faster access and better cache performance. Lists, on the other hand, are stored as arrays of pointers to objects, which can lead to more memory overhead and slower access times.
# Row Major Order (C-style) : The last index changes the fastest. For example, in a 2D array, the elements are stored row by row.
# Column Major Order (Fortran-style) : The first index changes the fastest. For example, in a 2D array, the elements are stored column by column.


