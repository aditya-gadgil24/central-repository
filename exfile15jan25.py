# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:23:56 2025

@author: adity
"""
#module3

#code01
has_passport = True
has_visa = False
if has_passport and has_visa:
    print('Eligible applicant')
#end of code

#code02

metro_city = True
salary = 1995000
if metro_city and salary > 1000000:
    print('Eligible')
#end of code

#code03

starkid = True
money = True
if starkid and money:
    print('You will get entry')
#end of code


#code04
brahmin_caste = False
salary_package = 1398000
if brahmin_caste or salary_package > 1500000:
    print('Can marry')
#print output to screen



#code05
zy = 6.99
ab = 6.88
if zy == ab:
    print('Equal')
elif zy < ab:
    print('Smaller')
else:
    print('Greater')
#end of code


#code06
#the below list has values of blood pressure readings taken from a smart device
bp_readings = [143, 124, 138, 155, 162, 179, 157, 147, 131, 122]
for dp in bp_readings:
    if dp < 125:
        print('Bp is normal')
    elif dp == 120:
        print('Bp is perfect')
    else:
        print('Bp is high, see a doctor')
#end of code


#code07
#writing function to calculate data consumption
def data_consumption(tdc, au):
    return tdc / au
#calling function with arguments
mdc = data_consumption(146292, 1794)
print('The per user data consumption for current month is:', mdc)
#end of code

#code08
a = 132903
b = 2998
tc = data_consumption(132903, 2998)
print(tc)
#end of code


#code09
rcb = 598
mi = 589
kkr = 593
franchise_value = (rcb, mi, kkr)
for current_value in franchise_value:
    if current_value <= 590:
        print('Top franchise')
    else:
        print('Low valued franchise')
#end of code



#module 04

import statistics as sts
age_samples = [7, 5, 11, 9, 13, 17, 15, 10, 6, 12, 21, 19, 18, 19]
mct1 = sts.mean(age_samples)
print(mct1)
mct2 = sts.fmean(age_samples)
print(mct2)
mct3 = sts.geometric_mean(age_samples)
print(mct3)
mct4 = sts.harmonic_mean(age_samples)
print(mct4)
mct5 = sts.median(age_samples)
print(mct5)
mct6 = sts.median_high(age_samples)
print(mct6)
mct7 = sts.median_low(age_samples)
print(mct7)
mct8 = sts.mode(age_samples)
print(mct8)
mct9 = sts.stdev(age_samples)
print(mct9)
mct10 = sts.variance(age_samples)
print(mct10)
#end of code

