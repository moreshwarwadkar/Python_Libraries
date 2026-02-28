#----- ----- DATAFRAME ----- -----

#- Collection of Rows and Columns. or
#- Collection of Series.

#----- ----- Way To Create ----- -----

#- pd.DataFrame(DICTIONARY)
#['D' and 'F' Should be Uppercase]

import pandas as pd

data = {
    "Name": ["Amit", "Riya", "John"],
    "Age": [25, 22, 30],
    "City": ["Mumbai", "Pune", "Delhi"]
}

df = pd.DataFrame(data)
print(df)

#Output:
'''
   Name  Age    City
0  Amit   25  Mumbai
1  Riya   22    Pune
2  John   30   Delhi
'''

#----- ----- READ CSV FILE

#Syntax :
#import pandas as pd
#df = pd.read_csv("file_name.csv")

#Example: 
import pandas as pd
df = pd.read_csv('dataset.csv',encoding='ISO-8859-1')
print(df)

# encoding : 
# - Sometimes when you read a CSV file, you get this error, That's why we use encoding.
# - encoding tells pandas how to read the characters inside the file.

#--------------------------
# In-Built Functions :

# 1) df.head(n) :
# - By Default it shows the first 5 rows of the DataFrame.

# 2) df.tail(n) :
# - By Default it shows the last 5 rows of the DataFrame.

# 3) df.sample(n) :
# - It is used to randomly select n rows from a DataFrame.




DATA CLEANING :

- It is a Process of removing unwanted data or handling missing values.

1) Rename Column Name
-> Syntax : df.rename(columns = {'old_col1':'new_col1',
				'old_col2':'new_col2',
				'old_coln':'new_coln'},
				inplace=True)

2) Remove Duplicate Rows :
-> df.drop_duplicates(inplace=True)

3) Apply Any String Function : 
-> df['col'].str.function_Name() : To Split, We can anything in parenthesis, then it will split based on this.
-> df['price'].str.strip('$')

# Use Override Here .. Instead of inplace.

4) Removing Unwanted Columns:

-> df.drop(columns = ['col1','col2',...,'coln']) or
-> df.drop(['col1','col2',...,'coln'],axis=1)

-> To Remove Row Pass Index Values inside square bracket [].

# Overrride - df = df.drop(['col1','col2',...,'coln'],axis=1)



5) REOMVING ROWS: 

-> df.drop([row_index1,row_index1,...,row_indexn])


6) CHANGING THE DATATYPE :;

-> df['col1'] = df['col'].astype('datatype')




# HANDLING NULL VALUES :

Handling NULL Values : 

1) Delete the which contains NULL values.

-> df.dropna(inplace=True)
-> df.dropna(how = 'all') : Entire Row Should contain null value.
-> df.dropna(how = 'any') : 
-> inplace = True : Any one Value can be null
-> df.dropna(subset=[ 'col1' , 'coln' ])


2) Filling NULL Values :

-> df.fillna(mean/median/0)



------------------------------------------------------------------

-> Syntax :  df['first'] = df['Full Name'].split(expand=True)[0]
[ TO SPLIT ]


3) Forward Filling :

i)
Syntax : df['col'] = df['col'].ffil() :  [It Will Fill Upper Values in IN PLACE OF NULL values ] It will not fill first value IF IT IS NULL


ii) Backward Filling :

Syntax : df['col'] = df['col'].bfil()  : [ IT WILL FILL LOWER VALUES IN PLACE OF NULL VALUES] IT WILL NOT FILL LAST VALUE IF IT IS NULL



-------------------------------------------------------------------


# GROUP BY :

- IT IS USED TO GROUP THE RECORDS.

SYNTAX : df.groupby('COL')



# ALSO USE AGGREGATE FUNCTIONS : 

- min()
- max()
- mean()
- sum()
- count()

