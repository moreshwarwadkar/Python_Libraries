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

#Example 1: 
import pandas as pd
df1 = pd.read_csv('dataset.csv',encoding='ISO-8859-1')
print(df1)

# encoding : 
# - Sometimes when you read a CSV file, you get this error, That's why we use encoding.
# - encoding tells pandas how to read the characters inside the file.

#Example 2:
import pandas as pd

data = {
    "Emp_ID": [101,102,103,104,105,106,107],
    "Name": ["Amit","Riya","John","Sara","Rahul","Neha","Arjun"],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance"],
    "Gender": ["Male","Female","Male","Female","Male","Female","Male"],
    "Salary": [60000,45000,70000,65000,40000,72000,68000],
    "Experience": [3,2,5,4,1,6,5],
    "City": ["Mumbai","Pune","Mumbai","Delhi","Pune","Mumbai","Delhi"]
}

df = pd.DataFrame(data)

#OUTPUT :
'''
   Emp_ID   Name Department  Gender  Salary  Experience    City
0     101   Amit         IT    Male   60000           3  Mumbai
1     102   Riya         HR  Female   45000           2    Pune
2     103   John         IT    Male   70000           5  Mumbai
3     104   Sara    Finance  Female   65000           4   Delhi
4     105  Rahul         HR    Male   40000           1    Pune
5     106   Neha         IT  Female   72000           6  Mumbai
6     107  Arjun    Finance    Male   68000           5   Delhi
'''

#[CONSIDER EXAMPLE 2 DataFrame FOR FOLLOWING EXAMPLES]


#--------------------------------
# In-Built Functions :

# 1) df.head(n) :
# - By Default it shows the first 5 rows of the DataFrame.

#Example :
df.head()

#OUTPUT :
'''
   Name   Age   City
0  Amit    25  Mumbai
1  Riya    22  Pune
2  John    30  Delhi
3  Sara    28  Delhi
4  Rahul   26  Pune
'''

#===============================
# 2) df.tail(n) :
# - By Default it shows the last 5 rows of the DataFrame.

#EXAMPLE :

df.tail()

#OUTPUT :
'''
   Emp_ID   Name Department  Gender  Salary  Experience   City
2     103   John        IT    Male   70000           5  Mumbai
3     104   Sara   Finance  Female   65000           4   Delhi
4     105  Rahul        HR    Male   40000           1    Pune
5     106   Neha        IT  Female   72000           6  Mumbai
6     107  Arjun   Finance    Male   68000           5   Delhi
'''


#===============================
# 3) df.sample(n) :
# - It is used to randomly select n rows from a DataFrame.

#EXAMPLE :

df.sample()
#[IF WE HAVE NOT GIVE ANY NUMBER IN FUNCTION, SO IT WILL GIVE ONLY 1 RECORD ]

#OUTPUT :
'''
   Emp_ID   Name Department  Gender  Salary  Experience   City
5     106   Neha        IT  Female   72000           6  Mumb
'''


#===============================
# 4) df.info():

# ---> We use it to:
# - Check missing values
# - Check data types
# - Understand dataset structure

#EXAMPLE :

df.info()

#OUTPUT: 
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7 entries, 0 to 6
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Emp_ID       7 non-null      int64
 1   Name         7 non-null      object
 2   Department   7 non-null      object
 3   Gender       7 non-null      object
 4   Salary       7 non-null      int64
 5   Experience   7 non-null      int64
 6   City         7 non-null      object
dtypes: int64(3), object(4)
memory usage: 520.0+ bytes
'''


#===============================
# 5) df.shape : (NO PARENTHESIS NEEDED, Because shape is an attribute not a function.)
# - It returns the number of rows and columns in a DataFrame as a tuple.
# - If You want Only Rows : df.shape[0] --> 7
# - If You want Only Column : df.shape[1] --> 7

#EXAMPLE : 

df.shape

#OUTPUT:
'''
(7, 7)  : (number_of_rows, number_of_columns)
'''


#===============================
# 6) df.columns : (NO PARENTHESIS NEEDED, Because columns is an attribute not a function.)
# - It shows list of column names.

#EXAMPLE :

df.columns

#OUTPUT :
'''
Index(['Emp_ID', 'Name', 'Department', 'Gender', 'Salary', 'Experience',
       'City'],
      dtype='object')
'''


#===============================
# 7) df.describe() :
'''
It gives statistical summary of numerical columns:

✔ count
✔ mean
✔ standard deviation (std)
✔ minimum value
✔ 25% (Q1)
✔ 50% (median)
✔ 75% (Q3)
✔ maximum value
'''

'''
It only works for numeric columns by default:
- Emp_ID
- Salary
- Experience

It does NOT show summary for:
- Name
- Department
- Gender
- City
'''

#EXAMPLE :

df.describe()

#OUTPUT :
'''
        Emp_ID        Salary     Experience
count   7.000000     7.000000      7.000000
mean  104.000000  60000.000000      3.714286
std     2.160247  12083.045973      1.799471
min   101.000000  40000.000000      1.000000
25%   102.500000  52500.000000      2.500000
50%   104.000000  65000.000000      4.000000
75%   105.500000  69000.000000      5.000000
max   107.000000  72000.000000      6.000000
'''

#===============================
# 8) df['column_name'].value_counts()
# - It is used to count the frequency of unique values in a column.

#EXAMPLE :

df['Gender'].value_counts()

#OUTPUT :
'''
Male      4
Female    3
Name: Gender, dtype: int64
'''


#===============================
# 9) df.sort_values(by="column_name", ascending=True/False)
# - It is used to sort a DataFrame by one or more columns. 
# - The ascending parameter controls whether sorting is ascending or descending.

#EXAMPLE :

df.sort_values(by="Salary", ascending=False)

#OUTPUT :

'''
   Emp_ID   Name Department  Gender  Salary  Experience   City
5     106   Neha        IT  Female   72000           6  Mumbai
2     103   John        IT    Male   70000           5  Mumbai
6     107  Arjun   Finance    Male   68000           5   Delhi
3     104   Sara   Finance  Female   65000           4   Delhi
0     101   Amit        IT    Male   60000           3  Mumbai
1     102   Riya        HR  Female   45000           2    Pune
4     105  Rahul        HR    Male   40000           1    Pune
'''


#===============================
# 10) df.T : [IT IS AN ATTRIBUTE NOT A FUNCTION]
# - It is used to transpose a DataFrame. It converts rows into columns and columns into rows.

#EXAMPLE :

df.T

#OUTPUT :
'''
                     0       1       2       3       4       5       6
Emp_ID              101     102     103     104     105     106     107
Name               Amit    Riya    John    Sara   Rahul    Neha   Arjun
Department            IT      HR      IT  Finance      HR      IT  Finance
Gender              Male  Female    Male  Female    Male  Female    Male
Salary             60000   45000   70000   65000   40000   72000   68000
Experience             3       2       5       4       1       6       5
City              Mumbai    Pune  Mumbai   Delhi    Pune  Mumbai   Delhi
'''


#===============================
# 11) df.loc[row_index, column_name] :
# - It is used to select data using row labels and column names.

#EXAMPLE :

df.loc[5, 'Name']

#OUTPUT :
'''
Neha
'''

#===============================
# 12) df.iloc[row_start:row_end, column_start:column_end]
# - It is used because a DataFrame is two-dimensional. 
# - The first part selects rows by position, and the second part selects columns by position.
# - Important: iloc does NOT include the last index.

#EXAMPLE :

df.iloc[0:2, 0:3]

#OUTPUT :

'''
	Emp_ID	Name	Department
0	101	    Amit	    IT
1	102	    Riya	    HR

'''


#===============================
# 13) df.loc[row_slice, [col1, col2, ..., coln]]
# - It is used to select specific rows and specific columns using labels.

#EXAMPLE :

df.loc[0:3, ['Gender', 'Salary']]

#OUTPUT :
'''
   Gender  Salary
0    Male   60000
1  Female   45000
2    Male   70000
3  Female   65000
'''




















































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

