# loops
# for loop
for y in range(500):
    print(y)
    y = y + 1
# end of code block

# example - 2 , for loop
block1 = [23, 34, 44, 43, 53, 35, 36, 42, 41]
for x in block1:
    if x < 25:
        print('poor-reading')
    elif x == 25:
        print('standard-reading')
    else:
        print('more-than-average reading')
# end of code block


# while loop

x = 1
while x < 14999:
    print('Current value is', x)
    x = x * 3.75
# end of code block

# lambda functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
# end of code block

# new code block
addfx = lambda a, b: a + b
result = addfx(100, 101)
print(result)

# lambda function-2
mulfx = lambda x: x ** 3
cube = mulfx(24)
print(cube)
# end of code block


# code block for working with tuples
my_tuple = (6, 'n', 14, 'rcc')
my_tuple[0] = 10
print(my_tuple)
# end

# begin
tuple_1 = (11, 29, 33, 39, 44, 47, 55, 56)
print(tuple_1[0])
print(tuple_1[1:6])
print(tuple_1[-1])
# end

# begin
tuple_x = (22, 33, 21, 23)
tuple_y = (26, 21, 29, 27)
new_tuple = tuple_x + tuple_y
print(new_tuple)

# begin
tuple_2 = (34, 45, 31, 56, 71, 42) * 6
print(tuple_2)
# end

# begin
tuple_ag = (22, 34, 44, 54, 67, 21, 26, 25, 29, 40, 43, 33, 39, 47, 45)
print(len(tuple_ag))
# end

# begin
tuple_ga = (1, 3, 1, 3, 5, 3, 5, 3, 1, 5, 1, 3, 1, 5, 1, 5)
print(tuple_ga.count(3))
print(tuple_ga.index(5))
# end

# begin
tuple_5 = 2, 6, 'vk'
print(tuple_5)
# end

# begin
d, e, f = tuple_5
print(d, e, f)
# end

# begin
single_tuple = (9,)
print(type(single_tuple))

sing_tuple = 9
print(type(sing_tuple))
# end



# DICTIONARY DATA TYPE

# mutable key value pairs for storing data
# keys are unique and cannot be modified

dict_1 = {}
dict2 = dict()
# end

# begin
oxford = {'name' : 'matkooram', 'gender' : 'female', 'age' : 65}
print(oxford)
# end

# begin
oxford_dict = dict(name='paaloo', age=14, breed='labrador')
print(oxford_dict)
# end

# begin
items = [('gold', 1), ('silver', 2), ('platinum', 3)]
print(items)
# end

# accessing values in dictionary
dict_01 = {'model' : 'taigun', 'type' : 'hatchback', 'price' : 2135473}
print(dict_01['price'])
print(dict_01['model'])
# end

# begin
dict2 = {'color' : 'red', 'code' : 'fgrr34', 'shade' : 'green'}
print(dict2.get('color'))
print(dict2.get('form', 'notfound'))
# end

dict2['shade'] = 'cyan' # updating the item of key value pair
dict2['rbg code'] = 'bg1213' # adding a new key-value pair
print(dict2)
# end

rbg = dict2.pop('rbg code')
print(rbg)
# end

item = dict2.popitem()
print(item)
# end

# begin
del dict2['code']
print(dict2)
# end

# begin
dicto = {'arpit' : 'pragati', 'yuvraj' : 'aabha', 'kashish' : 'yash'}
dicto.clear()
print(dicto)


webster = {'city' : 'london', 'country' : 'united kingdom', 'continet' : 'europe', 'currency' : 'british pounds'}
keys = webster.keys()
print(keys)
# end

values = webster.values()
print(values)
# end

items = webster.items()
print(items)
# end

merriam = {'name' : 'borris johnson', 'party' : 'labour party', 'constituency' : 'cheshire'}
webster.update(merriam)
print(webster)
# end

dictq = {'name' : 'borris johnson', 'party' : 'conservative party', 'constituency' : 'south hertfordshire'}
for key in dictq.keys():
    print(key)
for value in dictq.values():
    print(value)

for key, value in dictq.items():
    print(key, value)
# end

# begin
list1 = [22, 23, 11, 31, 44, 41, 55, 51, 57, 61]
sq_dict = {num: num ** 2 for num in list1}
print(sq_dict)
# end of script for dictionaries
