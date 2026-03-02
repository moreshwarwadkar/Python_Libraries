# ----- ----- GROUP BY ----- -----

# - IT IS USED TO GROUP THE RECORDS.
# - Perform aggregation (min,max,sum, mean, count, etc.)

# SYNTAX ---> df.groupby('column_Name')

# - GroupBy alone does nothing useful.
# - You must apply an aggregation function like:

# 1) .min()
# 2) .max()
# 3) .sum()
# 4) .mean()
# 5) .count()


# EXAMPLE (SAMPLE DATA) :

import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Salary": [60000, 45000, 70000, 65000, 40000, 72000]
}

df = pd.DataFrame(data)
print(df)

#OUTPUT :
'''
  Department  Salary
0        IT    60000
1        HR    45000
2        IT    70000
3   Finance    65000
4        HR    40000
5        IT    72000
'''


# EXAMPLE 1 : Group By Department & Find Total Salary
df.groupby('Department')['Salary'].sum()

#OUTPUT :
'''
Department
Finance     65000
HR          85000
IT         202000
Name: Salary, dtype: int64
'''


# EXAMPLE 2 : Find Average Salary Per Department
df.groupby('Department')['Salary'].mean()

#OUTPUT :
'''

Salary
Department	
Finance	65000.000000
HR	42500.000000
IT	67333.333333

dtype: float64
'''


# EXAMPLE 3 : Count Employees Per Department
df.groupby('Department')['Salary'].count()

#OUTPUT : 
'''
	Salary
Department	
Finance	1
HR	2
IT	3

dtype: int64
'''


# ----- ----- Why do we often use reset_index() after groupby?

# - After groupby(), the grouped column becomes the index, not a normal column.
# - We use reset_index() to convert that index back into a regular column.


# (SAMPLE DATA) :

import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "Finance"],
    "Salary": [60000, 45000, 70000, 65000]
}

df = pd.DataFrame(data)

#OUTPUT :
'''
  Department  Salary
0         IT   60000
1         HR   45000
2         IT   70000
3    Finance   65000
'''

# ---> Without reset_index() :
df.groupby('Department')['Salary'].mean()

#OUTPUT :
# Here, Department is the index.
'''
Department
Finance    65000
HR         45000
IT         65000
Name: Salary, dtype: int64
'''

# ---> With Using reset_index() :
df.groupby('Department')['Salary'].mean().reset_index()

#OUTPUT :
# Now Department is a normal column.
'''
  Department  Salary
0   Finance   65000
1        HR   45000
2        IT   65000
'''

