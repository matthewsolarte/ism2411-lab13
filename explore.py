# Reflection
#
# 1. A boolean filter asks a yes or no question about every row, like "is the
#    region South?". pandas builds a column of True and False answers, then
#    keeps only the rows that got True and drops the rest.
#
# 2. df["revenue"] gives back a Series, which is one column of values.
#    df[["revenue"]] gives back a DataFrame that has one column. It matters
#    when the next step expects a table, like saving to CSV with a header,
#    joining, or selecting more than one column, and when the next step
#    expects a Series, like math on a single column or .unique().
#
# 3. pandas can redo the whole job on 5,000 rows, or 5 million, in one run
#    with the same exact steps every time. In Excel you redo the filters and
#    sorts by hand each time the data changes, which is slow and easy to get
#    wrong.

import pandas as pd


# Exercise 1: Load the data
print("Exercise 1: load the data")
df = pd.read_csv("data/retail_sales.csv")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.dtypes)


# Exercise 2: Filter by region
print()
print("Exercise 2: South region only")
south = df[df["region"] == "South"]
print("South rows:", len(south))
print(south.head())
print("Every region is South:", (south["region"] == "South").all())


# Exercise 3: Top 5 by revenue
print()
print("Exercise 3: top 5 orders by revenue")
top5 = df.sort_values("revenue", ascending=False).head(5)
print(top5)


# Exercise 4: Two-condition filter
print()
print("Exercise 4: South orders over $1,000")
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]
print("Rows:", len(big_south))
print(big_south.head())
print("All rows over $1,000:", len(df[df["revenue"] > 1000]))


# Exercise 5: New column
print()
print("Exercise 5: revenue per unit")
df["per_unit"] = df["revenue"] / df["quantity"]
print(df.head())
print("Mean per_unit:", round(df["per_unit"].mean(), 2))


# Exercise 6: Unique values
print()
print("Exercise 6: regions")
print(df["region"].unique())
print(df["region"].value_counts())


# Exercise 7: Select columns
print()
print("Exercise 7: region, product, revenue only")
subset = df[["region", "product", "revenue"]]
print("Shape:", subset.shape)


# Exercise 8: Save
print()
print("Exercise 8: save")
df.to_csv("data/explored.csv", index=False)
print("Saved data/explored.csv")
