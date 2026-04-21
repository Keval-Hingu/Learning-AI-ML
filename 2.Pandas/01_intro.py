# What is pandas?
# Pandas is a powerful and flexible open-source data analysis and manipulation library for Python. It provides data structures and functions needed to work with structured data seamlessly. The primary data structures in pandas are Series (1-dimensional) and DataFrame (2-dimensional), which allow for easy handling of data in a tabular format. Pandas is built on top of NumPy and is designed to make data analysis and manipulation tasks easier and more efficient, especially when working with large datasets. It offers a wide range of functionalities for data cleaning, transformation, aggregation, and visualization, making it an essential tool for data scientists and analysts.

# Need of pandas
# 1. Handling Missing Data -> Pandas provides powerful tools for handling missing data, such as filling in missing values or dropping rows/columns with missing data.
# 2. Data Alignment -> Pandas automatically aligns data based on labels, which makes it easier to work with data from different sources or with different indices.
# 3. Data Manipulation -> Pandas provides a wide range of functions for manipulating data, such as filtering, sorting, grouping, and pivoting.
# 4. Time Series Analysis -> Pandas has built-in support for time series data, making it easier to work with date and time data.
# 5. Data Visualization -> Pandas integrates well with libraries like Matplotlib and Seaborn, allowing for easy data visualization.


# Importing pandas
import pandas as pd


# What is Series and DataFrame?
# Series -> A Series is a one-dimensional labeled array that can hold any data type (integers, floats, strings, etc.). It is similar to a column in a spreadsheet or a database table. Each element in a Series has an associated label (index) that can be used to access the data.
# DataFrame -> A DataFrame is a two-dimensional labeled data structure that can hold data of different types (integers, floats, strings, etc.). It is similar to a table in a relational database or a spreadsheet. A DataFrame consists of rows and columns, where each column can be thought of as a Series. Each row and column in a DataFrame has an associated label (index) that can be used to access the data.


# Creating a Series
s = pd.Series([1,2,3,4])
print(s) # 0    1 1    2 2    3 3    4 dtype: int64 -> A Series with default index and values from the list [1,2,3,4] 

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print(df)
#      Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
# 3    David   40      Houston -> A DataFrame created from a dictionary where the keys are column names and the values are lists of data for each column. The DataFrame has 4 rows and 3 columns (Name, Age, City).


