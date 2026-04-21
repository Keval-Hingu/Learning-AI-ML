# What is series in pandas?
# A Series is a one-dimensional labeled array that can hold any data type (integers, floats, strings, etc.). It is similar to a column in a spreadsheet or a database table. Each element in a Series has an associated label (index) that can be used to access the data.

# Creating a Series
import pandas as pd
s = pd.Series([1,2,3,4])
print(s) # 0    1 1    2 2    3 3    4 dtype: int64 -> A Series with default index and values from the list [1,2,3,4]

# Custom Index
s = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
print(s) # a    1 b    2 c    3 d    4 dtype: int64 -> A Series with custom index ['a', 'b', 'c', 'd'] and values from the list [1,2,3,4]

# Accessing elements in a Series
print(s[0]) # 1 -> Accessing the first element of the Series using integer index
print(s['a']) # 1 -> Accessing the first element of the Series using custom

# index
print(s[1]) # 2 -> Accessing the second element of the Series using integer index
print(s['b']) # 2 -> Accessing the second element of the Series using custom

# Operations on Series
s1 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([5,6,7,8], index=['a', 'b', 'c', 'd'])
print(s1 + s2) # a    6 b    8 c   10 d   12 dtype: int64 -> Element-wise addition of two Series with the same index

# The above example shows that we can perform element-wise operations on Series with the same index. The result is a new Series where each element is the result of the operation performed on the corresponding elements of the original Series. In this case, we added two Series together, resulting in a new Series where each element is the sum of the corresponding elements from s1 and s2.