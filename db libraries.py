# SHREE

# code block
import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('C:\\Users\\adity\\Desktop\\toffee.csv')
print(df)
# Reads data from csv into pandas dataframe 

# Configuring connection_parameters
DB_TYPE = 'postgresql'
DB_USERNAME = 'postgres'
DB_PASSWORD = 'Bigtable24$'
DB_NAME = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Creating connection string
engine = create_engine(f'{'postgresql'}//{'postgresql'}:{'Bigtable24$'}@{'localhost'}:{'5432'}/{'postgres'}')
new_file = popeye_table
df.to_sql('popeye_table', engine, index=False)
# end of code