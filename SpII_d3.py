#shree ganeshay namah
#code01
#This program will execute arithematic computations using operators
dec_v1 = 1988
dec_v2 = 1986
dec_v3 = 1959
dec_v4 = 1954
dec_v5 = 4
fx_cte = dec_v1 + dec_v2 - dec_v3 * dec_v4 / dec_v5
print('Hi, the output of this compute operation is:-', fx_cte)
#endcode

#code02
#This program compare two values and returns the value
pv1 = 28.99
pv2 = 29.89
if pv1 == pv2:
    print('Equal integers')
elif pv1 < pv2:
    print('Second greater than first')
else:
    print('First greater than second')
#print results
#end code

#code03
init_val = 1
while init_val < 19999:
    print(init_val)
    init_val = init_val * 1.15
#end code
#print results


#code04
string_l = 'follow steve jobs principles to succeed'
print(string_l[7])
#endcode

#code05
string_oftxt = 'putdinginuniverse'
print(string_oftxt[9])


#code06
dc_int = 1175750
dc_flt = 11.34
dc_string1 = 'lengthofstring'
dc_string2 = 'length of string'
dc_list = [88, 'me', 24, 'may', 'taigun']
dc_tuple = ('this', 'is', 'tuple', 'data', 'structure', 'type')
dc_dictionary = {'brand' : 'volkswagen',
                 'make' : 'taigun gt'}
dc_sets = {'sets', 'data', 'type', 'in', 'python'}
#end code


#code07
dtlist = [4, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70]
for rndm in dtlist:
    if rndm < 35:
        print('Value falls on left side of standard deviation')
    elif rndm == 35:
        print('Value falls on centre point near standard deviation')
    else:
        print('Value falls on right side of standard deviation')
#print screen
#end code


#code08
x = 5

if not x == 10:
    print("x is not equal to 10")  # This will execute


#code09
#program to create function to compute average execution time for postgresql db
def pg_avgex(qct, tet):
    return tet / qct
#calling function with arguments
pgaet = pg_avgex(64800, 11200)
print('Hi, the average execution time for postgresdb is:', pgaet)
#endcode

#code10
#program to compute measures of central tendency for a sequence of values inside tuple
import statistics as stics
std_tuple = (24, 27, 28, 33, 35, 39, 42, 45, 47, 50, 53, 56, 59, 60, 63, 65, 67, 70, 72, 75, 77, 78)
tpleavg = stics.geometric_mean(std_tuple)
print('The ct measure of mean for the tuple is:', tpleavg)
tplemedian = stics.median(std_tuple)
print('The ct measure of median for the tuple is:', tplemedian)
tplemod = stics.mode(std_tuple)
print('The ct measure of mode for the tuple is:', tplemod)
tplesd = stics.stdev(std_tuple)
print('The ct measure of standard deviation for the tuple is:', tplesd)
tpharmean = stics.harmonic_mean(std_tuple)
print('The ct measure of harmonic mean for the tuple is:', tpharmean)
tplevr = stics.variance(std_tuple)
print('The ct measure of variance for the tuple is:', tplevr)
#endcode


#code11
import numpy as np
arrynp = np.array([26.23, 32.46, 37.05, 39.18, 41.69])
print(arrynp)
#end lcode

#code12
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.add(arr1, arr2)
print("Addition:", result)  # Output: [5 7 9]


#code13
numbers = np.array([1.23456, 2.34567, 3.45678])
rounded = np.round(numbers, decimals=0)
print('The output of the operation is:', rounded)
#end code


#Dec11 2024
#code14

ary1 = np.array([101, 201, 301, 401, 501])
ary2 = np.array([102, 202, 302, 402, 502])
arsum = np.add(ary1, ary2)
print('Hi user, the value returned for the computation is:', arsum)
#print screen
#end code

#code15
week1 = np.array([97.50, 93.24, 91.27, 92.26, 92.92, 91.13, 90.12])
week2 = np.array([91.24, 90.13, 90.46, 92.54, 93.89, 93.96, 91.28])
dff = np.subtract(week1, week2)
print('Hi user, the value returned for computation 2 is:', dff)
#end code





