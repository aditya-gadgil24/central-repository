# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:53:11 2025

@author: adity
"""

#code01
#code block to import csv file data
import pandas as pd
airbnb = pd.read_csv('C:\\Users\\adity\\Desktop\\reservoir\\airbnb.csv', skiprows=1)
print(airbnb)
print(airbnb.head())
#end of code

#code02
import csv
with open('C:\\Users\\adity\\Desktop\\reservoir\\stores.csv') as file:
    otpt = csv.reader(file)
    for vls in otpt:
        print(otpt)
#end of code

#using numpy for loading csv data
import numpy as np
dataf1 = np.genfromtxt('C:\\Users\\adity\\Desktop\\reservoir\\staffs.csv', delimiter=',', skip_header=1)
print(dataf1)
#end of code

#code04
import dask.dataframe as dd
mydf = dd.read_csv('C:\\Users\\adity\\Desktop\\reservoir\\cdataset.csv')
print(mydf)
print(mydf.head())
#end of code
        