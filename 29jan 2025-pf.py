# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:37:44 2025

@author: adity
"""

# Shree ganesay namah

# code 01

# series is one dimensional labeled array
import pandas as pd
serees = pd.Series([11, 12, 13], index=['x', 'y', 'z'])
print(serees)
# Print to screen

# End of code

# Code to create dataframe from a list
# code 101

dta = {'Brand' : ['Hyundai', 'Vw', 'Skoda', 'Toyota'], 'Model' : [1121, 1023, 1156, 1223]}
dtfrm = pd.DataFrame(dta)
print(dtfrm)
# Print to screen for user
# End of code


# code 102

deta = {'Country' : ['Australia', 'UK', 'Germany', 'Finland'], 'City' : ['Perth', 'Berlin', 'London', 'Helsinki']}
kndtfrm = pd.DataFrame(deta)
print(kndtfrm)
# Print to screen for user
# End of code


# code 103

# This code will build dataframe from lists
lists_grp = [[92, 33, 44], [89, 39, 49], [56, 41, 61]]
dtform = pd.DataFrame(lists_grp, columns=['a', 'x', 'y'])
print(dtform)
# Print to screen
hinfo = dtform.head(1)
print(hinfo)
# Print to screen
tinfo = dtform.tail(1)
print(tinfo)
# Print to screen
inf = dtform.info()
print(inf)
# Print to screen
dinfo = dtform.shape
print(dinfo)
# Print to screen
dfsummary = dtform.describe()
print(dfsummary)
# Print to screen



# indexing and slicing
indx = dtform.iloc[2]
print(indx)
# end of code


             
# functions for data cleaning
null_v = dtform.isnull()
print(null_v)
# print to screen

# code for dropping na value rows
drop_df = dtform.dropna()
print(drop_df)
# print to screen

# code for filling na values
fill_df = dtform.fillna(value='empty')
print(fill_df)
# end of code

# adding a new column

dtform['u'] = dtform['x'] + dtform['y']
print(dtform)
# print the output to screen

# dropping a column
ndf = dtform.drop('u', axis=1)
print(ndf)
# print to screen

# new code

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr[indices])  
# end of code 