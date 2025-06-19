"""This file illustrates python functions, their types, definition, calling, default parameters
or arguments and higher order functions"""


# 1

def greet(name):
    return f"Hello, {name}"

# calling the function with arguments

message = greet('Sandra')
print(message)

# default args

# defining fx with def argument and without def arguments

def hello(person='Mike'):
    return f"Hi there, {person}"

# calling with def argument
message1 = hello()

# calling with supplied argument 
message2 = hello(('Dakota'))

print(message1)
print(message2)



# *args

def put_all(*args):
    return sum(args)

# calling function with args
sum_all = put_all(1, 4, 6, 8, 3, 5)
print(sum_all)

sum_int = put_all(11, 99, 44)
print(sum_int)


# *kwargs

def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# calling fx with args
new_message = print_dict(name='alice', age=33)
print(new_message)


# lambda functions - anonymous inline functions

sqrs = lambda x: x * x
sqr = sqrs(11)
print(sqr)
print(sqrs(24))


# higher order functions - that take or return functions

# 1

def upper_case(text):
    return text.upper()

case1 = upper_case('holomodor')
print(case1)


def lower_case(textsrings):
    return textsrings.lower()

case2 = lower_case('STALIN')
print(case2)


# map, filter and reduce - apply function to all iterables or items

# map
list_1 = [22, 41, 37, 19, 11]
squared_list = list(map(lambda x: x * x, list_1))
print(squared_list)

# filter

evens = [2, 9, 7, 11, 13, 18, 12, 16, 21, 22, 27]
fil_ints = list(filter(lambda x: x % 2 == 0, evens))
print(fil_ints)

# reduce
from functools import reduce

result = reduce(lambda x, y: x * y, [1, 2, 3, 4])  
print(result)  


# libraries and modules

import numpy as np
import pandas as pd


import os
dir(os)








