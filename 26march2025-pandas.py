# Shree

# Working with numpy arrays
import numpy as np
np_full = np.full((10, 3), 11)
print(np_full)
# end

array_1 = np.ones((20, 7), dtype=int)
print(array_1)
# end

array_3 = np.zeros((10, 5), dtype=float)
print(array_3)
# end

rnge_a = np.arange(0, 50, 2)
print(rnge_a)
# end

linarr = np.linspace(1, 500, 100)
print(linarr)
# end

full_arr = np.full((2, 3), 7)
print(f"\nFull array:\n{full_arr}")
# end

sq_set = {x * x for x in range(50)}
print(sq_set)
# end

np_f = np.array([-1.3, 2.7, 3.9, -5.2])
abs_v = np.floor(np_f)
print(abs_v)

arr = np.arange(1, 21)
newarr = arr.reshape((5, 4))
print(newarr)
# end

d2_arr = np.array([[8, 5, 3], [9, 6, 4]])
print(d2_arr)
flat_arr = d2_arr.flatten()
print(flat_arr)
trans_arr = d2_arr.transpose()
print()
