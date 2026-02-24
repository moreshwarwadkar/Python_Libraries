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

#Ex. 

import pandas as pd
import numpy as np

pd.Series([10,20,30])

'''
Output :

	0
0	10
1	20
2	30

dtype: int64
'''

#----- ----- Filtering ----- -----

#- var[condition]
#Ex. s2[s2>10]

#- var[(condition1) & (condition2)]     [IN CASE OF MULTIPLE CONDITIONS]
#- var[(condition1) | (condition2)]

#----- ----- DATAFRAME ----- -----

#- Collection of Rows and Columns. or
#- Collection of Series.

#----- ----- Way To Create ----- -----

#- pd.DataFrame(DICTIONARY)
#['D' and 'F' Should be Uppercase]
