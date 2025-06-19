# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:35:37 2025

@author: adity
"""

#shree ganeshay namah

#module01
#code01
llm = 'largelanguagemodels'
print(llm)
print(llm[:7])
#end of code

#code02
pr = 175000
i = 6
t = 60
intr = 7
u = 1.5
payable = pr * i / t + intr - u
print('Output of complex operation is:', payable)
#end of code


#code03
having_wife = True
having_job = False
if having_wife or having_job:
    print('Give entry')
#end of code

if having_wife and having_job:
    print('Entry permitted')
#end of code


#code04
#List has values of product price over the years
import statistics as sts
import math
price_list = [11, 14, 16, 19, 21, 25, 27, 29, 32, 33, 38, 40, 41, 47]
lowest_price = min(price_list)
print(lowest_price)
highest_price = max(price_list)
print(highest_price)
p_range = max(price_list) - min(price_list)
print(p_range)
avg_price = sum(price_list) / len(price_list)
print(avg_price)
avrg_price = sts.mean(price_list)
print(avrg_price)
#end of code
median_pl = sts.median(price_list)
print(median_pl)
mode_pl = sts.mode(price_list)
print(mode_pl)
stdev_pl = sts.stdev(price_list)
print(stdev_pl)
#end of code
median_h = sts.median_high(price_list)
print(median_h)
#print output to screen


#module3
#Module for numpy module functions
import numpy as np
#code01
my_array1 = np.array([11, 21, 26, 31, 41, 46, 51])
my_array2 = np.array([9, 19, 24, 34, 39, 49, 54])
array_sum = np.add(my_array1, my_array2)
print(array_sum)
#end of code

#code02
array_remainder = np.subtract(my_array1, my_array2)
print(array_remainder)
#end of code

#code03
array_product = np.multiply(my_array1, my_array2)
print(array_product)
#end of code

#code04
array_div = np.divide(my_array1, my_array2)
print(array_remainder)
#end of code

#code05
ar_mean = np.mean(my_array2)
print(ar_mean)
#end of code

#code06
ar_median = np.median(my_array1)
print(ar_median)
#print to screen
#end of code


#code07
gen_array = np.zeros(11)
print(gen_array)
#end of code

#code08
gen_array1 = np.zeros((11, 99))
print(gen_array1)
#end of code


#code09
array_of1 = np.ones(49)
print(array_of1)
#end of code


#code10
array_of1b = np.ones((11, 111))
print(array_of1b)
#end of code


#code11
array01 = np.array([1, 6, 11, 15, 22, 29, 33, 37, 39])
emp_values = np.isnan(array01)
print(emp_values)
#end of code


#new module for hacker rank
#code01
n = 11
if n % 2 == 0:
    print('even integer')
else:
    print('odd integer')
#end of code


#new code
n = 4
if n % 2 == 0 and 2 <= n <= 5:
    print('Not Weird')
#print to screen

