# SCRIPT TO WORK WITH PARQUET DATA FORMAT

# IMPORT DASK, PYARROW OR FASTPARQUET FOR WORKING WITH PARQUET FORMATS

# code block
# Importing necessary libraries
import pandas as pd
import pyarrow.parquet as pq
import dask.dataframe as dd
df = pd.read_parquet('C:\\Users\\adity\\Desktop\\flights.parquet', engine='pyarrow')
print(df)
# Print first few rows
print(df.head())
# Print last few rows
print(df.tail())

# Print the information about column data types and names
print(df.describe())
# Print statistical information of numeric columns
print(df.info())
df = df.rename(columns = {'FL_DATE' : 'flight_date', 'AIR_TIME' : 'airtime'})
print(df.head())
df = df.rename(columns={'DEP_DELAY' : 'departure_delay', 'ARR_DELAY' : 'arrival_delay', 'DISTANCE' : 'distance'})
print(df.head())
df = df.rename(columns={'DEP_TIME' : 'departure_time', 'ARR_TIME' : 'arrival_time'})
print(df.head())
df['travel_time'] = df['arrival_time'] - df['departure_time']
print(df['travel_time'])
df['speed'] = df['distance'] / df['airtime']
print(df['speed'])
df = df.drop(columns=['departure_delay', 'arrival_delay'])
print(df.head())
df['mean_airtime'] = df['departure_time'] + df['arrival_time'] + df['travel_time'] / 3
print(df['mean_airtime'])
print(df.info())
dfs = df.shape
print(dfs)
df['air_cost'] = df['airtime'] * df['distance']
print(df['air_cost'])

# Writing the processed data to a new parquet file
newdf = df.to_parquet('C:\\Users\\adity\\Desktop\\transformed_data.parquet', engine='pyarrow', compression='snappy')
print(newdf)
# End of script
# Code block ends


