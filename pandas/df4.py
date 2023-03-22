# Indexing & Selecting & Filtering in Pandas
import pandas as pd
import numpy as np


s1 = pd.Series(np.arange(5), index=["a","b","c","d","e"])
print(s1)


# Working with Index in Series
print(s1["c"])
print(s1[2])

# You can slice the data.
print("\n\n",s1[0:2])

# Let’s select the specific rows.
print("\n\n",s1[[0, 2]])
print("\n\n",s1[["a", "c"]])

# Filtering in Series
print("\n\n",s1[s1>2])

# You can slice the values.
print("\n\n",s1["a":"c"])

# You can assign a value to the sliced piece.
s1["a":"c"] = 5
print("\n\n", s1)

# Now, I’m going to use a negative index.
print("\n\n", s1[-1])

# Selecting in DataFrame :To show how to index in DataFrame, let me create a DataFrame.
# print(np.arange(16).reshape(4,4))
df1 = pd.DataFrame(np.arange(16).reshape(4,4), 
                   index = ["London", "Paris", "Berlin", "Istanbul"],
                   columns=["one", "two", "three", "four"])
print("\n\n", df1)

# You can select more than one column.
print("\n\n", df1["two"])
print("\n\n", df1[["two", "three"]])

# rows
print("\n\n", df1[:3])

# Filtering in DataFrame
print("\n\n", df1[df1["four"]>6])

#You can assign data to specific values.
df1[df1["four"]<6] = 0
print("\n\n", df1)

# Selecting with iloc and loc methods: You can use the iloc method to select a row using the row’s index.
print("\n\n", df1.iloc[1])

# You can select the specific columns of the row.
print("\n\n", df1.iloc[1,[1,2,3]])


# You can select specific columns of multiple rows.
print("\n\n", df1.iloc[[1,3],[1,2,3]])

# Let’s take a look at the loc method. You need to use names for loc.
print("\n\n", df1.loc["Paris",["one", "two"]])

# Let’s select the rows up to Paris and the column named four.
print("\n\n", df1.loc[:"Paris","four"])




