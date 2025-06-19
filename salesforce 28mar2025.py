# this script will work with salesforce app data

# script start
import os
from simple_salesforce import Salesforce

sf_username = os.environ.get('SF_USERNAME')
sf_password = os.environ.get('SF_PASSWORD')
sf_security_token = os.environ.get('SF_SECURITY_TOKEN')

if sf_username and sf_password and sf_security_token:
    try:
        sf = Salesforce(username=sf_username,
                        password=sf_password,
                        security_token=sf_security_token)
        print("Successfully connected to Salesforce!")
        # Now you can perform your basic Salesforce operations using the 'sf' object
        # Example:
        # results = sf.query("SELECT Id, Name FROM Account LIMIT 5")
        # print(results)
    except Exception as e:
        print(f"Error connecting to Salesforce: {e}")
else:
    print("Salesforce credentials not found in environment variables.")
# end of code block


# script for autom