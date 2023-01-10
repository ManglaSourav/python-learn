

# Pandas is an important library for data preprocessing. 
# Pandas often uses libraries such as NumPy and SciPy for numerical 
# computations and Matplotlib to visualize data.

# Series can only contain single list with index, whereas dataframe can be made of
# more than one series

# ctrl+z to run python file: manual key binding 


import pandas as pd

# print(pd.__version__)

# Series is a one-dimensional object and index start from 0 and represents a column:
series = pd.Series([1, "john", 3.5, "hey"])
print(series)
print(series.values)
# You can change the indexes:
series2 = pd.Series([1,2.5,3,"4"],["a","b","c","d"])
print(series2)
print(series2["a"])
print(series2.index)
# for i in series2.index:
#     print(i)


# You can convert data types such as list, tuple, or dictionary to Series structure:
score = {"jane":90, "bill":100,"cat":95}
s3 = pd.Series(score)
print(s3)
# You can choose specific names using the operations:
print(s3[s3>90])

s3[s3<96] = 99
print(s3)
print("cat" in s3)

# You can apply mathematical operations to Series:
print(s3/10)
print(s3**2)

# To see missing data, you can the isnull method:
print(s3.isnull())
