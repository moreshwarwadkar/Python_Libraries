# ----- ----- HANDLING NULL VALUES :

#=======================================
# 1) Delete the which contains NULL values.

# - df.dropna()  : Removes rows where any column contains NULL (DEFAULT BEHAVIOUR).
# - df.dropna(inplace=True)  : To Remove Permanently.
# - df.dropna(how='any') : Removes row if any one value is NULL. (DEFAULT BEHAVIOUR)
# - df.dropna(how='all')     : Removes row only if all values in that row are NULL.
# - df.dropna(subset=['Name']) : Remove Row Based on Specific Column.


# EXAMPLE (SAMPLE DATA):

import pandas as pd

data = {
    "Name": ["Amit", "Riya", None, "Sara"],
    "Salary": [60000, None, None, 65000]
}

df = pd.DataFrame(data)
print(df)

# OUTPUT : 
'''
   Name  Salary
0  Amit  60000
1  Riya   None
2  None   None
3  Sara  65000
'''


# i) df.dropna()
df.dropna()

#OUTPUT :
'''
	Name	Salary
0	Amit	60000.0
3	Sara	65000.0
'''


# ii) Using how='any'
df.dropna(how='any')

#OUTPUT:
#(Removed rows 1 and 2)
'''
   Name  Salary
0  Amit  60000
3  Sara  65000
'''

# iii) Using how='all'
df.dropna(how='all')

#OUTPUT:
#(Removed only row 2)
'''
   Name  Salary
0  Amit  60000
1  Riya   None
3  Sara  65000
'''


# iv) Remove NULL Based on Specific Columns
df.dropna(subset=['Salary'])

#OUTPUT :
#Removes rows where Name is NULL only.
'''
Name	Salary
0	Amit	60000.0
3	Sara	65000.0
'''



#=======================================
# 2) Filling NULL Values : It Will Fill 0 Where Null is Present.
# Syntax : df.fillna(value)

#EXAMPLE (SAMPLE DATA):

import pandas as pd

data = {
    "Name": ["Amit", "Riya", "John", "Sara"],
    "Salary": [60000, None, 70000, None],
    "Experience": [3, 2, None, 4]
}

df = pd.DataFrame(data)
print(df)

#OUTPUT :
'''
   Name   Salary  Experience
0  Amit  60000.0        3.0
1  Riya      NaN        2.0
2  John  70000.0        NaN
3  Sara      NaN        4.0
'''


#EXAMPLE :
df.fillna(0, inplace=True)

#OUTPUT:
'''
   Name	 Salary	   Experience
0	 Amit	 60000.0	   3.0
1	 Riya	 0.0	       2.0
2	 John	 70000.0	   0.0
3	 Sara	 0.0	       4.0
'''


#=======================================
# 3) Forward Filling (ffill)
# - It fills NULL values using the previous (upper) non-null value.
# - IMPORTANT NOTE : If the first value is NULL, it will NOT be filled.

# Syntax --> df['column_name'] = df['column_name'].ffill()

#EXAMPLE (SAMPLE DATA) :

import pandas as pd

data = {
    "Salary": [None, 60000, None, 65000, None]
}

df = pd.DataFrame(data)
print(df)

#OUTPUT :
'''
   Salary
0   NaN
1  60000
2   NaN
3  65000
4   NaN
'''


#EXAMPLE :

df['Salary'] = df['Salary'].ffill()

#OUTPUT :
'''
   Salary
0  NaN
1  60000
2  60000
3  65000
4  65000
'''



#=======================================
# 4) Backward Filling (bfill)
# - It fills NULL values using the next (lower) non-null value.
# - IMPORTANT NOTE : If the last value is NULL, it will NOT be filled.

# Syntax ---> df['column_name'] = df['column_name'].bfill()

# Example (SAMPLE DATA) :

import pandas as pd

data = {
    "Salary": [60000, None, None, 65000, None]
}

df = pd.DataFrame(data)
print(df)

#OUTPUT :
'''
   Salary
0  60000
1   NaN
2   NaN
3  65000
4   NaN
'''


#EXAMPLE :
df['Salary'] = df['Salary'].bfill()

#OUTPUT :
'''
   Salary
0  60000
1  65000
2  65000
3  65000
4   NaN
'''
