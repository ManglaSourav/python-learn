import pandas as pd


game_df = pd.read_csv("./vgsalesGlobale.csv")
print(game_df.head())


# Let’s look at the types of variables in the dataset.
print(game_df.dtypes)

#Let’s print the definitive statistics of the genre variable.
print("\n", game_df.Genre.describe())
# Let’s see the number of subcategories inside the variable.
print("\n", game_df.Genre.value_counts())


print("\n", game_df.Publisher.value_counts())
# print("\n", game_df.head())

# Let’s take a look at the percentage of each value.
print("\n\n", game_df.Genre.value_counts(normalize=True))

# Let’s take a look at Genre’s type.
print("\n\n", type(game_df.Genre.value_counts()))

# Since the type of this object is a Series, you can use Series methods. For example, let’s use the head method.
print("\n\n", game_df.Genre.value_counts().head())


# To illustrate the unique values individually, you can the unique method:
print(game_df.Genre.unique())

# You can see how many single values using nunique method:
print(game_df.Genre.nunique())



# To dispaly the mutual values of two variables as a table, you can use crosstab method.
print(pd.crosstab(game_df.Genre, game_df.Year))


# Let’s take a closer look at the Global Sales column, a numeric type. Let me show the definitive 
# statistics of this variable.
# game_df.Global_Sales.head()
print(game_df.Global_Sales.describe())
print("\n\n", game_df.Global_Sales.value_counts())
print("\n\n", game_df.Global_Sales.mean())


# visualize a Series. Let’s draw the histogram of the Year, a numeric type.
print(game_df.Year.plot(kind="hist"))
print(game_df.Genre.value_counts.plot(kind="hist"))
