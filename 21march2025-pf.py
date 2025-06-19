# SHREE

# simple data processing pipeline for local files
# 1. read data from local file
# 2. process data
# 3. write data to local file

# import libraries
import pandas as pd
import numpy as np
string1 = 'this is the latest stable version of python i installed today'
print(string1)
# end

# begin
x_value = 9.8
metro_loc = True
if x_value > 10 or metro_loc:
    print('The prospect meets one of the conditions')
else:
    print('The prospect does not meet any condition')
# end

# begin
xball = [3, 7, 9, 11, 13, 14, 17, 19, 28]
for x in xball:
    if x % 2 != 0:
        print(x, 'is an odd number')
    else:
        print('exit the loop')
# end