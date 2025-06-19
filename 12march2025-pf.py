# PANDAS LIBRARY FUNCTIONS

# code block 
# data inspection and viewing
import pandas as pd
df = pd.read_excel('C:\\Users\\adity\\Desktop\\sales.xlsx')
print(df)
# reading data from local file directory

dfhead = df.head()
print(dfhead)
# prints the first 5 records of dataframe

dftail = df.tail()
print(dftail)
# prints the last 5 records of dataframe

shapedf = df.shape
print(shapedf)
# prints the shape of the dataframe

dfinfo = df.info()
print(dfinfo)
# prints the information about the statistics of numeric fields

dfdesc = df.describe()
print(dfdesc)
# prints information about the statistical summary of dataframe


# code block
# data cleaning

null_values = df.isnull()
print(null_values)
# prints null values in dataframe

fill_na = df.fillna(value=0)
print(fill_na)
# fills na fields with 0

drop_na = df.dropna()
print(drop_na)
# drops records with na values

duplicate = df.duplicated()
print(duplicate)
# prints duplicate records

drop_duplicate = df.drop_duplicates()
print(drop_duplicate)
# drops all duplicate records


df['Total Business'] = df['Amount'] * df['Boxes Shipped']
print(df['Total Business'])
# creates new field by computing product of two fields

df = df.drop(columns='Date', axis=1)
print(df)
# drops a column from dataframe

df = df.rename(columns={'Sales Person' : 'Employee', 'Boxes Shipped' : 'Boxes'})
print(df)
# renames the field of dataframe

df['Country'] = df['Country'].str.upper()
print(df['Country'])
# changes field case from lower to upper

df['Product'] = df['Product'].str.upper()
print(df['Product'])
# changes field case from lower to upper

df['Product'] = df['Product'].str.strip()
print(df['Product'])
# clears the leading and trailing whitespaces in a character string

df['Product'] = df['Product'].str.lower()
print(df['Product'])
# changes case from upper to lowercase

highest_sale = max(df['Total Business'])
print('The highest sale for the month is:', highest_sale)
# prints the highest sale for month

lowest_sale = min(df['Total Business'])
print('The lowest sale for the month is:-', lowest_sale)
# prints the lowest sale for month

average_sale = sum(df['Total Business']) / len(df['Total Business'])
print('The average sales done by sales personnel this month was:', average_sale)
# prints the average sales by sales staff for the month

total_sales = sum(df['Total Business'])
print('Hi, the total sales for the month is:', total_sales)
# prints total sales for the month

newdf1 = df.to_excel('C:\\Users\\adity\\Desktop\\newoutput.xlsx', index=False)
print(newdf1)
# writes processed data to new file on local directory





# code block

# operations to move the new data file to postgresql db, google cloud storage

from sqlalchemy import create_engine

# Define PostgreSQL connection parameters
DATABASE_TYPE = "postgresql"
DB_USERNAME = "postgres"
DB_PASSWORD = "Bigtable24$"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

# Create the connection string
engine = create_engine(f"{'postgresql'}://{'postgres'}:{'Bigtable24$'}@{'localhost'}:{'5432'}/{'postgres'}")

