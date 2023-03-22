import pandas as pd
import numpy as np


# add two series
s1=pd.Series(np.arange(4),
             index=["a","c","d","e"])
s2=pd.Series(np.arange(5),
             index=["a","c","e","f","g"])
print(s1, s2)
print(s1+s2)


# adding two dfs
df1=pd.DataFrame(
    np.arange(6).reshape(2,3),
    columns=list("ABC"),
    index=["Tim","Tom"])
df2=pd.DataFrame(
    np.arange(9).reshape(3,3),
    columns=list("ACD"),
    index=["Tim","Kate","Tom"])
print(df1, df2)
print(df1+df2)

print(df1.add(df2, fill_value=0))
print(1/df1)
print(df1*2)

# Let’s take a look at the first row of the df2.
print(df1.iloc[0])

df=pd.DataFrame(
    np.random.randn(4,3),
    columns=list("ABC"),
    index=["Kim","Susan","Tim","Tom"])
df = abs(df)
print(df)
f=lambda x:x.max()-x.min()
# default columns wise
print(df.apply(f))
# apply row wise
print(df.apply(f,axis=1))
