# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:36:52 2025

@author: adity
"""

# module for working with pandas
import pandas as pd
df = pd.read_csv('C:\\Users\\adity\\Desktop\\reservoir\\blinkit_customers.csv')
print(df)
# end

# 1
ren1 = df.rename(columns={'customer_id' : 'id'})
print(ren1)
# end

# 2
ren2 = df.rename(columns={'customer_name' : 'name'})
print(ren2)
# end

# 3
df = df.sort_values(by='customer_id', ascending=True)
print(df)
# end

# 4
df['tov'] = df['total_orders'] * df['avg_order_value']
print(df['tov'])
print(df)
# end

# 5
df['pincode'] = df['pincode'].astype('int')
print(df)
# end

