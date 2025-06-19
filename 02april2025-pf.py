# script for reading data from parquet file, and writing it to postgresql database table

# begin
import pandas as pd
df = pd.read_parquet('C:\\Users\\adity\\eds.parquet')
print(df)



