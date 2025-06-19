# SHREE GANESHAY NAMAH

# data types in python

# integers
cs = 21
print(cs)
print(type(cs))
# end of code

# floating point precision
dj = 13.432
print(dj)
print(type(dj))
# end of code

# complex numbers
cn = 7+5j
print(cn)
print(type(cn))
# end of code

# strings
quote = 'stay hungry stay foolish'
print(quote)
print(type(quote))
# end of code


# lists
list_dt = [24, 5, 30, 8, 15, 10, 1, 12]
print(list_dt)
list_2 = ['adi', 'jaya', 'bugsbunny', 'molu']
print(list_2)
list_c = [1956000, 'taigun', 2213000, 'taigundsg']
print(list_c)
print(type(list_c))
# end of code


# tuples
tuple1 = (2, 9, 11, 13, 17, 14)
print(tuple1)
tuple2 = ('t', 'e', 'd', 'e','x')
print(tuple2)
tuple3 = ('z', 1, 'e', 9, 11, 'fc')
print(tuple3)
print(type(tuple3))
# end of code


# dictionaries
oxford = {'product' : 'apple phone',
          'price' : 91000,
          'quantity' : 1,
          'discount' : 0,}
print(oxford)
print(type(oxford))
# end of code

# tuples
tup = (10, 22, 29, 10, 39, 22)
print(tup)
print(type(tup))
# end of code



# new code
fruits = ['mango', 'banana', 'sapota']
fruits.append('cashwenut')
print(fruits)
# end of code


# sets

setx = {11, 29, 33, 42, 11, 38, 29, 49, 53, 57, 59, 61, 49}
print(setx)
print(type(setx))
# end of code


# code 01
list_x = [1, 22, 4, 11, 5]
list_x.append(66)
print(list_x)
list_x[1] = 24
print(list_x)
# end of code

# list operations
my_list = [1, 2, 3]  # Initial size

my_list.append(4)  # Fast append
my_list.append(5)  # Fast append

# If the underlying array is now full, appending again will trigger a resize
my_list.append(6) # Potentially slower resize operation

my_list.insert(1, 10)  # Slow insert (requires shifting elements)
print(my_list)
# end of code