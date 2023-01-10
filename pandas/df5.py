# You’re given two dataframes: transactions and products.
# The transactions dataframe contains transaction ids, product ids, and the total amount
# of each product sold.
# The products dataframe contains product ids and prices.
# Write a function to return a dataframe containing every transaction with a total
# value of over $100. Include the total value of the transaction as a new column in
# the dataframe.

import pandas as pd

transactions = { "transaction_id" : [1, 2, 3, 4, 5], 
                 "product_id" : [101, 102, 103, 104, 105], 
                 "amount" : [3, 5, 8, 3, 2]}

products = { "product_id" : [101, 102, 103, 104, 105], 
             "price" : [20.00, 21.00, 15.00, 16.00, 52.00]}

df_transactions = pd.DataFrame(transactions)
df_products = pd.DataFrame(products)
df_transactions["total_value"] = df_transactions["amount"]*df_products["price"]
df_transactions[df_transactions["total_value"]>100]
print()
