# Array Indexing and Slicing

# 1D Array Indexing and Slicing
import numpy as np
a = np.array([4,5,9,8])

# Indexing
print(a[0]) # 4 -> First element of the array
print(a[1]) # 5 -> Second element of the array
print(a[2]) # 9 -> Third element of the array
print(a[3]) # 8 -> Fourth element of the array

# Negative Indexing
print(a[-1]) # 8 -> Last element of the array
print(a[-2]) # 9 -> Second last element of the array
print(a[-3]) # 5 -> Third last element of the array
print(a[-4]) # 4 -> Fourth last element of the array

# Slicing
print(a[0:2]) # [4 5] -> Elements from index 0 to 1 (2 is not included)
print(a[1:3]) # [5 9] -> Elements from index 1
print(a[2:4]) # [9 8] -> Elements from index 2 to 3 (4 is not included)
print(a[:3]) # [4 5 9] -> Elements from index 0 to 2 (3 is not included)
print(a[1:]) # [5 9 8] -> Elements from index 1 to the end of the array
print(a[:]) # [4 5 9 8] -> All elements of the array

# Negative Slicing
print(a[-3:-1]) # [5 9] -> Elements from index -3 to -2 (-1 is not included)
print(a[-2:]) # [9 8] -> Elements from index -2 to the end of the array
print(a[:-2]) # [4 5] -> Elements from index 0 to -3 (-2 is not included)


# 2D Array Indexing and Slicing
b = np.array([[1,2,3,4],[5,6,7,8]])
# Indexing
print(b[0]) # [1 2 3 4] -> First row of the array
print(b[1]) # [5 6 7 8] -> Second row of the array
print(b[0][0]) # 1 -> First element of the first row
print(b[0][1]) # 2 -> Second element of the first row
print(b[0][2]) # 3 -> Third element of the first row
print(b[0][3]) # 4 -> Fourth element of the first row
print(b[1][0]) # 5 -> First element of the second row
print(b[1][1]) # 6 -> Second element of the second row
print(b[1][2]) # 7 -> Third element of the second row
print(b[1][3]) # 8 -> Fourth element of the second row

# Negative Indexing
print(b[-1]) # [5 6 7 8] -> Last row of the array
print(b[-2]) # [1 2 3 4] -> Second last row of the array
print(b[-1][-1]) # 8 -> Last element of the last row
print(b[-1][-2]) # 7 -> Second last element of the last row
print(b[-1][-3]) # 6 -> Third last element of the last row
print(b[-1][-4]) # 5 -> Fourth last element of the last row
print(b[-2][-1]) # 4 -> Last element of the second last row
print(b[-2][-2]) # 3 -> Second last element of the second last row
print(b[-2][-3]) # 2 -> Third last element of the second last row
print(b[-2][-4]) # 1 -> Fourth last element of the second last row

# Slicing
print(b[0:2]) # [[1 2 3 4] [5 6 7 8]] -> Elements from index 0 to 1 (2 is not included)
print(b[0:1]) # [[1 2 3 4]] -> Elements from index 0 to 0 (1 is not included)
print(b[1:2]) # [[5 6 7 8]] -> Elements from index 1 to 1 (2 is not included)
print(b[:1]) # [[1 2 3 4]] -> Elements from index
print(b[1:]) # [[5 6 7 8]] -> Elements from index 1 to the end of the array
print(b[:]) # [[1 2 3 4] [5 6 7 8]] -> All elements of the array

# Negative Slicing
print(b[-2:-1]) # [[1 2 3 4]] -> Elements