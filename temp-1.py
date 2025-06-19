#code id-2002319
string_ext = 'this data type is valid in python'
print(string_ext)
#end of code

#codeid-2002320
list_extracted = [12203, 13455, 12905, 13264, 122454, 139443, 136625, 133583, 122045, 129444]
for intx in list_extracted:
    if intx < 12449:
        print('xcv106')
    elif intx == 12449:
        print('xcv103')
    else:
        print('xcv101')
#end of code
#print to screen for user

#code id- 2002320
import pandas as pd
import numpy as np
arry1 = np.array([1, 9, 17, 33, 47, 59, 63, 77])
arry2 = np.array([2, 12, 28, 38, 42, 56, 78, 82])
arrsum = np.add(arry1, arry2)
print('Output of operation is', arrsum)
#end of code

#cd
minusop = np.subtract(arry1, arry2)
print(minusop)
#end of code

#codeid - 2002321
prdct = np.multiply(arry1, arry2)
print('Product is', prdct)
#end of code

#code id - 2002324
rem = np.divide(arry1, arry2)
print('Output is', rem)
#end of code

#import data from csv file into python
df = pd.read_csv('C:\\Users\\adity\\Desktop\\datalake\\invistico.csv')
print(df)
#end of code

#code id - 200323
df = pd.read_json('C:\\Users\\adity\\Desktop\\datalake\\orders.json')
print(df)
#end of code
#print output to terminal


#code id - 200325
import pandas as pd
import numpy as np
aryn1 = ([13.34, 15.66, 11.97, 12.67, 10.32, 14.19])
aryn2 = ([22.34, 21.74, 23.16, 20.07, 25.66, 24.80])
addundum = np.add(aryn1, aryn2)
print(addundum)
#end of code

subdundum = np.subtract(aryn1, aryn2)
print(subdundum)
#print to screen

prdundum = np.multiply(aryn1, aryn2)
print(prdundum)
#end of code

divdundum = np.divide(aryn1, aryn2)
print(divdundum)
#end of code
#print to screen


#code id- 3012icb
avrg = np.mean(aryn1)
print('Value of dc is:', avrg)
#end of code
#print to screen

mofct2 = np.median(aryn1)
print('Value of the ct measure is-', mofct2)
#end of code
#print to screen

#program to generate random array of ones and zeros
rndarry = np.zeros(99)
print(rndarry)
#print to screen

zeroa2 = np.zeros((99, 7))
#print to screen
print(zeroa2)
#end of code

zeroa3 = np.zeros((50, 7, 2))
print(zeroa3)
#end of code

#program to generate array with input as 1
array_of1 = np.ones((49, 4))
#print outout to screen
print(array_of1)
#end of code

arr_of1 = np.ones((99, 7))
print(arr_of1)
#end of code

#Using pandas lib to ingest data into python environment


#sprint 01-c

astring = 'focus is saying no to a thousand things'
print(astring)
#end of code

#