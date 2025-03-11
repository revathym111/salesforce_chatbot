import os #used to access environment variables for storing sensitive credentials securely
from simple_salesforce import Salesforce # python library that allows interaction with Salesforce API
from dotenv import load_dotenv # loads environment variables from .env file, so no hardcode credentials in the script

load_dotenv() #reads and loads key-value pairs from .env file into environment variables, secure credentials remain private

#define function to connect to salesforce
def connect_to_salesforce():
    try:
        sf = Salesforce(
            username=os.getenv("SALESFORCE_USERNAME"),
            password=os.getenv("SALESFORCE_PASSWORD"),
            security_token=os.getenv("SALESFORCE_SECURITY_TOKEN"),
            domain="login"
        )
        print("Salesforce connection successful.")
        return sf
    except Exception as e:
        print(f"Failed to connect to Salesforce: {e}")
        return None # return None if connection fails

def get_customer_data(email):
    sf = connect_to_salesforce()
    if sf is None:
        print("Error: Could not connect to Salesforce")
        return None
    
    query = f"SELECT Id, Name, Email FROM Contact WHERE Email = '{email}'"
    result = sf.query(query)
    return result['records'][0] if result['records'] else None # return all matching records else none





