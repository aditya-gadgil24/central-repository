# SHREE

# Working with NumPy library functions
# begin
import numpy as np
ds1 = np.array([1, 3, 5, 7, 9])
ds2 = np.array([11, 13, 15, 17, 19])
transpose_ds = np.transpose(ds1)
print(transpose_ds)    
new_array = np.concatenate((ds1, ds2))
print(new_array)
transpose_ds1 = np.transpose(new_array)
print(transpose_ds1)
# end

vstack_ds = np.hstack(new_array)
print(vstack_ds)
hstack_ds = np.hstack(new_array)
print(hstack_ds)
# end
uniq_ds = np.unique(new_array)
print(uniq_ds)
ds_sum = np.sum(new_array)
print(ds_sum)
ds_mean = np.mean(new_array)
print(ds_mean)
ds_med = np.median(new_array)
print(ds_med)
ds_std = np.std(new_array)
print(ds_std)
max_ds = np.max(new_array)
print(max_ds)
min_ds = np.min(new_array)
print(min_ds)
end = 'This is the end of this part of the exercise.'
print(end)
# end of code block 

# begin
spaced_array = np.arange(1, 1000, 2)
print(spaced_array)
lin_array = np.linspace(100, 10000, 50)
print(lin_array)
# end code

# begin
uniq_ele = np.unique(spaced_array)
print(uniq_ele)
# end 

# begin
array_x = np.array([29, 41, 52, 58, 63, 67, 73, 79, 82, 89, 93, 95, 99])
filtered_elements = np.where(array_x > 59)
print(filtered_elements)
# end