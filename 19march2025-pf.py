# SHREE

# PROGRAM FOR DATA READINGS FROM THE FILE, PROCESSING AND WRITING TO THE FILE


# begin
# importing the required libraries
# READING THE DATA FROM LOCAL FILE SYSTEM
import pandas as pd
df = pd.read_csv('C:\\Users\\adity\\Desktop\\orders_aggregate.csv')
print(df)
# end



# begin
# INSPECTING AND VIEWING THE DATA
shape = df.shape
print(shape)
head = df.head()
print(head)
tail = df.tail()
print(tail)
info = df.info()
print(info)
describe = df.describe()
print(describe)
# end



# begin
# CLEANING AND VALIDATING THE DATA
null = df.isnull()
print(null)
fill = df.fillna(value=0)
print(fill)
drop = df.dropna()
print(drop)
duplicate = df.duplicated()
print(duplicate)
drop_duplicate = df.drop_duplicates()
print(drop_duplicate)
# end




# begin
# DATA PROCESSING, MANIPULATION AND TRANSFORMATION
df['total_amt'] = df['order_amt'] + df['taxes']
print(df['total_amt'])
df['payable_amt'] = df['total_amt'] - df['discount']
print(df['payable_amt'])
df['customer_type'] = df['customer_type'].str.upper()
print(df['customer_type'])
df = df.drop(columns=['taxes', 'discount'])
print(df)
df = df.rename(columns={'customer_type' : 'type', 'order_amt' : 'total'})
print(df)
df['payable_amt'] = df['payable_amt'].astype('Int64')
print(df)
df['total_amt'] = df['total_amt'].astype('Int32')
print(df)
total_mean = sum(df['total']) / len(df['total'])
print('The mean value of orders for the month is:', total_mean)
# end




# begin
# WRITING THE PROCESSED DATA TO AN OUTPUT FILE IN LOCAL FILE SYSTEM
df.to_parquet('C:\\Users\\adity\\Desktop\\orders_aggregate.parquet')
# end

# The program runs successfully and the output is verified.
# end of the program