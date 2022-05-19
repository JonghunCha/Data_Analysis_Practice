import pandas

price_df = pandas.read_csv("data/vegetable_price.csv")
quantity_df = pandas.read_csv("data/vegetable_quantity.csv")

print(price_df)
print("\n")
print(quantity_df)
print("\n")

#inner join
print(pandas.merge(price_df, quantity_df, on="Product"))
print("\n")

#left outer join
print(pandas.merge(price_df, quantity_df, on="Product", how="left"))
print("\n")

#right outer join
print(pandas.merge(price_df, quantity_df, on="Product", how="right"))
print("\n")

#full outer join
print(pandas.merge(price_df, quantity_df, on="Product", how="outer"))
print("\n")