# SHREE GANESHAY NAMAH


# module for data ingestion, cleaning, transformation using pandas
# the source data format would be csv and excel spreadsheets


# code 01
# this code will import (ingest) data from excel sheet

import pandas as pd
df1 = pd.read_excel('C:\\Users\\adity\\Desktop\\reservoir\\moviedata.xlsx')
print(df1)
# end of code block


# inspecting the data skew and distribution
op1 = df1.shape
print(op1)
# end of code

# cde2
op2 = df1.info()
print(op2)
# end of code block

# cde3
op3 = df1.describe()
print(op3)
# end of code block

# cde4
op4 = df1.head()
print(op4)
# end of code block

# cde5
op5 = df1.tail()
print(op5)
# end of code block

# end of the first module of file


# **************************************************************************************


#  module 02
# this module will implement data cleaning functions
#cde 1
dc1 = df1.isnull()
print(dc1)
# code block ends

# cde 2
dc2 = df1.dropna()
print(dc2)
# code block ends

# cde 3
dc3 = df1.fillna(value=10)
print(dc3)
# end of code block



# identifying and removing duplicates
# cde 4
dfdup = df1.duplicated()
print(dfdup)
# print to screen

# cde 5
dropdup = df1.drop_duplicates()
print(dropdup)
print(df1)
# end of code block


# value replacements

# cde 6
repdf = df1.replace({'Horror' : 'Ghost'})
print(repdf)
print(df1)
# end of code block

# data type conversion

df1['runtime'] = df1['runtime'].astype(int)
print(df1)
# end of code block

# changing column to numeric data type
clnum2 = pd.to_numeric(df1['online'], errors='coerce')
print(clnum2)
print(df1)
# end of code block


# string cleaning

# technique for converting strings from lower case to upper case
df1['genre'] = df1['genre'].str.upper()
print(df1)
# end of code block

# function for converting uppercase to lowercase 
df1['genre'] = df1['genre'].str.lower()
print(df1)
# end of code

# lower case to upper case
df1['movie'] = df1['movie'].str.upper()
print(df1)
# end of code block

# lower to upper case
df1['director'] = df1['director'].str.upper()
print(df1)
# end of code block

# to generate error
df1['director'] = df1['director'].str.lower()
print(df1)
# end of code block

# upper to lcase type
df1['movie'] = df1['movie'].str.lower()
print(df1)
# end of code block

# removing whitespaces
df1['director'] = df1['director'].str.strip()
print(df1)
# end of code block



# function to check if a string contains a pattern or substring

ptrn = df1['director'].str.contains('eer')
print(ptrn)
# end of code block



# applying custom functions to elements, rows, columns

df1['imdb'] = df1['imdb'].apply(lambda x: x * 2)
print(df1)
# end of code block

# new code 

import pandas as pd
newdf = pd.read_excel('C:\\Users\\adity\\Desktop\\reservoir\\tstdf.xlsx')
print(newdf)
# end of code block

# cde2
newdf['date'] = pd.to_datetime(newdf['date'])
print(newdf)
# end of code block

# creating a copy of the df
newdf = newdf.copy()
# end of code