# SHREE

# This file is created by Aditya on 22 March 2025
# All code blocks in this file are for a revisit of Python basics.


# begin
# dt denotes data type
dt1 = 1772
dt2 = 81.34
dt3 = 'Molu'
dt4 = 'Molu battakh'
dt5 = 'Guddanpilloopompee'
dt6 = True
print(dt1)
print(dt2)
print(dt3)
print(dt4)
print(dt5)
print(dt6)
# end

# begin
# ds denotes data structure
ds1 = [24, 30, 1, 15, 11, 31, 21]
ds2 = (24, 30, 41, 15, 10, 34, 22)
ds3 = {11, 23, 22, 34, 33, 21, 12}
ds4 = {'name' : 'viviana', 'nationality' : 'italian', 'age' : 29,
         'profession' : 'music composer', 'genre' : 'western classical'}
ds5 = frozenset({11, 23, 22, 34, 33, 21, 12})
ds6 = bytearray(10)
ds7 = memoryview(bytes(10))
print(ds1)
print(ds2)
print(ds3)
print(ds4)
print(ds5)
print(ds6)
print(ds7)
# end

# begin
# op denotes operators
k1 = 1298
k2 = 2392
k3 = 1003
k4 = 5
k5 = 7
allop = k1 + k2 - k3 / k4 * k5
print('The output of this operation in python is:-', allop)
# end

# begin
x1 = 23
x2 = 7
x3 = x1 ** x2
print('The output of this operation in python is:-', x3)
# end

# begin
xvalues = [2, 9, 11, 18, 22, 28, 32, 31, 39, 33, 48, 52, 53, 68, 71, 77, 79, 82, 88, 92]
for b in xvalues:
    if b % 2 == 0:
        print('These values are even by nature')
    else:
        print('These values are odd by nature')
# end

# begin
# implementing while loop
x = 1
while x < 10000:
    print(x)
    x = x * 2
# end

# begin
# implementing for loop
dtray = [88.92, 92.43, 94.93, 96.23, 98.23, 100.23, 102.23, 104.23, 106.23, 108.23]
for b in dtray:
    if b > 100:
        print('The patient is down with high fever')
    elif b == 100:
        print('The patient is dealing with mild fever')
    else:
        print('The patient is hale and hearty!')
    # end

    # begin
    inx = 'string for indexing and slicing ops'
    print(inx[-1])
    print(inx[9])
    print(inx[0 : 7])
    # end

    # begin
    # writing function to compute the avg data size of files stored in gcs bucket
    def gcsavgsize(bucket_size, file_ct):
        return bucket_size / file_ct
    # calling the function with values
    avgsize = gcsavgsize(8388608, 190)
    print('Hey! The average object size for this google cloud bucket is:-', avgsize)
    # end

    # begin
    # this function will compute the average file size in megabytes
    def sizein_mb(gbsize, filect):
        return gbsize / filect
    # calling the function with values
    mbsize = sizein_mb(990208, 304)
    print('Hey!, The average size in MB for the objects stored in google cloud is:', mbsize)
    # end

    
