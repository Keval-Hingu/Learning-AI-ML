# Vectorization in NumPy

#what is vectorization?
# Vectorization is the process of converting an algorithm from operating on a single 
# value at a time to operating on a set of values at one time. This is achieved by 
# using NumPy's array operations, which are optimized for performance.

# Example of vectorization
import numpy as np
a = np.array([4,5,9,8])
b = np.array([1,2,3,4])

# Normal Python List
c = []
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c) # [5, 7, 12, 12] -> Result of adding two lists element-wise

# Numpy Array
d = a + b
print(d) # [5 7 12 12] -> Result of adding two arrays element-wise

# The above example shows that we can add two arrays element-wise using the + operator, which is much faster than using a for loop to add two lists element-wise. This is because NumPy's array operations are optimized for performance and can take advantage of parallelism and other optimizations under the hood.

# other examples of vectorization

# 1. Multiplication
e = a * b
print(e) # [ 4 10 27 32] -> Result of multiplying two arrays element-wise

# 2. Division
f = a / b
print(f) # [4. 2.5 3. 2.] -> Result of dividing two arrays element-wise

# 3. Subtraction
g = a - b
print(g) # [3 3 6 4] -> Result of subtracting two arrays element-wise

# 4. Power
h = a ** b
print(h) # [  4  25 729 4096] -> Result of raising one array to the power of another array element-wise

# 5. Modulo
i = a % b
print(i) # [0 1 0 0] -> Result of taking the modulo of two arrays element-wise

# 6. Comparison
j = a > b
print(j) # [ True  True  True  True] -> Result of comparing two arrays element-wise

k = a < b
print(k) # [False False False False] -> Result of comparing two arrays element-wise

l = a == b
print(l) # [False False False False] -> Result of comparing two arrays element-wise

m = a != b
print(m) # [ True  True  True  True] -> Result of comparing two arrays element-wise

n = a >= b
print(n) # [ True  True  True  True] -> Result of comparing two arrays element-wise

o = a <= b
print(o) # [False False False False] -> Result of comparing two arrays element-wise

# why is vectorization more faster?
# 1. Vectorization allows for the use of optimized libraries and hardware acceleration, which can significantly improve performance.
# 2. Vectorization reduces the overhead of Python's for loops and function calls, which can be slow when working with large datasets.
# 3. Vectorization allows for the use of parallelism, which can further improve performance when working with large datasets.

