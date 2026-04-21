# Numpy Random Module
import numpy as np

# Random Number Generation
a = np.random.rand(4)
print(a) # [0.5488135  0.71518937 0.60276338 0.54488318] -> Array of 4 random numbers between 0 and 1

b = np.random.randint(1, 10, size=5)
print(b) # [1 2 3 4 5] -> Array of 5 random integers between 1 and 9 (10 is not included)   

c = np.random.normal(loc=0, scale=1, size=5)
print(c) # [ 0.49671415 -0.13826436  0.64768854  1.52302986 -0.23415337] -> Array of 5 random numbers drawn from a normal distribution with mean 0 and standard deviation 1

d = np.random.randn(5)
print(d) # [ 0.49671415 -0.13826436  0.64768854  1.52302986 -0.23415337] -> Array of 5 random numbers drawn from a standard normal distribution (mean 0 and standard deviation 1)

e = np.random.randint(0,10,(3,3))
print(e) # [[0 1 2] [3 4 5] [6 7 8]] -> 3x3 array of random integers between 0 and 9 (10 is not included)

# Random Seed
np.random.seed(42)
f = np.random.rand(4)
print(f) # [0.37454012 0.95071431 0.73199394 0.59865848] -> Array of 4 random numbers between 0 and 1, generated with a seed of 42 (same seed will produce the same random numbers)

# Random Shuffle
g = np.array([1,2,3,4,5])
np.random.shuffle(g)
print(g) # [3 5 1 4 2] -> Array of 5 random integers between 1 and 5, shuffled in a random order

# Random Choice
h = np.random.choice([1,2,3,4,5], size=3, replace=False)
print(h) # [2 5 1] -> Array of 3 random integers between 1 and 5, chosen without replacement (no duplicates)
i = np.random.choice([1,2,3,4,5], size=3, replace=True)
print(i) # [2 5 1] -> Array of 3 random integers between 1 and 5, chosen with replacement (duplicates allowed)

# Random Permutation
j = np.random.permutation([1,2,3,4,5])
print(j) # [3 5 1 4 2] -> Array of 5 random integers between 1 and 5, permuted in a random order (same as shuffle but returns a new array instead of modifying the original array)

# Random Sample
k = np.random.sample(5)
print(k) # [0.37454012 0.95071431 0.73199394 0.59865848 0.15601864] -> Array of 5 random numbers between 0 and 1, drawn from a uniform distribution over [0, 1)
