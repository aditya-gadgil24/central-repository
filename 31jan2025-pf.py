# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:46:03 2025

@author: adity
"""

#  SHREE GANESHAY NAMAH

# Module for numpy module functions, practice

# code01
import numpy as np
arry1 = np.array([33, 47, 59, 67])
arry2 = np.array([27, 39, 49, 53])
# addition
compute1 = np.add(arry1, arry2)
print(compute1)
# end of code

# subtraction
compute2 = np.subtract(arry1, arry2)
print(compute2)
# end of code

# division
compute3 = np.divide(arry1, arry2)
print(compute3)
# end of code

# multiply
compute4 = np.multiply(arry1, arry2)
print(compute4)
# end of code

# average or mean

compute5 = np.mean(arry1)
print(compute5)
# end of code

# median 
compute6 = np.median(arry1)
print(compute6)
# end of code

# modular operation
compute7 = np.mod(arry1, arry2)
print(compute7)
# end of code


# printing the shape and dtype of array
print(arry1.shape, arry1.dtype)
# end of code

# addition of arrays
sarry = arry1 + arry2
print(sarry)
# end of code


# new code
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]], order='F')  
# Column-major (Fortran-order)

print(arr.flags)  
# Shows memory layout
# end of the code block



# new code

array_data = np.array([[13, 15, 14, 22], [25, 49, 81, 121]], order='F')
print(array_data.flags)
# Print to screen for user
# End of code


# adding two matrices with different dimensions
matrix_1 = np.array([[17, 21, 23, 27, 29], [11, 13, 19, 25, 31]])
matrix_2 = np.array([10, 20, 31, 41, 50])
matsum = matrix_1 + matrix_2
print(matsum)
# Print to screen for user
# End of code


# code for memory usage of different dtypes
arr_32 = np.arange(1000000, dtype=np.int32)
arr_64 = np.arange(1000000, dtype=np.int64)

print(arr_32.nbytes, arr_64.nbytes)  
# int32 uses less memory


# filtering data with numpy arrays

array_brit = np.array([2, 9, 11, 17, 23, 29, 31, 37])
fltrdta = array_brit[array_brit > 20]
print(fltrdta)


# custom data types for memory efficiency 
arr_77 = np.array([35, 31, 49, 41, 99], dtype=np.int8)
print(arr_77.nbytes)
# print to screen