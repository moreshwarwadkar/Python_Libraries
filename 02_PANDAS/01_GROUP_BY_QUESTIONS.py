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
