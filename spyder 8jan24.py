# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:53:30 2025

@author: adity
"""

#shree ganeshay namah

#module1
import math
crt = math.cbrt(729)
print(crt)
#end of code

#code02
fctr = math.factorial(10)
print(fctr)
#end of code

#code03
mth1 = math.ceil(11.323)
print(mth1)
#end of code


#code 04
mth2 = math.floor(99.999)
print(mth2)
#end of code

#code 05
rem = math.remainder(99, 12)
print(rem)
#end of code


#code 06
lyf = 'do something when you are young'
print(lyf)
#end of code

#code 07
lyf1 = 'stringoftextcharacters'
print(lyf1)
print(lyf1[7])
#end of code


#code 08

#arith computations on random integers and floating point

av = 9355700
yrs = 15
rte = 4
rdv = 1500000
dav = 1000000
nav = av / yrs * rte + rdv - dav
print('The nav of the asset at EOL is:', nav)
#end of code

#code 09
age = 36
while age < 100000:
    print(age)
    age = age * 1.25
#end of code

#code 10

aditya = 36.7
navy = 36.5
if aditya < navy:
    print('Navy is elder')
elif aditya == navy:
    print('They are same age')
else:
    print('Aditya is elder')
#end of code


#code 011

price_list = [42, 18, 39, 26, 12, 20, 53, 48, 22, 65, 52, 37, 16]
for iprices in price_list:
    if iprices < 20:
        print('Low value item')
    elif iprices == 20:
        print('Average value item')
    else:
        print('High value item')
#end of code


#code012

mah = 91.21
guj = 90.83
mp = 81.04
raj = 73.46
tn = 91.11
od = 71.26
states = (mah, guj, mp, raj, tn, od)
for ist in states:
    if ist < 85:
        print('poor')
    elif ist == 85:
        print('average')
    else:
        print('strong')
#end of code


#code 013

def atrapezium(i, a, b, h):
    return i * a + b * h
#calling the function with arguments
trapez = atrapezium(0.5, 7, 11, 3)
#print output to screen
print('Area of trapezium is:', trapez)
#end of code



