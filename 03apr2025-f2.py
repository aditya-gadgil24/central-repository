# SCRIPT FOR READING CSV/PARQUET FILE FROM GCS BUCKET, PROCESSING, WRITING BACK TO GCS BUCKET

# SCRIPT CODE BLOCK
import os
import io
import google.cloud.storage
import pandas as pd

# --Main execution--#
input_bucket_name = 'vfbusinessdata'
input_blob_name = 'csv files/mock_data.csv'
output_bucket_name = 'vfbusinessdata'
output_blob_name = 'csv files/dump_data.csv'

# Read from GCS
storage_client = google.cloud.storage.Client()
input_bucket_name = storage_client.bucket('vfbusinessdata')
input_blob = input_bucket_name.blob('csv files/mock_data.csv')
file_content = input_blob.download_as_bytes()
df = pd.read_csv(io.BytesIO(file_content))
print(df)
print(df.head())
# End of code block

# TRANSFORMATIONS ON THE DATA
df['first_name'] = df['first_name'].str.upper()
print(df['first_name'])

df['last_name'] = df['last_name'].str.upper()
print(df['last_name'])
print(df.head())

df = df.drop(columns=['ip_address'])
print(df.head())

df['email'] = df['email'].str.strip()
print(df['email'])

df['gender'] = df['gender'].str.upper()
print(df['gender'])

df = df.rename(columns={'email' : 'email_id', 'id' : 'serial_id'})
print(df.head())

df = df.rename(columns={'gender' : 'sex'})
print(df.tail())

df['sex'] = df['sex'].str.lower()
print(df['sex'])
# End of data transformation logic

# 3. Write back to GCS
output_bucket_name = storage_client.bucket('vfbusinessdata')
output_blob = output_bucket_name.blob('csv files/dump_data.csv')
buffer = io.StringIO()
df.to_csv(buffer, index=False)
output_blob.upload_from_string(buffer.getvalue(), content_type="application/octet-stream")

print("\nProcess complete.")
# End of script
# Exit
"""Simple script to read data from GCS bucket, process, write back to GCS bucket blob object"""

