# SHREE GANESHAY NAMAH

# code 01
string_df = 'samplestring'
print(string_df)
# end of code

# code 02
import pandas as pd
newdf = pd.read_csv('C:\\Users\\adity\\Desktop\\reservoir\\airbnb.csv')
print(newdf)
# end of code

# code 03
headf = newdf.head()
print(headf)
# end of code

# code 04
taildf = newdf.tail()
print(taildf)
# end of code

# code 05
shapedf = newdf.shape
print(shapedf)
# end of code

# code 06
dfinfo = newdf.info()
print(dfinfo)
# end of code

# code 07
dfdesc = newdf.describe()
print(dfdesc)
# end of code

# code 08
nvdf = newdf.isnull()
print(nvdf)
print(newdf)
# end of code

# code 09
dfna = newdf.dropna()
print(newdf)
# end of code

# code 10
dfill = newdf.fillna(value=100)
print(newdf)
# end of code