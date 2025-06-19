"""script for purging gmail account emails"""

# Import required libraries
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the permission scope (needed to modify Gmail)
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    # Starts the OAuth flow using credentials.json
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)  # Opens a browser for Google login
    service = build('gmail', 'v1', credentials=creds)  # Creates the Gmail API service object
    return service

def delete_unstarred_emails(service):
    # Search for unstarred emails
    query = '-is:starred'
    results = service.users().messages().list(userId='me', q=query, maxResults=500).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No unstarred emails found.")
        return
    
    for msg in messages:
        msg_id = msg['id']
        service.users().messages().delete(userId='me', id=msg_id).execute()
        print(f"Deleted email ID: {msg_id}")

        print(f"Deleted {len(messages)} unstarred emails in this batch.")
    
if __name__ == '__main__':
    gmail_service = authenticate_gmail()
    delete_unstarred_emails(gmail_service)


# Get emails except starred
results = service.users().messages().list(userId='me', q='-is:starred').execute()
messages = results.get('messages', [])

for msg in messages:
    msg_id = msg['id']
    service.users().messages().delete(userId='me', id=msg_id).execute()
    print(f"Deleted email with ID: {msg_id}")


print("Authentication successful.")

results = service.users().messages().list(userId='me', q='-is:starred').execute()
messages = results.get('messages', [])

print(f"Found {len(messages)} emails to delete.")

for msg in messages:
    msg_id = msg['id']
    service.users().messages().delete(userId='me', id=msg_id).execute()
    print(f"Deleted email with ID: {msg_id}")


"""This script executes the complete end to end workflow of authenticating and accessing the google account, executing the logic
of purging emails based on the filter, printing the status and output of the script, finally terminating once the task is done"""