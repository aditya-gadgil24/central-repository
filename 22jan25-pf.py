# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:43:34 2025

@author: adity
"""

#shree ganeshay namah
#code to import data from excel sheet, merge two columns, apply transformation
#load the new data into an excel file 

#code01
import pandas as pd
exdf = pd.read_excel('C:\\Users\\adity\\Desktop\\reservoir\\practice.xlsx')
print(exdf)
#end of code
exdf['customer_name'] = exdf['first_name'] + ' ' + exdf['last_name']
exdf.to_excel('output_file.xlsx', index=False)
#end of code

df1 = pd.read_excel('output_file.xlsx')
print(df1)
#end of code

#code02
#load data from excel, merge two columns using concatenate
#output will be saved to a new excel sheet and then printed to console 
#using dataframe

import pandas as pd
import numpy as np
movies_df = pd.read_excel('C:\\Users\\adity\\Desktop\\reservoir\\moviesdata.xlsx')
print(movies_df)
#end of code

#code to merge two columns by concatenating and creating a new column
#data transformation
movies_df['total_col'] = movies_df['Box_Office'] + ' ' + movies_df['Total_Earnings']
movies_df.to_excel('mdoutput.xlsx', index=False)
#end of code

bodf = pd.read_excel('mdoutput.xlsx')
print(bodf)

#code03
#import data from excel, apply transformations, load it into excel
#print data after loading it into dataframe

import pandas as pd
mve_df = pd.read_excel('C:\\Users\\adity\\Desktop\\reservoir\\moviedata.xlsx')
print(mve_df)
#end of code


