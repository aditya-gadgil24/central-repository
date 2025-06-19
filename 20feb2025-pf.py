# module for pandas dataframes functions

# begin
import pandas as pd # type: ignore
df = pd.read_csv('C:\\Users\\adity\\Desktop\\reservoir\\car.csv')
print(df)
# end

# 2
df['brand'] = df['brand'].str.upper()
print(df['brand'])
# end

# 3
df['model'] = df['model'].str.upper()
print(df['model'])
# end

# 4
df['model'] = df['model'].str.lower()
print(df['model'])
# end

# 5
df['transmission'] = df['transmission'].str.upper()
print(df['transmission'])
# end

# 6
df['model'] = df['model'].str.strip()
print(df['model'])
# end

# 7
df['brand'] = df['brand'].str.contains('Golf')
print(df['brand'])
# end

# 8
df['transmission'] = df['transmission'].str.split(',')
print(df['transmission'])
# end

# 9
df1 = pd.DataFrame({'metal' : 'gold', 'price' : 90000}, {'metal' : 'silver', 'price' : 40000})
df2 = pd.DataFrame({'model' : 'chain', 'metal' : 'gold'}, {'model' : 'bracelet', 'metal' : 'silver'})
print(df1)
print(df2)
# end
dfcon = pd.concat([df1, df2])
print(dfcon)
# end
dfmrge = pd.merge(df1, df2, on='metal', how='inner')
print(dfmrge)


# new code

df01 = pd.DataFrame({'pcode': [101, 103, 109, 110, 104, 105], 'make': ['sony', 'aiwa', 'samsung', 'lg', 'haier', 'bosch']})
df02 = pd.DataFrame({'cname' : ['gill', 'mike', 'bob', 'sam', 'stubbs', 'punter'], 'mcode': [101, 105, 105, 105, 103, 109]})
dfcte = pd.concat([df01, df02])
print(dfcte)
# end
dfmrge = pd.merge(df01, df02, left_on='pcode', right_on='mcode', how='inner')
print(dfmrge)

# end of code


# new module - dat