# Shree

# this script will contain code snippets for working with python sets

# unordered mutable collection of unique elements, you cant add duplicate elements to sets

# creating sets
set_1 = {'google', 'microsoft', 'facebook', 'apple', 'amazon', 'nvidia'}
set_2 = {1, 3, 2, 4, 6, 5}
print(set_1)
print(set_2)
# end of code block

# using set constructor

set3 = set([2, 1, 3, 2, 1, 3, 5, 2, 1, 3, 2, 2, 3, 1])
print(set3)
# end

set4 = set('towoomba')
print(set4)
# end

set5 = set()
print('This is an empty set', set5)
# end

ad_set = {'mangoes', 'banana', 'sapota'}
ad_set.add('strawberry')
print(ad_set)
ad_set.add('mangoes')
print(ad_set)
# end

set6 = {'white', 'yellow'}
set6.update(['red', 'blue'])
print(set6)
# end

set7 = {9, 3, 4, 5, 6, 1}
set7.remove(2)
print(set7)

set7.discard(3)
print(set7)
# end

set8 = {'pop', 'lol', 'sos', 'ror', 'yoy', 'fof'}
removed_item = set8.pop()
print(removed_item)
# end

set_ad = {44, 32, 21, 68, 62, 59, 53, 48}
set_ad.clear()
print(set_ad)
# end

set_x = {1, 3, 7, 9, 4}
set_y = {2, 5, 8, 10, 6}
new_set = set_x | set_y
print(new_set)
# end

set_01 = {22, 21, 29, 27, 25}
set_02 = {32, 31, 39, 37, 35}
set_03 = set_01.union(set_02)
print(set_03)
# end

st1 = {6, 2, 11, 9, 3}
st2 = {3, 15, 17, 21, 6}
nset = st1 & st2
print(nset)

nset2 = st1.intersection(st2)
print(nset2)
#  end

ds1 = {3, 1, 9, 6}
ds2 = {5, 9, 11, 14}
diff_set = ds1 - ds2
print(diff_set)
# end
difference_set = ds1.difference(ds2)
print(difference_set)

# Frozen Sets

fs1 = frozenset({6, 1, 8, 11, 2})
fs2 = frozenset({9, 4, 6, 13, 2})
print(fs1)
print(fs2)
print(7 in fs1)
print(10 not in fs2)
print(fs1.issubset(fs2))
print(fs2.issuperset(fs1))
print(fs2.isdisjoint(fs1))
# end

funion = fs1 | fs2
funion1 = fs1.union(fs2)
print(funion)
print(funion1)

finter = fs1 & fs2
print(finter)
finters = fs1.intersection(fs2)
print(finters)

diff1 = fs1 - fs2
print(diff1)
diff2 = fs1.difference(fs2)
print(diff2)
# end

sydf1 = fs1 ^ fs2
print(sydf1)
sydf2 = fs1.symmetric_difference(fs2)
print(sydf2)

for item in fs1:
    print(item)
# end

ints = [22, 34, 91, 102, 134, 149, 177, 201, 254]
bytarry = bytearray(ints)
print(bytarry)

ba = bytearray(50)
print(ba)
# end of script for data structures


# pandas dataframes


