#sprint4-day2-01
#cde001
#shree ganesha namah
thev = 4
if thev < 5:
    print('not good')
elif thev == 5:
    print('acceptable')
else:
    print('unacceptable')
#print to console for user



#code02
ab = 44566546556
bc = 54556564565
cd = 54454445654
asum = ab + bc + cd
print('the result of operation is', asum)
#print to console


#cd7
apluslist = [12.23, 12.29, 11.87, 13.43, 12.43, 11.94, 13.23]
for reading in apluslist:
    if reading < 11.99:
        print('put to class c')
    elif reading == 11.99:
        print('put to class b')
    else:
        print('put to class a')
    #print output to console


#spr4-d2-c7
cur_v = 9
while cur_v < 999:
    print('The value after this iteration is', cur_v)
    cur_v = cur_v * 1.95
#print results to screen for user


#spr4-d2-13
liferule = 'your heart and intuition already know what you want to do in life'
print(liferule)


#spr4-d2-22
n1 = 452.21
n2 = 467.33
n3 = 476.90
n4 = 498.32
op1 = n1 + n2 + n3 - n4
#the output will be printed to screen
print('Hi, the output of this operation is', op1)


#spr4-d2-32
p1 = 34333.37
p2 = 42912.22
p3 = 41222.83
p4 = 32333.33
op2 = p1 * p2 * p3 / p4
#output will be printed to console
print('Hey, the result of this operation is', )



#spr4-d2-34
x = 1
y = 1
if x < y:
    print('case a')
elif x == y:
    print('case b')
else:
    print('case c')
#print to consle


#spr4-d2-39
text_format = 'use the best data for ml models'
print(text_format[5])
#print to console

#fnctn
def intrst(pr, ir, x):
    return pr * ir / x
#calling the function with values to parameters
inamt = intrst(10000000, 11, 100)
print('Dear Customer, the total interest amt for your pr is', inamt)
#print output to console


#strings
#cde09
ly_string = 'to take and talk to them takes total time and tolerance to the core'
print(ly_string.count('t'))
#print to


#replace element in string
string_11 = 'www.immutable.com'
string_11.replace('immutable', 'mutable')
#end code

#new code
my_string = 'Do you know the muffin man?'
my_string.split()


#y43
boc_stats = [97, 104, 86, 98, 108, 124, 136, 128, 99, 101, 106, 117]
for earnings in boc_stats:
    if earnings < 100:
        print('flop flick')
    elif earnings == 100:
        print('sleeper hit')
    else:
        print('super hit')
#print output to console
#end of code

#newcode11
import re
my_string = 'Three sad tigers swallowed wheat in a wheat field'
re.search('wall', my_string)
#end of code

#code998
emp_list = []
print(emp_list)
#eoc

#code112
phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[-1])
#print to console

#eod44
phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[0:3])
#this code will throw an error

#ncode009
phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[:3])
print(phrase[3:])
#eocr

#ncode4
my_list = ['Macduff', 'Malcolm', 'Duncan', 'Banquo']
my_list[2] = 'James Whithall'
print(my_list)
#end of code

#start of new code
list_ofad = ['mom', 'dad', 'paaloo', 'mango', 'takli']
list_ofad[4] = 'poornima'
print(list_ofad)
#eocde

#nwcde
list_x = ['e', 'f', 'g', 'h']
list_y = [8, 1, 9, 2]
marriage = list_x + list_y
print(marriage)
#endofcode

#beginningofcode
my_list = [9, 6, 11, 12, 33]
variable = 99
my_list.append(variable)
print(my_list)
#edofcode

#codestarts
my_list = ['ag', 'bb', 'vd', 'nm']
my_list.insert(1, 'mb')
print(my_list)
#print to screen
#end of code


#start of code
list_xx = ['r', 'a', 'f', 'h', 'k', 'f']
list_xx.remove('f')
print(list_xx)
#print result to console
#end of code


#codebegins
my_list = ['axle', 'single', 'multi', 'lmv']
my_list.pop(2)
print(my_list)
#codends

#codebegin
list_abcd = ['shanaya', 'jahnvi', 'sara', 'yami', 'suhana']
list_abcd.pop(2)
print(list_abcd)
#print to console

#codestart
list_of_ds = ['jennifer', 'barry', 'sophie', 'nicole', 'amy']
list_of_ds.clear()
print(list_of_ds)
#endofcode

#codestart
vs_list = ['x', 'a', 'g', 'x', 'o', 'z', 'x']
print(vs_list.index('x'))
#codends

#startofcode
text_list = ['you', 'me', 'they', 'we', 'us']
ints_list = [12, 44, 32, 29, 16, 17]
text_list.sort()
ints_list.sort(reverse=True)
print(text_list)
print(ints_list)
#endofcode

#start of code
mi_string = 'you and me make the world beautiful'
print(mi_string)
#eoc


#boc
miy_string = 'you, and, me, are, good'
print(miy_string)
#end

#start
m_strings = 'youandmeareallgood'
print(m_strings)
#end

#codestart
cities = ['Paris', 'Lagos', 'Mumbai']
countries = ['France', 'Nigeria', 'India']
places = zip(cities, countries)


print(places)
#endofcode


#startcode
list_a = [1, 2, 3, 4, 5]
list_b = [n + 10 for n in list_a]
print(list_b)
#print result
#end of code

#initiatecode
list_1 = [200, 400, 800, 1600, 3200, 6400]
list_b = [a - 100 for a in list_1]
print(list_b)
#print to console
#eofcode

#dictionariescode
dictionary_a1 = {'Europe' : 'London',
'Africa' : 'Harare',
'Asia' : 'Tokyo',
'Oceania' : 'Sydney'}
print(dictionary_a1)
#printoconsole
#endofcode


#stcode
invalid_dict = {'numbers' : 'xd'}
print(invalid_dict)

        
    