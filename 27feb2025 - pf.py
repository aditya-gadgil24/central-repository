# Revision session

# block 1
# data types - python

p_int = 1
p_float = 1.3
p_complex = 1 + 2j
p_str = "hey"
p_bool = True
p_bytes = b"hey"
p_bytearray = bytearray(10)
print(p_int, p_float, p_complex, p_str, p_bool, p_bytes, p_bytearray)
# end of code block 1

# block 2
# data structures - python
import pandas as pd
ds_list = [1, 2, 3, 4, 5]
ds_tuple = (6, 9, 2, 11, 32, 29)
ds_set = {1, 2, 3, 4, 5}
ds_dict = {"name": "Vishakha", "age": 36}
ds_array = [11, 6, 17, 22, 20, 29]
ds_dataframe = pd.DataFrame(ds_array)
ds_frozen_set = frozenset({1, 2, 3, 4, 5})
print(ds_list, ds_tuple, ds_set, ds_dict, ds_array, ds_dataframe, ds_frozen_set)
# end of code block 2

# block 3
# code 01
x = 'av'
y = 'ac'
w = x + y
print(w)
# end

# begin
# code 02
cgs = 2933452.23
sales = 8758303.17
fixed_costs = 129376.93
variable_costs = 1176352.58
profit = sales - (cgs + fixed_costs + variable_costs)
print('Hi, the profit for this month is', profit)
# end

# begin
# code 03
estate = 472275202
portions = 6
each_portion = estate / portions
print('The share of each of Godrej heir is:', each_portion)
# end

# begin
# code 04
principal = 2500000
tenure = 15
rate = 7.5
emi = principal * rate * (1 + rate) ** tenure / ((1 + rate) ** tenure - 1)
print('The EMI for the loan is:', emi)
# end

# begin
# code 05
m_salary = 112570
rule_y = 8
max_sanction = m_salary * rule_y
print('This customer can be sanctioned a maximum loan of:-', max_sanction)
# end

# begin
# code 06
stinng = 'this drink is awesome'
print(stinng[-1])
print(stinng[0:4])
print(stinng[5:])
print(stinng[:4])
# end

# begin
# code 07
str_01 = 'applyoperationsonthisstring'
print(str_01.capitalize())
print(str_01.casefold())
print(str_01[0:9])
print(str_01.count('i'))
print(str_01.endswith('g'))
# end

# begin
# code 08
app_stream = [173, 209, 260, 182, 199, 243, 222, 201, 198, 196]
print('The maximum score is:', max(app_stream))
print('The minimum score is:', min(app_stream))
print('The average score is:', sum(app_stream) / len(app_stream))
for values in app_stream:
    if values < 200:
        print('Disqualified from inclusion')
    elif values == 200:
        print('Borderline case')
    else:
        print('Qualified for model inclusion')
# end

# begin
# code 09
init_value = 10000
while init_value < 100000000:
    print(init_value)
    init_value = init_value * 1.25
# end

# begin
# code 10
for i in range(1, 110):
    print(i)
# end

# begin
# code 11
g = 23
if g % 2 != 0:
    print('The numer is not divisible by 2')
else:
    print('The number is divisible by 2')
# end

# begin
# code 12
a_package = 993750
metro_location = False
if a_package > 1000000 or metro_location:
    print('This alliance is eligible for further consideration')
else:
    print('This alliance is not eligible for further consideration')
# end

# begin
# code 13
user_age = 17
passport_status = True
if user_age > 18 or passport_status:
    print('This user can enter the club')
else:
    print('His entry to club shall be barred')
# end

# begin
# code 14
candidate_age = 36
tot_experience = 10
if candidate_age < 35 and tot_experience > 10:
    print('This candidate is eligible for the job')
else:
    print('This candidate shall be disqualified')
# end

# begin
# code 15
pune = 134.23
bangalore = 168.94
hyderabad = 145.29
mumbai = 173.57
chennai = 156.14
gurgaon = 152.04
noida = 149.31
cities = (pune, bangalore, hyderabad, mumbai, chennai, gurgaon, noida)
for cli in cities:
    if cli < 150:
        print('This city is affordable')
    elif cli == 150:
        print('This city is borderline affordable')
    else:
        print('This city is expensive')
# end

# begin
# code 16
def ratings(r, n):
    return r / n
# calling the function with arguments
crating = ratings(269640, 64200)
print('The rating of the product on Amazon is-', crating)
# end

# begin
# code 17
import statistics as st
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('The mean of the data is:', st.mean(data))
print('The median of the data is:', st.median(data))
print('The mode of the data is:', st.mode(data))    # mode is not available in the data
print('The variance of the data is:', st.variance(data))
print('The standard deviation of the data is:', st.stdev(data))   # standard deviation  is not available in the data
# end

# begin
import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
print('The sum of the arrays is:', np.add(array1, array2))
print('The difference of the arrays is:', np.subtract(array1, array2))
print('The product of the arrays is:', np.multiply(array1, array2))
print('The division of the arrays is:', np.divide(array1, array2))
combined_array = np.concatenate((array1, array2))
print('The combined array is:', combined_array)
total_mean = np.mean(combined_array)
print('The combined mean of the two arrays is:-', total_mean)
# end
