# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:47:45 2025

@author: adity
"""

#code01
#load data from excel, merge columns into new one, save and print the new data
import pandas as pd
df01 = pd.read_excel('C:\\Users\\adity\\Desktop\\reservoir\\moviedata.xlsx')
print(df01)
#end of code

#code03
import pandas as pd
df03 = pd.read_excel('C:\\Users\\adity\\Desktop\\reservoir\\sales.xlsx')
print(df03)
#end of code
df03['tsales'] = df03['January'] + ' ' + df03['February']
df03.to_excel('compute.xlsx', index=False)
mydf = pd.read_excel('compute.xlsx')
print(mydf)
#end of code

#code04
import xlrd
workbook = xlrd.open_workbook('C:\\Users\\adity\\Desktop\\reservoir\\practice.xlsx')
print(workbook)
              