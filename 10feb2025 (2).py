# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:06:25 2025

@author: adity
"""

# SHREE GANESHAY NAMAH


# Using python modules for file formats like csv, json, xml, excel, parquet
# avro

# code 01

import csv
with open('C:\\Users\\adity\\Desktop\\reservoir\\fishcatch.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# print output to screen
# end of code


# code 01
# csv data ingestion, cleaning, transformation, loading to a new file

import pandas as pd
agdf = pd.read_csv('C:\\Users\\adity\\Desktop\\reservoir\\invistico.csv')
print(agdf)
# print to screen

agdfshpe = agdf.shape
print(agdfshpe)
# end of code

aginfo = agdf.info()
print(aginfo)
# end of code

desagdf = agdf.describe()
print(desagdf)
# end of code

nullagdf = agdf.isnull()
print(nullagdf)
# end of code

dropnl = agdf.dropna()
print(dropnl)
# end of code

fillagdf = agdf.fillna(value=100)
print(fillagdf)
# end of code

# writing the transformed data to a new file
nwfile = agdf.to_parquet('transdata.parquet')
print(nwfile)
# end of code


# new code
import dask.dataframe as dd
newdf = dd.read_csv('C:\\Users\\adity\\Desktop\\reservoir\\fishcatch.csv')
print(newdf)
# end of code

"""End of file and script for the module"""