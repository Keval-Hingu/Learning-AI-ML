# What is Broadcasting?
# Broadcasting is a powerful mechanism in NumPy that allows operations to be performed on arrays of different shapes and sizes. It enables you to perform arithmetic operations on arrays without explicitly reshaping them, as long as they are compatible for broadcasting.
# Example of Broadcasting
import numpy as np
a = np.array([1,2,3])
b = np.array([[1],[2],[3]])
# Adding two arrays of different shapes
c = a + b
print(c) # [[2 3 4] [3 4 5] [4 5 6]] -> Result of adding two arrays of different shapes
# Explanation of Broadcasting
# In the above example, we have two arrays a and b. The shape of a is (3,) and the shape of b is (3,1). When we add these two arrays, NumPy automatically broadcasts the smaller array (a) to match the shape of the larger array (b). This means that a is treated as if it were [[1,2,3],[1,2,3],[1,2,3]], which allows us to perform element-wise addition with b. The result is a new array c with the shape (3,3) where each element is the sum of the corresponding elements from a and b.


# Broadcasting Rules
# 1. If the arrays have different numbers of dimensions, the shape of the smaller array is padded with ones on its leading (left) side until both shapes have the same length.
# 2. If the shapes of the arrays do not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
# 3. If in any dimension the sizes disagree and neither is equal to 1, an error is raised.


# Rule 1 Example
a = np.array([1,2,3]) # Shape of a is (3,)
b = np.array([[1],[2],[3]]) # Shape of b is (3,1)
c = a + b
# Exapansion of a: [[1,2,3],[1,2,3],[1,2,3]] -> Shape of a is now (3,3)
# Expansion of b: [[1],[2],[3]] -> Shape of b is now (3,3)
# Now we can perform element-wise addition of a and b
# Addition of a and b: [[1+1, 2+1, 3+1], [1+2, 2+2, 3+2], [1+3, 2+3, 3+3]] -> Shape of c is (3,3)
print(c) # [[2 3 4] [3 4 5] [4 5 6]] -> Result of adding two arrays of different shapes using Rule 1

# Rule 2 Example
a = np.array([1,2,3]) # Shape of a is (3,)
b = np.array([1,1,1]) # Shape of b is (3,)
c = a + b
# Exapansion of a: [1,2,3] -> Shape of a is still (3,)
# Expansion of b: [1,1,1] -> Shape of b is still (3,)
# Now we can perform element-wise addition of a and b
# Addition of a and b: [1+1, 2+1, 3+1] -> Shape of c is (3,)
print(c) # [2 3 4] -> Result of adding two arrays of the same shape

# Rule 3 Example
a = np.array([1,2,3]) # Shape of a is (3,)
b = np.array([1,1]) # Shape of b is (2,)
try:
    c = a + b
except ValueError as e:
    print(e) # operands could not be broadcast together with shapes (3,) (2,) -> Error raised due to incompatible shapes for broadcasting
