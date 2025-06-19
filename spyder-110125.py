# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:07:13 2025

@author: adity
"""

#shree ganeshay namah

#module 1

#addtn
v1 = 34564
v2 = 45113
v3 = 56009
som = v1 + v2 + v3
print(som)
#end of code

#subtrctn
a1 = 456.223
a2 = 339.04
sbt = a1 - a2
print(sbt)
#end of code

#mult
m1 = 34.22
m2 = 41.03
m3 = 41.42
prdct = m1 * m2 * m3
print('Product of floating points is:', prdct)
#end of code


#div
d1 = 409
d2 = 73
rem = d1 / d2
print('The remainder of the operation is:', rem)
#end of code

#expon
ex1 = 88
ex2 = 6
expnt = 88 ** 6
print('Output is:', expnt)
#end of code


#quotient
q1 = 121
q2 = 20
qtnt = q1 % q2
print('The quotient of the operation is:-', qtnt)
#end of code


#module 2
#code1
my_strng = 'simplify and focus'
print(my_strng[7])
#end of code

#code2
my_strng2 = 'successisalousyteacher'
print(my_strng2)
print(my_strng2[1:7])
#end of code



#module3
#code1
x = 0
while x < 99:
    print(x)
    x = x + 1
#end of code

#code02
my_list = [451, 249, 239, 323, 660, 148, 233]
for bills in my_list:
    if bills < 200:
        print('well within budget')
    elif bills == 200:
        print('at par with threshold')
    else:
        print('you exceeded budgets')
#end of code

#code03
apple = 79999
samsung = 59990
pixel = 89990
oneplus = 59999
motorola = 49999
brands_mp = (apple, samsung, pixel, oneplus, motorola)
for msp in brands_mp:
    if msp <= 50000:
        print('Product is reasonably priced')
    else:
        print('Price is exorbitant')
#end of code


#code04
def global_sales(c1, c2, c3, c4, c5, c6):
    return c1 + c2 + c3 + c4 + c5 + c6
#calling the function with arguments
salesg = global_sales(458, 323, 279, 568, 789, 1021)
#all sales figures are in millions $
#print output to screen
print('The global sales value for iphones in 2024 are:', salesg)
#end of code



#module3
import statistics as sts
#mct is measure of central tendency
llp = [24, 37, 46, 59, 68, 83, 94, 98, 106]
mct1 = sts.mean(llp)
print('The mean value of elements is:', mct1)
mct2 = sts.fmean(llp)
print('The fmean for elements is:', mct2)
mct3 = sts.harmonic_mean(llp)
print('Geometric mean value is:-', mct3)
mct4 = sts.harmonic_mean(llp)
print('Hamonic mean value is:', mct4)
mct5 = sts.median(llp)
print('Median value is:', mct5)
mct6 = sts.median_high(llp)
print('High value is:-', mct6)
mct7 = sts.median_low(llp)
print('Low med value is:-', mct7)
mct8 = sts.mode(llp)
print('Mode value is:', mct8)
mct9 = sts.variance(llp)
print('Variance is:', mct9)
mct10 = sts.stdev(llp)
print('Standard dev value is:', mct10)
#end of code

