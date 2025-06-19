"""This script file works with Pandas, its various functions to read data, manipulate it, and 
finally write it to target data system or data store"""

# import libraries
import sys
import pandas as pd

df = pd.read_csv('C:\\Users\\adity\\Desktop\\sls.csv')
print(df.head())
print(df.tail())
print(sys.getsizeof(df))

dfshape = df.shape
print(dfshape)

desc = df.describe()
print(desc)

print(df.dtypes)

dfinfo = df.info()
print(dfinfo)

print(df.index)

print(df.isnull())
print(df.isna())

print(df['Category'].unique())

print(df.isnull().sum())
print(df.duplicated())
print(df.drop_duplicates())

print(df['Store ID'].nunique())


print(df['Region'].value_counts())
print(df.duplicated().sum())

print(df.memory_usage(deep=True))

print(df.head(n=5))

df_rename = df.rename(columns={'Store ID' : 'store', 'Product ID' : 'product'})
print(df_rename)

print(df.head(n=5))

purged_col = df.drop(columns=['Promotion', 'Epidemic'])
print(purged_col)

purged_field = df.drop(columns=['Weather Condition'])
print(purged_field)

print(df.columns)

print(df['Price'].unique())
print(df['Discount'].unique())

df['List Price'] = df['Price'] - df['Discount']
print(df['List Price'])

df['List Price'] = df['List Price'].astype('float32')
print(df['List Price'])


print(df.dtypes)

df['Discount'] = df['Discount'].astype('int32')
print(df['Discount'])

df['Competitor Pricing'] = df['Competitor Pricing'].astype('float32')
print(df.head(n=3))
print(df['Competitor Pricing'])

print(df.tail(n=4))

sorted_df = df.sort_values(by='List Price', ascending=True)
print(sorted_df)

df['Category'] = df['Category'].str.upper()
print(df['Category'])

df['Region'] = df['Region'].str.upper()
print(df['Region'])

df['Seasonality'] = df['Seasonality'].str.upper()
print(df['Seasonality'])


df['Category'] = df['Category'].str.lower()
print(df['Category'])

print(df.index)

def_value = df.fillna(value=100)
print(df.tail(n=2))


df['Category'] = df['Category'].apply(lambda x: x.upper())
print(df.head(n=3))


print(df[df['Demand'] > 100])

new_df = df.to_csv('C:\\Users\\adity\\Desktop\\mainframe\\bellpepper\\processed_sls.csv', header=True, index=False)
print(new_df)


"""This is the end of this script file"""

