# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:14:08 2025

@author: adity
"""

#shree ganeshay namah

#module 01

#code01
grouting = 4400
wproofing = 10355
tcost = grouting + wproofing
print('Hi, the total expenditure is-', tcost)
#end of code

#code02
material_cost = 81500
labour = 49000
taxes = 13275
total_cost = material_cost + labour + taxes
print('Hi, the total cost for this contract approx would be', total_cost)
#end of code

#code03
quotation = 143775
actual_invoice = 137390
refund = quotation - actual_invoice
print('The refund amount for this order id is:-', refund)
#end of code

#code04
labour_nos = 6
rate_perday_perlabour = 850
no_ofdays = 9
total_labour = labour_nos * rate_perday_perlabour * no_ofdays
print('The total cost of labour for this job will be:', total_labour)
#end of code


#code05
muleacnt = 1179000
emp_ct = 11
avg_pay = 83500
settlement_amt = emp_ct * avg_pay
print('The total cost of settlement is-', settlement_amt)
balance = muleacnt - settlement_amt
print('Hi, the balance in mule account after payout is', balance)
#end of code

#code 06
c_loc = False
spackage = 1011200
if c_loc and spackage > 1000000:
    print('Lets proceed')
else:
    print('Out of game')
#end of code


#code07
cstring = 'dont settle'
print(cstring[1:6])
print('The indexed string of characters is',cstring[1:6])
#end of code

#code08
tomato = 100
qty = 6
per_kg = tomato / qty
print('Per kg price is:', per_kg)
#end of code

#code09
peas = 200
qnty = 8
perkg = peas / qnty
print('The price of 1 kg of peas is:-', perkg)
#end of code

#code10
import pandas as pd
import numpy as np
bigdata = pd.read_csv('C:\\Users\\adity\\Desktop\\reservoir\\fishcatch.csv')
print(bigdata)

#code11
farray_1 = np.array([1, 2, 3, 4, 5])
farray_2 = np.array([5, 4, 3, 2, 1])
sum_of_arrays = np.add(farray_1, farray_2)
print(sum_of_arrays)
subt_of_arrays = np.subtract(farray_1, farray_2)
print(subt_of_arrays)
product_of_arrays = np.multiply(farray_1, farray_2)
print(product_of_arrays)
rem_ofa = np.divide(farray_1, farray_2)
print(rem_ofa)
#end of code

#code12
#code to define a function for future use
def life_expectancy(y, r, e):
    return y - r + e
#calling function with arguments
avg_life = life_expectancy(90, 8, 6)
print('Life expectancy for Laos is', avg_life)
#end of code

#code13
wyo = [28, 32, 26, 24, 30, 34, 18, 20, 24]
size_avg = sum(wyo) / len(wyo)
print('Average size purchased is', size_avg)
#end of code

#code 14
pulled_data = [1.36, 5.76, 3.35, 5.98, 2.26, 4.63, 3.68, 1.79]
avg = sum(pulled_data) / len(pulled_data)
print(avg)
upper_v = max(pulled_data)
print(upper_v)
lower_v = min(pulled_data)
print(lower_v)
#end of code

#code 15
ingested_data = [11, 6, 8, 3, 9, 14, 10, 17, 5]
for flv in ingested_data:
    if flv < 10:
        print('cat a')
    elif flv == 10:
        print('cat d')
    else:
        print('cat g')
#end of code

#end of module. This file can be pushed to Github for code review 