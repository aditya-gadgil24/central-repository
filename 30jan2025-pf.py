# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:44:54 2025

@author: adity
"""

# Shree Ganeshay namah

# MODULE 1

# code no 001

# using all the functions of pandas module for practice

import pandas as pd
df01 = pd.read_csv('C:\\Users\\adity\\Desktop\\reservoir\\profile.csv')
print(df01)
# reading data from csv into a dataframe

# df summary functions
# reading the first few top rows
toplines = df01.head(5)
print(toplines)
# print to screen

# reading the few botton rows
bottomlines = df01.tail(5)
print(bottomlines)
# print to screen for user

# taking count of total r and c
dfrnc = df01.shape
print(dfrnc)
# print to screen for user

# summary of the dataframe
dfsmry = df01.info()
print(dfsmry)
# end of code

# statisticl summary of the numerical columns
stsdf = df01.describe()
print(stsdf)
# print to screen

# finding out null values in the dataframe

nullv = df01.isnull()
print(nullv)
# print outout to screen

# dropping na values from dataframe
dropv = df01.dropna()
print(dropv)
# print to screen

# printing new shape of dataframe
newshape = df01.shape
print(newshape)
# end of code

# filling na with a value
fillv = df01.fillna(value=100)
print(fillv)
# end of code

descdf = df01.info()
print(descdf)
# end of code

# merging two columns of the dataframe

df01['aginc'] = df01['age'] + df01['income']
print(df01)
# end of code

# dropping a column from dataframe
drpcol = df01.drop('aginc', axis=1)
print(df01)
# end of code


# sorting values by column

srtdf = df01.sort_values(by='age', ascending=False)
print(df01)
# end of code

# writing the new data to a new csv file
newf = df01.to_csv('modata.csv', index=False)
print(newf)
# end of code

# filtering dataframe

filter01 = df01[df01['age'] > 15]
print(df01)


# indexing and slicing with dataframes
index1 = df01.iloc[16998]
print(index1)


#  creating dataframe from different data structures

# from a list

list_12 = [[2, 10, 3, 5], [7, 20, 9, 15]]
dfabc = pd.DataFrame(list_12)
print(dfabc)
# end of code

# creating dataframe from a dictionary

dict2488 = {'Fruits' : ['Apple', 'Banana', 'Peach', 'Mango'], 'Price' : [135, 60, 290, 330]}
dtodf = pd.DataFrame(dict2488)
print(dtodf)
# end of code

# code for precedence of execution

prop1 = 9955000
prop2 = 11025455
grate = 5500
fsi = (prop1 + prop2) / grate
print('The average property price in this area is', fsi)
# end of code

# function to compute difference
def actprice(cquote, fsi):
    return cquote - fsi
# Calling function with arguments
realv = actprice(4750, fsi)
print('Real price is', realv)
# print to screen for user