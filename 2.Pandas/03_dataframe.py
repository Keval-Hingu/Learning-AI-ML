# What is Dataframe in pandas?
# A DataFrame is a two-dimensional labeled data structure that can hold data of different types (integers, floats, strings, etc.). It is similar to a table in a relational database or a spreadsheet. A DataFrame consists of rows and columns, where each column can be thought of as a Series. Each row and column in a DataFrame has an associated label (index) that can be used to access the data.

# Creating a DataFrame
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print(df)
#      Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
# 3    David   40      Houston -> A DataFrame created from a dictionary where
# the keys are column names and the values are lists of data for each column. The DataFrame has 4 rows and 3 columns (Name, Age, City).

# Properties of DataFrame
print(df.shape) # (4, 3) -> The DataFrame has 4 rows and 3 columns
print(df.ndim) # 2 -> The DataFrame is a 2-dimensional data structure
print(df.size) # 12 -> The total number of elements in the DataFrame (4 rows * 3 columns)
print(df.dtypes) # Name    object Age     int64 City    object dtype: object

# The dtypes property shows the data type of each column in the DataFrame. In this case, the 'Name' and 'City' columns are of type 'object' (which is used for string data), while the 'Age' column is of type 'int64' (which is used for integer data).
