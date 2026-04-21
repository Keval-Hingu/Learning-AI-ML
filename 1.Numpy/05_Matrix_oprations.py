# Matrix Operations in Numpy
# In this section, we will learn about matrix operations in Numpy. We will learn how to perform matrix addition, subtraction, multiplication, and other operations using Numpy's array operations, which are optimized for performance.

# Example of matrix operations
import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
# Matrix Addition
c = a + b
print(c) # [[ 6  8] [10 12]] -> Result of adding two matrices element-wise
# Matrix Subtraction
d = a - b
print(d) # [[-4 -4] [-4 -4]] -> Result of subtracting two matrices element-wise
# Matrix Multiplication
e = a * b
print(e) # [[ 5 12] [21 32]] -> Result of multiplying two matrices element-wise
# Matrix Dot Product
f = np.dot(a, b)
print(f) # [[19 22] [43 50]] -> Result of dot product of two matrices
# Matrix Transpose
g = a.T
print(g) # [[1 3] [2 4]] -> Transpose of the matrix a
# Matrix Inverse
h = np.linalg.inv(a)
print(h) # [[-2.   1. ] [ 1.5 -0.5]] -> Inverse of the matrix a 

# Note: The above example shows that we can perform various matrix operations using Numpy's array operations, which are optimized for performance and can take advantage of parallelism and other optimizations under the hood.

# other examples of matrix operations
# 1. Matrix Power
i = np.linalg.matrix_power(a, 2)
print(i) # [[ 7 10] [15 22]] -> Result of raising the matrix a to the power of 2
# 2. Matrix Determinant
j = np.linalg.det(a)
print(j) # -2.0000000000000004 -> Determinant of the matrix a
# 3. Matrix Eigenvalues and Eigenvectors
k = np.linalg.eig(a)
print(k) # (array([-0.37228132,  5.37228132]), array([[-0.82456484, -0.41597356], [ 0.56576746, -0.90937671]])) -> Eigenvalues and Eigenvectors of the matrix a

# Reshapeing a matrix
l = a.reshape(4,1)
print(l) # [[1] [2] [3] [4]] -> Reshaped version of the matrix a with 4 rows and 1 column

# Axis operations
a = np.array([[1,2],[3,4]])
m = np.sum(a, axis=0)
print(m) # [4 6] -> Sum of the elements in the matrix a along the columns (axis=0)
n = np.sum(a, axis=1)
print(n) # [3 7] -> Sum of the elements in the matrix a along the rows (axis=1)

# '@' operator for matrix multiplication
o = a @ b
print(o) # [[19 22] [43 50]] -> Result of matrix multiplication of a and b using the '@' operator

# Difference between a * b and a @ b and a.dot(b)
p = a * b
print(p) # [[ 5 12] [21 32]] -> Result of element
q = a @ b
print(q) # [[19 22] [43 50]] -> Result of matrix multiplication of a and b using the '@' operator
r = a.dot(b)
print(r) # [[19 22] [43 50]] -> Result of matrix multiplication of a and b using the dot() method

# Explanation of the difference between a * b and a @ b and a.dot(b)
# a * b performs element-wise multiplication of the two matrices, which means that it multiplies each element of the first matrix with the corresponding element of the second matrix. The result is a new matrix where each element is the product of the corresponding elements from the input matrices.
# -> explanation of a * b: [[1*5, 2*6], [3*7, 4*8]] -> [[ 5 12] [21 32]]

# a @ b and a.dot(b) both perform matrix multiplication of the two matrices, which means that it multiplies the rows of the first matrix with the columns of the second matrix. The result is a new matrix where each element is the sum of the products of the corresponding elements from the input matrices.
# -> explanation of a @ b and a.dot(b): [[1*5 + 2*7, 1*6 + 2*8], [3*5 + 4*7, 3*6 + 4*8]] -> [[19 22] [43 50]]

