# ----- ----- PIVOT_TABLE ----- -----

# - It is used to perform multiple aggregation functionon multiple columns at same time.
# - It is also known as Powerhous of Pandas.

# - Syntax : pf.pivot_table(values=['COL1','COL2',...,'COLn'],index='CATEGORICAL COLUMN',aggfunc=['FunName1','FName2'...,'FNameN'])


# SAMPLE DATASSET (USE FOR FOLLOWING EXAMPLES) : 

import pandas as pd

data = {
    "City":["Mumbai","Mumbai","Pune","Pune","Delhi","Delhi"],
    "Category":["Electronics","Clothing","Electronics","Clothing","Electronics","Clothing"],
    "Sales":[5000,2000,3000,1500,4000,2500]
}

df = pd.DataFrame(data)
print(df)

# OUTPUT : 
'''
City	   Category	      Sales
Mumbai	 Electronics	  5000
Mumbai	 Clothing	      2000
Pune	   Electronics	  3000
Pune	   Clothing	      1500
Delhi	   Electronics	  4000
Delhi	   Clothing	      2500
'''

# EXAMPLE 1 : TOTAL SALES PER CITY 
df.pivot_table(values='Sales', index='City', aggfunc='sum')

# OUTPUT :
'''
City	Sales
Delhi	6500
Mumbai	7000
Pune	4500
'''

# EXAMPLE 2 : SALES PER COTY AND CATEGORY
df.pivot_table(values='Sales', index='City', columns='Category', aggfunc='sum')

# OUTPUT : 
'''
City	Clothing	Electronics
Delhi	  2500	       4000
Mumbai	  2000	       5000
Pune	  1500	       3000
'''


