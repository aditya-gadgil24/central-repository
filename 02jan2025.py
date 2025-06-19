# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:31:36 2025

@author: adity
"""

#shree ganeshay namah
#code 02-01-25
dt_string = 'Happy new year'
print(dt_string)
#end of code

#2125-002
bsc = 36000
bns = 17000
vre = 29500
ts  =bsc + bns + vre
print('Hi, the value of tsv is:', ts)
#end of code

#functions
def annuals(tms, m):
    return tms * m
#calling function with arguments
aes = annuals(84750, 12)
print('The annual salary for the employee is:', aes)
#end of code

#fgt4545
r = 1245.22
a = 2344.93
n = 12.33
d = 6.09
e = 17.34
randomc = r + a - n * d / e
print('Output on screen is:-', randomc)
#end of code

#special ops
op = 24
ps = 7
ops = 24 ** 7
print('Output from file is:', ops)
#end of code

#new code block
r = 26
d = 7
rmndr = r % d
print(rmndr)
#end of code

#new code block
y1 = 2024
y2 = 2025
if y1 <= y2:
    print('lol')
else:
    print('loll')
#end of  code

#new code block
cslry = 47500
while cslry < 575000:
    print(cslry)
    cslry = cslry * 1.15
#print to screen
#end of code

#new code block
list_syn = [65000, 68000, 74000, 77000, 79500, 81000, 69000, 76000]
for offers in list_syn:
    if offers < 69999:
        print('reject')
    elif offers == 69999:
        print('consider')
    else:
        print('accept')
#print to screen
#end of code

#new code block
#program to create 2 arrays and apply stat/arit computations
import numpy as np
yside = ([80, 84, 88, 86, 87, 90, 92, 96, 97])
xside = ([54, 59, 62, 63, 65, 67, 70, 55, 60])
yax = np.add(yside, xside)
print(yax)

#subs
ysx = np.subtract(yside, xside)
print(ysx)
#end of block

#new code
ymx = np.multiply(yside, xside)
print(ymx)
#end of code

#new code block
ydx = np.divide(yside, xside)
print(ydx)
#end of code

#new code block
average_of_array = np.mean(yside)
average_of_array2 = np.mean(xside)
print(average_of_array)
print(average_of_array2)
#end of code

#new code block
median_v = np.median(yside)
median_v2 = np.median(xside)
print(median_v)
print(median_v2)
#end of code

#new code block
#generating array of ones and zeros for sample analysis
array_a = np.zeros(99)
print(array_a)
#end of code

#new block code
array_b2 = np.zeros((100, 6))
print(array_b2)
#end of code

#new code block
array_c1 = np.ones(66)
print(array_c1)
# end of code

#new code block
array_c2 = np.zeros((59, 9))
print(array_c2)
#end of code


#this code loads data from csv file into python environment
import pandas as pd
import numpy as np
import statistics as sts
df = pd.read_csv('C:\\Users\\adity\\Desktop\\datalake\\airbnb.csv')
print(df)
#end of code

#new code block
mydf = pd.read_csv('C:\\Users\\adity\\Desktop\\datalake\\shared space\\fishcatch.csv')
print(mydf)
#end of code

#new code block
#loading data from excel sheet
exldf = pd.read_excel('C:\\Users\\adity\\Desktop\\datalake\\trainingdf.xlsx')
print(exldf)
#end of code

#new code block
jsondf = pd.read_json('C:\\Users\\adity\\Desktop\\datalake\\orders.json')
print(jsondf)
#end of code