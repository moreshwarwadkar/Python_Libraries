# ----- ----- DATA CLEANING :
# - It is a Process of removing unwanted data or handling missing values.
#============================================



# -----> 1) Rename Column Name :
# - To rename column names in pandas.

# Syntax -->

df.rename(columns={'old_name':'new_name'})
# OR
df.rename(columns = 
          {'old_col1':'new_col1',
				   'old_col2':'new_col2',
				   'old_coln':'new_coln'},
inplace=True)

# EXAMPLE :

df.rename(columns={
    'Salary': 'Monthly_Salary',
    'City': 'Location'
}, inplace=True)

# - If you remove inplace=True, it will NOT change the original DataFrame.
#============================================



# -----> 2) Remove Duplicate Rows :
# It removes duplicate rows from the DataFrame.
# If two rows are completely identical → one will be removed
# inplace=True → changes original DataFrame

# Syntax -->
df.drop_duplicates(inplace=True)


# EXAMPLE (SAMPLE DATA REFERE FOR FOLLOWING EXAMPLES ) :

import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 101],
    "Name": ["Amit", "Riya", "John", "Amit"],
    "Department": ["IT", "HR", "IT", "IT"]
}

df = pd.DataFrame(data)
print(df)

# OUTPUT OF SAMPLE DATA : 

'''
   Emp_ID  Name Department
0     101  Amit        IT
1     102  Riya        HR
2     103  John        IT
3     101  Amit        IT   ← Duplicate row
'''

# EXAMPLE (REMOVE DUPLICATE) :

df.drop_duplicates(inplace=True)

# OUTPUT :
'''
   Emp_ID  Name Department
0     101  Amit        IT
1     102  Riya        HR
2     103  John        IT
'''
#============================================



# -----> 3) Apply Any String Function :

# SYNTAX : 
df['col'].str.function_name()

# EXAMPLE (SAMPLE DATA) :

import pandas as pd

data = {
    "Name": [" Amit ", "Riya ", " John", "Sara"],
    "City": ["Mumbai-India", "Pune-India", "Delhi-India", "Goa-India"],
    "Price": ["$100", "$200", "$150", "$300"]
}

df = pd.DataFrame(data)
print(df)

# OUTPUT :
'''
     Name          City Price
0    Amit   Mumbai-India  $100
1    Riya     Pune-India  $200
2    John   Delhi-India  $150
3    Sara     Goa-India  $300
'''

# EXAMPLE (STRING FUNCTIONS) :

df['Price'].str.strip('$')

# HERE $ SIGNS ARE REMOVED.
# OUTPUT :
'''
0    100
1    200
2    150
3    300
'''

# TIP :  Use Override Here .. Instead of inplace. (df = df['Price'].str.strip('$') ) 
# We Have to store data in same variable again.

# Most Common Interview String Functions
# - .str.strip()
# - .str.split()
# - .str.replace()
# - .str.lower()
# - .str.upper()
# - .str.contains()

#============================================



# -----> 4) Removing Unwanted Columns:

# METHOD 1: 
df.drop(columns=['col1', 'col2'])

# METHOD 2 :
df.drop(['col1', 'col2'], axis=1)

# axis=1 means column
# axis=0 means row


# EXAMPLE (SAMPLE DATA):

import pandas as pd

data = {
    "Emp_ID": [101,102,103],
    "Name": ["Amit","Riya","John"],
    "Department": ["IT","HR","IT"],
    "Salary": [60000,45000,70000]
}

df = pd.DataFrame(data)
print(df)

# OUTPUT :
'''
   Emp_ID   Name Department  Salary
0     101   Amit        IT   60000
1     102   Riya        HR   45000
2     103   John        IT   70000
'''

# EXAMPLE (REMOVING DEPARMENT TABLE) :

df.drop(columns=['Department'], inplace=True)
# OR
df = df.drop(['Department'], axis=1)

# OUTPUT :

'''
   Emp_ID   Name  Salary
0     101   Amit   60000
1     102   Riya   45000
2     103   John   70000
'''
#============================================



# -----> 5) REMOVING ROW :

# SYNTAX :
df.drop([row_index1, row_index2, ...], axis=0)

# EXAMPLE (SAMPLE DATA):

import pandas as pd

data = {
    "Emp_ID": [101,102,103,104],
    "Name": ["Amit","Riya","John","Sara"],
    "Salary": [60000,45000,70000,65000]
}

df = pd.DataFrame(data)
print(df)

# OUTPUT :

'''
   Emp_ID   Name  Salary
0     101   Amit   60000
1     102   Riya   45000
2     103   John   70000
3     104   Sara   65000
'''

# EXAMPLE (REMOVING ROW) :

df.drop([2], axis=0)

# OUTPUT :
'''
	Emp_ID	Name	Salary
0	 101	  Amit	60000
1	 102	  Riya	45000
3	 104	  Sara	65000
'''

# EXAMPLE (TO REMOVE MULTIPLE ROWS) :

df.drop([1,3], axis=0)
# - IT WILL REMOVE 1 OR 3 ROW NUMBER ROWS.

'''
	Emp_ID	Name	Salary
0	101	    Amit	60000
2	103	      John	70000
'''
#============================================



# -----> 6) CHANGING THE DATATYPE :

# SYNTAX : 
df['column_name'] = df['column_name'].astype('new_datatype')

# EXAMPLE (SAMPLE DATA):

import pandas as pd

data = {
    "Emp_ID": ["101", "102", "103"],
    "Salary": ["60000", "45000", "70000"]
}

df = pd.DataFrame(data)
print(df.dtypes)

# OUTPUT :
'''
Emp_ID    object
Salary    object
dtype: object
'''

# EXAMPLE (CHANGE DATATYPE):

df['Salary'] = df['Salary'].astype('int')

# OUTPUT :
'''
Emp_ID    object
Salary     int64
dtype: object
'''

