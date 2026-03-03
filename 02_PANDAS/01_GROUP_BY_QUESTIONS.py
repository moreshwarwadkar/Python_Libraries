# ----- ----- GROUP BY QUESTIONS BASIC TO ADVANCE ----- -----

# 1) Find the total sales for each Category.
df.groupby('Category')['Total_Sales'].sum()


# 2) Find the average quantity ordered per Category.
df.groupby('Category')['Quantity'].mean()


# 3) Find both total sales AND average quantity per Category in a single query.
df.groupby('Category').agg({
    'Total_Sales': 'sum',
    'Quantity': 'mean'
})


# 4) Find the total sales per City.
df.groupby('City')['Total_Sales'].sum()


# 5) Find the total sales per City and Category combination.

df.groupby(['City','Category'])['Total_Sales'].sum()
# Whenever we want to pass multiple columns, that time we need to inclose in a SQUARE BRACKETS [].


# 6) Find the top-selling Category overall (based on total sales).
df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False).head(1) 


# 7) Find the top-selling Category within each City.

df.groupby(['City', 'Category'])['Total_Sales'].sum().groupby(level=0).idxmax()
