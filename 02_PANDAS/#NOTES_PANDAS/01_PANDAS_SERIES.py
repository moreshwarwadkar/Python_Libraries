#----- ----- PANDAS ----- -----
#- Pandas is mainly designed for work with Series and DataFrame.


#- SERIES : 1D Array
#- DATAFRAME : 2D Array (Rows and Column[Columns is also called as series])


#----- ----- Installation Of Pandas ----- -----

- pip install pandas
- import pandas as pd

#----- ----- Series ----- -----

#- pd.Series(collection) -> [set is not allowed in collection]
#- Here 'S' Should be capital in Series Word.


#ExAMPLE 1: (BASIC PROGRAM)

import pandas as pd
import numpy as np

pd.Series([10,20,30])

#Output :
'''
	0
0	10
1	20
2	30

dtype: int64
'''


# ExAMPLE 2 : (name)
# The name is used to give a label (title) to the Series.
pd.Series([10,20,30],name='Numbers')

#OUTPUT :
'''
	Numbers
0	10
1	20
2	30

dtype: int64
'''


# ExAMPLE 3 : (index)
# By default, pandas gives automatic integer index.
# Similar to Above Example [Indexes are : 0 1 2].
# We are customizing the row labels by using 'index'.
pd.Series([10,20,30],name='Numbers',index=['a','b','c'])

#OUTPUT :
'''
	Numbers
a	10
b	20
c	30

dtype: int64
'''


# ExAMPLE 4 : (dtype)
# dtype means Data Type of the values stored in the Series.
# By default, pandas automatically decides the data type (usually int64 for integers).
# But when we write: dtype='int32'
# We are forcing pandas to store data in a specific type.

pd.Series([10,20,30],name='Numbers',index=['a','b','c'],dtype='int32')

#OUTPUT :
'''
    Numbers
a	10
b	20
c	30

dtype: int32
'''


# ExAMPLE 5 : 

pd.Series([10,20,30],name='Numbers',index=['a','b','c'],dtype='float32')

#OUTPUT:
'''
    Numbers
a	10.0
b	20.0
c	30.0

dtype: float32
'''



#----- ----- Filtering ----- -----

#- var[condition]
#Ex. s2[s2>10]

#- var[(condition1) & (condition2)]     [IN CASE OF MULTIPLE CONDITIONS]
#- var[(condition1) | (condition2)]
