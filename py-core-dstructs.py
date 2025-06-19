"""This script and its code blocks will illustrate the use cases, internal represenation, memory/
storage layout, operations and performance/memory trade offs"""


"""list"""

# indexing
lst = [22, 43, 21, 41]
print(lst[0])
print(lst[-1])

# slicing
nlist = [1, 4, 7, 9, 3, 11, 13, 6, 19]
print(nlist[0:4])
print(nlist[:3])
nlist.append(22)
print(nlist)

nlist.extend([14, 12])
print(nlist)

nlist.insert(1, 3)
print(nlist)

nlist.pop()
nlist.pop(1)
print(nlist)

nlist.remove(11)
print(nlist)


import sys
x = [1003, 121231, 14423132, 100234543, 100234]
print(sys.getsizeof(x))


# floats dtype

import numpy as np
array_1 = np.array([1.23, 2.61, 2.93, 1.73], dtype=np.float32)
print(array_1)

str_array = np.array(['cucumber', 'cabbage', 'capsicum'], dtype='S10')
print(str_array)
print(str_array.dtype)

# end

"""Tuples data structure"""

tuple1 = (1, 'tuple', 2.45)
print(tuple1)

tuple2 = 1, 'supper', 1.42
print(tuple2)

t1 = (9, 11, 13, 17)

print(t1)

t2 = ([1, 2], 6, 8)
t2[0].append(6)
print(t2)


s = 24, 5, 88
print(s)

a, b, c = s
print(a, b)

# returning multiple values with tuples

def stats(data):
    return min(data), max(data), sum(data)/len(data)

low, high, avg = stats([10, 20, 30])
print(low, high, avg)

# memory model

import sys
print(sys.getsizeof([1, 2, 3]))   # More memory
print(sys.getsizeof((1, 2, 3)))   # Less memory



"""Dictionary data structure, behaviour, use cases, memory model/map, performance characteristics"""

person = {"name": "Mohita", "age": 33, "role": "support engineer"}
print(person)


# list comprehensions

squares = {x: x**2 for x in range(50)}
print(squares)

even_squares = {x: x**2 for x in range(50) if x % 2 == 0}
print(even_squares)


odd_sq = {x: x**2 for x in range(40) if x % 2 != 0}
print(odd_sq)

print(odd_sq.keys())
print(odd_sq.values())

print(odd_sq.items())


# Grouping names by first letter
names = ["Alice", "Anna", "Bob", "Brian"]
grouped = {}
for name in names:
    key = name[0]
    grouped.setdefault(key, []).append(name)



# defaultdict use cases

# Grouping words by first letter
from collections import defaultdict
words = ["apple", "ant", "banana", "bat"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
# {'a': ['apple', 'ant'], 'b': ['banana', 'bat']}

# collections counter

from collections import Counter

counts = Counter("abracadabracaabracadabra")
print(counts)

d1 = Counter("pathanamthitta")
d2 = Counter("parramatta")
print(d1 + d2)
print(d1 - d2)


"""Set data structure, behaviour, use cases, memory model, performance, time/memory complexity"""

s = {2, 4, 7}
empty = set()

set1 = set([4, 9, 11, 2, 7])
print(set1)


x = {56, 48}
x.add(21)
print(x)
x.remove(56)
print(x)


# operations and methods

b = {11, 23, 27}
d = {13, 19, 31}
ops1 = b | d
print(ops1)

ops2 = b & d
print(ops2)

ops3 = b - d
print(ops3)

ops4 = b ^ d
print(ops4)

# frozen set

f = frozenset([2, 4, 9])
print(f)


# membership tests

fruits = {'mango', 'banana', 'sapota', 'watermelon'}
print('apple' in fruits)
print('banana' in fruits)
print('sapota' not in fruits)


# logic

good_actors = {'steve', 'bill', 'allen', 'edgar'}
bad_actors = ['mike', 'garrison', 'turing', 'edgar']
for users in bad_actors:
    if users in good_actors:
        print('access granted')
    else:
        print('access denied')

# end

# 
stopwords = {"the", "is", "and", "in", "to"}
words = ["python", "is", "fast", "and", "flexible"]

filtered = [w for w in words if w not in stopwords]
print(filtered)

# case sensitive membership

g = {'airindia', 'flight', 'crash'}
print('Airindia' in g)


# code

big_list = list(range(1000000))
big_set = set(big_list)

print(999999 in big_list)  # O(n) → Slower
print(999999 in big_set)   # O(1) → Fast!
