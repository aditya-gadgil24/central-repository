# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:27:48 2025

@author: adity
"""

#shree ganeshay namah

#module 1

#1
stng = 'sometimes life is going to hit you in the head with a brick'
print(stng)
print(stng[7])
#end of code

#2
stng1 = 'listentoyourintuition'
print(stng1[6])
#end of code

#3
pckg1 = 1160000
pckg2 = 1029000
pckg3 = 1156000
pcksum = pckg1 + pckg2 + pckg3
print(pcksum)
#end of code


#4
comp1 = 965000
comp2 = 1130000
rng = comp2 - comp1
print('Range of the elements is:', rng)
#end of code

#5
msalary = 84500
months = 12
tsalary = msalary * months
print(tsalary)
#end of code


#6
annual_ctc = 1158748
pay_months = 12
spmonth = annual_ctc / pay_months
print('The pay per month for user is:', spmonth)
#end of code


#7
actc = 1225000
pym = 12
rdr = actc % pym
print('Remainder of the variable is:', rdr)
#end of code

#8
a = 36
b = 38
c = 37
d = 34
e = 31
f = 30
g = 35
bride_age = (a, b, c, d, e, f, g)
for iage in bride_age:
    if iage < 32:
        print('reject')
    elif iage == 32:
        print('consider')
    else:
        print('accept')
#end of code
#print to screen


#module b

#1
i = 5
while i < 99999:
    print(i)
    i = i * 1.15
#end of code

#2
mum_suburbs = [1231409, 1052342, 978515, 1102300, 1090722, 1049451]
for pop in mum_suburbs:
    if pop <= 1000000:
        print('category a')
    else:
        print('category b')
#end of code

#3
mum_suburbs = [1231409, 1052342, 978515, 1102300, 1090722, 1049451]
average_pop = sum(mum_suburbs) / len(mum_suburbs)
print('The average of data points in the list is:', average_pop)
#end of code


#4
sentence_1 = 'be the captain of your ship'
print(sentence_1[21])
#end of code

#5
def median_temp(totalsum, daysct):
    return totalsum / daysct
#calling the function with arguments
avgtemp = median_temp(574, 30)
print('The mean temperature for this month is:', avgtemp)
#end of code




#module c
#1
import statistics as sts
import numpy as np
dset = [12, 22, 19, 12, 17, 14, 16, 18, 17, 21, 23, 21, 14, 13, 11, 17, 12, 22, 23, 11]
mct1 = sts.mean(dset)
print(mct1)

#1b
mct2 = sts.median(dset)
print(mct2)

#1c
mct3 = sts.median_high(dset)
print(mct3)

#1d
mct4 = sts.median_low(dset)
print(mct4)

#1e
mct5 = sts.mode(dset)
print(mct5)
#end of code

#1f
mct6 = sts.stdev(dset)
print(mct6)

#1g
mct7 = sts.variance(dset)
print(mct7)


#1h
mct8 = sts.fmean(dset)
print(mct8)
#end of code
#end of module


#module d
import math
output = math.pow(7, 7)
print(output)

#12c
otpt2 = math.sqrt(121)
print(otpt2)

#endofcode