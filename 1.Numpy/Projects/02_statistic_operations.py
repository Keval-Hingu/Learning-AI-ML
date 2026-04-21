# Exercise 2
# Implement:

# Mean
# Variance
# Standard deviation

# Using only NumPy (no built-in mean).

# Mean
# Mean is the average of a set of numbers. It is calculated by summing all the numbers and dividing by the count of numbers.
# Formula: mean = np.sum(a) / a.size

import numpy as np
a = np.array([1,2,3,4,5])
mean = np.sum(a) / a.size
print(mean) # 3.0 -> Mean of the array

# Variance
# Variance is the average of the squared differences from the Mean. It is calculated by taking the difference of each number from the mean, squaring it, summing all the squared differences, and dividing by the count of numbers.
# Formula: variance = np.sum((a - mean) ** 2) / a.size
variance = np.sum((a - mean) ** 2) / a.size

# Standard Deviation
# Standard Deviation is the square root of the variance. It is calculated by taking the square root of the variance.
# Formula: std_dev = np.sqrt(variance)
std_dev = np.sqrt(variance) 
print(variance) # 2.0 -> Variance of the array
print(std_dev) # 1.4142135623730951 -> Standard Deviation of the array

# Vectorization
# The above calculations can be vectorized using NumPy's array operations, which are optimized for performance. This means that we can perform the calculations on the entire array at once, rather than using a loop to iterate through each element.
# Vectorized Mean
mean_vectorized = np.sum(a) / a.size
print(mean_vectorized) # 3.0 -> Mean of the array using vectorization
# Vectorized Variance
variance_vectorized = np.sum((a - mean_vectorized) ** 2) / a.size
print(variance_vectorized) # 2.0 -> Variance of the array using vectorization
# Vectorized Standard Deviation
std_dev_vectorized = np.sqrt(variance_vectorized)
print(std_dev_vectorized) # 1.4142135623730951 -> Standard Deviation of the array using vectorization

