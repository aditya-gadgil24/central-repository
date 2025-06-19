# SHREE 

# Moving data files from source to sink, use cases

# code block
import pandas as pd
df = pd.read_excel('C:\\Users\\adity\Desktop\\newoutput.xlsx')
print(df)
# reads data from file on local file system

# configuring connection to postgresql db
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
table_name = 'chocolate_table'
df.to_sql('chocolate_table', con=engine, if_exists="replace", index=False)
# writes data from xlsx file to table in postgresql database
# end of code block



# new code block 
# program to read data from postgresql table into python environment
import pandas as pd
import psycopg2


# Define PostgreSQL connection parameters
DATABASE_TYPE = "postgresql"
DB_USERNAME = "postgres"
DB_PASSWORD = "Bigtable24$"
DB_HOST = "localhost" 
DB_PORT = "5432"
DB_NAME = "postgres"

# Establish connection
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Bigtable24$",
    port='5432'
)

# Read data into pandas DataFrame
query = "SELECT * FROM chocolate_table;"
df = pd.read_sql("SELECT * FROM chocolate_table;", conn)
print(df)
# end of code block