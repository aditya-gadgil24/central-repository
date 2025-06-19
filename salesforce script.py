# script to pull data from salesforce to a python file

import os
from simple_salesforce import Salesforce
from datetime import datetime

# --- Configuration ---
SALESFORCE_USERNAME = "contact-ydcj@force.com"
SALESFORCE_PASSWORD = "Bigtable595488$"
SALESFORCE_SECURITY_TOKEN = "j5r7giE7dHRbpZc1ewFKw7VVW"  # Required if IP restricted

TABLES_TO_PULL = ["Account", "Contact", "Opportunity"]
OUTPUT_FILE_PREFIX = "salesforce_data_"
OUTPUT_DIRECTORY = "C:\\salesforce_data"  # Adjust as needed

# --- Salesforce Connection ---
try:
    sf = Salesforce(username=SALESFORCE_USERNAME, password=SALESFORCE_PASSWORD, security_token=SALESFORCE_SECURITY_TOKEN)
    print(f"{datetime.now()} - Successfully connected to Salesforce.")
except Exception as e:
    print(f"{datetime.now()} - Error connecting to Salesforce: {e}")
    exit(1)

# --- Create Output Directory if it doesn't exist ---
if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

# --- Function to Pull Data from a Table ---
    sf_pull_salesforce_data(table_name):
    print(f"{datetime.now()} - Starting data pull for table: {table_name}")
    try:
        query = f"SELECT * FROM {table_name}"
        result = sf.query_all(query)
        records = result['records']
        print(f"{datetime.now()} - Successfully pulled {len(records)} records for table: {table_name}")
        return records
    except Exception as e:
        print(f"{datetime.now()} - Error pulling data for table {table_name}: {e}")
        return None

# --- Main Execution ---
if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for table in TABLES_TO_PULL:
        data = pull_salesforce_data(table)
        if data:
            output_filename = os.path.join(OUTPUT_DIRECTORY, f"{OUTPUT_FILE_PREFIX}{table}_{timestamp}.txt")
            try:
                with open(output_filename, 'w') as f:
                    if data:
                        header_written = False
                        for row in data:
                            if not header_written:
                                f.write(','.join(row.keys()) + '\n')
                                header_written = True
                            # Remove the 'attributes' key which is specific to Salesforce API
                            row_values = {k: v for k, v in row.items() if k != 'attributes'}
                            f.write(','.join(map(str, row_values.values())) + '\n')
                print(f"{datetime.now()} - Data for {table} saved to: {output_filename}")
            except Exception as e:
                print(f"{datetime.now()} - Error saving data for {table}: {e}")

    print(f"{datetime.now()} - Data pull and save process completed.")