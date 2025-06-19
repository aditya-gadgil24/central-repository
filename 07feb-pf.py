# SHREE GANESHAY NAMAH

# code 01
import pandas as pd
df = pd.read_excel('C:\\Users\\adity\\Desktop\\reservoir\\globant.xlsx')
print(df)
# end of code

# code 02
ops1 = df.drop('holiday', axis=1, inplace=True)
print(ops1)
print(df)
# end of code

# code 03
ops2 = df.drop('school', axis=1, inplace=True)
print(ops2)
print(df)
# end of code

# code 03
ops4 = df.shape
print(ops4)
# end of code

# code 04
ops5 = df.info()
print(ops5)
# end of code

# code 05
ops6 = df.describe()
print(ops6)
# end of code

# code 06
ops11 = df.head()
print(ops11)
# end of code

# code 07
ops13 = df.tail()
print(ops13)
# end of code

# ***********************************************