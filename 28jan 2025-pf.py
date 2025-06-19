# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:15:49 2025

@author: adity
"""

#  Shree Ganeshay Namah

# code no 1

import pandas as pd
srs1 = pd.Series([2, 20, 3, 31, 4, 40])
print(srs1)
# Print to screen

# code 02
# dataframe from dictionary
dta = {'Serial' : [1, 2, 3, 4], 'Name' : ['Monica', 'Neha', 'Sharda', 'Swapna']}
df1 = pd.DataFrame(dta)
print(df1)
hd = df1.head(5)
print(hd)

# code 03
# dataframe from list
list_ab = [[6, 11], [7, 14]]
dtfrm = pd.DataFrame(list_ab, columns = ['X', 'Y'])
print(dtfrm)
# end of code
dtail = dtfrm.tail(1)
print(dtail)
# end of code
dshape = dtfrm.shape
print(dshape)
# end of code
dfsum = dtfrm.info
print(dfsum)
dfdes = dtfrm.describe()
print(dfdes)
dd1 = dtfrm.iloc[1]
print(dd1)

# new code
dfnull = dtfrm.isnull()
print(dfnull)