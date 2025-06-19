#ganesha namah:
valid_dict = {'numbers': [1, 2, 3]}
print(valid_dict)
#printoscreen
#endofcode

#startofcode
oxford = {'aditya' : 'vishakha',
          'adi' : 'neetu'}
print(oxford['adi'])
#printoscreen


#strtofcode
oxie = {'icici' : 'private',
        'hdfc' : 'private',
        'sbi' : 'public',
        'scb' : 'international'}
print(oxie.values())
#printoscreen
#endofcode


#codestart
encyclo = {'a' : '1',
           'b' : '2',
           'x' : '9',
           'r' : '11'}

#add new key value pair
encyclo['h'] = ['6']
print(encyclo)
#endofcode


#startofcode
smallest_countries = {'Africa': 'Seychelles',
                     'Asia': 'Maldives',
                     'Europe': 'Vatican City',
                     'Oceania': 'Nauru',
                     'North America': 'St. Kitts and Nevis',
                     'South America': 'Suriname'
                     }
print('africa' in smallest_countries)
#endofcode


#startofcode
my_dict = {'codew': [61, 72, 83],
          'ijp': ['ax', 'cb', 'dc']
          }
del my_dict['codew']
print(my_dict)
#printoscreen
#endofcode


#codestart
err = {'gold' : 'metal',
       'zinc' : 'alloy',
       'silver' : 'metal'}
print(err.values())
#printscreen
#codends

#startofcode
tcs = {'emp1' : 'ashok',
       'emp2' : 'nehal',
       'emp3' : 'saumya'}
print(tcs.values())
#printscreen
#endofcode


#startofcode
allset = {'bombay', 'poona', 'calcutta', 'madras'}
allset.add('bangalore')
print(allset)
#printscreen
#endofcode


#startofcode
set_1 = {'a', 'b', 'c'}
set_2 = {'b', 'c', 'd'}
print(set_1 | set_2)
print(set_1.union(set_2))
#print2screen
#endofcode

#startofcode
s1 = {'m', 'n', 'o', 'p'}
s2 = {'o', 'p', 'q', 'r'}
print(s1 & s2)
print(s1.intersection(s2))
#printoconsole
#codend


#codebegin
pqr = {'l', 'q', 's', 'y'}
eod = {'y', 'b', 'q', 's'}
print(pqr - eod)
#printoconsole
#codends


#codestarts
import numpy