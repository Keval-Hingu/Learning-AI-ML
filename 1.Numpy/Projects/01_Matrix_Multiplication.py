# Matrix Multiplication

# Rules for Matrix Multiplication
# 1. The number of columns in the first matrix must be equal to the number of rows in the second matrix.
# 2. The resulting matrix will have the number of rows of the first matrix and the number of columns of the second matrix.

# Example of Matrix Multiplication
import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

# Implement matrix multiplication manually using loops.
c = np.zeros((a.shape[0], b.shape[1])) # Initialize the result matrix with zeros
for i in range(a.shape[0]): # Iterate over the rows of the first matrix 
    for j in range(b.shape[1]): # Iterate over the columns of the second matrix
        for k in range(a.shape[1]): # Iterate over the columns of the first matrix (or rows of the second matrix)
            c[i][j] += a[i][k] * b[k][j] # Multiply and accumulate the results
print(c) # [[19. 22.] [43. 50.]] -> Result of matrix multiplication of a and b using loops

# Implement matrix multiplication using NumPy's dot() function.
d = np.dot(a, b)
print(d) # [[19 22] [43 50]] -> Result of matrix multiplication of a and b using the dot() function


