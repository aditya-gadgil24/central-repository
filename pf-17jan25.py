# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:33:02 2025

@author: adity
"""

#shree ganeshay namah

#moduleno1

#code01
import pandas as pd
dataf = pd.read_csv('C:\\Users\\adity\\Desktop\\reservoir\\staffs.csv')
print(dataf)
#end of code

newdataf = pd.notna(dataf)
print(newdataf)
#end of code

#code02
#code to import data from excel sheet
training_df = pd.read_excel('C:\\Users\\adity\\Desktop\\reservoir\\trainingdf.xlsx')
print(training_df)
#end of code
print(training_df.describe())